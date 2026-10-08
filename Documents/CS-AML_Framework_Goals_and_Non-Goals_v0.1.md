**CS-AML FRAMEWORK v0.1**

**Framework Goals and Non-Goals**

*Civil Society Financial Intelligence / AML Investigation*

| **Document status** | Normative component |
|----|----|
| **Version** | 0.1 |
| **Intended audience** | Civil society organisations, investigative journalists, researchers, public-interest investigators, technology implementers |
| **Normative language** | MUST / SHALL, SHOULD, MAY |
| **Purpose** | Define what CS-AML is intended to achieve, and the boundaries it MUST NOT cross |

# 1. Normative Purpose

This document defines the formal goals, intended outcomes, operational objectives, and non-goals of the CS-AML Framework v0.1. It is a normative component of the framework and SHALL be used to interpret the scope of all subordinate controls, procedures, data models, analytical methods, and technology implementations.

> **Primary Goal**  
> CS-AML SHALL enable civil society organisations to produce lawful, evidence-based, reproducible, proportionate, and actionable financial intelligence that can support public-interest investigation, referral, advocacy, or publication without assuming or exercising the powers of a regulator, financial intelligence unit, law-enforcement agency, or regulated financial institution.

The framework exists to increase the quality of civil-society financial investigation. It does not exist to expand surveillance powers, create private blacklists, or convert suspicion into guilt. All implementations SHALL preserve this distinction.

# 2. Strategic Outcome Model

CS-AML organises its strategic purpose around four linked outcomes:

| **Outcome** | **Normative meaning** |
|----|----|
| **DISCOVER** | Identify relevant entities, assets, relationships, events, documents, contracts, ownership structures, and value-transfer indicators from lawful sources. |
| **UNDERSTAND** | Reconstruct ownership, control, economic relationships, timelines, and direct or inferred flows of value in context. |
| **ASSESS** | Evaluate evidence, indicators, typologies, competing hypotheses, uncertainty, intelligence gaps, and analytical confidence. |
| **ACT** | Produce a decision-useful intelligence product suitable for further investigation, peer review, referral, advocacy, or responsible publication. |

# 3. Strategic Goals

## G1. Structure civil-society financial investigation

CS-AML SHALL transform fragmented investigative activity into a controlled lifecycle in which scope, sources, evidence, facts, indicators, hypotheses, assessments, and outputs are distinguishable and traceable.

## G2. Enable lawful follow-the-value investigation

CS-AML SHALL support reconstruction of economic value and control even where investigators have no lawful access to private bank transaction data. It SHALL explicitly distinguish direct financial evidence from reconstructed or inferred value flows.

## G3. Improve evidentiary quality and analytical credibility

Every material analytical judgement SHALL be traceable to recorded sources and evidence. Provenance, verification state, contradiction, uncertainty, and confidence SHALL remain visible.

## G4. Reduce confirmation bias and unsupported allegation

The framework SHALL require separation of fact, inference, indicator, hypothesis, assessment, and allegation. Material cases SHOULD include plausible alternative hypotheses and evidence that weakens as well as supports the preferred hypothesis.

## G5. Produce decision-useful financial intelligence

The output SHALL be structured so that another legitimate actor can understand what is known, how it is known, what remains unknown, why the issue matters, and what further action is justified.

## G6. Protect rights, privacy, sources, and safety

Collection and processing SHALL be proportionate to a defined public-interest purpose. Implementations SHALL minimise unnecessary personal data, protect sensitive sources, and apply access, retention, security, and dissemination controls.

## G7. Make investigation reproducible and auditable

A competent reviewer SHOULD be able to reconstruct the analytical path from final judgement back to supporting evidence and source provenance, including key analyst decisions.

## G8. Establish a common civil-society financial-intelligence language

CS-AML SHALL provide common definitions, object types, confidence semantics, control expectations, and product structures so that organisations can collaborate without losing analytical meaning.

## G9. Provide a technology-neutral foundation for tooling

The framework SHALL define capabilities and information objects independently of any specific software vendor or stack. Technology implementations MAY automate parts of the process but SHALL preserve the normative distinctions defined by the framework.

## G10. Preserve institutional boundaries

CS-AML SHALL NOT confer regulatory, coercive, investigative, interception, freezing, seizure, subpoena, or law-enforcement authority. Findings remain intelligence assessments unless and until a competent authority determines otherwise.

# 4. Operational Objectives

| **ID** | **Objective** | **Requirement** |
|----|----|----|
| **O1** | Case discipline | Every investigation SHALL have a documented question, scope, public-interest rationale, owner, and review state. |
| **O2** | Source discipline | Every material source SHALL have provenance, access context, acquisition date, and reliability attributes. |
| **O3** | Evidence discipline | Material evidence SHALL be distinguishable from analyst interpretation and, where appropriate, integrity-preserved. |
| **O4** | Entity discipline | Entity resolution decisions SHALL be explainable and confidence-qualified; name similarity alone SHALL NOT be sufficient for high-confidence merging. |
| **O5** | Relationship discipline | Material graph edges SHALL have an explicit relationship type, evidence basis, temporal context where known, and confidence. |
| **O6** | Value-flow discipline | Direct and reconstructed flows SHALL be separately typed. Unknown values SHALL remain unknown rather than estimated without basis. |
| **O7** | Hypothesis discipline | Material hypotheses SHALL record supporting evidence, contradicting evidence, unresolved questions, and confidence. |
| **O8** | Assessment discipline | Assessments SHALL state key judgements, confidence, significant assumptions, alternative explanations, and intelligence gaps. |
| **O9** | Dissemination discipline | Sensitive products SHALL undergo an appropriate review before external referral or publication. |
| **O10** | Protection discipline | Security, privacy, and source-protection requirements SHALL be proportionate to the sensitivity of the case and persons affected. |

