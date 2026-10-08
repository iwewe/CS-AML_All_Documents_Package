**CS-AML**

UX Specification

**Version 0.1.1**

User experience requirements for the Civil Society Anti-Money Laundering / Financial Intelligence Platform

> **Document status — v0.1.1**
> Version: 0.1.1 — Draft for Review (Proposed Internal Baseline). *[v0.1.1 · A01]*
> Supersedes: CS-AML UX Specification v0.1. The DOCX/PDF files in this repository are the unchanged v0.1 baseline (legacy); this Markdown file is the canonical source.
> Validation: not validated. No recorded approval decision, implementation test result, or independent audit exists for this baseline. Acceptance criteria in this document are targets, not evidence that tests have passed.
> CS-AML is not an external standard or certification. References to FATF, Wolfsberg, PPATK, UNODC or other bodies do not imply their endorsement.
> Changes in 0.1.1: see `CHANGELOG.md` at the repository root (audit findings A01–A16).

> **Status**  
> Draft for Review (Proposed Internal Baseline) — proposed normative UX baseline for MVP 0.1. The requirements below have not yet been validated through prototypes, usability testing or accessibility evaluation; the usability scenarios in §29 are planned, not completed. *[v0.1.1 · A01; N07]* This document defines interaction behaviour, user-facing semantics, task flow, feedback, safety, accessibility, and usability requirements. It intentionally does not define final information architecture, taxonomy, sitemap, or object hierarchy; those belong to the separate CS-AML Information Architecture Specification.

| **Document** | **Relationship** |
|----|----|
| PRD v0.1.1 | Defines product outcomes and MVP scope. *[v0.1.1 · A01]* |
| SRS v0.1.1 | Defines testable software requirements. *[v0.1.1 · A01]* |
| MVP Engineering Breakdown v0.1.1 | Defines implementation epics and stories. *[v0.1.1 · A01]* |
| Technical Stack & Repository v0.1.1 | Defines technical implementation baseline. *[v0.1.1 · A01]* |
| This UX Specification | Defines user interaction behaviour and experience quality. |
| Future IA Specification | Will define content/object organisation, taxonomy, navigation model, labels, hierarchy, and findability. |

*CS-AML Framework Suite • 2026*

# 1. Purpose and Scope

The purpose of this specification is to make the CS-AML investigation experience safe, intelligible, reviewable, and efficient for civil-society investigators working with sensitive financial intelligence. It translates product and analytical principles into interaction requirements that designers and frontend engineers can implement and test.

> **UX axiom**  
> The interface SHALL preserve analytical uncertainty rather than visually collapse it. Facts, claims, inferences, candidate matches, hypotheses, reconstructed value flows, and final assessments must remain perceptibly different throughout the user journey.

## 1.1 In scope

- Interaction models and user task flows.

- User-facing semantics for provenance, confidence, status, uncertainty, sensitivity, and review state.

- Data-entry behaviour, validation, confirmation, undo, conflict handling, and error recovery.

- Evidence handling, entity-resolution, graph, timeline, value-flow, typology, hypothesis, assessment, review, and dissemination experiences.

- Accessibility, keyboard operation, desktop layouts, responsive constraints, loading/empty/error states, and usability verification.

- User-facing behaviour for permission boundaries, protected sources, audit visibility, and AI-assisted features.

## 1.2 Explicitly out of scope

- Final sitemap or menu tree.

- Canonical navigation taxonomy and object hierarchy.

- Global naming/label taxonomy beyond interaction-specific terms.

- Content inventory and findability model.

- Final URL structure and route taxonomy.

- Cross-domain information architecture decisions.

Those topics SHALL be defined in the separate CS-AML Information Architecture Specification so that UX and IA can be owned by different engineering/design workstreams without ambiguity.

# 2. Target Users and Usage Context

| **Role** | **Primary UX needs** | **High-risk moments** |
|----|----|----|
| Investigator | Fast evidence capture, structured analysis, clear provenance, low-friction linking. | Uploading evidence, creating adverse relationships, changing scope, exporting. |
| Case Owner | Case status, gate readiness, risk visibility, approval context. | Gate approval, dissemination, closure/reopen. |
| Reviewer | Independent reconstruction of reasoning, contradictions, source quality and confidence. | Approving assessments/products, challenging identity resolution. |
| Evidence Custodian | Original preservation, hash/integrity, derivatives, provenance. | Replacement, mismatch, disposition. |
| Data Steward | Entity identity quality, merge/unmerge, vocabulary consistency. | High-impact merge, conflicting identifiers. |
| Source Handler | Protected source compartment and safe evidence handoff. | Identity reveal, export, search leakage. |
| Administrator/Auditor | Policy, retention, access and audit observability. | Role changes, retention execution, incident review. |

