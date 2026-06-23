---
name: czf-formatting-skill
description: Apply CZF manuscript DOCX formatting for biomedical submission files, including Manuscript_czf style transfer, submission-ready page structure, figure/legend placement, table/figure citation emphasis, metadata cleanup, and render QA. Use when formatting biomedical manuscript DOCX files for this project, preparing JOI/Nature/AJHG-style submission manuscripts, fixing figure legends/tables/references formatting, or when czf-writing-skill reaches its formatting step.
---

# CZF Formatting Skill

## Purpose

Apply the user's CZF manuscript formatting style without changing scientific content. This skill is a formatting layer, not a writing or scientific-editing layer.

## Assets And Scripts

- Use `assets/Manuscript_czf_format_reference.docx` as the local style and layout reference. It was derived from the current `submission/JOI/Manuscript_czf.docx` with Word comments and comment anchors removed.
- Prefer `scripts/czf_manuscript_format.py` for repeatable post-processing when a manuscript needs figure-page reconstruction, figure-legend normalization, Introduction pagination, or bold Table/Figure citations.

## Core Workflow

1. Preserve the user's manuscript content unless explicitly asked to edit text.
2. Use the format reference to match page setup, paragraph rhythm, heading hierarchy, abstract/body/reference/figure-legend appearance, and overall Word style behavior.
3. Do not include comments, comment ranges, or reviewer markup in the formatted output unless the user explicitly asks for comments.
4. Set document metadata author/creator and last modified by fields to Zefu Chen for formatted DOCX/XLSX outputs. When practical, remove stale generator or local-user metadata such as python-docx, openpyxl, WPS Office, Cocoon into butterfly, hdid, and userId.
5. Keep EndNote/reference fields if they are already part of the working manuscript and the user has not asked to flatten them.
6. After formatting a DOCX, run the Documents skill render-and-verify workflow when available. If LibreOffice/soffice fails on a Dropbox or non-ASCII path, copy the DOCX to an ASCII temporary directory for conversion, then copy QA outputs back to the workspace.

## Manuscript Structure Rules

- Keep `ABSTRACT` at the start of the manuscript.
- Force `INTRODUCTION` to begin on a new page with an explicit paragraph page break before the heading. Do not rely on accidental pagination from prior content.
- Preserve the existing heading ladder for `RESULTS`, `DISCUSSION`, `METHODS`, `ACKNOWLEDGEMENTS`, `AUTHOR CONTRIBUTIONS`, and `REFERENCES` unless the user requests a journal-specific restructure.
- Do not move, remove, or rewrite scientific content, references, tables, figures, or fields as part of formatting unless asked.

## Figure And Legend Rules

Use this structure for submission manuscripts unless the user explicitly asks for a separate centralized legend section:

1. Convert each final figure PDF to a high-resolution JPG.
2. Insert figures after `REFERENCES`.
3. Put each figure block on its own page: figure JPG first, then its matching legend immediately below it, then a page break before the next figure.
4. Use inline images, not floating or anchored images, unless the user explicitly needs a different layout.
5. Scale the image to leave enough room for the legend on the same page. If a double-spaced legend overflows, shrink the image modestly before allowing a split page.
6. Do not create a standalone `Figure Legends` page when figure legends are supposed to be attached to each figure.

Figure legend formatting:

- The legend title sentence, e.g. `Fig. 1. Study cohort...`, must be bold.
- The legend body must not be bold.
- Legend font size must match body text. For the current CZF manuscript template this is 12 pt Times New Roman.
- Legend line spacing must match body text. For the current CZF manuscript template this is double spacing.
- Legend paragraphs should use the same body-text font system as the rest of the manuscript.

## In-Text Table/Figure Citation Rules

Before `REFERENCES`, bold numbered table and figure citations wherever they appear in prose. Bold only the citation phrase, not the entire sentence.

Match at least these forms:

- `Figure 1`, `Figures 1 and 2`
- `Fig. 2`, `Figs. 2 and 3`
- `Table 1`, `Tables 1 and 2`
- `Supplementary Table 3`
- Compound parentheticals such as `Fig. 5, Table 2, and Supplementary Table 5`

Do not apply this rule to the reference list itself.

## Validation Checklist

After formatting, verify structurally and visually:

- `INTRODUCTION` has explicit page-break-before formatting.
- Inline image count matches the expected figure count.
- Each figure page contains one figure followed immediately by its matching legend.
- Each legend title is bold; each legend body is not bold.
- Legend font size and line spacing match body text.
- All numbered Table/Figure/Supplementary Table citations before `REFERENCES` are bold.
- Render DOCX to PDF/PNG and inspect all pages, especially Introduction and the final figure pages, for blank pages, clipping, overlap, shifted images, or split legends.

## Guardrails

- Do not treat the format reference as source content.
- Do not overwrite the user's manuscript without an explicit request or a backup.
- Do not remove scientific content, figures, tables, references, fields, or metadata that the user needs preserved.
- Use structural checks plus rendered-page QA; do not claim success based only on XML or text extraction.
