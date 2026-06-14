---
name: czf-writing-skill
description: Orchestrate the user's preferred manuscript workflow: first use nature-masterclass-writing-skill for scientific structure and argument, then ajhg-polishing-skill for elegant AJHG/Cell-style prose, then czf-formatting-skill for Word formatting. Use when the user asks to write, revise, polish, or prepare a CZF manuscript or manuscript section end to end.
---

# CZF Writing Skill

## Required Sequence

Use this skill as an orchestrator. The sequence below is mandatory for end-to-end CZF manuscript work. Do not skip, merge, or reorder these passes unless the user explicitly asks for only one named subtask.

1. **First, use `nature-masterclass-writing-skill` to write or revise the scientific structure.** Establish the main claim, IMRaD logic, reviewer-facing argument, section function, evidence hierarchy, and limits of inference. Do not polish around weak scientific logic.
2. **Second, use `ajhg-polishing-skill` to polish the settled prose.** Convert the scientifically settled content into restrained, concept-first, high-level AJHG/Cell-style biomedical prose. If the user writes `ajhg-poilsh-skill`, treat it as `ajhg-polishing-skill`.
3. **Third, use `czf-formatting-skill` to format the final manuscript output.** Apply the project's Word manuscript formatting only after the writing and polishing passes are complete.

When reporting work back to the user, preserve this order in the summary: Nature Masterclass writing pass -> AJHG polishing pass -> CZF formatting pass.

## If CZF Formatting Skill Is Missing

If `czf-formatting-skill` is absent, create it from the current `submission/JOI/Manuscript_czf.docx` formatting, excluding comments, before formatting any manuscript output.

## Operating Principles

- Content before polish; polish before formatting.
- Never invent data, citations, sample sizes, dates, analyses, or journal requirements.
- Treat clinical adjudication, subgroup analysis, sensitivity analysis, and limitations according to their real methodological role; do not inflate routine methods as novelty.
- When editing a DOCX, preserve unrelated sections and user comments unless the user asks to remove them or the edited section is being replaced.
- For final manuscript files, run document structural checks and the Documents render workflow when the environment supports it.
