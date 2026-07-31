# Hybrid Enterprise Connectivity with Direct Connect, VPN, Transit Gateway, and Central Inspection

<!-- GENERATED_ARCHITECTURE_DIAGRAM:START -->

## Rendered Architecture Diagram

![Advanced Networking Hybrid Connectivity](rendered/advanced-networking-hybrid-connectivity.png)

[Central rendered asset](../../architecture-diagrams/rendered/advanced-networking-hybrid-connectivity.png) · [Editable Python source](../../architecture-diagrams/sources/advanced-networking-hybrid-connectivity.py)

<!-- GENERATED_ARCHITECTURE_DIAGRAM:END -->


## Case Study
A large enterprise connects on-premises data centers to multiple AWS workload VPCs while requiring resilient connectivity, centralized inspection, controlled egress, and shared network services.

## Business Objective
Provide a scalable hybrid network architecture that reduces point-to-point routing complexity and keeps private workloads behind centralized security inspection.

## Technical Approach
Use AWS Direct Connect as the primary hybrid path, Site-to-Site VPN as an alternate path, Transit Gateway as the routing hub, and an inspection VPC containing AWS Network Firewall or an approved NGFW. Workload VPCs attach to Transit Gateway and approved internet egress passes through inspection and NAT.

Architecture source: `../diagrams/aws-icon/advanced-networking-hybrid-connectivity.puml`

## Configuration Steps
1. Create Transit Gateway in the network account.
2. Define segmented Transit Gateway route tables for production, non-production, shared services, and inspection.
3. Attach workload VPCs using dedicated attachment subnets.
4. Build the inspection VPC across multiple Availability Zones.
5. Deploy AWS Network Firewall or an approved NGFW in inspection subnets.
6. Enable appliance mode where required for symmetric stateful inspection.
7. Configure Direct Connect connectivity and gateway associations.
8. Configure Site-to-Site VPN according to failover routing policy.
9. Route private workload traffic to Transit Gateway.
10. Route approved egress through inspection and NAT Gateways.
11. Enable VPC Flow Logs, firewall logs, and Transit Gateway telemetry.
12. Validate internal DNS and shared-services reachability.

## Security and Privacy
- Segment routing domains.
- Avoid indiscriminate route propagation.
- Inspect selected north-south and east-west traffic.
- Prefer private AWS service endpoints.
- Centralize logs while minimizing sensitive payload collection.

## Validation
Test Direct Connect and VPN paths, symmetric inspection, firewall allow/deny policy, unintended internet routes, and log delivery.

## Failure Scenarios
Test Availability Zone failure, NAT failure, hybrid-path failover, route errors, and firewall-policy rollback.
