# How to use design-pack

Two entry points for people who know nothing about design, and direct access to 109 specialists for people who do.

```
/design-director   think: what should it look like / what is wrong / plan a redesign / which skill do I need
/design-builder    do: implement the approved brief, run review passes, fix what they find
```

The director writes only under `.design/` in your project (`brief.md`, `audit.md`, `shots/`, `directions/`). The builder edits product code. Nothing changes in your code until you say "approved" and ask to build.

## Scenario 1: new app, no idea what it should look like -> build

```
> /design-director
  I'm building a tool for small landlords to track rent, repairs and leases. Mostly used on a laptop,
  a few times a week. I have a Next.js app with the data model done and ugly default pages.
```
What happens:
- Director reads the repo (Next.js, Tailwind, no tokens, 6 pages), then asks one round: who exactly, the one task they come for most, usage frequency, two products whose feel you like. Each as options with a default; "you choose" is allowed.
- It decides the foundations itself: these are Operate screens (people work in them), the lead on the home page is "what needs my attention this week", body text 16px, AA contrast, phone must work but laptop first.
- It presents two directions in plain words, for example "Quiet ledger" (feels like a well-kept accounts book; Linear / Stripe dashboard) and "Warm office" (friendlier, more color, Notion / Basecamp). It recommends one and offers a board: the same real page rendered in each direction, opened in your browser.
- You push back: "too corporate". It warms the neutrals, drops the grid of equal cards, keeps the structure. "Show another" gives a new idea, not a recolor.
- It writes `.design/brief.md`, reads it back in three sentences, asks for "approved".
```
> approved, build it
```
- Builder posts a ten-line plan (tokens -> layout per page -> components and their eight states -> type -> copy -> motion: feedback only -> responsive -> a11y -> polish -> DESIGN.md), executes it, then runs the review passes (hierarchy, usability, accessibility, consistency, worst-case data, responsive, copy, generic tells), fixes Blockers and Majors, re-runs only the failed passes, up to three rounds.
- You get: what you will notice per page, a verified table (measured vs judged vs not run), open items, before/after screenshots.

## Scenario 2: existing app, "tell me what is wrong"

```
> /design-director audit
  Here is our support dashboard. Agents say it is tiring to use all day. Don't change the brand.
```
- Director asks which three screens matter and what the main task is on each, runs the app, screenshots desktop + phone + dark + empty/error states into `.design/shots/`.
- Runs the audit passes read-only: hierarchy (`design-review`), usability walkthrough (`ux-heuristics`), accessibility (`a11y-audit`), consistency and hardcode count (`improve-ui`, lint), worst-case data (`break-ui`), responsive, copy, generic tells last.
- Writes `.design/audit.md`: one verdict paragraph, findings ranked Blocker / Major / Minor / Polish with "what a user experiences" and measured-or-judged evidence, what is already good, and three tiers of next actions, each routed (builder fix run, scoped brief, or one specialist).
- It ends with "fix the fix-now list, or discuss first?" and does not touch code.
```
> fix the fix-now list
```
- Builder fixes only those findings via the Fix specialists, re-runs only the passes that produced them, reports.

## Scenario 3: existing app, complete redesign -> build

```
> /design-director redesign
  Our admin UI grew over four years; every page looks different. New design system, keep all the flows.
```
- Director inventories screens, shared components and usage counts, token files, hardcoded values, reconstructs the current system (`create-design-md` logic), runs a short audit so Preserve / Replace is grounded in findings.
- Asks: what must survive, the reason in one line, big-bang or page-by-page, two products to move toward and one to move away from.
- Offers two or three directions framed as "what changes for a user who already knows the product", with what stays identical in all of them. Board on the busiest screen if you want to see it.
- Brief adds Preserve / Replace / migration order (tokens -> typography and spacing -> component states -> motion -> screens by traffic) and "no behavior change except accessibility fixes".
```
> approved
> /design-builder
```
- Builder migrates in that order; one shared theme that every page consumes; smoke-tests each flow after its screen migrates; review loop; DESIGN.md.

## Scenario 4: you know the problem, not the skill

```
> /design-director route  the dropdown animations feel janky and slow
```
- Director maps the symptom (`reference/modes/route.md`): janky and slow is a performance symptom, so it states the plan in one line ("`animation-performance` finds why the dropdown drops frames and fixes it; then `review-animations` judges what remains") and runs it. No question unless the screen is unknown. `review-animations` is marked user-only by its author, so the director hands you the exact line to type: `/review-animations src/components/Dropdown.tsx`.
- If the symptom turns out systemic (every page slightly different, colors inconsistent), it stops and recommends AUDIT instead of a piecemeal fix.

## Expert path: call any specialist directly

Nothing changed here. Installed skills by name, clone-only by path.

```
/review-animations      audit src/components/Drawer.tsx
/break-ui               feed worst-case data into the invoice table
/emil-design-eng        polish the settings page
/impeccable critique    the pricing page
/design-taste-frontend  make this hero stop looking templated
Read design-pack/repos/plugin87_ux-ui-agent-skills/.claude/skills/design-tokens/SKILL.md and build a 3-tier token set.
```

Resolve any of the 109 names to "invoke X" or "read <path>":

```bash
python3 design-pack/skills/design-director/scripts/skills.py find design-tokens ux-heuristics animate
python3 design-pack/skills/design-director/scripts/skills.py list --layer motion --installed
python3 design-pack/skills/design-director/scripts/skills.py phase "audit: accessibility"
```

## Install a clone-only skill globally

Symlink the skill folder into `~/.claude/skills/` (keeps it in sync with the clone). Check for collisions first: `ls ~/.claude/skills | grep -x <name>`.

```bash
ln -s ~/Projects/main-things/design-pack/repos/plugin87_ux-ui-agent-skills/.claude/skills/design-tokens ~/.claude/skills/design-tokens
```

Suggested first installs (one per crowded cell, fills gaps): design-tokens, token-build, jobs-to-be-done, ai-elements, brandkit, web-design-guidelines, rams-braun-ui.

## Repos as reference code

```
Read design-pack/repos/emilkowalski_vaul/src/index.tsx and explain how swipe-to-dismiss velocity is handled.
Use design-pack/repos/sakofchit_system.css as the stylesheet for a System 7 style settings window.
Study design-pack/repos/ln-dev7_circle for the Linear sidebar layout and reproduce it here.
```

## Keeping it current

```bash
python3 design-pack/research/build-skills-grid.py   # regenerates SKILLS.md and skills/design-director/reference/catalog.json
# add a repo: append "owner/name<TAB>stars<TAB>source" to research/clone-list.txt, then
git clone --depth 1 https://github.com/owner/name design-pack/repos/owner_name
```

## Marketing imagery with Stageshow

```
I need a hero illustration of the dashboard for the landing page, animated, with a cursor.
```

`design-director` ROUTE sends this to `stageshow` (catalog: Screens/pages x Generate; read-by-path from `plugins/stageshow/skills/stageshow/SKILL.md` or `repos/benjitaylor_skills/stageshow/SKILL.md`, or installed as the `stageshow` plugin). It writes a React component into the host app and films it with `scripts/film.mjs --gate`; see its SKILL.md step 7. Mark the stage subtree `role="img"` so builder review passes (filler, a11y, worst-case data, motion timing, hardcode lint) skip it. Evaluation and caveats: `research/stageshow/REPORT.md`.
