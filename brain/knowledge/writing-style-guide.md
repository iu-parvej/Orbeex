# Writing Style Guide

Applies to all human-facing text: README files, documentation, release notes, comments,
and error messages. It does not change precise wording inside code where exact meaning
matters more than tone.

## Register

Professional and compact. Write the way a well-run software company documents its product:
clear, factual, and dense with information. Every sentence should earn its place.

## Rules

1. **Be concise.** State the fact and move on. Remove any word that doesn't add meaning.
2. **Be factual.** Describe what something does. Avoid adjectives that assert quality
   ("powerful", "robust", "seamless", "cutting-edge") unless strictly necessary.
3. **Be neutral in tone.** No exclamation marks, no enthusiasm, no marketing language.
   No emoji, no decorative icons in prose.
4. **Use plain words.** Short sentences. One idea each. Prefer the common word.
5. **Lead with the function.** Say what a feature does first; add context only if it helps.
6. **Structured, not flowing.** Short paragraphs, tight bullet lists, tables for
   comparisons. Scannable beats elegant.
7. **Define terms once.** If a technical term is required, define it briefly on first use.
8. **Be accurate about status.** State clearly whether something is stable, early, or
   planned. Never overstate.

## Avoid

| Avoid | Use |
|---|---|
| "It is important to note that…" | (delete) |
| "leverage", "utilize" | "use" |
| "robust", "seamless", "powerful" | describe the actual behavior |
| "delve into" | "review" |
| "a myriad of" | "many" |
| "in order to" | "to" |
| "prior to" | "before" |
| "game-changing", "next-generation" | (delete) |
| Exclamation points, emoji, icons in prose | (delete) |

## Structure of a feature description

For each feature, state in order:

1. **What it does** — one sentence.
2. **Why it matters** — one sentence, only if not obvious.
3. **How to use it** — the command, or a short list of steps.

Example:

```
### Reproject a layer

Reprojects a vector layer to a target coordinate reference system.

    orbeex reproject --layer roads --crs EPSG:3857

Supports any CRS in the EPSG registry.
```

## Enforcement

No automated tone check. Reviewer responsibility: if a sentence is longer than it needs to
be, says nothing, or claims a quality it doesn't prove, it should be cut. This guide lives in
`brain/` so both humans and the AI collaborator follow it.
