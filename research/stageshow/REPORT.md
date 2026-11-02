# Stageshow (benjitaylor/skills) research report

Date: 2026-11-02. Clone: `design-pack/repos/benjitaylor_skills` (shallow, commit 8020574 "Add Stageshow", 2026-10-30). Upstream: https://github.com/benjitaylor/skills (546 stars at clone time, author Benji Taylor; "how it works": https://benji.org/stageshow). Install command upstream: `npx skills add benjitaylor/skills --skill stageshow`.

## 1. What it is

- Skill + portable React/CSS kit + examples + verification scripts for **faux product UI illustrations**: stills, feature cards, bento tiles, cursor walkthrough loops, phone/notification stories. Marketing-page imagery, not real product UI.
- One idea (SKILL.md:12): reads as a real product, simplified to what the viewer needs, framed with intent, every motion has a cause. Five named failure modes: too much / wireframe / boxed / flat / bland.
- Authored, not automated: `a.click()` draws a cursor pressing, `a.set()` changes scene state. Output is a plain React component the host app imports.
- Author's stated limits: checks catch errors, not dull ideas; cannot draw illustration or photography; rules reflect the author's taste.

## 2. Layout of the skill folder (`stageshow/`)

| Part | Contents |
|---|---|
| `SKILL.md` (149 lines) | Philosophy, 7-step workflow, 10 recurring faults, Gold / Product-study / Specimen tables, kit summary |
| `references/` (15 docs, 1541 lines) | craft (still frame), framing (20 rules + 17 named layouts), motion (story, loops, pace, cursor, drags), teaching (53 bad/good lessons), looks (token mapping), bento, annotations, backgrounds (20 grounds), brands, choreography, products, kit (API), rehearse (how to film), verify (checklist + REHEARSAL.md template), review (fresh-eye protocol) |
| `kit/` (96 files, ~10.2k LOC: 5.5k ts/tsx + 4.7k css) | `Stage` + `Act` scripting; frames `Window`, `Phone` (iPhone 18 Pro / iOS 27 geometry), `Thread`/`Bubble`, `Keyboard`; 14 motion parts (`Collapse`, `Roll`, `Swap`, `Count`, `Connector`, `Fly`, `Follow`, `States`, `Stream`, `Popover`, `Scroll`, `Camera`, `Expand`); small parts (`Bar`, `Text`, `Row`, `Avatar`, `Menu`, `Chip`, `Field`, `Tabs`, `Chart`, `Code`, `BrandMark`...); `stageshow.css` tokens (`--ss-*`) in `@layer stageshow`; virtual clock |
| `examples/` (69) | 44 gold scenes, 16 product studies (Figma, Linear, Slack, Raycast, Finder, Spotify, Notion, Gmail, GCal, Docs, PowerPoint, Excel, Wikipedia, Telegram, iMessage), 9 specimen sheets |
| `teaching/` | 53 explicitly flawed/corrected pairs (composition 13, scenes 9, style 8, motion 8, details 6, relationships 4, continuity 2, edges 2, text-settle 1) |
| `scripts/` (12 .mjs) | film, film-checks (~50 DOM/CSS detectors), motion-watch, jumps, layout, class-clash, verification, browser, dev |
| `playground/` | Vite viewer: pause / step / slow / phone width 358 / reduced motion; `?capture=<id>` route for filming on native clocks |
| `assets/app-icons.ts` | 6 base64 PNG app icons lifted from macOS app bundles (NOT MIT) |
| `kit/brands/` | 44 SVG marks, per-file SHA-256 in SOURCES.md (SVGL MIT, payment-icons Apache-2.0, crypto icons CC0, Simple Icons CC0, official Linear / Amex / Circle under brand terms) |

## 3. Architecture

