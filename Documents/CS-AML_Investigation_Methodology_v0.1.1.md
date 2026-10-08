**CS-AML  
INVESTIGATION METHODOLOGY**

Derived Methodology · Version 0.1.1

Civil Society Anti-Money Laundering & Financial Intelligence Framework

Draft for Review · October 2026

Civil Society Anti-Money Laundering & Financial Intelligence Framework — Derived Methodology

Status: Draft for Review (Proposed Internal Baseline) \| Version: 0.1.1 \| Date: October 2026 *[v0.1.1 · A01]*

> **Document status — v0.1.1**
> Version: 0.1.1 — Draft for Review (Proposed Internal Baseline). *[v0.1.1 · A01]*
> Supersedes: CS-AML Investigation Methodology v0.1. The DOCX/PDF files in this repository are the unchanged v0.1 baseline (legacy); this Markdown file is the canonical source.
> Validation: not validated. No recorded approval decision, implementation test result, or independent audit exists for this baseline. Acceptance criteria in this document are targets, not evidence that tests have passed.
> CS-AML is not an external standard or certification. References to FATF, Wolfsberg, PPATK, UNODC or other bodies do not imply their endorsement.
> Changes in 0.1.1: see `CHANGELOG.md` at the repository root (audit findings A01–A16).

# 0. Document Control

| **Field** | **Value** |
|----|----|
| Document title | CS-AML Investigation Methodology v0.1.1 *[v0.1.1 · A01]* |
| Parent standard | CS-AML Framework v0.1.1 Expanded (`CS-AML_Framework_v0.1.1_Expanded.md`) *[v0.1.1 · A01]* |
| Companion standard | CS-AML Typology Catalogue v0.1.1 (`CS-AML_Typology_Catalogue_v0.1.1.md`) *[v0.1.1 · A01]* |
| Status | Draft for Review (Proposed Internal Baseline) / Derived Methodology *[v0.1.1 · A01]* |
| Primary audience | Civil society organisations, investigative journalists, public-interest researchers, anti-corruption organisations, environmental and human-rights organisations, digital-rights organisations, research institutions, and trusted technical partners. |
| Primary use | Lawful, evidence-based financial investigation and intelligence analysis performed without coercive state powers or privileged access to regulated financial systems. |
| Normative language | MUST/SHALL = mandatory; SHOULD = recommended unless documented justification exists; MAY = optional capability. |

This methodology specifies HOW a CS-AML investigation SHALL be conducted. It operationalises the parent framework’s analytical chain and translates the Typology Catalogue into a controlled case workflow.

**Normative analytical chain:** SOURCE → EVIDENCE → CLAIM → FACT → INDICATOR → HYPOTHESIS → ASSESSMENT → INTELLIGENCE PRODUCT

A material allegation, referral, or publication decision SHALL NOT bypass the stages needed to demonstrate provenance, corroboration, competing explanations, confidence, and uncertainty.

# 1. Purpose, Status, and Methodological Objectives

The purpose of this methodology is to create a repeatable, reviewable, auditable, and rights-respecting method for civil society financial investigations. It is designed for investigations where analysts may have rich public-source, corporate, procurement, legal, property, digital, or documentary information but do not possess compulsory powers, bank secrecy overrides, subpoena authority, or routine access to account-level financial records.

## 1.1 Primary methodological goal

The primary goal is to convert lawfully obtained information into decision-useful financial intelligence without converting suspicion into accusation prematurely.

## 1.2 Operational objectives

- Frame investigations around answerable questions rather than predetermined guilt narratives.

- Prioritise collection according to analytical value, legality, proportionality, and risk.

- Preserve source provenance and evidence integrity sufficiently for peer review and referral.

- Resolve identities and relationships before relying on network patterns.

- Reconstruct economic value flows when direct transaction data are unavailable.

- Use AML typologies as analytical lenses rather than proof templates.

- Test competing hypotheses and actively search for disconfirming evidence.

- State confidence, uncertainty, and intelligence gaps explicitly.

- Separate internal analytical judgements from externally publishable allegations.

- Create outputs that can be understood and re-evaluated by another qualified analyst.

## 1.3 Methodological boundaries

This methodology does not authorise hacking, covert interception, credential theft, deception to obtain protected financial data, unlawful processing of personal data, automated guilt scoring, or the representation of civil society analysis as an official FIU or law-enforcement determination.

# 2. Foundations and External Alignment

CS-AML adopts a risk-based and evidence-based approach. FATF standards treat understanding of money-laundering risk as central to prioritising resources. FATF financial-investigation guidance recognises financial investigation and asset tracing as core operational elements for competent authorities (pending verification — specific publication/section not yet identified), while UNODC recognises that civil society can support asset tracing through open-source investigation, financial investigation, forensic auditing, and legal analysis (pending verification — page-level support not confirmed). *[v0.1.1 · A13]* PPATK has publicly recognised that information from NGO/CSO and the public can support early detection and financial-intelligence analysis. CS-AML adapts these ideas to a non-coercive civil-society setting.

| **Reference lineage** | **Methodological implication** |
|----|----|
| FATF Recommendations (amended June 2026) | Risk-based proportionality; focus resources on higher-risk areas; distinguish technical controls from effectiveness. |
| FATF Money Laundering National Risk Assessment Guidance (updated 2025) | Use structured, evidence-based, dynamic risk understanding; document assumptions and changing context. |
| FATF Financial Investigations Guidance (pending verification — specific publication/section not yet identified) | Treat financial investigation and asset tracing as structured operational disciplines; maintain links between evidence, proceeds, assets, and offences. *[v0.1.1 · A13]* |
| UNODC asset tracing / civil-society guidance (pending verification — page-level support not confirmed) | Use public records and lawful sources; generate information on assets, origin, ownership, and control; distinguish access authority from analytical usefulness. *[v0.1.1 · A13]* |
| PPATK NGO/CSO public complaint initiative (2025) | Improve quality, structure, and supporting information in civil-society referrals. |

# 3. Investigation Lifecycle

**Standard lifecycle:** INTAKE → TRIAGE → CHARTER → RISK REVIEW → COLLECTION PLAN → COLLECTION → STRUCTURE → ANALYSIS → HYPOTHESIS TESTING → ASSESSMENT → REVIEW → DISSEMINATION → CLOSURE / MONITORING

The lifecycle is iterative. Analysts MAY return to earlier stages when new information changes scope or hypotheses. However, material decisions SHALL pass the applicable control gate before proceeding.

