#!/usr/bin/env python3
"""Regenerate design-pack/SKILLS.md (layer x mode grid) and skills/design-director/reference/catalog.json
(machine-readable catalog used by design-director / design-builder to resolve specialists)."""
import json
import re, sys
from pathlib import Path
H = Path.home()
PACK = Path(__file__).resolve().parent.parent
ROOT = PACK/'repos'
CLONED = ['emilkowalski_skills','ibelick_ui-skills','vercel-labs_agent-skills','nextlevelbuilder_ui-ux-pro-max-skill',
 'wondelai_skills','plugin87_ux-ui-agent-skills','LottieFiles_motion-design-skill','kylezantos_design-motion-principles',
 'Jakubantalik_transitions.dev','Dammyjay93_interface-design','dominikmartn_nothing-design-skill','yangyue1974_rams-braun-ui',
 'fatihaydost_brand-identity-skill','anthropics_skills','vercel_ai-elements','VoltAgent_awesome-design-md','benjitaylor_skills']
INSTALLED_DIRS = {
 'local ~/.claude/skills': H/'.claude/skills',
 'plugin impeccable': H/'.claude/plugins/cache/impeccable',
 'plugin taste-skill': H/'.claude/plugins/cache/taste-skill',
 'plugin frontend-design': H/'.claude/plugins/cache/claude-plugins-official/frontend-design',
 'plugin figma': H/'.claude/plugins/cache/claude-plugins-official/figma',
 'plugin design (knowledge-work)': H/'.claude/plugins/cache/knowledge-work-plugins/design',
}
BUILTIN = {'canvas-design','docx','pdf','pptx','xlsx','skill-creator','internal-comms','frontend-design','claude-api','doc-coauthoring'}
LAYERS = ['Philosophy/taste','Product/why','Brand/identity','Tokens/system','Components/API','Motion','Screens/pages','AI-specific UX','Cross-cutting (a11y, copy, perf)']
MODES  = ['Doctrine','Generate','Audit/review','Fix','Gate/pipeline','Reference']
P,PR,B,T,C,M,S,AI,X = LAYERS
D,G,A,F,GT,R = MODES
TAG = {
 'emil-design-eng':(P,D),'apple-design':(P,D),'rams-braun-ui':(P,D),'nothing-design':(P,D),'design-everyday-things':(P,D),'37signals-way':(P,D),
 'ios-hig-design':(P,D),'design-doctrine':(P,D),'design-taste-frontend':(P,D),'impeccable':(P,D),'taste-skill':(P,D),'design-consultation':(P,R),
 'top-design':(P,R),'steve-jobs-design-review':(P,A),
 'jobs-to-be-done':(PR,D),'lean-ux':(PR,D),'continuous-discovery':(PR,G),'mom-test':(PR,D),'hooked-ux':(PR,D),'design-sprint':(PR,G),'grill-me':(PR,A),
 'user-research':(PR,G),'research-synthesis':(PR,G),'design-brief':(PR,G),'office-hours':(PR,R),
 'brand-identity':(B,G),'brand':(B,D),'brandkit':(B,G),'brand-guidelines':(B,D),'theme-factory':(B,G),'apply-aesthetic':(B,G),'banner-design':(B,G),'design':(B,G),
 'design-tokens':(T,G),'token-build':(T,GT),'design-system':(T,G),'migrate-design-system':(T,F),'governance':(T,D),'create-design-md':(T,G),
 'figma-integration':(T,GT),'awesome-design-md':(T,R),'figma-generate-library':(T,G),'figma-spec':(T,R),'figma-use':(T,R),'web-typography':(T,D),
 'design-component':(C,G),'design-code':(C,G),'ui-styling':(C,G),'pick-ui-library':(C,R),'ask-sonner':(C,R),'component-canvas':(C,A),
 'vercel-composition-patterns':(C,D),'break-ui':(C,A),'shadcn':(C,R),'figma-design-to-code':(C,G),'figma-swiftui':(C,G),
 'animate':(M,G),'animate-expo':(M,G),'improve-animations':(M,A),'review-animations':(M,A),'remove-animations':(M,F),'animation-performance':(M,D),
 'animation-vocabulary':(M,R),'find-animation-opportunities':(M,A),'fixing-motion-performance':(M,F),'transitions-agent':(M,F),'transitions-dev':(M,R),
 'transitions-polish':(M,F),'refine-live':(M,F),'design-motion-principles':(M,D),'motion-design':(M,D),'vercel-react-view-transitions':(M,G),
 'microinteractions':(M,D),'figma-implement-motion':(M,G),'figma-use-motion':(M,R),
 'design-screen':(S,G),'redesign':(S,F),'data-dashboard':(S,G),'interface-design':(S,D),'frontend-design':(S,D),'ui-ux-pro-max':(S,R),'prototype':(S,G),
 'image-to-code':(S,G),'improve-ui':(S,A),'baseline-ui':(S,F),'critique':(S,A),'design-review':(S,A),'design-critique':(S,A),'design-html':(S,G),
 'design-shotgun':(S,G),'create-canvas':(S,G),'canvas-design':(S,G),'algorithmic-art':(S,G),'web-artifacts-builder':(S,G),'slides':(S,G),'mobile-native':(S,F),
 'ios-design-review':(S,A),'plan-design-review':(S,A),'figma-generate-design':(S,G),'figma-shaders':(S,G),'figma-generative-plugins':(S,G),'anatomy':(S,G),'stageshow':(S,G),
 'dataviz':(S,D),'design-handoff':(S,GT),'ui-skills-root':(S,R),'refactoring-ui':(S,D),'ux-heuristics':(S,A),'diagram':(S,G),'excalidraw-skill':(S,G),
 'ai-elements':(AI,G),'discernment-nudge':(AI,D),'transitions-ui-generation':(AI,G),
 'a11y-audit':(X,A),'fixing-accessibility':(X,F),'accessibility-review':(X,A),'web-design-guidelines':(X,A),'ux-writing':(X,G),'ux-copy':(X,G),
 'performance':(X,F),'design-qa':(X,GT),'gate':(X,GT),'ship':(X,GT),'skill-creator':(X,R),
}
def fm(path):
    t = path.read_text(errors='replace'); m = re.match(r'^---\n(.*?)\n---', t, re.S); name = desc = ''
    if m:
        for line in m.group(1).splitlines():
            if line.startswith('name:'): name = line[5:].strip().strip('"\'')
            if line.startswith('description:'): desc = line[12:].strip().strip('"\'>|').strip()
    if not name: name = path.parent.name
    if not desc:
        body = t[m.end():] if m else t
        desc = next((l.strip() for l in body.splitlines() if l.strip() and not l.startswith('#')), '')
    return name, desc[:150]
