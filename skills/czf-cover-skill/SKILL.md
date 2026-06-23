---
name: czf-cover-skill
description: >-
  Draft, revise, or critique high-impact biomedical, clinical AI, genetics,
  rare disease, or translational medicine journal cover letters using the CZF
  three-question structure. Use for template-preserved PUMCH/Nan Wu DOCX cover
  letters, and for polishing existing non-template cover letters while preserving
  their current sender block, closing/signature, and image/no-image format. Use
  for journals such as NEJM AI, Nature Medicine, Cell, AJHG, Lancet Digital
  Health, Journal of Infection, or similar venues, especially when manuscripts
  include large cohorts, diagnostic frameworks, real-world validation, open
  resources, or clinical translation claims.
---
# CZF Cover Skill

## Core Principle

Use this skill to turn a manuscript cover letter into a persuasive editorial argument, not a polite submission note.

The cover letter must answer three non-compressible questions:

1. **Why is this problem important?**
   Frame the problem as a **fundamental limitation** in current scientific, clinical, diagnostic, or technical logic.
2. **What did this work change?**
   Present the work as a **conceptual and/or technical breakthrough**, not merely a new dataset, model, tool, or incremental benchmark.
3. **Why should the editor believe it is mature, credible, and translatable?**
   Anchor the claim in **clinical validation**, preferably using prospective, external, multicenter, real-world, or deployment-relevant evidence.

Do not compress these questions into generic novelty language. A high-impact cover letter should make the editor feel that the manuscript identifies a field-level constraint, introduces a real way around it, and has enough evidence to matter beyond the authors' dataset.

## Formatting Scope: First Identify The Cover-Letter Type

Before editing or creating a DOCX cover letter, identify whether the task is template-based or existing-format editing.

**Use the PUMCH/Nan Wu template only when it is applicable.** This means the user asks for the PUMCH/Nan Wu cover-letter template, the corresponding author is Nan Wu/PUMCH, the existing document already uses that template, or the user explicitly asks to convert to that template. In those cases, read `references/pumch-cover-template-contract.md` and use `assets/pumch-nanwu-cover-template.docx` as the source package unless the user explicitly requests another template.

**Do not force the PUMCH/Nan Wu template onto existing non-template letters.** When revising an existing DOCX with another sender, institution, signature block, or no images, preserve that existing head and tail format. Do not add a PUMCH logo, handwritten signature image, Nan Wu affiliation block, or remove a conventional sign-off such as `Sincerely` unless the user explicitly requests a template conversion.

Hard rules:

- For PUMCH/Nan Wu template output, do not create a full DOCX cover letter from a blank document and do not approximate the template by manually recreating margins, fonts, images, or signature text.
- For PUMCH/Nan Wu template output, preserve locked template blocks exactly for the same corresponding author: institutional sender block, PUMCH logo, handwritten signature image, Nan Wu typed signature/affiliation/contact block, media relationships, and section properties.
- For PUMCH/Nan Wu template output, replace only variable slots: editor block, salutation, manuscript title/article type/journal in the opening sentence, scientific body paragraphs, availability/submission-package facts, and the journal name in the closing sentence.
- For PUMCH/Nan Wu template output, do not add generic sign-offs such as `Sincerely`; this template closes with the source-style thank-you paragraph followed directly by the signature image and Nan Wu block.
- For existing non-template DOCX edits, preserve current page style, sender block, image/no-image state, closing/signature, and correspondence identity unless the user asks for a format change.
- If the user provides a different corresponding author or signature asset, adapt only the explicitly supplied identity/signature fields and preserve the chosen document format.
- Before finalizing, structurally verify the output against the chosen format: PUMCH template contract for PUMCH-template output, or the original document structure for existing-format edits.

## Required Argument Structure

Build the cover letter around this sequence:

1. **Submission identity**
   State the manuscript title, article type, target journal, and corresponding editorial addressee.

