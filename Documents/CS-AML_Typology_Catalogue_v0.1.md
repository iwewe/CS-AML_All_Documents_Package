**CS-AML TYPOLOGY CATALOGUE**

Civil Society Financial Intelligence / AML Investigation

**Version 0.1 \| Normative Typology Standard**

> **Purpose**
>
> This catalogue provides a controlled vocabulary and analytical standard for identifying, documenting, testing, and communicating money-laundering typologies using lawful civil-society information. A typology match is an analytical lead, not a finding of criminal liability.

**Status: Baseline v0.1**

Intended users: CSOs, investigative journalists, anti-corruption researchers, public-interest investigators, and partner analysts.

# Document Control

|  |  |
|----|----|
| Document | CS-AML Typology Catalogue |
| Version | 0.1 |
| Status | Normative derivative / baseline catalogue |
| Parent framework | CS-AML Framework v0.1 |
| Normative terms | SHALL/MUST = mandatory; SHOULD = recommended; MAY = optional |
| Review cycle | At least annually, and upon material typology or legal change |
| Primary orientation | Civil-society financial intelligence using lawful and proportionate sources |
| Exclusions | No covert financial surveillance, unauthorized access, or criminal-liability determination |

# 0. Normative Position

The CS-AML Typology Catalogue is a controlled analytical reference for the CS-AML Framework. It does not create legal presumptions. It standardises how typologies are described, observed, tested, compared, and cited within civil-society financial intelligence products.

**REQUIREMENT —** An analyst SHALL NOT label a person, entity, transaction, asset, or relationship as money laundering solely because one or more catalogue indicators are present.

**REQUIREMENT —** A typology assessment SHALL distinguish observed facts from inference, and SHALL record alternative legitimate explanations where reasonably available.

**REQUIREMENT —** A typology match SHALL be traceable to evidence and provenance. Generic risk factors alone are insufficient.

**REQUIREMENT —** Where the available information cannot establish a financial flow directly, the analyst SHALL label any reconstructed flow as inferred or reconstructed.

# 1. Purpose and Objectives

- The catalogue provides a common typology language across CS-AML investigations, enabling consistent analysis across cases and organisations.

- It converts broad AML concepts into observable analytical patterns suitable for civil-society work, where access to private banking records is normally unavailable.

- It provides evidentiary guardrails so that red flags remain leads rather than accusations.

- It supports technology implementation by defining stable typology IDs, required fields, indicator structures, confidence rules, and review metadata.

# 2. Core Definitions

| **Term** | **Normative definition** |
|----|----|
| Typology | A recurring method, structure, mechanism, or pattern through which illicit value may be concealed, moved, transformed, controlled, or integrated. |
| Mechanism | The operational means by which the typology functions, such as use of shell companies, false invoicing, nominee ownership, or conversion to assets. |
| Indicator | An observed fact or pattern that is relevant to a typology but is not sufficient on its own to establish that typology. |
| Red flag | An indicator that warrants increased scrutiny because it is associated with known financial-crime risks. |
| Observable | Information that a civil-society investigator may lawfully encounter or derive from public, consensual, published, or otherwise authorised sources. |
| Direct financial flow | A transfer of value evidenced by a reliable record that directly records sender/origin, recipient/destination, amount/value, and transaction or transfer event. |
| Reconstructed value flow | An analytically inferred movement or transformation of value supported by multiple events, contracts, ownership records, assets, or other evidence, but lacking direct transactional proof. |
| Typology match | An analytical judgement that observed facts are consistent with a defined typology to a stated confidence level. It is not a finding of criminal conduct. |
| Alternative explanation | A reasonably plausible lawful or non-criminal explanation for the observed facts. |
| Disconfirming evidence | Evidence that weakens or contradicts a typology hypothesis. |

# 3. Catalogue Taxonomy

Typologies are grouped by the primary laundering function they perform. A real case MAY involve multiple typologies simultaneously; analysts SHOULD therefore treat the catalogue as composable rather than mutually exclusive.

| **Family** | **Name** | **Primary analytical focus** |
|----|----|----|
| A | Ownership & Control Concealment | Hide the person who owns, controls, benefits from, or directs property or legal entities. |
| B | Layering & Movement | Fragment, route, circulate, settle, or reposition value to make provenance harder to trace. |
| C | Business, Trade & Contract Abuse | Embed illicit value in apparently legitimate commercial, procurement, trade, or corporate activity. |
| D | Asset Conversion & Integration | Convert or integrate value into property, luxury goods, businesses, investments, or other stores of value. |
| E | Professional & Network Facilitation | Use intermediaries, laundering networks, money mules, or alternative settlement mechanisms. |
| F | Digital & Cross-Border Channels | Exploit virtual assets, digital payment systems, cyber-enabled fraud ecosystems, or jurisdictional distance. |

# 4. Typology Assessment Standard

Every typology analysis SHALL record the status of relevant indicators using the following controlled values: OBSERVED, PARTIALLY OBSERVED, NOT OBSERVED, UNKNOWN, or NOT APPLICABLE.

| **Assessment** | **Minimum analytical meaning** |
|----|----|
| No analytical basis | No mechanism-specific indicator supported by reliable evidence. |
| Weak consistency | One or more generic indicators are present, but no mechanism-specific pattern is adequately corroborated. |
| Plausible consistency | At least one mechanism-specific indicator plus independent corroborating evidence; material gaps remain. |
| Strong consistency | Multiple mutually reinforcing mechanism-specific indicators, independently supported, with alternative explanations assessed and materially weakened. |
| Compelling consistency | Direct or authoritative evidence establishes the mechanism or value movement and is corroborated by additional evidence. This still does not determine criminal liability. |

**MINIMUM RULE —** Except where direct authoritative evidence establishes the mechanism, an analyst SHALL NOT assess a typology above “Plausible consistency” on the basis of a single indicator or a single source.

# 5. Indicator Classes

| **Class** | **Name** | **Use** |
|----|----|----|
| M | Mechanism-specific | Directly reflects how the typology operates; highest analytical weight. |
| C | Corroborating | Supports a mechanism-specific indicator through an independent fact, relationship, event, or source. |
| K | Contextual | Raises or lowers plausibility but is not specific enough to support a typology on its own. |
| D | Disconfirming | Contradicts, weakens, or provides a more credible alternative explanation. |
| G | Gap | Material information that is missing and limits confidence. |

# 6. Typology Index

