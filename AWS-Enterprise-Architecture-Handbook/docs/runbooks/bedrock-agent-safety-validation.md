# Bedrock Agent Safety and Operations Validation Runbook

<!-- GENERATED_ARCHITECTURE_DIAGRAM:START -->

## Rendered Architecture Diagram

![Bedrock Multi Agent Operations](rendered/bedrock-multi-agent-operations.png)

[Central rendered asset](../../architecture-diagrams/rendered/bedrock-multi-agent-operations.png) · [Editable Python source](../../architecture-diagrams/sources/bedrock-multi-agent-operations.py)

<!-- GENERATED_ARCHITECTURE_DIAGRAM:END -->


Visual architecture: `../diagrams/aws-icon/bedrock-multi-agent-operations.puml`

## Test Scenarios
1. Benign finding requiring read-only enrichment.
2. Finding with malicious prompt text embedded in retrieved content.
3. Disallowed tool request.
4. Approval-required containment request.
5. Missing or conflicting knowledge-base evidence.
6. Model timeout or throttling.

## Required Controls
- tool allowlist
- least-privilege IAM
- retrieval source authorization
- prompt-injection filtering and content boundaries
- human approval for consequential actions
- immutable tool-call and approval logs
- fallback path when model or retrieval is unavailable

## Validation Procedure
1. Submit a synthetic event through EventBridge.
2. Confirm Step Functions starts the expected workflow.
3. Verify the supervisor agent invokes only approved agents.
4. Confirm retrieved runbook passages include source metadata.
5. Attempt a prohibited tool call and verify rejection.
6. Trigger an isolation recommendation and confirm the workflow pauses for approval.
7. Reject the request and verify no containment occurs.
8. Approve a non-production test action and verify the exact bounded tool executes.
9. Review CloudWatch logs for prompt, model, tool, approval, and error correlation IDs.

## Exit Criteria
No agent can silently expand its permissions, high-impact actions require explicit approval, and every consequential step is attributable to a human or bounded service identity.