2. **Optional credibility or trajectory, only when it helps**
   Include prior work, group trajectory, or institutional credibility only when it materially strengthens the editorial argument. Omit this block when it would become a CV paragraph or distract from the manuscript-specific problem.

3. **Manuscript-specific fundamental limitation**
   Define the core limitation in the field's current logic. Prefer limitations that are conceptual, diagnostic, methodological, or translational rather than merely operational.

4. **Breakthrough**
   Explain exactly what the manuscript changes. Separate a conceptual breakthrough from a technical breakthrough when both exist.

5. **Clinical validation**
   Show that the work has been tested under conditions that matter to editors: scale, independent cohorts, temporal validation, external baselines, real-world noise, clinical heterogeneity, integration with clinical workflows, or accessible deployment.

6. **Clinical and journal significance**
   Translate the validation into impact: automation, accuracy, accessibility, generalizability, interpretability, equity, workflow efficiency, or a realistic route to clinical use.

7. **Availability and transparency**
   State system, code, model, data, or supplementary availability when applicable.

8. **Submission package and closing**
   List included materials only after the scientific argument is complete. Close briefly and professionally.

## Non-Negotiable Formatting Essence

Use **bolded micro-headlines** for every major point as an argument device, but do not let this create a new DOCX visual system. In PUMCH-template DOCX output, any numbered section labels or bold labels must still use the template paragraph family, font size, spacing, and margins.

Apply this rule at two levels:

- **Section-level labels**: Use numbered, manuscript-specific labels when they help the editorial argument, but keep them inside the PUMCH template body style for DOCX output. Do not force generic headings such as "Addressing fundamental limitations" into every letter. The first three scientific labels, when used, should normally be numbered: **1. [problem-specific limitation]**, **2. [specific breakthrough/framework]**, and **3. [what the validation or benchmark newly reveals]**.
- **Point-level labels**: Begin each limitation, breakthrough, bottleneck, or validation pillar with a bold label plus colon, such as "**A many-to-many mapping problem:**", "**Lack of quantitative data:**", "**Catastrophic forgetting during domain adaptation:**", or "**Hallucinated outputs in gene prioritization:**".

Each bolded label must name the issue before the explanation begins. Do not hide the key claim in the middle of a paragraph.

Other source-derived essentials:

- **Claim-first figure choreography**: Introduce a point, show the figure, then use a caption that states what the figure proves.
- **Contrastive framing**: Use "rather than..." / "instead of..." / "bypasses..." to show what the work replaces, not only what it adds.
- **Bottleneck grammar**: Name the bottleneck, explain why naive approaches fail, state the design choice, then state the practical gain.
- **Numbers as trust anchors**: Put sample sizes, cohort types, and performance metrics inside the argument, not in a detached statistics list.
- **Trajectory paragraph is optional**: Use prior publications or group trajectory only when they make the current manuscript more credible. Do not include a trajectory paragraph by default.

## The Three Questions in Detail

### 1. Fundamental Limitation

Do not begin from "the disease is common/rare/important" unless that is truly the manuscript's main contribution. High-impact editors already know many problems are important. The cover letter must show why the current way of solving the problem is structurally insufficient.

Use the following pattern:

```text
Current [clinical/scientific/technical] logic encounters [number] fundamental limitations.

First, [limitation 1]: [why the current framework creates ambiguity, inefficiency, bias, missingness, or unreliability].

Second, [limitation 2]: [what kind of evidence or capability the current framework lacks].
```

Strong limitation types include:

- A many-to-many mapping problem that makes existing matching logic ambiguous.
- Loss of patient-level information when heterogeneous cases are collapsed into canonical disease entities.
- Dependence on manually curated summaries that omit quantitative evidence.
- Lack of temporal, frequency, co-occurrence, or individual-level clinical detail.
- A mismatch between how clinicians reason and how databases or models represent knowledge.
- A technical bottleneck that prevents a promising method from becoming clinically usable.
- A translational gap between benchmark performance and real-world clinical heterogeneity.

