# Review loop

Runs after phase 10, and after any fix run. Findings only from the passes; fixing is a separate step so a pass cannot grade its own work.

## Passes (playbook "audit:" sections), in order

| # | Pass | Specialist (primary) | Kind | Blocks completion when |
|---|---|---|---|---|
| 1 | Hierarchy and visual craft | `design-review` (gstack), `refactoring-ui` | judged | any Major |
| 2 | Usability | `ux-heuristics`, `design-critique` | judged | severity 3+ on the primary task |
| 3 | Accessibility | `a11y-audit` / `accessibility-review` / `web-design-guidelines` | measured where axe runs | any violation |
| 4 | Consistency and drift | `improve-ui`, `lint_hardcodes.py` | measured count | new hardcodes > 0 in touched files |
| 5 | Motion | `review-animations` | judged | any Major |
| 6 | Worst-case data | `break-ui` | judged | anything that breaks layout or hides data |
| 7 | Responsive and performance | `impeccable audit`, `performance`, `verify_responsive.mjs` | measured where kit runs | horizontal overflow at floor width; CLS |
| 8 | Copy | `ux-copy` | judged | placeholder or filler shipped |
| 9 | Generic tells and taste | `impeccable critique`, `critique` | judged | critic's blockers only |

Run 1-4 always. Run 5 if motion exists. Run 6-8 always. Run 9 last, once, after 1-8 are green.

## Triage

- Merge duplicates across passes; keep the highest severity.
- Severity from `foundations.md`: Blocker / Major / Minor / Polish.
- Blocker and Major: fix in this round. Minor: fix if local to touched code, else list. Polish: list.
- A finding that contradicts the approved brief (e.g. critic wants a different direction) is not a defect; record it as "critic disagrees with brief" and move on.

## Fix routing

| Pass | Fix with |
|---|---|
| 1 | `baseline-ui`, `impeccable layout` / `typeset` |
| 2 | `design-everyday-things` rules, `impeccable clarify` / `onboard`; flow changes need the brief's permission |
| 3 | `fixing-accessibility` |
| 4 | tokens (`design-tokens`), `impeccable extract` |
| 5 | `animate` (rebuild), `fixing-motion-performance`, `remove-animations` when motion has no purpose |
| 6 | `impeccable harden` |
| 7 | `impeccable adapt` / `optimize`, `performance` |
| 8 | `ux-copy`, `impeccable clarify` |
| 9 | `impeccable bolder` / `quieter` / `distill` / `polish` inside the brief's direction |

## Stop rules

- Re-run only the passes that produced the fixed findings.
- Maximum three rounds. After that, remaining items are reported as open with severity and a one-line cost.
- Never claim green for a pass that did not run. "Not run: no browser" is the honest line.
- Render and look: gates pass while a screen is visibly broken. Screenshot every in-scope surface after the final round into `.design/shots/after/` and click the primary flow once.