- **Stage** (`kit/stage.tsx`): design-size canvas scaled to fit container; `compact` is a second design under a breakpoint (redesign at 358, not a squeeze); scene state passed to a render function with `rect(name)` measuring every `[data-target]`; `play: loop | once | hover`; runs only on-screen + visible tab; reduced motion or no script shows `poster` state.
- **Act API** (`kit/act.ts`): `set put wait rect caret center move click scroll cursor snap key stagger mark type drag place enter`. `data-cursor` on elements auto-switches cursor kind; `mark()` sets `data-mark` the film script can wait on; dev-mode loop seam check warns if end state differs from initial.
- **Looks** (`kit/looks.ts`, `references/looks.md`): `Theme light|dark|blueprint|glass`, `Palette accent|mono`, `Fidelity minimal|standard|realistic`, `Layout wide|compact`. Map a product's tokens (primary -> `--ss-accent`, bg -> canvas/surface, font, radius, control height) into a `.look-acme .ss-stage {}` block or `<Stage tokens>`. Kit CSS is layered so unlayered host CSS wins.
- **Workflow** (SKILL.md:32-40): medium + place -> look -> story (3-5 beats, 10-16 s) -> copy the closest gold example and film it first -> screen (word budget 3-7 real strings, `Bar` filler elsewhere) -> choreograph -> rehearse (poster first, contact sheets at wide and 390, gate, fresh-eye review, `REHEARSAL.md` handover).

## 4. Verification / self-filming

- `film.mjs <url> --select --gate | --still | --states | --width 390 | --reduced | --dark | --slow | --hover | --zoom | --report`. Playwright-core + locally installed Chrome (`CHROME_PATH` override; never downloads a browser). Shoots a contact sheet (36 frames every 500 ms by default), injects ~50 per-frame DOM/CSS detectors plus a motion watcher.
- `--gate` = regex over the "never intentional" lines (framing, cut by the crop, tight stack, loose list, empty pane, fat row, emoji icon, kit override, uneven inset/padding/gutters, tight control, invented mark, anchor drift, spills its slot...) plus console `selection drift`. Any hit -> `rehearsal failed`, exit 1. Gate deliberately ignores motion lines (`jump`, `vanishes with no exit`, `settle snap`) and coverage; docs say passing is necessary, not sufficient.
- `jumps.mjs`: rAF geometry recorder; flags one-frame jumps, sibling drift, popover anchor drift. `layout.mjs`: single-snapshot box-fit audit of any page (works outside a Stage). `class-clash.mjs`: PostCSS static check that example classes do not collide across files.
- Correction to a common assumption: filming does NOT use the virtual clock. `?capture=` keeps native timers; only the viewer iframe installs `installVirtualClock` for pause/step.
- Portability: `film.mjs` and `jumps.mjs` require `.ss-stage` / `.ss-fit` in the top document, so they are not a general product-UI gate. `layout.mjs` and `class-clash.mjs` are host-agnostic.
- Handover: `REHEARSAL.md` beside the component (gold copied, beats, widths/states captured, film lines and responses, assumptions, unresolved, not checked). `review.md` is a fresh-eye protocol: reviewer gets frames + brief + gold still only, never the builder's notes, and answers "could this be any product?" first.

## 5. Verified on this machine (2026-11-02, Node 26.4, pnpm 10.30, Chrome present)

| Step | Result |
|---|---|
| `pnpm install` | ok (esbuild build script ignored by pnpm; harmless) |
| `pnpm run typecheck` | clean |
| `pnpm run check:css` | clean, 81 CSS files |
| `node scripts/dev.mjs` | portless -> http://stageshow.localhost:1355 (vite on 4870) |
| film `static-card --gate` | rehearsal passed (1 non-gate `lopsided` line) |
| film `payout-flow --gate` | rehearsal passed (motion lines reported, not gated) |
| film `hero-demo --gate` (wide and 390) | **rehearsal failed**: 6 / 8 never-intentional lines (`tight control` Add button 6px under field, `selection drift` warnings) plus caret jumps, dashed edge crawl, selection vanishes with no exit |
| film `ai-chat --gate` | **rehearsal failed**: 1 line (`uneven inset` on window bar) |

Shots and report JSON saved in `design-pack/research/stageshow/` (`hero-demo-still.png`, `hero-demo-poster.png`, `hero-demo-sheet.png`, `hero-demo-390.png`, `static-card-*`, `payout-flow-sheet.png`, `ai-chat-sheet.png`, `hero-demo-report.json`).

