**Civil Society Anti-Money Laundering & Financial Intelligence Framework**

*Expanded Normative Specification*

A governance, investigation, evidence, intelligence, technology, and assurance standard for civil society financial intelligence.

> **Document status — v0.1.1**
> Version: 0.1.1 — Draft for Review (Proposed Internal Baseline). *[v0.1.1 · A01]*
> Supersedes: CS-AML Framework v0.1 Expanded. The DOCX/PDF files in this repository are the unchanged v0.1 baseline (legacy); this Markdown file is the canonical source.
> Validation: not validated. No recorded approval decision, implementation test result, or independent audit exists for this baseline. Acceptance criteria in this document are targets, not evidence that tests have passed.
> CS-AML is not an external standard or certification. References to FATF, Wolfsberg, PPATK, UNODC or other bodies do not imply their endorsement.
> Changes in 0.1.1: see `CHANGELOG.md` at the repository root (audit findings A01–A16).

| **Status** | Draft for Review (Proposed Internal Baseline) *[v0.1.1 · A01]* |
|----|----|
| **Version** | 0.1.1 Expanded *[v0.1.1 · A01]* |
| **Date** | October 2026 |
| **Primary audience** | Civil society, investigative journalism, public-interest research |
| **Normative terms** | MUST / SHALL / SHOULD / MAY |
| **Core chain** | SOURCE → EVIDENCE → FACT → INDICATOR → HYPOTHESIS → ASSESSMENT → INTELLIGENCE PRODUCT |

**Design axiom**

Evidence is not an allegation. Case is context; Entity and Evidence are reusable truth objects. Every material conclusion must remain traceable to provenance.

# Contents

0\. Document Control

1\. Purpose, Scope, and Boundaries

2\. Foundational Principles

3\. Conformance Model

4\. Governance and Operating Model

5\. Investigation Lifecycle and Control Gates

6\. Case Model and Case Taxonomy

7\. Source Management Standard

8\. Evidence and Provenance Standard

9\. Fact, Claim, and Proposition Model

10\. Entity Resolution and Identity Standard

11\. Relationship, Ownership, and Control Model

12\. Asset and Wealth Analysis

13\. Event and Timeline Analysis

14\. Value Flow and Follow-the-Value Model

15\. Indicator and Typology Framework

16\. Hypothesis Management and Structured Analytic Techniques

17\. Analytical Confidence and Intelligence Gaps

18\. Risk Model for Civil Society Investigations

19\. Lawful Collection, Privacy, and Data Protection

20\. Review, Challenge, and Quality Assurance

21\. Intelligence Product Standard

22\. Dissemination, Sharing, and Referral

23\. Technology Architecture Requirements

24\. Security and Operational Protection

25\. Auditability, Logging, and Reproducibility

26\. Metrics and Effectiveness

27\. Assurance and Control Testing

28\. Maturity Model

29\. Control Catalogue

30\. Canonical Data Model

31\. Reference Operating Procedure

32\. Implementation Roadmap for a CSO

33\. Annex A — Case Charter Template

34\. Annex B — Source and Evidence Register Template

35\. Annex C — Hypothesis Matrix Template

36\. Annex D — Intelligence Product Template

37\. Annex E — Dissemination Review Checklist

38\. Annex F — Typology Record Template

39\. Annex G — Glossary of Core Terms

40\. Annex H — External Standards Mapping

41\. Annex I — Minimum Conformance Evidence Pack

42\. Annex J — Normative and Informative References

# 0. Document Control

**Document title:** CS-AML Framework v0.1.1 — Civil Society Anti-Money Laundering & Financial Intelligence Framework

**Status:** Draft for Review (Proposed Internal Baseline) *[v0.1.1 · A01]*

**Version:** 0.1.1 Expanded *[v0.1.1 · A01]*

**Publication date:** October 2026

**Primary audience:** civil society organisations, investigative journalists, public-interest researchers, anti-corruption organisations, humanitarian and human-rights organisations, digital-rights organisations, research institutions, and trusted technical partners.

**Primary use:** lawful, evidence-based financial intelligence and AML-related investigation performed outside regulated financial institutions and without coercive state powers.

## 0.1 Normative language

The keywords **MUST**, **MUST NOT**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **MAY**, and **OPTIONAL** are to be interpreted as normative requirements. MUST/SHALL indicate mandatory requirements for conformance. SHOULD indicates a recommended control whose omission requires documented justification. MAY indicates an optional capability.

## 0.2 Framework intent

CS-AML does not create law-enforcement powers, banking privileges, suspicious transaction reporting obligations, or authority to compel disclosure. It establishes a disciplined method for converting lawfully obtained information into structured financial intelligence that can support internal decisions, public-interest reporting, advocacy, referrals, or further investigation by competent authorities.

## 0.3 Design axiom

The framework is built on one core analytical chain:

``` text
SOURCE → EVIDENCE → FACT → INDICATOR → HYPOTHESIS → ASSESSMENT → INTELLIGENCE PRODUCT
```

No stage may be silently skipped when a material allegation or escalation decision depends on the result.

# 1. Purpose, Scope, and Boundaries

## 1.1 Purpose

The purpose of CS-AML is to provide a repeatable and auditable framework for civil society financial intelligence. It is intended to help organisations identify, organise, analyse, test, communicate, and safely retain information about potentially suspicious economic relationships, ownership structures, assets, contracts, transfers of value, and financial-crime indicators.

The framework has five objectives:

**1.** establish a common vocabulary and domain model;

**2.** create minimum standards for lawful collection, provenance, evidence, and analytical reasoning;

**3.** define a lifecycle from case initiation through dissemination and closure;

**4.** create controls that protect individuals, sources, analysts, and legitimate civil-society activity; and

**5.** make outputs sufficiently structured that they can be reviewed, reproduced, challenged, and—where appropriate—referred to competent authorities.

## 1.2 In scope

CS-AML covers public-source and lawfully obtained investigations involving, among other things: corruption proceeds, fraud proceeds, procurement abuse, environmental crime, illicit trade, sanctions-evasion indicators, abuse of legal persons, nominee ownership, shell-company structures, hidden beneficial ownership, asset concealment, unexplained economic relationships, suspicious value transfers, and possible laundering typologies.

## 1.3 Out of scope

CS-AML does not authorise or standardise:

- unauthorised access to bank systems, private communications, or protected databases;

- credential theft, pretexting, impersonation, covert interception, or hacking;

- purchase or trafficking of stolen personal data;

- automated accusation, criminal attribution, or guilt scoring;

- publication of sensitive personal data merely because it is technically obtainable;

- replacement of legal advice, prosecutorial judgment, FIU analysis, or regulated-entity AML obligations.

## 1.4 Relationship to formal AML regimes

CS-AML is complementary to—not a substitute for—formal AML/CFT systems. FATF standards are directed primarily at states, competent authorities, financial institutions, and designated non-financial businesses and professions. Civil society occupies a different position: it can identify public-interest risks, trace assets using lawful sources, expose relationships, support victims, contribute information to authorities, and improve accountability. PPATK has publicly recognised the value of information from NGO/CSO and the public in supporting early detection and financial-intelligence analysis. UNODC likewise recognises civil-society contributions to asset tracing through open-source investigation, financial investigation, forensic auditing, and legal analysis (Annex J, reference 4 — pending verification — page-level support not confirmed). *[v0.1.1 · A13]*

## 1.5 Risk-based proportionality

Controls implemented under CS-AML SHALL be proportionate to the sensitivity, potential harm, legal exposure, and public-interest value of the investigation. The framework rejects both extremes: uncontrolled collection and publication on one side, and risk-avoidance so broad that legitimate accountability work becomes impossible on the other.

# 2. Foundational Principles

## 2.1 Evidence before allegation

An investigation SHALL begin with a question, anomaly, event, or documented concern—not with a predetermined conclusion that a person has committed money laundering. Evidence and analysis must precede allegation.

## 2.2 Follow the value

Civil society often lacks lawful access to banking transaction data. CS-AML therefore uses **follow-the-value** as the broader analytical concept. Analysts may trace money, assets, ownership, contractual rights, debt, corporate control, procurement awards, property, beneficial interests, grants, donations, crypto-assets, and other economically meaningful value transformations.

## 2.3 Lawful collection

Every source item SHALL have a collection basis and provenance record. A source being visible on the internet does not automatically make unlimited processing, redistribution, or publication lawful or ethical.

## 2.4 Separation of analytical states

The framework SHALL distinguish:

- **Source:** where information came from;

- **Evidence:** a preserved item or extract supporting a proposition;

- **Fact:** a proposition sufficiently established for the current analytical purpose;

- **Indicator:** a fact or pattern relevant to a risk or typology;

- **Hypothesis:** a testable explanation;

- **Assessment:** an analytical judgement with confidence and caveats;

- **Allegation:** an assertion that may have legal or reputational consequences.

## 2.5 Competing hypotheses

Material assessments SHOULD include at least one plausible non-criminal alternative explanation unless the evidence makes alternatives objectively unreasonable. Analysts SHALL actively search for disconfirming information.

## 2.6 Provenance by default

Every material entity, relationship, event, value flow, and indicator SHALL be traceable to evidence. “Analyst knows” is not a valid provenance category.

## 2.7 Unknown is valid

Unknown, unavailable, not verified, and disputed are valid values. They are preferable to invented precision. Systems SHALL NOT force analysts to fill unknown fields with guesses.

## 2.8 Graphs generate leads, not guilt

A network relationship may establish proximity, shared infrastructure, common ownership, timing, or control indicators. It does not by itself establish criminality.

## 2.9 Typology match is not proof

A pattern resembling layering, nominee ownership, shell-company use, asset conversion, funnel-account behaviour, or another typology SHALL be treated as an indicator requiring context and corroboration.

## 2.10 Necessity and minimisation

Personal data SHALL be collected, processed, retained, and disseminated only where necessary and proportionate to the investigation purpose.

## 2.11 Right to challenge analysis

Where practicable and consistent with source protection and investigative integrity, high-impact findings SHOULD be subjected to peer review, legal review, and factual challenge before external dissemination.

## 2.12 Protection of legitimate civil society

AML concepts SHALL NOT be used to stigmatise nonprofit organisations merely because they operate internationally, work in conflict areas, receive foreign funding, or serve vulnerable communities. FATF Recommendation 8 now emphasises targeted and proportionate measures and avoidance of unintended suppression of legitimate NPO activity.

# 3. Conformance Model

## 3.1 Conformance statement

An organisation may describe itself as **CS-AML v0.1.1 Aligned** only if it can demonstrate the mandatory requirements in this section and the applicable control objectives in Sections 4–20. Alignment is a self-assessed claim against this draft framework; it is not an external certification, and no organisation has yet been assessed against v0.1.1. *[v0.1.1 · A01]*

## 3.2 Minimum mandatory controls

At minimum, an aligned implementation SHALL have:

**1.** documented case initiation and scope;

**2.** source registration and provenance;

**3.** evidence preservation and integrity controls;

**4.** explicit separation of fact, indicator, hypothesis, and assessment;

**5.** entity and relationship records with confidence and evidence links;

**6.** lawful collection and data-protection review for sensitive data;

**7.** peer review for high-impact conclusions;

**8.** an intelligence-gap register;

**9.** dissemination classification and approval;

**10.** audit logging sufficient to reconstruct material analytical actions.

## 3.3 Conformance levels

**Level 1 — Foundation.** Manual or semi-manual workflow, basic case/source/evidence registers, minimum review controls.

**Level 2 — Operational.** Structured entity/relationship model, formal hypothesis testing, sensitivity classification, quality assurance, defined escalation paths.

**Level 3 — Integrated.** Knowledge graph, reusable entities, automated provenance support, controlled connectors, role-based access, metrics, and cross-case analysis.

**Level 4 — Assured.** Independent assurance, control testing, model validation where analytics are automated, mature threat modelling, formal retention schedules, and evidence of continuous improvement.

## 3.4 Exceptions

A mandatory requirement MAY be temporarily excepted only when: the reason is documented; a responsible approver is identified; compensating controls are recorded; the exception has an expiry date; and the exception does not authorise illegal collection or unsafe publication.

No exception MAY cover the non-waivable invariants: unauthorized access or authorization bypass; source identity exposure; evidence corruption or loss of provenance/integrity for material records; certainty promotion (for example a reconstructed or hypothetical flow presented as direct, insufficient basis presented as a confidence level, or a claim treated as fact without a verification decision); approval bypass, including export without approval; and broken, missing, or editable audit history. Where such a condition exists, the only permitted path is to disable the affected capability with tested evidence that it cannot be reached. *[v0.1.1 · A16]*

# 4. Governance and Operating Model

## 4.1 Governance objective

The governance objective is to ensure that investigative independence is balanced by accountability, source protection, privacy, legal compliance, and quality control.

## 4.2 Roles

A mature CS-AML programme SHOULD define at least the following roles, which may be combined in small organisations if conflicts are managed:

- **Case Owner:** accountable for purpose, scope, priorities, and closure;

- **Lead Analyst:** responsible for analytical plan and assessment;

- **Collector/Researcher:** acquires and registers information;

- **Evidence Custodian:** maintains integrity, preservation, and chain of custody where required;

- **Peer Reviewer:** challenges reasoning and checks provenance;

- **Legal/Data Protection Reviewer:** reviews legality, privacy, defamation, publication, and sensitive-source issues;

- **Security Owner:** protects systems, credentials, source identities, and operational security;

- **Approving Authority:** authorises high-impact dissemination or referral.

## 4.3 Three-function model

For higher-risk programmes, organisations SHOULD separate:

- **Investigation function** — collection and analysis;

- **Control function** — privacy, legal, security, methodology, and QA;

- **Independent assurance function** — periodic testing of whether the framework is followed and effective.

This adapts—but does not mechanically copy—the separation of operational, oversight, and assurance functions used in regulated environments.

## 4.4 Conflict management

Potential conflicts of interest SHALL be declared. An analyst with a personal, financial, political, organisational, or adversarial conflict that could materially affect judgement SHALL be recused or subject to enhanced review.

## 4.5 Decision rights

Organisations SHALL document who may: open a high-risk case; ingest restricted data; merge identities; designate a hypothesis as supported; approve external referrals; approve publication; unmask protected source identities; and destroy or archive evidence.

## 4.6 Case risk committee

High-impact organisations SHOULD maintain a periodic case-risk forum to review cases involving serious reputational harm, vulnerable persons, cross-border legal risk, whistleblower exposure, covert-source risk, sanctions issues, or highly sensitive financial/personal data.

# 5. Investigation Lifecycle and Control Gates

## 5.1 Lifecycle

The standard lifecycle is:

``` text
INTAKE → TRIAGE → SCOPE → COLLECTION PLAN → COLLECTION → STRUCTURE → ANALYSIS → HYPOTHESIS TEST → ASSESSMENT → REVIEW → DISSEMINATION → CLOSURE / MONITORING
```

## 5.2 Gate G0 — Intake legitimacy

Before opening a case, the organisation SHALL record the trigger, public-interest rationale, known sensitivities, and any immediate legal/security constraints. Anonymous tips MAY initiate triage but SHALL NOT be treated as verified evidence merely because they are detailed.

## 5.3 Gate G1 — Scope approval

A case SHALL have a written investigation question, subject boundary, time period, jurisdictions, expected data classes, and an initial harm assessment. Scope creep SHALL be documented.

## 5.4 Gate G2 — Collection approval

Before collecting sensitive or restricted data, the team SHALL identify the legal/lawful basis, collection method, necessity, expected retention, access restrictions, and whether consent, legal advice, or additional safeguards are required.

## 5.5 Gate G3 — Analytical readiness

A case SHOULD not proceed to material assessment until core entities are resolved sufficiently, major source conflicts are identified, evidence is linked, and known data gaps are recorded.

## 5.6 Gate G4 — Assessment quality

Before a material judgement is finalised, the team SHALL document supporting evidence, contradictory evidence, alternative hypotheses, confidence, intelligence gaps, and any assumptions.

## 5.7 Gate G5 — Dissemination

External referral, publication, or partner sharing SHALL be approved according to sensitivity. The package SHALL specify what is fact, what is assessment, what remains unknown, and what handling restrictions apply.

## 5.8 Gate G6 — Closure and learning

Closure SHALL record outcome, unresolved gaps, retention status, lessons learned, reusable typology insights, and whether ongoing monitoring is justified. Cases SHALL NOT remain open indefinitely without a documented reason.

# 6. Case Model and Case Taxonomy

## 6.1 Case definition

A **Case** is a bounded analytical context containing questions, tasks, subjects, evidence references, hypotheses, assessments, risks, decisions, and dissemination records. A case is not the authoritative identity store for entities.

## 6.2 Case classes

Organisations MAY classify cases as:

- **Lead:** preliminary information requiring validation;

- **Inquiry:** bounded research to answer a specific question;

- **Investigation:** structured multi-source analytical effort;

- **Network Investigation:** cross-entity or cross-case investigation focused on a connected system;

- **Asset Tracing Case:** investigation primarily focused on locating, attributing, or explaining assets/value;

- **Referral Support Case:** preparation of information for a competent authority or partner;

- **Monitoring Case:** continuing observation of a known risk pattern or network.

## 6.3 Case fields

Minimum fields SHALL include case identifier, title, purpose, investigation question, owner, status, sensitivity, jurisdictions, start date, scope, legal/privacy notes, subjects, linked hypotheses, key gaps, dissemination status, and closure decision.

## 6.4 Case sensitivity

Cases and their content SHALL be classified using the five-level model defined authoritatively in the CS-AML Data Model Specification v0.1.1, Section 16 (`CS-AML_Data_Model_Specification_v0.1.1.md`). Levels, ordered least to most restrictive (wire value — display label): *[v0.1.1 · A08]*

- **PUBLIC — Public:** suitable for public release after normal review;

- **INTERNAL — Internal:** routine internal operational information;

- **SENSITIVE — Sensitive:** could create privacy, reputational, safety, or investigative harm if disclosed;

- **RESTRICTED — Restricted:** high-risk information requiring named-role or case-specific authorization;

- **SOURCE_PROTECTED — Source-protected:** information whose disclosure could identify or endanger a confidential source.

Access labels (purpose, jurisdiction, embargo, legal-review, compartment, and similar) are additive restrictions; the most restrictive applicable level and all applicable labels apply. Derived objects and exports inherit the highest classification of their inputs unless a recorded reviewer downgrade decision exists. Unknown or missing classification SHALL fail closed (access denied; object flagged for classification). *[v0.1.1 · A08]*

**Legacy mapping note.** v0.1 of this framework suggested four levels (Public, Internal, Restricted, Highly Restricted). These map as follows and the last two SHALL NOT be mapped automatically: Public → PUBLIC; Internal → INTERNAL; Restricted → SENSITIVE or RESTRICTED as chosen by the data owner during migration (RESTRICTED until decided); Highly Restricted → SOURCE_PROTECTED only where the reason is source-identifying information, otherwise RESTRICTED plus the relevant access label (e.g. legal-privilege, physical-security). See the Data Model Specification, Section 16. *[v0.1.1 · A08]*

Access SHALL follow least privilege.

# 7. Source Management Standard

## 7.1 Source definition

A **Source** is the origin from which information is obtained. Sources include official registries, court records, procurement systems, corporate filings, public websites, journalism, academic records, social media, satellite imagery, archival records, interviews, whistleblowers, partner organisations, and documents received lawfully.

## 7.2 Source classes

Sources SHOULD be tagged as **official**, **first-party**, **professional secondary**, **open social**, **human source**, **partner-provided**, **restricted**, or **unknown provenance**. The class does not determine truth; it informs evaluation.

## 7.3 Mandatory source metadata

Each source SHALL record, where applicable: source ID, title/description, publisher/origin, URL or location, publication date, access date/time, collector, access method, licence/terms constraints, legal sensitivity, archive location, checksum for preserved files, and reliability assessment.

## 7.4 Reliability scale

CS-AML recommends the following source reliability scale:

- **A — Highly reliable:** strong institutional or technical basis; consistent record;

- **B — Generally reliable:** usually dependable with known limitations;

- **C — Mixed:** reliability varies or cannot be generalised;

- **D — Generally unreliable:** repeated issues or strong incentives to mislead;

- **E — Unreliable:** demonstrably unreliable;

- **F — Unknown:** insufficient basis to assess.

Reliability SHALL NOT substitute for evaluating the specific information.

## 7.5 Acquisition record

For material sources, the organisation SHOULD preserve enough acquisition context to show how the item was obtained. Screenshots without URL, timestamp, or context SHOULD be avoided where a more robust capture is possible.

## 7.6 Source protection

Human-source identity SHALL be separated from analytical content when exposure would create meaningful risk. Pseudonymous source IDs SHOULD be used in analyst-facing products unless identity is necessary.

# 8. Evidence and Provenance Standard

## 8.1 Evidence definition

**Evidence** is a preserved item, observation, or extract that supports or contradicts a proposition. Evidence in CS-AML may be evidentiary for analytical purposes without satisfying a court's admissibility rules.

## 8.2 Evidence principles

Evidence SHALL be attributable, preserved, contextualised, and linked to propositions. Analysts SHALL distinguish originals, copies, extracts, translations, transcriptions, derived datasets, and analyst-created visualisations.

## 8.3 Integrity

Downloaded files and critical digital evidence SHOULD be hashed using SHA-256 or an equivalent contemporary integrity mechanism. The evidence register SHOULD record the original filename, size, hash, acquisition timestamp, source, and storage location.

## 8.4 Chain of custody

A formal chain of custody SHOULD be used when material may be referred for legal proceedings, when authenticity may be challenged, or when evidence passes across organisations. At minimum record acquisition, transfer, access, transformation, and disposition events.

## 8.5 Derivative evidence

Translations, OCR outputs, entity-extraction outputs, AI summaries, and analyst notes SHALL be marked as derivatives and SHALL retain a link to the original source object.

## 8.6 Evidence grading

Specific information may be graded separately from source reliability:

- **1 — Independently confirmed**;

- **2 — Probably true**;

- **3 — Possibly true**;

- **4 — Doubtful**;

- **5 — Improbable**;

- **6 — Cannot be judged**.

A combined notation such as A1, B2, or F3 MAY be used, but teams SHALL understand that this is an analytical aid, not mathematical proof.

## 8.7 Conflict handling

Where sources conflict, the conflict SHALL remain visible. The system SHALL NOT silently overwrite an earlier claim with a later one merely because the later source seems more authoritative.

# 9. Fact, Claim, and Proposition Model

## 9.1 Why a proposition layer is required

Many investigative failures arise because raw source statements are immediately treated as facts. CS-AML therefore requires an explicit proposition layer.

## 9.2 Claim

A **Claim** is a statement made by a source. Example: “Person A owns Company X.” A claim may be true, false, incomplete, outdated, or disputed.

## 9.3 Fact

A **Fact** is a proposition that the analysis treats as sufficiently established for a stated purpose, based on evidence and verification. Facts SHOULD be narrowly worded and time-bound where appropriate. A Fact is a separate object supported by evidence (mandatory), optionally by claims, and by a recorded verification decision *[v0.1.1 · C02]*; the supporting Claim remains a permanent record of what the source asserted and is never converted into the Fact. *[v0.1.1 · A10]*

## 9.4 Example

Source: corporate filing.

Claim: Person A is listed as director of Company X.

Fact: On the filing date, the registry listed Person A as director of Company X.

Inference: Person A may exercise management influence over Company X.

Hypothesis: Person A exercises de facto control over Company X on behalf of another person.

## 9.5 Materiality

Only propositions material to the investigation need formal fact status. Trivial details MAY remain unstructured notes.

# 10. Entity Resolution and Identity Standard

## 10.1 Entity definition

An **Entity** is a uniquely tracked person, organisation, legal arrangement, account, wallet, asset, identifier, infrastructure object, or other object relevant to the investigation.

## 10.2 Canonical entity classes

Core classes SHOULD include Person, Organisation, Company/Legal Person, Government Body, Trust/Legal Arrangement, Bank/Payment Account, Crypto Wallet, Property, Vehicle, Vessel/Aircraft, Address, Phone, Email, Domain, Device Identifier, Contract, Project, Court Case, and Document.

## 10.3 Identity resolution

Entity resolution SHALL be evidence-based. Name similarity alone SHALL NOT justify merging persons. Resolution MAY consider official identifiers, dates of birth, addresses, phone numbers, email addresses, roles, family relationships, corporate filings, device indicators, transaction context, and temporal consistency.

## 10.4 Resolution outcomes

A record comparison SHALL resolve to one of: **same entity**, **probable same**, **possible same**, **different entity**, or **unresolved**. Systems SHOULD preserve the underlying records so merges can be reversed. In implementations these outcomes are recorded as append-only resolution decisions (Data Model v0.1.1 §8.4): same entity → MERGE; probable or possible same → POSSIBLE_MATCH; different entity → KEEP_SEPARATE; unresolved → DEFER; a reversed merge → UNMERGE. *[v0.1.1 · ER]*

