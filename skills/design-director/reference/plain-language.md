# Plain language

The user may know nothing about design. Every recommendation is stated as what they will notice and why it matters to their users. Jargon is allowed once, glossed in the same sentence.

## Glossary (term -> what to say instead)

| Term | Say |
|---|---|
| Hierarchy | what the eye lands on first, second, third |
| Visual weight | how much something pulls the eye (size, boldness, color, space around it) |
| Design tokens | the named list of allowed colors, sizes and spaces, so every screen uses the same ones |
| Type scale | the fixed set of text sizes, so headings and body text relate on purpose |
| Measure | how many characters fit on one line of text |
| Leading | the space between lines of text |
| Contrast | how clearly text stands out from its background |
| Affordance | whether something looks like it can be clicked, dragged, typed into |
| Signifier | the hint that tells you what something does (underline, button shape, cursor) |
| Feedback | the screen's reaction when you do something |
| States | how a control looks when idle, hovered, pressed, focused, disabled, loading, empty, errored |
| Density | how much is packed into one screen |
| Whitespace | empty space used on purpose |
| Rhythm | spacing that repeats predictably down the page |
| Optical alignment | nudging things so they look lined up, even if the math says otherwise |
| Persuade / Operate / Read / Experience | the screen is for deciding / doing / understanding / being inside the work |
| Operate mode | screens people work in: calm, predictable, familiar patterns |
| Persuade mode | pages that sell: bolder, more distinct, earns attention |
| Heuristic evaluation | an expert checklist walk-through of the screens |
| WCAG / a11y | the accessibility standard: keyboard, screen readers, contrast, motion |
| Slop / generic tells | the patterns that make a screen look auto-generated: equal cards, everything centered, rainbow accents |
| Design system | the shared parts and rules every screen is built from |
| Semantic color | a color named for its job (danger, success, link) rather than its hue |
| Lead | the one thing on a screen that matters most |

## Feedback vocabulary (what the user says -> what to change)

| User says | Usually means | Levers to move |
|---|---|---|
| too corporate | safe blue/grey, uniform grid, stock-photo feel | warmer neutrals, one distinctive type choice, asymmetry, real content instead of filler, fewer boxes |
| too playful / not serious | bright palette, rounded everything, bouncy motion | tighter radii, restrained palette, settle the motion, more precise alignment |
| simpler | too many elements competing | one lead per screen, remove decoration, fewer type sizes, fewer colors, merge or hide secondary actions |
| too empty / boring | restraint read as absence | add one deliberate strong element (type, image, color block), not three |
| too busy / cluttered | no hierarchy, no spacing scale | group, align, add macro-whitespace between sections, demote secondary things |
| looks generic / AI-made | the banned defaults | break them: no equal card rows, off-black on warm-white, one accent, varied section composition |
| more premium / expensive | wants restraint and precision | more whitespace, larger size contrast between heading and body, fewer borders, considered motion, fewer colors |
| more modern | usually dated type or heavy chrome | update type, flatten chrome, lighter borders, better spacing; do not chase trends |
| hard to read | measure, size, contrast, leading | 16px+ body, 45-75ch lines, contrast 4.5:1, leading 1.4-1.6 |
| feels slow / clunky | missing feedback, layout shift, long animations | instant state change, skeletons, 150-250ms transitions, no shift after load |
| I want it to feel like X | a reference product | name the three things X does (type, density, motion) and adopt those, not its logo |
| show me another direction | the current direction is wrong in kind, not degree | change the idea (mode, metaphor, composition), not the color |
| make it pop | wants contrast | increase size contrast and whitespace first; color last |

## How to describe a direction to a non-designer

Four sentences, then a table. Example:

> Direction B, "Quiet instrument". It feels like a well-made tool, not a brochure. The first thing you see is the number you came for, big; everything else is smaller and grey until you need it. It suits people who open this ten times a day. The risk: it can feel plain on a marketing page, so the landing page would get its own treatment.

| Aspect | What you will notice |
|---|---|
| Type | one clean sans, headings barely larger than text, numbers in a tabular font |
| Color | warm grey surfaces, one blue for actions, red only for danger |
| Density | tight, lots on one screen, but grouped |
| Motion | almost none; things appear, they do not fly |
| Closest product you know | Linear, Stripe dashboard |

Always give a "closest product you know". It is the fastest way a non-designer understands a direction.