Take-away: the author's own gold examples do not all pass the author's own gate as shipped. Either the detectors drifted after the examples were finalized, or thresholds are environment-sensitive. Treat `--gate` as a linter with false positives, and expect agents following SKILL.md literally to loop on gold-example failures they did not cause.

## 6. Dependencies and licensing

- Runtime: `react ^18.3.1`, `react-dom ^18.3.1`, `lucide-react 0.468.0` (pinned exact; used only by `kit/parts/Icon.tsx`, transitively `Field` and `Chip`, plus 15 product studies). No animation library. React 19: no blocking patterns found; README says 18 and later.
- Dev: vite 6, typescript 5.6, playwright-core ~1.48, postcss; optional portless. Node >= 20.19.
- Portability into a host app: components import their own CSS (fine in Vite / Next app router; pages router needs `stageshow.css` global import); `new URL(..., import.meta.url)` for brand SVGs; `@layer`, `color-mix()`, `revert-layer`, CSS nesting (modern browsers only); needs `use client` in Next.
- MIT covers source only. Excluded: `assets/app-icons.ts` (Apple Mail/Calendar/TestFlight, Slack, Figma, Notion icons from app bundles, no license), official Linear / Amex / Circle marks (brand terms), two CC0 Wikimedia photos (`examples/wikipedia/PHOTOS.md`). Product studies reproduce trade dress and `hero-demo` draws Claude Code branding. NOTICE.md explicitly disclaims trademark rights.

## 7. Strengths

- The doctrine is specific and testable: numeric framing rules, a word budget, loop and poster rules, 53 bad/good pairs. This is the part most skills lack.
- Gold-first workflow (film the closest gold, copy its folder, swap look and content) is a strong anti-slop control.
- Kit solves the frame-level problems a model gets wrong by hand: digit rolls, retained-track swaps, carried rows, FLIP threads, true iPhone geometry, cursor morphs.
- Filming closes the loop with evidence (contact sheets at two widths, states sheet, reduced-motion poster) rather than self-assessment.
- Clean separation: skill text, kit, examples, teaching, scripts, playground. `read`-only use of the doctrine needs no install.

## 8. Limitations

- Narrow domain: marketing illustrations of products. Not a product-UI design skill, not an audit skill, no a11y, no copy, no design-system work.
- Gate false positives on shipped gold examples (section 5). Motion faults are reported but not gated; the docs insist a human watches playback.
- Scripts need Chrome + playwright-core + a Vite-served page with `.ss-stage`; nothing works against a static PNG or a Figma file.
- Heavy: 69 examples, 10k LOC kit, 4.6 MB clone. The playground is a dev dependency, not part of a host app.
- Conflicts with design-pack's builder rules (next section).
- Single commit, two days old, one author; no issue history or community fixes yet.

## 9. Fit with design-pack / design-director / design-builder

Overlap matrix (design-pack equivalents checked in `catalog.json`, repos, and installed plugins):

| Stageshow capability | design-pack today |
|---|---|
| Faux product UI still | None with a kit. taste-skill imagery doctrine only says "real fragment in HTML, `data-ui`" |
| Animated cursor walkthrough | None. `animate`, `emil-design-eng`, `prototype` target real product motion |
| Bento feature grid | None (taste-skill lists bento as a generic tell) |
| Product-look token mapping into a stage | None (`design-tokens`, `create-design-md` are for the product itself) |
| Motion parts (`Roll`, `Fly`, `Collapse`, `Count`) | Doctrine only (`motion-design`, `design-motion-principles`, `transitions.dev`), no primitives |
| Film-and-gate verification | Partial: plugin87 `gate`/`design-qa`, `verify_responsive.mjs`, gstack `design-review` screenshots; nothing samples motion per frame |
| Teaching bad/good pairs | None (closest: kylezantos anti-slop list, taste-skill `tells.md`) |
| Brand mark registry, backgrounds catalog | None |

Complementary: Stageshow fills the "Persuade surface imagery" cell (hero, feature card, bento tile, docs hero, demo loop) which the SKILLS.md grid currently has no specialist for. design-pack covers everything Stageshow does not: real product UI, 8 states, audits, a11y, copy, tokens, page composition around the illustration. `anatomy` (same author, already installed) covers isometric explainers with the same filming philosophy; no overlap between the two.