| **Gate** | **Decision** | **Minimum evidence of readiness** |
|----|----|----|
| G0 Intake legitimacy | Is the matter suitable for CS-AML work? | Trigger, public-interest rationale, preliminary legal/safety concerns, no prohibited purpose. |
| G1 Charter approval | Is the investigation question bounded and proportionate? | Approved charter, scope, subjects, period, jurisdictions, initial hypotheses, expected outputs. |
| G2 Collection approval | May planned data be collected and retained? | Collection plan, data classes, lawful basis/access route, necessity, safeguards, source-risk assessment. |
| G3 Analytical readiness | Is the case sufficiently structured for material analysis? | Core entities resolved, provenance linked, source conflicts logged, major gaps identified. |
| G4 Assessment quality | Is the judgement analytically supportable? | Supporting and contradicting evidence, alternatives, typology analysis, confidence, gaps, assumptions. |
| G5 Dissemination approval | Can the product be shared, referred, or published? | Peer review, legal/privacy review where needed, handling classification, redactions, approval. |
| G6 Closure/monitoring | Can active investigation stop or change status? | Outcome, unresolved gaps, retention decision, monitoring rationale, lessons learned. |

# 4. Stage 1 — Intake and Triage

## 4.1 Intake sources

A case may originate from a whistleblower report, media investigation, public database anomaly, procurement analysis, court record, partner referral, internal research lead, leaked material lawfully received, or prior-case correlation. Intake source type does not determine truthfulness.

## 4.2 Intake record requirements

- Unique intake identifier and date/time.

- Origin and channel.

- Raw allegation or question preserved separately from analyst interpretation.

- Named subjects or entities, if any.

- Immediate safety, privacy, source-protection, or legal concerns.

- Initial public-interest rationale.

- Initial data sensitivity classification.

- Disposition: reject, hold, preliminary research, or open case.

## 4.3 Triage questions

| **Question** | **Why it matters** |
|----|----|
| What exactly is being alleged or questioned? | Prevents scope drift and conflation of separate allegations. |
| What would make the issue a financial-intelligence matter? | Ensures there is an ownership, asset, contract, value-flow, proceeds, or control dimension. |
| What is already known from credible sources? | Avoids duplicating basic validation work. |
| What is the potential harm if wrong? | Drives proportionality, review, and publication thresholds. |
| Is there a plausible lawful path to useful evidence? | Prevents investigations that would depend on prohibited access. |
| Is there an urgent preservation need? | Identifies disappearing web pages, documents, source risk, or volatile digital material. |

## 4.4 Intake rejection criteria

A matter SHOULD be rejected or deferred when it is primarily based on protected characteristics, partisan retaliation, personal vendetta, speculative association, absence of public-interest rationale, impossible lawful collection, or demands for unlawful surveillance. Rejection SHALL be documented without destroying the original intake record if retention is justified.

# 5. Stage 2 — Investigation Charter and Question Design

Every Investigation or Network Investigation SHALL have an Investigation Charter. The charter is the control against open-ended surveillance and confirmation bias.

## 5.1 Investigation question

The investigation question SHALL be answerable through evidence and SHALL NOT presuppose criminal guilt. Preferred formulations ask who controls, who benefits, what changed, where value moved, whether declared and observed structures are consistent, and what explanations fit the evidence.

**Poor question:** “How is Person X laundering money?”

**Preferred question:** “What ownership, control, asset, contract, and value-flow relationships link Person X and the identified entities during the defined period, and which legitimate or illicit explanations are consistent with the evidence?”

## 5.2 Charter fields

- Case ID and title.

- Public-interest purpose.

- Primary and secondary investigation questions.

- Subjects and excluded subjects.

- Time period.

- Jurisdictions.

- Predicate issue(s), if any, described as alleged or established.

- Initial hypotheses, including at least one non-criminal alternative when plausible.

- Expected data classes and high-risk data classes.

- Expected outputs and intended audiences.

- Risk classification and required reviewers.

- Stop conditions and review date.

## 5.3 Scope change control

Material expansion to new persons, jurisdictions, sensitive data classes, or alleged predicate offences SHALL be documented as a scope amendment and reassessed for necessity, legal risk, and proportionality.

# 6. Stage 3 — Investigation Risk and Harm Assessment

Risk assessment in CS-AML concerns both the subject matter and the conduct of the investigation. It SHALL NOT be reduced to “risk of money laundering”.

| **Risk domain** | **Examples** | **Required response** |
|----|----|----|
| Legal/regulatory | Privacy, defamation, secrecy restrictions, court orders, cross-border data law | Legal review, narrower scope, controlled access, jurisdictional analysis. |
| Source safety | Whistleblower exposure, retaliation, coercion | Need-to-know identity access, secure channels, source-risk plan. |
| Subject harm | Reputational harm, vulnerable persons, mistaken identity | Higher verification threshold, minimisation, redaction, right-of-reply review. |
| Analyst safety | Harassment, travel risk, digital targeting | Operational security controls, role separation, incident plan. |
| Data security | Sensitive financial/personal data, credentials, leaked datasets | Restricted repository, encryption, logging, retention limits. |
| Analytical risk | Confirmation bias, graph overreach, weak source base | Competing hypotheses, peer challenge, confidence discipline. |
| Publication/referral risk | Irreversible disclosure, source compromise | Approval gate, legal/privacy review, dissemination controls. |

## 6.1 Investigation risk rating

Organisations SHOULD classify investigation risk as Low, Moderate, High, or Critical. The rating SHALL determine review intensity, access controls, approval level, and whether specialist legal/security advice is required. Risk rating SHALL be revisited after major new evidence or scope expansion.

# 7. Stage 4 — Collection Planning

Collection SHALL be driven by analytical requirements, not by curiosity or tool availability. The Collection Plan links each information requirement to a lawful source strategy.

| **Collection-plan field** | **Required content** |
|----|----|
| Information Requirement (IR) | Specific question whose answer changes an analytical judgement. |
| Priority | Critical / High / Normal / Low. |
| Target entity/event/value flow | What the IR concerns. |
| Expected source classes | Registries, court files, procurement, corporate filings, web, interviews, documents, etc. |
| Collection method | Manual search, API, archive, interview, partner request, document review. |
| Lawful access note | Why the method is permitted and proportionate. |
| Sensitivity | Expected personal/confidential/high-risk data. |
| Success condition | What constitutes sufficient answer. |
| Stop condition | When additional collection would add little value or increase harm disproportionately. |

## 7.1 Collection priority model