## 2.1 Operating conditions

- Desktop-first investigation work, frequently involving multiple documents and long analytical sessions.

- Potentially slow or unreliable networks; users must not lose work silently.

- Cases may involve personally sensitive or reputationally harmful information.

- Analysts may work across multiple languages and jurisdictions.

- Users may be technically sophisticated but should not need to understand database or graph internals.

- Reviewers may enter a case late and must quickly understand what is known, inferred, disputed, and unknown.

# 3. UX Goals and Quality Attributes

| **Goal** | **Meaning** | **UX success signal** |
|----|----|----|
| U1 Traceable | Users can move backward from judgement to evidence without losing context. | Reviewer reaches supporting evidence within a small number of intentional interactions. |
| U2 Uncertainty-aware | The interface makes fact/inference/hypothesis states perceptible. | Users can correctly identify status in usability testing. |
| U3 Reversible | High-impact actions can be reviewed, undone, superseded, or corrected. | No irreversible merge/edit occurs without explicit confirmation and recovery path. |
| U4 Safe-by-default | Sensitive actions require context and authorization, not accidental clicks. | Exports/reveals cannot occur unintentionally. |
| U5 Efficient | Repeated investigative work avoids needless re-entry and context switching. | Common workflows complete without duplicate data entry. |
| U6 Reviewable | A reviewer can understand analytical reasoning independently. | Reviewer can inspect support, contradiction, assumptions and gaps. |
| U7 Accessible | Core workflows are keyboard and assistive-technology usable. | Critical operations do not rely on color, pointer precision, or hover only. |
| U8 Calm | The system supports deliberate judgement rather than alert overload. | No gratuitous urgency or suspicion scoring in default interface. |

# 4. Core UX Principles

### UX-P01 Evidence before assertion

When a user creates a material fact, relationship, asset attribution, value flow, indicator or assessment, the interface SHOULD make the evidence link visible and easy to add.

### UX-P02 Status is visible

Candidate, confirmed, disputed, rejected, superseded, direct, reconstructed, hypothetical, draft, approved and restricted states SHALL never be hidden only in metadata.

### UX-P03 No silent promotion

A candidate or AI suggestion SHALL NOT visually or functionally become a canonical fact without explicit user action.

### UX-P04 No accusation by styling

Red color, warning icons, threat metaphors, or risk-like visual emphasis SHALL NOT imply criminality merely because an entity appears in an investigation.

### UX-P05 Progressive disclosure

Advanced provenance, audit and metadata are available without overwhelming the primary task.

### UX-P06 Reversibility

Merge, classification change, dissemination, correction, disposition and other high-impact actions SHALL expose consequences before commitment.

### UX-P07 Context preservation

Opening evidence, graph edges, timeline events or hypotheses SHOULD preserve case context and allow return without losing state.

### UX-P08 Explicit unknowns

Unknown, unavailable and not-yet-assessed are distinct from zero, none, false or cleared.

### UX-P09 Reviewer independence

Review surfaces SHOULD support challenge and contradiction, not merely sign-off.

### UX-P10 Permission dignity

Denied access SHALL be handled without leaking sensitive object existence or encouraging users to bypass controls.

# 5. Interaction Model and Analytical State Semantics

## 5.1 User-visible analytical states

| **Concept** | **Required visual semantics** | **Prohibited simplification** |
|----|----|----|
| Claim | Attributed statement from a source; not yet accepted as fact. Shows its claim status (Recorded, Under review, Corroborated, Contradicted, Unresolved — proposed, pending product-owner approval). | Displaying as verified fact; showing a claim as a fact without a recorded verification decision. *[v0.1.1 · A10]* |
| Fact | Verified/time-bounded proposition with evidence, its source claim(s) and the verification decision that created it; shows its fact status (Provisional, Established, Disputed, Superseded). | Hiding provenance; hiding the verification decision; presenting a Provisional fact as Established. *[v0.1.1 · A10]* |
| Candidate entity match | Possible identity equivalence requiring review. | Auto-merge appearance. |
| Relationship | Typed connection with evidence/status/time. | Graph edge with no provenance status. |
| Indicator | Observed pattern relevant to typology. | Label as suspicious/proven crime by default. |
| Hypothesis | Testable explanation with support and contradiction. | Present as conclusion. |
| Assessment | Analyst judgement with confidence (High, Moderate, Low, Insufficient basis) and gaps. | Present confidence as mathematical probability unless validated; show Insufficient basis as Low, as an adverse result, or as missing. *[v0.1.1 · A09]* |
| Value flow class | DIRECT / DOCUMENTED / RECONSTRUCTED / HYPOTHETICAL (`flow_class` wire values; display labels may be translated). | One undifferentiated arrow style; showing RECONSTRUCTED or HYPOTHETICAL as DIRECT or DOCUMENTED. *[v0.1.1 · A09]* |
| Intelligence product | Versioned product with review/approval state. | Overwrite prior approved version. |

