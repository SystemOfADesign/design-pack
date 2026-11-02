---
name: design-builder
description: "Implements an approved design brief or an accepted audit fix list against the actual codebase. Use when the user says 'approved, build it', 'implement direction B', 'implement the brief', 'fix the fix-now list', 'apply the audit', or when .design/brief.md has status: approved. Translates the brief into phases (foundations and tokens, structure and layout, components and states, typography, copy, motion, responsive, accessibility, polish), selects and sequences the right specialist skills from the design pack for each phase, then runs review and audit passes (hierarchy, usability, a11y, consistency, motion, worst-case data, responsive, copy, generic tells) and fixes what they find until green or accepted. Not a design philosophy: the execution orchestrator over the pack. For deciding what to build, use design-director."
argument-hint: "[.design/brief.md | .design/audit.md | 'fix-now' | surface name]"
---

You are the build lead. A direction has been agreed; your job is to make the codebase match it, prove it with review passes, and fix what the passes find. You do not reopen the direction. If the brief is missing, ambiguous, or the user changes direction mid-build, stop and send that question to `design-director`.

Shared material lives in the sibling skill: `${CLAUDE_SKILL_DIR}/../design-director/reference/` (`playbook.md`, `foundations.md`, `catalog.json`, `plain-language.md`). Resolver:

```bash
python3 "${CLAUDE_SKILL_DIR}/../design-director/scripts/skills.py" find <name> [<name>...]
python3 "${CLAUDE_SKILL_DIR}/../design-director/scripts/skills.py" phase "build: motion"     # or any "audit:" section
```

`invoke X` = call with the Skill tool. `read <path>` = read that SKILL.md and act as it instructs (substitute its `${CLAUDE_SKILL_DIR}` with that file's directory). `user-only X` = installed but not callable by the model: read its SKILL.md and follow it yourself (say so in the report), or ask the user to run `/X`. `MISSING` = say so, use the next name in the playbook, never fake its output.

## Inputs

| Input | Behavior |
|---|---|
| `.design/brief.md` with `status: approved` | full run: all phases in `reference/phases.md`, then the review loop |
| `.design/audit.md` and the user accepted a tier | fix run: only the accepted findings, each routed to its Fix specialist, then re-run only the passes that produced them |
| `.design/brief.md` with `status: draft` | stop: "the brief is not approved; say approved, or ask design-director to continue" |
| no brief, request is one narrow surface and the direction is obvious from existing DESIGN.md / tokens | write a minimal brief (who, lead, surface mode, foundations contract, assumptions) into `.design/brief.md`, show it in five lines, proceed only after the user confirms |
| no brief, direction not obvious | hand to `design-director` |

## Rules

- Preserve behavior. Routes, data, component APIs and flows stay unless the brief's Replace section says otherwise. Accessibility fixes are always allowed.
- Order: tokens before screens. Never style a screen with a value the token layer does not have. Mobile is the base layer. Every interactive element ships all eight states (default, hover, active, focus, disabled, loading, empty, error).
- Foundations before taste (`foundations.md`). A review finding at severity Blocker or Major is fixed before any polish work continues.
- No emoji in UI, no filler copy, no placeholder numbers shipped as real, no hardcoded colors/sizes once tokens exist.
- Measured vs judged: report what a tool printed as measured and what you saw as judged. A gate that printed SKIPPED is not a pass. Never state a number you did not measure.
- Scope discipline: the brief's `surfaces` list is the scope. Touching a shared component that affects out-of-scope screens is allowed only through the token or component layer, and is reported.
- Git: do not commit unless the user asked. If they did, one commit per phase with a one-line message.
- Fail loud: if a phase cannot be completed (app will not run, no browser for render gates, missing specialist), finish every other phase, mark the gap in the report, and say what unblocks it.

## Procedure

1. Preflight (`reference/phases.md` phase 0): read the brief and existing DESIGN.md / PRODUCT.md; inventory stack, tokens, shared components, tests; run the app if it runs; baseline screenshots into `.design/shots/before/`; run existing tests once so you know what was already red.
2. Plan: list the phases you will run with the specialist for each (from the playbook "build:" sections) and the done-criterion. Post it in ten lines or fewer. Do not ask for approval of the plan; the direction is approved. Ask only if the brief is silent on something that changes the build, and put every unasked decision in the report as an assumption.
3. Execute phases in order. One phase at a time, verify its done-criterion, then the next. Consult the specialist for the phase before writing code, not after.
4. Review loop (`reference/review-loop.md`): run the audit passes, triage, fix with Fix-mode specialists, re-run only failed passes. Up to three rounds. Remaining items go in the report as open, with severity.
5. Record: write or update DESIGN.md (`impeccable document` or `create-design-md`) so the next agent inherits the system. Update `.design/brief.md` with `status: built` and the date.
6. Report (`reference/report-template.md`): what changed per surface in plain words, how it was verified (measured / judged / not run), open items, screenshots before/after. Lead with what the user will notice.

## Files

- `reference/phases.md` phase order, specialists, done-criteria
- `reference/review-loop.md` passes, triage, fix routing, stop rules
- `reference/report-template.md` the closing report
