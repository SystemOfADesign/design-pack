# .design/audit.md template

Written by `design-director` in AUDIT mode. Findings only. No product code changes.

```markdown
# Design audit: <product>

date: YYYY-MM-DD
surfaces reviewed: <list, with screenshot paths under .design/shots/>
passes run: <pass -> specialist -> measured | judged | not run (why)>

## Verdict in one paragraph
<plain language: what works, the two or three things holding it back, where to go next>

## Findings (highest severity first)
| # | Severity | Foundation | Where | What a user experiences | Evidence (measured / judged) | Fix in one line | Specialist |
|---|---|---|---|---|---|---|---|

## What is already good
- <keep these; the builder must not regress them>

## Recommended next actions
### Fix now (blockers and majors) -> `design-builder` fix run from this audit
- <#, #, #>
### Next (minors that cluster) -> scoped brief or specialist
- <#, # -> /animate, /break-ui, ...>
### Later (polish) 
- <...>
### Consider a redesign? <yes / no, and the one reason>

## Not reviewed
- <pass not run and why, e.g. no browser, app does not run locally>
```
