---
name: czf-writing-skill
description: Orchestrate the user's preferred manuscript workflow: first use nature-masterclass-writing-skill for scientific structure and argument, then ajhg-polishing-skill for elegant AJHG/Cell-style prose, then czf-formatting-skill for Word formatting. Use when the user asks to write, revise, polish, or prepare a CZF manuscript or manuscript section end to end.
---

# CZF Writing Skill

## Required Sequence

Use this skill as an orchestrator. Do the work in this order:

1. **Scientific writing pass**: Use `nature-masterclass-writing-skill` first. Establish the main claim, IMRaD logic, reviewer-facing argument, section function, and evidence hierarchy. Do not polish around weak scientific logic.
2. **Prose polishing pass**: Use `ajhg-polishing-skill` next. Convert the settled content into restrained, concept-first, high-level scientific prose. If the user writes `ajhg-poilsh-skill`, treat it as `ajhg-polishing-skill`.
3. **Formatting pass**: Use `czf-formatting-skill` last to apply the project's Word manuscript formatting.

## If CZF Formatting Skill Is Missing

If `czf-formatting-skill` is absent, create it from the current `submission/JOI/Manuscript_czf.docx` formatting, excluding comments, before formatting any manuscript output.

## Operating Principles

- Content before polish; polish before formatting.
- Never invent data, citations, sample sizes, dates, analyses, or journal requirements.
- Treat clinical adjudication, subgroup analysis, sensitivity analysis, and limitations according to their real methodological role; do not inflate routine methods as novelty.
- When editing a DOCX, preserve unrelated sections and user comments unless the user asks to remove them or the edited section is being replaced.
- For final manuscript files, run document structural checks and the Documents render workflow when the environment supports it.