Priority SHOULD consider analytical value × urgency × source volatility × risk reduction. High-volume collection is not inherently better. An organisation SHOULD prefer the smallest set of sources that can answer the question with adequate corroboration.

# 8. Stage 5 — Lawful Collection Methodology

## 8.1 Source classes

| **Class** | **Examples** | **Default posture** |
|----|----|----|
| Authoritative public records | Court decisions, government registries, procurement, official disclosures | High utility; verify currency, scope, self-reporting limitations. |
| Corporate/public disclosures | Annual reports, websites, ownership statements, filings | Useful; distinguish self-assertion from independently verified fact. |
| Professional journalism / research | Investigative reporting, NGO reports, academic work | Use as lead and secondary corroboration; inspect underlying evidence where possible. |
| Open web / social media | Public profiles, posts, archived pages | Volatile; preserve context and avoid identity inference from weak signals. |
| Human sources | Whistleblowers, witnesses, experts | Record access restrictions, reliability, corroboration, and source-protection controls. |
| Lawfully received non-public documents | Contracts, invoices, statements, correspondence | Verify authenticity and access basis; restrict handling. |
| Leaked/breached datasets | Public leak or provided dataset | High legal/security risk; require review before ingestion or redistribution. |
| Prohibited acquisition | Hacking, stolen credentials, covert interception, impersonation | MUST NOT be used as collection methods. |

## 8.2 Collection record

- Source ID.

- Collector.

- Date/time and method.

- Original URL/location or providing source.

- Access conditions and licence/terms where relevant.

- Original file or snapshot hash where material.

- Sensitivity and handling marking.

- Preservation action.

- Legal/access note.

- Related Information Requirements.

## 8.3 Web preservation

Material web evidence SHOULD be preserved with URL, access time, full-page or document capture where appropriate, contextual metadata, and hash. Screenshots alone are weak preservation when underlying HTML/PDF/downloadable records are available.

# 9. Source Evaluation and Provenance

The methodology separates source reliability from information credibility. A reliable institution can publish incomplete or self-reported data; an unknown source can provide a document later independently verified.

| **Source reliability** | **Meaning**                      |
|------------------------|----------------------------------|
| A                      | Highly reliable                  |
| B                      | Generally reliable               |
| C                      | Mixed or variable                |
| D                      | Generally unreliable             |
| E                      | Unreliable                       |
| F                      | Unknown / cannot yet be assessed |

| **Information credibility** | **Meaning**                                  |
|-----------------------------|----------------------------------------------|
| 1                           | Independently confirmed / directly supported |
| 2                           | Probably true; strong corroboration          |
| 3                           | Possibly true; plausible but incomplete      |
| 4                           | Doubtful; material conflicts or weak support |
| 5                           | Improbable                                   |
| 6                           | Cannot yet be assessed                       |

Ratings SHALL be justified in notes for material evidence. A rating such as A1 or F3 is an analytical aid, not a mathematical truth.

## 9.1 Provenance requirement

Every material fact, relationship, event, asset attribution, and value flow SHALL link to at least one evidence item. Derived calculations SHALL record input evidence and transformation logic.

# 10. Evidence Preservation and Integrity

Civil-society intelligence is not automatically courtroom evidence. Nevertheless, preserving integrity increases credibility, referral value, and reproducibility.

## 10.1 Evidence object minimum fields

- Evidence ID.

- Source ID.

- Description.

- File/object location.

- Acquisition date/time.

- Original/derivative status.

- Cryptographic hash for material digital files where feasible.

- Extractor/analyst.

- Sensitivity.

- Authentication/verification status.

- Related claims, entities, relationships, events, and hypotheses.

## 10.2 Original and derivative separation

Original files SHALL be preserved read-only when feasible. Analyst extracts, translations, OCR, annotations, charts, and redacted copies SHALL be stored as derivatives linked to the original.

## 10.3 Chain-of-custody-lite

Where an evidence item may be referred to authorities or contested, the organisation SHOULD record acquisition, transfers, transformations, access, and integrity checks. This is a civil-society preservation control and does not claim formal evidentiary admissibility.

# 11. Claim, Fact, and Proposition Management

Analytical discipline requires separating what a source says from what the investigation accepts as established.

| **State** | **Definition** | **Example** |
|----|----|----|
| Claim | A proposition asserted by a source or person. | “Person A controls Company X.” |
| Corroborated claim | A claim supported by multiple or stronger sources but not yet adopted as fact. | Registry + contract signature + official profile point to same role. |
| Fact | A proposition sufficiently established for the current analytical purpose. | Person A is listed as director of Company X on date Y. |
| Indicator | A fact/pattern relevant to a typology or risk. | Three related companies share the same address and director. |
| Hypothesis | A testable explanatory proposition. | Company Y may act as nominee holder for Person A. |
| Assessment | A reasoned judgement combining evidence, alternatives, confidence, and gaps. | Available evidence moderately supports common control. |

Facts SHALL be time-bounded where status may change. “Person A is director” without a date can be materially misleading.

The stored states for these objects follow the Data Model Specification v0.1.1, Sections 7.4–7.6 (proposed lifecycle, pending product-owner approval): a Claim carries `claim_status` (RECORDED, UNDER_REVIEW, CORROBORATED, CONTRADICTED, UNRESOLVED) — “Corroborated claim” above corresponds to CORROBORATED — and a Fact carries `fact_status` (PROVISIONAL, ESTABLISHED, DISPUTED, SUPERSEDED). A Claim becomes a Fact only through a recorded VerificationDecision. *[v0.1.1 · A09, A10]*

# 12. Entity Resolution Methodology

Entity resolution SHALL precede high-impact graph conclusions. Name similarity alone is insufficient for merging records.

## 12.1 Resolution dimensions

- Stable identifiers: registration numbers, national/company identifiers where lawfully available.

- Names and aliases.

- Date/place of birth or incorporation where lawfully available.

- Addresses.

- Phone/email/domain identifiers.

- Directors/shareholders/beneficial owners.

- Shared documents and signatures.

- Temporal consistency.

- Known relationships and operational context.

## 12.2 Resolution outcomes

| **Outcome** | **Meaning** |
|----|----|
| MERGED | Records represent the same entity with sufficient confidence. |
| LINKED_POSSIBLE | Likely or possible same entity; keep separate records with candidate link. *[v0.1.1 · A09]* |
| SEPARATE | Evidence indicates distinct entities. |
| UNRESOLVED | Insufficient evidence. |

## 12.3 Merge decision record

- Candidate records.

- Matching and conflicting attributes.

- Evidence.

- Analyst decision.

- Confidence.