| **ID** | **Typology** | **Family** | **Primary function** |
|----|----|----|----|
| CSAML-TYP-A01 | Concealment Through Shell, Shelf, or Low-Substance Companies | A | Separate apparent legal ownership from the person who ultimately controls or benefits from value, while c… |
| CSAML-TYP-A02 | Nominee, Proxy, or Straw Ownership and Control | A | Place legal title or formal authority in another person while control, benefit, or decision-making remain… |
| CSAML-TYP-B01 | Structuring, Smurfing, and Deliberate Fragmentation | B | Break a larger amount or activity into smaller units to reduce visibility, avoid controls, or obscure lin… |
| CSAML-TYP-B02 | Circular Flow, Round-Tripping, and Self-Returning Value | B | Move value through a chain and return it to the same economic controller, creating apparent distance, rev… |
| CSAML-TYP-B03 | Rapid Pass-Through and Layered Onward Movement | B | Minimise the time value remains with an intermediary and rapidly increase transactional distance from ori… |
| CSAML-TYP-C01 | Cash-Intensive Business Commingling | C | Blend illicit cash or value with legitimate business revenue so that proceeds appear to arise from normal… |
| CSAML-TYP-C02 | Trade-Based Money Laundering (TBML) | C | Move or disguise value through trade transactions by manipulating price, quantity, quality, description, … |
| CSAML-TYP-C03 | Procurement and Contract Value Diversion | C | Convert public, donor, corporate, or project expenditure into private benefit and then obscure or integra… |
| CSAML-TYP-C04 | Sham Loans, Loan-Back, and Fictitious Debt | C | Give illicit or undisclosed value the appearance of legitimate financing, repayment, or debt settlement.… |
| CSAML-TYP-D01 | Real Estate Acquisition, Transfer, and Value Storage | D | Store, transform, or integrate value in real property, including through ownership layers, financing, ren… |
| CSAML-TYP-D02 | Luxury Goods, Precious Metals/Stones, Art, Vehicles, and Portable Stores of Value | D | Convert proceeds into movable, durable, high-value assets that can store, transport, transfer, or resell … |
| CSAML-TYP-E01 | Professional Money Laundering Networks | E | Provide laundering as a service to one or more criminal clients through specialised roles, infrastructure… |
| CSAML-TYP-E02 | Money Mule, Collector, Funnel, and Consolidation Networks | E | Receive funds through distributed accounts/persons and consolidate or forward value to reduce direct link… |
| CSAML-TYP-E03 | Underground Banking, Hawala, and Alternative Settlement | E | Transfer or settle value outside conventional bank-to-bank movement, often through brokers, offsetting ob… |
| CSAML-TYP-F01 | Virtual Asset Conversion, Layering, and Obfuscation | F | Move or transform value through virtual assets, services, wallets, bridges, mixers, privacy features, or … |
| CSAML-TYP-F02 | Cyber-Enabled Fraud Proceeds Laundering | F | Receive, disperse, convert, and cash out proceeds generated by scams, BEC, account takeover, investment f… |
| CSAML-TYP-F03 | Cross-Border Cash and Physical Value Movement | F | Move illicit value physically across borders or locations using currency, bearer instruments, precious it… |
| CSAML-TYP-F04 | Digital Payment and Fintech Layering | F | Exploit e-money, payment service providers, prepaid instruments, merchant accounts, or fast digital payme… |
| CSAML-TYP-D03 | Gambling, Gaming, and Betting-Based Value Conversion | D | Use gambling or gaming systems to commingle, transfer, convert, or re-characterise funds as winnings, bal… |
| CSAML-TYP-C05 | Environmental and Natural-Resource Crime Proceeds Laundering | C | Monetise and integrate proceeds from illegal extraction, logging, mining, wildlife, fisheries, waste, or … |

**CSAML-TYP-A01**

# Concealment Through Shell, Shelf, or Low-Substance Companies

**Family:** A — Ownership & Control Concealment

> **Criminal / concealment objective**
>
> Separate apparent legal ownership from the person who ultimately controls or benefits from value, while creating layers of corporate distance.

## Mechanism model

- Create or acquire one or more legal entities with limited observable operations.

- Route ownership, contracts, assets, or payments through those entities.

- Use the legal entity as a holder, pass-through vehicle, contracting party, or account owner.

- Preserve plausible legitimacy through registration, professional services, or routine corporate documentation.

## Civil-society observables

- Corporate registry records and beneficial-ownership declarations.

- Repeated registered addresses, directors, commissioners, shareholders, company secretaries, or contact details.

- Minimal operational footprint relative to assets, contracts, or transaction value described in public records.

- Rapid creation, transfer, dormancy, or dissolution around economically significant events.

- Cross-jurisdiction structures without a clear operational rationale.

## Indicator set

| **Class** | **Indicator** |
|----|----|
| M | Entity holds significant assets/contracts while showing little observable operating substance. |
| M | Multiple layers of legal entities separate the relevant person from ownership/control. |
| C | Common directors, addresses, agents, or contact points connect nominally separate entities. |
| C | Entity formation or ownership change is temporally close to a contract, asset acquisition, or legal event. |
| K | Use of jurisdictions or service providers associated with corporate structuring. |
| D | Documented legitimate group structure, staffing, operations, tax/business rationale, and independent counterparties support ordinary commercial purpose. |

## Minimum analytical questions

- What legitimate commercial function does each legal entity perform?

- Who ultimately controls decisions, bankable assets, contracts, or disposal rights?

- Which relationships are legal ownership, beneficial ownership, control, agency, or merely association?

- Is the structure older than the suspicious event or was it assembled around it?

## False-positive / alternative-explanation cautions

- Shell or special-purpose companies can have legitimate purposes.

- Shared addresses and professional agents are common in ordinary corporate administration.

## Useful evidence classes

- Company registry / AHU or equivalent

- Beneficial ownership records

- Annual reports / filings

- Procurement and contract records

- Court records

- Company websites and archived web material

## Assessment rule for this typology

The analyst SHALL document which mechanism-specific indicators are observed, which independent evidence corroborates them, which disconfirming facts were considered, and which intelligence gaps materially limit confidence. The typology SHALL NOT be treated as established solely because contextual risk factors are present.

## Primary reference lineage

- FATF-Egmont, Concealment of Beneficial Ownership (2018)

- FATF Guidance on Beneficial Ownership of Legal Persons (2023)

**CSAML-TYP-A02**

# Nominee, Proxy, or Straw Ownership and Control

**Family:** A — Ownership & Control Concealment

> **Criminal / concealment objective**
>
> Place legal title or formal authority in another person while control, benefit, or decision-making remains elsewhere.

## Mechanism model

- Use relatives, employees, associates, service providers, or other proxies as formal owners/directors.

- Maintain informal control through financing, instructions, asset use, contractual rights, or personal relationships.

- Transfer legal title without materially changing practical control.

## Civil-society observables

- Disparity between formal owner and person who appears to use, finance, manage, or benefit from the asset/entity.

- Repeated appointment of close associates across connected companies.

- Ownership changes among connected persons without evident economic rationale.

- Public statements, court records, or contracts indicating control inconsistent with formal title.

## Indicator set

| **Class** | **Indicator** |
|----|----|
| M | Documented divergence between legal ownership and practical control/benefit. |
| M | Proxy lacks plausible economic capacity while another person funds, uses, or directs the asset/entity. |
| C | Close personal, employment, family, or business relationship connects nominee and suspected controller. |
| C | Ownership changes preserve the same practical user, address, manager, or financing source. |
| D | Independent financing, management, and benefit by the registered owner are well documented. |

## Minimum analytical questions

- Who paid for acquisition, operating costs, debt service, or maintenance?

- Who can sell, encumber, direct, or economically benefit?

- Does the formal owner have independent capacity and decision-making?

## False-positive / alternative-explanation cautions

- Family ownership and delegated management are common legitimate arrangements.

- Control cannot be inferred from relationship alone.

## Useful evidence classes

- Ownership records

- Asset records

- Financing documents if lawfully available

- Court findings

- Public declarations

- Corporate management history

## Assessment rule for this typology

The analyst SHALL document which mechanism-specific indicators are observed, which independent evidence corroborates them, which disconfirming facts were considered, and which intelligence gaps materially limit confidence. The typology SHALL NOT be treated as established solely because contextual risk factors are present.

