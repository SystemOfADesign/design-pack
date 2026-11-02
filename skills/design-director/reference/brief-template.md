# .design/brief.md template

Written by `design-director` at the end of EXPLORE or REDESIGN. Read by `design-builder`.
Status moves `draft` -> `approved` only when the user says so in their own words.
Everything the builder needs is here; nothing lives only in the conversation.

```markdown
# Design brief: <product or surface>

status: draft | approved
mode: explore | redesign
date: YYYY-MM-DD
surfaces: <list of screens / pages in scope>
out of scope: <explicit>

## Who and what
- Who uses this: <one or two kinds of people, in plain words>
- The job they hire it for: <one sentence>
- Primary task per surface: <surface -> task>
- Success looks like: <what they have done when they leave>

## Surface modes
| Surface | Mode (Persuade / Operate / Read / Experience) | Lead (the one thing the eye lands on) |
|---|---|---|

## Direction: "<name>"
<four plain sentences: how it feels, what you notice first, who it suits, the risk>

| Aspect | Decision | In plain words |
|---|---|---|
| Type | <families, scale ratio, body size> | |
| Color | <neutrals, one primary, semantic set, dark mode yes/no> | |
| Density | <loose / medium / tight, with a px rhythm> | |
| Shape | <radii, borders vs surfaces, elevation policy> | |
| Motion | <none / feedback only / expressive; durations and curves> | |
| Layout | <grid, max width, section composition rules> | |
| Imagery / icons | <icon set, illustration policy, photography> | |
| Closest products you know | <2-3 names> | |

Directions considered and rejected: <name: one line why>

## Foundations contract (not negotiable by taste)
- Body text >= 16px, measure 45-75ch, contrast >= 4.5:1 (3:1 large), focus visible, keyboard complete.
- Every interactive element ships all eight states: default, hover, active, focus, disabled, loading, empty, error.
- Mobile is the base layer; narrowest supported width: <px>.
- Destructive actions wear the danger variant and confirm.
- No emoji in UI; no filler copy; no placeholder numbers shipped as real.

## Content reality
- Empty / one / many: <per key list or table>
- Longest real strings: <examples>
- Real vs placeholder data: <what is real now>

## Existing system (redesign only)
- Preserve: <components, tokens, flows, behaviors that stay>
- Replace: <what goes, and why in one line each>
- Migration order: tokens -> typography/spacing -> component states -> motion -> screens

## Stack and constraints
- Framework / styling / component library: <detected>
- Where tokens live or will live: <path>
- Constraints: <brand rules, legal, platform, RTL, AA/AAA>

## Assumptions (each with its cost if wrong)
- <assumption> -> default taken; cost if wrong: <one line>

## Done when
- Builder phases complete: <list>
- Review passes green or accepted: hierarchy, usability, a11y, consistency, motion, worst-case, responsive, copy, generic-tells
- DESIGN.md recorded
```
