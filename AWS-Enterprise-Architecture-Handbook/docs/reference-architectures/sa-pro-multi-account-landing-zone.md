# Multi-Account Landing Zone Reference Architecture

<!-- GENERATED_ARCHITECTURE_DIAGRAM:START -->

## Rendered Architecture Diagram

![Sa Pro Multi Account Landing Zone](rendered/sa-pro-multi-account-landing-zone.png)

[Central rendered asset](../../architecture-diagrams/rendered/sa-pro-multi-account-landing-zone.png) · [Editable Python source](../../architecture-diagrams/sources/sa-pro-multi-account-landing-zone.py)

<!-- GENERATED_ARCHITECTURE_DIAGRAM:END -->


Architecture: `../diagrams/aws-icon/sa-pro-multi-account-landing-zone.puml`

## Case Study
A regulated enterprise is migrating business applications to AWS and needs centralized governance without forcing every workload into a single account.

## Business Objective
Establish repeatable account vending, identity federation, centralized logging, security aggregation, network connectivity, and guardrails while preserving workload-team autonomy.

## Technical Approach
Use AWS Organizations with organizational units for Security, Infrastructure, Production, Non-Production, and Sandbox. Use Control Tower for landing-zone governance, IAM Identity Center for workforce access, delegated security administration, organization CloudTrail, centralized log archive, and a network account for shared connectivity.

## Requirements
- Separate production and non-production blast radii.
- Centralize audit evidence and security findings.
- Use short-lived federated access instead of long-lived IAM users.
- Apply SCPs and preventive guardrails.
- Maintain workload-level cost attribution.
- Support Transit Gateway or cloud WAN connectivity patterns.

## Configuration Steps
1. Create AWS Organizations and enable all features.
2. Design OUs: Security, Infrastructure, Prod, NonProd, Sandbox.
3. Deploy or enroll accounts through Control Tower.
4. Configure IAM Identity Center permission sets mapped to job functions.
5. Delegate GuardDuty, Security Hub, Inspector, Macie, and Firewall Manager administration to the security account where appropriate.
6. Enable organization CloudTrail and AWS Config aggregation.
7. Deliver logs to an encrypted S3 log-archive bucket with restricted deletion.
8. Create a network account for Transit Gateway, Route 53 Resolver, inspection, and shared endpoints.
9. Apply SCPs that deny disabling security services, public S3 access, and unapproved Regions as required.
10. Configure budgets, cost allocation tags, and account ownership metadata.

## Validation
- Confirm new accounts inherit required controls.
- Verify federated access and permission boundaries.
- Confirm organization trails deliver into the log archive.
- Confirm security findings aggregate centrally.
- Test an SCP denial using a non-production account.

## Security and Privacy
Use least privilege, separate duties, immutable logging, KMS encryption, data classification, and Region controls. Do not centralize sensitive workload data unless the receiving account is explicitly authorized.

## Well-Architected Review
This pattern primarily supports Security, Operational Excellence, Reliability, and Cost Optimization through blast-radius reduction, consistent controls, centralized evidence, and chargeback/showback.
