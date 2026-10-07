# CS-AML Control Implementation Guide v0.1

**Status:** Normative derivative / implementation baseline

## Purpose
This guide translates the CS-AML v0.1 minimum control catalogue into operational, testable controls.

## Control catalogue

### GOV-01 — Accountable ownership

**Family:** Governance

**Requirement:** Every case SHALL have an accountable owner.

**Risk addressed:** Prevent orphaned investigations, ambiguous authority, and decisions without a clearly responsible human.

**Primary roles:** Case owner; Investigation lead; Governance approver

**Implementation**
- Create a named Case Owner role at case opening.
- Record owner, deputy, approving manager, and review date in the Case Charter.
- Require transfer-of-ownership records when responsibility changes.
- Ensure the owner has authority to pause, narrow, escalate, or close the case.

**Evidence of operation**
- Case Charter
- Case register
- Ownership transfer log
- Gate approval records

**Assurance test**
- Sample open cases and verify a current owner is recorded.
- Compare ownership changes with audit events.
- Interview analysts to confirm decision authority is understood.

**Common failure modes**
- Cases assigned to teams rather than accountable persons.
- Owner listed but lacking authority.
- Ownership changes without recorded rationale.

### GOV-02 — Conflict control

**Family:** Governance

**Requirement:** Material conflicts SHALL be declared and managed.

**Risk addressed:** Protect analytical independence where personal, organisational, donor, political, financial, or partnership interests could influence investigation decisions.

**Primary roles:** All investigators; Case owner; Governance approver

**Implementation**
- Require conflict declarations at intake and before high-impact dissemination.
- Define recusal, secondary review, and transfer procedures.
- Record both actual and reasonably perceived conflicts.
- Do not disclose protected-source identity unnecessarily when assessing conflicts.

**Evidence of operation**
- Conflict declaration
- Conflict register
- Recusal/mitigation record
- Independent review sign-off

**Assurance test**
- Review a sample of high-impact cases for conflict declarations.
- Check declared conflicts against mitigation actions.
- Test whether conflicted reviewers were excluded from approvals.

**Common failure modes**
- No declaration process.
- Conflicts considered only after publication.
- Informal mitigation with no evidence.

### CAS-01 — Defined purpose

**Family:** Case Management

**Requirement:** Every case SHALL have a documented investigation question and scope.

**Risk addressed:** Prevent open-ended surveillance, mission creep, and evidence collection without a defined legitimate purpose.

**Primary roles:** Case owner; Analyst; Approver

**Implementation**
- Create an Investigation Charter before substantive collection.
- State the issue, question, subjects, time period, jurisdiction, inclusion/exclusion boundaries, intended outputs, and stop conditions.
- Record material scope changes and require re-approval when risk increases.

**Evidence of operation**
- Investigation Charter
- Scope-change record
- Investigation question
- Closure decision

**Assurance test**
- Verify each sampled case has a question framed without presuming guilt.
- Compare collected data with approved scope.
- Inspect scope changes after discovery of new subjects.

**Common failure modes**
- Question framed as an accusation.
- No geographic/time boundary.
- Collection expands without updated charter.

### CAS-02 — Gate approval

**Family:** Case Management

**Requirement:** High-risk cases SHALL pass defined lifecycle gates.

**Risk addressed:** Ensure increasing analytical, privacy, legal, reputational, and safety risk receives proportionate review before the case advances.

**Primary roles:** Case owner; Privacy/security reviewer; Independent approver

**Implementation**
- Apply G0-G6 stage gates defined in the Investigation Methodology.
- Define criteria for high-risk cases, including sensitive personal data, protected sources, high-impact allegations, vulnerable persons, and planned public attribution.
- Record gate decision, approver, conditions, and unresolved gaps.

**Evidence of operation**
- Gate checklist
- Approval record
- Risk review
- Conditions/waivers

**Assurance test**
- Trace sample cases through required gates.
- Confirm gate approvals predate the controlled action.
- Check that conditions were resolved or explicitly accepted.

**Common failure modes**
- Retroactive approvals.
- Same person self-approves high-impact gates.
- Gate used as paperwork only.

