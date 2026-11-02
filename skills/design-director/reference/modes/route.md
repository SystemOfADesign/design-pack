# Mode: ROUTE (user knows the problem, not which specialist)

Outcome: the right specialist named and run. No brief needed. One question at most, usually none.

## Symptom -> specialist

| User says | Likely foundation | Send to |
|---|---|---|
| animations are janky / slow / drop frames | motion (performance) | `animation-performance` first (names the cause, then fixes), then `review-animations` on what remains |
| animations feel off / too much / wrong timing | motion (craft) | `review-animations` (findings only) then `animate` to rebuild what it flags |
| nothing moves and it feels dead | motion | `find-animation-opportunities`, then `animate` |
| it looks amateur / off / messy, cannot say why | hierarchy, spacing | `design-review` (gstack) findings, then `baseline-ui` or `impeccable layout` |
| text is hard to read | readability | `web-typography` rules, `impeccable typeset` |
| colors feel wrong / washed out / clashing | color system | `design-tokens` (semantic set), `impeccable colorize` or `quieter` |
| looks generic / like every AI site | taste | `design-taste-frontend` (public pages) or `impeccable critique` then `bolder` / `distill` |
| too busy / cluttered | hierarchy, density | `impeccable distill`, `interface-design` focal point rule |
| too bland / empty | taste | `impeccable bolder` / `delight` |
| users get confused / cannot find things | usability | `ux-heuristics`, `design-everyday-things` |
| breaks on phone / small screens | responsive | `impeccable adapt` |
| breaks with real data / long names / empty lists | content reality | `break-ui`, `impeccable harden` |
| accessibility complaint / keyboard / screen reader / contrast | a11y | `a11y-audit` or `accessibility-review`, then `fixing-accessibility` |
| error messages / labels / empty-state text are bad | copy | `ux-copy`, `impeccable clarify` |
| every page looks slightly different | consistency | `improve-ui`, `create-design-md`, `design-system`, then `design-tokens` |
| first-run is confusing / blank | onboarding | `impeccable onboard` |
| page feels slow / things jump | performance | `performance`, `impeccable optimize` |
| need a component (sheet, toast, command menu) | components | `ask-sonner`, `pick-ui-library`, `design-component`, reference repos `vaul` `sonner` `cmdk` |
| I have a Figma / screenshot to match | screens | `image-to-code`, `figma-design-to-code` |
| want a dashboard with lots of numbers | screens | `data-dashboard`, `dataviz` |
| want it to feel like Apple / Rams / Nothing / Linear | philosophy | `apple-design`, `rams-braun-ui`, `nothing-design`, `repos/ln-dev7_circle` |
| building chat / AI features | AI UX | `ai-elements`, `discernment-nudge` |
| should this exist / is the concept right | product fit | `steve-jobs-design-review`, `jobs-to-be-done`, `mom-test` |
| need a hero image / product shot / feature-card or bento imagery of the app for a landing or docs page | marketing imagery | `stageshow` (Generate, writes a React component; still or looped demo decided in its step 1). Not for the product's real UI |
| need a demo gif / cursor walkthrough / animated product tour | marketing imagery | `stageshow` (gold example first, film with its `scripts/film.mjs --gate`; its own gold examples can fail the gate, so a failure before any edit is upstream) |
| need an isometric explainer figure / system diagram illustration | explainer imagery | `anatomy`; raster banners go to `banner-design` |

## Procedure
ROUTE skips the shared procedure's screenshot and question-round steps. It is one message, then action.
1. Resolve the candidates: `python3 <design-director>/scripts/skills.py find <names>`. `user-only` means the user must type it (`/review-animations src/Dropdown.tsx`); tell them the exact line.
2. Say in one line what the specialist will do and whether it edits code. Catalog mode tells you: Audit/review and Reference never edit; Generate and Fix do; Doctrine skills vary, so read the SKILL.md's first paragraph before promising.
3. Ask at most one question, only if the symptom spans two foundations or the screen is unknown. Otherwise do not ask: state the plan in one line and invoke (installed), read-and-follow (clone-only), or hand the user the `/name` line (user-only). The user can stop you; a question they did not need is worse.
4. If the fix touches more than one screen or the system (tokens, shared components), stop and recommend AUDIT or a scoped brief instead; piecemeal fixes to systemic problems make consistency worse.
