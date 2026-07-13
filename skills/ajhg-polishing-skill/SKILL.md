---
name: ajhg-polishing-skill
description: Polish biomedical and scientific manuscripts, abstracts, summaries, cover letters, and response text in a restrained AJHG/Cell-style prose, using the bundled AJHG Perspective PDF style exemplar when available. Use when the user asks for AJHG style, Cell/AJHG-like elegance, or refined scientific prose after the scientific content is already decided.
---

# AJHG Polishing Skill

## Purpose

Use this skill after the scientific argument is mostly fixed. The goal is not to make prose casual, promotional, or ornate. The goal is controlled elegance: concept-first framing, precise nouns, calm verbs, and a clear account of what the work establishes, clarifies, tests, or enables.

## Required Style-Reading Step

At the start of every invocation, re-read the bundled AJHG style exemplar:

- `references/ajhg-dyadic-approach-style-exemplar.pdf`
- `references/ajhg-style-notes.md`

Do not rely on memory from previous sessions or previous polishing jobs. First inspect the PDF directly when PDF text extraction or visual reading is available. Read the Summary, Introduction opening, and at least several body paragraphs to recalibrate grammar, paragraph rhythm, transitions, hedging, and conceptual framing before touching the user's text. Use `references/ajhg-style-notes.md` as a compact backup or orientation, not as a replacement when the PDF can be read.

This rereading step is mandatory because repeated polishing from memory can drift toward generic high-level biomedical prose. If direct PDF reading is not technically available, disclose that limitation and use `references/ajhg-style-notes.md` as the fallback, but do not pretend the PDF was reread.

Do not copy the exemplar's content, citations, disease examples, or distinctive phrases into the user's manuscript unless they are scientifically appropriate and supplied by the user. The PDF is a grammar and style model, not a source to cite or paraphrase.

## Style Model

The model is the prose logic common in AJHG/Cell perspective and summary writing:

- Begin with the conceptual or clinical problem, not generic background.
- Acknowledge prior work without attacking it.
- State the unresolved need as something to characterize, delineate, clarify, locate, or test.
- Use abstract nouns only when they sharpen the argument: value, yield, distribution, relationship, framework, setting, or context.
- Prefer restrained verbs: establish, characterize, evaluate, assess, compare, support, preserve, quantify, and test.
- Use `Here, we...` sparingly and only when it cleanly identifies the contribution.
- Keep repeated key terms stable. Do not cycle synonyms for variety.
- Prefer balanced clauses that state complexity and then the need for a clearer framework: `X is complex, yet...`; `Whereas prior work..., current evidence...`; `It is essential that... while...`.
- Use careful scope markers such as `preferably`, `when feasible`, `when warranted`, `in this setting`, and `for this population` when they preserve scientific accuracy.

## Abstract Workflow

1. Identify the central contribution in one sentence:
   `This study evaluates where [test/intervention/phenomenon] is most informative in [population/context], using [design/analysis].`
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
   - Keep the analysis population, counting unit, and eligible record count visible.
   - Use plain comparison language such as `records tested by both methods` when appropriate.
   - Avoid opaque gatekeeping terms such as `interpretable` unless the manuscript states an operational criterion and the audience needs it.
5. Conclusions:
   - State what the results establish, clarify, or support.
   - Say where the approach is most informative.
   - Preserve the role of existing standards when warranted, without creating a strawman.

## Sentence-Level Guardrails

- Do not use conversational phrases such as `the clinically important question is` unless rewritten formally.
- Do not write promotional claims such as `revolutionary`, `groundbreaking`, or `game-changing`.
- Do not attack prior studies. Prefer `further evidence is needed` or `remains less clearly characterized` over `limited by` unless a critique is necessary and supported.
- Do not over-summarize. Let the study's design, analysis population, and results carry the force.
- Reserve `define`, `defined`, `definition`, and related forms for formal nomenclature or a necessary operational criterion. Do not use them as generic rhetorical verbs for a study's contribution, results, coverage, comparison set, or clinical value.
- Prefer `analysis population`, `eligible records`, `total`, or the named counting unit over the abstract label `denominator` in reader-facing prose and tables.
- Do not add explanatory main tables whose columns merely restate claims, limitations, or `Scope`, especially rows dominated by `Not ...`, `outside ...`, or generic interpretation. Keep a table when it reports data, methods, settings, or results that readers need to compare; place concise inference limits in prose, notes, or legends.
- Avoid a generic `Interpretation` column. Name the specific scientific content instead, such as `comparison`, `evidence source`, `counting unit`, or `inference limit`, and omit the column when it adds no data.
- Do not direct-quote source articles unless the user explicitly asks. Paraphrase with citation-aware accuracy.
- Do not imitate the exemplar mechanically. Preserve the user's scientific meaning, target journal, article type, and data structure.

## Useful Patterns

- `Prior studies have established that...`
- `What remains less clearly characterized is...`
- `Here, we evaluated...`
- `The primary analysis compared... Secondary analyses assessed...`
- `These findings identify the settings in which...`
- `...while preserving the role of...`
