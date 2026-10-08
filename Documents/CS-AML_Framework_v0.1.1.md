**CS-AML FRAMEWORK**

Civil Society Anti-Money Laundering & Financial Intelligence Framework

**Version 0.1 \| Normative Draft \| October 2026**

> **Document status — v0.1.1 (LEGACY)**
> **Legacy — superseded by CS-AML Framework v0.1.1 Expanded (`CS-AML_Framework_v0.1.1_Expanded.md`); retained for history; do not use as an implementation source.** *[v0.1.1 · A01, N08]*
> Version: 0.1.1 — Legacy (content unchanged from v0.1 except for the notes marked v0.1.1). *[v0.1.1 · A01]*
> Supersedes: CS-AML Framework v0.1. The DOCX/PDF files in this repository are the unchanged v0.1 baseline (legacy). Where this file and the Expanded framework differ, the Expanded framework governs.
> Validation: not validated. No recorded approval decision, implementation test result, or independent audit exists for this baseline. Acceptance criteria in this document are targets, not evidence that tests have passed.
> CS-AML is not an external standard or certification. References to FATF, Wolfsberg, PPATK, UNODC or other bodies do not imply their endorsement.
> Changes in 0.1.1: see `CHANGELOG.md` at the repository root (audit findings A01–A16).

> **Purpose**
>
> A structured, evidence-based framework for civil society organisations, investigative journalists, public-interest researchers, and accountability actors to develop lawful, reproducible, and responsible financial intelligence without assuming the powers or access rights of regulated financial institutions, FIUs, or law-enforcement agencies.

This document defines the minimum analytical, evidentiary, governance, and technology-neutral requirements for CS-AML v0.1. It is designed as an internal standard and reference model. It does not create legal powers, does not authorise access to non-public financial records, and is not a substitute for legal advice, statutory AML obligations, FIU analysis, or criminal investigation.

# Document Control

| **Field** | **Value** |
|----|----|
| Document | CS-AML Framework v0.1 |
| Status | Legacy — superseded by CS-AML Framework v0.1.1 Expanded (`CS-AML_Framework_v0.1.1_Expanded.md`); retained for history; do not use as an implementation source *[v0.1.1 · A01, N08]* |
| Version | 0.1.1 (legacy copy of v0.1 content) *[v0.1.1 · A01]* |
| Date | October 2026 |
| Primary audience | Civil society organisations, investigative journalists, public-interest researchers, accountability and anti-corruption actors |
| Primary function | Open-source and lawfully sourced financial intelligence and AML-oriented investigation |
| Not intended as | Bank transaction-monitoring standard, STR/SAR filing standard, law-enforcement procedure, or legal opinion |

## Normative Language

The key words MUST, MUST NOT, SHALL, SHALL NOT, SHOULD, SHOULD NOT, MAY, and OPTIONAL are used to distinguish mandatory controls from recommended and discretionary practices.

| **Term** | **Meaning** |
|----|----|
| MUST / SHALL | Mandatory for conformance with CS-AML v0.1. |
| MUST NOT / SHALL NOT | Prohibited within a conformant implementation. |
| SHOULD | Strongly recommended; deviation requires documented rationale. |
| SHOULD NOT | Normally avoided; use requires documented rationale. |
| MAY | Permitted but optional. |

## Conformance Levels

| **Level** | **Minimum expectation** |
|----|----|
| Foundational | Case, source, evidence, entity, relationship, hypothesis, assessment, audit trail, and guardrails are implemented. |
| Operational | Adds asset mapping, event/timeline analysis, value-flow analysis, typology mapping, peer review, and intelligence products. |
| Advanced | Adds entity resolution automation, graph analytics, structured confidence scoring, cross-case correlation, quality assurance, and controlled data integrations. |

# 1. Purpose, Scope, and Positioning

## 1.1 Purpose

CS-AML is a civil-society financial-intelligence framework for transforming lawful information into structured, reviewable, and decision-useful financial intelligence. Its primary objective is to support public-interest investigation while preserving analytical discipline, source protection, privacy, provenance, and procedural fairness.

- Identify relationships among persons, organisations, companies, assets, contracts, events, and economic value.

- Reconstruct value flows where direct banking data is unavailable.

- Compare observed patterns with known money-laundering and financial-crime typologies.

- Test competing hypotheses rather than confirming a predetermined allegation.

- Produce intelligence products suitable for internal decision-making, further investigation, lawful referral, or responsible publication.

## 1.2 Scope

CS-AML v0.1 applies to investigations based on public information, lawfully obtained records, voluntary disclosures, whistleblower material received through lawful channels, and other sources that the organisation is authorised to process. It is technology-neutral and can be implemented using paper procedures, spreadsheets, case-management systems, graph databases, or integrated investigative platforms.

## 1.3 Position in the AML Ecosystem

``` text
Regulated institution               Civil society                         State authority
```

``` text
KYC / transaction monitoring   ->  research / investigation   ->  FIU / regulator / law enforcement
```

``` text
STR / SAR obligations              public-interest intelligence    statutory analysis / coercive powers
```

Civil society does not become a regulated AML reporting entity merely by using this framework. CS-AML operates as an independent investigative and intelligence discipline. In Indonesia, PPATK has explicitly recognised that initial information from NGO/CSO and the public can contribute to early detection of suspected money laundering. This framework therefore focuses on improving the quality, structure, reproducibility, and responsible handling of such information.

# 2. Foundational Principles

### P1. Evidence before allegation