## 10.5 Confidence and merge authority

High-impact entity merges SHOULD require a second reviewer where the merge materially changes the network or supports an allegation. Automated entity resolution MAY propose links but SHALL NOT silently create authoritative identity merges.

## 10.6 Identity uncertainty

Aliases, transliterations, name changes, married names, titles, and local naming conventions SHALL be preserved. Canonicalisation SHALL NOT erase original forms.

# 11. Relationship, Ownership, and Control Model

## 11.1 Relationship as evidence-bearing object

A relationship is not merely a graph edge; it is an analytical object with type, direction, time, evidence, and confidence.

## 11.2 Core relationship types

Recommended relationship types include OWNS, BENEFICIAL_OWNER_OF, CONTROLS, DIRECTOR_OF, COMMISSIONER_OF, EMPLOYED_BY, REPRESENTED_BY, RELATED_TO, ASSOCIATE_OF, SHARES_ADDRESS_WITH, SHARES_PHONE_WITH, SHARES_DOMAIN_WITH, CONTRACTED_BY, SUPPLIER_TO, PAID_BY, TRANSFERRED_VALUE_TO, LENDER_TO, ACQUIRED, SOLD_TO, LEASED_TO, DONATED_TO and FUNDED_BY. These are registered `relationship_type` wire values (`schemas/enums.yaml`; Data Model Annex B). Earlier names map as follows: REPRESENTS and ACTS_FOR → inverse of REPRESENTED_BY; SHARES_CONTACT_WITH → SHARES_PHONE_WITH, SHARES_ADDRESS_WITH or SHARES_DOMAIN_WITH; TRANSFERRED_TO → TRANSFERRED_VALUE_TO; LOANED_TO → LENDER_TO. *[v0.1.1 · C09]*

## 11.3 Legal ownership versus beneficial ownership

The framework SHALL distinguish at least:

- legal title;

- beneficial interest;

- control;

- management authority;

- use/possession;

- economic benefit.

These concepts MUST NOT be collapsed into a generic “owns” relationship.

## 11.4 Control indicators

Possible control indicators include authority to appoint directors, signature authority, funding dependence, repeated decision-making patterns, common representatives, nominee relationships, shared infrastructure, or contractual dominance. Control SHALL be expressed as an assessment unless directly established.

## 11.5 Temporal validity

Relationships SHOULD contain start/end dates or “known as of” dates. Investigations spanning years SHALL avoid treating historical relationships as current.

# 12. Asset and Wealth Analysis

## 12.1 Asset object

An **Asset** is anything of measurable or material economic value relevant to a case. Assets include real property, shares, securities, vehicles, vessels, aircraft, businesses, intellectual property, contractual rights, crypto-assets, receivables, cash equivalents, and valuable movable property.

## 12.2 Asset attributes

An asset SHOULD record legal owner, beneficial owner if known, controller, user/possessor, acquisition date, acquisition mechanism, estimated value, value date, valuation basis, disposal status, encumbrances, location, and supporting evidence.

## 12.3 Valuation standard

Valuations SHALL identify whether they are transaction price, official assessed value, market estimate, analyst estimate, or unknown. Estimated values SHALL include date, method, range where appropriate, and uncertainty.

## 12.4 Wealth comparison

Where declared assets or public disclosures exist, analysts MAY compare declared versus observed interests. Differences SHALL NOT automatically be labelled unexplained wealth. Analysts SHOULD account for debt, jointly held assets, valuation changes, inheritance, legitimate business income, asset disposals, and incomplete registries.

## 12.5 Asset attribution levels

Recommended attribution levels are: **legally owned**, **beneficially owned**, **controlled**, **used**, **associated**, and **unresolved**. This avoids overstating asset ownership.

# 13. Event and Timeline Analysis

## 13.1 Event model

An **Event** is a time-bounded occurrence connecting entities, assets, relationships, documents, or value flows. Examples include company incorporation, director change, contract award, asset acquisition, litigation event, transfer, donation, loan, dissolution, border movement, or public appointment.

## 13.2 Timeline objective

Timeline analysis identifies temporal correlations, sequencing, bursts, and changes that may be invisible in static graphs.

## 13.3 Temporal caution

Sequence is not causation. “Contract awarded, then property purchased” is a temporal fact. “Contract proceeds funded property purchase” is an inference requiring evidence.

## 13.4 Event confidence

Each event SHALL record date precision: exact, approximate, range, before/after, or unknown. Systems SHOULD preserve uncertainty instead of coercing approximate dates into exact timestamps.

# 14. Value Flow and Follow-the-Value Model

## 14.1 Value flow definition

A **Value Flow** represents a transfer, transformation, allocation, or economic movement of value from one entity or asset state to another. It generalises beyond bank transactions.

## 14.2 Flow types

Types MAY include payment, transfer, contract award, subcontract, loan, repayment, investment, share transfer, dividend, donation, grant, asset purchase, asset sale, lease, debt assignment, crypto transfer, in-kind benefit, or unexplained value movement.

## 14.3 Direct versus reconstructed flows

- **Direct flow:** supported by transactional or primary evidence of value movement.

- **Reconstructed flow:** inferred from linked economic events such as contract, invoice, asset acquisition, ownership change, and timeline.

Reconstructed flows SHALL be clearly marked as inferred and SHALL include the reasoning path.

In stored records the flow class is one of the four wire values `DIRECT`, `DOCUMENTED`, `RECONSTRUCTED`, `HYPOTHETICAL` defined in the Data Model Specification v0.1.1 (Section 11 and Annex A). *[v0.1.1 · A09]*

## 14.4 Flow attributes

A flow SHOULD record origin, destination, intermediate entities if known, amount, currency, date/time, mechanism, purpose if known, evidence, confidence, and whether amount is exact, estimated, bounded, or unknown.

## 14.5 No false precision

If the value is unknown, record unknown. If a range is supported, record the range. If only a contract ceiling is known, do not represent it as money actually paid.

## 14.6 Flow-chain analysis

Analysts MAY trace multiple hops to identify concentration, fragmentation, circular movement, rapid conversion to assets, offshore relocation, or movement through related entities. Each hop SHALL retain its evidentiary status.

# 15. Indicator and Typology Framework

## 15.1 Indicator definition

An **Indicator** is an observed fact, relationship, event, or pattern that increases or decreases the plausibility of a risk hypothesis. Indicators are not findings of criminal conduct.

## 15.2 Indicator classes

Indicators SHOULD be grouped by categories such as ownership opacity, transactional/value-flow anomaly, corporate behaviour, asset behaviour, procurement conflict, geographic exposure, professional intermediary use, identity inconsistency, network concentration, timing, and concealment behaviour.

## 15.3 Typology definition

A **Typology** is a documented pattern or method associated with financial crime or laundering risk. Typologies help generate and test hypotheses; they do not prove offences.

## 15.4 Typology catalogue structure

Each typology SHOULD have: identifier, name, description, predicate-crime context, expected indicators, counter-indicators, required data, common false positives, jurisdictional notes, detection logic, example patterns, and references.

## 15.5 Initial CS-AML typology families

A baseline catalogue SHOULD include:

- nominee or proxy ownership;

- shell-company layering;

- rapid legal-person turnover;

- circular ownership/control;

- asset conversion and resale;

- procurement-to-related-party value transfer;

- trade-based value manipulation indicators;

- professional intermediary concentration;

- mule/collector network indicators where lawful data exists;

- crypto/off-ramp layering indicators where public-chain data exists;

- cross-border legal-entity layering;

- charitable/nonprofit abuse indicators, applied cautiously and proportionately.

## 15.6 Counter-indicators

For every typology, analysts SHOULD record facts that make the typology less likely. Example: a company with shared address may be a legitimate serviced-office tenant; repeated director changes may reflect restructuring rather than concealment.

# 16. Hypothesis Management and Structured Analytic Techniques

## 16.1 Hypothesis object

A **Hypothesis** is a testable explanation for observed facts and indicators. It SHALL include scope, supporting evidence, contradicting evidence, assumptions, confidence, alternatives, and status.

## 16.2 Required hypothesis statuses

OPEN, SUPPORTED, WEAKENED, REJECTED, and INCONCLUSIVE.

## 16.3 Competing hypotheses

For significant cases, analysts SHOULD maintain multiple hypotheses, including at least one legitimate explanation. A simple Analysis of Competing Hypotheses matrix MAY be used to compare how evidence supports or contradicts each explanation.

## 16.4 Assumption register