## Primary reference lineage

- FATF-Egmont, Concealment of Beneficial Ownership (2018)

- FATF Beneficial Ownership guidance

**CSAML-TYP-B01**

# Structuring, Smurfing, and Deliberate Fragmentation

**Family:** B — Layering & Movement

> **Criminal / concealment objective**
>
> Break a larger amount or activity into smaller units to reduce visibility, avoid controls, or obscure linkage.

## Mechanism model

- Split deposits, payments, purchases, transfers, or ownership interests across time, entities, persons, or instruments.

- Use multiple participants or accounts to fragment the apparent source or destination.

- Recombine value later through consolidation, asset purchase, or onward transfer.

## Civil-society observables

- Series of similarly sized transactions or purchases just below relevant thresholds where lawfully observable.

- Multiple related entities or persons making coordinated payments or acquisitions.

- Rapid consolidation after fragmentation.

- Repeated structured invoices, donations, or transfers without commercial explanation.

## Indicator set

| **Class** | **Indicator** |
|----|----|
| M | Fragmentation is followed by recombination into a common beneficiary, asset, or controller. |
| M | Transaction or event pattern clusters closely below a known threshold or control point. |
| C | Participants share address, employer, device, contact, controller, or other relationship. |
| K | High cash intensity or repeated small-value activity. |
| D | Business model naturally produces high-volume small transactions with independently supported commercial purpose. |

## Minimum analytical questions

- What threshold or control would fragmentation plausibly avoid?

- Do the fragments converge to a common beneficiary or purpose?

- Are participants independent?

## False-positive / alternative-explanation cautions

- Small-value repetitive transactions are common in retail, fundraising, payroll, and remittance contexts.

## Useful evidence classes

- Court cases

- Published transaction records

- Procurement/payment data

- Asset purchase records

- Corporate relationships

## Assessment rule for this typology

The analyst SHALL document which mechanism-specific indicators are observed, which independent evidence corroborates them, which disconfirming facts were considered, and which intelligence gaps materially limit confidence. The typology SHALL NOT be treated as established solely because contextual risk factors are present.

## Primary reference lineage

- APG Yearly Typologies Reports

- FATF Professional Money Laundering (2018)

**CSAML-TYP-B02**

# Circular Flow, Round-Tripping, and Self-Returning Value

**Family:** B — Layering & Movement

> **Criminal / concealment objective**
>
> Move value through a chain and return it to the same economic controller, creating apparent distance, revenue, investment, debt repayment, or legitimacy.

## Mechanism model

- Transfer value through related entities, jurisdictions, counterparties, or instruments.

- Change legal form or transaction label along the route.

- Return equivalent value to the originating controller or related asset.

## Civil-society observables

- Circular corporate ownership, recurring reciprocal contracts, mirrored loans, investments, or payments.

- Same or related persons appear at both origin and endpoint of a value chain.

- Assets or funds leave and re-enter through a nominally independent entity.

## Indicator set

| **Class** | **Indicator** |
|----|----|
| M | Economic value demonstrably returns to the same controller or closely related entity after intermediate steps. |
| C | Intermediate entities have weak independent commercial rationale. |
| C | Amounts/timing are closely matched across outward and inward legs. |
| D | Independent market transactions, arm’s-length pricing, and distinct beneficial owners are supported. |

## Minimum analytical questions

- Who is the ultimate economic beneficiary at the end of the cycle?

- What independent economic purpose exists for each leg?

- Is value identical, approximately matched, or transformed?

## False-positive / alternative-explanation cautions

- Legitimate group treasury, intercompany finance, supply chains, and investment structures can create circular-looking flows.

## Useful evidence classes

- Corporate ownership data

- Loan/investment documents

- Court records

- Trade and contract records

- Public financial statements

## Assessment rule for this typology

The analyst SHALL document which mechanism-specific indicators are observed, which independent evidence corroborates them, which disconfirming facts were considered, and which intelligence gaps materially limit confidence. The typology SHALL NOT be treated as established solely because contextual risk factors are present.

## Primary reference lineage

- FATF Methods and Trends

- APG typologies case studies

**CSAML-TYP-B03**

# Rapid Pass-Through and Layered Onward Movement

**Family:** B — Layering & Movement

> **Criminal / concealment objective**
>
> Minimise the time value remains with an intermediary and rapidly increase transactional distance from origin.

## Mechanism model

- Receive value and quickly transfer, convert, withdraw, purchase, or route it onward.

- Use multiple accounts/entities/wallets as short-lived pass-through points.

- Repeat across several layers or jurisdictions.

## Civil-society observables

- Court or case records describe near-immediate onward transfers.

- Entities receive significant value without observable business reason and soon dispose/transfer related value.

- Short-lived companies or wallets appear primarily in routing roles.

## Indicator set

| **Class** | **Indicator** |
|----|----|
| M | Substantial incoming value is followed by closely timed outward movement with limited retention. |
| C | Pass-through entity lacks observable economic role or margin consistent with the movement. |
| C | Repeated use of the same routing pattern across cases. |
| D | Escrow, settlement, payment processing, agency, marketplace, or treasury function explains rapid movement. |

## Minimum analytical questions

- What is the intermediary’s legitimate economic function?

- How much value is retained and why?

- Does the timing recur systematically?

## False-positive / alternative-explanation cautions

- Payment processors, marketplaces, escrow agents, treasury centres, and brokers legitimately move funds quickly.

## Useful evidence classes

- Court records

- Published investigative records

- Financial statements

- Corporate role descriptions

- Lawfully obtained transaction documentation

## Assessment rule for this typology

The analyst SHALL document which mechanism-specific indicators are observed, which independent evidence corroborates them, which disconfirming facts were considered, and which intelligence gaps materially limit confidence. The typology SHALL NOT be treated as established solely because contextual risk factors are present.

## Primary reference lineage

- FATF Professional Money Laundering (2018)

- FATF cyber-enabled fraud paper (2026)

**CSAML-TYP-C01**

# Cash-Intensive Business Commingling

**Family:** C — Business, Trade & Contract Abuse

> **Criminal / concealment objective**
>
> Blend illicit cash or value with legitimate business revenue so that proceeds appear to arise from normal commerce.

## Mechanism model

- Use a business capable of plausible cash turnover.

- Record illicit cash as sales or receipts.

- Deposit, spend, invest, or distribute commingled value as business proceeds.

## Civil-society observables

- Declared business scale appears inconsistent with observable customer activity, premises, staffing, or market conditions.

- Unusual revenue growth without corresponding expansion.

- Multiple connected cash businesses with shared controllers.

## Indicator set

| **Class** | **Indicator** |
|----|----|
| M | Material mismatch between claimed cash revenue and observable business capacity. |
| C | Rapid asset accumulation or distributions unsupported by operating footprint. |
| C | Business has weak documentation of customers, inventory, or service delivery in records that are lawfully available. |
| D | Independent sales records, tax filings, market data, staffing, inventory, and operating evidence support revenue levels. |

## Minimum analytical questions

- What observable activity would generate the claimed revenue?

- Do costs, staffing, inventory, and customers scale with revenue?

## False-positive / alternative-explanation cautions

- Civil society usually lacks full accounting records; absence of visible activity is not proof of fictitious revenue.

## Useful evidence classes

