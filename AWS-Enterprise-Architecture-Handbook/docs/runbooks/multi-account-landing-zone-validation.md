# Multi-Account Landing Zone Validation Runbook

<!-- GENERATED_ARCHITECTURE_DIAGRAM:START -->

## Rendered Architecture Diagram

![Sa Pro Multi Account Landing Zone](rendered/sa-pro-multi-account-landing-zone.png)

[Central rendered asset](../../architecture-diagrams/rendered/sa-pro-multi-account-landing-zone.png) · [Editable Python source](../../architecture-diagrams/sources/sa-pro-multi-account-landing-zone.py)

<!-- GENERATED_ARCHITECTURE_DIAGRAM:END -->


Visual architecture: `../diagrams/aws-icon/sa-pro-multi-account-landing-zone.puml`

## Validate Organization Structure
```bash
aws organizations list-roots
aws organizations list-organizational-units-for-parent --parent-id <root-id>
aws organizations list-accounts
```

## Validate Identity
- Confirm workforce users authenticate through IAM Identity Center.
- Confirm permission sets map to job functions.
- Confirm no unnecessary long-lived IAM user credentials exist.

## Validate Central Logging
```bash
aws cloudtrail describe-trails
aws cloudtrail get-trail-status --name <trail-name>
```
Confirm organization events arrive in the encrypted log-archive bucket.

## Validate Guardrails
Attempt a prohibited non-production action covered by an SCP and confirm explicit denial. Record the test account, policy, expected result, and evidence.

## Validate Security Aggregation
Confirm GuardDuty and Security Hub delegated administration and member-account coverage.

## Exit Criteria
- Required OUs and accounts exist.
- Federated access works.
- Central logging is complete.
- Guardrails prevent tested prohibited actions.
- Security findings aggregate centrally.
- Account owners and cost metadata are documented.