## 5.2 Status presentation rule

Every high-impact object SHALL expose its status near the object title or primary identifier, using text labels plus secondary visual encoding. Color MAY reinforce status but SHALL NOT be the only carrier of meaning.

# 6. End-to-End UX Journey

1.  Open or create a governed case with a clear investigation question and scope.

2.  Register a source and preserve original evidence.

3.  Create extracts or claims while retaining provenance.

4.  Create or resolve entities and link identifiers without premature merge.

5.  Build evidence-backed relationships, ownership/control assertions and assets.

6.  Place events on a chronology and reconstruct value flows with explicit class.

7.  Compare observations to typologies and capture counter-indicators.

8.  Test competing hypotheses, document gaps and produce a confidence-rated assessment.

9.  Generate an intelligence product with an evidence index.

10. Complete independent review, resolve changes, approve dissemination and record sharing.

> **Journey rule**  
> The user SHOULD be able to move forward and backward through this chain without losing provenance or being forced to duplicate canonical information. The UX SHALL support iteration: investigation is not a one-way wizard.

# 7. Case and Workflow Experience

## 7.1 Case creation

| **Requirement ID** | **UX requirement** | **Acceptance** |
|----|----|----|
| UXR-CASE-001 | Case creation SHALL make owner, purpose, investigation question and classification understandable before activation. | User cannot accidentally activate an incomplete case; missing fields explain why. |
| UXR-CASE-002 | Investigation question entry SHALL encourage neutral wording and avoid guilt-presuming templates. | Prompt/example text uses question framing, not accusation framing. |
| UXR-CASE-003 | Material scope changes SHALL show what changes and require rationale. | User can compare current and proposed scope before saving. |
| UXR-CASE-004 | Lifecycle gate status SHALL be visible at the point of blocked actions. | Blocked action explains gate requirement and authorized next step. |
| UXR-CASE-005 | Task completion SHALL not hide historical ownership or prior state. | Closed task retains owner, timestamps and linked objects. |

## 7.2 Gate and approval interactions

- Gate approval SHOULD summarize the decision context: requested action, case classification, unresolved gaps, risk conditions, and reviewer independence requirement.

- Approval/rejection SHALL require an intentional action and SHALL not share a primary button style with navigation controls.

- When self-approval is prohibited, the UI SHALL explain that a different authorized reviewer is required rather than presenting a generic error.

# 8. Source, Evidence and Document Experience

## 8.1 Evidence ingestion

| **ID** | **UX requirement** | **Acceptance** |
|----|----|----|
| UXR-EVD-001 | Upload experience SHALL separate original evidence from analyst-created derivatives. | Original and derivative have visibly different labels and actions. |
| UXR-EVD-002 | After upload, integrity/hash status SHOULD be visible without requiring a technical console. | User can see success, pending or mismatch state. |
| UXR-EVD-003 | Failed upload or scan SHALL never look like a successfully preserved evidence item. | Incomplete items are clearly marked and retryable. |
| UXR-EVD-004 | Evidence extract creation SHALL retain parent and precise location. | User can return from extract to parent location. |
| UXR-EVD-005 | Reliability and information credibility SHALL be entered separately. | One control cannot overwrite or substitute for the other. |
| UXR-EVD-006 | Mutable web sources SHOULD expose whether an archived copy exists. | Missing archive is distinguishable from archived status. |

## 8.2 Document reading interaction

- The reading view SHOULD allow side-by-side or quickly switchable evidence context and analytical notes without requiring users to lose their place.

- Citations/extracts SHOULD be creatable from the reader with visible source/page context.

- Derived OCR text SHOULD be labelled as extracted text and not replace the visual/original evidence representation.

- Copying text from evidence SHOULD preserve or offer citation metadata where practical.

# 9. Entity Resolution UX

> **High-impact design principle**  
> Entity resolution is a decision, not a convenience feature. Candidate similarity SHALL be presented as evidence for review, not as proof of sameness.