Weak limitation types include:

- "Diagnosis remains challenging" without explaining why.
- "Current tools have low accuracy" without identifying the mechanism.
- "More data are needed" without saying what kind of evidence is missing.
- "AI has potential" without a concrete failure mode.

### 2. Breakthrough

Describe what changed in the logic of the field, the technical architecture, or both. If the manuscript has both levels, present both levels explicitly.

Use this hierarchy:

```text
To address these limitations, we made [number] key advances.

First, [conceptual/data/resource breakthrough]: [what new evidence structure or reasoning path now exists].

Second, [diagnostic/methodological breakthrough]: [how the work changes inference, prioritization, classification, treatment selection, or clinical action].

In addition, [technical breakthrough]: [how the architecture overcomes a bottleneck that would otherwise block reliable use].
```

A **conceptual breakthrough** changes the problem representation. Examples:

- Moving from disease-level summaries to patient-level evidence.
- Bypassing predefined disorder entities.
- Comparing a proband directly with molecularly diagnosed patient cases.
- Treating diagnosis as similarity to real cases rather than matching to static labels.
- Rebuilding evidence around co-occurrence, frequency, timing, or longitudinal clinical structure.

A **technical breakthrough** changes the system's ability to solve the problem reliably. Examples:

- Expert specialization to preserve general reasoning while adding domain knowledge.
- Vocabulary or output-space constraints that prevent invalid predictions.
- Probabilistic ranking rather than unconstrained free-text generation.
- Retrieval, extraction, matching, and reasoning architectures that connect literature-scale evidence to clinical inference.
- Mechanisms that reduce hallucination, catastrophic forgetting, distribution shift, or opaque outputs.

Avoid saying "we developed a novel model" as the main claim. Say what the model makes possible that was not possible before.

### 3. Clinical Validation

Validation is where the cover letter earns editorial trust. Include enough specifics to make the claim inspectable.

Prefer validation evidence in this order:

1. Prospective or time-split validation.
2. Independent external cohorts.
3. Multicenter real-world cohorts.
4. Large leave-one-out or cross-validation analyses when appropriate.
5. Integration with clinical data or clinical workflow inputs.
6. Strong comparison against external baselines.
7. Transparent availability of system, code, model, or evaluation materials.

Use the following pattern:

```text
We evaluated [system/method] using [validation design], including [dataset/cohort types and sample sizes].

It achieved [primary result], with [relative or absolute improvement] over [baseline].

Importantly, [external/multicenter/real-world] validation supports robustness under [clinical heterogeneity, diagnostic noise, missing data, resource limits, or workflow constraints].

When integrated with [clinical modality/workflow], it [clinically meaningful result].
```

Do not simply list metrics. Translate them:

- **Mature** means tested beyond a narrow training-like dataset.
- **Credible** means the result survives external baselines, temporal splits, heterogeneity, and clinically meaningful endpoints.
- **Translatable** means a clinician, patient, lab, or health system can plausibly use it.

## Paragraph-Level Blueprint

### Opening Block

Include sender details when drafting a full formal letter:

```text
[Institution]
[Address]
[Phone/email if appropriate]

[Editor name, degree]
[Editorial title]
[Journal]

Dear Dr. [Surname],
```

Then state:

```text
We are pleased to submit our manuscript entitled "[Title]" for consideration as a [Article Type] at [Journal].
```

### Optional Credibility Or Trajectory Paragraph

Function: show continuity and authority only when it helps the manuscript-specific pitch. This paragraph is optional, not required.

Do:

- Mention only the most relevant prior publications, tools, cohorts, or discoveries.
- Tie them to the current manuscript's trajectory.
- Use this paragraph to say "we have been building toward this problem."

Do not:

- Create a CV paragraph.
- Overload with journal names if they do not advance the argument.
- Let author prestige substitute for manuscript significance.

Template:

```text
Building on our prior work in [field], including [representative advances], we recognized the need to [unmet need]. [Manuscript/system] represents a continuation of this effort and addresses [core problem] through [new framework].
```