Investigation SHALL begin with an issue, question, anomaly, or relationship to be tested—not with a presumption of guilt.

### P2. Follow the value

Investigators SHALL follow economic value through money, assets, ownership, control, contracts, debt, benefits, and other forms of economic transfer. Direct bank records are not required to reconstruct every relevant value relationship.

### P3. Lawful and proportionate collection

Information MUST be collected and processed lawfully, for a defined purpose, and in a manner proportionate to investigative need.

### P4. Fact ≠ inference ≠ hypothesis ≠ allegation

Every analytical statement MUST be classified so readers can distinguish what is directly evidenced from what is inferred or alleged.

### P5. Competing hypotheses

Investigators MUST identify reasonable alternative explanations and actively search for contradicting evidence.

### P6. Data minimisation

The organisation MUST NOT collect personal or sensitive data merely because it is technically obtainable.

### P7. Provenance and reproducibility

Material findings MUST be traceable to sources, evidence, analytical steps, dates, and responsible analysts.

### P8. Source and subject protection

The safety of sources, whistleblowers, staff, subjects, and affected communities MUST be incorporated into collection, storage, review, and dissemination decisions.

### P9. Human judgement

Automated tools MAY support analysis but MUST NOT independently convert a pattern match into an allegation or adverse determination.

### P10. Right-sized risk

Controls SHOULD be proportionate to risk; low-risk inquiries should not be burdened with unnecessary intrusive measures, while high-risk matters require stronger review and protection.

> **Analytical Chain**
>
> SOURCE → EVIDENCE → FACT → INDICATOR → HYPOTHESIS → ASSESSMENT → INTELLIGENCE PRODUCT. A conformant implementation SHALL preserve this distinction throughout the lifecycle.

# 3. Investigation Lifecycle

| **Stage** | **Name** | **Required outcome** |
|----|----|----|
| 1 | Case initiation | Capture the trigger, public-interest purpose, intake source, and initial risk. |
| 2 | Scoping | Define investigation question, subjects, time period, jurisdiction, exclusions, and expected outputs. |
| 3 | Collection planning | Identify lawful sources, collection methods, data minimisation constraints, and source risks. |
| 4 | Collection and preservation | Acquire, archive, hash where appropriate, and document provenance. |
| 5 | Entity resolution | Determine whether records refer to the same person, organisation, asset, or other entity. |
| 6 | Relationship mapping | Create explicit, sourced relationships among entities. |
| 7 | Asset and event mapping | Identify ownership/control/use of assets and build a dated event timeline. |
| 8 | Value-flow reconstruction | Map transfers or transformations of economic value, with uncertainty explicitly recorded. |
| 9 | Typology and indicator analysis | Compare facts and patterns with recognised typologies without treating similarity as proof. |
| 10 | Hypothesis testing | Evaluate supporting, contradicting, missing, and alternative explanations. |
| 11 | Assessment | Produce analytic judgements with confidence statements and intelligence gaps. |
| 12 | Review and dissemination | Peer review, legal/editorial review as appropriate, then close, continue, refer, or publish. |

## 3.1 Lifecycle Gate Requirements

The following gates SHALL prevent weak or unsafe cases from automatically progressing:

- Gate A – Authority and purpose: lawful purpose and access basis are documented before intrusive collection.

- Gate B – Evidence sufficiency: material facts have source provenance before typology mapping.

- Gate C – Analytical integrity: competing hypotheses and intelligence gaps are recorded before final assessment.

- Gate D – Dissemination review: sensitive external reporting receives peer review and appropriate legal/editorial review.

# 4. Core Domain Model

``` text
CASE
```

``` text
├── SOURCE
```

``` text
├── EVIDENCE
```

``` text
├── ENTITY
```

``` text
├── RELATIONSHIP
```

``` text
├── ASSET
```

``` text
├── EVENT
```

``` text
├── VALUE FLOW
```

``` text
├── INDICATOR
```

``` text
├── TYPOLOGY
```

``` text
├── HYPOTHESIS
```

``` text
├── ASSESSMENT
```

``` text
└── INTELLIGENCE PRODUCT
```

The domain model defines semantic separation between records. Implementations MAY use different database schemas, but they SHALL preserve equivalent distinctions.

## 4.1 Case

A Case is the investigative context, not the primary container of truth. A person, company, asset, source, or evidence item MAY be relevant to multiple cases. Systems SHOULD support controlled cross-case linking without duplicating or silently mutating source records.

| **Required field** | **Description** |
|----|----|
| Case ID | Unique persistent identifier. |
| Title | Neutral, descriptive title; SHOULD NOT assert guilt. |
| Investigation question | The principal question the case seeks to answer. |
| Purpose/public interest | Why the investigation is legitimate and necessary. |
| Scope | Subjects, period, jurisdictions, included and excluded issues. |
| Predicate issue | Known or alleged underlying conduct, if relevant. |
| Status | Intake, scoped, collecting, analysing, review, disseminated, closed. |
| Risk classification | Operational, source, legal, privacy, and safety risks. |
| Owner/reviewer | Responsible analyst and reviewer. |
| Retention class | Required retention and disposal handling. |

## 4.2 Source

A Source describes where information originates. It SHALL be distinct from the evidence extracted from it.