### SRC-01 — Provenance

**Family:** Sources

**Requirement:** Material sources SHALL have provenance metadata.

**Risk addressed:** Allow another analyst to determine where information originated, how it was obtained, when it was accessed, and whether it remains reproducible.

**Primary roles:** Collector; Analyst; Evidence custodian

**Implementation**
- Register every material source with source ID, origin, publisher/owner where known, access method, access time, URL/location, archival copy where appropriate, legal/access note, and handling classification.
- Preserve original context and avoid detached screenshots when a fuller record is available.

**Evidence of operation**
- Source register
- Archived copy
- Collection metadata
- Access/legal note

**Assurance test**
- Select material claims and trace them to registered sources.
- Verify URLs/locations and access dates are present.
- Check archived copy policy for mutable web content.

**Common failure modes**
- Screenshots with no URL/date.
- Copied text with no original context.
- Sources referenced only in analyst notes.

### SRC-02 — Reliability assessment

**Family:** Sources

**Requirement:** Material source reliability SHOULD be assessed separately from information credibility.

**Risk addressed:** Avoid treating a generally reputable source as proof that every item it contains is accurate, or dismissing useful information solely because the source is unfamiliar.

**Primary roles:** Analyst; Reviewer

**Implementation**
- Use the CS-AML source reliability scale A-F and information credibility scale 1-6 where material.
- Document rationale for ratings that materially influence an assessment.
- Reassess when corroboration or contradiction emerges.

**Evidence of operation**
- Source rating
- Credibility rating
- Rating rationale
- Reassessment history

**Assurance test**
- Check that source and information ratings are not conflated.
- Review whether high-impact claims rely on weak/unknown sources without corroboration.

**Common failure modes**
- Everything from official sources marked A1 automatically.
- Anonymous source treated as unreliable without assessing the information.

### EVD-01 — Integrity

**Family:** Evidence

**Requirement:** Critical digital evidence SHOULD be integrity-protected.

**Risk addressed:** Preserve the ability to demonstrate that critical digital material has not silently changed since collection.

**Primary roles:** Evidence custodian; Collector; Security administrator

**Implementation**
- Preserve originals read-only where feasible.
- Compute cryptographic hashes for critical files at acquisition or entry into the evidence store.
- Record acquisition time, collector, source, and hash algorithm.
- Use derivative working copies rather than editing originals.

**Evidence of operation**
- Hash record
- Original evidence store
- Acquisition log
- Read-only/immutability configuration

**Assurance test**
- Recompute hashes for a sample.
- Confirm analyst work occurs on derivatives.
- Check that replaced files create new versions rather than overwriting originals.

**Common failure modes**
- Original PDFs annotated directly.
- No distinction between original and working copy.
- Hashes calculated only at case closure.

### EVD-02 — Derivative lineage

**Family:** Evidence

**Requirement:** Derived artefacts SHALL link to their originals.

**Risk addressed:** Ensure extracts, translations, cropped images, parsed tables, OCR text, and analyst-created datasets remain traceable to the source evidence from which they were produced.

**Primary roles:** Analyst; Evidence custodian

**Implementation**
- Assign IDs to derivative artefacts.
- Record parent evidence reference, transformation type, tool/version when material, creator, and creation time.
- Do not replace original wording with corrected or translated text without retaining both.

**Evidence of operation**
- Evidence lineage
- Derivative metadata
- Transformation log

**Assurance test**
- Trace sample extracts backward to originals.
- Check translations retain source text and translator/method metadata.

**Common failure modes**
- Orphan spreadsheets.
- OCR text treated as original.
- Translated quotes without source-language text.

### ENT-01 — Evidence-based resolution

**Family:** Entities

**Requirement:** Material entity merges SHALL be evidence-based and reversible.

**Risk addressed:** Prevent false network connections caused by prematurely treating similar names, addresses, identifiers, or profiles as the same person or organisation.

**Primary roles:** Analyst; Entity reviewer; Data steward

**Implementation**
- Maintain candidate-match state before merge.
- Record match features, conflicting features, confidence, analyst rationale, and evidence references.
- Support unmerge or superseding decisions without losing history.
- Do not merge solely on common names.

