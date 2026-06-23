# PUMCH/Nan Wu Cover Letter Template Contract

Use `../assets/pumch-nanwu-cover-template.docx` as the canonical DOCX package only for PUMCH/Nan Wu template-based cover-letter deliverables. This contract is derived from `coverletter_20260618_LancetDigit.docx` and controls formatting, layout, locked institutional blocks, signature images, and closing structure for that template. Do not apply this contract to an existing non-template cover letter unless the user explicitly asks to convert it to the PUMCH/Nan Wu template.

## Core Rule

Do not recreate this cover-letter format from a blank DOCX when the task calls for the PUMCH/Nan Wu template. Copy the template DOCX package and replace only the allowed variable text slots. The template controls the Word formatting; the CZF skill controls the scientific argument.

## Non-Applicability

If the user is revising an existing cover letter with a different institution, corresponding author, signature block, or no images, preserve that document's existing head and tail format. Do not add the PUMCH logo, handwritten signature image, Nan Wu affiliation block, or no-`Sincerely` closing rule unless the user explicitly asks for a PUMCH/Nan Wu template conversion.

## Page And Style Tokens

- Page size: US Letter, `12240 x 15840` twips.
- Margins: top/right/bottom/left all `1440` twips (1 inch).
- Header/footer distance: `708` twips each; gutter `0`.
- Columns: one column, `w:space="708"`.
- Default visible font: Times New Roman, 11 pt (`w:sz="22"`), black.
- East Asian font in locked/template runs: Songti/Chinese serif where present; preserve it.
- Line spacing on visible paragraphs: `w:line="276"`, `w:lineRule="auto"`.
- Body style: `Normal (Web)` / style id `a3` for editor block, salutation, opening, body, closing, and signature-image paragraph.
- Sender and typed signature blocks use `Normal` with direct paragraph/run formatting from the template.
- Do not introduce tables, text boxes, colored rules, decorative headings, cover pages, footers, or boxed callouts.

## Media And Relationships

Preserve the template media package and relationships unless the user explicitly supplies a different sender/signature asset.

- `word/media/image1.png`: PUMCH letterhead/logo image, original bitmap `886 x 214`, embedded in paragraph 0 with extent `2577465 x 528955` EMU.
- `word/media/image2.tiff`: handwritten signature image, original bitmap `209 x 82`, embedded in the signature-image paragraph with extent `1261745 x 539115` EMU.
- Preserve `word/header1.xml` even though it is visually blank.
- Preserve the mailto relationship for `dr.wunan@pumch.cn` in the sender block.

## Locked Document Skeleton

For the same corresponding author/template owner, keep these blocks exactly in wording and formatting.

1. Paragraph 0: right-aligned sender line with the PUMCH logo followed by `Peking Union Medical College Hospital`.
2. Paragraph 1: right-aligned `No.1 Shuaifuyuan`.
3. Paragraph 2: right-aligned `Beijing, China`.
4. Paragraph 3: right-aligned `+(86)13520846110`.
5. Paragraph 4: right-aligned `dr.wunan@pumch.cn`, preserving the mailto hyperlink.
6. Paragraph 14: handwritten signature image only.
7. Paragraphs 15-33: the typed Nan Wu signature/affiliation/contact block exactly as in the template:
   - `Nan Wu, M.D.`
   - `on behalf of all co-authors`
   - blank line
   - bold `Department Vice Chairman, Chief Surgeon & Professor`
   - `Department of Orthopedic Surgery, Peking Union Medical College Hospital (PUMCH)`
   - blank line
   - bold `Laboratory chief`
   - `Key Laboratory of Big Data for Spinal Deformities, Chinese Academy of Medical Sciences (CAMS), https://spinebigdata.com/`
   - blank line
   - bold `PI `, preserving the trailing space
   - `Peking Union Medical College (PUMC) & CAMS`
   - `State Key Laboratory of Complex Severe and Rare Diseases`
   - blank line
   - bold `Co-founder`
   - `Deciphering disorders Involving Scoliosis and COmorbidities (DISCO) study`
   - blank line
   - `Address: No.1 Shuaifuyuan, Beijing 100730`
   - `Tel: +8613520846110`
   - `E-mail: dr.wunan@pumch.cn/nanwu86@gmail.com`

Do not add `Sincerely`, `Yours sincerely`, or another generic sign-off to this template.

## Variable Text Slots

Only these areas should normally change.

- Editor block: one `Normal (Web)` paragraph with three soft-line-separated lines: editor name, editorial title, journal name. Italicize the journal name within the same paragraph.
- Salutation: `Dear Dr. [Surname]` with no comma, unless the journal/editor convention requires otherwise.
- Opening sentence: `We are pleased to submit our manuscript entitled "[Title]" for consideration as an [Article Type] in/at [Journal].` Italicize the journal name.
- Scientific body: use `Normal (Web)` paragraphs matching the template line spacing and run size. The body may contain CZF-style scientific argument, but it must not create a new visual system.
- Closing sentence: follow the template pattern, normally `Thank you and the editorial team for considering our submission. We look forward to the opportunity for our manuscript to be reviewed by [Journal].` Italicize the journal name.

## Implementation Method

1. Copy `assets/pumch-nanwu-cover-template.docx` to the output path.
2. Modify `word/document.xml` directly, or use a helper that preserves paragraph properties and run properties from the template.
3. Replace text only inside variable slots; clone template paragraph properties for any inserted body paragraphs.
4. Keep locked paragraphs as copied OOXML whenever possible, not as reconstructed text.
5. Preserve media files, content types, relationships, section properties, header references, and existing styles.
6. If the body needs more or fewer paragraphs than the template, insert/remove only within the scientific body zone between the opening paragraph and the closing paragraph.

## Final Verification

Before delivering a DOCX generated with this template, verify:

- Page size and margins match the template.
- `word/media/image1.png` and `word/media/image2.tiff` remain present when using the same sender/signature.
- The logo paragraph and signature-image paragraph still contain drawing elements.
- Locked sender and Nan Wu signature blocks match the template text sequence, run-level emphasis, and paragraph alignment.
- The email line keeps the sender hyperlink where present.
- No `Sincerely` or generic replacement signature appears.
- No tracked changes or comments remain unless explicitly requested.
- Render with the Documents skill when LibreOffice/`soffice` is available; otherwise perform structural OOXML checks and disclose that visual render QA was skipped.