Conflicts to resolve explicitly (otherwise builder review passes will flag every stage):

- **Filler**: builder forbids placeholder copy and runs worst-case data; Stageshow is built on `Bar` filler and fixed fake data. Exempt `.ss-stage` subtrees (same idea as taste-skill `data-ui`).
- **Readability / a11y**: foundations want body >= 16px and real roles; stage text is 11-15px and controls are divs. Mark stages `role="img"` + `aria-hidden` content and exempt from a11y, copy, worst-case and generic-tells passes.
- **Device frames and bento**: taste-skill says no browser chrome or phone frames and warns on bento; Stageshow's `Window`/`Phone`/bento are the product. Decide per brief, by surface type.
- **Motion timing**: builder's 150-250 ms feedback rule applies to real controls; Stageshow storytelling arrivals run 0.8-1 s while its own feedback stays fast. Exempt stage code from the motion review pass.
- **Hardcode lint**: `--ss-*` tokens are a consumer layer; `lint_hardcodes.py` must skip `.ss-stage`.
- **Boundaries**: director never edits code; Stageshow writes React + `REHEARSAL.md` into the host and wants a Vite/Chrome loop. It belongs on the builder side only.

## 10. Recommendation

Incorporate as a vendored specialist, keep it separate from the orchestrators' core, do not fork the kit.

1. **Catalog it** (read-by-path, no install needed): add `benjitaylor_skills` to `CLONED` and `'stageshow': (S, G)` to `TAG` in `research/build-skills-grid.py`; append `benjitaylor/skills` to `research/clone-list.txt`; rerun the grid script so `skills.py find stageshow` resolves to `read repos/benjitaylor_skills/stageshow/SKILL.md`.
2. **Route to it**: new rows in `skills/design-director/reference/modes/route.md` for "hero illustration / product shot / demo gif / cursor walkthrough / feature-card or bento imagery / fake UI for a landing page" -> `stageshow`; keep `anatomy` for isometric explainers and `banner-design` for raster banners. Add `stageshow` to the playbook's consult-marketing section and a `build: product imagery` section; add an "Imagery: still | demo, gold example, widths" row to the brief template.
3. **Builder hook**: optional "Imagery" phase for Persuade surfaces whose done-rule is `film.mjs --gate` passing at wide, 390 and `--states` plus a `REHEARSAL.md`; add a review pass "Illustration" (measured gate + judged fresh-eye from `review.md`); exempt `.ss-stage` subtrees from the filler, a11y, worst-case, motion-timing and hardcode passes as listed in section 9.
4. **Borrow doctrine, not just the tool**: the craft Type/Spacing/Icons/Color sections, the 18 motion pairs, the 8 style/slop pairs and the choreography timing table are general UI wisdom; reference them from the builder's motion and polish phases and from the generic-tells pass.
5. **Install as a Claude Code skill only when actually producing imagery**: `npx skills add benjitaylor/skills --skill stageshow` into the target project (or symlink `repos/benjitaylor_skills/stageshow` into `~/.claude/skills/stageshow` for `invoke`). The playground deps (Vite, playwright-core, Chrome) are per-project dev deps and should not go into `~/.claude/skills`.
6. **If it ever ships inside the SystemOfADesign marketplace**: vendor the folder with LICENSE + NOTICE.md + `kit/brands/SOURCES.md` and the brand license texts; strip or replace `assets/app-icons.ts`; drop or clearly label the product studies and the Claude Code artwork in `hero-demo`; pin `lucide-react 0.468.0`. Nothing is packaged yet; that is a later call.
7. **Known caveat to document in the pack**: the author's `hero-demo` and `ai-chat` fail the shipped gate on this machine. When an agent copies a gold example and the gate fails before any edits, that is upstream, not the agent. Worth an upstream issue once the repo accepts them.

## 11. Delegate reports (raw, verbatim)

Three Opus-class delegates produced the underlying detail; their full reports are saved as `delegate-scripts.md`, `delegate-kit.md`, `delegate-overlap.md` in this folder.