| **Attribute** | **Requirement** |
|----|----|
| Source ID | Persistent unique identifier. |
| Source type | Registry, court record, procurement record, media, website, social media, interview, whistleblower, dataset, document, other. |
| Publisher/custodian | Who published or supplied it. |
| Location | URL, archive URI, repository path, or physical reference. |
| Access date | When the organisation accessed it. |
| Publication date | Where known. |
| Access status | Public, permissioned, confidential, restricted, unknown. |
| Reliability | Source reliability rating plus rationale. |
| Preservation | Archived copy or reason not retained. |
| Sensitivity | Public, internal, confidential, highly restricted. Superseded: use the five-level classification (PUBLIC, INTERNAL, SENSITIVE, RESTRICTED, SOURCE_PROTECTED) and legacy mapping in the Data Model Specification v0.1.1, Section 16, and Framework v0.1.1 Expanded, Section 6.4. *[v0.1.1 · A08]* |

## 4.3 Evidence

Evidence is a preserved item or extract that supports or contradicts an analytical proposition. Evidence SHALL retain a link to its Source and MUST NOT be rewritten in a manner that obscures the original context.

- Digital evidence SHOULD be preserved in original form when lawful and feasible.

- Material files SHOULD have a cryptographic hash recorded, preferably SHA-256.

- Screenshots SHOULD include enough context to identify the page, date, and relevant content; a screenshot alone SHOULD NOT replace preserved source content where an archive is available.

- Translations and analyst extracts MUST identify the original material and translator/analyst where relevant.

## 4.4 Entity

An Entity is a uniquely tracked object about which facts and relationships are recorded. Entities SHOULD use stable internal identifiers independent of names.

| **Entity class** | **Examples** |
|----|----|
| Person | Natural person, aliases, public official, professional intermediary. |
| Organisation | Company, NGO, foundation, agency, trust or other legal arrangement. |
| Financial identifier | Account reference, wallet, payment handle—only where lawfully obtained. |
| Asset | Property, vehicle, vessel, aircraft, securities, digital asset. |
| Contact/technical | Phone, email, domain, address, device identifier where lawful and relevant. |
| Commercial/public | Contract, procurement project, grant, licence, concession. |
| Document/case | Court case, corporate filing, licence, report, invoice, deed. |

## 4.5 Entity Resolution

Entity resolution is the process of deciding whether multiple records refer to the same real-world entity. A conformant implementation SHALL support uncertainty and SHALL NOT force uncertain matches into a single entity.

| **Evidence class** | **Examples** | **Typical weight** |
|----|----|----|
| Strong identifiers | Registration number, verified date of birth plus another identifier, official unique ID where lawful. | High |
| Strong relational | Same confirmed beneficial owner, same verified legal address plus matching officers. | Medium–High |
| Weak identifiers | Name similarity, shared surname, common address, visual resemblance. | Low |
| Contextual | Same business domain, same event, same social network. | Low–Medium |

Every merge SHOULD record match reason, supporting evidence, confidence, analyst, and date. Every split or reversal SHOULD preserve the audit history.

## 4.6 Relationship

A Relationship is an explicit, directional or non-directional link between two entities. The relationship SHALL carry its own evidence and confidence; it MUST NOT inherit confidence simply because both entities are verified.

| **Relationship family** | **Examples** |
|----|----|
| Ownership/control | OWNS, BENEFICIAL_OWNER_OF, CONTROLS, NOMINEE_FOR. |
| Governance/employment | DIRECTOR_OF, COMMISSIONER_OF, EMPLOYED_BY, REPRESENTS. |
| Personal/association | RELATIVE_OF, ASSOCIATE_OF, BUSINESS_PARTNER_OF. |
| Shared attributes | SHARES_ADDRESS_WITH, SHARES_PHONE_WITH, SHARES_DEVICE_WITH. |
| Commercial | SUPPLIER_TO, CONTRACTED_BY, SUBCONTRACTED_TO, INVESTED_IN. |
| Financial/value | PAID_BY, TRANSFERRED_TO, LOANED_TO, DONATED_TO. |
| Asset | OWNS_ASSET, CONTROLS_ASSET, USES_ASSET, SOLD_TO, LEASED_TO. |

## 4.7 Asset

Asset records SHALL distinguish legal ownership, beneficial ownership, control, possession/use, and economic benefit. These concepts MUST NOT be collapsed into a single “owner” field.

| **Field** | **Examples** |
|----|----|
| Asset type | Land/building, vehicle, vessel, aircraft, shareholding, security, crypto asset, IP right. |
| Legal owner | Person/entity appearing in authoritative ownership record. |
| Possible beneficial owner | Analytical proposition, with evidence and confidence. |
| Controller/user | Who appears to control or use the asset. |
| Value | Known price, declared value, estimate, range, or unknown. |
| Acquisition/disposal | Date, mechanism, counterparty, consideration where known. |
| Source/evidence | Registry, filing, court record, contract, publication, other. |

## 4.8 Event and Timeline

Events anchor entities and relationships in time. Timeline analysis SHALL distinguish date-known, date-estimated, and date-unknown events. Correlation in time MUST NOT be described as causation without additional evidence.

- Examples: company creation, officer change, contract award, asset acquisition, licence issuance, court filing, ownership transfer, resignation, dissolution, loan, donation, or public appointment.

## 4.9 Value Flow

Value Flow represents a transfer, allocation, conversion, or transformation of economic value. It is broader than bank transfer and is the core of the CS-AML “follow the value” method.

| **Value-flow type** | **Example** |
|----|----|
| Payment | Buyer → supplier. |
| Contract allocation | Government/Donor → prime contractor. |
| Subcontract | Prime contractor → subcontractor. |
| Loan/debt | Lender → borrower; repayment in reverse direction. |
| Investment/equity | Investor → company / ownership interest. |
| Asset conversion | Cash/value → property, vehicle, shares, digital asset. |
| Donation/grant | Donor → recipient. |
| Sale/disposal | Asset → buyer, with consideration where known. |
| Non-cash benefit | Use, control, concession, preferential access, or other economic benefit. |

