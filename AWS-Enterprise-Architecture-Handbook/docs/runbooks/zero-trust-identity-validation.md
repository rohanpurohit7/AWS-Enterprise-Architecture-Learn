# Zero Trust Identity Validation Runbook

<!-- GENERATED_ARCHITECTURE_DIAGRAM:START -->

## Rendered Architecture Diagram

![Security Zero Trust Identity](rendered/security-zero-trust-identity.png)

[Central rendered asset](../../architecture-diagrams/rendered/security-zero-trust-identity.png) · [Editable Python source](../../architecture-diagrams/sources/security-zero-trust-identity.py)

<!-- GENERATED_ARCHITECTURE_DIAGRAM:END -->


Visual architecture: `../diagrams/aws-icon/security-zero-trust-identity.puml`

## Test Cases
1. Authorized user on trusted device accesses an approved application.
2. Authorized user on untrusted device is denied or challenged according to policy.
3. Unauthorized group member is denied.
4. Workload role can access only required resources.
5. Private service is unreachable over the public internet.
6. Secrets rotate without embedding credentials in source code.

## AWS Validation
```bash
aws sso-admin list-permission-sets --instance-arn <instance-arn>
aws iam list-roles
aws ec2 describe-vpc-endpoints
aws secretsmanager list-secrets
aws cloudtrail lookup-events --max-results 20
```

## Evidence
Capture policy name, identity, application, timestamp, expected decision, observed decision, and CloudTrail event reference.

## Exit Criteria
- No broad standing credentials.
- Application access is identity-aware.
- Workload permissions are least privilege.
- Private services remain private.
- Sensitive secrets are managed and auditable.
