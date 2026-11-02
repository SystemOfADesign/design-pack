# design-pack

Claude Code plugin marketplace from SystemOfADesign, plus the study pack it grew out of.

## Install

```sh
/plugin marketplace add SystemOfADesign/design-pack
/plugin install design-orchestrators@design-pack
/plugin install stageshow@design-pack
```

| Plugin | Skills | What |
|---|---|---|
| `design-orchestrators` | `design-director`, `design-builder` | Design direction and execution for people who are not designers. Director writes `.design/brief.md` or `.design/audit.md` and never edits product code; builder implements an approved brief in phases and runs review passes |
| `stageshow` | `stageshow` | Vendored copy of Benji Taylor's Stageshow (faux product UI illustrations, cursor demo loops, bento tiles, film-based verification). Pinned commit and licence notes in `plugins/stageshow/VENDORED.md` |

Clone: `git clone https://github.com/SystemOfADesign/design-pack.git`. The `repos/` study clones (1.8 GB) are not in the repo; re-create them from `research/clone-list.txt` with `git clone --depth 1`.

## Study pack

Study pack built from the Instagram reel **The Modern Designer's Knowledge Map** by Rajat Patel (@designwithrajatpatel), https://www.instagram.com/reels/DcTdh84K6uN/ (44 s, watched 2026-11-01 with the /watch skill, transcribed on the home DGX Spark).

The reel itself names **no GitHub repos, URLs, or tools**. It is a rapid-fire list of 15 concepts, 6 people and 2 org cultures, one hand-drawn card each, then a pitch to follow the account. Everything under `repos/` is therefore *inferred*: for every person and concept an Opus 5.5 delegate searched GitHub for the highest-starred repos that embody that philosophy, verified star counts with `gh api` on 2026-11-01, and the top picks were shallow-cloned here.

## Layout

| Path | What |
|---|---|
| `watch-report/report.md` | Filled /watch report: TL;DR, every card with timestamp, hook analysis, corrected transcript |
| `watch-report/frames/` | 5 hero frames + 24 card frames (`card_NN.jpg`, 2 fps pass at 768 px) |
| `watch-report/instagram-caption.txt` | Title, uploader, full caption text |
| `research/*.json` | One file per person / org / concept list; repos sorted by stars with `why`, license, pushed_at |
| `research/clone-list.txt` | Everything cloned: `full_name  stars  source` |
| `repos/<owner>_<name>/` | Shallow clones (`git clone --depth 1`), 45 repos, ~1.7 GB |
| `skills/design-director/` | Top-level entry for non-designers: explore / audit / redesign / route. Writes `.design/brief.md` or `.design/audit.md`; never edits product code. `reference/` holds the playbook, foundations, plain-language glossary, templates, `catalog.json`; `scripts/skills.py` resolves any specialist |
| `skills/design-builder/` | Execution orchestrator: implements an approved brief in phases, runs review passes, fixes findings, records DESIGN.md |
| `plugins/stageshow/` | Vendored Stageshow skill (`skills/stageshow/`), `VENDORED.md` with upstream commit and licence notes |
| `research/stageshow/` | Evaluation report, delegate notes and filmed stills from the 2026-11-02 review |
| `.claude-plugin/marketplace.json` | Marketplace manifest: `design-orchestrators` (source `./`) and `stageshow` (source `./plugins/stageshow`) |
| `SKILLS.md` | Layer x mode grid of every design skill (cloned + installed), gaps, duplicates, catalog |
| `USAGE.md` | Four scenarios (new app -> build, audit, redesign -> build, targeted specialist) plus the expert path |

## Transcript corrections

Whisper mis-heard several proper names; all were checked against the on-screen captions and cards.

| Heard | Actual |
|---|---|
| Data Ramps | **Dieter Rams** (person, card at 0:02) |
| Susan Care | Susan Kare |
| Paul Asher | Paula Scher |
| Boris Cherney | Boris Cherny |
| Rajak Patel | Rajat Patel |

`research/concepts.json` still contains a "Data ramps" (colour scales) entry from before the correction; it is annotated as a transcription error and kept as a bonus.

## Inventory from the video

**People** (in order shown): Dieter Rams (0:02), Susan Kare (0:07), Paula Scher (0:12), Emil Kowalski (0:17, X card: @emilkowalski, "Currently @linear, animations.dev", emilkowal.ski), Boris Cherny (0:22, card "Claude Code Creator"), Jordan Singer (0:25, card "Generative Interface Design"). Author: Rajat Patel.

**Org cultures**: Linear's design engineering culture (0:15), Notion's craft team (0:25).

**Concepts** (card titles): Semantic Token, Optical Alignment, Component API Design, Perceived Performance, Non-Deterministic Systems, Progressive Disclosure, OKLCH, Generative UI, Model Latency as a Design Constraint, Jobs To Be Done, Motion Choreography, Trust and Error States (of probabilistic systems), Design Debt. Caption adds: design engineering, AI for designers, systems thinking.

## Dieter Rams

Rams (Braun 1955-1997, Vitsoe) held that good design is 'Weniger, aber besser' -- less, but better: innovative, useful, aesthetic, understandable, unobtrusive, honest, long-lasting, thorough, environmentally friendly, and as little design as possible. His functionalist minimalism uses strict grids, honest materials, muted greys and whites with a single functional accent colour, and tactile dials and switches whose form explains their use. It directly shaped Apple's Jony Ive-era products and today's Teenage Engineering / Nothing industrial aesthetic.

Emulating repos:

