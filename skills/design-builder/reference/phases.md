# Build phases

Run in order. Skip a phase only when the brief makes it empty (e.g. "motion: none") and say so. Specialist names resolve via the playbook "build:" sections; primary first.

| # | Phase | Do | Specialists | Done when |
|---|---|---|---|---|
| 0 | Preflight | Read brief + DESIGN.md/PRODUCT.md. Inventory framework, styling, component lib, token files, shared components and their usage counts, tests. Run app, baseline screenshots to `.design/shots/before/`. Run tests once. | `create-design-md` (read-only scan), `impeccable` context | inventory written to `.design/build-log.md`; baseline shots exist or "app does not run" recorded |
| 1 | Foundations and tokens | Build or extend the token layer from the brief's direction table: primitives -> semantic -> component. Color must pass contrast before it exists. Type scale, spacing scale, radii, shadows, motion durations/easings, breakpoints. Wire tokens into the stack (CSS vars / Tailwind theme / platform). Redesign: migrate existing values to tokens; `migrate-design-system`. | `design-tokens`, `token-build`, `design-system`, `impeccable extract`, `web-typography` | token file exists; `validate_tokens.py` + `validate_contrast.py` pass (measured) or "kit absent" recorded; no new hardcodes in files you touched |
| 2 | Structure and layout | Per in-scope surface: lead element first, then grouping, grid, max-width, section composition per the direction. Mobile base, widen with min-width. Apply the surface's mode (Operate: scanability; Persuade: composition). | `impeccable layout` (existing), `design-screen` (new), `interface-design`, `design-html`, `data-dashboard` | each surface has one clear lead at phone and desktop widths (judged, screenshot) |
| 3 | Components and states | Shared components get all eight states, token-only styling, keyboard and focus. Compose, do not fork. Destructive = danger variant + confirm. | `design-component`, `shadcn`, `vercel-composition-patterns`, `design-doctrine`, reference repos `radix-ui_primitives` `emilkowalski_vaul` `emilkowalski_sonner` `dip_cmdk` | every interactive element in scope has the eight states; keyboard reaches everything |
| 4 | Typography | Apply the scale and measure; headings 2.5x+ body on Persuade, flatter on Operate; tabular numerals where numbers align. | `impeccable typeset`, `web-typography` | body >= 16px, measure 45-75ch, one family per role (measured where possible) |
| 5 | Copy | Labels say the concrete thing; errors say what to do next; empty states say what will appear and how to start. No filler. | `impeccable clarify`, `ux-copy`, `ux-writing` | every empty / error state in scope has real copy |
| 6 | Motion | Only what the brief's motion row allows. Purpose first: feedback, continuity, orientation. Composite-only properties, 150-250ms for feedback, interruptible, reduced-motion honored. | `animate`, `emil-design-eng`, `apple-design`, `animation-performance`, `impeccable animate` | `review-animations` pass has no Major findings |
| 7 | Responsive | Narrowest width in the brief survives with no horizontal overflow; touch targets 24px+ (44 on native); density adapts. | `impeccable adapt`, `mobile-native` | screenshots at floor width and desktop; `verify_responsive.mjs` if kit + browser present |
| 8 | Accessibility | Labels, roles, landmarks, focus order, contrast, reduced motion, form errors announced. | `fixing-accessibility`, `a11y-audit`, `accessibility-review`, `web-design-guidelines` | axe (or equivalent) 0 violations measured, or "not run" with reason |
| 9 | Polish and harden | Deslop spacing/hierarchy; worst-case data; first-run and empty states; i18n length; error paths. | `baseline-ui`, `impeccable polish` / `harden` / `onboard`, `break-ui` | `break-ui` report has fixes applied; nothing truncates silently |
| 10 | Record | DESIGN.md from the shipped code; brief status `built`. | `impeccable document`, `create-design-md` | DESIGN.md matches the code (judged) |

Then `review-loop.md`.

## Redesign runs

Migration order from the brief: tokens -> typography/spacing -> component states -> motion -> screens by traffic. One shared theme; every page consumes it. After each screen migrates, smoke-test its flows and compare before/after shots. Nothing is "done" while two pages run on different palettes.

## Fix runs (from an audit)

Group accepted findings by foundation. Route each group to the Fix specialist in the playbook (`audit:` section's counterpart under `build:`). Systemic findings (consistency, tokens) are fixed at the token or component layer, never per page. Re-run only the passes that produced the findings.