| **ID** | **UX requirement** | **Acceptance** |
|----|----|----|
| UXR-ENT-001 | Candidate match view SHALL present matching and conflicting attributes side by side. | Reviewer can see both evidence for and against merge. |
| UXR-ENT-002 | Common-name similarity SHALL not receive visual treatment equivalent to a confirmed identifier match. | Similarity rationale is explicit. |
| UXR-ENT-003 | Merge confirmation SHALL summarize affected aliases, identifiers, relationships, cases and provenance. | User sees consequence preview. |
| UXR-ENT-004 | Unmerge/reversal path SHALL be discoverable to authorized users. | No hidden support-only reversal for MVP. |
| UXR-ENT-005 | Entity status such as candidate, probable, confirmed, disputed or unresolved SHALL be visible in graph and detail views. | Status is text-visible, not color-only. |

# 10. Relationship, Ownership and Asset UX

## 10.1 Relationship creation

- Relationship creation SHALL require explicit relationship type selection.

- The interface SHALL distinguish legal ownership, beneficial ownership, control, use and association.

- Unknown percentage SHALL be representable without defaulting to 0%.

- Relationship status, valid time and evidence SHALL be reviewable from any visual edge representation.

## 10.2 Asset attribution

- The interface SHALL distinguish “owned by”, “controlled by”, “used by”, and “associated with”.

- Estimated valuation SHALL visibly show date, currency, source and uncertainty.

- A material asset attribution without evidence SHOULD trigger a visible incomplete-state cue before assessment use.

# 11. Timeline UX

| **ID** | **UX requirement** | **Acceptance** |
|----|----|----|
| UXR-TIM-001 | Timeline SHALL preserve date precision. | Year-only/month-only events are not rendered as exact dates. |
| UXR-TIM-002 | Events SHALL link back to evidence and canonical event details. | User can inspect basis without losing timeline context. |
| UXR-TIM-003 | Filters SHALL not silently change analytical meaning. | Active filters are always visible and clearable. |
| UXR-TIM-004 | Temporal correlation SHALL not be worded as causation. | Default labels use neutral temporal language. |

# 12. Follow-the-Value UX

## 12.1 Flow classes

| **Class** | **Required user-facing meaning** | **Minimum visual cue** |
|----|----|----|
| DIRECT | Supported by direct transactional evidence. | Text class label + solid relationship semantics. |
| DOCUMENTED | Movement/value relationship supported by documentary evidence but not necessarily a direct account transaction. | Text label distinct from DIRECT. |
| RECONSTRUCTED | Analytical reconstruction from multiple evidence points. | Text label + non-solid/differentiated line semantics. |
| HYPOTHETICAL | Proposed flow used for testing a hypothesis. | Text label + clearly tentative visual treatment. |

Color SHALL NOT be the sole method for distinguishing classes. Legend/labels SHALL survive screenshot, print and export.

## 12.2 Flow builder

- Users SHOULD build flows leg by leg, with evidence and class attached per leg.

- Unknown amount, approximate amount, range and exact amount SHALL be distinct input states.

- The interface SHALL not coerce unknown amount to zero.

- Deleting a visual flow leg SHALL not delete underlying evidence.

- Before a reconstructed or hypothetical flow is used in an assessment, the interface SHOULD show its class and confidence in the assessment context.

# 13. Typology and Indicator UX

| **ID** | **UX requirement** | **Acceptance** |
|----|----|----|
| UXR-TYP-001 | Typology catalogue SHALL display mechanism, observables, counter-indicators, false positives and version. | User can inspect cautionary context before matching. |
| UXR-TYP-002 | Indicator capture SHALL require neutral proposition wording and linkable evidence. | Indicator is not labelled “crime detected”. |
| UXR-TYP-003 | Typology match SHALL expose observed indicators and counter-indicators together. | Counterevidence is not hidden in secondary tab only. |
| UXR-TYP-004 | Consistency level SHALL require analyst rationale. | System cannot silently elevate match level. |
| UXR-TYP-005 | One weak indicator SHALL not generate strong visual warning by default. | Visual emphasis reflects evidence quality, not mere presence. |

# 14. Hypothesis and Assessment UX

## 14.1 Competing hypotheses

> **Reasoning UX**  
> The hypothesis workspace SHOULD make it easy to record evidence that weakens the analyst’s preferred explanation. The interaction should reward completeness, not confirmation.

- Multiple hypotheses SHOULD be visible in parallel comparison where screen space allows.

- Supporting and contradicting evidence SHALL be visually separable without implying numerical scoring.

- Rejected hypotheses SHALL remain accessible in history.

- Assumptions and intelligence gaps SHOULD be shown near the hypothesis they affect.

## 14.2 Assessment drafting

