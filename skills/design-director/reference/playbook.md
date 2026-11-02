# Playbook: which specialist for which job

Used by `design-director` (consult + audit sections) and `design-builder` (build sections).
Resolve any name with `python3 <design-director>/scripts/skills.py find <name>`; it prints
`invoke <x>` (call it with the Skill tool) or `read <abs path>` (read that SKILL.md and follow it).

Rules for every section:
- First name in a list is the primary. Later names are fallbacks or complements; use them when the primary is missing, or when the job spans two viewpoints.
- `user-only` skills are installed but marked `disable-model-invocation`; you cannot call them. Either ask the user to type `/name <target>` or read their SKILL.md and follow it yourself, and say which you did.
- `invoke` skills are already installed. `read` skills are clone-only: read the SKILL.md, then act as it instructs. Where it writes `${CLAUDE_SKILL_DIR}`, substitute the directory of the file you read. plugin87 skills reference `${CLAUDE_SKILL_DIR}/../../../` = the kit root `repos/plugin87_ux-ui-agent-skills/`; that works from the clone.
- Consulting is silent: read the doctrine, apply it, do not recite it to the user. Translate with `plain-language.md`.
- Never claim a specialist ran if it did not. "Not run" is an acceptable report; a guessed verdict is not.

## Director: consult (read for knowledge, never edits)

### consult: product UI (apps, dashboards, tools, settings)
- `interface-design` one focal point per view, type ratio, density in px, layering, restraint. The best single doctrine for Operate-mode screens.
- `refactoring-ui` hierarchy, spacing, color, depth as fixable rules. Plain enough to quote to a non-designer.
- `emil-design-eng` the invisible details: states, feedback, polish.
- `impeccable` read its `reference/operate.md` for Operate / Read surfaces; its Modes section decides Persuade / Operate / Read / Experience.
- `design-doctrine` the five non-negotiables and the eight states.

### consult: marketing, landing, brand
- `design-taste-frontend` researched directions (idea, composition, type, palette) for public pages; the anti-generic house style.
- `frontend-design` aesthetic direction, typography, non-templated choices.
- `brand-identity` `brandkit` brand foundation when none exists.
- `top-design` only when the brief is explicitly award-level / immersive.

### consult: usability and product fit (why, workflow, affordances)
- `ux-heuristics` Nielsen + Krug, severity scale, dark patterns.
- `design-everyday-things` affordances, signifiers, feedback, conceptual models. Use when "users are confused".
- `jobs-to-be-done` what the user hires the product for; drives the lead element and the primary flow.
- `mom-test` how to ask the user questions that do not lead them.
- `lean-ux` hypothesis framing when the user is unsure what to build.
- `steve-jobs-design-review` ruthless simplicity pass on the concept, not the pixels.
- `grill-me` the question bank; its "every question must change the work" rule is ours too.

### consult: motion
- `design-motion-principles` `motion-design` when motion should exist and what it is for.
- `emil-design-eng` `apple-design` physicality, interruptibility, springs vs easing.
- `animation-performance` the budget.

### consult: typography and color
- `web-typography` measure, scale, leading, optical sizing.
- `design-tokens` how color/type/space become a system (3-tier DTCG).
- `rams-braun-ui` `nothing-design` `37signals-way` `ios-hig-design` named philosophies; consult only when the user asks for that feel or the brief lands there.
- `awesome-design-md` corpus of real DESIGN.md files; useful to show what a finished system reads like.

### consult: AI product UX
- `ai-elements` chat, reasoning, sources, confirmation states.
- `discernment-nudge` when the UI should slow the user down.
- `transitions-ui-generation` streaming / generated UI transitions.

### consult: inspect what exists (read-only)
- `create-design-md` reconstruct the current design language from code and screenshots; the most reliable "what do we have" scan.
- `impeccable` `impeccable context` (its launcher) loads PRODUCT.md / DESIGN.md if present; `document` writes DESIGN.md (builder only).
- `improve-ui` audits a surface against its own design evidence, read-only, and writes implementation plans.
- `browse` (gstack) open the running app, screenshot every main screen and state. `design-review` (gstack) has the same browser setup.

### consult: show directions (seeing beats reading)
- `design-shotgun` generate several variants on a comparison board and collect structured feedback.
- `impeccable` `generate [n] [element]` variants in the live browser; `live` pick-and-iterate.
- `design-html` one direction rendered as production-quality HTML for a real screen.
- `design-consultation` full system proposal with font + color preview pages.

## Director: audit passes (read-only; findings only, no edits)

### audit: hierarchy and visual craft
- `design-review` (gstack) designer's-eye QA: inconsistency, spacing, hierarchy, slop patterns, slow interactions. Run in findings-only mode; do not let it fix.
- `refactoring-ui` quick diagnostic checklist.
- `interface-design` one-focal-point and type-ratio checks for product UI.