- Reviewer for high-impact merges.

- Reversal history if later split.

A mistaken entity merge can contaminate every downstream relationship. High-impact merges SHOULD be peer reviewed.

# 13. Relationship and Control Mapping

Relationships SHALL be represented as typed, dated, evidence-linked propositions. Graph proximity is not equivalent to control or wrongdoing.

| **Relationship class** | **Examples** |
|----|----|
| Legal ownership | OWNS, SHAREHOLDER_OF, BENEFICIAL_OWNER_OF |
| Governance/control | DIRECTOR_OF, CONTROLS, AUTHORIZED_SIGNATORY_OF |
| Economic | PAID_BY, CONTRACTED_BY, SUPPLIER_TO, LENDER_TO, BORROWER_FROM |
| Asset | OWNS_ASSET, USES_ASSET, ACQUIRED_FROM, SOLD_TO |
| Personal/association | RELATIVE_OF, ASSOCIATE_OF — only when relevant and lawfully supported |
| Infrastructure | SHARES_ADDRESS_WITH, SHARES_PHONE_WITH, SHARES_DOMAIN_WITH |
| Transactional/value | TRANSFERRED_VALUE_TO, RECEIVED_VALUE_FROM — only with evidence or clearly marked reconstruction |

## 13.1 Ownership versus control

Analysts SHALL distinguish legal ownership, beneficial ownership, operational control, economic benefit, and mere use. The framework MUST NOT convert association or use into ownership without evidence.

# 14. Event and Timeline Analysis

Timeline analysis is mandatory when sequence materially affects interpretation. Temporal coincidence can generate a lead but does not establish causation.

## 14.1 Event object

- Event ID and type.

- Date or date range with precision flag.

- Entities involved.

- Location/jurisdiction if relevant.

- Evidence links.

- Status: confirmed / probable / possible / disputed.

- Analytical relevance.

## 14.2 Timeline techniques

- Compare appointments, incorporation, procurement awards, payments, loans, property acquisitions, disposals, litigation, and ownership changes.

- Mark known versus estimated dates.

- Identify events that precede or follow value creation.

- Test whether alleged causal narratives remain plausible under the actual sequence.

- Record missing periods and unknown dates as intelligence gaps.

# 15. Asset Tracing and Asset Attribution

Asset tracing under CS-AML seeks to identify assets, ownership, control, acquisition/disposal, value, and relationships to potential proceeds or value flows using lawful sources.

## 15.1 Asset classes

- Real property.

- Vehicles, vessels, aircraft.

- Corporate shares and beneficial interests.

- Securities/investments where lawfully observable.

- Crypto-assets/wallets where lawfully attributable.

- Precious metals, art, luxury goods, portable stores of value.

- Intellectual property or contractual rights when economically material.

## 15.2 Attribution states

| **State** | **Meaning** |
|----|----|
| LEGAL_OWNER | Ownership supported by authoritative or strong documentary evidence. |
| BENEFICIAL_INTEREST | Evidence indicates economic benefit/control distinct from legal title. |
| CONTROL/USE | Subject appears to control or use asset; ownership unproven. |
| ASSOCIATED | Asset linked through a related entity; no ownership inference. |
| UNRESOLVED | Attribution not established. |

Observed associated assets SHALL NOT be described as “hidden wealth” unless the evidentiary and legal basis supports that characterisation.

# 16. Value-Flow Reconstruction

Follow-the-value is the central analytical adaptation for civil society. A value flow SHALL be classified as DIRECT, DOCUMENTED, RECONSTRUCTED, or HYPOTHETICAL (wire values of `flow_class`, defined in the Data Model Specification v0.1.1, Annex A). The method SHALL preserve that distinction. *[v0.1.1 · A09]*

| **Flow class** | **Evidence threshold** | **Example** |
|----|----|----|
| DIRECT | Direct transaction/account/blockchain record lawfully available. | Account A → Account B, amount/date supported by record. |
| DOCUMENTED (display: Documented economic) *[v0.1.1 · A09]* | Contract, invoice, loan, dividend, asset sale, grant, procurement payment documented. | Agency awards Rp X contract to Company A. |
| RECONSTRUCTED | Sequence inferred from multiple economic events without direct transfer record. | Contract revenue precedes related entity property acquisition; causal link not directly proven. |
| HYPOTHETICAL | Analytical scenario requiring evidence. | Possible movement through intermediary Company C. |

## 16.1 Value-flow record

- Origin entity.

- Destination entity or asset.

- Value and currency if known.

- Date/range.

- Mechanism.

- Flow class.

- Evidence links.

- Confidence.

- Assumptions.

- Alternative explanations.

## 16.2 Reconstruction rule

A reconstructed flow SHALL NOT be visualised or described in a way that is indistinguishable from a directly evidenced transaction. Diagrams SHOULD use different line styles and display labels (e.g. “Documented”, “Reconstructed”, “Hypothetical”) mapped from the stored `flow_class` value; display labels SHALL NOT replace the stored value. *[v0.1.1 · A09]*

# 17. Typology Analysis

The CS-AML Typology Catalogue is an analytical reference, not a guilt classifier. A typology match assesses consistency between observed mechanisms and known laundering patterns.

## 17.1 Typology workflow

``` text
Observed facts → Indicators → Candidate typology → Mechanism test → Alternative explanations → Evidence gaps → Consistency assessment
```

## 17.2 Indicator classes

| **Class** | **Meaning** |
|----|----|
| M | Mechanism-specific indicator: closely tied to the typology mechanism. |
| C | Corroborating indicator: increases plausibility but is not distinctive alone. |
| K | Contextual indicator: provides environment/background. |
| D | Disconfirming indicator: weakens or contradicts the typology explanation. |
| G | Gap: missing information necessary to test the mechanism. |

## 17.3 Typology consistency levels

| **Level** | **Meaning** |
|----|----|
| No analytical basis | Evidence does not meaningfully support the mechanism. |
| Weak consistency | Some indicators exist but plausible benign explanations dominate or corroboration is weak. |
| Plausible consistency | Multiple relevant indicators; mechanism is credible but important gaps remain. |
| Strong consistency | Mechanism is supported by multiple independent evidence lines and alternatives are materially weaker. |
| Compelling consistency | Available evidence closely and coherently matches the mechanism; nevertheless this is not a legal finding of money laundering. |

Except where direct authoritative evidence establishes the mechanism, a typology SHALL NOT be assessed above Plausible consistency solely on one indicator or one source.

# 18. Hypothesis Generation and Testing