| **ID** | **UX requirement** | **Acceptance** |
|----|----|----|
| UXR-ASM-001 | Assessment authoring SHALL separate judgement, confidence, basis, assumptions, alternatives and gaps. | A single narrative box is insufficient for material assessment. |
| UXR-ASM-002 | Confidence selection SHALL require rationale and SHOULD show descriptive guidance. Options are High, Moderate, Low and Insufficient basis (wire `HIGH`, `MODERATE`, `LOW`, `INSUFFICIENT_BASIS`); Insufficient basis is a distinct, neutral choice — not a level below Low. | User cannot save material assessment with confidence but no basis (for every level, including Insufficient basis); a finalized assessment cannot be left without a confidence level. *[v0.1.1 · A09]* |
| UXR-ASM-003 | Assessment SHALL expose backward trace to supporting evidence. | Reviewer can traverse to provenance. |
| UXR-ASM-004 | Unresolved gaps SHALL remain visible when product is drafted. | Drafting report does not hide gaps. |
| UXR-ASM-005 | System SHALL avoid probability-like visual precision unless model is validated. | No default 0-100 “guilt/risk score”. |

# 15. Search and Investigation Graph UX

## 15.1 Search interaction

- Search results SHALL never reveal unauthorized object titles, snippets, counts or facets.

- Filters and case scope SHALL remain visible while results are shown.

- Search result type, status and case context SHOULD be distinguishable.

- Search is a discovery tool; the interface SHALL not imply that result ranking equals analytical significance.

## 15.2 Graph interaction

| **ID** | **UX requirement** | **Acceptance** |
|----|----|----|
| UXR-GRF-001 | Every edge SHALL expose relationship type, status and provenance access. | No anonymous decorative edges for material relationships. |
| UXR-GRF-002 | Graph SHALL distinguish entity status and flow class without color-only encoding. | Text/shape/line semantics are available. |
| UXR-GRF-003 | Expanding a node SHALL not imply discovered entities are analytically relevant. | Expansion is neutral and reviewable. |
| UXR-GRF-004 | Filtering SHALL show active filter state and allow reset. | User cannot unknowingly interpret a partial graph as complete. |
| UXR-GRF-005 | Graph layout changes SHALL not change canonical data. | Repositioning nodes is presentation-only. |

# 16. Review Experience

## 16.1 Independent review workspace

- Reviewer SHOULD see the product version, author, case scope, assessment confidence, unresolved gaps, source/evidence index, and review status in one coherent review context.

- Reviewer SHALL be able to comment or request change without editing the author’s approved history directly.

- The interface SHOULD support challenge prompts covering identity, provenance, alternative explanations, confidence and potential harm.

- Where independence is required, the author SHALL not see an enabled self-approve control.

## 16.2 Review resolution

| **State** | **UX behaviour** |
|----|----|
| Draft | Editable by authorized author; clearly not approved. |
| In review | Version is review-targeted; major edits create or update draft according to product rules. |
| Changes requested | Reviewer comments and required changes are visible and actionable. |
| Approved | Approved version is frozen; edits require new version. |
| Superseded | Prior version remains readable with link to current version. |
| Retracted | Status and reason remain visible; record is not silently deleted. |

# 17. Dissemination and Export UX

> **Safety gate**  
> External dissemination is a consequential action. The UX SHALL make recipient, purpose, classification, version, included objects, minimisation/redaction state, and handling restrictions visible before final export.

| **ID** | **UX requirement** | **Acceptance** |
|----|----|----|
| UXR-DIS-001 | External export SHALL be blocked until required approval exists. | No hidden bypass through alternate export button. |
| UXR-DIS-002 | Export preview SHALL show what will be included and excluded. | User can inspect manifest before generation. |
| UXR-DIS-003 | Restricted/protected source identity SHALL never be included by default. | Explicit policy-controlled inclusion only if authorized. |
| UXR-DIS-004 | Sharing completion SHALL show recipient, version, time and restrictions. | Sharing log confirmation is visible after action. |
| UXR-DIS-005 | Correction/supersession state SHALL appear on later exports. | Recipient-facing document identifies current/superseded status. |

# 18. Permission and Protected-Source UX

## 18.1 Permission feedback

- Denied access SHOULD use non-disclosing language such as “You do not have access to this resource” rather than confirming sensitive object identity.

- If access can legitimately be requested, the interface MAY provide a controlled request path without revealing protected metadata.

- Permission state changes SHOULD be reflected promptly without requiring users to infer stale access.

- Classification SHALL be shown with the canonical display labels Public, Internal, Sensitive, Restricted and Source-protected (wire `PUBLIC`, `INTERNAL`, `SENSITIVE`, `RESTRICTED`, `SOURCE_PROTECTED`); additional access labels (e.g. embargo, legal-review) are shown as restrictions alongside the level. Objects with unknown or missing classification fail closed. *[v0.1.1 · A08]*

## 18.2 Protected source interactions

- Protected source identity SHALL be visually and functionally compartmentalized from routine source-derived evidence.

