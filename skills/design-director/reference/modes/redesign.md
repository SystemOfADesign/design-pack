# Mode: REDESIGN (existing product, major overhaul)

Outcome: `.design/brief.md` with `mode: redesign`, approved, with a Preserve / Replace / Migration section. Often preceded by a short AUDIT.

## 1. Inspect what exists (read-only)
- Everything in `audit.md` step 2 (screenshots, reconstructed system).
- Inventory: screens, shared components and how many places use each, token or theme files, hardcoded values count, flows that must not change, brand marks.
- Decide with evidence what is worth keeping. Keep: anything users rely on, anything consistent and accessible, anything expensive to rebuild for little gain. Replace: inconsistent, inaccessible, dated chrome, one-off styling, components with missing states.

## 2. Ask (one round, max four, from `questions.md` REDESIGN)
What must survive, the reason for the redesign, migration appetite, two products to move toward and one to move away from.

## 3. Short audit first if there is none
Run the hierarchy, usability, a11y and consistency passes; this grounds the Preserve / Replace list in findings, not taste.

## 4. Directions (`directions.md`)
Two or three, each framed as "what changes for a user who already knows the product". Say what stays identical in every direction (flows, data, component behaviors). Recommend one. Offer a board on the busiest screen.

## 5. Iterate, then write the brief
Same loop as EXPLORE. The brief adds: Preserve, Replace (one reason each), migration order (tokens -> typography/spacing -> component states -> motion -> screens by traffic), and a "no behavior change except a11y fixes" line unless the user said behaviors may change.

## 6. Approve and hand off
On "approved": status flips, say `/design-builder` will migrate in the stated order and run the review loop per screen. Nothing in the code has changed yet.

## Never
- Redesign screen by screen without a token layer first.
- Drop a working feature, route, or accessibility affordance for aesthetics.
- Propose "polish the old look" when the user asked for a redesign, or a new world when they asked for polish.