Hypotheses are explicit, testable explanations. They prevent analysts from treating the first plausible narrative as the conclusion.

## 18.1 Minimum hypothesis set

For material cases, analysts SHOULD maintain: (1) the principal suspected explanation, (2) at least one legitimate/benign explanation where plausible, and (3) an “insufficient information / alternative actor or mechanism” hypothesis where relevant.

## 18.2 Hypothesis matrix

| **Evidence / observation** | **H1 suspected mechanism** | **H2 legitimate explanation** | **H3 alternative mechanism** | **Notes** |
|----|----|----|----|----|
| Common director across companies | Supports | Neutral | Supports | Not distinctive alone. |
| No observable operations | Supports | Weakens | Supports | Could reflect holding company. |
| Direct legitimate commercial contract | Neutral | Supports | Neutral | Need pricing/related-party context. |
| Sequential asset transfer after contract | Supports | Neutral | Supports | Temporal association, not causation. |

## 18.3 Disconfirming search

Analysts SHALL deliberately search for evidence that would weaken the leading hypothesis. This search and its result SHALL be documented for High/Critical cases.

## 18.4 Hypothesis status

- OPEN — actively tested.

- SUPPORTED — evidence currently favours the hypothesis.

- WEAKENED — contradicting evidence materially reduces plausibility.

- REJECTED — evidence is inconsistent with the hypothesis.

- INCONCLUSIVE — evidence is insufficient or balanced.

# 19. Structured Analytical Techniques

Analysts MAY use structured techniques provided the method is transparent and does not create false mathematical precision.

## 19.1 Recommended techniques

- Chronology/timeline analysis.

- Entity-link and ownership mapping.

- Value-flow reconstruction.

- Comparison of declared versus observed relationships.

- Pattern and typology mapping.

- Competing-hypothesis matrix.

- Source cross-validation.

- Peer-group or baseline comparison when a defensible baseline exists.

- Cross-case correlation.

- Gap analysis and collection requirements.

## 19.2 Prohibited analytical shortcuts

- Treating network centrality as guilt.

- Treating PEP status, religion, ethnicity, nationality, activism, NPO status, or political association as a standalone AML indicator.

- Treating secrecy, privacy, offshore use, cash use, remittance, or crypto use as inherently illicit.

- Using opaque AI scores as final findings.

- Converting a weak match into an entity merge to “complete” the graph.

- Conflating correlation, sequence, opportunity, and causation.

# 20. Confidence and Uncertainty

Confidence describes the analyst’s confidence in an assessment given evidence quality, consistency, independence, coverage, and unresolved alternatives. It does not describe the probability that a person is guilty.

| **Confidence** | **Typical conditions** |
|----|----|
| LOW | Material evidence is limited, conflicting, weakly corroborated, or core identity/value-flow questions remain unresolved. |
| MODERATE | Multiple evidence lines support the judgement, but important gaps or viable alternatives remain. |
| HIGH | Multiple independent, strong evidence lines converge; key alternatives have been tested and materially weakened; critical gaps are limited. |
| INSUFFICIENT_BASIS | A judgement was attempted but the available evidential basis is insufficient to support any confidence level. This is not a level below LOW. *[v0.1.1 · A09]* |

Confidence wire values are `HIGH`, `MODERATE`, `LOW`, and `INSUFFICIENT_BASIS` (Data Model Specification v0.1.1, Section 14.1 and Annex A). A rationale is mandatory for every value. INSUFFICIENT_BASIS SHALL NOT be converted to LOW, null, zero, or omitted; a missing (null) confidence is permitted only on drafts where no judgement has yet been made, and a finalized assessment SHALL carry a non-null value. *[v0.1.1 · A09]*

## 20.1 Confidence statement format

**Required pattern:** Assessment + confidence + principal basis + principal caveat.

Example: “Available evidence supports with MODERATE confidence that Companies A and B were under common operational control during 2025, based on overlapping directors, authorised signatories, address infrastructure, and contract execution. Beneficial ownership remains unresolved and no direct financial transfer between the companies has been established.”

## 20.2 Do not quantify without basis

Percent probabilities SHOULD NOT be used unless the organisation has a validated, documented quantitative method and the data support calibration. Narrative confidence is preferred for ordinary CS-AML work.

# 21. Intelligence Gaps and Collection Feedback

An intelligence gap is a material unknown that affects interpretation, confidence, or actionability. Gaps SHALL be visible, not hidden in prose.

| **Gap ID** | **Question** | **Impact** | **Priority** | **Collection option** | **Status** |
|----|----|----|----|----|----|
| G-01 | Who beneficially controls Company B? | High — affects ownership hypothesis | Critical | BO registry, filings, contracts, interviews | Open |
| G-02 | What consideration was paid for Property X? | Medium — affects value-flow reconstruction | High | Property record, court file, seller source | Open |

New gaps SHOULD update the Collection Plan. Collection SHOULD stop when marginal analytical value becomes lower than the legal, safety, privacy, or resource cost.

# 22. Cross-Case and Network Analysis

Reusable entity records permit cross-case intelligence, but cross-case correlation increases privacy and inference risk.

## 22.1 Cross-case rules

- A cross-case link SHALL identify its evidence basis and source cases.

- Case access restrictions SHALL carry into cross-case views where appropriate.

- Analysts SHALL NOT expose a sensitive case merely because a shared entity appears in another case.

- Cross-case correlation MAY create a new Network Investigation when the relationship is analytically material.

- Automated similarity suggestions SHALL be treated as leads until reviewed.

## 22.2 Network investigation triggers

- Repeated beneficial-owner or nominee pattern across unrelated cases.

- Shared intermediaries, addresses, professionals, wallets, companies, or assets across cases.

- Recurring procurement/vendor pattern.

- Repeated asset-conversion sequence.

- Recurring typology with common infrastructure.

# 23. Assessment Writing

Assessment writing SHALL be precise, bounded, evidence-linked, and calibrated to confidence.

## 23.1 Key judgements

A final product SHOULD begin with a small number of Key Judgements. Each judgement SHALL state confidence and material caveats.

## 23.2 Language discipline

| **Avoid** | **Prefer** |
|----|----|
| “X laundered money.” | “The observed structure is consistent with \[typology\] to \[level\], but direct evidence of laundering has not been established.” |
| “X owns the villa.” | “The villa is legally owned by Company Y; available evidence indicates X may exercise control/use. Beneficial ownership is unresolved.” |
| “Money flowed from contract to property.” | “The property acquisition followed the contract award and is linked through related entities; the intervening financial transfer is reconstructed, not directly evidenced.” |
| “Suspicious company.” | “The company exhibits the following documented indicators...” |