**Evidence of operation**
- Entity-resolution decision
- Merge history
- Candidate match record
- Evidence links

**Assurance test**
- Review merged high-impact entities and verify multiple discriminating attributes.
- Test reversibility.
- Search for merges based only on name.

**Common failure modes**
- One-record-per-name logic.
- Hidden merges.
- Merged entity loses alternate identifiers/provenance.

### REL-01 — Relationship proof

**Family:** Relationships

**Requirement:** Material analytical relationships SHALL link to evidence and carry temporal/confidence metadata.

**Risk addressed:** Prevent visual graph edges from being mistaken for established relationships merely because they appear connected.

**Primary roles:** Analyst; Graph/data steward

**Implementation**
- Represent relationships as first-class records, not display-only edges.
- Record relationship type, endpoints, source/evidence, valid time where known, confidence, status, and analyst.
- Use controlled vocabulary.
- Distinguish asserted, observed, inferred, and disputed relationships where needed.

**Evidence of operation**
- Relationship record
- Edge provenance
- Graph audit
- Confidence metadata

**Assurance test**
- Click/trace sample material graph edges to evidence.
- Check historical relationships include valid time.
- Look for unsupported edges created manually in visualisation.

**Common failure modes**
- Graph edge with no provenance.
- Current director relationship shown as timeless.
- Association inferred from co-occurrence only.

### AST-01 — Attribution distinction

**Family:** Assets

**Requirement:** Legal ownership, beneficial ownership, control, use, and association SHALL be represented distinctly.

**Risk addressed:** Avoid overstating that a subject owns an asset merely because they use, control, finance, occupy, or are associated with it.

**Primary roles:** Analyst; Reviewer; Legal/editorial reviewer where applicable

**Implementation**
- Use separate relationship types for legal title, beneficial interest, control, use/occupancy, financing, and association.
- Record valuation source/date and uncertainty separately from ownership.
- Require stronger review before public statements of beneficial ownership.

**Evidence of operation**
- Asset record
- Ownership/control records
- Valuation provenance
- Assessment wording

**Assurance test**
- Compare graph labels with underlying attribution type.
- Review publications for language stronger than recorded evidence.

**Common failure modes**
- “Associated with” converted to “owns”.
- Asset value presented without date/source.
- Beneficial ownership inferred solely from family relationship.

### VAL-01 — Flow epistemic status

**Family:** Value Flow

**Requirement:** Direct, documented, reconstructed, and hypothetical value flows SHALL be distinguished.

**Risk addressed:** Prevent analytical reconstruction from being presented as if it were a known bank transaction or verified transfer.

**Primary roles:** Analyst; Reviewer; UI/data owner

**Implementation**
- Set flow_class on every material ValueFlow.
- DIRECT requires direct transaction-level evidence; DOCUMENTED requires reliable documentation of the transfer/value movement; RECONSTRUCTED represents analytical linkage from multiple facts; HYPOTHETICAL is a scenario for testing only.
- Use distinct visual styling and narrative language for each class.
- Record amount/date uncertainty explicitly.

**Evidence of operation**
- ValueFlow record
- Flow-class field
- Evidence links
- Visualisation legend

**Assurance test**
- Sample flows and verify classification against evidence.
- Check reports/graphs preserve class distinction.
- Review whether hypothetical flows leaked into findings.

**Common failure modes**
- All arrows look identical.
- Reconstructed contract-to-asset chain called a transfer.
- Estimated values displayed as exact.

### TYP-01 — Typology caution

**Family:** Typologies

**Requirement:** A typology match SHALL NOT be treated as proof of money laundering or predicate crime.

**Risk addressed:** Use typologies as structured analytical lenses without converting pattern similarity into a determination of wrongdoing.

**Primary roles:** Analyst; Peer reviewer

**Implementation**
- Use the CS-AML Typology Catalogue entry ID and indicator classes.
- Record supporting, contextual, disconfirming indicators and intelligence gaps.
- Require corroboration before assessments above Plausible consistency unless direct authoritative evidence establishes the mechanism.
- Document legitimate alternative explanations.

