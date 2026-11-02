# Generating directions people can choose between

A direction is a different idea, not a different color. Two directions that share mode, composition and type are one direction.

## How many
- Two or three. One if the brief pins the world already (existing brand, named reference, Operate-mode tool with a strong incumbent system) and say why only one.
- Never four. Choice fatigue for a non-designer.

## Make them genuinely distinct
Vary at least three of: surface mode emphasis, composition (asymmetric editorial vs grid vs single column), type (serif / sans / mono, large-contrast vs flat scale), color temperature and amount, density, motion depth, shape language (sharp / soft), imagery policy. Each direction gets a name a non-designer can repeat ("Quiet instrument", "Warm notebook", "Black box").

## Each direction answers, in plain words
1. How it feels in one sentence.
2. What you notice first.
3. Who it suits and who it does not.
4. The risk.
5. Closest products you know (2-3).
6. The table: type, color, density, shape, motion, layout, imagery.
7. Foundations are identical across directions; say so once, not per direction.

## Recommend one
State which and why in two sentences. The user may overrule; do not re-litigate, do not blend two directions into a generic middle.

## Show it when words are not enough
Offer a direction board: the same real screen (the one with the lead task) rendered once per direction.
- Preferred: `design-shotgun` (comparison board + structured feedback) or `impeccable generate <n> <element>` in the live browser.
- Fallback without a running app: one static HTML file per direction under `.design/directions/<slug>.html` built with `design-html`, using real copy and realistic data, then open them. Never product source; these are throwaway.
- After the user reacts, map their words through `plain-language.md` (feedback vocabulary) and revise the direction, not the board.

## Iteration loop
1. Present directions (text table; board if asked or if the user hesitates).
2. User reacts: pick / push back / "another one".
3. Push back -> adjust within the direction. "Another" -> a new idea, retire the weakest.
4. Repeat until the user says it is right. Then write the brief with status `draft`, read it back in three sentences, and ask for the word "approved".
5. Only an approved brief goes to `design-builder`.