- Corporate filings

- Tax/court records where public

- Licensing records

- Site observations conducted lawfully

- Media and archival material

## Assessment rule for this typology

The analyst SHALL document which mechanism-specific indicators are observed, which independent evidence corroborates them, which disconfirming facts were considered, and which intelligence gaps materially limit confidence. The typology SHALL NOT be treated as established solely because contextual risk factors are present.

## Primary reference lineage

- FATF-Egmont Concealment of Beneficial Ownership (front companies)

- FATF Professional Money Laundering (2018)

**CSAML-TYP-C02**

# Trade-Based Money Laundering (TBML)

**Family:** C — Business, Trade & Contract Abuse

> **Criminal / concealment objective**
>
> Move or disguise value through trade transactions by manipulating price, quantity, quality, description, shipment, or invoicing.

## Mechanism model

- Over- or under-invoice goods/services.

- Issue multiple invoices for the same shipment or payment.

- Misdescribe quantity, quality, origin, or type of goods.

- Use phantom shipments or third-party invoicing.

- Settle illicit obligations through trade value rather than direct financial transfer.

## Civil-society observables

- Trade values materially inconsistent with market benchmarks or customs data.

- Repeated counterparties with unusual routing, goods, or pricing.

- Company’s stated business does not match goods traded.

- Shipping, customs, invoice, and company records conflict.

## Indicator set

| **Class** | **Indicator** |
|----|----|
| M | Material documentary inconsistency in price, quantity, quality, shipment, or invoicing. |
| M | Trade transaction has no plausible relationship to the parties’ ordinary business. |
| C | Complex third-party payments or jurisdictions unrelated to shipment. |
| C | Repeated use of commodities suited to value manipulation. |
| D | Price variation is supported by grade, freight, insurance, scarcity, contract terms, or other market factors. |

## Minimum analytical questions

- What is the defensible market-value range?

- Do shipping and customs records corroborate invoicing?

- Why are payer, seller, shipper, and consignee different?

## False-positive / alternative-explanation cautions

- Trade pricing can vary legitimately; public benchmarks may not capture quality, contract, or freight differences.

## Useful evidence classes

- Customs/trade datasets

- Bills of lading if lawful/public

- Corporate records

- Invoices from court/public records

- Commodity benchmarks

- Shipping data

## Assessment rule for this typology

The analyst SHALL document which mechanism-specific indicators are observed, which independent evidence corroborates them, which disconfirming facts were considered, and which intelligence gaps materially limit confidence. The typology SHALL NOT be treated as established solely because contextual risk factors are present.

## Primary reference lineage

- FATF Trade-Based Money Laundering (2006 and later updates)

- APG Yearly Typologies Reports

**CSAML-TYP-C03**

# Procurement and Contract Value Diversion

**Family:** C — Business, Trade & Contract Abuse

> **Criminal / concealment objective**
>
> Convert public, donor, corporate, or project expenditure into private benefit and then obscure or integrate the diverted value.

## Mechanism model

- Steer contract to related or controlled entity.

- Inflate price, quantity, scope, or variation.

- Subcontract to connected entities or create false/low-value deliverables.

- Transform proceeds into assets, dividends, loans, related-party payments, or further corporate layers.

## Civil-society observables

- Shared ownership/control between procurement beneficiary and decision-connected persons.

- Repeated awards to connected companies or newly created entities.

- Large contract variations, subcontracting chains, or low observable performance.

- Asset acquisitions or company changes temporally linked to contract proceeds.

## Indicator set

| **Class** | **Indicator** |
|----|----|
| M | Award/contract value is linked to an entity controlled by or for a conflicted beneficiary. |
| M | Material discrepancy between contracted value and documented delivery/market value. |
| C | Subcontractors share owners, addresses, directors, or controllers with prime contractor. |
| C | Related asset acquisitions occur soon after economically significant contract events. |
| D | Competitive process, delivery evidence, market pricing, conflict disclosure, and independent oversight support legitimacy. |

## Minimum analytical questions

- Who ultimately benefits from the contract chain?

- What portion of value corresponds to observable delivery?

- Are related-party links disclosed and controlled?

## False-positive / alternative-explanation cautions

- Procurement irregularity is not automatically money laundering; predicate misconduct and laundering are separate analytical questions.

## Useful evidence classes

- Procurement portals

- Contracts and amendments

- Company/BO registries

- Project delivery records

- Audit reports

- Court/oversight findings

## Assessment rule for this typology

The analyst SHALL document which mechanism-specific indicators are observed, which independent evidence corroborates them, which disconfirming facts were considered, and which intelligence gaps materially limit confidence. The typology SHALL NOT be treated as established solely because contextual risk factors are present.

## Primary reference lineage

- PPATK court-based typology research

- FATF corruption/beneficial ownership work

**CSAML-TYP-C04**

# Sham Loans, Loan-Back, and Fictitious Debt

**Family:** C — Business, Trade & Contract Abuse

> **Criminal / concealment objective**
>
> Give illicit or undisclosed value the appearance of legitimate financing, repayment, or debt settlement.

## Mechanism model

- Create a loan between related or controlled parties.

- Use illicit value to fund the lender or offshore entity.

- Return funds as a documented loan, repayment, interest, or secured financing.

- Use false debt to justify asset transfer or cash flow.

## Civil-society observables

- Loans between related entities without clear commercial basis.

- Unusual loan terms, weak security, no repayment pattern, or lender with unclear capacity.

- Loan appears soon before asset acquisition or wealth increase.

## Indicator set

| **Class** | **Indicator** |
|----|----|
| M | Lender lacks plausible independent source of funds or appears controlled by borrower/related person. |
| M | Loan documentation does not align with actual payment, repayment, or commercial terms. |
| C | Loan coincides with asset purchase or unexplained increase in wealth. |
| D | Independent lender, market terms, repayment, credit assessment, and source-of-funds evidence support legitimacy. |

## Minimum analytical questions

- Who funded the lender?

- Were principal and interest actually paid?

- Were terms commercially reasonable?

## False-positive / alternative-explanation cautions

- Related-party financing is common and may be legitimate when properly documented and funded.

## Useful evidence classes

- Court filings

- Corporate financial statements

- Security/charge registries

- Loan agreements when public/lawfully held

- Asset records

## Assessment rule for this typology

The analyst SHALL document which mechanism-specific indicators are observed, which independent evidence corroborates them, which disconfirming facts were considered, and which intelligence gaps materially limit confidence. The typology SHALL NOT be treated as established solely because contextual risk factors are present.

## Primary reference lineage

- FATF Methods and Trends case studies

- FATF real estate typologies

**CSAML-TYP-D01**

# Real Estate Acquisition, Transfer, and Value Storage

**Family:** D — Asset Conversion & Integration

> **Criminal / concealment objective**
>
> Store, transform, or integrate value in real property, including through ownership layers, financing, renovation, resale, or third-party title.

## Mechanism model

- Purchase property directly or through legal entities/proxies.

- Use complex financing, cash, related-party loans, or offshore entities.

- Resell, refinance, lease, or transfer property to create apparently legitimate proceeds.

## Civil-society observables

- Property ownership linked to companies with opaque BO.

- Acquisition inconsistent with known resources or business profile.

- Rapid resale or repeated transfers among related entities.

- Property used by one person but legally owned by another connected person/entity.

