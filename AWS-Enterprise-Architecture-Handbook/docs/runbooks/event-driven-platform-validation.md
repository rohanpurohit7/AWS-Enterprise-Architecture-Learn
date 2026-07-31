# Event-Driven Application Validation Runbook

<!-- GENERATED_ARCHITECTURE_DIAGRAM:START -->

## Rendered Architecture Diagram

![Developer Event Driven Platform](rendered/developer-event-driven-platform.png)

[Central rendered asset](../../architecture-diagrams/rendered/developer-event-driven-platform.png) · [Editable Python source](../../architecture-diagrams/sources/developer-event-driven-platform.py)

<!-- GENERATED_ARCHITECTURE_DIAGRAM:END -->


Architecture: `../diagrams/aws-icon/developer-event-driven-platform.puml`

## Objective
Validate an API Gateway, Lambda, EventBridge, SQS, Step Functions, DynamoDB, and S3 workflow with retry, failure isolation, and observability.

## Validation Steps
1. Send an authenticated test request through API Gateway.
2. Confirm request validation and Lambda invocation.
3. Confirm the expected domain event is published to EventBridge.
4. Confirm the matching event rule delivers to the intended SQS queue.
5. Confirm Step Functions consumes the work and executes the expected workflow path.
6. Confirm DynamoDB state updates are idempotent.
7. Confirm generated objects are written to the correct S3 location.
8. Trigger a controlled downstream failure and verify retry behavior.
9. Exhaust retries in a test path and confirm dead-letter handling.
10. Confirm CloudWatch logs, metrics, alarms, and correlation identifiers support end-to-end troubleshooting.

## Failure Scenarios
- duplicate API submission
- duplicate event delivery
- Lambda timeout
- SQS backlog
- Step Functions task failure
- DynamoDB conditional-write failure
- S3 access denial

## Success Criteria
The workflow completes correctly for a valid request, handles duplicate or failed events safely, preserves auditability, and exposes actionable operational metrics.