> **Critical rule**
>
> Where value, origin, destination, or mechanism is unknown, the field SHALL remain unknown. Investigators MUST NOT infer an exact financial transfer merely because related events occur near each other in time.

## 4.10 Indicator

An Indicator is an observed fact or pattern relevant to a financial-crime hypothesis. An indicator is not a finding of money laundering. Indicators SHOULD be atomic, testable, and linked to evidence.

- Example: multiple related companies share one address.

- Example: corporate officers change rapidly shortly before or after a major contract.

- Example: an asset is acquired by a related entity soon after a large value event.

- Example: a company has significant contracts but little observable operating footprint.

## 4.11 Typology

A Typology is a recognised pattern of conduct that may be associated with money laundering or related financial crime. Typology mapping SHALL be used as an analytical aid, not as proof of criminal conduct.

| **Typology** | **Illustrative indicators** |
|----|----|
| Nominee ownership | Formal owner differs from apparent controller; shared addresses, close associates, unusual control arrangements. |
| Shell-company layering | Multiple entities, thin operational footprint, repeated officer/address overlap, sequential transfers. |
| Asset conversion | Economic value appears converted into property, vehicles, shares, or digital assets. |
| Circular ownership/value | Ownership or value returns to an originating or related entity through a chain. |
| Professional intermediary | Lawyer, accountant, agent, nominee, company service provider, or other intermediary appears to structure control or transfer. |
| Trade-/contract-based laundering | Contracts, invoices, goods/services, procurement, pricing, or cross-border trade may be used to move or disguise value. |
| Mule/funnel pattern | Many sources converge to an intermediary entity then rapidly disperse or consolidate, where evidence exists. |

## 4.12 Hypothesis

A Hypothesis is a proposition that explains observed facts and is capable of being supported, weakened, rejected, or left inconclusive. Every significant case SHOULD maintain at least one legitimate alternative hypothesis.

| **Field**              | **Requirement**                                    |
|------------------------|----------------------------------------------------|
| Hypothesis ID          | Unique identifier.                                 |
| Statement              | Specific, neutral, falsifiable proposition.        |
| Supporting evidence    | Evidence that increases plausibility.              |
| Contradicting evidence | Evidence that decreases plausibility.              |
| Alternative hypotheses | Reasonable competing explanations.                 |
| Unknowns               | Facts needed to evaluate further.                  |
| Status                 | Open, supported, weakened, rejected, inconclusive. |
| Confidence             | Analyst confidence with rationale.                 |

## 4.13 Assessment

An Assessment is a reasoned analytical judgement derived from facts, indicators, tested hypotheses, and acknowledged gaps. It SHALL state confidence and MUST NOT overstate what the evidence establishes.

> **Example**
>
> “Available public-source information indicates that Company A and Company B are likely under common control. Confidence: moderate. This assessment is based on shared beneficial-ownership records, overlapping directors, and common addresses. Direct financial transactions and purchase consideration are not available and remain intelligence gaps.”

## 4.14 Intelligence Product

An Intelligence Product is the controlled output of the analytical process. Products MAY include Financial Intelligence Notes, Investigation Briefs, Entity Profiles, Asset Profiles, Network Analyses, Case Reports, and Referral Packages.

# 5. Analytical Standards

## 5.1 Fact, Inference, Hypothesis, Allegation

| **Class** | **Definition** | **Example** |
|----|----|----|
| Fact | Directly supported by identified evidence. | Company X lists Person A as director in an official filing. |
| Inference | Reasoned conclusion drawn from one or more facts. | Person A likely has management influence over Company X. |
| Hypothesis | Testable explanatory proposition. | Company X may act as a nominee structure for Person B. |
| Allegation | Claim that misconduct occurred. | Company X was used to launder proceeds. |

All analyst notes and products SHOULD use language that reflects the class of statement. Systems SHOULD provide visual labels or metadata to prevent accidental collapse of these categories.

## 5.2 Confidence Model

CS-AML v0.1 uses two separate axes: source reliability and information credibility. Organisations MAY map these to an existing intelligence rating scheme, provided both concepts remain distinct.

| **Source rating** | **Meaning**                    |
|-------------------|--------------------------------|
| A                 | Highly reliable                |
| B                 | Generally reliable             |
| C                 | Mixed reliability              |
| D                 | Generally unreliable           |
| E                 | Unreliable                     |
| F                 | Unknown / insufficient history |

| **Information rating** | **Meaning**                                     |
|------------------------|-------------------------------------------------|
| 1                      | Independently confirmed / directly corroborated |
| 2                      | Probably true                                   |
| 3                      | Possibly true                                   |
| 4                      | Doubtful                                        |
| 5                      | Improbable                                      |
| 6                      | Cannot be judged                                |

The combined code (for example A1, B2, F3) describes source and information separately. It SHALL NOT be used as a numeric probability unless the organisation has a documented calibration method.

## 5.3 Analytical Confidence Statements

| **Confidence** | **Use** |
|----|----|
| High | Multiple independent high-quality sources or direct authoritative evidence support the judgement; material contradictions are absent or explained. |
| Moderate | The judgement is supported by credible evidence but meaningful gaps, assumptions, or unresolved contradictions remain. |
| Low | Limited, indirect, or weakly corroborated information supports the judgement; alternative explanations remain substantial. |

