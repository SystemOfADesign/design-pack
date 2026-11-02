# Delegate report: Stageshow kit, examples, dependencies, licensing (2026-11-02)

Repo: `design-pack/repos/benjitaylor_skills/stageshow`

## 1. Architecture

**Stage** (`kit/stage.tsx`)
- Design size: `width`/`height` props; outer `.ss-fit` div sized `height: designH * scale`, inner `.ss-stage` at design px with `transform: scale(s)` (`stage.tsx:567-583`). Scale = `min(fill ? 2 : 1, containerW / designW)` via ResizeObserver (`stage.tsx:192-205`); `data-ss-fill` / `data-ss-wide` ancestor attrs override policy (MutationObserver, `:211-214`).
- Compact: `compact={{ below, width, height }}` switches to second design when container < `below`; `layout` becomes `'compact'`, script restarts (`:96-97`, `:179-205`).
- Scene state: `initial`, children render fn `(state, rect, layout) => JSX` (`:81`). `rect(name)` returns rects of every `[data-target]`, remeasured after each commit (useLayoutEffect, max 4 passes/frame) and on `transitionend`/`animationend` (`:217-258`).
- Playback: `play: 'loop' | 'once' | 'hover'` (`:18`); hover degrades to `once` on `(hover: none)` (`:111`). Script runs only while IntersectionObserver says on-screen + tab visible (`:507-525`); each run gets its own `AbortController` -> `Act` (`:390-397`). Loop mode runs `checkSeam` in dev (`act.ts:664-669`) warning if end state != initial or cursor not at rest.
- Reduced motion/poster: `still = !script || reduced` (`:127`); state becomes `poster ?? initial`; cursor hidden unless `cursor.still`; `data-still` attr lets CSS skip tweens; `StillContext` makes motion parts settle (`reduced-motion.ts`).
- Look: `theme/palette/fidelity/greys/tokens/accent/ground` -> data attrs + inline `--ss-*` CSS vars on `.ss-stage` (`:567-583`); `LookContext` provided to children.
- Cursor: `cursor={{ at, kind, style, still, ripple, idle }}`; kind auto-follows `data-cursor` under pointer via `elementsFromPoint` hit-test (`act.ts:192-250`); idle fade after 4000 ms (`stage.tsx:424-470`).
- Virtual clock: `kit/clock.ts` wraps RAF/timers/CSS animations so recorder/playground can step frames deterministically.

**Act API** (`kit/act.ts:17-104`)

| Method | Semantics |
|---|---|
| `set(patch)` | Merge state, resolves after 2 frames painted, re-reads cursor kind |
| `put(patch)` | Same, no await (per-frame in drag) |
| `wait(ms)` | Timer / speed, abortable |
| `rect(name, {layout?})` | Target rect in stage px; `layout` ignores transforms |
| `caret(name, at)` | Char offset a selection reaches at point (OS semantics) |
| `center(name)` | Target center point |
| `move(to, {duration, path, onMove})` | Hand-like arc; hovered chain gets `data-hover` |
| `click(to?, {double, right})` | Move + press; `data-pressed` |
| `scroll(name, to, {duration, offset})` | Trackpad-style scroll of `.ss-scroll` area |
| `cursor(kind)` | Set cursor kind |
| `snap(patch, scope?)` | Patch with transitions off (stage or one target) |
| `key(combo)` | Show keycaps, resolves on key-up |
| `stagger(items, fn, gap=60)` | Staggered starts |
| `mark(name)` | `data-mark` on stage for film.mjs `--at` |
| `type(key, text, {interval=35})` | Char-by-char into string state key |
| `drag(to, onMove, {duration, cursor:'preserve', path})` | Press, dip to grab, arc, release; `onMove` runs in `flushSync` (`:373`, `:626`) |
| `place(to)` | Teleport cursor (behind cuts only) |
| `enter(to, {duration})` | Cursor arrives from nearest frame edge |
| `signal`, `layout` | Readonly |

**Measuring** (`kit/measure.ts`): `Target = string | Point | {at,x,y} | {wide,compact}` (`:12`). `rectOf` uses `getBoundingClientRect` divided by drawn scale (`:43-48`); `targetRectOf` strips the element's own scale transform so press/hover lifts do not shift overlays (`:54-67`); `layoutRectOf` walks `offsetLeft/Top` ignoring transforms (`:81-100`). Helpers `inset/box/between/contains`.

