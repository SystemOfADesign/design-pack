#!/usr/bin/env python3
"""Resolve design-pack specialists at runtime.

  skills.py find <name> [<name>...]   how to use each skill right now: "invoke <x>" or "read <abs SKILL.md>"
  skills.py list [--layer L] [--mode M] [--installed]
  skills.py phase <phase>              playbook entries for a builder phase / audit pass, resolved
  skills.py root                       print the design-pack root this script resolved

Resolution order for a name: installed in ~/.claude/skills -> installed plugin cache ->
vendored sibling skills/<name>/SKILL.md -> catalog path under the pack root (clone-only, read by path).
"user-only" = installed but frontmatter has disable-model-invocation: true, so the model cannot call it
with the Skill tool; ask the user to run /name, or read its SKILL.md and follow it yourself.
Never guesses: a name that resolves nowhere prints "missing" and exits 1.
"""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent            # .../skills/design-director/scripts
SKILL = HERE.parent                                # .../skills/design-director
PACK = SKILL.parent.parent                         # .../design-pack  (or plugin root when vendored)
HOME = Path.home()
CATALOG = SKILL / 'reference' / 'catalog.json'
PLAYBOOK = SKILL / 'reference' / 'playbook.md'

def fm(path):
    """(name, user_only) from frontmatter. user_only = disable-model-invocation: true (only the user can /invoke it)."""
    t = path.read_text(errors='replace')
    m = re.match(r'^---\n(.*?)\n---', t, re.S)
    name, user_only = path.parent.name, False
    if m:
        for line in m.group(1).splitlines():
            if line.startswith('name:'): name = line[5:].strip().strip('"\'')
            if re.match(r'^disable-model-invocation:\s*true', line): user_only = True
    return name, user_only

def fm_name(path): return fm(path)[0]

def installed_index():
    """name -> (invoke string, path) for everything invocable in this Claude Code install."""
    idx = {}
    local = HOME / '.claude' / 'skills'
    if local.exists():
        for d in sorted(local.iterdir()):
            f = d / 'SKILL.md'
            if f.exists():
                n, uo = fm(f); idx[n] = (f"/{n}", f, uo)
    cache = HOME / '.claude' / 'plugins' / 'cache'
    if cache.exists():
        for f in cache.glob('*/*/*/skills/*/SKILL.md'):
            n, uo = fm(f); plugin = f.parts[f.parts.index('cache') + 2]
            idx.setdefault(n, (f"{plugin}:{n}", f, uo))
    return idx

def load_catalog():
    if not CATALOG.exists():
        sys.exit(f"missing {CATALOG}; run research/build-skills-grid.py")
    return {s['name']: s for s in json.loads(CATALOG.read_text())['skills']}

def resolve(name, cat, inst):
    if name in inst:
        inv, path, user_only = inst[name]
        if user_only:
            return {'name': name, 'how': 'user-only', 'target': inv, 'path': str(path)}
        return {'name': name, 'how': 'invoke', 'target': inv, 'path': str(path)}
    sib = PACK / 'skills' / name / 'SKILL.md'
    if sib.exists():
        return {'name': name, 'how': 'read', 'target': str(sib), 'path': str(sib)}
    e = cat.get(name)
    if e:
        for rel in e['paths']:
            p = Path(rel) if rel.startswith('/') else PACK / rel
            if p.exists():
                return {'name': name, 'how': 'read', 'target': str(p), 'path': str(p)}
    return {'name': name, 'how': 'missing', 'target': None, 'path': None}

def fmt(r, cat):
    e = cat.get(r['name'], {})
    tag = f"[{e.get('layer','?')} / {e.get('mode','?')}]"
    if r['how'] == 'invoke': return f"{r['name']:28} invoke {r['target']:40} {tag}"
    if r['how'] == 'read':   return f"{r['name']:28} read   {r['target']} {tag}"
    if r['how'] == 'user-only': return f"{r['name']:28} user-only {r['target']} (model cannot invoke; ask the user to run it, or read {r['path']}) {tag}"
    return f"{r['name']:28} MISSING (not installed, no clone found) {tag}"

def main(argv):
    if not argv or argv[0] in ('-h', '--help'): print(__doc__); return 0
    cmd, args = argv[0], argv[1:]
    cat = load_catalog(); inst = installed_index(); as_json = '--json' in args; args = [a for a in args if a != '--json']
    if cmd == 'root': print(PACK); return 0
    if cmd == 'find':
        rs = [resolve(n, cat, inst) for n in args]
        print(json.dumps(rs, indent=1)) if as_json else print("\n".join(fmt(r, cat) for r in rs))
        return 1 if any(r['how'] == 'missing' for r in rs) else 0
    if cmd == 'list':
        layer = mode = None; only_inst = False
        it = iter(args)
        for a in it:
            if a == '--layer': layer = next(it)
            elif a == '--mode': mode = next(it)
            elif a == '--installed': only_inst = True
        rows = []
        for n, e in sorted(cat.items()):
            if layer and layer.lower() not in e['layer'].lower(): continue
            if mode and mode.lower() not in e['mode'].lower(): continue
            r = resolve(n, cat, inst)
            if only_inst and r['how'] != 'invoke': continue
            rows.append((r, e))
        if as_json: print(json.dumps([dict(r, layer=e['layer'], mode=e['mode'], description=e['description']) for r, e in rows], indent=1))
        else:
            for r, e in rows: print(fmt(r, cat) + f"  {e['description'][:90]}")
        return 0
    if cmd == 'phase':
        if not args: sys.exit('phase <name>')
        want = args[0].lower(); txt = PLAYBOOK.read_text(); out = []
        for sec in re.split(r'\n(?=### )', txt):
            head = sec.splitlines()[0] if sec else ''
            if head.startswith('### ') and want in head.lower():
                names = re.findall(r'`([a-z0-9-]+)`', sec)
                seen = []
                for n in names:
                    if n in cat and n not in seen: seen.append(n)
                out.append(head)
                out += ["  " + fmt(resolve(n, cat, inst), cat) for n in seen]
        print("\n".join(out) if out else f"no playbook section matches '{want}'"); return 0 if out else 1
    sys.exit(f"unknown command {cmd}; see --help")

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