- Routine analyst views SHALL reference a protected source token/alias rather than identity.

- Reveal actions, where permitted, SHALL require explicit intent and SHOULD be logged as high-sensitivity audit events.

- Protected identity SHALL not appear in ordinary search, graph labels, exports, autocomplete, browser title text, or routine notifications.

# 19. Form and Data Entry Standards

| **Pattern** | **Requirement** |
|----|----|
| Required fields | Required vs optional SHALL be explicit before submit. |
| Unknown | Provide “Unknown / Not established” where analytically valid; do not force false precision. |
| Date precision | Support exact date, month, year, range and unknown. |
| Money/value | Support exact, approximate, minimum, maximum, range and unknown; preserve currency. |
| Confidence | Use controlled descriptive scale with rationale; avoid pseudo-precision. Insufficient basis SHALL NOT be converted to Low, blank or zero. *[v0.1.1 · A09]* |
| Autosave | Long-form analytical drafting SHOULD protect against accidental loss while preserving version/audit semantics. |
| Validation | Validation messages SHALL state what is wrong and how to resolve it. |
| Destructive action | Use consequence preview and explicit confirmation; typed confirmation reserved for exceptionally high-impact actions, not routine use. |
| Cancel/back | Leaving a dirty form SHALL warn unless safe autosave/versioning exists. |

# 20. System Feedback and State Handling

| **State** | **Required UX behaviour** |
|----|----|
| Loading | Show activity without implying completion; long jobs SHOULD expose progress/state where available. |
| Empty | Explain what the area represents and the next legitimate action; avoid making absence look like “cleared/no risk”. |
| Partial | Clearly label partial or filtered results. |
| Error | Preserve user input where safe and provide recovery action. |
| Offline/interrupted | Warn before losing work; retry idempotently where applicable. |
| Background job | Show queued/running/completed/failed; prevent duplicate submission. |
| Conflict | When another user/version changed the object, show comparison or safe reload path rather than silent overwrite. The "record changed" recovery is triggered by an API 412 PRECONDITION_FAILED (stale version); a 409 STATE_CONFLICT means a workflow/business-state conflict (e.g. gate not satisfied, object already finalized) and SHALL be explained as such, not as a concurrent edit. *[v0.1.1 · A04]* |
| Permission changed | Terminate or refresh affected actions; do not continue with stale authorization. |
| Integrity mismatch | Use high-severity but factual language; do not allow normal analyst dismissal without authorized process. |

# 21. Undo, Correction and Reversibility

- Routine edits SHOULD support undo or version recovery where feasible.

- Entity merge MUST support authorized unmerge.

- Approved products MUST use correction/supersession, not destructive overwrite.

- Relationship deletion SHOULD preserve audit history; where possible, status “withdrawn/rejected/superseded” is preferable to erasure.

- Export/share actions cannot be undone externally; the UX SHALL explicitly communicate this before dissemination.

# 22. Accessibility Requirements

| **ID** | **Requirement** |
|----|----|
| UXR-A11Y-001 | Core workflows SHALL be operable with keyboard only. |
| UXR-A11Y-002 | Focus indicators SHALL remain visible and logical. |
| UXR-A11Y-003 | Color SHALL NOT be the sole carrier of flow class, status, warning, evidence quality or confidence. |
| UXR-A11Y-004 | Interactive graph/timeline SHALL have accessible alternative representations such as lists/tables. |
| UXR-A11Y-005 | Form controls SHALL have programmatic labels and useful validation text. |
| UXR-A11Y-006 | Text and UI contrast SHOULD meet WCAG 2.2 AA targets. These are design targets; no WCAG conformance is claimed until a recorded evaluation of the implemented product exists. *[v0.1.1 · A01; N07]* |
| UXR-A11Y-007 | Critical confirmation dialogs SHALL not trap or unpredictably move focus. |
| UXR-A11Y-008 | Hover-only information SHALL also be available by focus/click or persistent text. |

# 23. Desktop, Responsive and Multi-Panel Behaviour

MVP is desktop-first. The interface SHOULD optimize for 1280px and wider investigation workspaces while remaining usable on smaller laptop displays. Mobile MAY support read-only or limited review flows later but is not a primary MVP target.

- Multi-panel layouts SHOULD collapse gracefully rather than compress critical text below readable width.

- Evidence/analysis side panels SHOULD remember reasonable user state within a session.

- Primary actions SHALL remain discoverable when a detail panel is open.

- Graph and timeline views SHOULD provide full-screen focus mode without severing provenance access.

# 24. Visual Semantics and Design System Behaviour

## 24.1 Semantic design tokens