## 2. Looks system
- Types (`kit/looks.ts:8-13`): `Theme = light|dark|blueprint|glass`, `Palette = accent|mono`, `Fidelity = minimal|standard|realistic`, `Layout = wide|compact`. `useLook()` reads context.
- Token prefix `--ss-`; `LookTokens = { [`--ss-${string}`]: string }` (`stage.tsx:21`). Defined on `.ss-stage` in `kit/stage.css` inside `@layer stageshow` (`stage.css:6`). Groups (`references/looks.md:11-22`): surfaces (`canvas/surface/chrome/well/raised`), lines, text (`strong/text/faint`), icon, accent (`accent/accent-2/accent-soft/accent-text`), status (`success/danger/warning` + `-soft/-text`), type (`font/mono`), shape (`radius-sm/md/lg/window/pill`), density (`control` 34px, `row` 26px), shadows (`hero/satellite/ground/window/float/lift/card`), placeholder inks `--ss-ink-1..5`.
- Product mapping (`looks.md:40-48`): find product tokens (CSS vars / Tailwind config / theme.ts), map primary->`--ss-accent`, bg->`canvas/surface`, text scale->3 text tokens, borders->`--ss-line`, font->`--ss-font`, button radius->`-md`, input height->`--ss-control`; write `.look-acme .ss-stage { ... }` file or `<Stage tokens={{...}}>`.
- All kit CSS is layered so unlayered host CSS wins; unlayered guards revert host rules / Tailwind preflight (`stage.css:399-429`).

## 3. Motion parts (`kit/motion/`)
- **Collapse**: height open/close so siblings move with it; dims + dissolves content across travel (empty box never seen).
- **Roll**: text where only the changed span rolls (digits up/out, words whole), width eases.
- **Swap**: keyed crossfade where box eases between sizes (no snap).
- **Count**: number with per-digit rolling, last digit first, 3 decades so 9->0 rolls.
- **Connector**: line draws between two points (h/v/straight/step/curve), dots/arrows/labels.
- **Fly**: element carried on an arc from one measured rect to another; hidden until `go`.
- **Follow**: spring overlay that retargets with momentum (selection rings); `cellOf` sticky grid cells.
- **States**: control states stacked + crossfaded, box holds largest (nothing shifts).
- **Stream**: word-by-word reveal with all words pre-laid-out (no reflow); `mark` for changed runs.
- **Popover**: scale-from-origin + fade, never resizes while opening; freezes contents on close.
- **Scroll**: scroll area driven by `a.scroll`, macOS overlay bar, edge fades once scrolled.
- **Camera**: push-in on a layout rect and back, feathered edges.
- **Expand**: iOS card-to-screen open as one clipped element; `face` = app launch.

## 4. Frames and parts
- **Window** (`kit/window.tsx`, `window.css:42-58`): fixed 38px bar, 9px lights 6px apart, lights centered 19px from top/left; macOS 26 opt-ins (`lightsSize="large"` 12px/8px, `barSize="tall"` 64px, `sidebarStyle="floating"`); chromes `native|glass|terminal|card|hairline`.
- **Phone** (`phone.tsx:5-25`): iPhone 18 Pro / iOS 27 points: screen 402x874, status bar 62, island 95x37 at 14, home indicator 144x5; superellipse corner 71pt exp 2.31; Pixel 412x915; screen laid out at true points then scaled. 9 frames (`:36`).
- **Thread/Bubble** (`messages.tsx:6-9`): FLIP glide of older messages, tails on last-of-run, typing->message grows as one object. **Keyboard** (`ios.tsx`): iOS 27 keyboard at true points.
- **lucide-react** dependency: only `kit/parts/Icon.tsx:3` (31 icons); `Field` and `Chip` import `Icon` (so transitively). 15 example studies + `teaching/details.tsx`, `teaching/style.tsx` import it directly.