**Evidence of operation**
- Typology worksheet
- Indicator map
- Alternative explanation
- Assessment language

**Assurance test**
- Review a sample of typology matches for disconfirming indicators.
- Search products for deterministic phrases unsupported by adjudicated facts.

**Common failure modes**
- Single red flag equals typology match.
- Typology label used as allegation.
- No alternatives considered.

### HYP-01 — Competing explanations

**Family:** Hypotheses

**Requirement:** Material investigations SHOULD maintain plausible competing hypotheses.

**Risk addressed:** Reduce confirmation bias and make analytical reasoning explicit, testable, and reviewable.

**Primary roles:** Analyst; Peer reviewer

**Implementation**
- Create hypothesis records with supporting, contradicting, and unknown evidence.
- Include a legitimate/non-criminal explanation where plausible.
- Update status as evidence changes.
- Avoid deleting rejected hypotheses; retain decision history.

**Evidence of operation**
- Hypothesis matrix
- Status history
- Evidence links

**Assurance test**
- Check high-impact cases for more than one plausible hypothesis.
- Verify rejected hypotheses show rationale.

**Common failure modes**
- Only inculpatory hypothesis exists.
- Hypothesis rewritten after evidence arrives to appear correct.

### HYP-02 — Disconfirmation

**Family:** Hypotheses

**Requirement:** High-impact adverse findings SHALL document reasonable efforts to find disconfirming evidence.

**Risk addressed:** Prevent strong conclusions from being produced solely by accumulating confirmatory material.

**Primary roles:** Lead analyst; Independent reviewer

**Implementation**
- Define what evidence would weaken or falsify each material hypothesis.
- Perform targeted searches for legitimate explanations, contradictory records, timing inconsistencies, identity mismatches, and alternative controllers/owners.
- Record searches even when no disconfirming evidence is found.

**Evidence of operation**
- Disconfirmation log
- Search notes
- Hypothesis matrix
- Peer-review checklist

**Assurance test**
- Inspect high-impact findings for explicit disconfirmation actions.
- Assess whether searches were meaningful rather than ceremonial.

**Common failure modes**
- “No contradiction found” with no search record.
- Only sources likely to confirm the hypothesis are used.

### ASM-01 — Confidence statement

**Family:** Assessment

**Requirement:** Material assessments SHALL carry an explicit confidence level and basis.

**Risk addressed:** Communicate the strength and limitations of analytical judgments so readers do not interpret all findings as equally certain.

**Primary roles:** Analyst; Reviewer

**Implementation**
- Use controlled confidence levels (e.g., Low/Moderate/High) with documented basis.
- Base confidence on evidence quality, corroboration, inference distance, unresolved contradictions, and intelligence gaps—not merely number of sources.
- Separate confidence in identity, relationship, flow, typology, and overall judgment where materially different.

**Evidence of operation**
- Assessment record
- Confidence rationale
- Evidence matrix

**Assurance test**
- Compare confidence level with source quality and gaps.
- Check for high confidence despite unresolved identity or provenance issues.

**Common failure modes**
- Numeric score with no explanation.
- High confidence because many articles repeat the same claim.

### GAP-01 — Explicit unknowns

**Family:** Assessment

**Requirement:** Material intelligence gaps SHALL be explicit and linked to affected judgments.

**Risk addressed:** Make clear what is not known and prevent absence of data from being mistaken for evidence of absence.

**Primary roles:** Analyst; Reviewer

**Implementation**
- Maintain a gap register with gap description, impact, priority, possible collection path, legal/ethical constraints, and status.
- Link gaps to hypotheses, assessments, or value flows they affect.
- Carry critical unresolved gaps into intelligence products.

**Evidence of operation**
- Intelligence Gap Register
- Assessment limitations
- Collection plan

**Assurance test**
- Select key judgments and verify critical unknowns are visible.
- Check closed gaps have supporting evidence.

**Common failure modes**
- Unknown source of funds omitted.
- Bank data unavailable but flow written as complete.

### PRI-01 — Data minimisation

**Family:** Privacy

**Requirement:** Sensitive personal data SHALL be necessary, proportionate, and relevant to an approved investigation purpose.