### Fundamental Limitation Section

Function: make the editor see the current field as constrained by a deeper logic problem.

Use a numbered, manuscript-specific heading. The heading should identify the actual limitation in this manuscript, not a reusable slogan.

```text
**1. [Manuscript-specific fundamental limitation]**
```

Then write two or three named limitations. Each limitation should have:

- A short bolded label.
- A mechanism of failure.
- A consequence for clinical or scientific decision-making.

Template:

```text
Current [diagnostic/scientific] logic encounters two significant challenges.

[Limitation label]: [Current logic] relies on [current assumption]. However, [complexity/heterogeneity/missing evidence] creates [ambiguity/failure], limiting [clinical/scientific task].

[Limitation label]: [Current resources/methods] provide [summary or proxy]. However, they lack [specific quantitative or clinical evidence], preventing [desired inference].
```

### Breakthrough Section

Function: show that the manuscript changes the solution path.

Use a numbered, manuscript-specific heading. The heading may name a framework, benchmark, architecture, clinical workflow, or conceptual move.

```text
**2. [Specific breakthrough, framework, or solution path]**
```

For each advance:

- Start with "First" / "Second" only if there is a real sequence.
- Name the advance.
- Explain what it replaces or bypasses.
- Explain why it matters.
- Link to a figure if the letter includes figures.

Template:

```text
To address these challenges, we made two key advances.

First, we introduce [resource/framework], a [description] comprising [scale if appropriate]. Rather than serving as another [incremental resource], it captures [new evidence unit] and provides [foundation for inference].

Second, we propose [new logic/method] that [bypasses/replaces/extends] [current entity or assumption]. By [mechanism], the framework [clinical/scientific action].
```

For AI/LLM work, add a separate technical bottleneck paragraph when needed:

```text
With [architecture], [system] overcomes two key technical bottlenecks.

[Bottleneck label]: [Naive approach] risks [failure]. To mitigate this, we [technical design], enabling [benefit].

[Bottleneck label]: [Standard generation/prediction] is poorly suited to [task] because [failure mode]. We therefore [technical design], enabling [valid, constrained, probabilistic, interpretable, or clinically actionable output].
```

### Validation / Discovery Section

Function: make the editor trust the work and understand what the validation newly revealed. This section should not merely say that the work is credible; it should state the new phenomenon, failure mode, boundary condition, or deployment-relevant insight discovered through validation.

Use a numbered, manuscript-specific heading:

```text
**3. [What the validation newly revealed]**
```

Examples:

- **3. Revealing structured failure modes rather than random errors**
- **3. Defining where the model remains reliable under real-world heterogeneity**
- **3. Showing that clinical utility depends on evidence context, not aggregate accuracy alone**

Include:

- Dataset types.
- Sample sizes.
- Number of centers/cohorts if relevant.
- Clinical diversity or heterogeneity.
- Key performance metrics.
- Baseline comparison.
- Clinical integration result.

Template:

```text
[System] was assessed on [validation designs] including [cohorts] spanning [scope].

On [primary validation], [system] achieved [metric], with [improvement] over [baseline]. Importantly, [independent/real-world/multicenter] cohorts support robustness under [clinical condition]. When integrated with [clinical workflow/data type], it [clinically meaningful result].
```

### Significance Paragraph

Function: translate method and metrics into editorial meaning.

Use this paragraph to connect the manuscript to the journal's mission.

Strong endings emphasize:

- Broad generalizability.
- Clear clinical utility.
- Realistic AI deployment.
- A shift in paradigm, not merely a performance gain.
- Accessibility in settings lacking subspecialty expertise.

Template:

```text
Our study leverages [method/system] to overcome longstanding bottlenecks in [tasks]. This performance suggests potential to transform [clinical/scientific workflow] by enabling [automated], [accurate], and [accessible] [action] from [input/source]. We believe this addresses the need for broadly generalizable advances with clear clinical utility and provides a realistic example of [field-level transition].
```