| **Semantic intent** | **Use** | **Rule** |
|----|----|----|
| Neutral | Most entities, facts, navigation and informational surfaces. | Default visual state. |
| Informational | Derived/secondary context, system notices. | Must not imply suspicion. |
| Caution | Incomplete provenance, unresolved contradiction, high-impact action. | Use factual wording. |
| Critical | Integrity mismatch, security failure, blocked unsafe action. | Reserved for actionable system/safety conditions. |
| Positive | Completed verification, approved review, successful integrity check. | Do not use to imply “innocent/cleared”. |

## 24.2 Prohibited visual patterns

- Crime-style red highlighting for a person/company merely because it is a subject or graph hub.

- “Risk gauge” or “guilt score” without validated model and explicit approved use.

- Flashing/pulsing alerts for analytical indicators.

- Graph size encoding that users could mistake as proof of importance without clear explanation.

- Hidden uncertainty revealed only on hover.

# 25. Notifications and Attention Management

- Notifications SHOULD be limited to actionable events: assignment, review request, approval/rejection, integrity/security event, failed processing, or required gate action.

- The system SHOULD avoid generic “suspicious activity” alerts as an attention mechanism.

- Sensitive case details SHALL be minimized in email/push notifications.

- Users SHOULD be able to distinguish urgent security/integrity events from routine workflow updates.

# 26. Collaboration UX

- Concurrent work SHOULD show object version or recent-change awareness where collisions are plausible.

- Comments/review notes SHOULD be attributable and timestamped.

- Users SHOULD not assume another analyst has read a comment merely because it is present; acknowledgement state MAY be used where useful.

- Collaborative editing SHALL not erase individual authorship of material analytical changes.

# 27. AI-Assisted UX Guardrails

> **AI interaction principle**  
> AI output is a suggestion layer. It SHALL look and behave like generated/derived material until a human explicitly verifies or promotes the relevant proposition.

| **ID** | **UX requirement** | **Acceptance** |
|----|----|----|
| UXR-AI-001 | AI-generated text/candidate SHALL be labelled generated and include model/tool context where material. | User can distinguish generated output from evidence. |
| UXR-AI-002 | AI suggestions SHALL require review before becoming canonical entity/relationship/fact. | No one-click silent promotion. |
| UXR-AI-003 | AI answers SHOULD cite authorized canonical objects/evidence. | Unsupported answer is visibly limited. |
| UXR-AI-004 | AI SHALL not present guilt determination, dissemination approval or identity merge as an autonomous decision. | Consequential action remains human-controlled. |
| UXR-AI-005 | Protected-source identity SHALL be excluded from AI context unless explicitly authorized by policy. | Default context builder omits compartmented identity. |

# 28. Onboarding and Learnability

- First-use guidance SHOULD explain the analytical chain and the difference between evidence, fact, indicator, hypothesis and assessment.

- Inline help SHOULD be contextual and concise; methodology depth may link to framework guidance rather than crowd the interface.

- Dangerous or uncommon actions such as merge, unmerge, dissemination and source reveal SHOULD include just-in-time guidance.

- Terminology SHALL remain consistent across forms, review states and exports.

# 29. Usability Testing and UX Verification

## 29.1 Required test scenarios

| **Scenario** | **Participant goal** | **Pass condition** |
|----|----|----|
| UT-01 Case start | Create governed case and understand why activation is blocked/incomplete. | User completes without moderator explanation. |
| UT-02 Evidence trace | Create evidence extract and later return from assessment to exact evidence. | Provenance path succeeds. |
| UT-03 Entity resolution | Review candidate pair with conflicting attributes and decline/merge appropriately. | User understands candidate != confirmed. |
| UT-04 Value flow | Build mixed direct/reconstructed flow and interpret exported result. | Class distinction understood without color reliance. |
| UT-05 Hypothesis | Record support and contradiction for two hypotheses. | User can explain difference between hypothesis and assessment. |
| UT-06 Peer review | Reviewer finds gaps, evidence and alternatives and requests changes. | Independent review completes without author guidance. |
| UT-07 Dissemination | User attempts export before approval, then completes approved minimized export. | Unsafe path blocked; approved path understandable. |
| UT-08 Protected source | Routine analyst uses derived evidence but cannot discover source identity. | No leakage via search/export/labels. |

## 29.2 UX success measures

- Task success rate for required scenarios.

- Critical error rate (e.g., mistaken merge, wrong flow class, accidental export attempt).

- Time-to-evidence trace for reviewer.

- Percentage of users who correctly identify fact vs hypothesis vs assessment states.

- Accessibility defects in critical workflow.

- User-reported confidence in understanding uncertainty and provenance.

