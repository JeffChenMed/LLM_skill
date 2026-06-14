---
name: czf-formatting-skill
description: Apply the user's CZF manuscript formatting style based on the current Manuscript_czf.docx format reference, excluding comments. Use when formatting biomedical manuscript DOCX files for this project or when czf-writing-skill reaches its formatting step.
---

# CZF Formatting Skill

## Purpose

Apply the manuscript formatting style used in the user's `Manuscript_czf.docx` without carrying over comments. This skill is a formatting layer, not a writing or scientific-editing layer.

## Asset

Use `assets/Manuscript_czf_format_reference.docx` as the local style and layout reference. It was derived from the current `submission/JOI/Manuscript_czf.docx` with Word comments and comment anchors removed.

## Workflow

1. Preserve the user's manuscript content unless explicitly asked to edit text.
2. Use the format reference to match document-level styling: page setup, paragraph rhythm, heading hierarchy, abstract/body/reference/figure-legend appearance, and overall Word style behavior.
3. Do not include comments, comment ranges, or reviewer markup in the formatted output unless the user explicitly asks for comments.
4. Set document metadata author/creator and last modified by fields to Zefu Chen for formatted DOCX/XLSX outputs. When practical, remove stale generator or local-user metadata such as python-docx, openpyxl, WPS Office, Cocoon into butterfly, hdid, and userId.
5. Keep EndNote/reference fields if they are already part of the working manuscript and the user has not asked to flatten them.
6. After formatting a DOCX, run the Documents skill render-and-verify workflow when available. If LibreOffice/soffice is missing, perform structural DOCX checks and disclose that visual render QA could not be completed.

## Guardrails

- Do not treat the format reference as source content.
- Do not overwrite the user's manuscript without an explicit request.
- Do not remove scientific content, figures, tables, references, or fields as part of formatting unless asked.