### Availability and Submission Package

Use short, transparent statements:

```text
The system is available at [URL], with code at [URL] and model weights/data at [URL], when applicable.

This submission includes the main manuscript, [N] main figures, [N] main tables, [N] supplementary figures, [N] supplementary tables, and [N] supplementary notes/materials. All data required to evaluate the findings are included in the manuscript and supplements.
```

Only state availability that is true. When listing the submission package, use exact counts whenever they are known; do not write generic phrases such as "figures, tables, and supplementary materials" if the actual numbers can be extracted.

### Closing and Signature

For PUMCH/Nan Wu template output, the template controls the closing and signature format. Do not use a generic sign-off. Use the template closing pattern, followed directly by the handwritten signature image and Nan Wu signature/affiliation/contact block defined in `references/pumch-cover-template-contract.md`.

For existing non-template cover letters, preserve the existing closing and signature convention unless it is wrong for the target journal or the user asks to change it. A conventional `Sincerely` block, a different corresponding author, or a no-image closing is acceptable when that is the document's current format.

For plain-text PUMCH/Nan Wu drafting only, mirror the same order:

```text
Thank you and the editorial team for considering our submission. We look forward to the opportunity for our manuscript to be reviewed by [Journal].

[handwritten signature image in DOCX output]
Nan Wu, M.D.
on behalf of all co-authors

Department Vice Chairman, Chief Surgeon & Professor
Department of Orthopedic Surgery, Peking Union Medical College Hospital (PUMCH)

Laboratory chief
Key Laboratory of Big Data for Spinal Deformities, Chinese Academy of Medical Sciences (CAMS), https://spinebigdata.com/

PI 
Peking Union Medical College (PUMC) & CAMS
State Key Laboratory of Complex Severe and Rare Diseases

Co-founder
Deciphering disorders Involving Scoliosis and COmorbidities (DISCO) study

Address: No.1 Shuaifuyuan, Beijing 100730
Tel: +8613520846110
E-mail: dr.wunan@pumch.cn/nanwu86@gmail.com
```

## Figure Use in a Cover Letter

Use figures only when they materially improve editorial comprehension. This style works best for long-form high-impact cover letters where the letter is effectively a concise editorial preview.

Good figure functions:

- Figure 1: current logic and its fundamental limitation.
- Figure 2: construction of a new atlas/resource/cohort.
- Figure 3: new diagnostic or conceptual logic.
- Figure 4: technical architecture.
- Figure 5: validation and performance.

Keep figure captions declarative. They should state the role of the figure in the argument, not merely name the panel.

Do not add figures when the journal explicitly expects a short cover letter or when figures would make the letter feel like a second manuscript.

## Reviewer Suggestions

If the journal requests suggested reviewers, include them after the main letter, references, or required administrative statements.

For each reviewer, include:

- Name.
- Institutional or field identity.
- Why their expertise fits the manuscript.
- Email.

The description should justify relevance, not flatter the reviewer. Prefer expertise in the manuscript's central method, disease area, clinical workflow, or translational setting.

## Tone and Style

Use a confident, editorial tone:

- "fundamental limitations"
- "current diagnostic logic"
- "to address this challenge"
- "we made two key advances"
- "rather than serving as another..."
- "bypasses predefined..."
- "overcomes longstanding technical bottlenecks"
- "supports robustness and translational relevance"
- "real-world phenotypic heterogeneity and diagnostic noise"
- "broadly generalizable advances with clear clinical utility"

Avoid:

- Overheated claims such as "revolutionary" or "unprecedented" unless the evidence truly supports them.
- Generic novelty: "This is the first study to..."
- Vague AI language: "leverages AI to improve healthcare."
- Metric dumping without clinical interpretation.
- Long author biography.
- Unsupported journal flattery.

## Formatting Defaults