| Repo | Stars | Cloned | Why |
|---|---|---|---|
| [dominikmartn/nothing-design-skill](https://github.com/dominikmartn/nothing-design-skill) | 2,849 | yes (not cloned) | Claude Code skill whose SKILL.md is explicitly grounded in Braun industrial design and Swiss typography: monochrome, typographic, restrained UI generation -- the most-starred living descendant of the Braun aesthetic (Rams cited via Braun, not by name). |
| [helloSystem/hello](https://github.com/helloSystem/hello) | 2,470 |  | FreeBSD desktop whose tagline is literally Rams' 'Less, but better!' -- applies unobtrusive, honest, simple design to an entire OS (last push 2024-07). |
| [zedr/dieter-rams-10-applied-to-software](https://github.com/zedr/dieter-rams-10-applied-to-software) | 434 | yes (not cloned) | Maps each of the Ten Principles of Good Design onto software engineering; canonical text reference (older: last push 2021-11, included as best Rams-specific match). |
| [cideM/yui](https://github.com/cideM/yui) | 144 |  | Vim/Neovim colorscheme explicitly inspired by Rams: near-monochrome palette with minimal accent, color only where it carries meaning. |
| [joe-bell/tenprinciples.design](https://github.com/joe-bell/tenprinciples.design) | 45 | yes (not cloned) | Typographic site presenting Rams' Ten Principles; grid-driven, restrained layout to study and reuse. |
| [Gayaya999/product-design-three-views](https://github.com/Gayaya999/product-design-three-views) | 42 |  | Industrial-design agent skill with a Braun mode (functional zoning, physical controls, restrained accent colour) for product concept renders. |
| [HermeticOrmus/design-mastery-claude-code](https://github.com/HermeticOrmus/design-mastery-claude-code) | 19 |  | Claude Code plugin teaching design via masters including Rams; systematic principle-driven workflows. |
| [sneed-and-feed/braun_rb-26](https://github.com/sneed-and-feed/braun_rb-26) | 16 |  | Audio reverb plugin with Braun/Rams-style hardware faceplate UI (tagged dieter-rams): dials, switches, one orange accent. |
| [sneed-and-feed/braun_as-42](https://github.com/sneed-and-feed/braun_as-42) | 8 |  | Companion synth plugin in the same Braun hardware idiom -- reference for tactile knob/switch UI. |
| [tr0drigues/TactileBar](https://github.com/tr0drigues/TactileBar) | 6 |  | macOS menu-bar instrument explicitly inspired by Rams/Braun and Teenage Engineering, citing 'Weniger, aber besser'; SwiftUI Canvas switches and gauges. |
| [stefanvanburen/rams](https://github.com/stefanvanburen/rams) | 6 |  | Minimal Neovim colorscheme named for Rams (Lua port of rams.vim, 16 stars, 2021); quiet palette, few accents. |
| [yangyue1974/rams-braun-ui](https://github.com/yangyue1974/rams-braun-ui) | 4 | yes (not cloned) | Agent Skill encoding a Braun-era Rams design system: tokens, hard rules and a forbidden list -- directly reusable in Claude Code. |
| [CodeInPas/BraunUI](https://github.com/CodeInPas/BraunUI) | 4 |  | Skeuomorphic component library (Lazarus/FPC) inspired by Rams' Braun products: knobs, faders, switches, LEDs -- reference for honest tactile controls. |

Skills / tools: yangyue1974/rams-braun-ui -- drop-in Rams/Braun Agent Skill for Claude Code (tokens + forbidden list); dominikmartn/nothing-design-skill -- Claude Code skill, Braun/TE-derived monochrome industrial UI; kevinpostal/dieter-rams-design-skill (0 stars) -- skill applying the 10 principles to software design; Nightingall/design-review-skills (0 stars) -- Claude skill: Dieter Rams product-judgement review; cipriantitire/tactile-modernism (1 star) -- agent skill: design UIs the way Braun made radios; benjaminsehl/omarchy-rams (0 stars) -- Omarchy desktop theme after Rams/Braun; ghaida/dieter-rams-vscode-theme (1 star) -- VS Code themes from Rams product palette; c-ehrlich/calculator (0 stars) -- React replica of Braun ET-55 calculator; LaravZ/calculator-ts -- ET66 clone

## Susan Kare

Kare designed the original Macintosh icons and bitmap fonts (Chicago, Geneva, Monaco) on a strict pixel grid, often 32x32 in 1-bit black and white, treating each pixel as a deliberate decision. Her icons rely on instantly readable real-world metaphors (trash can, watch, Happy Mac) so meaning survives extreme constraint. The result is friendly, human, legible design where clarity beats ornament.

Emulating repos:

| Repo | Stars | Cloned | Why |
|---|---|---|---|
| [piskelapp/piskel](https://github.com/piskelapp/piskel) | 12,937 |  | Browser grid editor for drawing icons pixel-by-pixel the way Kare did on graph paper and in the Mac icon editor. |
| [Orama-Interactive/Pixelorama](https://github.com/Orama-Interactive/Pixelorama) | 10,913 |  | Full pixel-art toolkit (palettes limited to 1-bit, grid, symmetry) for producing tiny constrained icon metaphors. |
| [felixrieseberg/macintosh.js](https://github.com/felixrieseberg/macintosh.js) | 8,512 |  | Runnable classic Mac OS to study Kare-lineage icons, Chicago menus and desktop metaphors in their native context. |
| [sakofchit/system.css](https://github.com/sakofchit/system.css) | 3,928 | yes (not cloned) | CSS design system recreating System 6/7 windows, buttons and Chicago-style type, i.e. Kare's 1-bit UI vocabulary for the web. |
| [the-moonwitch/Cozette](https://github.com/the-moonwitch/Cozette) | 3,866 |  | Modern bitmap font that proves legibility on a strict pixel grid, the same discipline behind Chicago/Geneva/Monaco. |
| [rektdeckard/departure-mono](https://github.com/rektdeckard/departure-mono) | 3,625 |  | Pixel-grid typeface usable as a web font today, applying Kare-style bitmap type to contemporary UI. |
| [mihaip/infinite-mac](https://github.com/mihaip/infinite-mac) | 1,653 |  | In-browser System 1 through Mac OS 9 emulation; the best reference for seeing Kare's original 1984 icons, fonts and Finder in place. |
| [robhagemans/hoard-of-bitfonts](https://github.com/robhagemans/hoard-of-bitfonts) | 1,494 |  | Large archive of historical bitmap fonts from classic platforms to study how letterforms survive at 8-12 px. |
| [ryokun6/ryos](https://github.com/ryokun6/ryos) | 1,280 |  | Web desktop recreating classic Mac OS/System 7 chrome and apps; a modern React take on Kare-era desktop metaphors. |
| [halfmage/pixelarticons](https://github.com/halfmage/pixelarticons) | 886 | yes (not cloned) | Consistent 24px pixel-grid icon set (SVG/React/font) applying Kare's clarity-at-tiny-size icon thinking to modern products. |
| [hackernoon/pixel-icon-library](https://github.com/hackernoon/pixel-icon-library) | 420 |  | Production pixel icon library with Kare-like bold, readable metaphors at 16-24px. |
| [KingDuane/Chicago-Kare](https://github.com/KingDuane/Chicago-Kare) | 350 | yes (not cloned) | Direct, faithful revival of Kare's own Chicago bitmap font; the most literal artifact of her work on GitHub. |
| [npjg/classic.css](https://github.com/npjg/classic.css) | 237 |  | Lightweight CSS for classic Mac windows, menus and controls; alternate take to system.css on the 1-bit Mac look. |
| [danmorgandesigns/classic-mac-elements](https://github.com/danmorgandesigns/classic-mac-elements) | 12 |  | Low-star but highly on-target: extracted System 1-7 and HyperCard 1-bit UI elements and icons for direct study. |

Skills / tools: Local Claude Code skills: frontend-design, design-html, impeccable, design-consultation (use with system.css + Chicago-Kare as constraints for a Kare-style UI); Piskel / Pixelorama (listed above) for 1-bit 32x32 icon drafting; Figma: View > Pixel Grid + Snap to Pixel Grid, 1-bit two-color palette, 32x32 / 16x16 frames; mihaip/infinite-mac web emulator (infinitemac.org) for side-by-side reference with originals; Not verified in this run: kreativekorp/bitsnpicas (bitmap font editor), FontForge, Aseprite

## Paula Scher

Paula Scher treats typography as image: letters are scaled, stacked, colliding and loud, carrying emotion and meaning before they are read. Her identities (The Public Theater, Citi, MoMA, Windows) are flexible typographic systems rather than fixed logos, and her hand-painted maps and environmental graphics make text itself the texture and architecture of a space.

Emulating repos:

| Repo | Stars | Cloned | Why |
|---|---|---|---|
| [chenglou/pretext](https://github.com/chenglou/pretext) | 50,980 | yes (not cloned) | Per-line text measurement/layout lets you flow type into arbitrary shapes, the core mechanic behind Scher-style text-as-texture typographic maps. |
| [greensock/GSAP](https://github.com/greensock/GSAP) | 30,014 | yes (not cloned) | SplitText + timelines are the industry standard for kinetic, large-scale typography that behaves like environmental signage in motion. |
| [ubuwaits/beautiful-web-type](https://github.com/ubuwaits/beautiful-web-type) | 7,343 |  | Curated open typefaces with strong character, useful for picking loud display faces the way Scher mixes wood-type-like weights. |
| [opentypejs/opentype.js](https://github.com/opentypejs/opentype.js) | 5,041 |  | Exposes glyph outlines as paths so letters can be treated as image/shape material, typography-as-image at the code level. |
| [github/mona-sans](https://github.com/github/mona-sans) | 4,182 |  | Wide width/weight axes let one family stretch and compress like Scher's Public Theater wordmarks across many formats. |
| [arrowtype/recursive](https://github.com/arrowtype/recursive) | 3,918 |  | Casual/slant/weight axes give an identity a flexing, expressive voice from one source font, a flexible-system building block. |
| [gkurt/tegaki](https://github.com/gkurt/tegaki) | 3,290 |  | Stroke-by-stroke lettering animation evokes the hand-made, hand-painted quality of her map paintings. |
| [shshaw/Splitting](https://github.com/shshaw/Splitting) | 1,757 |  | Splits text into per-char CSS variables so headlines can be stacked, scaled, and choreographed as bold typographic compositions. |
| [Jolg42/awesome-typography](https://github.com/Jolg42/awesome-typography) | 1,554 |  | Reference index of type tools, foundries, and variable-font resources to mine for expressive type systems. |
| [franktisellano/datatype](https://github.com/franktisellano/datatype) | 1,471 |  | Turns typed text into data graphics, literally type becoming image and information, close to her information-as-typography maps. |
| [iart-ai/motion-skills](https://github.com/iart-ai/motion-skills) | 1,129 |  | Agent skills for kinetic typography output, a fast way to produce Scher-like animated type identities via Claude Code. |
| [fontra/fontra](https://github.com/fontra/fontra) | 854 |  | Browser font editor (variable-capable) to draw custom display letterforms, the base of any bespoke identity wordmark system. |
| [fatihaydost/brand-identity-skill](https://github.com/fatihaydost/brand-identity-skill) | 277 | yes (not cloned) | Treats identity as one coherent typographic system rather than a logo, matching her Public Theater / Citi systems thinking. |
| [NaN-xyz/Glyph-Filters](https://github.com/NaN-xyz/Glyph-Filters) | 173 |  | Generative display-type filters produce loud, poster-grade letterforms for expressive headline systems. |

Skills / tools: Local Claude Code skill: design-html (gstack, Pretext-native HTML/CSS) for typographic layouts; Local Claude Code skill: frontend-design:frontend-design and taste-skill:design-taste-frontend for bold type-led art direction; Local Claude Code skill: animate (kinetic type motion decisions); Local Claude Code skill: anthropic-skills:canvas-design for poster-style typographic compositions; Local Claude Code skill: figma:figma-generate-library for building a flexible identity system in Figma; iart-ai/kinetic-typography-skills (22 stars) - agent skills for beat-synced kinetic type; pablostanley/typexperiments (34 stars) - kinetic type engine on Pretext; bangtutorial/bang-motion (942 stars) - agent skill for kinetic typography/motion graphics

## Emil Kowalski

Motion must earn its place: animate only when it adds purpose (feedback, spatial continuity, orientation), keep it fast (mostly under 300ms) with strong custom ease-out curves or springs, and never block the user. Interactions should be interruptible and gesture-driven (velocity-aware drags, momentum, rubber-banding), animate only transform/opacity for performance, respect reduced-motion, and sweat invisible details so components feel native and opinionated rather than configurable.

Own repos:

| Repo | Stars | Cloned | Why |
|---|---|---|---|
| [emilkowalski/skills](https://github.com/emilkowalski/skills) | 52,622 | yes (not cloned) | Skills for Designers and Engineers. (animate, emil-design-eng, review-animations, improve-animations, animation-performance, apple-design, animation-vocabulary, ask-sonner, etc.) |
| [emilkowalski/sonner](https://github.com/emilkowalski/sonner) | 13,118 | yes (not cloned) | An opinionated toast component for React. |
| [emilkowalski/vaul](https://github.com/emilkowalski/vaul) | 8,671 | yes (not cloned) | A drawer component for React. |

Emulating repos:

| Repo | Stars | Cloned | Why |
|---|---|---|---|
| [juliangarnier/anime](https://github.com/juliangarnier/anime) | 74,156 |  | Lightweight timeline/stagger engine for choreographing multi-element sequences framework-free. |
| [motiondivision/motion](https://github.com/motiondivision/motion) | 34,762 | yes (not cloned) | Springs, layout animations, AnimatePresence exits and variant orchestration; the library Emil teaches with in animations.dev. |
| [greensock/GSAP](https://github.com/greensock/GSAP) | 30,014 | yes (not cloned) | Industry-standard timeline choreography and scroll-driven motion for complex sequences. |
| [pmndrs/react-spring](https://github.com/pmndrs/react-spring) | 29,259 |  | Physics-based, interruptible spring animations that retarget mid-flight. |
| [magicuidesign/magicui](https://github.com/magicuidesign/magicui) | 23,020 |  | Copy-paste animated shadcn-style components built on Motion for design engineers. |
| [radix-ui/primitives](https://github.com/radix-ui/primitives) | 19,461 | yes (not cloned) | Accessible unstyled primitives Vaul is built on (Dialog); data-state attrs enable enter/exit CSS animation. |
| [formkit/auto-animate](https://github.com/formkit/auto-animate) | 13,953 |  | Drop-in FLIP transitions for list add/remove/reorder with tasteful defaults. |
| [dip/cmdk](https://github.com/dip/cmdk) | 13,057 | yes (not cloned) | Paco Coursey's craft-level command menu (formerly pacocoursey/cmdk); same opinionated-primitive school as Sonner/Vaul. |
| [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | 10,440 | yes (not cloned) | Agent skills encoding design-engineer UI/motion rules, parallel to emilkowalski/skills. |
| [pmndrs/use-gesture](https://github.com/pmndrs/use-gesture) | 9,627 | yes (not cloned) | Velocity-aware drag/pinch/wheel handling for building gesture-driven sheets and swipe-to-dismiss. |
| [ai/easings.net](https://github.com/ai/easings.net) | 8,714 |  | Reference of cubic-bezier easing curves for picking tasteful custom ease-outs. |
| [ibelick/motion-primitives](https://github.com/ibelick/motion-primitives) | 6,875 |  | Small, restrained Motion-based primitives (morphing dialog, text effects, transitions) close to Emil's taste. |
| [sergey-pimenov/awesome-web-animation](https://github.com/sergey-pimenov/awesome-web-animation) | 1,599 |  | Curated index of web animation libs, tools and learning resources. |
| [kylezantos/design-motion-principles](https://github.com/kylezantos/design-motion-principles) | 1,472 | yes (not cloned) | Explicitly distills Emil's published motion principles into a build/audit skill. |
| [vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines) | 1,083 | yes (not cloned) | Vercel design-engineering checklist (Rauno/Paco lineage) for interaction and animation details. |

Skills / tools: animations.dev (Emil's paid course on web animation craft); emilkowal.ski blog (e.g. 'Great animations', 'You don't need animations', 'Building a drawer component', 'Building a toast component'); emilkowalski/skills Claude Code skills: animate, emil-design-eng, review-animations, improve-animations, find-animation-opportunities, animation-performance, animation-vocabulary, apple-design, ask-sonner, remove-animations, pick-ui-library (most already installed locally); kylezantos/design-motion-principles (Claude skill distilled from Emil/Krehel/Jhey); ibelick/ui-skills (design-engineer agent skills); motion.dev docs + Motion DevTools; easings.net and cubic-bezier.com for curve tuning; Chrome DevTools Animations panel (slow-mo / scrub) for review

## Boris Cherny

Boris Cherny builds terminal-first agentic tools (Claude Code) that keep the human in the loop: the agent proposes, permission prompts gate risky actions, and state like todos, diffs and tool calls stays visible so users can trust a probabilistic system and recover when it errs. His background in type-safe APIs (Programming TypeScript, json-schema-to-typescript) shows in a preference for explicit contracts, progressive disclosure, and composable primitives (hooks, skills, plugins, subagents) over hidden magic.

Own repos:

| Repo | Stars | Cloned | Why |
|---|---|---|---|
| [bcherny/json-schema-to-typescript](https://github.com/bcherny/json-schema-to-typescript) | 3,350 |  | Compile JSON Schema to TypeScript type declarations |
| [bcherny/undux](https://github.com/bcherny/undux) | 1,564 |  | Dead simple state for React. Now with Hooks support. |
| [bcherny/frontend-interview-questions](https://github.com/bcherny/frontend-interview-questions) | 1,144 |  | Answers for Boris Cherny's Frontend Interview Questions blog post |
| [bcherny/programming-typescript-answers](https://github.com/bcherny/programming-typescript-answers) | 561 |  | Official answers for exercises from O'Reilly's Programming TypeScript |
| [bcherny/flow-to-typescript](https://github.com/bcherny/flow-to-typescript) | 438 |  | Convert Flow-annotated files to TypeScript |
| [bcherny/draggable](https://github.com/bcherny/draggable) | 204 |  | High performance, fully cross browser, full featured drag and drop in a tiny (2k gzipped), dependency-free package |

Emulating repos:

| Repo | Stars | Cloned | Why |
|---|---|---|---|
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | 223,744 | yes (not cloned) | Most-starred open-source Claude Code alternative (formerly sst/opencode); full TUI source for permission prompts, plan/build modes, session UX. |
| [anthropics/skills](https://github.com/anthropics/skills) | 186,148 | yes (not cloned) | Official skill format built on progressive disclosure; includes discernment-nudge, a skill that prompts users to calibrate trust in AI output. |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | 154,136 |  | Boris's flagship; issues, changelog and examples show permission modes, hooks and error-state design decisions in public (source not open). |
| [openai/codex](https://github.com/openai/codex) | 132,672 |  | Direct competitor with open source; approval modes and sandbox levels show another take on agent trust (Rust/ratatui TUI). |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | 108,649 | yes (not cloned) | Open-source Ink/React terminal agent built in the Claude Code style; readable source for tool-confirmation dialogs and themes. |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | 57,020 |  | Curated index of the Claude Code ecosystem: status lines, hooks and workflows that extend its human-in-the-loop UX. |
| [Aider-AI/aider](https://github.com/Aider-AI/aider) | 49,877 |  | Early terminal pair-programmer; git-commit-per-change is a trust and undo pattern worth studying. |
| [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | 45,661 |  | Reference plugins (hookify, security-guidance, explanatory-output-style, frontend-design) that show guardrail and transparency patterns in practice. |
| [charmbracelet/bubbletea](https://github.com/charmbracelet/bubbletea) | 45,578 |  | Go Elm-architecture TUI framework behind Crush and many AI CLIs; Charm sets the visual-craft bar for terminals. |
| [vadimdemedes/ink](https://github.com/vadimdemedes/ink) | 40,206 | yes (not cloned) | React-for-terminal renderer used by Claude Code and gemini-cli; the base layer for its component UX. |
| [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | 29,072 | yes (not cloned) | Shows agent state in a compact status HUD (context, tools, subagents), a direct pattern for making AI work legible. |
| [charmbracelet/crush](https://github.com/charmbracelet/crush) | 28,909 |  | Design-forward agentic coding TUI from Charm; strong reference for visual hierarchy and permission UI in terminals. |
| [ratatui/ratatui](https://github.com/ratatui/ratatui) | 23,137 |  | Rust TUI framework behind the Codex CLI; widget library for diffs, lists and modal prompts. |
| [humanlayer/humanlayer](https://github.com/humanlayer/humanlayer) | 12,739 |  | Started as human-approval-for-agent-tool-calls SDK; now a Claude Code orchestration UI built around human-in-the-loop review. |
| [HenryPengZou/Awesome-Human-Agent-Collaboration-Interaction-Systems](https://github.com/HenryPengZou/Awesome-Human-Agent-Collaboration-Interaction-Systems) | 242 |  | Research survey and reading list on human-agent feedback, control and trust: the theory behind permission UX. |

Skills / tools: anthropics/skills: discernment-nudge (prompts user to sanity-check AI output; trust calibration); anthropics/skills: skill-creator (progressive-disclosure skill authoring); anthropics/claude-plugins-official: hookify (turn unwanted agent behaviors into guardrail hooks); anthropics/claude-plugins-official: security-guidance (pattern warnings on edits plus Stop-time review; error-state surfacing); anthropics/claude-plugins-official: explanatory-output-style / learning-output-style (agent explains its choices; transparency); anthropics/claude-plugins-official: frontend-design; Claude Code built-ins: permission modes (default/acceptEdits/plan/bypass), PreToolUse/PostToolUse hooks, plan mode, todo list, checkpoints/rewind; jarrodwatts/claude-hud plugin (status-line agent state visibility)

## Jordan Singer

AI should be a playful design collaborator, not a replacement: describe intent in plain language and get real, editable interface (prompt-to-interface, generative UI) inside the tools designers already use, as shown by his GPT-3 Figma 'Designer' demos, Magician and Diagram (acquired by Figma). He ships small, delightful, opinionated prototypes fast ('I build my ideas'), favoring craft and recreating native UIs in code (SwiftUI samples) to learn by building.

Own repos:

| Repo | Stars | Cloned | Why |
|---|---|---|---|
| [jordansinger/SwiftUI-Kit](https://github.com/jordansinger/SwiftUI-Kit) | 2,534 |  | A SwiftUI system components and interactions demo app |
| [jordansinger/Hook](https://github.com/jordansinger/Hook) | 1,621 |  | Pull to refresh for the web |
| [jordansinger/UIDraw](https://github.com/jordansinger/UIDraw) | 470 |  | Draw and build a website on your phone. |
| [jordansinger/messages-multiplatform-swiftui-sample](https://github.com/jordansinger/messages-multiplatform-swiftui-sample) | 419 |  | Multiplatform Messages app for macOS, iOS, iPadOS in SwiftUI |
| [jordansinger/health-macos-swiftui-example](https://github.com/jordansinger/health-macos-swiftui-example) | 344 |  | Health app macOS Big Sur built in SwiftUI |
| [jordansinger/todo-macos-swiftui-sample](https://github.com/jordansinger/todo-macos-swiftui-sample) | 332 |  | Todo macOS app in built SwiftUI |

Emulating repos:

| Repo | Stars | Cloned | Why |
|---|---|---|---|
| [abi/screenshot-to-code](https://github.com/abi/screenshot-to-code) | 80,962 | yes (not cloned) | Image-to-interface pipeline; closest OSS echo of his GPT-3 'Designer' demos turning intent into real layouts. |
| [tldraw/tldraw](https://github.com/tldraw/tldraw) | 51,176 |  | Canvas SDK behind the (now archived) make-real demo: sketch a UI, AI makes it real; playful prototype-first spirit. |
| [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | 38,448 |  | Production stack for agent-driven generative UI in React; AI as an in-app collaborator. |
| [vercel/ai](https://github.com/vercel/ai) | 27,671 |  | AI SDK with streamUI/tool-rendered components; reference implementation of generative UI patterns. |
| [onlook-dev/onlook](https://github.com/onlook-dev/onlook) | 27,070 |  | Open-source AI-first visual design tool editing real code; Figma-meets-prompt workflow like Magician/Diagram. |
| [wandb/openui](https://github.com/wandb/openui) | 22,723 |  | Describe a UI in words and see it rendered live; direct prompt-to-interface clone. |
| [vercel-labs/json-render](https://github.com/vercel-labs/json-render) | 18,870 | yes (not cloned) | Generative UI framework: LLM emits constrained JSON rendered by your own component catalog. |
| [a2ui-project/a2ui](https://github.com/a2ui-project/a2ui) | 16,923 |  | Google-originated Agent-to-UI declarative protocol for agents to compose native interfaces (A2UI). |
| [GLips/Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP) | 16,132 |  | Framelink MCP feeding Figma layout data to coding agents; design-to-code bridge for AI collaborators. |
| [thesysdev/openui](https://github.com/thesysdev/openui) | 14,598 |  | Thesys open standard + SDK (C1) for LLM responses rendered as interactive UI. |
| [tambo-ai/tambo](https://github.com/tambo-ai/tambo) | 11,221 |  | React generative UI SDK where the model picks and fills registered components. |
| [grab/cursor-talk-to-figma-mcp](https://github.com/grab/cursor-talk-to-figma-mcp) | 7,078 | yes (not cloned) | Lets Claude Code/Cursor read and modify Figma canvas programmatically; modern Magician-style prompt-to-Figma. |
| [ZSeven-W/openpencil](https://github.com/ZSeven-W/openpencil) | 7,007 |  | Open-source AI-native vector design tool; prompt-driven canvas generation. |
| [narrowin/awesome-generative-ui](https://github.com/narrowin/awesome-generative-ui) | 144 |  | Curated index of generative UI frameworks, protocols, papers; map for further study. |
| [figma/ai-plugin-template](https://github.com/figma/ai-plugin-template) | 143 |  | Official Figma starter for plugins calling GPT; minimal base to rebuild a Magician-like plugin. |

Skills / tools: figma:figma-generate-design (Claude Code skill: prompt -> Figma layout); figma:figma-generative-plugins (Claude Code skill: build generative Figma plugins); figma:figma-use / figma:figma-design-to-code (Claude Code skills, Figma MCP); vercel:ai-sdk (Claude Code skill: AI SDK generative UI / streamUI); Figma official Dev Mode MCP server (figma/mcp-server-guide, 2138 stars); Framelink Figma MCP (GLips/Figma-Context-MCP); TalkToFigma MCP (grab/cursor-talk-to-figma-mcp); Figma Console MCP (southleft/figma-console-mcp, 2637 stars)

## Linear design engineering culture

Design engineers own UI end to end and ship it themselves, so craft survives into production. Product UI is keyboard-first (Cmd+K, chorded shortcuts), fast, dense and dark-mode-native, with the 'Linear look' of subtle gradients, glass, grain, tight Inter-style type and restrained, purposeful motion. The Linear Method frames this as opinionated, focused building with high quality bars.

Official repos: [linear/linear](https://github.com/linear/linear) (1,652), [linear/linear-release](https://github.com/linear/linear-release) (70), [linear/linear-solutions](https://github.com/linear/linear-solutions) (24)

| Repo | Stars | Cloned | Why |
|---|---|---|---|
| [makeplane/plane](https://github.com/makeplane/plane) | 61,806 | yes (not cloned) | Largest OSS Linear alternative; study its issue list, cycles, keyboard nav and dense dark UI end to end. |
| [hcengineering/platform](https://github.com/hcengineering/platform) | 28,032 |  | Huly: full Linear/Notion-style workspace; reference for fast issue tracking with keyboard-driven flows. |
| [emilkowalski/sonner](https://github.com/emilkowalski/sonner) | 13,118 | yes (not cloned) | Emil Kowalski's toast; canonical design-engineer motion craft (stacking, swipe, easing) in Linear-style apps. |
| [dip/cmdk](https://github.com/dip/cmdk) | 13,057 | yes (not cloned) | Paco Coursey's cmdk: the Cmd+K command menu primitive behind Linear/Vercel-style palettes (moved from pacocoursey/cmdk). |
| [emilkowalski/vaul](https://github.com/emilkowalski/vaul) | 8,671 | yes (not cloned) | Physics-feeling drawer; study interruptible gestures and spring timing. |
| [pacocoursey/next-themes](https://github.com/pacocoursey/next-themes) | 6,346 |  | Flash-free dark mode; baseline for dark-mode-native product UI. |
| [timc1/kbar](https://github.com/timc1/kbar) | 5,261 |  | Portable Cmd+K interface with nested actions and shortcuts; alt to cmdk with built-in registry. |
| [ln-dev7/circle](https://github.com/ln-dev7/circle) | 4,572 | yes (not cloned) | Closest OSS replica of Linear's app UI (sidebar, issue list, density) on Next.js + shadcn/ui; best reuse target. |
| [jamiebuilds/tinykeys](https://github.com/jamiebuilds/tinykeys) | 4,104 |  | 650B keybinding lib with sequences (g then i); fits Linear-style chorded shortcuts. |
| [JohannesKlauss/react-hotkeys-hook](https://github.com/JohannesKlauss/react-hotkeys-hook) | 3,505 |  | React hook for scoped shortcuts; practical layer for keyboard-first components. |
| [vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines) | 1,083 | yes (not cloned) | Rauno/Vercel interface detail checklist; codifies design-engineer craft rules (successor to raunofreiberg/interfaces). |
| [frontendfyi/rebuilding-linear.app](https://github.com/frontendfyi/rebuilding-linear.app) | 315 |  | Rebuild of Linear's marketing site: gradients, glow, grain, tight type, Framer Motion reveals. |

## Notion craft team

Polish is a dedicated team function, not an afterthought: a craft team sweeps edges, transitions and copy across the product. Everything is a block, editing is direct and forgiving (slash menu, drag handles, nesting), and delight comes from small micro-interactions and thoughtful empty states that teach the product.

Official repos: [makenotion/notion-sdk-js](https://github.com/makenotion/notion-sdk-js) (5,680), [makenotion/notion-mcp-server](https://github.com/makenotion/notion-mcp-server) (4,691), [makenotion/skills](https://github.com/makenotion/skills) (179), [makenotion/claude-code-notion-plugin](https://github.com/makenotion/claude-code-notion-plugin) (502), [makenotion/takehome-mentions](https://github.com/makenotion/takehome-mentions) (8)

| Repo | Stars | Cloned | Why |
|---|---|---|---|
| [AppFlowy-IO/AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) | 78,067 |  | Biggest OSS Notion alternative; full block docs + databases + empty states to study. |
| [toeverything/AFFiNE](https://github.com/toeverything/AFFiNE) | 74,040 |  | Notion+Miro hybrid with high polish; study block/edgeless transitions and micro-interactions. |
| [outline/outline](https://github.com/outline/outline) | 41,130 | yes (not cloned) | Most Notion-quality docs UX in OSS: slash menu, mentions, fast search, careful empty states. |
| [ueberdosis/tiptap](https://github.com/ueberdosis/tiptap) | 38,922 |  | Headless ProseMirror framework underpinning most Notion-style editors (Novel, BlockNote, Docmost). |
| [codex-team/editor.js](https://github.com/codex-team/editor.js) | 31,987 |  | Pure block-style editor with clean JSON output; reference block data model. |
| [docmost/docmost](https://github.com/docmost/docmost) | 22,183 |  | OSS Confluence/Notion wiki; polished page tree, comments and editor on Tiptap. |
| [udecode/plate](https://github.com/udecode/plate) | 16,685 |  | Slate + shadcn/ui rich editor with AI, DnD blocks, slash commands; copyable components. |
| [steven-tey/novel](https://github.com/steven-tey/novel) | 16,463 | yes (not cloned) | Notion-style WYSIWYG with AI autocomplete; small, readable Tiptap reference (last push 2025-01). |
| [TypeCellOS/BlockNote](https://github.com/TypeCellOS/BlockNote) | 10,351 | yes (not cloned) | Drop-in Notion-style block editor (drag handles, slash menu, nesting); fastest path to Notion feel. |
| [toeverything/blocksuite](https://github.com/toeverything/blocksuite) | 6,080 |  | AFFiNE's editor toolkit; deep dive into block architecture and collaborative editing. |
| [yoopta-editor/Yoopta-Editor](https://github.com/yoopta-editor/Yoopta-Editor) | 3,093 |  | Notion/Craft-like block editor on Slate with plugin blocks and marks toolbar. |
| [ddoemonn/interior](https://github.com/ddoemonn/interior) | 1,209 |  | Micro-interaction library for 'the half-second after a click'; maps to Notion craft-team delight. |

## Concepts

### Semantic tokens

Name design decisions by intent (color.bg.danger) in a primitive->semantic->component token layer, exported to every platform from one source.

| Repo | Stars | Cloned | Why |
|---|---|---|---|
| [style-dictionary/style-dictionary](https://github.com/style-dictionary/style-dictionary) | 4,875 | yes (not cloned) | De facto token build system; v4+ supports DTCG format, transforms tokens to CSS/iOS/Android. |
| [design-tokens/community-group](https://github.com/design-tokens/community-group) | 2,160 |  | W3C DTCG spec repo: the canonical token JSON format ($value/$type, aliases). |
| [tokens-studio/figma-plugin](https://github.com/tokens-studio/figma-plugin) | 1,629 |  | Most-used Figma token authoring plugin; semantic sets/themes synced to git. |
| [sturobson/Awesome-Design-Tokens](https://github.com/sturobson/Awesome-Design-Tokens) | 1,298 |  | Curated reading + tooling list covering token naming and semantic layering. |

### Optical alignment

Center things by perceived visual mass, not bounding boxes (play icons, text cap-height, rounded shapes).

| Repo | Stars | Cloned | Why |
|---|---|---|---|
| [seek-oss/capsize](https://github.com/seek-oss/capsize) | 1,735 |  | Trims font leading so text aligns optically to cap-height/baseline; most-starred practical optical-alignment tool. |
| [jantimon/text-box-trim-examples](https://github.com/jantimon/text-box-trim-examples) | 403 |  | Playground for CSS text-box-trim, the native way to optically align text in boxes. |
| [ledgelabs/optical-center](https://github.com/ledgelabs/optical-center) | 0 |  | Exact match (build-time optical centering of Lucide/Phosphor SVG icons) but ~0 stars; study, not depend on. |

### Data ramps

Perceptually uniform sequential/diverging/categorical color scales so data viz encodes value honestly and accessibly.  
> TRANSCRIPTION ERROR: the video says 'Dieter Rams' (person), not 'Data Ramps'. Kept as a bonus concept (colour scales for data viz); see research/dieter-rams.json for the real item.

| Repo | Stars | Cloned | Why |
|---|---|---|---|
| [gka/chroma.js](https://github.com/gka/chroma.js) | 10,608 |  | Color scales, bezier interpolation and lightness correction for building data ramps. |
| [adobe/leonardo](https://github.com/adobe/leonardo) | 2,162 |  | Generates color ramps targeted by contrast ratio; good for accessible sequential scales. |
| [axismaps/colorbrewer](https://github.com/axismaps/colorbrewer) | 1,109 |  | Source of ColorBrewer, the classic tested cartographic/data-viz palettes. |
| [d3/d3-scale-chromatic](https://github.com/d3/d3-scale-chromatic) | 817 |  | Reference implementation of viridis/turbo/ColorBrewer interpolators used across d3 viz. |

### Component API design

Composable APIs (compound components, slots, asChild, controlled/uncontrolled) that scale without prop explosion.

| Repo | Stars | Cloned | Why |
|---|---|---|---|
| [radix-ui/primitives](https://github.com/radix-ui/primitives) | 19,461 | yes (not cloned) | Canonical compound-component + asChild API pattern most libs copy. |
| [mui/base-ui](https://github.com/mui/base-ui) | 11,271 |  | Next-gen headless lib by Radix/MUI/Floating UI authors; refined composition (render prop) API. |
| [adobe/react-spectrum](https://github.com/adobe/react-spectrum) | 16,005 |  | React Aria hooks + components: deepest public thinking on accessible, layered component APIs. |
| [kentcdodds/advanced-react-patterns](https://github.com/kentcdodds/advanced-react-patterns) | 374 |  | Workshop teaching compound components, prop getters, state reducer, control props. |

### Perceived performance

Make apps feel fast via skeletons, optimistic updates and speculative prefetch, independent of real latency.

| Repo | Stars | Cloned | Why |
|---|---|---|---|
| [TanStack/query](https://github.com/TanStack/query) | 50,510 |  | Optimistic updates, stale-while-revalidate and prefetch primitives for perceived speed. |
| [GoogleChromeLabs/quicklink](https://github.com/GoogleChromeLabs/quicklink) | 11,305 |  | Prefetches in-viewport links during idle time (speculative loading). |
| [danilowoz/react-content-loader](https://github.com/danilowoz/react-content-loader) | 13,999 |  | SVG skeleton screens matching real layout. |
| [instantpage/instant.page](https://github.com/instantpage/instant.page) | 6,221 |  | Hover/touchstart preloading; tiny drop-in speculative navigation. |

### Designing for non-deterministic systems

UX for outputs that vary per run: steerability, human-in-the-loop, regenerate/branch, shared agent state. No mature dedicated pattern-library repo exists; best code references below.

| Repo | Stars | Cloned | Why |
|---|---|---|---|
| [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | 38,448 |  | Agent frontend stack with human-in-the-loop, shared state and generative UI patterns. |
| [ag-ui-protocol/ag-ui](https://github.com/ag-ui-protocol/ag-ui) | 16,960 |  | Agent-User Interaction protocol: event model for streaming, tool calls, interrupts between agent and UI. |
| [assistant-ui/assistant-ui](https://github.com/assistant-ui/assistant-ui) | 12,885 |  | Chat primitives with branching, edit/regenerate, tool-call UI for variable outputs. |
| [Halaska-Studio/ui](https://github.com/Halaska-Studio/ui) | 42 |  | Low stars but on-topic: React kit of ~40 AI UX patterns built on shadcn. |

### Progressive disclosure

Show only what's needed now, reveal depth on demand (disclosure, accordions, staged forms, skill files loaded lazily). No dedicated repo; implemented as primitives.

| Repo | Stars | Cloned | Why |
|---|---|---|---|
| [tailwindlabs/headlessui](https://github.com/tailwindlabs/headlessui) | 28,805 |  | Disclosure/Popover/Dialog primitives: the building blocks of progressive disclosure. |
| [radix-ui/primitives](https://github.com/radix-ui/primitives) | 19,461 | yes (not cloned) | Collapsible, Accordion, HoverCard, Popover with accessible reveal semantics. |
| [anthropics/skills](https://github.com/anthropics/skills) | 186,150 | yes (not cloned) | Agent Skills are built on progressive disclosure (metadata -> SKILL.md -> references); useful mental model for AI context too. |

### OKLCH

Perceptually uniform color space (lightness, chroma, hue) for predictable palettes, theming and P3 wide gamut.

| Repo | Stars | Cloned | Why |
|---|---|---|---|
| [evilmartians/oklch-picker](https://github.com/evilmartians/oklch-picker) | 2,018 | yes (not cloned) | Source of oklch.com picker; shows gamut boundaries and P3 fallback. |
| [color-js/color.js](https://github.com/color-js/color.js) | 2,314 |  | By CSS Color spec editors; full OKLCH/OKLab conversion, gamut mapping. |
| [Evercoder/culori](https://github.com/Evercoder/culori) | 1,246 |  | Comprehensive tree-shakable color lib with OKLCH, interpolation, difference metrics. |
| [argyleink/open-props](https://github.com/argyleink/open-props) | 5,560 |  | CSS custom-property system with OKLCH-based color/palette props. |

### Generative UI

LLM chooses/streams real UI components (from a catalog or spec) instead of only text.

| Repo | Stars | Cloned | Why |
|---|---|---|---|
| [vercel-labs/json-render](https://github.com/vercel-labs/json-render) | 18,870 | yes (not cloned) | Generative UI framework: model emits JSON constrained to your component catalog. |
| [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | 38,448 |  | Frontend stack for agents with generative UI across React/Angular/mobile. |
| [a2ui-project/a2ui](https://github.com/a2ui-project/a2ui) | 16,923 |  | A2UI (originated at Google): declarative agent-to-UI spec rendered natively by clients. |
| [thesysdev/openui](https://github.com/thesysdev/openui) | 14,598 |  | Thesys open standard + SDK for generative UI (successor of Crayon/C1 tooling). |

### Model latency as a design constraint

Design around seconds-long, streaming responses: token streaming, shimmer/thinking states, partial rendering, cancel/queue.

| Repo | Stars | Cloned | Why |
|---|---|---|---|
| [vercel/ai](https://github.com/vercel/ai) | 27,671 |  | AI SDK: streamText/useChat/streamObject give partial-result streaming to the UI. |
| [vercel/streamdown](https://github.com/vercel/streamdown) | 5,742 |  | Markdown renderer that handles incomplete, streaming LLM output without jank. |
| [vercel/ai-elements](https://github.com/vercel/ai-elements) | 2,503 | yes (not cloned) | shadcn registry with Shimmer, Reasoning, Queue, Task, PromptInput (stop) components for slow models. |
| [Jakubantalik/thinking-orbs](https://github.com/Jakubantalik/thinking-orbs) | 3,905 |  | Purpose-built 'thinking' loading indicators for AI/agent UIs. |

### Design engineering

Hybrid craft of designing in code: interaction detail, motion, polish, guidelines.

| Repo | Stars | Cloned | Why |
|---|---|---|---|
| [vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines) | 1,083 | yes (not cloned) | Vercel's interface guidelines (also packaged as agent skill); checklist of design-eng detail. |
| [raunofreiberg/interfaces](https://github.com/raunofreiberg/interfaces) | 1,955 |  | Rauno Freiberg's original list of details that make a good web interface. |
| [raphaelsalaja/userinterface-wiki](https://github.com/raphaelsalaja/userinterface-wiki) | 936 |  | Living manual of interface craft from a design engineer. |
| [remvze/desengs](https://github.com/remvze/desengs) | 276 |  | Closest thing to an awesome-design-engineering list (low stars, active). |

### Jobs To Be Done

Frame product work around the progress a user is trying to make in a circumstance, not features or personas. Weak GitHub presence.

| Repo | Stars | Cloned | Why |
|---|---|---|---|
| [wondelai/skills](https://github.com/wondelai/skills) | 2,551 | yes (not cloned) | Agent skills repo with a jobs-to-be-done skill (plus lean-ux, ux-heuristics, refactoring-ui). |
| [brianrhea/awesome-jtbd](https://github.com/brianrhea/awesome-jtbd) | 110 |  | Only notable JTBD awesome list; stale (last push 2018), use as reading list only. |

### Motion choreography

Sequence multiple elements' motion (stagger, orchestration, shared layout, timing) so transitions read as one story.

| Repo | Stars | Cloned | Why |
|---|---|---|---|
| [motiondivision/motion](https://github.com/motiondivision/motion) | 34,762 | yes (not cloned) | Motion (ex Framer Motion): variants, staggerChildren, layout/shared transitions = orchestration. |
| [juliangarnier/anime](https://github.com/juliangarnier/anime) | 74,156 |  | Anime.js v4 timelines + stagger utilities for sequenced choreography. |
| [formkit/auto-animate](https://github.com/formkit/auto-animate) | 13,953 |  | Zero-config list/layout transitions; cheapest choreography win. |
| [LottieFiles/motion-design-skill](https://github.com/LottieFiles/motion-design-skill) | 2,672 | yes (not cloned) | Agent skill encoding timing, easing, choreography and Disney principles. |

### Trust and error states of probabilistic systems

Communicate uncertainty, sources, reasoning and recoverable failure so users calibrate trust. Thin on GitHub; component kits are best refs.

| Repo | Stars | Cloned | Why |
|---|---|---|---|
| [vercel/ai-elements](https://github.com/vercel/ai-elements) | 2,503 | yes (not cloned) | Sources, InlineCitation, ChainOfThought, Reasoning, Confirmation components for trust/attribution. |
| [assistant-ui/assistant-ui](https://github.com/assistant-ui/assistant-ui) | 12,885 |  | Error/retry, regenerate, branch, tool-approval UI primitives. |
| [dgesteves/signoff-ui](https://github.com/dgesteves/signoff-ui) | 44 |  | Low stars but on-topic: review + approve agent changes UI components. |
| [sinhaankur/Probabilistic-UI](https://github.com/sinhaankur/Probabilistic-UI) | 0 |  | ~0 stars but exact topic: vocabulary for calibrated-confidence AI surfaces; study only. |

### Design debt

Accumulated inconsistency (hardcoded values, detached components, one-offs) between design system and product; detect and pay down.

| Repo | Stars | Cloned | Why |
|---|---|---|---|
| [destefanis/design-lint](https://github.com/destefanis/design-lint) | 521 |  | Figma plugin that flags missing styles/tokens in design files (last push 2024). |
| [AndyOGo/stylelint-declaration-strict-value](https://github.com/AndyOGo/stylelint-declaration-strict-value) | 145 |  | Stylelint rule enforcing tokens/variables instead of hardcoded values in code. |
| [moroshko/react-scanner](https://github.com/moroshko/react-scanner) | 661 |  | Audits component + prop usage across a codebase to measure design-system adoption. |
| [projectwallace/wallace-cli](https://github.com/projectwallace/wallace-cli) | 645 |  | CSS analytics (unique colors, font sizes, specificity) to quantify style sprawl. |

### Claude Code design skills

Agent skills that give Claude design taste, guidelines and review loops.

| Repo | Stars | Cloned | Why |
|---|---|---|---|
| [anthropics/skills](https://github.com/anthropics/skills) | 186,150 | yes (not cloned) | Official skills incl. frontend-design, canvas-design, theme-factory, brand-guidelines. |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 143,665 | yes (not cloned) | Largest design-intelligence skill: styles, palettes, font pairings, UX rules across stacks. |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 107,476 |  | Anti-slop art direction skill with reference library + browser check loop. |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 98,944 |  | Design vocabulary commands (polish, bolder, critique, audit) for coding agents. |

## Claude Code design skills

Already installed locally (from `~/.claude/skills` and plugins): animate, animate-expo, animation-performance, animation-vocabulary, apple-design, emil-design-eng, find-animation-opportunities, improve-animations, review-animations, design-review, design-html, design-consultation, impeccable:impeccable, taste-skill:design-taste-frontend, frontend-design:frontend-design, anatomy, dataviz, figma:* skills. The reel's Emil Kowalski segment maps directly to the emilkowalski/skills pack that is already installed.

Skill repos found by research (cloned under `repos/` unless marked):

| Repo | Stars | Cloned | Why |
|---|---|---|---|
| [anthropics/skills](https://github.com/anthropics/skills) | 186,150 | yes (not cloned) |  |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 143,665 | yes (not cloned) |  |
| [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | 125,021 | yes (not cloned) |  |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 107,476 |  |  |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 98,944 |  |  |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 78,487 |  |  |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | 57,020 |  |  |
| [emilkowalski/skills](https://github.com/emilkowalski/skills) | 52,621 | yes (not cloned) |  |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | 36,697 |  |  |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | 33,334 | yes (not cloned) |  |
| [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | 15,660 |  |  |
| [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | 10,440 | yes (not cloned) |  |
| [Jakubantalik/transitions.dev](https://github.com/Jakubantalik/transitions.dev) | 6,004 | yes (not cloned) |  |
| [Dammyjay93/interface-design](https://github.com/Dammyjay93/interface-design) | 5,893 | yes (not cloned) |  |
| [plugin87/ux-ui-agent-skills](https://github.com/plugin87/ux-ui-agent-skills) | 3,067 | yes (not cloned) |  |
| [LottieFiles/motion-design-skill](https://github.com/LottieFiles/motion-design-skill) | 2,672 | yes (not cloned) |  |
| [wondelai/skills](https://github.com/wondelai/skills) | 2,551 | yes (not cloned) |  |

## Clone list

| Repo | Stars | Source | Size |
|---|---|---|---|
| anomalyco/opencode | 223,744 | boris-cherny | not cloned |
| anthropics/skills | 186,150 | concepts | not cloned |
| nextlevelbuilder/ui-ux-pro-max-skill | 143,665 | concepts | not cloned |
| VoltAgent/awesome-design-md | 125,021 | skills | not cloned |
| google-gemini/gemini-cli | 108,649 | boris-cherny | not cloned |
| abi/screenshot-to-code | 80,962 | jordan-singer | not cloned |
| makeplane/plane | 61,806 | linear-and-notion-craft | not cloned |
| emilkowalski/skills | 52,621 | concepts | not cloned |
| chenglou/pretext | 50,980 | paula-scher | not cloned |
| outline/outline | 41,130 | linear-and-notion-craft | not cloned |
| vadimdemedes/ink | 40,206 | boris-cherny | not cloned |
| motiondivision/motion | 34,762 | concepts,emil-kowalski | not cloned |
| vercel-labs/agent-skills | 33,334 | skills | not cloned |
| greensock/GSAP | 30,014 | paula-scher | not cloned |
| jarrodwatts/claude-hud | 29,072 | boris-cherny | not cloned |
| radix-ui/primitives | 19,461 | concepts | not cloned |
| vercel-labs/json-render | 18,870 | concepts,jordan-singer | not cloned |
| steven-tey/novel | 16,463 | linear-and-notion-craft | not cloned |
| emilkowalski/sonner | 13,118 | emil-kowalski | not cloned |
| dip/cmdk | 13,057 | linear-and-notion-craft | not cloned |
| ibelick/ui-skills | 10,440 | skills | not cloned |
| TypeCellOS/BlockNote | 10,351 | linear-and-notion-craft | not cloned |
| pmndrs/use-gesture | 9,627 | emil-kowalski | not cloned |
| emilkowalski/vaul | 8,671 | emil-kowalski | not cloned |
| grab/cursor-talk-to-figma-mcp | 7,078 | jordan-singer | not cloned |
| Jakubantalik/transitions.dev | 6,004 | skills | not cloned |
| Dammyjay93/interface-design | 5,893 | skills | not cloned |
| style-dictionary/style-dictionary | 4,875 | concepts | not cloned |
| ln-dev7/circle | 4,572 | linear-and-notion-craft | not cloned |
| sakofchit/system.css | 3,928 | susan-kare | not cloned |
| plugin87/ux-ui-agent-skills | 3,067 | skills | not cloned |
| dominikmartn/nothing-design-skill | 2,849 | dieter-rams | not cloned |
| LottieFiles/motion-design-skill | 2,672 | skills | not cloned |
| wondelai/skills | 2,551 | skills | not cloned |
| vercel/ai-elements | 2,503 | concepts | not cloned |
| evilmartians/oklch-picker | 2,018 | concepts | not cloned |
| kylezantos/design-motion-principles | 1,472 | skills | not cloned |
| vercel-labs/web-interface-guidelines | 1,083 | concepts | not cloned |
| halfmage/pixelarticons | 886 | susan-kare | not cloned |
| zedr/dieter-rams-10-applied-to-software | 434 | dieter-rams | not cloned |
| KingDuane/Chicago-Kare | 350 | susan-kare | not cloned |
| jordansinger/build-it-figma-ai | 315 | jordan-singer | not cloned |
| fatihaydost/brand-identity-skill | 277 | paula-scher | not cloned |
| joe-bell/tenprinciples.design | 45 | dieter-rams | not cloned |
| yangyue1974/rams-braun-ui | 4 | dieter-rams | not cloned |

## Re-create

```bash
cd design-pack
while IFS=$'\t' read -r name stars src; do
  git clone --depth 1 "https://github.com/$name.git" "repos/$(echo "$name" | tr '/' '_')"
done < research/clone-list.txt
```

## Caveats

- Star counts are a 2026-11-01 snapshot.
- Licenses vary; `build-it-figma-ai`, `helloSystem/hello` and a few others have no license file (study only). GSAP uses its own free license.
- Delegates hit GitHub's shared 30 req/min search limit; some searches were skipped and backfilled by direct lookups. See `notes` fields in each JSON.
- Repos that moved: pacocoursey/cmdk is now dip/cmdk; framer/motion is now motiondivision/motion; google/A2UI is a2ui-project/a2ui.