# 5. Intended Outcomes

- Investigations that are better scoped, documented, and reviewable.

- Financial and ownership relationships that can be understood without misrepresenting inference as transaction fact.

- Intelligence products that clearly communicate what is known, what is assessed, and what remains uncertain.

- Referrals that are more useful to competent authorities because they contain structured entities, timelines, evidence references, analytical rationale, and intelligence gaps.

- Public-interest reporting that is less vulnerable to analytical overreach because claims and confidence are explicit.

- Cross-organisational collaboration based on shared object definitions and evidence provenance rather than disconnected spreadsheets and screenshots.

- Technology systems that reinforce analytical discipline instead of merely producing more alerts, graphs, or personal-data collection.

# 6. Non-Goals and Explicit Boundaries

> **Interpretation rule**  
> A non-goal is not merely something outside the initial implementation roadmap. It is a boundary that protects the legitimacy, safety, and analytical integrity of CS-AML.

## NG1. Not a criminal adjudication framework

CS-AML SHALL NOT be used to determine criminal guilt or to label a person as a money launderer solely on the basis of framework output.

## NG2. Not a substitute for an FIU or law-enforcement investigation

The framework does not provide compulsory information-gathering powers, bank-record access, search powers, seizure powers, or legal process.

## NG3. Not a bank AML compliance programme

CS-AML is not intended to replace customer due diligence, transaction monitoring, sanctions compliance, regulatory reporting, or other obligations of regulated institutions.

## NG4. Not a mass-surveillance framework

Implementation SHALL NOT treat broader data collection as inherently better. Data volume is not a maturity metric.

## NG5. Not a private scoring or blacklist system

The framework SHALL NOT be used to create opaque reputational scores or persistent blacklists of persons based on unverified suspicion.

## NG6. Not an authorisation for unlawful collection

The framework does not justify hacking, credential theft, impersonation, unlawful interception, unauthorised account access, or acquisition of unlawfully obtained private data.

## NG7. Not an automated accusation engine

AI, graph analytics, rules, or typology matching MAY identify leads; they SHALL NOT autonomously convert a pattern match into a finding of wrongdoing.

## NG8. Not a replacement for legal review or editorial judgement

Referral, publication, and sensitive dissemination remain human-governed decisions.

## NG9. Not an excuse to over-collect sensitive personal data

Investigators SHALL apply purpose limitation, necessity, proportionality, retention limits, and access controls.

## NG10. Not limited to money-laundering prosecutions

The framework MAY support public-interest investigations into corruption, fraud, environmental crime, illicit trade, procurement abuse, sanctions evasion, trafficking, or other financial-crime contexts where following ownership, assets, and value is relevant.

# 7. Success Criteria

CS-AML SHOULD be considered effective when it improves the quality of investigative decision-making rather than merely increasing activity volume. Implementations SHOULD measure success against criteria such as:

- Percentage of material judgements traceable to evidence and source provenance.

- Percentage of high-impact entity merges that have documented resolution rationale and reviewer approval.

- Percentage of material assessments that state confidence and intelligence gaps.

- Frequency of unsupported claims or unreferenced graph relationships identified during quality review.

- Time required for an independent reviewer to reconstruct the basis of a key judgement.

- Quality and usefulness of referrals as assessed by receiving legitimate partners, where feedback is available.

- Reduction in duplicate collection and unnecessary retention of personal data.

- Percentage of sensitive products receiving peer, legal, editorial, or protection review as required.

- Ability to distinguish direct evidence from inferred or reconstructed relationships in exported products.

- Number and severity of privacy, source-protection, or security incidents.

# 8. Principles for Interpreting Goal Achievement

## Quality over volume

More sources, more entities, more graph edges, more alerts, or more cases do not by themselves represent success.

## Proportionality over maximal collection

A mature implementation SHOULD collect the minimum information needed to answer a defined investigative question with sufficient confidence.

## Transparency over analytical mystique

A conclusion that cannot be explained and traced SHOULD carry less weight than a simpler conclusion that can be independently reviewed.

## Human judgement over automation

Automation MAY accelerate discovery and organisation, but consequential analytical judgements SHALL remain subject to accountable human review.

## Uncertainty is information

Unknown, disputed, and contradictory facts SHALL be preserved as analytical information rather than hidden to make a case appear stronger.

## Public interest over curiosity

The framework SHOULD be applied where there is a legitimate public-interest investigative purpose, not merely because information about a person is available.

# 9. Relationship to the CS-AML Normative Core

All CS-AML controls, procedures, technology requirements, typology catalogues, data models, and maturity claims SHALL be interpreted consistently with this document. Where a subordinate implementation creates tension with these goals or non-goals, the goals and boundaries in this document SHALL prevail unless the framework is formally revised.

> **Design axiom**  
> A more mature CS-AML implementation is not one that sees more people. It is one that produces better-supported, more proportionate, more secure, and more decision-useful intelligence with clearer limits and stronger accountability.