## Indicator set

| **Class** | **Indicator** |
|----|----|
| M | Property funding or beneficial use is materially inconsistent with registered ownership. |
| M | Rapid related-party transfer or resale lacks credible economic rationale. |
| C | Complex company/loan structure obscures ultimate control. |
| C | Property event follows closely after predicate-risk event or major value inflow. |
| D | Documented financing, income, independent valuation, market sale, and beneficial ownership support legitimacy. |

## Minimum analytical questions

- Who funded, occupies, controls, maintains, and can dispose of the property?

- What was purchase price versus market range?

- What changed economically after each transfer?

## False-positive / alternative-explanation cautions

- Property ownership structures and family use can be legitimate; valuations vary.

## Useful evidence classes

- Land/property records where lawful/public

- Company/BO records

- Mortgage/charge records

- Court records

- Planning/building records

- Public sale listings

## Assessment rule for this typology

The analyst SHALL document which mechanism-specific indicators are observed, which independent evidence corroborates them, which disconfirming facts were considered, and which intelligence gaps materially limit confidence. The typology SHALL NOT be treated as established solely because contextual risk factors are present.

## Primary reference lineage

- FATF Money Laundering and Terrorist Financing Through the Real Estate Sector

**CSAML-TYP-D02**

# Luxury Goods, Precious Metals/Stones, Art, Vehicles, and Portable Stores of Value

**Family:** D — Asset Conversion & Integration

> **Criminal / concealment objective**
>
> Convert proceeds into movable, durable, high-value assets that can store, transport, transfer, or resell value.

## Mechanism model

- Purchase high-value goods directly or through intermediaries.

- Use cash, third parties, companies, or cross-border movement.

- Resell or pledge assets to reintroduce value.

## Civil-society observables

- High-value assets inconsistent with known resources.

- Repeated purchase/resale through connected parties.

- Dealers, auctions, import/export, or ownership records link assets to subject networks.

## Indicator set

| **Class** | **Indicator** |
|----|----|
| M | Asset acquisition is linked to unexplained funding or related-party concealment mechanism. |
| C | Use of proxy purchaser or corporate owner without commercial rationale. |
| C | Rapid resale or cross-border movement. |
| D | Documented legitimate wealth, business use, collection/investment purpose, and independent purchase funds. |

## Minimum analytical questions

- Who paid, who holds title, who possesses, and who benefits?

- How liquid is the asset and was it resold or pledged?

## False-positive / alternative-explanation cautions

- Luxury ownership alone is never a laundering indicator.

## Useful evidence classes

- Vehicle/vessel/aircraft registries

- Auction/public sale records

- Customs records

- Company records

- Court cases

- Public asset declarations

## Assessment rule for this typology

The analyst SHALL document which mechanism-specific indicators are observed, which independent evidence corroborates them, which disconfirming facts were considered, and which intelligence gaps materially limit confidence. The typology SHALL NOT be treated as established solely because contextual risk factors are present.

## Primary reference lineage

- FATF Professional Money Laundering (2018)

- APG typologies reports

**CSAML-TYP-E01**

# Professional Money Laundering Networks

**Family:** E — Professional & Network Facilitation

> **Criminal / concealment objective**
>
> Provide laundering as a service to one or more criminal clients through specialised roles, infrastructure, accounts, entities, settlement methods, and asset acquisition.

## Mechanism model

- Separate predicate offender from laundering specialists.

- Use collectors, coordinators, account controllers, transmitters, company/asset facilitators, and professional service providers.

- Pool or net-settle obligations across multiple clients and jurisdictions.

## Civil-society observables

- Same intermediaries, companies, addresses, wallets, or facilitators recur across otherwise unrelated cases.

- Network nodes appear to serve multiple clients/predicate offences.

- Professional services or company formation patterns connect dispersed actors.

## Indicator set

| **Class** | **Indicator** |
|----|----|
| M | A common facilitator or infrastructure serves multiple unrelated illicit-value chains. |
| M | Roles are specialised and repeatable across cases. |
| C | Network receives fees, spreads, commissions, or other compensation. |
| C | Multiple mechanisms—trade, cash, accounts, crypto, assets—are coordinated by the same network. |
| D | Professional service relationship is routine, documented, and unrelated to suspicious clients/events. |

## Minimum analytical questions

- Which nodes are clients, facilitators, controllers, transmitters, and beneficiaries?

- Does the network persist beyond a single predicate offence?

- How is compensation generated?

## False-positive / alternative-explanation cautions

- Lawyers, accountants, agents, remitters, and corporate service providers often perform legitimate work; role and knowledge must not be inferred from profession alone.

## Useful evidence classes

- Cross-case entity graph

- Court records

- Corporate service records

- Company formations

- Public disciplinary findings

- Multiple independent investigations

## Assessment rule for this typology

The analyst SHALL document which mechanism-specific indicators are observed, which independent evidence corroborates them, which disconfirming facts were considered, and which intelligence gaps materially limit confidence. The typology SHALL NOT be treated as established solely because contextual risk factors are present.

## Primary reference lineage

- FATF Professional Money Laundering (2018)

- FATF PML, Underground Banking and Hawala report (2026)

**CSAML-TYP-E02**

# Money Mule, Collector, Funnel, and Consolidation Networks

**Family:** E — Professional & Network Facilitation

> **Criminal / concealment objective**
>
> Receive funds through distributed accounts/persons and consolidate or forward value to reduce direct linkage between victims/origin and controllers.

## Mechanism model

- Recruit or control multiple account holders or payment recipients.

- Receive distributed inbound transfers.

- Withdraw, convert, or consolidate funds.

- Send value onward to controllers, exchanges, merchants, or laundering networks.

## Civil-society observables

- Court/scam reports show multiple recipients converging on common beneficiaries.

- Numerous accounts/entities share devices, addresses, contacts, employers, or controllers.

- Common onward destination or cash-out point recurs.

## Indicator set

| **Class** | **Indicator** |
|----|----|
| M | Multiple ostensibly independent recipients converge on a shared controller/destination. |
| M | Accounts/entities function mainly as receiving/pass-through nodes. |
| C | Common recruitment, device, contact, address, or payment infrastructure. |
| D | Marketplace, payroll, aggregator, franchise, charity, or platform relationship explains convergence. |

## Minimum analytical questions

- Are account holders knowing participants, coerced, deceived, or unwitting?

- Who consolidates and controls onward movement?

## False-positive / alternative-explanation cautions

- Do not assume mule intent; some participants may be victims or unwitting intermediaries.

## Useful evidence classes

- Court and police releases

- Victim reports with consent

- Published scam datasets

- Cross-case entity correlation

- Lawfully held payment records

## Assessment rule for this typology

The analyst SHALL document which mechanism-specific indicators are observed, which independent evidence corroborates them, which disconfirming facts were considered, and which intelligence gaps materially limit confidence. The typology SHALL NOT be treated as established solely because contextual risk factors are present.

## Primary reference lineage

- FATF Professional Money Laundering (2018)

- FATF Cyber-Enabled Fraud (2026)

**CSAML-TYP-E03**

# Underground Banking, Hawala, and Alternative Settlement

**Family:** E — Professional & Network Facilitation

> **Criminal / concealment objective**
>
> Transfer or settle value outside conventional bank-to-bank movement, often through brokers, offsetting obligations, trade, cash, or net settlement.

