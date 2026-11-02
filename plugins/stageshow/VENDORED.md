# Vendored: Stageshow

| | |
|---|---|
| Upstream | https://github.com/benjitaylor/skills (folder `stageshow/`) |
| Author | Benji Taylor, https://benji.org/stageshow |
| Commit | 802057409787133703c56001080169e347305572 ("Add Stageshow", 2026-10-30) |
| Vendored | 2026-11-02 into `plugins/stageshow/skills/stageshow/` |
| Modifications | None. Byte-for-byte copy minus `node_modules/`, lockfiles and `shots/` |
| Upstream install | `npx skills add benjitaylor/skills --skill stageshow` |

## Licence

Source is MIT (`skills/stageshow/LICENSE`). `skills/stageshow/NOTICE.md` lists what the MIT licence does not cover and is reproduced unchanged:

- `assets/app-icons.ts`: six app icons taken from macOS app bundles (Mail, Calendar, TestFlight, Slack, Figma, Notion). Illustrative references, not licensed for reuse. Used only by the `phones`, `parts` and `bento` specimen examples.
- `kit/brands/`: SVG marks from SVGL (MIT), payment-icons (Apache-2.0), Cryptocurrency Icons (CC0), Simple Icons (CC0) and official Linear, American Express and Circle assets under their brand terms. Per-file sources and hashes in `kit/brands/SOURCES.md`.
- `examples/wikipedia/PHOTOS.md`: two CC0 photographs.
- Product and OS names, device geometry and recreated interfaces (Figma, Linear, Slack, Finder, Notion, Gmail, Office, iMessage, Telegram...) remain their owners' marks; no endorsement implied.

## Why vendored rather than referenced

design-pack's catalog resolves specialists by path so `design-director` can read the skill without a network or an install step. Pin to the commit above; refresh by re-copying upstream and updating this file.

## Playground and filming

The skill folder is self-contained. To run the playground or `scripts/film.mjs`, `cd skills/stageshow && pnpm install && pnpm run dev` (Node 20.19+, Chrome installed). Those are dev dependencies of the skill, not of any host app.

Known upstream caveat (2026-11-02): the gold examples `hero-demo` and `ai-chat` fail the shipped `film.mjs --gate`; `static-card` and `payout-flow` pass. Treat a gate failure before any edit as upstream.
