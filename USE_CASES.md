# OpenClaw use-case blueprints

> **Status: Blueprint** — These pages describe architectures and operating patterns, not guaranteed built-in integrations. Skill names and commands inside a blueprint are conceptual unless explicitly marked **Verified command** and linked to the official CLI reference. Validate integrations in a non-production environment and keep consequential actions behind human approval.

The collection contains 46 implementation ideas across software, research, operations, public infrastructure, and regulated domains.

## Software, security, and knowledge work

| Blueprint | Primary pattern | Risk boundary |
| --- | --- | --- |
| [Academic research](use-cases/academic-research.md) | search, synthesis, citations | verify every source |
| [Autonomous laboratory](use-cases/autonomous-lab.md) | experiment coordination | no unattended physical actions |
| [Content automation](use-cases/content-automation.md) | research-to-publishing pipeline | approval before publishing |
| [Cybersecurity forensics](use-cases/cybersecurity-forensics.md) | evidence collection and correlation | preserve chain of custody |
| [Cybersecurity threat hunting](use-cases/cybersecurity-threat-hunting.md) | telemetry triage | isolate response actions |
| [DevOps automation](use-cases/devops-automation.md) | release and incident operations | approval before production change |
| [Game development pipeline](use-cases/game-dev-pipeline.md) | asset and build coordination | isolate generated assets |
| [Market research](use-cases/market-research.md) | monitored sources and briefs | respect access and rate limits |
| [Media production](use-cases/media-production.md) | production workflow orchestration | rights and publication review |

## Business and customer operations

| Blueprint | Primary pattern | Risk boundary |
| --- | --- | --- |
| [Customer support](use-cases/customer-support.md) | retrieval and ticket routing | identity and data minimization |
| [E-commerce monitoring](use-cases/ecommerce-monitoring.md) | price and inventory monitoring | no deceptive interaction |
| [Event management](use-cases/event-management.md) | RSVP and vendor coordination | approval before outreach |
| [Hospitality revenue](use-cases/hospitality-revenue.md) | forecasting and pricing support | human pricing review |
| [HR and recruitment](use-cases/hr-recruitment.md) | candidate workflow assistance | no autonomous employment decision |
| [Last-mile delivery](use-cases/last-mile-delivery.md) | dispatch and route support | human operational control |
| [Luxury concierge](use-cases/luxury-concierge.md) | preference-aware coordination | approval before booking or spend |
| [Philanthropy and nonprofit](use-cases/philanthropy-nonprofit.md) | grant and donor operations | consent and ethical outreach |
| [Real-estate investment](use-cases/real-estate-investment.md) | deal analysis | no autonomous financial decision |
| [Real-estate leads](use-cases/real-estate-leads.md) | qualification and CRM routing | consent before contact |
| [Supply-chain logistics](use-cases/supply-chain-logistics.md) | tracking and inventory decisions | approval before orders |
| [Sustainable fashion](use-cases/sustainable-fashion.md) | traceability and compliance evidence | verify sustainability claims |

## Industrial, energy, and infrastructure

| Blueprint | Primary pattern | Risk boundary |
| --- | --- | --- |
| [Architecture and construction](use-cases/architecture-construction.md) | project and safety monitoring | no autonomous safety certification |
| [Aviation maintenance](use-cases/aviation-maintenance.md) | maintenance intelligence | qualified engineer sign-off |
| [Industry 4.0](use-cases/industry-4-0.md) | telemetry and predictive maintenance | hardware failsafes |
| [Maritime logistics](use-cases/maritime-logistics.md) | vessel and port coordination | human navigation authority |
| [Mining exploration](use-cases/mining-exploration.md) | geospatial decision support | field and environmental review |
| [Oil and gas integrity](use-cases/oil-gas-integrity.md) | anomaly and integrity monitoring | safety-system independence |
| [Renewable energy](use-cases/renewable-energy.md) | generation and storage optimization | grid operator approval |
| [Space operations](use-cases/space-ops-satellite.md) | tracking and ground operations | no autonomous critical command |
| [Waste management](use-cases/waste-management.md) | sensing and route optimization | human dispatch authority |

## Agriculture and environment

| Blueprint | Primary pattern | Risk boundary |
| --- | --- | --- |
| [Environmental conservation](use-cases/environmental-conservation.md) | sensor and field intelligence | protect sensitive locations |
| [Precision agriculture](use-cases/precision-agriculture.md) | imagery and treatment planning | approval before application |
| [Smart agriculture](use-cases/smart-agriculture.md) | farm monitoring and control | hardware failsafes |
| [Vertical farming](use-cases/vertical-farming.md) | climate and nutrient control | independent safety limits |

## Health, education, finance, and legal

| Blueprint | Primary pattern | Risk boundary |
| --- | --- | --- |
| [Bioinformatics and genomics](use-cases/bioinformatics-genomics.md) | scientific pipeline coordination | protect genomic data |
| [Education and tutoring](use-cases/education-tutoring.md) | adaptive learning assistance | educator and guardian oversight |
| [Finance tracking](use-cases/finance-tracking.md) | read-only aggregation and reports | no transaction authority |
| [Financial fraud detection](use-cases/financial-fraud-detection.md) | anomaly triage | no autonomous enforcement |
| [Healthcare administration](use-cases/healthcare-admin.md) | scheduling and document workflow | protect health information |
| [Legal automation](use-cases/legal-automation.md) | document and deadline assistance | qualified legal review |
| [Wellness coaching](use-cases/wellness-coaching.md) | habit and wearable summaries | not diagnosis or treatment |

## Cities, response, sports, and culture

| Blueprint | Primary pattern | Risk boundary |
| --- | --- | --- |
| [Disaster response](use-cases/disaster-response.md) | situational awareness and coordination | incident commander authority |
| [E-sports analytics](use-cases/esports-analytics.md) | replay and performance analysis | competition-rule compliance |
| [Smart urban planning](use-cases/smart-urban-planning.md) | city data and scenario analysis | privacy and public review |
| [Sports analytics](use-cases/sports-analytics.md) | performance and tactical briefs | medical and coaching oversight |

## Blueprint implementation contract

Before turning any page into a working system, define:

1. Real integrations and their authentication model.
2. Data classification, retention, and allowed destinations.
3. Read-only and mutation-capable tools as separate capability sets.
4. Sender allowlists, sandbox scope, and approval rules.
5. Idempotency, retry, rate-limit, and failure behavior.
6. Evidence required before the workflow may report completion.
7. A rollback or safe-stop path.

Start with [Security hardening](docs/SECURITY.md) and [Automation](docs/AUTOMATION.md).