## Mechanism model

- Sender provides value to local broker.

- Counterpart broker pays recipient from separate pool or obligation.

- Brokers later settle balances through trade, cash, accounts, assets, or netting.

## Civil-society observables

- Value appears to move across borders without corresponding direct transfer.

- Recurring brokers/intermediaries connect communities or commercial networks.

- Trade or cash movements appear to settle unrelated obligations.

- Court records describe token/code-based or ledger-based informal settlement.

## Indicator set

| **Class** | **Indicator** |
|----|----|
| M | Documented paired pay-in/pay-out or net settlement without direct origin-to-recipient transfer. |
| M | Broker network maintains settlement obligations across jurisdictions. |
| C | Trade, cash, or third-party accounts used to settle broker balances. |
| D | Licensed remittance, family remittance, or legitimate informal finance context explains activity and complies with applicable law. |

## Minimum analytical questions

- How are obligations recorded and settled?

- Which broker controls each side?

- What mechanism ultimately balances the network?

## False-positive / alternative-explanation cautions

- Hawala and similar systems can serve legitimate remittance needs; the mechanism itself is not proof of laundering.

## Useful evidence classes

- Court judgments

- Regulatory findings

- Business/licensing records

- Trade/cash movement records

- Cross-border case studies

## Assessment rule for this typology

The analyst SHALL document which mechanism-specific indicators are observed, which independent evidence corroborates them, which disconfirming facts were considered, and which intelligence gaps materially limit confidence. The typology SHALL NOT be treated as established solely because contextual risk factors are present.

## Primary reference lineage

- FATF Investigating PML, Underground Banking and Hawala/HOSSPs (2026)

**CSAML-TYP-F01**

# Virtual Asset Conversion, Layering, and Obfuscation

**Family:** F — Digital & Cross-Border Channels

> **Criminal / concealment objective**
>
> Move or transform value through virtual assets, services, wallets, bridges, mixers, privacy features, or exchanges to increase distance from origin or enable cross-border transfer.

## Mechanism model

- Convert fiat/other assets to virtual assets.

- Move through wallets, services, chains, or obfuscation tools.

- Bridge or swap assets.

- Cash out, purchase assets, or retain value digitally.

## Civil-society observables

- Public blockchain movements connected to known addresses or entities.

- Use of multiple hops, chains, mixers/tumblers, privacy-enhancing services, or high-risk VASPs.

- Rapid conversion between fiat and virtual assets around relevant events.

## Indicator set

| **Class** | **Indicator** |
|----|----|
| M | On-chain path connects identified illicit/subject value to conversion or cash-out infrastructure. |
| M | Deliberate obfuscation features are used in a context lacking credible legitimate rationale. |
| C | Wallets share counterparties, timing, ownership indicators, or off-chain identifiers. |
| K | Cross-border/high-risk jurisdiction exposure. |
| D | Documented trading, treasury, privacy, technical testing, or business purpose explains pattern. |

## Minimum analytical questions

- What attribution evidence links the wallet to the entity?

- Where does value enter and leave the virtual-asset ecosystem?

- Which hops are evidence and which are heuristic attribution?

## False-positive / alternative-explanation cautions

- Blockchain address attribution can be probabilistic; privacy-enhancing tools have legitimate uses.

## Useful evidence classes

- Public blockchain data

- Court records

- Sanctions/designation records

- Exchange/VASP records if public or lawfully obtained

- Wallet attribution with provenance

## Assessment rule for this typology

The analyst SHALL document which mechanism-specific indicators are observed, which independent evidence corroborates them, which disconfirming facts were considered, and which intelligence gaps materially limit confidence. The typology SHALL NOT be treated as established solely because contextual risk factors are present.

## Primary reference lineage

- FATF Virtual Assets Red Flag Indicators (2020)

- FATF VA/VASP Targeted Update (2026)

- FATF DeFi report (2026)

**CSAML-TYP-F02**

# Cyber-Enabled Fraud Proceeds Laundering

**Family:** F — Digital & Cross-Border Channels

> **Criminal / concealment objective**
>
> Receive, disperse, convert, and cash out proceeds generated by scams, BEC, account takeover, investment fraud, impersonation, or other cyber-enabled fraud.

## Mechanism model

- Victim pays account/wallet controlled directly or through mules.

- Funds are rapidly dispersed or consolidated.

- Value moves through banks, PSPs, crypto, cash, goods, or laundering networks.

- Controllers cash out or reinvest proceeds.

## Civil-society observables

- Victim reports, police/court releases, account/wallet identifiers, scam infrastructure, and recipient networks.

- Rapid onward movement from victim-facing nodes.

- Shared infrastructure across multiple fraud campaigns.

## Indicator set

| **Class** | **Indicator** |
|----|----|
| M | Victim-originating value is directly linked to a recipient then rapidly layered/consolidated. |
| M | Recipient infrastructure is reused across multiple fraud incidents. |
| C | Mule/collector network or crypto cash-out pattern is present. |
| D | Commercial dispute or authorised payment explains transfer and no fraud predicate is supported. |

## Minimum analytical questions

- What is the predicate fraud evidence?

- Which nodes are victim-facing versus laundering infrastructure?

- Where does consolidation occur?

## False-positive / alternative-explanation cautions

- A suspicious payment recipient is not necessarily the fraud controller; account holders may be mules or victims.

## Useful evidence classes

- Victim evidence with consent

- Police/court records

- Domain/website records

- Account/wallet correlations

- Public blockchain data

## Assessment rule for this typology

The analyst SHALL document which mechanism-specific indicators are observed, which independent evidence corroborates them, which disconfirming facts were considered, and which intelligence gaps materially limit confidence. The typology SHALL NOT be treated as established solely because contextual risk factors are present.

## Primary reference lineage

- FATF Cyber-Enabled Fraud paper (2026)

- PPATK cybercrime risk assessments

**CSAML-TYP-F03**

# Cross-Border Cash and Physical Value Movement

**Family:** F — Digital & Cross-Border Channels

> **Criminal / concealment objective**
>
> Move illicit value physically across borders or locations using currency, bearer instruments, precious items, or other portable stores of value.

## Mechanism model

- Carry, courier, conceal, ship, or split physical value.

- Use multiple travellers/couriers or routes.

- Convert physical value into accounts/assets at destination.

## Civil-society observables

- Court/customs records of undeclared or falsely declared cash/value.

- Repeated travel/courier links around relevant events.

- Subsequent deposits, purchases, or settlement consistent with imported value.

## Indicator set

| **Class** | **Indicator** |
|----|----|
| M | Documented physical movement of undeclared/falsely declared value linked to subject network. |
| C | Fragmentation across couriers/routes or repeated border events. |
| C | Destination-side asset purchase or settlement is temporally/economically linked. |
| D | Lawful declared transport, business purpose, and source/destination evidence support legitimacy. |

## Minimum analytical questions

- Who owns the value, who carried it, and for whose benefit?

- Was it declared as required?

- How was it integrated at destination?

## False-positive / alternative-explanation cautions

- Physical cash movement can be lawful; declaration obligations vary by jurisdiction.

## Useful evidence classes

- Customs/court records

- Travel records where lawfully/publicly available

- Asset acquisition records

- Seizure notices

## Assessment rule for this typology

