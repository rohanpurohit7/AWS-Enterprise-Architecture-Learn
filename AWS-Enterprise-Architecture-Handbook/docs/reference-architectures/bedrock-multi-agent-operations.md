# Bedrock Multi-Agent Operations Reference Architecture

<!-- GENERATED_ARCHITECTURE_DIAGRAM:START -->

## Rendered Architecture Diagram

![Bedrock Multi Agent Operations](rendered/bedrock-multi-agent-operations.png)

[Central rendered asset](../../architecture-diagrams/rendered/bedrock-multi-agent-operations.png) · [Editable Python source](../../architecture-diagrams/sources/bedrock-multi-agent-operations.py)

<!-- GENERATED_ARCHITECTURE_DIAGRAM:END -->


Architecture: `../diagrams/aws-icon/bedrock-multi-agent-operations.puml`

## Case Study
A large enterprise SOC receives thousands of security and operational findings per day. Analysts need faster triage and contextual recommendations, but automated containment must remain bounded and human-approved.

## Business Objective
Reduce analyst toil, improve consistency of triage, preserve auditability, and accelerate low-risk enrichment while preventing unconstrained autonomous actions.

## Technical Approach
Use EventBridge to route findings into Step Functions. A Bedrock supervisor agent coordinates specialized triage and remediation-advisor agents. Knowledge Bases retrieve approved runbooks and policy content. Tool access is mediated through Lambda or an MCP-compatible gateway with explicit allowlists. Case state is persisted in DynamoDB and all actions are logged.

## Configuration Steps
1. Select approved Bedrock models and Regions consistent with organizational data-handling rules.
2. Create an encrypted S3 repository for approved runbooks, threat-intelligence procedures, and escalation playbooks.
3. Build a Bedrock Knowledge Base over approved content with source metadata.
4. Create triage and remediation-advisor agents with narrowly scoped instructions.
5. Create a supervisor agent that delegates only to approved subagents.
6. Implement tool adapters using Lambda or an MCP gateway that exposes only allowlisted actions.
7. Mark consequential tools such as host isolation or credential revocation as approval-required.
8. Use Step Functions for deterministic orchestration, retries, timeout handling, and approval pauses.
9. Store case context in DynamoDB with encryption and TTLs where appropriate.
10. Send agent invocation, tool, approval, and failure telemetry to CloudWatch and the audit platform.

## Validation
- Submit a synthetic GuardDuty or Security Hub finding.
- Confirm enrichment occurs without write privileges.
- Attempt a disallowed tool call and verify rejection.
- Trigger an approval-required containment action and confirm the workflow pauses.
- Review the generated response for source provenance and factual grounding.

## Security and Privacy
Minimize sensitive content sent to models, authorize retrieval at the source, log tool calls, prevent cross-tenant context leakage, defend against prompt injection in retrieved content, and prohibit silent autonomous containment.

## Well-Architected Review
The pattern separates probabilistic reasoning from deterministic control flow. Step Functions controls the workflow; Bedrock provides reasoning and summarization; tool adapters enforce least privilege; humans retain authority over high-impact actions.