Material assumptions SHALL be explicit. Example: “Assumption A3: registry ownership data was current at the relevant date.” If an assumption fails, affected assessments SHALL be reviewed.

## 16.5 Key intelligence questions

Each case SHOULD maintain Key Intelligence Questions (KIQs) and Priority Intelligence Requirements (PIRs) such as: Who controls Company X? What funded Asset Y? Are Company A and B under common beneficial ownership? What is the relationship between procurement award and later asset acquisition?

## 16.6 Disconfirmation requirement

Before a high-confidence adverse assessment, the analyst SHALL record what evidence would disprove or materially weaken the hypothesis and what steps were taken to look for it.

# 17. Analytical Confidence and Intelligence Gaps

## 17.1 Confidence is not probability

Confidence expresses the analyst's judgement about the robustness of the assessment given source quality, evidence consistency, reasoning, and remaining gaps. It is not automatically a statistical probability.

## 17.2 Confidence scale

Recommended scale:

- **High confidence:** multiple strong and substantially independent sources; limited critical gaps; alternatives materially weaker;

- **Moderate confidence:** credible supporting evidence but material gaps or unresolved conflicts remain;

- **Low confidence:** limited, indirect, or weak evidence; significant gaps; multiple plausible alternatives;

- **Insufficient basis:** available information does not justify an assessment.

## 17.3 Confidence factors

Analysts SHOULD consider source reliability, evidence credibility, independence of corroboration, temporal relevance, identity certainty, completeness, possibility of deception, analytical assumptions, and alternative explanations.

## 17.4 Intelligence-gap register

Every active investigation SHOULD maintain a gap register containing: gap description, importance, effect on hypotheses, possible collection methods, legality/safety constraints, owner, and status.

## 17.5 Decision relevance

Gaps SHALL be prioritised by how much resolving them could change the decision. Collecting more data that cannot change the assessment is not automatically valuable.

# 18. Risk Model for Civil Society Investigations

## 18.1 Purpose

CS-AML risk management is broader than money-laundering risk. It must consider risks created by the investigation itself.

## 18.2 Risk domains

The case risk assessment SHOULD cover:

- **Analytical risk:** false attribution, confirmation bias, entity misidentification;

- **Legal risk:** privacy, defamation, confidentiality, evidentiary restrictions, cross-border law;

- **Source risk:** retaliation, exposure, coercion, re-identification;

- **Subject harm risk:** disproportionate reputational, economic, or physical harm;

- **Security risk:** compromise of systems, accounts, evidence, or communications;

- **Operational risk:** loss of data, uncontrolled sharing, process failure;

- **Partner risk:** differing standards, onward dissemination, jurisdictional exposure;

- **Mission risk:** AML concepts being misused to stigmatise legitimate civil society or vulnerable communities.

## 18.3 Risk equation

Organisations MAY use a qualitative model: Risk = Likelihood × Impact, but SHALL document what the values mean. Where risk is difficult to quantify, structured qualitative categories are preferable to pseudo-precision.

## 18.4 Risk treatment

Treatments include avoid, reduce, transfer/share, accept, delay, redact, compartmentalise, or seek legal review. High residual risk SHALL be approved by an appropriately senior authority.

# 19. Lawful Collection, Privacy, and Data Protection

## 19.1 Collection rule

Collection SHALL be lawful, necessary, proportionate, and relevant to a defined purpose. Investigators SHALL distinguish availability from permission.

## 19.2 Data categories

The framework SHOULD distinguish public professional information, public personal information, restricted-source information, sensitive personal data, financial data, location data, criminal-allegation data, source identity, and privileged/confidential material.

## 19.3 Indonesia context

Under Indonesia's Personal Data Protection Law (Law No. 27 of 2022), financial data and criminal-record information are among categories of specific personal data. Implementers operating in Indonesia SHOULD obtain legal advice for their concrete processing activities and SHOULD apply heightened protection to sensitive data.

## 19.4 Collection decision test

Before collecting sensitive data, answer:

**1.** What investigative purpose does it serve?

**2.** Is there a lawful method to obtain it?

**3.** Is less intrusive data sufficient?

**4.** What harm could collection create?

**5.** Who needs access?

**6.** How long is retention justified?

**7.** Can it be safely shared or published?

## 19.5 Prohibited methods

CS-AML SHALL NOT be used to justify unauthorised access, credential theft, malicious software deployment, deceptive impersonation, illegal interception, or acquisition of stolen credentials.

## 19.6 Leaked or breached datasets

Use of leaked datasets presents elevated legal, ethical, security, and source risks. Organisations SHOULD require legal and security review before acquisition, processing, or publication and SHOULD avoid redistributing unnecessary personal data.

## 19.7 Retention

Retention SHALL be purpose-bound. Retention periods SHOULD differ for case material, protected-source identity, published evidence, raw personal data, and derived intelligence. Destruction or irreversible anonymisation SHOULD be documented.

# 20. Review, Challenge, and Quality Assurance

## 20.1 Peer review

Material assessments SHALL receive review by a person who did not author the main analysis. The reviewer SHALL examine provenance, entity resolution, reasoning, alternative hypotheses, confidence, gaps, and wording.

## 20.2 Legal/publication review

External products creating significant reputational or legal risk SHOULD receive qualified legal review, especially where they name identifiable individuals or allege criminal conduct.

## 20.3 Red-team challenge

High-impact investigations SHOULD use a structured challenge: assume the main hypothesis is wrong and identify the strongest legitimate explanation, missing evidence, identity errors, source manipulation possibilities, and misleading graph effects.

## 20.4 Quality criteria

A conformant intelligence product SHOULD be accurate, relevant, timely, clear, sourced, proportionate, reproducible, caveated, and decision-useful.

## 20.5 Common failure modes

QA SHALL check for: circular sourcing, repeated copies mistaken for independent corroboration, name collision, outdated corporate records, graph overinterpretation, speculative ownership, contract-value versus paid-value confusion, missing time context, selective evidence, hidden assumptions, and publication language stronger than the underlying assessment.

# 21. Intelligence Product Standard

## 21.1 Product types

Approved product classes are:

- Intelligence Note;

- Entity Profile;

- Asset Profile;

- Network Analysis;

- Value-Flow Analysis;

- Investigation Brief;

- Referral Package;

- Public Investigative Report;

- Strategic Typology Note.

## 21.2 Mandatory components

A material intelligence product SHALL contain:

**1.** product identifier and classification;

**2.** purpose and intended audience;

**3.** executive assessment;

**4.** investigation question and scope;

**5.** key findings, clearly separating facts from assessments;

**6.** entity/relationship summary;

**7.** relevant timeline and value flows;

**8.** supporting evidence and source notes;

**9.** relevant indicators/typologies;

**10.** alternative explanations;

**11.** confidence statement;

**12.** intelligence gaps;

**13.** handling/dissemination restrictions;

**14.** reviewer/approval record.

## 21.3 Executive assessment language

The framework encourages calibrated language: “indicates,” “is consistent with,” “likely,” “possibly,” “we assess with moderate confidence,” or “insufficient information to determine.” Avoid categorical criminal labels unless supported by authoritative legal findings or exceptionally strong verified evidence and reviewed for publication.

## 21.4 Referral package

A referral package SHOULD maximise utility to the recipient by providing structured subject identifiers, chronology, entity relationships, documentary references, value-flow logic, key unknowns, and contact details for follow-up, while minimising unnecessary personal data.

# 22. Dissemination, Sharing, and Referral

## 22.1 Dissemination principle

Information SHALL be shared on a need-to-know and purpose-appropriate basis. Publication is only one dissemination mode; others include secure referral, partner sharing, legal counsel review, or internal strategic learning.

## 22.2 Handling markings

Products SHOULD include a classification marking (PUBLIC, INTERNAL, SENSITIVE, RESTRICTED, or SOURCE_PROTECTED; see Section 6.4), together with explicit onward-sharing instructions when necessary. *[v0.1.1 · A08]*

## 22.3 Referral decision

Referral SHOULD consider seriousness, credibility, immediacy, competence of recipient, source protection, legal obligations, risk of retaliation, and whether referral could prejudice ongoing investigation.

## 22.4 Indonesia referral context

Where appropriate, relevant information may be submitted to competent authorities such as PPATK or other lawful channels. A CSO submission is not equivalent to a regulated institution's formal suspicious-transaction report. The value of a CSO referral lies in structured, well-sourced, decision-useful information.

## 22.5 Publication standard