## 23.3 Mandatory caveats

Where applicable, products SHALL disclose that civil society lacks compulsory access to bank records, tax records, beneficial-ownership verification, or other non-public data necessary to establish certain mechanisms.

# 24. Peer Review, Challenge, and Red-Team Review

Review is a substantive analytical control, not copy-editing.

## 24.1 Peer reviewer questions

- Can every key judgement be traced to evidence?

- Are identity merges defensible?

- Are facts time-bounded?

- Are graph relationships typed accurately?

- Is a reconstructed flow clearly distinguished from a direct flow?

- Were benign alternatives tested?

- What evidence most strongly contradicts the assessment?

- Does confidence match evidence quality and gaps?

- Is personal data necessary and proportionate?

- Could wording imply guilt beyond the evidence?

## 24.2 Red-team review triggers

High/Critical cases, major public allegations, cases involving vulnerable persons, high-profile officials, cross-border legal exposure, or novel analytical models SHOULD receive enhanced challenge by a reviewer who was not part of the core investigation.

## 24.3 Review outcomes

- APPROVE.

- APPROVE WITH CONDITIONS.

- RETURN FOR ANALYSIS.

- NARROW OR REDACT.

- DO NOT DISSEMINATE.

# 25. Dissemination, Referral, and Publication

The same analysis may require different products for internal decision-makers, trusted partners, competent authorities, or public publication. Dissemination SHALL be purpose-limited.

| **Product** | **Typical audience** | **Characteristics** |
|----|----|----|
| Analytical Note | Internal team | Rapid, clearly caveated, may contain unresolved leads. |
| Investigation Brief | Management/partner | Structured findings, graph/timeline, confidence, gaps. |
| Financial Intelligence Package | Competent authority / trusted specialist | Evidence index, entity profiles, source provenance, value-flow analysis, typology/hypothesis assessment, handling caveats. |
| Public Investigation Report | Public/media/advocacy | Fact-checked, minimised personal data, legal/privacy reviewed, source-protection applied. |
| Referral Memorandum | PPATK/LEA/regulator or authorised recipient | Concise allegation/issue, supporting evidence, identities, relationships, gaps, contact channel, handling restrictions. |

## 25.1 Dissemination classification

Every product SHALL carry an information classification from the five-level CS-AML model (Data Model Specification v0.1.1, Section 16): PUBLIC, INTERNAL, SENSITIVE, RESTRICTED, SOURCE_PROTECTED. Unknown or missing classification fails closed. A product inherits the highest classification of its inputs unless a recorded reviewer downgrade decision exists. *[v0.1.1 · A08]*

The intended dissemination scope is recorded separately from the classification, with access labels where needed: *[v0.1.1 · A08]*

- Organisation only (internal use).

- Named project/partner group — recorded as a compartment/purpose access label, not as a classification level.

- Referral — prepared for a competent authority or designated recipient; recorded as a Dissemination record (recipient, purpose), not as a classification level.

- Public release — requires classification PUBLIC after review and approval.

Legacy note: v0.1 listed INTERNAL / RESTRICTED / CONFIDENTIAL / REFERRAL / PUBLIC here. CONFIDENTIAL (need-to-know, sensitive sources or data) maps to SENSITIVE or RESTRICTED as decided by the data owner, or to SOURCE_PROTECTED where the reason is source-identifying information; it SHALL NOT be mapped automatically. *[v0.1.1 · A08]*

## 25.2 Referral threshold

Referral SHOULD be based on actionable, structured information rather than certainty of a crime. A referral SHALL clearly distinguish established facts, analytical assessments, and unresolved allegations. PPATK’s public engagement with NGO/CSO emphasises the usefulness of better-quality supporting information; CS-AML therefore prioritises structured, evidence-linked referral packages.

## 25.3 Publication threshold

Publication normally requires a higher harm-control standard than internal analysis or confidential referral. The organisation SHALL consider factual accuracy, public interest, necessity of naming individuals, source protection, privacy, defamation exposure, and whether the wording fairly reflects uncertainty.

# 26. Closure, Monitoring, and Reopening

Cases SHALL be closed, suspended, converted to monitoring, or escalated; they SHOULD NOT remain indefinitely open by default.

## 26.1 Closure reasons

- Question answered.

- Hypothesis rejected or unsupported.

- Insufficient lawful evidence and no proportionate collection path.

- Referred to competent authority or partner.

- Merged into network investigation.

- Risk exceeds organisational capacity.

- Public-interest rationale no longer sufficient.

## 26.2 Closure record

- Disposition.

- Final key judgement.

- Confidence.

- Unresolved gaps.

- Disseminations/referrals.

- Retention/destruction decision.

- Monitoring triggers, if any.

- Lessons learned and typology updates.

## 26.3 Reopening triggers

A case MAY reopen on new evidence, authoritative findings, relevant ownership/asset changes, related-case correlation, or a new allegation that materially changes the analytical picture. Reopening SHALL create an audit record and refreshed risk review.

# 27. Quality Assurance and Auditability

Quality assurance assesses whether the methodology was followed and whether analytical products are useful, proportionate, and reproducible.

## 27.1 Minimum QA checks

- Case charter completeness.

- Source and provenance completeness.

- Evidence integrity.

- Fact/claim separation.

- Entity-resolution decisions.

- Relationship evidence links.

- Value-flow classification.

- Typology use and caveats.

- Hypothesis testing.

- Confidence calibration.

- Gap visibility.

- Peer review.

- Dissemination approval.

- Retention compliance.

## 27.2 Effectiveness metrics

| **Metric family** | **Examples** |
|----|----|
| Quality | % key judgements with direct evidence links; peer-review rework rate; identity-merge reversal rate. |
| Timeliness | Time from intake to triage; time to first analytical assessment; referral preparation time. |
| Actionability | % referrals acknowledged; partner feedback; information requests generated by product. |
| Proportionality | Volume of sensitive data collected versus used; deletion/minimisation rate. |
| Learning | Typology updates; recurring gaps; detection of repeated infrastructure across cases. |
| Safety | Source/security incidents; unauthorized disclosures; high-risk access exceptions. |

Metrics SHALL NOT reward volume of suspects, allegations, or personal data collected.

# 28. Technology-Enabling Requirements

Technology supports methodology; it does not replace analyst judgement. Any CS-AML platform SHOULD implement the following methodological controls.

- Case and scope management.

- Source registry and immutable provenance fields.

- Evidence repository with hashing/versioning.

