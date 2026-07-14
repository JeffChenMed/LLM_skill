---
name: nature-masterclass-writing-skill
description: Apply Nature Masterclass scientific-writing logic to draft, review, restructure, or polish research manuscripts, abstracts, cover letters, figure legends, and IMRaD sections, using the bundled GPT-extracted Nature Masterclass reference markdown as the controlling source and requiring author confirmation of the core sentence before narrative drafting. Use when Codex needs to improve Introduction, Methods, Results, Discussion, Conclusion, title/abstract, manuscript narrative, paragraph logic, reviewer-facing argument strength, or pre-submission manuscript quality for biomedical or scientific papers.
---

# Nature Masterclass Writing Skill

## Overview

Use this skill to turn a scientific manuscript into a clear argument rather than a data dump. Treat the paper as one main claim supported by Methods, Results, figures, and Discussion; remove or move anything that does not serve that claim.

## Required Source-Reading Step

At the start of every invocation, read and use the bundled GPT-extracted Nature Masterclass reference:

- Combined reference: `references/nature-masterclass-gpt-extraction/nature-masterclass-gpt-extraction.md`
- Page-level references: `references/nature-masterclass-gpt-extraction/pages/page-001.md` through `page-065.md`
- Original source for spot checks only: `references/nature-masterclass-original.pdf`

Do not rely on memory from previous sessions or previous uses of this skill. Before drafting, reviewing, or restructuring a manuscript, inspect the relevant extracted markdown again and use it to recalibrate manuscript logic, section purpose, paragraph function, sentence-level clarity, and reviewer-facing argument. This required rereading step prevents gradual drift into generic scientific-editing habits.

First summarize the relevant Nature Masterclass principles from the extracted markdown in working notes, then apply those principles to the user's text. When the task concerns a specific section, prioritize the pages whose headings and writing principles match that section. Use the original PDF only if a page-level extraction is unclear or needs verification; do not treat the scanned PDF as the primary working source.

If the extracted markdown is unavailable, disclose that limitation and use this `SKILL.md` as the fallback. Do not pretend the Nature Masterclass reference was consulted.

## Mandatory Core Sentence Checkpoint

Before drafting new manuscript prose or restructuring a manuscript narrative, formulate one candidate core sentence that states the paper’s principal contribution and why it matters. Present the exact sentence to the user, discuss it, and obtain explicit confirmation before writing the Abstract, Introduction, Results, Methods, Discussion, title, figure legends, or cover letter.

Apply the checkpoint as follows:

1. Derive the sentence from the evidence and the author’s intended article identity, not from the most visually prominent experiment.
2. Ask the user to confirm or revise that sentence. Do not begin narrative drafting while the sentence remains disputed or ambiguous.
3. If the user has already explicitly confirmed the same sentence in the current conversation, record it in working notes and proceed without asking again.
4. Map every manuscript section to the confirmed sentence. If later evidence or feedback would materially change the central claim, pause narrative drafting and reconfirm the revised sentence.
5. Purely mechanical formatting, reference correction, or copyediting that does not alter the argument may use the manuscript’s existing confirmed thesis without reopening the checkpoint.

## Core Principle

After the checkpoint, use the confirmed one-sentence main argument as the narrative thread:

```text
This study shows that [main finding] in [population/system] using [key approach], which matters because [field/clinical/community implication].
```

Use this sentence as the narrative thread. If a paragraph, figure, table, or citation does not advance this thread, recommend deleting it, shortening it, or moving it to supplementary material.

## Workflow

1. Identify the target journal, article type, audience, and word/figure limits if available.
2. Complete the mandatory core sentence checkpoint and record the confirmed sentence.
3. Extract the primary evidence and highest-risk reviewer objections around that sentence.
4. Check whether each IMRaD section performs its proper job.
5. Edit top-down: section purpose, paragraph order, paragraph topic sentence, sentence clarity, then wording.
6. Preserve factual claims and uncertainty. Do not invent references, data, dates, sample sizes, or journal requirements.

## Introduction

Purpose: set up the objective. Do not write a general textbook review.

Use this structure:

1. Start relatively general, but only with background directly relevant to the main argument.
2. Explain what is already known from studies with similar objectives.
3. Define the gap, unresolved problem, limitation, or controversy.
4. Explain why the objective matters to the target audience.
5. End with the study objective or hypothesis; optionally add one brief statement of the principal finding.