Before naming persons in public reporting, organisations SHOULD verify identity, seek corroboration proportionate to harm, distinguish allegation from fact, offer a fair opportunity to respond where appropriate, and document editorial/legal approval.

# 23. Technology Architecture Requirements

## 23.1 Architecture principle

Technology SHALL support analytical discipline rather than replace it. The recommended architecture is modular and capability-based.

## 23.2 Core capabilities

A mature platform SHOULD provide:

- case management;

- source registry;

- evidence repository;

- entity registry and resolution;

- relationship/knowledge graph;

- asset register;

- event/timeline engine;

- value-flow model;

- indicator/typology catalogue;

- hypothesis workspace;

- assessment and confidence model;

- intelligence-product generation;

- role-based access control;

- audit logging;

- secure export/referral.

## 23.3 Truth model

Entity and Evidence objects SHOULD be reusable across cases. Case objects provide investigative context, permissions, questions, and conclusions. This avoids duplicated identities and enables cross-case discovery while preserving case compartmentalisation.

## 23.4 Data stores

Implementations MAY combine relational storage for transactional consistency, object storage for evidence, full-text search for documents, and a graph database for relationships. Technology choice is secondary to provenance, access control, reversibility, and auditability.

## 23.5 API and connector controls

Connectors SHALL document source, authentication method, data licence/terms, collection frequency, fields ingested, retention, and failure behaviour. Automated connectors SHALL NOT bypass access controls or terms that prohibit automated extraction without legal review.

## 23.6 AI use

AI MAY assist OCR, translation, entity extraction, summarisation, link suggestions, and triage. AI-generated outputs SHALL be treated as derived analytical material, not primary evidence. Material facts and adverse assessments SHALL be verified against underlying sources. Models SHALL NOT autonomously publish allegations or merge identities without review.

## 23.7 Explainability

If risk scoring, anomaly detection, or graph ranking is used, the system SHOULD show the contributing signals, model/rule version, data snapshot, and limitations. “Score 87” without explanation is not sufficient for a material decision.

# 24. Security and Operational Protection

## 24.1 Security objective

The security objective is to preserve confidentiality, integrity, availability, source protection, and analyst safety without making the framework unusable.

## 24.2 Minimum controls

Systems SHALL implement strong authentication, least-privilege access, secure backups, encryption in transit, protected storage for restricted data, timely patching, audit logs, and offboarding controls.

## 24.3 Compartmentalisation

Highly sensitive source identities and legal-risk material SHOULD be compartmentalised from routine analytical data. Analysts should receive the minimum identity detail necessary.

## 24.4 Threat modelling

High-risk investigations SHOULD consider adversaries capable of phishing, credential theft, legal pressure, physical surveillance, insider compromise, malware, account takeover, doxxing, and disinformation.

## 24.5 Evidence preservation

Security controls SHALL preserve evidentiary integrity. Analysts SHOULD avoid editing original files; transformations SHOULD create derived copies.

## 24.6 Incident response

The programme SHALL maintain a response plan for source exposure, evidence compromise, accidental publication, credential compromise, and loss of devices containing sensitive material.

# 25. Auditability, Logging, and Reproducibility

## 25.1 Audit objective

A reviewer should be able to reconstruct how a material assessment was reached without relying on the memory of the original analyst.

## 25.2 Logged actions

Systems SHOULD log creation, modification, merge/split of entities, evidence access where appropriate, relationship changes, hypothesis status changes, assessment approvals, exports, and dissemination events.

## 25.3 Versioning

Material assessments, typologies, analytical rules, and reports SHALL be versioned. Later changes SHALL NOT erase what was known or assessed at an earlier time.

## 25.4 Reproducibility package

For important assessments, the case SHOULD be able to generate a reproducibility package containing evidence references, entity IDs, key queries, analytical steps, assumptions, and tool/model versions, excluding secrets not needed by the reviewer.

# 26. Metrics and Effectiveness

## 26.1 Avoid vanity metrics

Number of cases, scraped records, graph nodes, or alerts are not sufficient indicators of effectiveness.

## 26.2 Outcome metrics

Programmes SHOULD track measures such as:

- percentage of material claims with direct provenance;

- entity-resolution correction rate;

- percentage of high-impact products peer-reviewed;

- time from intake to triage decision;

- proportion of assessments with documented alternatives and gaps;

- referral acceptance/follow-up rate where measurable;

- correction/retraction rate;

- source-exposure incidents;

- data-retention exceptions;

- usefulness feedback from legitimate recipients.

## 26.3 Effectiveness review

At least annually, mature programmes SHOULD examine whether controls improve useful outcomes rather than merely create process. This reflects the wider financial-crime principle of focusing on proportionality, prioritisation, and effectiveness rather than box-ticking.

# 27. Assurance and Control Testing

## 27.1 Assurance objective

Assurance determines whether the framework is not only documented but operating as intended.

## 27.2 Control testing

Representative cases SHOULD be sampled to test source provenance, evidence integrity, entity resolution, privacy handling, review, dissemination, and retention.

## 27.3 Analytical audit

An analytical audit SHOULD test whether conclusions are supported by the evidence, whether contradictory evidence was considered, and whether confidence language matches the record.

## 27.4 Technology validation

Where automated matching, ranking, anomaly detection, or AI is used, the organisation SHOULD evaluate false positives, false negatives, bias, drift, explainability, access-control effects, and reproducibility.

## 27.5 Corrective actions

Findings SHALL have owners, target dates, severity, remediation status, and verification of closure.

# 28. Maturity Model

## 28.1 Level 0 — Ad hoc

Investigations are person-dependent; evidence and provenance are inconsistent; little formal review exists.

## 28.2 Level 1 — Foundation

Basic policies, case/source/evidence registers, lawful collection rules, manual review, and secure storage are in place.

## 28.3 Level 2 — Operational

Formal lifecycle gates, entity resolution, hypothesis management, confidence scales, gap registers, sensitivity classification, and peer review are consistently used.

## 28.4 Level 3 — Integrated intelligence

Reusable entity/evidence layer, graph analysis, cross-case discovery, standard typology catalogue, controlled automation, metrics, and structured referral products are operational.

## 28.5 Level 4 — Assured and adaptive

Independent assurance, advanced security, controlled AI/analytics, model validation, continual typology updates, partner governance, measurable effectiveness, and continuous improvement are institutionalised.

## 28.6 Maturity rule

Higher maturity does not mean greater surveillance. A mature system may collect less data, more deliberately, with stronger provenance and higher analytical value.

# 29. Control Catalogue

The following controls form the minimum catalogue for CS-AML v0.1.1. Organisations MAY add local controls.

| **ID** | **Control objective** | **Mandatory requirement** | **Evidence of operation** |
|----|----|----|----|
| GOV-01 | Accountable ownership | Every case SHALL have an accountable owner. | Case register / approval |
| GOV-02 | Conflict control | Material conflicts SHALL be declared and managed. | Conflict log |
| CAS-01 | Defined purpose | Case SHALL have investigation question and scope. | Case charter |
| CAS-02 | Gate approval | High-risk cases SHALL pass defined lifecycle gates. | Gate records |
| SRC-01 | Provenance | Material sources SHALL have provenance metadata. | Source register |
| SRC-02 | Reliability | Source reliability SHOULD be assessed. | Source rating |
| EVD-01 | Integrity | Critical digital evidence SHOULD be integrity-protected. | Hash / preservation record |
| EVD-02 | Derivatives | Derived artefacts SHALL link to originals. | Evidence lineage |
| ENT-01 | Resolution | Material entity merges SHALL be evidence-based and reversible. | Merge history |
| REL-01 | Relationship proof | Material graph edges SHALL link to evidence. | Edge provenance |
| AST-01 | Attribution | Ownership, control, use, and association SHALL be distinct. | Asset record |
| VAL-01 | Flow status | Direct and reconstructed value flows SHALL be distinguished. | Flow record |
| TYP-01 | Typology caution | Typology match SHALL NOT be treated as proof. | Assessment wording |
| HYP-01 | Competing explanations | Material cases SHOULD record plausible alternatives. | Hypothesis matrix |
| HYP-02 | Disconfirmation | High-impact adverse findings SHALL document disconfirming search. | Review checklist |
| ASM-01 | Confidence | Material assessments SHALL carry confidence and basis. | Assessment record |
| GAP-01 | Unknowns | Material intelligence gaps SHALL be explicit. | Gap register |
| PRI-01 | Minimisation | Sensitive data SHALL be necessary and proportionate. | Collection decision |
| PRI-02 | Retention | Sensitive data SHALL have retention/disposition rules. | Retention schedule |
| SEC-01 | Least privilege | Access SHALL be role/need based. | Access matrix |
| SEC-02 | Source protection | Protected source identities SHALL be compartmentalised. | Restricted store |
| QUA-01 | Peer review | High-impact products SHALL be independently reviewed. | Review sign-off |
| DIS-01 | Handling | Dissemination SHALL have classification and approval. | Dissemination log |
| AUD-01 | Auditability | Material analytical changes SHOULD be logged. | Audit trail |
| TEC-01 | AI verification | AI outputs SHALL NOT become material facts without verification. | QA record |
| TEC-02 | Explainability | Automated scores used materially SHOULD be explainable. | Model/rule record |