installed = set(p.name for p in (H/'.claude/skills').iterdir() if p.is_dir()) | BUILTIN
for d in list(INSTALLED_DIRS.values())[1:]:
    for f in d.rglob('SKILL.md'): installed.add(f.parent.name)
rows, skipped = {}, set()
def invoke_for(path, name):
    """How an installed skill is called: /name for ~/.claude/skills, plugin:name for plugin cache."""
    parts = path.parts
    if 'cache' in parts and 'plugins' in parts:
        i = parts.index('cache'); return f"{parts[i+2]}:{name}"
    return f"/{name}"
def add(name, desc, source, inst, path=None):
    if name not in TAG: skipped.add(name); return
    r = rows.setdefault(name, {'desc':desc,'sources':[],'installed':False,'paths':[],'invoke':None})
    r['sources'].append(source); r['installed'] = r['installed'] or inst
    if path is not None:
        try: rel = str(path.relative_to(PACK))
        except ValueError: rel = str(path)
        if rel not in r['paths']: r['paths'].append(rel)
        if inst and not r['invoke'] and not str(path).startswith(str(PACK)): r['invoke'] = invoke_for(path, name)
for repo in CLONED:
    d = ROOT/repo
    if not d.exists(): continue
    files = [f for f in d.rglob('SKILL.md') if 'node_modules' not in f.parts]
    if repo == 'VoltAgent_awesome-design-md' and not files:
        add('awesome-design-md','Corpus of DESIGN.md files reverse-engineered from real brand design systems (reference, not a skill)', repo.replace('_','/',1), False, d/'README.md'); continue
    seen = set()
    for f in sorted(files):
        n, ds = fm(f)
        if n in seen: continue
        seen.add(n); add(n, ds, repo.replace('_','/',1), n in installed, f)
for label, d in INSTALLED_DIRS.items():
    if d.exists():
        for f in sorted(d.rglob('SKILL.md')):
            n, ds = fm(f); add(n, ds, label, True, f)
for n, r in rows.items():
    if r['installed'] and not r['invoke']: r['invoke'] = f"/{n}"
cell = {(l,m):[] for l in LAYERS for m in MODES}
for n, r in sorted(rows.items()):
    cell[TAG[n]].append(n + ('' if r['installed'] else '*'))