The analyst SHALL document which mechanism-specific indicators are observed, which independent evidence corroborates them, which disconfirming facts were considered, and which intelligence gaps materially limit confidence. The typology SHALL NOT be treated as established solely because contextual risk factors are present.

## Primary reference lineage

- FATF Recommendation 32 context

- PPATK cross-border cash risk assessments

**CSAML-TYP-F04**

# Digital Payment and Fintech Layering

**Family:** F — Digital & Cross-Border Channels

> **Criminal / concealment objective**
>
> Exploit e-money, payment service providers, prepaid instruments, merchant accounts, or fast digital payments to fragment, route, or cash out value.

## Mechanism model

- Use multiple digital accounts or wallets.

- Exploit merchant/payment rails for apparent purchases, refunds, peer transfers, or cash-out.

- Move value rapidly across platforms and into bank/crypto/cash channels.

## Civil-society observables

- Public cases show chains across multiple PSPs or digital wallets.

- Merchant entities have little observable commerce but significant payment activity in public/court records.

- Repeated refund/chargeback/merchant settlement patterns where documented.

## Indicator set

| **Class** | **Indicator** |
|----|----|
| M | Multiple digital payment instruments are used sequentially without plausible commercial purpose. |
| M | Merchant/payment account functions primarily as a pass-through or cash-out point. |
| C | Rapid platform hopping or conversion to other stores of value. |
| D | Marketplace, payment aggregation, remittance, or platform business model explains flow. |

## Minimum analytical questions

- What legitimate function does each platform/account serve?

- Who controls the merchant/payment account?

- Where is final cash-out or asset conversion?

## False-positive / alternative-explanation cautions

- Civil society rarely sees complete PSP data; avoid inferring patterns from partial records.

## Useful evidence classes

- Court/regulatory records

- Published PSP cases

- Merchant/company records

- Victim evidence with consent

## Assessment rule for this typology

The analyst SHALL document which mechanism-specific indicators are observed, which independent evidence corroborates them, which disconfirming facts were considered, and which intelligence gaps materially limit confidence. The typology SHALL NOT be treated as established solely because contextual risk factors are present.

## Primary reference lineage

- FATF Money Laundering Using New Payment Methods

- PPATK fintech sectoral risk assessments

**CSAML-TYP-D03**

# Gambling, Gaming, and Betting-Based Value Conversion

**Family:** D — Asset Conversion & Integration

> **Criminal / concealment objective**
>
> Use gambling or gaming systems to commingle, transfer, convert, or re-characterise funds as winnings, balances, chips, credits, or payouts.

## Mechanism model

- Buy chips/credits or fund account.

- Conduct limited or coordinated play, transfers, or cash-out.

- Obtain payout or balance that appears linked to gambling activity.

## Civil-society observables

- Court/regulatory records linking funds to gambling operators.

- Large buy-ins and rapid cash-out with limited play where documented.

- Related persons repeatedly transact through same gambling ecosystem.

## Indicator set

| **Class** | **Indicator** |
|----|----|
| M | Value enters and exits gambling system with minimal risk exposure/play, where records establish this. |
| C | Third-party funding or payout to unrelated persons. |
| C | Gambling operator/account connected to broader laundering network. |
| D | Normal entertainment or professional gambling activity supported by play history and source of funds. |

## Minimum analytical questions

- How much genuine gaming risk was taken?

- Who funded and who received payout?

- Was the operator licensed/regulated?

## False-positive / alternative-explanation cautions

- Gambling activity alone is not evidence of laundering.

## Useful evidence classes

- Court/regulator records

- Operator disclosures if lawful/public

- Payment records if lawfully available

## Assessment rule for this typology

The analyst SHALL document which mechanism-specific indicators are observed, which independent evidence corroborates them, which disconfirming facts were considered, and which intelligence gaps materially limit confidence. The typology SHALL NOT be treated as established solely because contextual risk factors are present.

## Primary reference lineage

- APG Yearly Typologies Reports

- FATF methods and trends

**CSAML-TYP-C05**

# Environmental and Natural-Resource Crime Proceeds Laundering

**Family:** C — Business, Trade & Contract Abuse

> **Criminal / concealment objective**
>
> Monetise and integrate proceeds from illegal extraction, logging, mining, wildlife, fisheries, waste, or other environmental crime through legitimate-looking trade and corporate structures.

## Mechanism model

- Mix illegal and legal commodities.

- Use licensed companies, false permits, trade misdescription, or supply-chain opacity.

- Route proceeds through traders, exporters, processors, shell/front companies, or asset purchases.

## Civil-society observables

- Permits, concessions, production volumes, export data, and physical/satellite evidence conflict.

- Companies linked to environmental violations also show opaque ownership or unexplained trade volumes.

- Commodity flows exceed plausible legal production.

## Indicator set

| **Class** | **Indicator** |
|----|----|
| M | Documented mismatch between legal production/permit capacity and traded/exported volume. |
| M | Illegal-source commodity is mixed into legitimate supply chain. |
| C | Ownership/control links connect violator, trader, processor, exporter, and asset beneficiary. |
| D | Independent production records, permits, traceability, and audited supply chain support legality. |

## Minimum analytical questions

- What is legal production capacity versus observed output/trade?

- Where does illegal commodity acquire apparently legitimate documentation?

- Who captures the economic benefit?

## False-positive / alternative-explanation cautions

- Production estimates and satellite analysis carry uncertainty; environmental violation does not automatically establish laundering.

## Useful evidence classes

- Permits/concessions

- Satellite/remote sensing

- Customs/trade data

- Company/BO records

- Court/enforcement records

- Supply-chain certifications

## Assessment rule for this typology

The analyst SHALL document which mechanism-specific indicators are observed, which independent evidence corroborates them, which disconfirming facts were considered, and which intelligence gaps materially limit confidence. The typology SHALL NOT be treated as established solely because contextual risk factors are present.

## Primary reference lineage

- FATF environmental crime work and national risk-assessment materials

- PPATK smuggling typology (2025)

# 7. Cross-Typology Analysis

Money-laundering schemes frequently combine several typologies. Analysts SHALL preserve the distinction between typologies while documenting the mechanism that connects them.

| **Analytical layer**     | **Illustrative typology composition** |
|--------------------------|---------------------------------------|
| Predicate / value source | Procurement diversion                 |
| Ownership concealment    | A01 Shell company + A02 nominee       |
| Layering                 | B03 rapid pass-through                |
| Integration              | D01 real estate                       |
| Facilitation             | E01 professional network              |

**COMPOSITION RULE —** A combined scheme assessment SHALL identify the evidence supporting each typology separately before describing the overall laundering hypothesis.

# 8. Typology Record Schema

| **Field** | **Meaning** | **Requirement** |
|----|----|----|
| typology_id | Stable identifier, e.g., CSAML-TYP-C02 | MUST |
| version | Entry version | MUST |
| title | Controlled title | MUST |
| family | Catalogue family | MUST |
| objective | Concealment/movement/integration objective | MUST |
| mechanism | Ordered mechanism description | MUST |
| indicators | Classed M/C/K/D/G indicators | MUST |
| observables | Civil-society observable sources/signals | MUST |
| questions | Minimum analytical questions | MUST |
| cautions | Alternative explanations / false-positive cautions | MUST |
| evidence_classes | Evidence types commonly useful | SHOULD |
| source_lineage | Authoritative reference basis | MUST |
| last_reviewed | Review date | MUST |
| status | active/deprecated/experimental | MUST |