## 5.4 Intelligence Gaps

Every material assessment SHALL identify the information that would most change the judgement. Typical gaps include direct transaction data, source of funds, beneficial ownership, asset purchase consideration, tax records, contractual performance, foreign corporate records, or identity confirmation.

## 5.5 Negative Evidence and Absence

Absence of public evidence SHALL NOT automatically be treated as evidence of absence. Statements such as “no operating activity” SHOULD be framed as “no operating activity was identified in the sources reviewed as of \[date\]” unless a stronger evidentiary basis exists.

# 6. Lawful Collection, Privacy, and Ethics

## 6.1 Collection Categories

| **Category** | **Examples** | **Default handling** |
|----|----|----|
| Public authoritative | Corporate registries, procurement portals, court decisions, official disclosures. | Collect and preserve; verify scope and currentness. |
| Public non-authoritative | Company sites, media, open social media, public directories. | Collect cautiously; corroborate material claims. |
| Permissioned/confidential | Voluntary disclosures, internal records, whistleblower material. | Collect only under appropriate authority, security, and source-protection procedures. |
| Restricted/sensitive | Personal financial data, criminal records, private communications. | Process only where lawful, necessary, and proportionate; apply enhanced access controls. |
| Unlawfully obtained/accessed | Hacked systems, stolen credentials, unauthorised interception. | MUST NOT be solicited or accessed through unlawful means; obtain legal advice for unsolicited material. |

## 6.2 Indonesian Personal Data Context

Under Indonesia’s Law No. 27 of 2022 on Personal Data Protection, personal financial data and criminal records are classified as specific personal data. A CS-AML implementation operating in Indonesia SHOULD therefore treat these classes as high-sensitivity by default and establish documented purpose, access, security, retention, and dissemination controls before processing them.

## 6.3 Collection Decision Test

``` text
1. Is the investigative purpose legitimate and documented?
```

``` text
2. Is the source access lawful or authorised?
```

``` text
3. Is the information relevant to the investigation question?
```

``` text
4. Is collection necessary and proportionate?
```

``` text
5. Is a less intrusive source sufficient?
```

``` text
6. Can the information be stored securely?
```

``` text
7. Is retention necessary?
```

``` text
8. Can it be disseminated, and to whom?
```

## 6.4 Prohibited Practices

- Unauthorised access to accounts or systems.

- Credential theft, password reuse, or use of stolen credentials.

- Impersonation or pretexting designed to obtain protected financial data without lawful authority.

- Illegal interception of communications.

- Purchase or solicitation of stolen credentials or clearly illicitly acquired personal datasets.

- Doxxing, harassment, intimidation, or unnecessary publication of private data.

- Automated accusations, blacklists, or adverse labels based solely on algorithmic scoring.

# 7. Follow-the-Value Method

## 7.1 Concept

Civil society commonly lacks lawful access to bank transaction records. CS-AML therefore broadens traditional “follow the money” into “follow the value”: trace how economic value is created, allocated, controlled, transferred, transformed, or enjoyed using open and lawfully obtained information.

## 7.2 Direct vs Reconstructed Trails

| **Trail** | **Definition** | **Typical civil-society use** |
|----|----|----|
| Direct financial trail | Evidence of an actual transfer between financial accounts or wallets. | Use only where records are lawfully available. |
| Reconstructed value trail | Inference from contracts, corporate relations, asset transfers, invoices, ownership changes, disclosures, court records, and chronology. | Primary method where direct transactions are unavailable. |

## 7.3 Reconstruction Rules

- Every edge in a value-flow map MUST identify whether it is observed, reported, inferred, or hypothetical.

- Contract value MUST NOT be assumed to equal profit, personal benefit, or money transferred to a related party.

- Asset acquisition near a contract award MAY be an indicator, but temporal proximity alone does not establish funding source.

- Ownership SHOULD be separated from control and use.

- Where value is estimated, the basis and range SHOULD be recorded.

## 7.4 Value-Flow Example

``` text
Government contract (known: Rp X)
```

``` text
          │
```

``` text
          ▼
```

``` text
      Company A
```

``` text
          │ subcontract (documented)
```

``` text
          ▼
```

``` text
      Company B
```

``` text
          │ asset acquisition (documented)
```

``` text
          ▼
```

``` text
       Property P
```

``` text
          │ controlled/used by (analytical relationship)
```

``` text
          ▼
```

``` text
       Person C
```

The example supports a sequence of economic relationships. It does not, by itself, establish that contract proceeds funded Property P or that Person C laundered money. The funding-source link remains a hypothesis unless evidence establishes it.

# 8. Graph and Network Analysis

## 8.1 Purpose

Graph analysis is used to reveal relationships that are difficult to identify in tabular records. It SHOULD enhance, not replace, evidence review.

## 8.2 Node and Edge Semantics

| **Graph component** | **Rule** |
|----|----|
| Node | Represents an entity, asset, event, contract, document, or other defined object. |
| Edge | Represents an explicit relationship or value flow; SHALL have provenance and confidence. |
| Derived edge | Computed by rule or algorithm; MUST be labelled as derived. |
| Hypothetical edge | Analytical proposition; MUST NOT visually appear equivalent to verified relationship. |
| Cross-case edge | SHOULD respect access restrictions and purpose limitations of each case. |

## 8.3 Permitted Analytical Techniques

- Shared-attribute analysis: address, officer, phone, domain, service provider, or other identifiers.

