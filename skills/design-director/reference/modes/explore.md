# Mode: EXPLORE (new product, direction unknown)

Outcome: `.design/brief.md` with `mode: explore`, approved by the user, plus optional `.design/directions/*.html`.

## 1. Read before asking (2-5 minutes, read-only)
- Project: framework, styling, component library, routing, existing screens, README, PRODUCT.md / DESIGN.md / BRIEF.md, brand assets, tokens or theme files. Record what is decided already.
- If nothing exists yet (idea stage): skip to questions; note "greenfield".

## 2. Ask (one round, max five, from `questions.md` EXPLORE)
Lead with audience + primary task + usage frequency. Feel: one question, with "you choose" as an option. Everything else becomes an assumption.

## 3. Decide the foundations (no user input needed)
- Surface modes per screen (Persuade / Operate / Read / Experience) from `impeccable`'s Modes.
- The lead per surface from the primary task.
- Content reality assumptions.
- Platform floor, dark mode default, a11y target (AA).
Consult silently: `interface-design` or `design-taste-frontend` depending on mode, `jobs-to-be-done` for the lead, `ux-heuristics` for the primary flow.

## 4. Generate directions (`directions.md`)
Two or three. Name them. Recommend one. Offer the board.

## 5. Iterate
Map feedback through `plain-language.md`. Adjust or replace directions. Stop when the user says it is right.

## 6. Write and approve
Fill `brief-template.md`. Read back: who, the lead, the direction name, the three things they will notice. Ask for "approved". On approval set `status: approved` and say: run `/design-builder` (or "say build it") to implement; nothing has been changed in the code yet.

## Never
- Write product source. Only `.design/`.
- Ask the user to name a font, a hex, a spacing scale, a motion curve.
- Offer a blended "safe" direction after the user pushed back. Change the idea.
