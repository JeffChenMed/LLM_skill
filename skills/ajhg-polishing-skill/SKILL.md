---
name: ajhg-polishing-skill
description: Polish biomedical and scientific manuscripts, abstracts, summaries, cover letters, and response text in a restrained AJHG/Cell-style prose: concept-first, precise, non-conversational, elegant, and suitable for high-level journal writing. Use when the user asks for AJHG style, Cell/AJHG-like elegance, or refined scientific prose after the scientific content is already decided.
---

# AJHG Polishing Skill

## Purpose

Use this skill after the scientific argument is mostly fixed. The goal is not to make prose casual, promotional, or ornate. The goal is controlled elegance: concept-first framing, precise nouns, calm verbs, and a clear account of what the work defines, clarifies, reconciles, or enables.

## Style Model

The model is the prose logic common in AJHG/Cell perspective and summary writing:

- Begin with the conceptual or clinical problem, not generic background.
- Acknowledge prior work without attacking it.
- Define the unresolved need as something to characterize, delineate, define, clarify, or locate.
- Use abstract nouns only when they sharpen the argument: value, yield, distribution, relationship, framework, setting, context, interpretation.
- Prefer restrained verbs: establish, define, characterize, evaluate, assess, compare, support, preserve.
- Use `Here, we...` sparingly and only when it cleanly identifies the contribution.
- Keep repeated key terms stable. Do not cycle synonyms for variety.

## Abstract Workflow

1. Identify the central contribution in one sentence:
   `This study defines where [test/intervention/phenomenon] is most informative in [population/context], using [design/analysis].`
2. Background:
   - Sentence 1: what prior work has established.
   - Sentence 2: what remains less clearly characterized.
   - Sentence 3: what this study evaluates.
   - Avoid generic severity statements unless they directly motivate the study.
3. Methods:
   - State design, population, time window, and primary analysis.
   - Present routine clinical adjudication as a method, not as novelty.
   - Separate primary analysis from secondary or subgroup analyses.
4. Results:
   - Keep the main denominator visible.
   - Use plain comparison language such as `records tested by both methods` when appropriate.
   - Avoid opaque gatekeeping terms such as `interpretable` unless the manuscript explicitly defines them and the audience needs them.
5. Conclusions:
   - State what the results define or clarify.
   - Say where the approach is most informative.
   - Preserve the role of existing standards when warranted, without creating a strawman.

## Sentence-Level Guardrails

- Do not use conversational phrases such as `the clinically important question is` unless rewritten formally.
- Do not write promotional claims such as `revolutionary`, `groundbreaking`, or `game-changing`.
- Do not attack prior studies. Prefer `further evidence is needed` or `remains less clearly characterized` over `limited by` unless a critique is necessary and supported.
- Do not over-summarize. Let the study's design, denominator, and analysis carry the force.
- Do not direct-quote source articles unless the user explicitly asks. Paraphrase with citation-aware accuracy.

## Useful Patterns

- `Prior studies have established that...`
- `What remains less clearly characterized is...`
- `Here, we evaluated...`
- `The primary analysis compared... Secondary analyses assessed...`
- `These findings define the settings in which...`
- `...while preserving the role of...`