- Path analysis: identify how a subject connects to an asset, company, contract, or intermediary.

- Centrality and hub identification: prioritise structurally significant nodes for review.

- Community/cluster detection: identify dense groups for analyst inspection.

- Cycle detection: identify circular ownership or value relationships.

- Temporal graph analysis: identify changes in relationships over time.

Automated graph findings SHALL be treated as leads until supported by evidence and analyst review.

# 9. Typology Analysis

## 9.1 Typology Matching Model

``` text
Observed facts
```

``` text
    +
```

``` text
Indicators
```

``` text
    +
```

``` text
Relationship structure
```

``` text
    +
```

``` text
Timeline / value flow
```

``` text
        ↓
```

``` text
Typology comparison
```

``` text
        ↓
```

``` text
Possible match / partial match / no meaningful match
```

``` text
        ↓
```

``` text
Hypothesis testing
```

## 9.2 Typology Object Requirements

A configurable typology definition SHOULD contain: typology ID, name, description, relevant predicate context, expected indicators, disconfirming indicators, required evidence strength, jurisdiction notes, references, version, and review date.

## 9.3 Avoiding Typology Overreach

- A typology match SHALL NOT automatically raise an allegation.

- Common business practices that resemble indicators MUST be assessed in context.

- Analysts SHOULD document benign explanations for each material typology match.

- Typology libraries SHOULD be periodically reviewed against authoritative sources such as FATF, FIU publications, court decisions, and reputable research.

# 10. Review, Escalation, and Dissemination

## 10.1 Escalation States

| **State** | **Meaning** | **Default action** |
|----|----|----|
| Information only | Insufficient analytical significance. | Archive or monitor. |
| Analytical lead | Potentially relevant pattern requiring more collection. | Continue targeted research. |
| Active investigation | Defined hypothesis and evidence plan. | Collect, test, review. |
| Reasonable indicators | Multiple supported indicators warrant independent review. | Peer review and risk/legal assessment. |
| Actionable intelligence | Structured package can support a legitimate external decision or further investigation. | Refer, brief, or publish under controlled process. |

## 10.2 Dissemination Paths

- Internal: programme leadership, legal, security, or governance review.

- Regulatory/FIU referral: structured factual package, where lawful and appropriate.

- Law enforcement or anti-corruption body: where the matter falls within jurisdiction and safety risks are managed.

- Investigative publication: fact-checked, legally reviewed where appropriate, and privacy-minimised.

- Partner CSO/journalist: only under clear handling and source-protection terms.

## 10.3 Minimum Referral Package

| **Section** | **Minimum content** |
|----|----|
| Executive assessment | What the available evidence indicates, confidence, and key caveats. |
| Investigation question | What was examined and why. |
| Subjects/entities | Stable IDs, names/aliases, roles, identifiers. |
| Chronology | Material events and dates. |
| Relationship/asset graph | Sourced relationships only; inferred links clearly marked. |
| Value-flow analysis | Observed and reconstructed value relationships. |
| Typology indicators | Relevant indicators and benign alternatives. |
| Evidence index | Source, archive/reference, date, hash where applicable. |
| Intelligence gaps | What remains unknown. |
| Handling notes | Sensitivity, source protection, dissemination restrictions. |

# 11. Governance and Roles

## 11.1 Minimum Roles

| **Role** | **Responsibilities** |
|----|----|
| Case owner / analyst | Scoping, collection, analysis, documentation. |
| Peer reviewer | Challenge hypotheses, evidence quality, confidence, and wording. |
| Information-security custodian | Access control, secure storage, incident response, backups. |
| Legal/privacy reviewer | Required for high-risk collection, restricted data, or sensitive publication where available. |
| Editorial/management approver | Approves external dissemination under organisational policy. |

## 11.2 Separation of Duties

High-impact external products SHOULD NOT be approved solely by the analyst who produced them. Sensitive referrals or publications SHOULD receive at least one independent analytical review and, where appropriate, legal/privacy review.

## 11.3 Case Risk Assessment

Each case SHOULD assess at least: source risk, subject risk, legal risk, privacy risk, physical safety risk, digital-security risk, retaliation risk, reputational risk, and harm-to-bystanders risk. Controls SHALL be proportionate to these risks.

# 12. Security, Auditability, and Data Governance

## 12.1 Access Control

- Least-privilege access SHALL apply to case data.

- Highly sensitive source identities SHOULD be compartmentalised from general case material.

- Administrative access SHOULD be logged and reviewed.

- Export and bulk-download capability SHOULD be restricted for sensitive datasets.

## 12.2 Audit Trail

A conformant digital implementation SHALL log material changes to evidence metadata, entity merges/splits, relationship assertions, hypothesis status, assessments, exports, and external dissemination decisions.

## 12.3 Integrity and Preservation

- Original evidence SHOULD be immutable or write-protected after preservation where feasible.

- Hashes SHOULD be used for material digital files.

- Analyst annotations SHOULD be stored separately from original files.

- Deletion and correction SHOULD preserve sufficient audit metadata to explain what changed and why, subject to lawful privacy/retention obligations.

## 12.4 Retention

Organisations SHALL establish retention schedules based on purpose, legal requirements, sensitivity, source agreements, and risk. “Keep everything forever” is not conformant with the data-minimisation principle.

# 13. Technology Capability Model

CS-AML v0.1 is technology-neutral, but the following capability model supports a scalable implementation.