## 5. Gold example anatomy (hero-demo)
- Files: `index.tsx` (1 line re-export default), `HeroDemo.tsx` (338 LOC), `hero.css`, `icons.tsx` (product's own SVG paths).
- Catalog: `playground/catalog.ts:7` curated entry `{ id:'hero-demo', kind:'Scene' }`; `preview.tsx:6` loads via `import.meta.glob('../examples/*/index.tsx')`; unlisted dirs auto-appear under Kit (`catalog.ts:86-90`).
- Script beats (`HeroDemo.tsx:72-144`): open toolbar -> click Export + annotate -> drag-select sidebar icons + annotate -> I-beam select title + annotate -> copy -> terminal comes forward, `cmd+v` paste -> reset to `initial` for loop seam. `POSTER` = finished state (`:58`); `REST` cursor per layout (`:57`); compact 358x400 below 600 (`:148`).
- CSS scoping: `<Stage className="hd">` -> all rules under `.hd` with `hd-` class prefix (`hero.css:1-15`); `hero.css:1` comment "All rules belong to this example". `scripts/class-clash.mjs` checks class namespaces across examples so two demos on one page do not restyle each other; `check:css` runs with `--bundle teaching --bundle examples/looks` (`package.json`).

## 6. Dependencies
- Runtime (`package.json`): `react ^18.3.1`, `react-dom ^18.3.1`, `lucide-react 0.468.0` (pinned exact). Dev: vite 6, @vitejs/plugin-react, typescript 5.6, playwright-core, postcss; optional `portless`.
- Kit third-party imports: only `react` (43), `react-dom` (1, `flushSync` in `act.ts:1`), `lucide-react` (1). No animation lib confirmed (README:45 claims same).
- Portability concerns:
  - `kit/brands/index.ts` uses `new URL('./x.svg', import.meta.url).href`: works in Vite/webpack 5/Next; may need asset-loader config elsewhere.
  - CSS imported from TSX (`import './stage.css'`): Next app router fine, pages router requires global CSS workaround or bundling `stageshow.css`.
  - Uses `@layer`, `color-mix()`, `revert-layer`, CSS nesting in example CSS (`hero.css:8`): modern browsers only.
  - Browser APIs in effects (`matchMedia`, `ResizeObserver`, `document.fonts`); `window` guarded at `stage.tsx:111,140`; `use client` needed in Next.
  - tsconfig: `jsx: react-jsx`, `moduleResolution: bundler`, ES2022 target (`playground/tsconfig.json`).
- React 19 signals: no `forwardRef`, `defaultProps`, `findDOMNode`, legacy render; uses `createRoot`, `flushSync`, `useId`, `StrictMode`. README:45 "React 18 and later". Nothing found that blocks 19.

## 7. Licensing / provenance
- `LICENSE`: MIT, Benji Taylor 2026, covers source only.
- `NOTICE.md`: trademarks remain with owners; Radix look uses public values; `assets/app-icons.ts` icons NOT MIT: 6 base64 PNGs (`mail, calendar, testFlight, slack, figma, notion`) "taken from macOS app bundles" (`app-icons.ts:1-3`, 84 KB).
- `kit/brands/SOURCES.md`: 44 SVGs, per-file SHA-256; SVGL (MIT), payment-icons (Apache 2.0), cryptocurrency-icons (CC0), Simple Icons (CC0, bank hex applied), official Linear/Amex/Circle assets "subject to brand usage terms". License texts bundled.
- `examples/wikipedia/PHOTOS.md`: 2 Wikimedia CC0 photos, not under MIT, also used by finder/telegram/annotation studies.
- No bundled fonts; no runtime fetches; `Phone frame="photo"` bezel is caller-supplied.
- Vendoring flags: (a) strip or replace `assets/app-icons.ts` (Apple/Slack/Figma/Notion bundle artwork, no license) before redistributing in a marketplace; (b) Linear/Amex/USDC official marks carry brand terms, not OSS licenses; (c) product studies (Figma, Slack, Spotify etc) reproduce trade dress: fine as examples, risky as marketed assets; (d) hero-demo draws Claude Code branding (`HeroDemo.tsx:305-336`); (e) keep NOTICE.md + brand LICENSE-*.txt alongside.

## 8. Counts
- Examples: 69 dirs. Gold/Scene: 44 (42 unique ids in SKILL.md Gold table incl. `cursors`, `cursor-morph`, `cursor-resize`; catalog `curated` = 45 incl. `contrasts` teaching entry). Product studies: 16. Specimen/reference: 9.
- Teaching pairs: 53 lessons across `teaching/`: composition 13, scenes 9, style 8, contrasts motion cases 8, details 6, relationships 4, continuity 2, edges 2, text-settle 1 (+1 choreography lesson from `examples/choreography`).
- Kit LOC: 10,225 total (96 files): 5,509 ts/tsx + 4,716 css. Largest: `act.ts` 669, `stage.tsx` 611, `phone.tsx` 362.