# 30. Canonical Data Model

## 30.1 Object hierarchy

The canonical model is:

``` text
CASE → SOURCE → EVIDENCE → CLAIM/FACT → ENTITY → RELATIONSHIP → ASSET → EVENT → VALUE FLOW → INDICATOR → TYPOLOGY → HYPOTHESIS → ASSESSMENT → INTELLIGENCE PRODUCT
```

Objects are linked rather than nested wherever reuse matters.

## 30.2 Minimum schemas

**Case:** id, title, purpose, question, owner, status, sensitivity, jurisdictions, scope, dates, risks, linked objects.

**Source:** id, type, origin, publisher, URL/location, dates, collector, reliability, legal/access notes, archive/hash.

**Evidence:** id, source_id, type, original/derivative, hash, acquired_at, custodian, extract/location, verification.

**Entity:** id, type, canonical_name, aliases, identifiers, jurisdiction, status, confidence.

**Relationship:** id, from_entity, type, to_entity, start/end, evidence_ids, confidence, status.

**Asset:** id, type, identifiers, legal_owner, beneficial_owner, controller, location, valuation, valuation_date, evidence.

**Event:** id, type, date_precision, start/end, entities, assets, place, evidence.

**ValueFlow:** id, type, origin, destination, amount/range, currency, date, direct_or_reconstructed, evidence, confidence.

**Indicator:** id, category, proposition, linked_objects, direction, significance, evidence.

**Hypothesis:** id, statement, status, support, contradictions, assumptions, alternatives, confidence.

**Assessment:** id, judgement, confidence, basis, gaps, alternatives, reviewer, version.

**Product:** id, type, audience, classification, assessments, approvals, dissemination.

## 30.3 Provenance graph

Every Assessment SHOULD be traceable backwards to Hypotheses, Indicators, Facts/Claims, Evidence, and Sources. This backward chain is a core conformance feature.

# 31. Reference Operating Procedure

A conformant investigation can follow the procedure below:

**1. Receive lead.** Record origin, urgency, sensitivity, and immediate protection needs.

**2. Triage.** Determine public-interest relevance, scope feasibility, legal/security risk, and whether the lead should be rejected, monitored, or opened.

**3. Create case charter.** State question, scope, jurisdictions, timeline, subjects, initial hypotheses, and prohibited collection methods.

**4. Create collection plan.** Map key questions to lawful sources and prioritise high-decision-value gaps.

**5. Register sources.** Capture provenance, reliability, access constraints, and preserved copies.

**6. Preserve evidence.** Hash critical files; register extracts and derivatives.

**7. Extract claims/entities/events.** Keep source statements separate from verified facts.

**8. Resolve entities.** Compare identifiers, preserve uncertainty, require review for impactful merges.

**9. Build relationships and asset map.** Distinguish legal ownership, control, use, and beneficial interest.

**10. Build timeline and value-flow model.** Mark direct versus reconstructed flows.

**11. Map indicators to typologies.** Record counter-indicators and false-positive explanations.

**12. Test competing hypotheses.** Search for disconfirming evidence.

**13. Draft assessment.** State judgement, confidence, basis, assumptions, and gaps.

**14. Peer/legal/security review.** Apply review depth proportional to harm and sensitivity.

**15. Decide dissemination.** Close, continue, refer, share, or publish.

**16. Archive/retain.** Apply retention rules and document lessons learned.

# 32. Implementation Roadmap for a CSO

## Phase 1 — Policy and manual workflow

Create case charter, source register, evidence register, entity sheet, relationship sheet, hypothesis matrix, risk review, and intelligence-report template. This phase can operate with encrypted document storage and a spreadsheet/database if access control is adequate.

## Phase 2 — Structured case platform

Implement reusable entities, controlled vocabularies, relationship provenance, asset/event/value-flow objects, role-based access, and basic graph visualisation.

## Phase 3 — Integrated open-source intelligence

Add lawful connectors to corporate registries, procurement data, court decisions, sanctions/PEP data where relevant, public-chain data, and archival services. Add deduplication and entity-resolution assistance.

## Phase 4 — Analytical automation

Introduce rule-based indicators, graph queries, anomaly support, NLP/entity extraction, and AI-assisted document processing under strict verification and audit controls.

## Phase 5 — Assurance and ecosystem collaboration

Establish independent assurance, partner-sharing agreements, common schemas, secure referral mechanisms, typology exchange, and periodic methodology review.

# 33. Annex A — Case Charter Template

**Case ID:**

**Title:**

**Owner:**

**Classification:**

**Date opened:**

**Trigger/lead:**

**Public-interest rationale:**

**Investigation question:**

**Scope included:**

**Scope excluded:**

**Jurisdictions:**

**Time period:**

**Initial subjects/entities:**

**Initial hypotheses:**

**Key intelligence questions:**

**Expected sensitive data:**

**Legal/privacy constraints:**

**Security/source risks:**

**Collection methods authorised:**

**Collection methods prohibited:**

**Reviewer/approver:**

# 34. Annex B — Source and Evidence Register Template

| **Field** | **Description** |
|----|----|
| Source ID | Stable identifier |
| Source type | Official / first-party / media / human / partner / other |
| Origin | Publisher/person/system |
| URL/location | Retrieval location |
| Publication date | If known |
| Access date | When collected |
| Collector | Responsible person |
| Access method | Browser/API/received/etc. |
| Reliability | A–F |
| Legal/access note | Terms, permission, sensitivity |
| Archive | Preserved copy location |
| Evidence ID | Linked preserved object |
| SHA-256 | For critical files |
| Derivative status | Original / OCR / translation / extract / analysis |
| Verification | 1–6 or narrative |

# 35. Annex C — Hypothesis Matrix Template

For each hypothesis record:

| **Evidence / indicator** | **H1 Legitimate** | **H2 Conflict/undisclosed interest** | **H3 Nominee/control concealment** | **H4 Laundering-related explanation** |
|----|----|----|----|----|
| Shared address | Neutral | Supports | Supports | Weak support |
| Common director | Neutral | Supports | Supports | Weak support |
| Direct payment evidence | Depends | Depends | Supports if concealed | Stronger support |
| Active operating footprint | Supports | Neutral | Weakens | Weakens |
| Independent financing | Supports | Weakens | Weakens | Weakens |

Use symbols or short notes rather than pseudo-precise numerical scoring unless a validated model exists. Record what evidence would most discriminate between hypotheses.

# 36. Annex D — Intelligence Product Template

## Product metadata

Product ID, title, date, author, reviewer, classification, intended audience, handling restrictions.

## Executive assessment

A concise statement of the principal judgement and confidence.

## Investigation question and scope

What the work sought to answer and what it did not cover.

## Key facts

Only verified/time-bounded propositions, each linked to evidence.

## Analytical findings

Relationships, control, assets, events, and value flows.

## Typology relevance

Observed similarities and important counter-indicators.

## Alternative explanations

Plausible non-criminal or less adverse interpretations.

## Intelligence gaps

Unknowns capable of changing the assessment.

## Confidence

High / Moderate / Low / Insufficient basis with rationale.

## Recommended action

Continue collection, close, monitor, seek specialist review, refer, or publish.

## Evidence index

Structured list of evidence and sources sufficient for independent review.

# 37. Annex E — Dissemination Review Checklist

Before external dissemination confirm:

- identity has been adequately resolved;

- statements distinguish fact, claim, inference, and allegation;

- key evidence is accessible to the reviewer;

- counterevidence and alternatives were considered;

- sensitive personal data is necessary for the audience;

- source identity is protected where required;

- legal/privacy/security review was completed at the appropriate level;

- confidence language matches evidence strength;

- intelligence gaps are visible;

- onward-sharing restrictions are stated;

- corrections/update mechanism exists.

# 38. Annex F — Typology Record Template