**Risk addressed:** Limit harm, legal exposure, and surveillance creep by collecting only data that materially serves the investigation.

**Primary roles:** Case owner; Privacy reviewer; Collector

**Implementation**
- Apply necessity/relevance test before collecting or retaining sensitive data.
- Document justification for special-category/sensitive financial or protected-source information.
- Avoid collecting relatives, associates, contacts, or location history merely because technically available.
- Use redaction/pseudonymisation where identity is not required.

**Evidence of operation**
- Collection decision
- Privacy review
- Data inventory
- Redaction record

**Assurance test**
- Compare collected sensitive fields with case purpose.
- Sample unrelated persons for documented necessity.
- Check bulk imports for minimisation controls.

**Common failure modes**
- “May be useful later” as sole justification.
- Whole datasets retained when only a few records are relevant.

### PRI-02 — Retention and disposition

**Family:** Privacy

**Requirement:** Sensitive data SHALL have retention, review, and disposition rules.

**Risk addressed:** Prevent indefinite accumulation of personal data and ensure closed-case material is retained only for justified periods.

**Primary roles:** Data steward; Privacy reviewer; Evidence custodian

**Implementation**
- Assign retention class at ingestion or case association.
- Define review triggers, legal holds, archival criteria, deletion/anonymisation methods, and exceptions.
- Log destruction or irreversible anonymisation.
- Protect evidence that must be preserved from premature deletion.

**Evidence of operation**
- Retention schedule
- Disposition log
- Legal hold record
- Retention review

**Assurance test**
- Identify expired items and verify disposition occurred.
- Review exceptions for approvals and reasons.

**Common failure modes**
- Everything retained indefinitely.
- Manual deletion with no audit.
- Retention policy exists but no job/workflow implements it.

### SEC-01 — Least privilege

**Family:** Security

**Requirement:** Access SHALL be role- and need-based.

**Risk addressed:** Reduce insider risk and unnecessary exposure of sensitive case, source, and personal data.

**Primary roles:** Security administrator; Case owner; Data owner

**Implementation**
- Define roles and data-access attributes.
- Separate ordinary case access from protected-source identity, highly sensitive evidence, and dissemination authority.
- Review access periodically and on role change.
- Use strong authentication and log privileged actions.

**Evidence of operation**
- Access-control matrix
- IAM configuration
- Access review
- Privileged audit log

**Assurance test**
- Sample users and compare permissions with role.
- Test terminated/transferred users.
- Review dormant privileged accounts.

**Common failure modes**
- All investigators are administrators.
- Shared accounts.
- Case access never expires.

### SEC-02 — Protected-source compartmentalisation

**Family:** Security

**Requirement:** Protected source identities SHALL be compartmentalised from ordinary case material.

**Risk addressed:** Reduce risk that compromise, sharing, publication, or broad team access reveals whistleblowers or confidential informants.

**Primary roles:** Source handler; Security administrator; Case owner

**Implementation**
- Use source aliases in general case records.
- Store identifying data in a restricted compartment with separate permissions.
- Minimise cross-links that expose identity.
- Define controlled re-identification process and emergency disclosure rules.

**Evidence of operation**
- Restricted source store
- Alias mapping
- Access log
- Re-identification approval

**Assurance test**
- Verify ordinary analysts cannot retrieve source identity without authorisation.
- Check exports/publication packages for leakage.

**Common failure modes**
- Source name embedded in filenames.
- Identity repeated in notes and chat.
- Alias mapping stored beside public product.

### QUA-01 — Independent peer review

**Family:** Quality

**Requirement:** High-impact products SHALL be independently reviewed before external dissemination.

**Risk addressed:** Detect analytical error, unsupported inference, overstatement, privacy harm, and inconsistent application of the framework.

**Primary roles:** Peer reviewer; Approver; Lead analyst

**Implementation**
- Define high-impact criteria.
- Reviewer SHALL be sufficiently independent from primary analysis.
- Review provenance, entity resolution, key relationships, flow classification, typology use, alternatives, confidence, gaps, privacy, and wording.
- Material reviewer disagreements SHALL be resolved or recorded.

