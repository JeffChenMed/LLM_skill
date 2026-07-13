---
name: czf-formatting-skill
description: Apply or audit biomedical manuscript DOCX formatting while preserving scientific content, tables, references, and figure pixels. Use when matching a user-provided Manuscript.docx, transferring page setup, fonts, sizes, paragraph spacing, heading hierarchy, bibliography formatting, figure embedding and legends, preparing CZF/Genome Medicine/AJHG/Nature-style Word files, or diagnosing why a generated DOCX differs from a reference.
---

# CZF Formatting Skill

## Scope

Treat formatting as a separate layer. Do not rewrite scientific content, alter table values, or edit figure artwork unless the user explicitly requests those changes.

## Reference precedence

1. Use a user-provided DOCX as the controlling format reference whenever one is supplied.
2. Use `assets/Manuscript_czf_format_reference.docx` only when no user reference exists.
3. Never let bundled defaults override a supplied reference. In particular, do not assume double spacing, centered author blocks, a 16 pt title, forced Introduction pagination, centralized legends, or unembedded figures.
4. Inspect both style definitions and direct paragraph/run formatting. A reference may use `Normal` plus direct formatting rather than named Heading or Caption styles.
5. Treat the user's explicit section order, page-break, table-placement, and figure-placement instructions as overrides to both the reference and bundled defaults.

## Required workflow

### 1. Establish the preservation boundary

Before editing, record hashes for source manuscript text and figure files. Treat normalized paragraph text, table-cell text, equations, citations, references, and image pixels as frozen unless instructed otherwise.

Splitting one legend body into panel-specific paragraphs is a formatting operation, but verify that normalized text remains identical.

### 2. Audit the reference and target

Run:

```bash
python scripts/audit_docx_reference_format.py \
  --reference reference.docx \
  --target manuscript.docx \
  --expected-figures 7 \
  --json format_audit.json
```

Review at least:

- page size, margins, header/footer distances, page numbers, and line numbering; count PAGE fields in every footer part and require exactly one visible page-number field unless the reference explicitly requires otherwise;
- body font, size, alignment, line spacing, paragraph spacing, and indentation;
- title and front-matter alignment and spacing;
- section/subsection font hierarchy and pagination;
- bibliography line spacing, hanging indentation, and item spacing;
- figure count, inline versus anchored placement, image width, page breaks, and legend formatting;
- requested section order and every requested page break, including whether an abstract is isolated between two breaks;
- whether each visible figure drawing occurs inside the requested Figure Legends section and is paired with the correct legend;
- comments, tracked changes, stale identity metadata, and orphaned visible content.

Do not claim a match from font names or palette alone.

### 3. Implement reference-derived formatting

Prefer a repeatable builder or post-processing script. Derive values from the supplied reference; do not hardcode generic CZF values when they conflict.

Preserve reference page geometry by starting from a copy of the reference, clearing only the document body, and retaining the section properties, headers, footers, styles, and page-number fields that control layout. Recreate missing styles only when required by target content.

If the target contains tables absent from the reference, preserve their content and use a restrained, readable grid without inventing a new document-wide style system.

Before building, write a short structure contract containing the required top-level section order, headings that start new pages, whether each main table starts a new page, and whether figures must be embedded beside their legends. Implement this contract in the repeatable builder rather than by manually inserting breaks into one output file.

### 4. Handle figures explicitly

Distinguish two outputs:

- **Embedded review manuscript**: contains the expected number of inline images.
- **Journal-clean manuscript**: may contain legends but no images only when that output is explicitly intended.

If the user asks whether figures are embedded, report the inline shape count for each DOCX. Media files present inside the ZIP package do not count as embedded figures unless referenced by a visible drawing.

When the reference embeds figures:

1. Use inline drawings, not floating/anchored drawings, unless the reference does otherwise.
2. Preserve each image's aspect ratio and source pixels.
3. Match reference width behavior; do not shrink every image merely to force its full legend onto one page if the reference allows legend spillover.
4. Follow reference page-break placement.
5. Match legend font, size, line spacing, paragraph spacing, bold title treatment, and panel-paragraph structure.

For wide multi-panel figures, inspect the effective embedded size rather than the source pixel count alone. If labels become unreadable at portrait text width and the user prioritizes readability, place the Figure Legends block in an explicit landscape next-page section and fit each image within both the section width and height. Store the portrait width and height before creating the new section, then assign the landscape width and height explicitly; never rely on a chained swap through live section proxies, which can produce a square page. Preserve source pixels and aspect ratio, retain the reference typography for legends, and audit the section break, orientation, image dimensions, footer linkage, and that every section is either the reference page size or its exact landscape rotation.

When the user asks for figures "in Figure Legends," create a visible `FIGURE LEGENDS` heading, place every inline drawing after that heading, and keep each drawing adjacent to its corresponding legend. A correct media count alone is insufficient; images appended outside the section or present only inside the DOCX ZIP fail this requirement.

### 5. Validate before delivery

Verify structurally:

- normalized manuscript text is unchanged;
- table-cell text is unchanged;
- source figure hashes are unchanged;
- expected inline image count and zero unexpected anchors;
- requested top-level section order and page-break-before properties;
- requested table page starts;
- every expected figure drawing occurs after the Figure Legends heading and has a visible matching legend before the next drawing;
- reference-format audit passes;
- comments and stale people metadata are absent;
- page-number and line-number fields remain present when required, with exactly one PAGE field across active footer parts unless an explicit section-specific design requires more.
- every section uses the reference page dimensions or their exact width-height rotation; reject square or otherwise nonstandard sections introduced by an orientation bug.

Render the DOCX when LibreOffice/Word rendering is available and inspect the title page, section transitions, references, every figure page, and long legends. If rendering is unavailable, state that visual pagination remains unrendered and rely on structural checks without overstating completion.

## Existing post-processor

Use `scripts/czf_manuscript_format.py` for citation bolding and figure-block reconstruction when appropriate. Pass reference-derived font, line-spacing, and image-height values rather than accepting generic defaults blindly.

## Metadata

For final CZF outputs, set author/creator and last modified by to Zefu Chen when requested by the project. Remove comments, comment anchors, and stale local identities while preserving EndNote fields unless the user asks to flatten them.

## Guardrails

- Do not treat the reference as source content.
- Do not overwrite the user's only copy; make a backup.
- Do not silently deliver a clean manuscript when the user expects embedded figures.
- Do not change manuscript wording or figure artwork to make pagination easier.
- Do not call a document reference-matched until structural comparison and, when available, rendered-page QA both pass.