| **Capability** | **Purpose** |
|----|----|
| Investigation management | Case intake, scope, status, assignments, risks, tasks. |
| Source management | Source registry, reliability, access status, archiving. |
| Evidence management | Preservation, hashes, excerpts, verification, chain of provenance. |
| Entity resolution | Record linkage, aliases, merge/split review, match confidence. |
| Knowledge graph | Entity and relationship storage with provenance. |
| Asset tracing | Legal/beneficial ownership, control, use, valuation, transfers. |
| Timeline analysis | Events, date uncertainty, temporal comparison. |
| Value-flow analysis | Observed/inferred value relationships and transformations. |
| Typology engine | Configurable indicators and typology comparisons. |
| Hypothesis management | Supporting/contradicting evidence, alternatives, status. |
| Assessment workspace | Judgements, confidence, intelligence gaps. |
| Intelligence reporting | Reusable structured products and referral packages. |
| Audit/security | Access control, logs, sensitivity, retention, export controls. |
| Cross-case correlation | Controlled discovery of recurring entities/relationships across cases. |

## 13.1 Conceptual Architecture

``` text
CASE / WORKSPACE
```

``` text
      │
```

``` text
      ├── SOURCE REGISTRY ── ARCHIVE
```

``` text
      ├── EVIDENCE STORE ── HASH / PROVENANCE
```

``` text
      │
```

``` text
      ▼
```

``` text
ENTITY RESOLUTION
```

``` text
      │
```

``` text
      ▼
```

``` text
KNOWLEDGE GRAPH
```

``` text
      ├── PERSON / ORGANISATION
```

``` text
      ├── ASSET / CONTRACT / EVENT
```

``` text
      └── RELATIONSHIP / VALUE FLOW
```

``` text
      │
```

``` text
      ├── TIMELINE ANALYSIS
```

``` text
      ├── GRAPH ANALYTICS
```

``` text
      └── TYPOLOGY MATCHING
```

``` text
              │
```

``` text
              ▼
```

``` text
      HYPOTHESIS WORKSPACE
```

``` text
              │
```

``` text
              ▼
```

``` text
      ANALYST ASSESSMENT
```

``` text
              │
```

``` text
              ▼
```

``` text
      INTELLIGENCE PRODUCT
```

``` text
              │
```

``` text
      REVIEW / REFERRAL / PUBLICATION
```

## 13.2 Critical Architectural Rules

- Entity and Evidence SHOULD be reusable truth objects; Case is contextual access and analytical workspace.

- Evidence MUST NOT be silently overwritten by analyst interpretation.

- Derived and hypothetical relationships MUST be visually and semantically distinct from verified relationships.

- Every analytical object SHOULD expose source provenance to the analyst.

- Automation SHOULD be explainable enough for analysts to understand why a match, score, or relationship was proposed.

# 14. Quality Assurance and Metrics

## 14.1 QA Checklist

- Investigation question remains neutral and answerable.

- All material facts link to evidence.

- Entity merges have documented match rationale.

- Relationship edges have provenance and confidence.

- Value-flow links distinguish observed from inferred.

- Alternative hypotheses are documented.

- Contradicting evidence is not omitted.

- Confidence is consistent with evidence quality and gaps.

- Sensitive personal data is necessary and access-controlled.

- External products received required review.

## 14.2 Suggested Metrics

| **Metric** | **Purpose** |
|----|----|
| Evidence provenance completeness | Percentage of material assertions with source/evidence links. |
| Entity-resolution reversal rate | Quality signal for over-merging or weak matching. |
| Hypothesis challenge rate | Whether analysts record contradicting evidence and alternatives. |
| Referral usefulness | Qualitative feedback from recipients where available. |
| Correction rate | Number/severity of post-publication or post-referral corrections. |
| Sensitive-data exposure incidents | Security/privacy effectiveness. |
| Time to analytical decision | Operational efficiency, not a quality substitute. |
| Cross-case discovery yield | Value of controlled correlation capability. |

Alert volume, graph size, number of entities, and number of allegations are NOT quality metrics and SHOULD NOT be used as performance targets.

# 15. Intelligence Product Standard

## 15.1 Required Structure

1.  Executive Assessment

2.  Investigation Question

3.  Purpose and Scope

4.  Method and Source Limitations

5.  Key Entities

6.  Key Findings

7.  Relationship Analysis

8.  Asset Analysis

9.  Timeline

10. Value-Flow Analysis

11. Relevant Indicators and Typologies

12. Hypothesis Evaluation

13. Alternative Explanations

14. Intelligence Gaps

15. Confidence Assessment

16. Evidence Index

17. Recommended Next Steps

18. Handling / Dissemination Restrictions

## 15.2 Writing Standard

- Use neutral language and attribution.

- Prefer “records indicate”, “available information suggests”, or “we assess with moderate confidence” over categorical claims where evidence is incomplete.

- Avoid labels such as “money launderer”, “criminal”, or “shell company” as definitive descriptions unless supported by authoritative adjudication or clearly attributed allegation.

- State limitations close to the judgement they qualify, not only in a disclaimer at the end.

# 16. Implementation Roadmap for v0.1

## 16.1 Phase A – Method First

- Adopt case, source, evidence, entity, relationship, hypothesis, and assessment templates.

- Train analysts on fact/inference distinction, source reliability, hypothesis testing, and privacy.

- Establish peer-review and escalation procedure.

## 16.2 Phase B – Structured Data

- Move entity, relationship, asset, event, and value-flow records into structured storage.

- Introduce stable IDs, controlled vocabularies, confidence, and provenance.

- Implement cross-case duplicate detection under access controls.

