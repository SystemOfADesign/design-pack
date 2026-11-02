# Delegate report: Stageshow references vs design-pack (2026-11-02)

Paths: `SS = design-pack/repos/benjitaylor_skills/stageshow`, `DP = design-pack`.

Summary: Stageshow is a self-contained faux-product-UI illustration system (React kit + doctrine + film-based verification) that design-pack has no equivalent for; its still-frame craft and motion-pair rules are reusable general UI wisdom, while framing/story/cursor/bento/filming are marketing-specific. Integration needs one TAG entry, one CLONED entry, route/playbook rows, and explicit exemptions in builder passes (filler bars, a11y, 16px body).

## 1. Stageshow philosophy distilled

- One idea: reads as a real product, simplified to what the viewer needs, framed with intent, every motion has a cause (`SS/SKILL.md:12`). Five failure modes: too much / wireframe / boxed / flat / bland (`:14-20`). Authored illustration, not automation: `a.click()` draws a cursor pressing (`:24`).
- Workflow 7 steps: medium + place, look, story, copy a gold example, screen, choreograph, rehearse (`:32-40`); 10 recurring faults (`:42-53`); 45 gold examples (`:61-104`).
- Restraint word budget: count real strings, 3-7; rest is `Bar` (`references/craft.md:9`); word budget is not an element budget (`:10`); bars never where eye lands (`:12`); one big number (`:21`); say it once (`:24`); no sparkle/purple for AI (`:97`); no invented logo (`:98`); icons from one set, one stroke, one size (`:84-89`); 11-15px UI text, never 7px (`:44`); faux titles are `div`, never `h1-h6` (`:48`).
- Framing rules 1-20 (`references/framing.md:7-26`): one hero + <=2 satellites; crop only filler (4); crop 10-40% of hero off stage, hero fills >=2/3 width and bleeds (5); satellites straddle half outside (7); one gutter (10); no dead corners (15); two satellites = two kinds (17). Layout table, 17 named layouts (`:32-50`): Pinned bottom bleed, Corner bleed, Stage with gutters, Satellite focus, Wide hero, Row of windows, Device pair, Many of one, Fade crop, Close-up, Panel over product, Overlapping windows, Stacked cards, Opposite corners, Tilted stack, Corner chip, Monochrome row. Page is the ground: no plate (`:85`); `compact` is a redesign at 358, not a squeeze (`:87`).
- Story shapes (`references/motion.md:22-24`): how it feels to use / a flow / what the system does. 10-16s loop (`:26`), 3-5 beats to a payoff (`:27`), poster = the frame most people see, never mid-change (`:37`). Loop rules (`:41-51`): reset removes what loop added as one thing; every reset has a seen cause or is invisible; never play navigation backwards; data never rewinds in view; payoff holds 2s; nothing still >3s. Pace: two curves (`:55`), feedback stays product-fast, only storytelling slows (`:58`), stagger 40-80ms (`:61`). Cursor rules (`:117-126`): no stand-in halos; `data-cursor` decides kind; never covers words it clicks; morphs, never pops; every move explained; keys shown via `act.key`.
- Teaching pairs (`references/teaching.md`): 18 motion pairs (`:11-30`), 13 still UI details (`:40-56`), 9 whole-scene (`:58-70`), 8 style/slop (`:72-83`: purple slop, tiny text, glow, caps, invented icons, AI shorthand, onion skin), 6 details (`:101-110`).
- General UI wisdom (portable to real product work): craft Type/Spacing/Icons/Color sections (`craft.md:40-118`: optical centering via `text-box: trim-both`, nested radius = inner + padding, no near-tangents, one neutral family + accent, dark depth from lighter surface not shadow), all 18 motion teaching pairs, choreography timing table (`references/choreography.md:15-22`), style slop list.
- Marketing-illustration-specific: word budget + bars, framing/crop/satellites, layout table, story/loop/poster/cursor, bento rules, brand marks, backgrounds, product studies, film gate lines.

## 2. design-pack and its orchestrators

