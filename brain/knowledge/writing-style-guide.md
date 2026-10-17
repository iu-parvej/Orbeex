# Writing Style Guide

**This applies to every human-facing document:** README files, documentation, code
comments, error messages, release notes, and doc-comments. It does **not** change the
precise technical wording inside code where clarity of meaning matters more than tone.

> **Rule of thumb: write like you're explaining it to a smart colleague who is new to the
> project. Clear, warm, and plain. Not stiff, not robotic.**

## The short version

1. **Use simple, everyday English.** If a simpler word works, use it.
2. **Write in a natural, human voice.** Talk to the reader as "you." Use contractions
   sparingly but naturally ("you'll", "it's").
3. **Keep sentences short.** One idea per sentence. Break up long ones.
4. **Lead with why, then how.** Tell people what a thing does and why they'd care, then the
   details.
5. **Avoid AI-sounding filler.** No "In today's fast-paced world", "It is important to note
   that", "delve", "leverage", "robust", "seamless", "cutting-edge", "game-changing",
   "unlock", "empower". Just say the thing.
6. **No needless jargon.** If a technical term is necessary, explain it once in plain words.
7. **Be honest about status.** Say when something is early, unfinished, or a work in
   progress. Don't oversell.

## What to do / what to avoid

| Avoid (AI-ish) | Use instead (human) |
|---|---|
| "This module facilitates the orchestration of…" | "This part decides the order of steps." |
| "It is important to note that…" | (just say it) |
| "Robust, seamless, enterprise-grade solution" | "Built to handle big datasets without crashing." |
| "Leverage the power of AI" | "Use AI to…" |
| "Utilize" | "Use" |
| "Prior to" | "Before" |
| "In order to" | "To" |
| "A myriad of" | "Many" |
| "Delve into" | "Look at" / "dig into" |

## Structure

- Start each doc with a one-line summary of what it is.
- Use short sections with clear headings.
- Prefer bullet lists and short tables over dense paragraphs.
- Put the most important thing first.
- End with what the reader should do next, if anything.

## Examples in this repo

- `README.md` — the model to follow: warm, plain, explains GIS without assuming the reader
  knows it.
- `CONTRIBUTING.md` — friendly and direct.
- `SECURITY.md` — plain and serious without being cold.

## Enforcement

There is no automated linter for tone. It's a review responsibility: reviewers should ask
"would a normal person say it this way?" and push back on stiff or filler-filled wording.
This guide lives in `brain/` so the AI collaborator and humans both follow it.
