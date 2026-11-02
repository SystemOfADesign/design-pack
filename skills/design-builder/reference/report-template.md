# Closing report (chat + `.design/build-log.md`)

```markdown
# Build report: <product / surfaces>  (<date>)

## What you will notice
- <surface>: <two plain sentences: what changed, what it feels like now>
- ...

## Verified
| Pass | Result | Kind | Detail |
|---|---|---|---|
| Accessibility | 0 violations | measured | axe via a11y-audit, 6 pages |
| Consistency | 0 new hardcodes | measured | lint_hardcodes.py on src/ |
| Hierarchy | green | judged | design-review round 2 |
| Responsive | green at 360px | measured | verify_responsive.mjs |
| Motion | not run | - | no motion in brief |

## Open (not fixed)
| # | Severity | What | Why open | Cost if ignored |
|---|---|---|---|---|

## Assumptions made during the build
- <assumption> -> <default>; cost if wrong: <one line>

## Files
- tokens: <path>
- DESIGN.md: <path>
- screenshots: .design/shots/before/, .design/shots/after/
- phases log: .design/build-log.md

## Next
- <one of: ship; run design-director audit in a month; the two open Majors need a decision>
```

Chat version: the "What you will notice" bullets, the Verified table, open items, and the Next line. Nothing else.