- Pack = study clones (45 repos, `DP/research/clone-list.txt`) + two vendored orchestrators (`DP/README.md:17-18`).
- `design-director` (`DP/skills/design-director/SKILL.md`): never edits product source, writes only `.design/` (`:13`); modes EXPLORE/AUDIT/REDESIGN/ROUTE + hand-off/bypass (`:24-31`); consults playbook sections silently (`:48`); outputs brief/audit (`:51`). ROUTE = symptom table (`reference/modes/route.md:8-31`), one message then action (`:34-38`).
- `design-builder` (`DP/skills/design-builder/SKILL.md`): phases 0-10 (`reference/phases.md:7-17`: tokens, layout, components/8 states, type, copy, motion, responsive, a11y, polish, record), then review loop of 9 passes (`reference/review-loop.md:9-17`), max 3 rounds (`:45`), measured vs judged, SKIPPED is not a pass (`SKILL.md:34`).
- `skills.py` resolution: installed `~/.claude/skills` -> plugin cache -> sibling `skills/<name>` -> catalog `paths` under pack root, else `missing` (`DP/skills/design-director/scripts/skills.py:9-13, 59-74`); `phase` greps playbook `###` sections for backticked names in catalog (`:111-123`).
- Catalog: 111 skills (`catalog.json`), layers x modes grid (`DP/research/build-skills-grid.py:23-24`); a SKILL.md only enters if its name is in `TAG` (`:27`, skipped otherwise `:73`) and its repo is in `CLONED` (`:10-13`). Playbook sections: consult marketing (`playbook.md:23-27`), consult motion (`:38-41`), build motion (`:146-150`), build polish (`:160-164`), gates (`:170-172`).

## 3. Overlap matrix

| Stageshow capability | design-pack equivalent |
|---|---|
| Faux UI still | Partial, doctrine only: `taste-skill` imagery section 7 "real fragment in HTML, `data-ui`" (`~/.claude/plugins/cache/taste-skill/.../references/imagery.md:229-240`); `image-to-code` (plugin87) is screenshot->code, not illustration. No kit, no framing rules |
| Animated cursor demo | None. `animate`/`emil-design-eng`/`prototype` target real product motion, not authored walkthroughs |
| Bento planning | None; taste-skill warns bento as a tell (`references/tells.md:44`) |
| Product-look token mapping (`looks.md:46-52`) | Analog: `create-design-md`, `design-tokens`; nothing maps to a stage kit |
| Motion choreography parts (`Roll`,`Fly`,`Collapse`,`Count`) | Doctrine only: `motion-design` (Lottie choreography), `design-motion-principles`, `transitions-dev` recipes; no retained-track primitives |
| Filming/gate verification (`film.mjs`, `rehearse.md:54-78` never-intentional lines) | Partial: plugin87 `gate`/`design-qa`, `verify_responsive.mjs` (`playbook.md:100,171`); gstack `design-review` screenshots. None samples motion frame-by-frame |
| Teaching pairs | None (closest: kylezantos anti-slop checklist, taste-skill `tells.md`) |
| Brand marks registry (`brands.md:21-26`) | None; `brand-identity`/`brandkit` make own brand |
| Backgrounds catalog (`backgrounds.md`, 20 grounds) | Partial: taste-skill palette/imagery, `impeccable colorize` |