**Typology ID:**

**Name:**

**Description:**

**Relevant predicate crimes:**

**Typical entities:**

**Expected indicators:**

**Counter-indicators:**

**Required data:**

**Common false positives:**

**Geographic/jurisdiction notes:**

**Detection/graph queries:**

**Known limitations:**

**References:**

**Version / review date:**

# 39. Annex G — Glossary of Core Terms

**Adverse assessment:** an analytical judgement that, if disseminated, could materially affect an identifiable person's or organisation's reputation, rights, safety, or legal position.

**Allegation:** an assertion that a person or entity engaged in wrongdoing; stronger than an analytical hypothesis.

**Assessment:** a reasoned analytical judgement derived from evidence, indicators, hypotheses, and context, expressed with confidence and caveats.

**Asset:** an item, right, interest, or resource of economic value.

**Beneficial ownership:** the natural person(s) who ultimately own, control, or benefit from a legal person or arrangement, subject to applicable legal definitions.

**Case:** a bounded investigative context; not the authoritative store for entity identity.

**Claim:** a proposition asserted by a source, not yet necessarily verified.

**Confidence:** an analyst's judgement about the robustness of an assessment; not automatically a probability.

**Control:** a measure designed to prevent, detect, reduce, or respond to a risk or process failure.

**Direct value flow:** a movement of value supported by direct transactional or primary evidence.

**Entity:** a uniquely tracked person, organisation, legal arrangement, account, asset, identifier, or other relevant object.

**Entity resolution:** the process of determining whether records refer to the same or different real-world entities.

**Evidence:** a preserved item, observation, or extract supporting or contradicting a proposition.

**Fact:** a proposition treated as sufficiently established for the current analytical purpose.

**Follow-the-value:** tracing economic value across money, assets, ownership, contracts, debt, rights, and transformations.

**Indicator:** an observed fact or pattern that changes the plausibility of a risk hypothesis.

**Intelligence gap:** missing information that limits or could materially change an assessment.

**Intelligence product:** a reviewed analytical output designed to support a decision, referral, publication, or further investigation.

**Legal owner:** the person or entity holding formal title under applicable law or registry.

**Material:** sufficiently important that an error or omission could change the assessment, action, or harm profile.

**Predicate offence:** an underlying offence capable, under applicable law, of generating proceeds that may be laundered.

**Provenance:** documented origin and lineage of information and evidence.

**Reconstructed value flow:** an inferred movement or transformation of value derived from linked economic events rather than direct transaction records.

**Relationship:** an evidence-bearing connection between entities, with type, time, direction, confidence, and provenance.

**Source:** the origin from which information is obtained.

**Typology:** a documented pattern or method associated with financial-crime risk, used for analysis rather than proof.

**Value flow:** a transfer, transformation, allocation, or economic movement of value.

**Verification:** the process of testing a claim, identity, event, or evidence item against independent or authoritative information.

# 40. Annex H — External Standards Mapping

This mapping explains how CS-AML draws concepts from recognised external sources without claiming equivalence to a regulated AML programme.

| **CS-AML domain** | **External concept** | **Relationship** |
|----|----|----|
| Risk-based proportionality | FATF Recommendation 1; Wolfsberg RBA | CS-AML adapts proportionality, prioritisation, and effectiveness to civil-society investigation risk. |
| NPO safeguards | FATF Recommendation 8 materials | CS-AML explicitly prevents over-application of AML concepts to legitimate NPO activity. |
| Beneficial ownership | FATF Recommendations 24/25 concepts | CS-AML uses ownership/control distinction for open-source investigation; it does not create official BO determinations. |
| Asset tracing | UNCAC Chapter V / UNODC civil-society guidance (pending verification — page-level support not confirmed) | CS-AML structures public-source asset tracing, legal analysis, and evidence packaging. *[v0.1.1 · A13]* |
| Public referral | PPATK public/CSO engagement | CS-AML structures decision-useful public information; it is not an STR/TKM substitute. |
| Effectiveness and assurance | Wolfsberg effectiveness principles | CS-AML measures useful outcomes, control operation, and quality rather than raw activity volume. |
| Privacy and minimisation | Indonesia PDP Law and applicable privacy law | CS-AML requires purpose limitation, sensitivity handling, retention, and proportionality. |

The mapping is informative. Compliance with CS-AML does not imply compliance with FATF Recommendations, national AML law, regulated-entity obligations, or professional standards.

# 41. Annex I — Minimum Conformance Evidence Pack

An organisation claiming CS-AML v0.1.1 alignment SHOULD be able to produce, under appropriate confidentiality controls, a sample evidence pack containing:

**1.** framework adoption decision or policy statement;

**2.** role and decision-right matrix;

**3.** case charter template and a completed sample;

**4.** source and evidence registers showing provenance;

**5.** evidence-integrity example including a checksum or equivalent control;

**6.** entity-resolution record including one reviewed merge or non-merge decision;

**7.** relationship record with evidence-linked graph edge;

**8.** asset/value-flow record distinguishing direct and reconstructed information;

**9.** hypothesis matrix showing supporting and contradicting evidence;

**10.** intelligence-gap register;

**11.** risk/privacy review for sensitive collection;

**12.** peer-review record for a material assessment;

**13.** approved intelligence product showing confidence language and caveats;

**14.** dissemination record and handling classification;

**15.** retention/disposition evidence;

**16.** audit log or equivalent change history;

**17.** annual control-effectiveness or methodology review where maturity level requires it.

Absence of a specific software feature does not automatically mean non-conformance if the organisation can demonstrate the control objective through another reliable mechanism.

# 42. Annex J — Normative and Informative References

The framework is informed by, but is not a replacement for, the following sources:

**Source verification status.** References 1, 2, 5, 6, and 7 were confirmed to exist at the cited official locations during the 2026-10-07 documentation audit (publication-level verification only). References marked `pending verification` have not been confirmed at the publication, section, or page level. A reference supports the concept it is cited for; it does not mean that individual CS-AML requirements, indicators, thresholds, or grades are derived from or endorsed by that source. *[v0.1.1 · A13]*

**CS-AML design conventions.** The lifecycle gates G0–G6, conformance and maturity levels, A–F source-reliability and 1–6 information-credibility grading as applied here, the four value-flow classes, indicator classes, and the typology identifiers of the Typology Catalogue are CS-AML design decisions. They are not FATF or other external requirements. *[v0.1.1 · A13, N01]*

**1.** Financial Action Task Force (FATF), **The FATF Recommendations**, as amended June 2026. International standards covering AML/CFT/CPF and the risk-based approach.

https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Fatf-recommendations.html

**2.** FATF, **Non-Profit Organisations / Recommendation 8 materials**, including revisions intended to ensure targeted and proportionate measures and avoid suppression of legitimate NPO activity.

https://www.fatf-gafi.org/en/topics/non-profit-organisations.html

**3.** FATF, **Best Practices — Combating the Terrorist Financing Abuse of Non-Profit Organisations (Recommendation 8)**. Status: pending verification — specific publication/section not yet identified (edition and direct URL not recorded). *[v0.1.1 · A13]*

https://www.fatf-gafi.org/

**4.** UNODC, **Civil Society Guide to the United Nations Convention against Corruption**, including civil-society roles in asset tracing, public information, financial investigation, forensic auditing, and legal analysis. Status: pending verification — page-level support not confirmed (URL indexed on the official UNODC domain; bibliographic title and page locations for the specific roles listed have not been confirmed from the full PDF). *[v0.1.1 · A13]*

https://www.unodc.org/documents/NGO/Corruption/251113-CSU-UNCAC_Guide-Web.pdf

**5.** PPATK, **Klinik Dumas Special Edition: PPATK dan NGO/CSO Perkuat Aduan TPPU**, 26 November 2025.

https://www.ppatk.go.id/news/read/1570/klinik-dumas-special-edition-ppatk-dan-ngocso-perkuat-aduan-tppu-melalui-peluncuran-laporppatkgoid.html

**6.** Wolfsberg Group, **Guidance on the Risk-Based Approach**, June 2026, emphasising proportionality, prioritisation, and effectiveness in financial-crime risk management.

https://wolfsberg-group.org/resources/165/205

**7.** Republic of Indonesia, **Law No. 27 of 2022 on Personal Data Protection**, for data-protection context applicable to implementations in Indonesia.

Implementers SHALL identify additional national law, sector rules, journalistic ethics, professional duties, contractual restrictions, and organisational policies applicable to their actual activity.