## 16.3 Phase C – Graph and Automation

- Add graph visualisation and path/cluster/cycle analysis.

- Add assisted entity resolution with human approval.

- Add configurable typology rules and structured analyst feedback.

- Maintain explainability and never convert automation into automatic allegation.

# 17. Explicit Non-Goals of v0.1

- Replacing bank AML transaction-monitoring systems.

- Submitting statutory STR/SAR reports on behalf of regulated entities unless separately authorised by law.

- Performing covert surveillance or unauthorised account access.

- Creating public “risk scores” or guilt rankings of individuals.

- Automating criminal accusations.

- Building a general-purpose personal-data warehouse.

- Replacing FIU, regulator, prosecutor, police, court, or judicial functions.

# 18. Reference Alignment

CS-AML v0.1 is an independent civil-society framework. It is informed by, but does not claim formal compliance certification against, the following sources:

| **Reference** | **Relevance** | **URL** |
|----|----|----|
| FATF Recommendations | Risk-based approach, beneficial ownership, financial intelligence, NPO safeguards. | https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Fatf-recommendations.html |
| FATF NPO guidance / Recommendation 8 | Focused, proportionate, risk-based measures and protection of legitimate NPO activity. | https://www.fatf-gafi.org/en/topics/non-profit-organisations.html |
| UNODC Civil Society Guide to UNCAC | Civil society role in asset tracing, open-source and financial investigation, forensic audit, legal analysis. Pending verification — page-level support not confirmed. | https://www.unodc.org/documents/NGO/Corruption/251113-CSU-UNCAC_Guide-Web.pdf *[v0.1.1 · A13]* |
| UNODC Confiscation / asset tracing manual | Public records, internet sources, financial records, and evidence-access considerations in asset tracing. | https://www.unodc.org/documents/organized-crime/Publications/Confiscation_Manual_Ebook_E.pdf |
| PPATK – Klinik Dumas NGO/CSO | Recognition of NGO/CSO and public information as useful inputs for early detection and financial-intelligence analysis. | https://www.ppatk.go.id/news/read/1570/klinik-dumas-special-edition-ppatk-dan-ngocso-perkuat-aduan-tppu-melalui-peluncuran-laporppatkgoid.html |
| Indonesia Law No. 27/2022 on Personal Data Protection | Personal financial data and criminal records are specific personal data. | https://peraturan.bpk.go.id/Details/229798/uu-no-27-tahun-2022 |

# Annex A – Minimum Case Record

``` text
Case ID:
```

``` text
Title:
```

``` text
Investigation question:
```

``` text
Public-interest purpose:
```

``` text
Predicate issue (if any):
```

``` text
Subjects:
```

``` text
Time period:
```

``` text
Jurisdiction(s):
```

``` text
Scope exclusions:
```

``` text
Case risk:
```

``` text
Case owner:
```

``` text
Peer reviewer:
```

``` text
Status:
```

``` text
Retention class:
```

``` text
Dissemination restriction:
```

# Annex B – Minimum Evidence Record

``` text
Evidence ID:
```

``` text
Source ID:
```

``` text
Title/description:
```

``` text
Original location:
```

``` text
Access date/time:
```

``` text
Publication date/time:
```

``` text
Archived copy:
```

``` text
SHA-256 (if file):
```

``` text
Extract / proposition supported:
```

``` text
Verification status:
```

``` text
Sensitivity:
```

``` text
Analyst:
```

``` text
Notes / limitations:
```

# Annex C – Hypothesis Worksheet

``` text
Hypothesis ID:
```

``` text
Statement:
```

``` text
Why it matters:
```

``` text
Supporting evidence:
```

``` text
Contradicting evidence:
```

``` text
Alternative hypotheses:
```

``` text
Unknowns / intelligence gaps:
```

``` text
Next collection actions:
```

``` text
Status: OPEN / SUPPORTED / WEAKENED / REJECTED / INCONCLUSIVE
```

``` text
Confidence: LOW / MODERATE / HIGH
```

``` text
Analyst rationale:
```

``` text
Reviewer comments:
```

# Annex D – Pre-Dissemination Review

- [ ] Every material factual claim is sourced.

- [ ] Inference and allegation are clearly distinguished.

- [ ] Contradicting evidence and alternatives are represented fairly.

- [ ] Sensitive personal data is necessary and minimised.

- [ ] Source identity and whistleblower risk are addressed.

- [ ] Graph visuals distinguish verified, derived, and hypothetical edges.

- [ ] Confidence and intelligence gaps are explicit.

- [ ] The intended recipient has a legitimate need for the information.

- [ ] Required peer, legal/privacy, editorial, and security reviews are complete.

- [ ] The dissemination decision and version are logged.

# Annex E – v0.1 Design Axioms

| **\#** | **Axiom** |
|----|----|
| Axiom 1 | Evidence is not an allegation. |
| Axiom 2 | Case is context; Entity and Evidence are reusable truth objects. |
| Axiom 3 | Every material relationship has provenance. |
| Axiom 4 | Unknown is a valid value and is preferable to invented precision. |
| Axiom 5 | Graph structure generates leads, not guilt. |
| Axiom 6 | Typology similarity is an indicator, not proof. |
| Axiom 7 | Analytical confidence must reflect both evidence quality and intelligence gaps. |
| Axiom 8 | Civil society follows value lawfully; it does not imitate coercive state powers. |
| Axiom 9 | Sensitive data requires proportional protection. |
| Axiom 10 | A strong intelligence product makes uncertainty visible. |