Sibling note: `anatomy` (Benji's isometric-figure skill) is already installed and cataloged (Screens/pages x Generate); no UI-illustration overlap, same filming philosophy.

## 4. Complementary value

- Stageshow fills: Persuade-page product imagery (hero, feature card, bento tile), demo loops/gifs, docs heroes, device/phone stories, a measured motion gate. SKILLS.md gaps list has no such cell; it sits in the crowded Screens/pages x Generate (`DP/SKILLS.md:50`) but nothing there does this.
- design-pack covers what Stageshow does not: real product UI (`interface-design`, 8 states), audits (`review-loop.md`), a11y (`fixing-accessibility`), copy (`ux-copy`), tokens/system (`design-tokens`), product fit (`jobs-to-be-done`), page composition around the illustration (`design-taste-frontend`).

## 5. Conflicts

- Filler: builder "no filler copy, no placeholder numbers shipped as real" (`design-builder/SKILL.md:33`); copy pass blocks on "placeholder or filler shipped" (`review-loop.md:17`); `break-ui` worst-case data (`:14`) vs Stageshow `Bar` filler and fixed fake data (`craft.md:9-12`). Needs a stage-subtree exemption (like taste-skill `data-ui`).
- Readability/a11y: foundations body >=16px (`foundations.md:10`) vs 11-15px UI text (`craft.md:44`); a11y phase labels/roles/keyboard (`phases.md:15`) vs decorative divs posing as buttons. Stageshow does honor reduced motion via `poster` (`motion.md:37`), aligning with `foundations.md:12`.
- Frames: taste-skill "no device mock-ups, no browser chrome" (`imagery.md:204`), "no laptop, no phone frame" (`:231`) vs Stageshow `Window`/`Phone` frames (`SKILL.md:142`); bento warned (`tells.md:44`) vs `bento.md`. Both agree: grey bars where eye lands are bad (`imagery.md:233` / `craft.md:12`), bleed off edges (`imagery.md:198` / `framing.md:11`).
- Motion timing: builder feedback 150-250ms (`phases.md:13`) and `review-animations` strictness vs Stageshow 0.8-1s storytelling arrivals (`motion.md:55`); Stageshow itself says feedback stays fast (`:58`), so exempt stage code from pass 5.
- Tokens: `--ss-*` kit tokens (`looks.md:11-22`) are a consumer layer; builder rule "never style with a value the token layer lacks" (`design-builder/SKILL.md:31`) satisfied only if looks map from semantic tokens, and `lint_hardcodes.py` must skip `.ss-stage`.
- Boundaries: director never edits code (`:13`); Stageshow writes React + `REHEARSAL.md` into the host and wants a copied `examples/<yours>/` loop (`SKILL.md:37`) plus node/playwright/Chrome (`rehearse.md:27`). Fits builder side only.

## 6. Integration options

- Catalog: add `'benjitaylor_skills'` to `CLONED` (`build-skills-grid.py:10-13`) and `'stageshow':(S,G)` to `TAG` (`:27`) (or `(B,G)` beside `banner-design`); append `benjitaylor/skills<TAB><stars><TAB>skills` to `clone-list.txt`; rerun script (`USAGE.md:112`). `skills.py find stageshow` then resolves `read repos/benjitaylor_skills/stageshow/SKILL.md`; symlink into `~/.claude/skills` for `invoke` (`USAGE.md:93-96`). Playground deps are not needed for `read`.
- Director ROUTE: new rows in `route.md:8-31`: "need a hero illustration / product shot / demo gif / cursor walkthrough / bento feature grid / fake UI for landing" -> `stageshow` (Generate, writes code; still vs animation decided by `SKILL.md:34`). Keep `anatomy` for isometric explainers, `banner-design` for raster banners.
- Playbook: add `stageshow` under "consult: marketing, landing, brand" (`playbook.md:23-27`) and a new `### build: product imagery (Persuade surfaces)` section listing `stageshow`, `anatomy`, `banner-design`; brief-template "Imagery / icons" row (`brief-template.md:37`) gains "product illustration: still|demo, gold example, widths".
- Builder phases: optional phase 2b "Imagery" for Persuade surfaces, done when `film.mjs --gate` prints `rehearsal passed` at wide + 390 + `--states` and `REHEARSAL.md` exists (`verify.md:7-10, 72-82`). Motion phase (`phases.md:13`) borrows `motion.md` loop/poster rules when brief motion = expressive. Polish phase (`:16`) can borrow `scripts/layout.mjs`, which checks ordinary UI outside a Stage (`rehearse.md:15-18`) as a measured layout gate; `film.mjs` only discovers `.ss-stage` (`rehearse.md:41`), so it is not a general product-UI gate.
- Review loop: add pass 10 "Illustration" (measured `--gate` + judged `review.md` fresh-eye, `review.md:11-25`), and exempt `.ss-stage` subtrees from passes 3/4/6/8 with `aria-hidden`/`role="img"`. Reuse the 8 style pairs (`teaching.md:72-83`) as inputs to pass 9 generic tells.