### audit: usability
- `ux-heuristics` Nielsen 10 with severity 0-4 and a cognitive walkthrough of the primary task.
- `design-critique` structured usability / hierarchy / consistency feedback.
- `design-review` (plugin87, read) six weighted dimensions, prioritized findings table.

### audit: accessibility
- `accessibility-review` WCAG 2.1 AA audit.
- `a11y-audit` WCAG 2.2 AA/AAA criterion-referenced findings with fixes.
- `web-design-guidelines` Vercel Web Interface Guidelines compliance on the code.

### audit: consistency and system drift
- `improve-ui` verified drift from the product's own system.
- `create-design-md` reconstructs the system; disagreements between code and screens are findings.
- plugin87 `lint_hardcodes.py` under `repos/plugin87_ux-ui-agent-skills/scripts/` counts off-token values (measured, not judged).

### audit: motion
- `review-animations` craft bar on existing motion code.
- `find-animation-opportunities` what should move and does not.
- `improve-animations` whole-codebase motion survey with a prioritized plan.

### audit: worst-case data
- `break-ui` long names, empty, one, hundreds, non-Latin, extreme numbers.
- `impeccable` `harden` playbook lists the states to check.

### audit: responsive and performance
- `impeccable` `audit` technical checks: a11y, perf, responsive.
- `performance` Core Web Vitals, layout shift, animation cost.
- plugin87 `verify_responsive.mjs`, `verify_target_size.mjs` (need node + playwright; a SKIPPED gate is not a pass).

### audit: copy
- `ux-copy` labels, errors, empty states, CTAs.
- `ux-writing` voice and tone system.

### audit: generic tells and taste
- `impeccable` `critique` heuristic-scored design review.
- `critique` adversarial; argues for rejection. Use last.
- `design-taste-frontend` its inspector for public pages.

### audit: product fit
- `steve-jobs-design-review` focus and end-to-end excellence.
- `jobs-to-be-done` does the primary flow serve the job.

## Builder: phases (edits product code)

### build: foundations and tokens
- `design-tokens` 3-tier DTCG tokens (primitive, semantic, component); validate with the kit's `validate_tokens.py` + `validate_contrast.py`.
- `token-build` emit CSS variables / platform outputs; `style-dictionary` repo is the reference tool.
- `design-system` audit / extend an existing system before adding to it.
- `impeccable` `extract` pulls reusable tokens and components out of existing code.
- `migrate-design-system` when the brief says replace the system.

### build: structure and layout
- `impeccable` `layout` spacing, rhythm, hierarchy on an existing screen; new surfaces go through its new-work path.
- `design-screen` whole-screen pipeline: brief inference, direction, tokens, build, gate, critic (needs plugin87 kit).
- `interface-design` the rules you build against for product UI.
- `design-html` production HTML/CSS for a finalized screen.
- `data-dashboard` dense data screens.

### build: components and states
- `design-component` one component's spec with all states.
- `shadcn` (vercel) when the stack is shadcn/Tailwind.
- `vercel-composition-patterns` compound components, no boolean-prop explosions.
- `ask-sonner` `pick-ui-library` choosing primitives; `radix-ui_primitives`, `emilkowalski_vaul`, `emilkowalski_sonner`, `dip_cmdk` as reference implementations under `repos/`.
- `design-doctrine` the eight states every interactive element ships.

### build: typography
- `impeccable` `typeset` hierarchy and fonts.
- `web-typography` scale, measure, leading rules.

### build: copy
- `impeccable` `clarify` labels, errors, microcopy.
- `ux-copy` write or review specific strings.

### build: motion
- `animate` purpose, tool, properties, curve, duration, interruption, exit.
- `emil-design-eng` `apple-design` the taste behind it.
- `impeccable` `animate` when motion is part of a wider polish pass.
- `animation-performance` keep it composite-only.

### build: responsive
- `impeccable` `adapt` devices and widths; mobile is the base layer.
- `mobile-native` when it must feel native on phones.

### build: accessibility
- `fixing-accessibility` ARIA, keyboard, focus, contrast, form errors.
- `a11y-audit` re-check after fixes.

### build: polish and harden
- `baseline-ui` fast deslop of spacing, hierarchy, typography.
- `impeccable` `polish` final pass; `harden` errors, i18n, edge cases; `onboard` first-run and empty states.
- `break-ui` then fix what it broke.
- `emil-design-eng` the last 5%.

### build: record the system
- `impeccable` `document` writes DESIGN.md from the shipped code.
- `create-design-md` same job without impeccable.

### build: gates
- `gate` `design-qa` plugin87 one-command gate (tokens, contrast, hardcodes, axe, keyboard, target size, responsive, slop tells). Needs `node`, `npm install && npx playwright install chrome` inside the kit; SKIPPED is not a pass.
- `ship` pre-release checklist.