Rules:

- Do not deviate from the main argument.
- Move from general to specific.
- Discuss prior papers that reached similar conclusions; do not hide them until Discussion.
- Make paragraphs logically connected, with one idea per paragraph.
- Write for the target audience, not only for insiders.

Useful paragraph plan:

1. Context: why this field/problem exists.
2. Current knowledge and current standard.
3. Gap or limitation in previous work.
4. Objective, approach, and contribution.

## Methods

Purpose: allow a knowledgeable reader to understand exactly what was done, why key choices were made, and whether the work can be reproduced or audited.

Check for:

- Study design, setting, time window, population, samples, and data source.
- Sample size and justification, even for retrospective or convenience cohorts.
- Inclusion and exclusion criteria, including all data exclusions.
- Randomization, blinding, adjudication, or lack thereof when relevant.
- Definitions of index tests, comparator tests, outcomes, reference standards, and analysis sets.
- Exact statistical tests, assumptions, software, thresholds, primary analyses, secondary analyses, and sensitivity analyses.
- Handling of missing data, repeated samples, discordant results, and indeterminate results.
- Data availability, repository deposition, or access restrictions.

When a method follows a previous publication exactly, cite and summarize it briefly. When any detail differs, describe the difference fully. When a method is new, describe it fully.

## Results

Purpose: present the core evidence as a clear and succinct narrative.

For each Results paragraph, use this pattern:

```text
[Link to previous paragraph.] To [aim of this analysis], we [method/approach].
We found that [key result with figure/table reference and statistics].
This suggests/shows [take-home message for this result only].
```

Rules:

- Guide readers through the most important features of the data, not every result.
- Put figures and tables to work; do not repeat every cell in prose.
- State key findings explicitly and support them with appropriate statistics.
- Add only local interpretation needed to understand the result; save broader implications for Discussion.
- Number figures, tables, and panels in the order cited.
- Use supplementary material for peripheral validation, exploratory, or low-priority results.

Common order:

1. Cohort or sample flow and baseline characteristics.
2. Primary result.
3. Secondary results.
4. Subgroup or stratified results.
5. Sensitivity and robustness analyses.

## Discussion

Purpose: evaluate the data and explain implications. Answer two questions: "Why should I trust your data?" and "Why should I care?"

Use this loose structure:

1. Begin with the culminating result or principal finding, not a second Introduction.
2. Anticipate the strongest reviewer objections and address them directly.
3. Set the key findings in context with prior literature.
4. Explain how far the results move the field beyond previous work.
5. Discuss unresolved issues, contradictions, and features that cannot be explained.
6. State limitations honestly, including design, bias, measurement, missing data, generalizability, and causal limits.
7. End with a short conclusion focused on immediate implications and future work.

Avoid:

- Repeating the Results section.
- Presenting new results.
- Ignoring flaws in the argument.
- Wandering into tedious nuances unrelated to the main argument.
- Making speculative claims that outgrow the data.

## Conclusion

Purpose: provide a short, substantiated take-home message.

The conclusion should:

- Relate directly to the stated objective.
- Be supported by the presented results.
- Explain how the result fits into the broader picture.
- Avoid new data, new claims, and inflated clinical or field-wide implications.

## Title And Abstract

Title:

- Make it accurate, specific, brief, and declarative.
- Focus on the main novel finding.
- Avoid jargon, abbreviations, question titles, puns, and unserious wording.

Abstract:

- Make it self-contained.
- State the objective and scope when not obvious from the title.
- Summarize principal methods, results, and conclusions.
- Convey the context in which the results matter.
- Do not include claims absent from the manuscript body.

## Pre-Submission Checklist

Check these before delivery:

- Is the manuscript logically organized and easy to follow?
- Is the thesis presented early?
- Do Results and Discussion address the main points and provide clear conclusions?
- Does each paragraph have one idea and a topic sentence?
- Is the writing concise, active, and free of redundant overlap between sections?
- Are terminology, units, denominators, and scales consistent?
- Are references selective, representative, and formatted for the target journal?
- Are figures complete, legible, self-contained, and cited in order?
- Does the cover letter make a strong journal-specific case without exaggeration?
