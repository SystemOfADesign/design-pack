# Foundations before taste

Order of concerns. A lower item never overrides a higher one. Taste (fonts, color, motion, personality) lives inside these constraints and is not cosmetic: type sets hierarchy, color carries meaning, motion explains change. But a beautiful screen that fails item 1 is a failed screen.

| # | Foundation | Plain test | Why the user cares | Checked by |
|---|---|---|---|---|
| 1 | Workflow fit | Can the main person finish their main task without a detour? | They came to do one thing. | ux-heuristics walkthrough, jobs-to-be-done |
| 2 | Hierarchy | Does the eye land on one thing first, then the next? | Four equal boxes means nothing is important. | design-review, interface-design, refactoring-ui |
| 3 | Readability | Body text 16px+, lines 45-75 characters, enough contrast, real headings? | Squinting is quitting. | web-typography, a11y-audit (contrast) |
| 4 | Affordances and feedback | Does every clickable thing look clickable, and react when used? | People stop trusting controls that do nothing. | design-everyday-things, design-doctrine eight states |
| 5 | Accessibility | Keyboard works, labels exist, contrast passes, motion can be reduced? | Legal in many places; also just more users. | accessibility-review, a11y-audit, web-design-guidelines |
| 6 | Spacing and alignment | One spacing scale, things that belong together are closer than things that do not? | Misalignment reads as broken even when it works. | refactoring-ui, baseline-ui, lint_hardcodes |
| 7 | Consistency | Same thing looks and behaves the same everywhere? | Every exception is something new to learn. | improve-ui, create-design-md, design-system |
| 8 | Content reality | Empty, one, many, long names, errors, loading all handled? | Real data is never the demo data. | break-ui, impeccable harden |
| 9 | Responsiveness | Works at the narrowest width users actually have? | Half the traffic is a phone. | impeccable adapt/audit, verify_responsive |
| 10 | Performance | Nothing jumps after load, interactions feel instant? | Slow feels broken. | performance, animation-performance |
| 11 | Copy | Labels say the concrete thing, errors say what to do next? | Words are most of the interface. | ux-copy, ux-writing, impeccable clarify |
| 12 | Taste and direction | Does it feel like one deliberate choice, suited to who it is for? | Generic reads as untrustworthy; wrong tone reads as not-for-me. | design-taste-frontend, impeccable critique, critique |

## Universal vs. subjective

- Universal (1-11): the audit reports these as defects with severity. The user does not get to prefer a 3:1 contrast on body text; they can accept the risk, and the report says so.
- Subjective (12): the director offers options and the user chooses. The director still recommends, and still refuses to split the difference into something generic.

## Severity words for a non-designer

- Blocker: people cannot complete the task, or cannot use it at all (keyboard trap, unreadable, destructive action without confirm).
- Major: people can complete it but will make mistakes or give up more than they should.
- Minor: it works; it looks less trustworthy or careful than it should.
- Polish: only a designer would notice; still worth doing last.

## Measured vs. judged

Label every finding. Measured: a tool printed it (contrast 3.2:1, 14 hardcoded colors, 3 axe violations). Judged: a trained eye says so. Both are valid. Never present a judged number as measured.