- Number of support interventions needed for first end-to-end pilot.

# 30. UX Analytics and Privacy

Product analytics SHALL be privacy-preserving and SHALL NOT capture evidence content, protected identities, case narrative, document text, search terms, or graph payloads unless explicitly approved for a specific controlled research purpose.

- Prefer event-level telemetry such as screen/action type, duration, validation failure category and feature usage.

- Telemetry payloads SHOULD use opaque object identifiers where needed and SHOULD avoid sensitive labels.

- Session replay tools SHALL be disabled by default for sensitive investigation environments.

- UX research exports SHALL be minimized and reviewed before leaving the protected environment.

# 31. UX Requirement Traceability

| **UX family** | **Primary upstream source** | **Engineering workstream** |
|---------------|-----------------------------|----------------------------|
| UXR-CASE      | PRD/SRS FR-CASE; E2         | Case/workflow frontend     |
| UXR-EVD       | FR-EVD/DOC; E3              | Evidence/document frontend |
| UXR-ENT       | FR-ENT; E4                  | Entity resolution UI       |
| UXR-TIM       | FR-TIM; E5                  | Timeline UI                |
| UXR-TYP       | FR-TYP; E6                  | Analytical reasoning UI    |
| UXR-ASM       | FR-ASM; E6                  | Assessment UI              |
| UXR-GRF       | FR-GRF; E7                  | Graph/search UI            |
| UXR-DIS       | FR-PRD/REV/DIS; E8          | Product/review/export UI   |
| UXR-A11Y      | SRS UX/NFR                  | Cross-cutting frontend     |
| UXR-AI        | SRS AI                      | Future assistive/AI layer  |

# 32. UX Definition of Done

1\. Interaction satisfies applicable UXR requirements and SRS acceptance criteria.

2\. Loading, empty, partial, error, conflict and permission-denied states are designed, not left implicit.

3\. Keyboard navigation and focus behaviour are verified for critical workflows.

4\. Color is not the sole carrier for analytical state, value-flow class or warnings.

5\. Provenance and uncertainty remain visible at consequential decision points.

6\. High-impact action has consequence preview, authorization handling and audit-aware confirmation.

7\. Usability test or design review covers the relevant critical scenario.

8\. No interaction introduces terminology or hierarchy that conflicts with the future IA specification without an explicit cross-document decision.

# 33. UX–IA Handoff Contract

> **Separation of ownership**  
> UX owns interaction behaviour. IA owns organisation and findability. Both specifications SHALL share the same canonical domain vocabulary and resolve conflicts through explicit architecture/product decisions rather than local UI workarounds.

| **UX team owns** | **IA team owns** | **Joint decision** |
|----|----|----|
| Task flows and interaction states | Sitemap/navigation model | Where a task enters/exits global structure |
| Forms, validation, feedback, undo | Object grouping and hierarchy | Object labels visible to users |
| Graph/timeline interaction behaviour | Content/object taxonomy | Cross-object discoverability |
| Review/dissemination interaction | Global navigation and findability | Role-specific entry points |
| Accessibility and interaction semantics | Label system and information scent | Terminology consistency |
| Loading/error/permission states | Route/content organisation | Deep-link and context preservation behaviour |

# Annex A — UX Review Checklist

☐ Can the user tell what is fact, claim, inference, hypothesis and assessment?

☐ Can every material analytical object expose its provenance?

☐ Does the UI distinguish DIRECT / DOCUMENTED / RECONSTRUCTED / HYPOTHETICAL without color alone?

☐ Does a denied user learn more than they should?

☐ Can a reviewer identify contradictions and gaps?

☐ Can a high-impact action be reversed or superseded where appropriate?

☐ Does export show exactly what leaves the system?

☐ Are unknown and zero/none clearly different?

☐ Are error and partial states explicit?

☐ Can the workflow be completed with keyboard?

☐ Does any styling imply guilt or suspicion without analytical basis?

☐ Could AI output be mistaken for evidence or verified fact?

# Annex B — Recommended UX Deliverables

| **Deliverable** | **Purpose** |
|----|----|
| Critical task-flow diagrams | Model interaction sequences without deciding final IA. |
| Low-fidelity wireframes | Validate interaction and state behaviour. |
| State matrices | Document empty/loading/error/permission/conflict states. |
| Interaction prototypes | Test evidence, merge, value-flow, hypothesis, review and export flows. |
| Design-system semantic tokens | Standardize status, caution, provenance and uncertainty behaviour. |
| Accessibility annotations | Specify keyboard/focus/alternative representations. |
| Usability test scripts | Validate required UT-01..UT-08 scenarios. |
| UX decision log | Record consequential deviations/decisions and handoffs to IA. |