- Claim/fact/indicator objects.

- Reusable entity store with reversible entity merges.

- Typed, dated, evidence-linked relationships.

- Asset and event models.

- Direct/documented/reconstructed/hypothetical value-flow classes.

- Typology worksheets linked to Catalogue IDs.

- Hypothesis matrix and disconfirming evidence.

- Confidence and intelligence-gap fields.

- Role-based access and sensitive-source compartmentalisation.

- Peer review and approval workflow.

- Audit history.

- Controlled export/redaction.

- Cross-case correlation with access-aware filtering.

## 28.1 Automation and AI

Automation MAY assist extraction, translation, entity suggestions, document classification, similarity detection, and graph discovery. Automated outputs SHALL be labelled as machine-generated until reviewed. AI SHALL NOT independently establish guilt, assign criminality, merge high-impact identities, or approve dissemination.

# 29. Roles, Competencies, and Separation of Duties

| **Role** | **Core responsibilities** | **Minimum competency** |
|----|----|----|
| Case Owner | Purpose, scope, resources, closure | Public-interest rationale; risk judgement; governance. |
| Lead Analyst | Analysis plan, hypotheses, assessment | Financial investigation concepts; structured analysis; writing. |
| Collector/Researcher | Lawful acquisition, provenance | OSINT/research methods; source handling. |
| Evidence Custodian | Integrity, storage, preservation | Digital evidence basics; records management. |
| Peer Reviewer | Challenge and quality | Independent analytical judgement; framework knowledge. |
| Legal/Privacy Reviewer | Rights and legal risk | Applicable law/policy; privacy/defamation/data protection. |
| Security Owner | Operational and information security | Access control, incident response, source protection. |
| Approver | Dissemination authority | Organisational accountability and risk acceptance. |

Small organisations MAY combine roles, but high-impact dissemination SHOULD preserve at least one independent reviewer/approver distinct from the primary analyst.

# 30. Conformance Requirements for Methodology

An implementation claiming alignment with CS-AML Investigation Methodology v0.1.1 SHALL demonstrate the following minimum artefacts for a material investigation:

- Intake/Triage Record.

- Investigation Charter.

- Investigation Risk Assessment.

- Collection Plan.

- Source Register.

- Evidence Register.

- Entity Resolution Decisions for contested/high-impact identities.

- Relationship/Asset/Event records linked to evidence.

- Value-Flow Worksheet where economic movement is material.

- Typology Worksheet where a typology is referenced.

- Hypothesis Matrix including contradictory/disconfirming evidence.

- Intelligence Gap Register.

- Assessment with confidence statement.

- Peer Review Record.

- Dissemination/Referral Approval.

- Closure or Monitoring Record.

- Audit history sufficient to reconstruct material changes.

## 30.1 Methodology conformance levels

| **Level** | **Characteristics** |
|----|----|
| M1 — Basic | Manual artefacts; minimum provenance, hypothesis, peer review, dissemination approval. |
| M2 — Operational | Structured registers, formal risk review, entity resolution, typology/value-flow worksheets, QA. |
| M3 — Integrated | Technology-enforced provenance, graph/value-flow integration, cross-case controls, role-based workflow, metrics. |
| M4 — Assured | Independent assurance, periodic control testing, calibrated automated analytics where used, mature privacy/security governance. |

# 31. Standard Operating Sequence

``` text
01 Receive intake
```

``` text
02 Preserve original intake
```

``` text
03 Triage legitimacy and urgency
```

``` text
04 Create Investigation Charter
```

``` text
05 Perform risk/harm review
```

``` text
06 Define Information Requirements
```

``` text
07 Approve Collection Plan
```

``` text
08 Collect and preserve sources
```

``` text
09 Register evidence and provenance
```

``` text
10 Resolve core entities
```

``` text
11 Build relationships, assets, and events
```

``` text
12 Construct timeline
```

``` text
13 Map direct/documented value flows
```

``` text
14 Reconstruct value flows where justified
```

``` text
15 Map candidate typologies
```

``` text
16 Create/test competing hypotheses
```

``` text
17 Identify contradictory evidence and gaps
```

``` text
18 Draft key judgements and confidence
```

``` text
19 Peer/red-team review
```

``` text
20 Legal/privacy/publication review where applicable
```

``` text
21 Approve dissemination/referral/publication
```

``` text
22 Close, monitor, or reopen
```

``` text
23 Capture lessons and typology updates
```

# 32. Annex A — Investigation Charter Template

| **Field**               | **Template prompt**                      |
|-------------------------|------------------------------------------|
| Case ID / Title         |                                          |
| Public-interest purpose | Why is this investigation justified?     |
| Primary question        | What specific question must be answered? |
| Secondary questions     |                                          |
| Subjects / entities     |                                          |
| Excluded scope          |                                          |
| Time period             |                                          |
| Jurisdictions           |                                          |
| Predicate issue(s)      | Established / alleged / unknown          |
| Initial hypotheses      | Include plausible benign alternative     |
| Expected data classes   |                                          |
| Sensitive data expected |                                          |
| Expected outputs        |                                          |
| Risk level              | Low / Moderate / High / Critical         |
| Required reviewers      |                                          |
| Review date             |                                          |
| Stop conditions         |                                          |

# 33. Annex B — Collection Plan Template

| **IR ID** | **Information Requirement** | **Priority** | **Source classes** | **Method** | **Lawful-access note** | **Sensitivity** | **Success/stop condition** |
|----|----|----|----|----|----|----|----|
| IR-01 |  |  |  |  |  |  |  |
| IR-02 |  |  |  |  |  |  |  |
| IR-03 |  |  |  |  |  |  |  |

# 34. Annex C — Source & Evidence Evaluation Template

| **Field**                     | **Entry** |
|-------------------------------|-----------|
| Source ID                     |           |
| Evidence ID                   |           |
| Source type                   |           |
| Origin / URL / provider       |           |
| Acquisition date/time         |           |
| Collection method             |           |
| Lawful-access note            |           |
| Reliability rating (A–F)      |           |
| Information credibility (1–6) |           |
| Hash / preservation           |           |
| Sensitivity / handling        |           |
| Related claims                |           |
| Verification notes            |           |

# 35. Annex D — Entity Resolution Decision Template

