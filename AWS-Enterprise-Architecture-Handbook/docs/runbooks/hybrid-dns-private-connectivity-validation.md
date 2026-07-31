# Hybrid DNS and Private Connectivity Validation Runbook

<!-- GENERATED_ARCHITECTURE_DIAGRAM:START -->

## Rendered Architecture Diagram

![Hybrid Dns Private Connectivity](rendered/hybrid-dns-private-connectivity.png)

[Central rendered asset](../../architecture-diagrams/rendered/hybrid-dns-private-connectivity.png) · [Editable Python source](../../architecture-diagrams/sources/hybrid-dns-private-connectivity.py)

<!-- GENERATED_ARCHITECTURE_DIAGRAM:END -->


Architecture: `../diagrams/aws-icon/hybrid-dns-private-connectivity.puml`

## Validation Commands
```bash
aws ec2 describe-transit-gateways
aws ec2 describe-transit-gateway-attachments
aws ec2 describe-vpn-connections
aws directconnect describe-connections
aws route53resolver list-resolver-endpoints
aws route53resolver list-resolver-rules
aws ec2 describe-vpc-endpoints
```

## DNS Tests
1. Query an on-premises private zone from an AWS workload.
2. Query an AWS private hosted zone from an on-premises client.
3. Confirm the expected Resolver rule is used.
4. Confirm query logs arrive at the approved destination.
5. Test a nonexistent or unauthorized namespace and verify expected failure behavior.

## Connectivity Tests
1. Trace the primary path over Direct Connect.
2. Disable or isolate the primary path in a controlled maintenance window.
3. Verify backup VPN routing converges as designed.
4. Validate workload-to-workload routes through approved TGW route tables.
5. Confirm segmented VPCs remain unreachable when policy requires isolation.

## PrivateLink Tests
1. Resolve the interface endpoint private DNS name.
2. Connect from an approved consumer subnet.
3. Attempt access from an unapproved network and verify denial.
4. Confirm the endpoint policy and security group are scoped correctly.

## Operational Review
- Check TGW route-table associations and propagations.
- Review Resolver endpoint capacity and health.
- Review DX/VPN BGP state.
- Review DNS query logs for loops, high NXDOMAIN rates, and anomalous domains.
