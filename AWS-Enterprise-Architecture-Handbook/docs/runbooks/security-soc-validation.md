# Central Security Operations Validation Runbook

<!-- GENERATED_ARCHITECTURE_DIAGRAM:START -->

## Rendered Architecture Diagram

![Security Specialty Central Soc](rendered/security-specialty-central-soc.png)

[Central rendered asset](../../architecture-diagrams/rendered/security-specialty-central-soc.png) · [Editable Python source](../../architecture-diagrams/sources/security-specialty-central-soc.py)

<!-- GENERATED_ARCHITECTURE_DIAGRAM:END -->


Architecture: `../diagrams/aws-icon/security-specialty-central-soc.puml`

## Objective
Validate that organization-wide security telemetry, findings, investigation context, and controlled response automation are working end to end.

## Validation Sequence
1. Confirm CloudTrail organization logging is active and delivering to the expected centralized destination.
2. Confirm GuardDuty is enabled for required accounts and Regions.
3. Confirm Security Hub aggregation is receiving findings from member accounts.
4. Confirm Detective is available to investigators and linked to supported findings.
5. Confirm Security Lake sources are enabled and expected data classes are arriving.
6. Confirm EventBridge rules route selected findings to enrichment or response workflows.
7. Confirm Lambda enrichment executes with least-privilege permissions.
8. Confirm SNS, ticketing, or chat notifications reach the intended responders.
9. Confirm OpenSearch ingestion and dashboard freshness meet operational targets.
10. Confirm automation does not perform destructive containment without the required approval gate.

## Test Event
Generate or simulate a benign test finding in a controlled account. Trace it through:

```text
Finding source
  -> Security Hub
  -> EventBridge
  -> Lambda enrichment
  -> notification/ticket
  -> analyst review
```

## Operational Checks
- Failed Lambda invocations are alarmed.
- Dead-letter or retry paths exist where asynchronous delivery can fail.
- Security Lake and OpenSearch retention follow policy.
- Cross-account roles do not grant broader access than needed.
- Finding metadata does not expose unnecessary PII in notifications.

## Success Criteria
A test finding is visible in the central security account, enriched successfully, searchable by analysts, and routed to the correct escalation channel with a complete audit trail.
