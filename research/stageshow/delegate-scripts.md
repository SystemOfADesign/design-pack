# Delegate report: Stageshow verification tooling (2026-11-02)

Root: `design-pack/repos/benjitaylor_skills/stageshow`

## 1. Scripts

| Script | Purpose | Flags | Deps |
|---|---|---|---|
| `scripts/browser.mjs` | Shared `launch()`; dynamic-imports `playwright-core`, launches `channel: 'chrome'` or `CHROME_PATH` (l.13-15). Exit 2 with install hint if missing. Never downloads Chrome. | env `CHROME_PATH` | playwright-core, installed Chrome |
| `scripts/dev.mjs` | Starts Vite playground; on darwin/linux wraps via `portless stageshow <vite-shim>` (l.32) -> `http://stageshow.localhost:1355`. Windows runs Vite directly. | passthrough to vite | vite, portless (optional) |
| `scripts/verification.mjs` | Shared helpers: `visibleStages()` finds `.ss-fit, .ss-stage` (l.4); `watchStages()` sets `window.__ssVerification`, `__ssStageKey`, `data-ss-verification-stage`; `coverage()` marks inconclusive if <4 frames, short, gaps >1.6x median, median >40ms (l.55-60); `reportResult()` exit 2 incomplete / 1 strict+findings / 0 (l.70); `motionFindings()` adds `near-empty frames:` (l.95). | - | none |
| `scripts/class-clash.mjs` + `-core` | Static CSS: classes defined in >1 file without distinct scope root. `--bundle <dir>` groups one component's sheets; defaults `examples/ teaching/`. Skips `ss-*` classes (core l.97); CSS Modules isolated (l.100); `@scope`, nesting handled; `:is/:where` without root, escapes, `:global` -> `manual:` -> exit 2. | `--bundle`, `--help` | postcss |
| `scripts/layout.mjs` + `-core` | One-snapshot box-fit audit of any selector (default `body`). Rules: `control-block-fit` (core l.88), `control-edge-inset` (l.100), `container-block-inset` (l.129), `nested-composition-crop` (l.146). Moving geometry -> `deferred` -> inconclusive. | `--select --width --delay --report --screenshot --strict` | playwright |
| `scripts/jumps.mjs` + `-core` | rAF geometry recorder of every element in stage (stage px). `analyse()`: `jump:` (>2px and >3x neighbours' motion in one frame, l.106), `drift:` (sibling gap wobbles >=4 frames, l.169), `anchor drift:` (`ss-popover|menu|sheet` top moves while height changes, l.149). `contentChanges()` -> `manual: same-box content change`. | `--ms --width --select --report --strict` | playwright |
| `scripts/motion-watch.mjs` | Injected per-frame watcher. Lines: `hard edge:` (l.74), `steps in its box:` (l.118), `fly size:` (l.149,172), `handoff shift:` (l.290), `settle snap:` (l.311), `appears with no entrance:` (l.430), `vanishes with no exit:` (l.440), `dashed edge resizes:` (l.449), `lands on a transform:` (l.486), `appears, then moves:` (l.507), ink samples for `near-empty frames`. | - | none |
| `scripts/film-checks.mjs` | 1920 lines of per-shot DOM/CSS detectors, injected via `Function.toString()` (l.1908-1920) as `window.__ssFilmChecks`. `checkStage()` l.1764 runs ~50 detectors in fixed order. Lines: `clipped`, `uneven:`, `covers:`, `lopsided:`, `near-tangent:`, `unclipped:`, `tight lines:`, `double corner:`, `translucent icon:`, `skeleton ladder:`, `loose list:`, `tight control:`, `invented mark:`, `avatar alignment:`, `near aligned:`, `uneven inset:`, `mixed icons:`, `emoji icon:`, `fat row:`, `empty pane:`, `tight inset:`, `uneven padding:`, `uneven gutters:`, `tight stack:`/`loose stack:`, `kit override:`, `clipped glyph:`, `unit wrapped:`, `onion skin:`, `tight mark:`, `half-pixel glyph:`, `squeezed:`, `framing:` (many sub-cases l.1301-1675), `touching:`, `dark slab:`, `cut by the crop:`, `spills its slot:`, `small text:` (width<600). | - | none |
| `scripts/film.mjs` | Orchestrator. Opens page, injects instrumentation + checks + motion watcher, shoots contact sheet via in-browser HTML grid (l.644-658). Self-respawns as child (`FILM_CHILD`) up to 6x on Vite reload / `vite-error-overlay` (l.131-152, exit 3). `--slow` via CDP `Animation.setPlaybackRate` + `window.__stageshow.slow` (l.268-278); kit's Stage reads it (`kit/stage.tsx:144-146`). | `--out --every --count --delay --at --select --width --cols --zoom --scale --pad --reduced --dark --still --slow --hover --hover-for --leave-for --gate --states --states-for --report --strict --help` | playwright, Chrome |

## 2. Virtual clock, filming, gate

- `kit/clock.ts:installVirtualClock()` (l.82) replaces `setTimeout/setInterval/rAF/performance.now/Date` on `window`; time moves only on `step()`/`advance()`. Per step: fire due timers in order (each followed by `settle()` = 4 MessageChannel round-trips so React commits land, l.129-143), run one rAF round, then hold every CSS Animation at `playbackRate=0` and set `currentTime` by hand (l.160-190). Exposed at `window.__stageshow.clock`.
- `film.mjs` does NOT use the virtual clock. Only the viewer iframe (`?embed=`) installs it (`playground/main.tsx:21-32`); `?capture=` explicitly keeps native timers, RAF and CSS clocks (main.tsx:14-19). Filming uses real time + CDP slow-down. The viewer's `createPlayback` (playback.ts) drives it with real elapsed ms (`advance`, capped 100ms, l.74) or fixed `step()`; Pause/Step/speed via postMessage.
- Why `?capture`: viewer wraps scene in iframe; film refuses iframes (film.mjs:300) and needs `.ss-stage` in the top document.
- `--gate` (film.mjs:521-526): regex `NEVER` over findings: `framing|cut by the crop|tight stack|loose stack|tight mark|tight inset|skeleton ladder|onion skin|kit override|unit wrapped|clipped glyph|loose list|empty pane|fat row|emoji icon|anchor drift|uneven padding|mixed icons|tight control|invented mark|uneven inset|uneven gutters|avatar alignment|spills its slot` plus console `[stageshow] selection drift:` (kit/act.ts:632). Any hit -> `rehearsal failed`, exit 1; else prints `rehearsal passed (necessary, not sufficient...)`. Gate ignores coverage status, motion lines (`jump:`, `settle snap:`...), `touching:`, `near-tangent:`, `small text:`.
- Per-shot findings need >=2 frames unless `translucent|covers|framing|small text` (l.490).
- Docs' own limits (rehearse.md l.110): contact sheet misses one-frame flashes; tools cannot judge whether a morph/story/gesture is right; must watch playback, interruptions, reduced motion, offscreen return; playground Phone changes width not touch; l.107 "virtual clock proves geometry, not frame rate". `no-issues-detected` is not approval (l.47). Gate required at wide, 390, and `--states` (verify.md l.7-9).

## 3. Mechanics

- class-clash: PostCSS parse; expand nested/`@scope` selectors to full strings; strip `:not()/:has()`, attributes; class scope = first `.x`/`#x` anchor before the class in the selector (core l.98-100). Clash = same class name, different files, no shared `--bundle` owner, neither CSS-module, and scopes equal or one empty (l.119-124).
- layout-core: controls = `button, [role=button], [data-layout-control]` or class matching `btn|button` (l.34). Collect text rects (via Range) + svg/img/canvas; compare content height + padding + borders vs box height (l.85-90); edge inset asymmetry; padded containers' last-child bottom vs bottom padding; `.ss-window` crossing inner `.ss-stage` clip within `[data-crop]` tile.
- jumps-core: skips `[data-snap] [data-typing] .ss-caret...`, `.ss-cursor` glyphs, moving `.ss-camera` contents, non-painting wrappers, alpha<=0.02 (l.43-61). Late frames (>1.6x median) excluded.
- film-checks: all `getBoundingClientRect`/`getComputedStyle`; thresholds in stage px (scale = rect/offsetWidth). Heavy use of kit classes: `.ss-camera`, `.ss-window/.ss-phone` (hero), `.ss-bar`, `.ss-fly`, `.ss-roll/.ss-count`, `.ss-cursor/.ss-keys`, data attrs `data-crop data-snap data-typing data-target data-specimen data-fidelity data-receded data-zoomed data-lead data-unframed data-still data-placing data-mark`. `detectKitOverride` reads stylesheets, skips `/kit/|/playground/` by `data-vite-dev-id`/href (l.1006).

## 4. Handover + review

- `REHEARSAL.md` template (verify.md l.72-82): `Gold`, `Beats`, `Captured: widths <wide,390>, looks, states, reduced motion`, `Film: <gate line> -> <frame> -> <fix or why it stands>`, `Review: <reviewer list> -> <response>`, `Assumptions`, `Unresolved`, `Not checked`. Must state what was not watched (l.83).
- review.md protocol: reviewer gets only review.md, verify.md, `examples/`, URL, frames, one-line brief + gold still; never the builder's plan or REHEARSAL.md (l.3). First question: could this be any product? Judge from frames only; film missing frames yourself; ranked list framing > hierarchy > motion > polish; each item = frame file + one-line fix; "nothing" + frames listed if clean; builder's "intentional" calls re-judged (l.22); platform chrome is not a placeholder (l.26).

## 5. Portability

- Scripts are URL-agnostic (no hard-coded host/port; `stageshow.localhost:1355` appears only in README/dev.mjs via portless). `layout.mjs` and `class-clash.mjs` work on any page/CSS.
- `film.mjs`, `jumps.mjs` require `.ss-stage` (or `.ss-fit`) elements (verification.mjs:4; film.mjs:300-301 error otherwise). On a plain React app they find no stage and exit 2. `--select` only narrows within that.
- Other coupling: `window.__stageshow.slow/theme` read by kit Stage (slow works on CSS via CDP regardless); `--at`/`--states` need `data-mark` from `act.mark()`; `--zoom target:` needs `[data-target]`; `#example[data-example]` playground guard (film.mjs:192-196, 349-351); Vite-specific reload/overlay retries; `data-still`/`data-placing` waits.
- Many detectors are kit-class-tuned; on foreign DOM they would run but with reduced meaning (hero framing needs `.ss-window/.ss-phone`; anchor drift needs `ss-popover` class names).

## 6. Risk / robustness

- No network calls except the page URL; no Chrome download (fails loud with exit 2).
- Writes: `--out` (default `shots/film.png` relative to cwd), `--report`, `--screenshot`; `mkdirSync` recursive. Nothing else touched.
- film.mjs spawns itself synchronously up to 6 times, with `Atomics.wait` sleeps (l.142); exit 3 if page keeps reloading.
- Viewport auto-grows to doc height (l.390); sheets rendered via `setContent` with base64 PNGs; large `--count` = big memory.
- Virtual clock monkey-patches `Date`/`performance.now` globally in the embed iframe; string timer callbacks ignored (clock.ts:146).
- `--gate` passing is weak by design: ignores motion/coverage; docs insist on manual watch + fresh-eye review.
