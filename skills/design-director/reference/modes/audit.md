# Mode: AUDIT (existing product, "what is wrong and where next")

Outcome: `.design/audit.md` (template in `audit-template.md`) and screenshots under `.design/shots/`. No product code changes, no redesign proposals unless asked at the end.

## 1. Scope (one round of questions, max three, from `questions.md` AUDIT)
Which surfaces, what the main task is on each, whether the look is negotiable. Default: the three screens with the most traffic or the primary flow end to end.

## 2. Capture evidence (read-only)
- Run the app if it runs; screenshot each in-scope screen at desktop and a narrow phone width, light and dark if both exist, plus the empty / loading / error states you can reach. Use `browse` (gstack) or the browser setup from `design-review`. Save to `.design/shots/`.
- No running app: ask for screenshots, or audit from code only and mark every render-dependent pass "not run".
- Reconstruct the current system with `create-design-md` logic (read-only): tokens, type scale, spacing, components, where the code disagrees with itself.

## 3. Run the passes (playbook "audit:" sections), in this order, findings only
1. hierarchy and visual craft
2. usability (walk the primary task; severity 0-4)
3. accessibility
4. consistency and system drift (include the measured hardcode count if the kit's lint runs)
5. worst-case data
6. responsive and performance
7. motion (only if the product has motion, or clearly lacks feedback)
8. copy
9. generic tells and taste (last; judged)
10. product fit (only when the user asked "should this exist like this")

Specialists that want to fix (gstack `design-review`, `baseline-ui`, impeccable refine verbs) run in findings-only form: ask them for the findings table and stop before edits, or read their checklists and apply them yourself.
Each pass records: specialist used, measured or judged, not run and why.

## 4. Triage
Merge duplicates across passes. Rank by `foundations.md` severity. Attach the foundation number and the plain "what a user experiences". Keep "what is already good" so the builder does not regress it.

## 5. Recommend, do not redesign
Three tiers: fix now, next, later. Each item names the route: `design-builder` fix run from this audit, a scoped brief (EXPLORE/REDESIGN on one surface), or one specialist by name. End with the one-line redesign verdict: not needed / worth it because <reason>.

## 6. Deliver
Write `.design/audit.md`. In chat: the verdict paragraph, the top five findings as bullets, the fix-now list, and the question "fix the fix-now list, or discuss first?" Do not start fixing.