out = ["# Design skills grid\n\nGenerated by `research/build-skills-grid.py` from every `SKILL.md` in the cloned skill repos under `repos/` plus the design skills already installed on this Mac (`~/.claude/skills`, impeccable, taste-skill, frontend-design, figma and design plugins).\n\n`name` = installed and invocable now. `name*` = only in a clone, not installed. Non-design skills (business, code architecture, docx/pdf, Vercel deploy, repo-internal dev workflows in opencode/gemini-cli/motion/json-render) are excluded.\n",
       "## Start here (orchestrators, not specialists)\n",
       "| Skill | What it does | When |", "|---|---|---|",
       "| `design-director` | Thinks with you. Explore a new product's direction, audit an existing one, or plan a redesign. Writes `.design/brief.md` or `.design/audit.md`. Never edits product code. | You do not know what it should look like, what is wrong, or which specialist to use. |",
       "| `design-builder` | Executes an approved brief against the codebase: tokens, layout, components, copy, motion, responsive, a11y, then review-and-fix loops. | A brief is approved, or an audit's fix list is accepted. |",
       "\nBoth live in `skills/` and resolve specialists through `skills/design-director/reference/catalog.json` + `playbook.md`. Experts skip them and call any specialist below directly.\n",
       "## Layer x mode\n", "| Layer \\ Mode | " + " | ".join(MODES) + " |", "|---|" + "---|"*len(MODES)]
for l in LAYERS:
    out.append(f"| **{l}** | " + " | ".join("<br>".join(f"`{x}`" for x in cell[(l,m)]) for m in MODES) + " |")
tot = len(rows); inst = sum(r['installed'] for r in rows.values())
out.append(f"\nTotal design skills: {tot}. Installed: {inst}. Clone-only: {tot-inst}.\n\n## Gaps (empty cells)\n")
for l in LAYERS:
    e = [m for m in MODES if not cell[(l,m)]]
    if e: out.append(f"- {l}: " + ", ".join(e))
out.append("\n## Crowded cells (pick one, park the rest)\n")
for (l,m), xs in cell.items():
    if len(xs) >= 4: out.append(f"- {l} x {m} ({len(xs)}): " + ", ".join(f"`{x}`" for x in xs))
out += ["\n## Catalog\n", "| Skill | Layer | Mode | Installed | Source | Description |", "|---|---|---|---|---|---|"]
for l in LAYERS:
    for m in MODES:
        for x in cell[(l,m)]:
            n = x.rstrip('*'); r = rows[n]
            out.append(f"| `{n}` | {l} | {m} | {'yes' if r['installed'] else 'no'} | {', '.join(dict.fromkeys(r['sources']))} | {r['desc'].replace('|','/')} |")
out.append("\n## Seen but not design (left out)\n\n" + ", ".join(f"`{n}`" for n in sorted(skipped)) + "\n")
(PACK/'SKILLS.md').write_text("\n".join(out))
catalog = {'generated_from': 'research/build-skills-grid.py', 'layers': LAYERS, 'modes': MODES, 'skills': []}
for n, r in sorted(rows.items()):
    l, m = TAG[n]
    catalog['skills'].append({'name': n, 'layer': l, 'mode': m, 'installed_at_generation': r['installed'],
        'invoke': r['invoke'], 'paths': r['paths'], 'sources': list(dict.fromkeys(r['sources'])), 'description': r['desc']})
for n, l, m, d in [('design-director','Orchestration','Direct','Conversational design direction: explore / audit / redesign / route. Writes .design/brief.md or .design/audit.md; never edits product code.'),
                   ('design-builder','Orchestration','Build','Implements an approved .design/brief.md: foundations, tokens, layout, components, copy, motion, responsive, a11y, then review-and-fix loops.')]:
    catalog['skills'].append({'name': n, 'layer': l, 'mode': m, 'installed_at_generation': (H/'.claude/skills'/n).exists(),
        'invoke': f'/{n}', 'paths': [f'skills/{n}/SKILL.md'], 'sources': ['design-pack'], 'description': d})
cat = PACK/'skills/design-director/reference/catalog.json'; cat.parent.mkdir(parents=True, exist_ok=True)
cat.write_text(json.dumps(catalog, indent=1)); print(f"catalog.json: {len(catalog['skills'])} entries")
print(f"SKILLS.md: {tot} skills, {inst} installed, {tot-inst} clone-only; {len(skipped)} non-design skipped")