**Evidence of operation**
- Peer-review form
- Reviewer comments
- Resolution log
- Approval record

**Assurance test**
- Reperform selected key judgments from evidence.
- Check reviewer independence and timing.
- Verify disagreements were not silently removed.

**Common failure modes**
- Copy-editing mistaken for analytical review.
- Reviewer approves without evidence access.

### DIS-01 — Handling and approval

**Family:** Dissemination

**Requirement:** External dissemination SHALL have classification, audience, purpose, and approval recorded.

**Risk addressed:** Prevent intelligence products from reaching audiences that lack need, context, legal basis, or adequate handling capability.

**Primary roles:** Product owner; Approver; Security/privacy reviewer

**Implementation**
- Classify product and define intended audience/use.
- Apply redaction, minimisation, source protection, and caveats appropriate to recipient.
- Record approval, recipient, date, version, transfer method, and restrictions.
- Create separate referral and public versions where necessary.

**Evidence of operation**
- Dissemination log
- Approved product version
- Recipient restrictions
- Transfer record

**Assurance test**
- Match sent files to approved hashes/versions.
- Verify recipients and restrictions.
- Check whether superseded drafts were shared.

**Common failure modes**
- Emailing working files.
- No record of who received which version.
- Same product sent to FIU and published publicly.

### AUD-01 — Material change auditability

**Family:** Audit

**Requirement:** Material analytical and evidentiary changes SHOULD be logged.

**Risk addressed:** Allow reconstruction of how the case changed and who made decisions affecting findings.

**Primary roles:** System owner; Security; Assurance reviewer

**Implementation**
- Audit creation/update/deletion/merge/unmerge of material entities, evidence metadata, relationships, hypotheses, assessments, approvals, dissemination, and access to highly sensitive records.
- Protect logs from routine user alteration.
- Synchronise time sources where practical.

**Evidence of operation**
- Audit trail
- Version history
- Log-retention policy
- Integrity monitoring

**Assurance test**
- Trace a sample material change end-to-end.
- Check logs identify actor, time, object, action, and previous/new state where required.

**Common failure modes**
- Only login events logged.
- Analysts can edit audit logs.
- No history after entity merge.

### TEC-01 — AI verification

**Family:** Technology

**Requirement:** AI-generated material SHALL NOT become a material fact without human verification against authoritative or primary evidence.

**Risk addressed:** Prevent hallucinated, decontextualised, or misattributed model output from contaminating evidentiary records and assessments.

**Primary roles:** Analyst; Technology owner; Reviewer

**Implementation**
- Label AI-assisted outputs.
- Require source-level human verification before promotion to Claim/Fact.
- Do not permit generative summaries to overwrite original evidence.
- Record model/tool use when material to reproducibility.
- Apply stricter controls to identity resolution, allegation drafting, translation, and extraction from sensitive records.

**Evidence of operation**
- AI-use record
- Verification record
- Source links
- Prompt/output retention where policy permits

**Assurance test**
- Sample AI-assisted facts and reproduce verification.
- Search for facts whose only provenance is an AI output.

**Common failure modes**
- LLM answer cited as source.
- AI confidence treated as analytical confidence.
- Unverified OCR/translation promoted to fact.

### TEC-02 — Explainable automation

**Family:** Technology

**Requirement:** Automated scores or models used materially SHOULD be explainable and governed.

**Risk addressed:** Ensure risk scores, entity matching, anomaly flags, and typology ranking can be understood, challenged, validated, and changed.

**Primary roles:** Model owner; Analyst; Independent validator

**Implementation**
- Document purpose, input features/data, output meaning, thresholds, version, known limitations, owner, validation status, and override process.
- Do not use a score as a substitute for assessment.
- Monitor drift and false positives where outcomes are available.

**Evidence of operation**
- Model/rule card
- Validation record
- Threshold rationale
- Override log
- Performance metrics

**Assurance test**
- Select material automated outcomes and explain why they occurred.
- Check model version used at decision time.
- Review overrides for patterns.

**Common failure modes**
- Black-box score with no feature explanation.
- Threshold chosen only to reduce workload.
- Model changes without versioning.