| **Field**              | **Entry**                                        |
|------------------------|--------------------------------------------------|
| Candidate records      |                                                  |
| Proposed entity        |                                                  |
| Matching attributes    |                                                  |
| Conflicting attributes |                                                  |
| Evidence               |                                                  |
| Decision               | MERGED / LINKED_POSSIBLE / SEPARATE / UNRESOLVED *[v0.1.1 · A09]* |
| Confidence             | HIGH / MODERATE / LOW / INSUFFICIENT_BASIS *[v0.1.1 · A09]* |
| Analyst                |                                                  |
| Reviewer               |                                                  |
| Date                   |                                                  |
| Reversal notes         |                                                  |

# 36. Annex E — Value-Flow Worksheet

| **Flow ID** | **Origin** | **Destination/asset** | **Value** | **Date** | **Mechanism** | **Class** | **Evidence** | **Confidence** | **Assumptions/gaps** |
|----|----|----|----|----|----|----|----|----|----|
| VF-01 |  |  |  |  |  |  |  |  |  |
| VF-02 |  |  |  |  |  |  |  |  |  |

# 37. Annex F — Typology Worksheet

| **Field** | **Entry** |
|----|----|
| Typology ID / name |  |
| Observed mechanism |  |
| M indicators |  |
| C indicators |  |
| K indicators |  |
| D indicators |  |
| Gaps |  |
| Alternative explanations |  |
| Consistency level | No basis / Weak / Plausible / Strong / Compelling |
| Confidence / caveat |  |
| Supporting evidence IDs |  |

# 38. Annex G — Hypothesis Matrix Template

| **Evidence / observation** | **H1** | **H2** | **H3** | **Diagnosticity / notes** |
|----------------------------|--------|--------|--------|---------------------------|
|                            |        |        |        |                           |
|                            |        |        |        |                           |
|                            |        |        |        |                           |
|                            |        |        |        |                           |

# 39. Annex H — Intelligence Gap Register

| **Gap ID** | **Question / missing fact** | **Impact** | **Priority** | **Collection option** | **Owner** | **Status** |
|----|----|----|----|----|----|----|
| G-01 |  |  |  |  |  |  |
| G-02 |  |  |  |  |  |  |

# 40. Annex I — Peer Review Checklist

- Investigation question remains within approved scope.

- Key facts are evidence-linked and time-bounded.

- Contested entities are resolved appropriately.

- Relationships do not overstate control or ownership.

- Direct and reconstructed value flows are visually/textually distinct.

- Typology analysis includes disconfirming indicators and gaps.

- Leading hypothesis has been challenged.

- Alternative explanations are fairly represented.

- Confidence matches evidence and uncertainty.

- Sensitive personal data are necessary and minimised.

- Key judgements are not stronger than the evidence.

- Referral/publication wording distinguishes fact, assessment, and allegation.

# 41. Annex J — Intelligence Product Template

- Document control and handling classification.

- Executive assessment / Key Judgements.

- Investigation question and scope.

- Method and limitations.

- Key entities and relationships.

- Timeline.

- Asset analysis.

- Value-flow analysis.

- Typology analysis.

- Hypothesis assessment.

- Contradictory/disconfirming evidence.

- Confidence statement.

- Intelligence gaps.

- Source/evidence index.

- Recommended next steps.

- Dissemination and redaction notes.

# 42. Annex K — Closure / Monitoring Record

| **Field** | **Entry** |
|----|----|
| Case ID |  |
| Disposition | Closed / Suspended / Monitoring / Referred / Merged |
| Final key judgement |  |
| Confidence |  |
| Unresolved gaps |  |
| Disseminations/referrals |  |
| Retention decision |  |
| Monitoring triggers |  |
| Lessons learned |  |
| Typology/catalogue update needed |  |
| Approved by / date |  |

# 43. Glossary

| **Term** | **CS-AML meaning** |
|----|----|
| Assessment | A reasoned analytical judgement that states confidence, basis, caveats, and gaps. |
| Claim | A proposition asserted by a source; not automatically accepted as fact. |
| Evidence | A preserved item or extract supporting or contradicting a proposition. |
| Fact | A proposition sufficiently established for the current analytical purpose. |
| Indicator | A fact or pattern relevant to risk or a typology. |
| Intelligence gap | A material unknown affecting judgement, confidence, or actionability. |
| Hypothesis | A testable explanatory proposition. |
| Provenance | Traceable origin and handling history of information/evidence. |
| Reconstructed value flow | An inferred economic sequence supported by evidence but lacking a direct transfer record. |
| Typology | A known pattern or mechanism used to understand possible laundering or financial-crime behaviour. |

# 44. References and Source Lineage

- Financial Action Task Force (FATF), The FATF Recommendations, as amended June 2026.

- FATF, Money Laundering National Risk Assessment Guidance, updated 28 August 2025.

- FATF, Financial Investigations Guidance (Operational Issues). Pending verification — specific publication/section not yet identified. *[v0.1.1 · A13]*

- FATF, Investigating Professional Money Laundering, Underground Banking, and the Use of Hawala and Other Similar Service Providers, 3 September 2026.

- United Nations Office on Drugs and Crime (UNODC), Civil Society Guide to the UNCAC / civil-society entry points for asset tracing and recovery (https://www.unodc.org/documents/NGO/Corruption/251113-CSU-UNCAC_Guide-Web.pdf). Pending verification — page-level support not confirmed. *[v0.1.1 · A13]*

- UNODC, Manual on International Cooperation for the Purposes of Confiscation of Proceeds of Crime — asset tracing sections. Pending verification — specific publication/section not yet identified. *[v0.1.1 · A13]*

- PPATK, Klinik Dumas Special Edition: PPATK dan NGO/CSO Perkuat Aduan TPPU melalui peluncuran lapor.ppatk.go.id, 26 November 2025.

- CS-AML Framework v0.1.1 Expanded (`CS-AML_Framework_v0.1.1_Expanded.md`). *[v0.1.1 · A01]*

- CS-AML Typology Catalogue v0.1.1 (`CS-AML_Typology_Catalogue_v0.1.1.md`). *[v0.1.1 · A01]*

- CS-AML Data Model Specification v0.1.1 (`CS-AML_Data_Model_Specification_v0.1.1.md`) — authoritative registry for classification, flow-class, and confidence enumerations. *[v0.1.1 · A08, A09]*

Reference lineage informs the methodology; it does not mean that each CS-AML step, gate (G0–G6), grade, or threshold is derived from a cited source — these are CS-AML design conventions unless a specific source is cited. *[v0.1.1 · A13, N01]* Reference lineage does not transform CS-AML into an official FATF, UNODC, PPATK, FIU, law-enforcement, or regulated-entity standard. Jurisdiction-specific legal advice remains necessary for sensitive collection, data processing, referral, and publication decisions.
