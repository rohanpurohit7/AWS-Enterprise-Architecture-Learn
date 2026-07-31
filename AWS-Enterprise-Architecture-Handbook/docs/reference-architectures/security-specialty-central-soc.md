# Centralized AWS Security Operations Center

<!-- GENERATED_ARCHITECTURE_DIAGRAM:START -->

## Rendered Architecture Diagram

![Security Specialty Central Soc](rendered/security-specialty-central-soc.png)

[Central rendered asset](../../architecture-diagrams/rendered/security-specialty-central-soc.png) · [Editable Python source](../../architecture-diagrams/sources/security-specialty-central-soc.py)

<!-- GENERATED_ARCHITECTURE_DIAGRAM:END -->


## Case Study

A regulated enterprise operates multiple AWS accounts for production, development, shared services, networking, and security. Leadership needs centralized visibility, faster investigation, consistent detection engineering, and controlled automated response without granting a single automation component unrestricted access to every workload.

## Business Objective

Create a central security operations architecture that aggregates findings and telemetry across accounts, supports threat hunting and investigation, and enables bounded automation with human approval for high-impact actions.

## Technical Approach

Use an organization-level logging strategy, GuardDuty for managed threat detections, Security Hub for normalized finding aggregation, Detective for investigation context, Security Lake for governed security telemetry, OpenSearch for search and dashboards, EventBridge for routing, and Lambda for controlled enrichment or response.

![AWS-icon source diagram](../diagrams/aws-icon/security-specialty-central-soc.puml)

## Account Model

- Security tooling account: Security Hub delegated administration, GuardDuty administration, Detective, automation.
- Log archive account: immutable or tightly controlled centralized logs.
- Workload accounts: application and platform telemetry producers.
- Network account: centralized inspection and network telemetry where used.

## Configuration Steps

1. Establish AWS Organizations and designate security/logging accounts.
2. Configure organization CloudTrail and central log destinations.
3. Enable GuardDuty across member accounts and Regions required by policy.
4. Configure Security Hub aggregation and delegated administration.
5. Enable Detective for investigation workflows where appropriate.
6. Configure Security Lake sources and subscriber access.
7. Route selected findings through EventBridge rules.
8. Invoke Lambda enrichment functions using least-privilege roles.
9. Send high-severity events to SNS or ticketing integrations.
10. Index approved telemetry in OpenSearch with retention and access policies.

## Security and Privacy

- Centralize only required telemetry; minimize PII in logs.
- Separate security administration from workload administration.
- Encrypt data at rest and in transit.
- Use resource policies and cross-account roles rather than long-lived credentials.
- Require approval before destructive containment actions.
- Retain audit evidence for automated decisions and operator overrides.

## Performance and Scalability

Use event-driven routing so findings scale independently from analyst dashboards. Separate raw telemetry retention from hot searchable data. Apply lifecycle policies and tiering to control cost.

## Monitoring and Validation

Validate that new findings arrive from each member account, EventBridge rules match expected severities, Lambda failures are alarmed, and OpenSearch ingestion lag remains within operational targets.

## Well-Architected Review

**Security:** centralized visibility, delegated administration, least privilege.  
**Reliability:** decoupled event flow and retry-aware automation.  
**Operational Excellence:** runbooks for investigation, escalation, containment, and rollback.  
**Cost:** separate hot search from long-term retention.