# 9. Case-Level Typology Assessment Record

| **Field** | **Requirement** |
|----|----|
| Case ID | Required |
| Typology ID/version | Required |
| Assessment level | Required |
| Observed mechanism-specific indicators | Required |
| Corroborating evidence IDs | Required |
| Disconfirming evidence IDs | Required if available |
| Alternative explanations | Required |
| Intelligence gaps | Required |
| Analyst judgement | Required |
| Confidence | Required |
| Reviewer | Required for Strong/Compelling assessments |
| Date / revision | Required |

# 10. Governance and Catalogue Maintenance

- Each typology SHALL have a stable identifier and version history.

- New typologies SHOULD be supported by multiple authoritative or case-based sources before promotion to Active status.

- Experimental entries MAY be used for research but SHALL be clearly labelled and SHALL NOT be used as sole basis for escalation.

- Entries SHALL be reviewed when material FATF/APG/PPATK guidance, major case-law patterns, or technological changes emerge, and at least annually.

- Deprecated typologies SHALL remain resolvable by ID so historical case records remain interpretable.

- Changes to indicators SHALL document rationale and source lineage.

# 11. Safety, Rights, and Proportionality Guardrails

**GUARDRAIL —** The catalogue SHALL NOT be used to justify intrusive collection merely because a typology could theoretically apply.

**GUARDRAIL —** Investigators SHALL collect only information that is lawful, relevant, proportionate, and necessary to the investigation question.

**GUARDRAIL —** Protected characteristics, political activity, religious activity, civil-society participation, or association alone SHALL NOT be treated as AML indicators.

**GUARDRAIL —** Use of a professional service provider, remittance mechanism, virtual asset, charity/NPO, cash, or cross-border structure SHALL NOT be treated as suspicious by itself.

**GUARDRAIL —** Publication or referral decisions SHALL apply the parent framework’s evidence, privacy, review, source-protection, and dissemination controls.

# 12. Conformance Requirements

| **Level** | **Minimum requirement** |
|----|----|
| Catalogue-aware | Organisation uses controlled typology IDs and distinguishes indicators from findings. |
| Catalogue-conformant | In addition, case records document indicator classes, evidence links, alternative explanations, intelligence gaps, and assessment level. |
| Catalogue-assured | In addition, strong/compelling assessments receive independent review; catalogue changes are versioned and annually reviewed; QA samples verify typology use. |

# Annex A — Source Lineage and Reference Basis

FATF Recommendations, updated June 2026 — [<u>https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Fatf-recommendations.html</u>](https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Fatf-recommendations.html)

FATF Methods and Trends — [<u>https://www.fatf-gafi.org/en/topics/methods-and-trends.html</u>](https://www.fatf-gafi.org/en/topics/methods-and-trends.html)

FATF Professional Money Laundering (2018) — [<u>https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/Professional-Money-Laundering.pdf</u>](https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/Professional-Money-Laundering.pdf)

FATF Investigating Professional Money Laundering, Underground Banking, Hawala and HOSSPs (2026) — [<u>https://www.fatf-gafi.org/en/publications/Methodsandtrends/pml-underground-banking-hawala-hossps.html</u>](https://www.fatf-gafi.org/en/publications/Methodsandtrends/pml-underground-banking-hawala-hossps.html)

FATF-Egmont Concealment of Beneficial Ownership — [<u>https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/FATF-Egmont-Concealment-beneficial-ownership.pdf</u>](https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/FATF-Egmont-Concealment-beneficial-ownership.pdf)

FATF Guidance on Beneficial Ownership of Legal Persons — [<u>https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-Beneficial-Ownership-Legal-Persons.html</u>](https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-Beneficial-Ownership-Legal-Persons.html)

FATF Trade-Based Money Laundering — [<u>https://www.fatf-gafi.org/en/publications/Methodsandtrends/Trade-basedmoneylaundering.html</u>](https://www.fatf-gafi.org/en/publications/Methodsandtrends/Trade-basedmoneylaundering.html)

FATF Money Laundering Through Real Estate — [<u>https://www.fatf-gafi.org/en/publications/Methodsandtrends/Moneylaunderingandterroristfinancingthroughtherealestatesector.html</u>](https://www.fatf-gafi.org/en/publications/Methodsandtrends/Moneylaunderingandterroristfinancingthroughtherealestatesector.html)

FATF Virtual Assets Red Flag Indicators — [<u>https://www.fatf-gafi.org/en/publications/Methodsandtrends/Virtual-assets-red-flag-indicators.html</u>](https://www.fatf-gafi.org/en/publications/Methodsandtrends/Virtual-assets-red-flag-indicators.html)

FATF Cyber-Enabled Fraud (2026) — [<u>https://www.fatf-gafi.org/en/publications/Methodsandtrends/cyber-enabled-fraud-digitalisation-ml-tf-pf-risks.html</u>](https://www.fatf-gafi.org/en/publications/Methodsandtrends/cyber-enabled-fraud-digitalisation-ml-tf-pf-risks.html)

FATF DeFi targeted report (2026) — [<u>https://www.fatf-gafi.org/en/news/targeted-report-decentralised-finance-2026.html</u>](https://www.fatf-gafi.org/en/news/targeted-report-decentralised-finance-2026.html)

PPATK Tipologi Pencucian Uang Berdasarkan Putusan Pengadilan — [<u>https://www.ppatk.go.id/publikasi/read/132/tipologi-</u>](https://www.ppatk.go.id/publikasi/read/132/tipologi-)

PPATK Riset Tipologi Tahun 2021 — [<u>https://www.ppatk.go.id/publikasi/read/160/riset-tipologi-tahun-2021-berdasarkan-putusan-pengadilan-pencucian-uang-tahun-2020.html</u>](https://www.ppatk.go.id/publikasi/read/160/riset-tipologi-tahun-2021-berdasarkan-putusan-pengadilan-pencucian-uang-tahun-2020.html)

PPATK Tipologi Pencucian Uang yang Berasal dari Penyelundupan (2025) — [<u>https://www.ppatk.go.id/publikasi/read/250/tipologi-pencucian-uang-yang-berasal-dari-penyelundupan.html</u>](https://www.ppatk.go.id/publikasi/read/250/tipologi-pencucian-uang-yang-berasal-dari-penyelundupan.html)

PPATK Publications / Risk Assessments — [<u>https://www.ppatk.go.id/dalam_negeri/read/1397/publikasi-penilaian-risiko.html</u>](https://www.ppatk.go.id/dalam_negeri/read/1397/publikasi-penilaian-risiko.html)

# Annex B — Controlled Interpretation Language

| **Type** | **Language** |
|----|----|
| Preferred | “The observed pattern is strongly consistent with CSAML-TYP-A01, subject to the stated intelligence gaps.” |
| Preferred | “Public-source evidence supports a reconstructed value-flow hypothesis; direct transactional evidence is unavailable.” |
| Preferred | “The indicators warrant further financial investigation but do not establish money laundering.” |
| Avoid | “This proves money laundering.” |
| Avoid | “The company is a shell company” unless the factual basis and definition are established. |
| Avoid | “X owns Y” when the evidence supports only association, management, use, or inferred control. |

**END OF CS-AML TYPOLOGY CATALOGUE v0.1**
