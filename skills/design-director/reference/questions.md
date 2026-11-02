# Question bank

Rules (from grill-me, kept):
- Read before asking. Framework, component inventory, existing tokens, PRODUCT.md / DESIGN.md / BRIEF.md, README, screenshots: the code answers these.
- Maximum five questions per round, one round if possible. Each must change the work; if both answers give the same build it is a default, take it and say so.
- Never ask the user to pick jargon. Offer concrete options in plain words with a recommended default marked.
- Never ask what you can choose well. Taste is your job; intent, audience, content, constraints are theirs.
- Everything unasked becomes a written assumption in the brief, with its cost if wrong.
- Prefer AskUserQuestion with 2-4 options plus the free-text "Other"; the user may know nothing, so options teach.

## EXPLORE (new product)

Purpose
- Who is this for, and what is the one thing they come to do? (options from the product description)
- Is the first screen mostly for deciding (sign up / buy), doing (work), or understanding (read)?
- How often will the same person use it: once, weekly, all day?

Feel (ask at most one of these; infer the rest)
- Pick the closest: calm tool / friendly consumer app / premium brand / playful / editorial / no idea, you choose.
- Name two products whose feel you like, or one you dislike. (Free text; most useful single question.)

Content reality
- What does a typical screen hold: a few things, dozens, hundreds?
- Longest thing a user types or that shows up (names, titles, amounts)?

Constraints
- Must it match an existing brand (colors, logo, fonts)? Dark mode needed?
- Phones first, desktop first, or both equally?

## AUDIT (existing product)

- Which screens matter most, and what is the main task on each? (or: let me pick the three busiest)
- What do users complain about, or where do they drop off? (free text; "don't know" is fine)
- Is the look negotiable, or must the audit stay inside the current brand?
- Should I run the app locally to screenshot it, or use screenshots you give me?

Do not ask about taste in AUDIT. Report foundations; taste comes last as a note.

## REDESIGN (existing product, replace)

- What must survive: flows, data, components, brand marks? (offer: everything behaves the same, only looks change / behaviors can change where they are confusing / clean slate within the brand)
- What is the reason for the redesign in one line: looks dated, inconsistent, users confused, new audience, rebrand?
- Big-bang or page-by-page migration? (default: tokens and shared components first, then screens by traffic)
- Two products whose feel you want to move toward; one you want to move away from.

## ROUTE (user knows the problem, not the specialist)

- Which screen, and what do you see happening? (one question; then diagnose from the symptom table in `modes/route.md`)

## When the answer is "I don't know"

Take the default, state it as an assumption, and keep going. Show, do not ask again: a direction board answers most taste questions better than a question does.