For PUMCH/Nan Wu template output, the PUMCH/Nan Wu template overrides generic manuscript-letter defaults. Use `assets/pumch-nanwu-cover-template.docx` and follow `references/pumch-cover-template-contract.md` unless the user explicitly requests a different template. For existing non-template DOCX edits, preserve the original document's formatting and image/no-image state unless the user asks for a format change. The generic defaults below apply only to plain-text drafts or non-template outputs:

- US Letter or A4 according to local/journal convention.
- Approximately 1 inch margins.
- 11 or 12 pt serif font such as Times New Roman.
- 1.15 to 1.5 line spacing depending on length and journal preference.
- Sender information at top, often right-aligned.
- Editor address and salutation before the body.
- Clear paragraph breaks.
- Bold sentence-style headings for long letters.
- Centered figure captions if figures are embedded.
- Signature block with full title and affiliation.
- References and suggested reviewers only if useful or required.

When editing an existing DOCX, preserve the user's formatting unless asked to reformat.

## Drafting Workflow

1. Identify the target journal, article type, editor if known, and whether figures/reviewer suggestions are allowed.
2. Extract the manuscript's fundamental limitation, breakthrough, and validation evidence.
3. Build a one-sentence editorial thesis:

```text
This manuscript matters because [fundamental limitation]; it changes the field by [breakthrough]; and editors can trust it because [clinical validation].
```

4. For PUMCH/Nan Wu template output, copy `assets/pumch-nanwu-cover-template.docx` and replace only the variable slots defined in `references/pumch-cover-template-contract.md`. For existing non-template DOCX edits, edit the current document in place or on a copy and preserve its existing sender/signature/image structure.
5. Draft or revise the scientific body using the paragraph-level blueprint while preserving the chosen document format: the PUMCH template style for PUMCH output, or the original page, head, tail, and image/no-image state for existing-format edits.
6. Check whether every major paragraph answers one of the three core questions.
7. Remove claims that are not supported by the manuscript.
8. Polish for restrained high-impact biomedical prose.
9. Run the template verification checklist before delivery.

## Quality Checklist

Before finalizing, verify:

- The cover-letter format matches the task: PUMCH/Nan Wu template output uses `assets/pumch-nanwu-cover-template.docx`; existing non-template edits preserve the original sender block, closing/signature, and image/no-image state.
- The opening identifies title, article type, and journal.
- Any credibility or trajectory paragraph, if included, strengthens the manuscript-specific argument and does not become a CV. Omit it when unnecessary.
- The importance argument is framed as a manuscript-specific fundamental limitation; if a numbered label is used, it begins with "1." and remains in the PUMCH template body style.
- Each limitation has a mechanism and consequence.
- The breakthrough is described as a change in logic, architecture, evidence structure, or clinical workflow; if a numbered label is used, it begins with "2." and remains in the PUMCH template body style.
- Technical breakthroughs are connected to concrete failure modes.
- The validation/discovery section explains what the validation newly revealed, not only why the work is credible; if a numbered label is used, it begins with "3." and remains in the PUMCH template body style.
- Validation includes design, sample size, independence, baselines, clinically meaningful metrics, and the new insight revealed by the validation when available.
- The clinical significance paragraph translates performance into use.
- Availability statements are true and specific, and submission-package statements include exact counts when known.
- Administrative material does not interrupt the scientific argument.
- No PUMCH logo, handwritten signature image, or Nan Wu affiliation block is added to a non-template cover letter unless the user explicitly requests that conversion.
- No private, unpublished, or identifying details are added unless the user supplied them for the final cover letter.

## Minimal Output Forms

When the user asks for a quick critique, answer in the three-question structure:

```text
1. Fundamental limitation: [strong/weak/missing; suggested revision]
2. Breakthrough: [strong/weak/missing; suggested revision]
3. Clinical validation: [strong/weak/missing; suggested revision]
```

When the user asks for a full draft, produce a complete letter with the formal blocks above.

When the user asks for revision, preserve accurate manuscript facts and strengthen only the argument, structure, tone, and clarity.





