# Hybrid Networking and Inspection Validation Runbook

<!-- GENERATED_ARCHITECTURE_DIAGRAM:START -->

## Rendered Architecture Diagram

![Advanced Networking Hybrid Connectivity](rendered/advanced-networking-hybrid-connectivity.png)

[Central rendered asset](../../architecture-diagrams/rendered/advanced-networking-hybrid-connectivity.png) · [Editable Python source](../../architecture-diagrams/sources/advanced-networking-hybrid-connectivity.py)

<!-- GENERATED_ARCHITECTURE_DIAGRAM:END -->


Architecture: `../diagrams/aws-icon/advanced-networking-hybrid-connectivity.puml`

## Objective
Validate Direct Connect, VPN backup connectivity, Transit Gateway routing, centralized inspection, NAT egress, and network telemetry.

## Validation Steps
1. Confirm Direct Connect virtual interface and gateway status.
2. Confirm Site-to-Site VPN tunnels are established according to the resilience design.
3. Inspect Transit Gateway attachments and route tables.
4. Confirm production, non-production, shared-services, and inspection routes are segmented as designed.
5. Confirm workload VPC traffic traverses the intended inspection attachment.
6. Validate AWS Network Firewall or NGFW policy enforcement with approved and denied test traffic.
7. Confirm return traffic follows a symmetric path for stateful inspection.
8. Confirm internet-bound traffic exits through the intended NAT path.
9. Validate private AWS service access through VPC endpoints where configured.
10. Confirm VPC Flow Logs and firewall telemetry reach the central monitoring destination.

## Useful Checks
```bash
aws ec2 describe-transit-gateway-attachments
aws ec2 describe-transit-gateway-route-tables
aws ec2 describe-vpn-connections
aws ec2 describe-route-tables
aws ec2 describe-nat-gateways
```

## Failure Tests
- Withdraw or disable the primary hybrid path in a controlled maintenance test and verify backup routing.
- Test an inspection Availability Zone outage.
- Test a firewall rule rollback.
- Verify that a route-table error is detected before broad propagation.

## Success Criteria
Approved traffic follows the intended primary path, backup connectivity operates as designed, inspection is symmetric, unauthorized routes are absent, and network telemetry is centrally available.
