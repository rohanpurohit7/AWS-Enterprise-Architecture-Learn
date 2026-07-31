# Hybrid DNS and Private Connectivity Reference Architecture

<!-- GENERATED_ARCHITECTURE_DIAGRAM:START -->

## Rendered Architecture Diagram

![Hybrid Dns Private Connectivity](rendered/hybrid-dns-private-connectivity.png)

[Central rendered asset](../../architecture-diagrams/rendered/hybrid-dns-private-connectivity.png) · [Editable Python source](../../architecture-diagrams/sources/hybrid-dns-private-connectivity.py)

<!-- GENERATED_ARCHITECTURE_DIAGRAM:END -->


Architecture source: `../diagrams/aws-icon/hybrid-dns-private-connectivity.puml`

## Case Study
An enterprise operates on-premises applications and multiple AWS accounts. Workloads must resolve private DNS names in both directions, consume services privately, and maintain resilient hybrid connectivity without sending internal service traffic across the public internet.

## Business Objective
- Provide consistent private name resolution across on-premises and AWS.
- Maintain resilient private connectivity.
- Centralize shared DNS and routing controls.
- Reduce internet exposure through PrivateLink and interface endpoints.

## Technical Approach
Direct Connect provides primary hybrid connectivity and Site-to-Site VPN provides a backup path. Transit Gateway centralizes VPC connectivity. Route 53 Resolver inbound and outbound endpoints forward selected DNS namespaces between environments. PrivateLink and VPC interface endpoints expose approved services privately to consumer VPCs.

## Network Layout
- Shared Services VPC hosts Resolver endpoints.
- Workload VPCs remain separately routed and governed.
- Transit Gateway connects workload, shared-services, and hybrid attachments.
- Route tables are segmented by environment and trust zone.

## Configuration Steps
1. Establish non-overlapping CIDR plans for on-premises and AWS VPCs.
2. Provision Direct Connect with resilient virtual interfaces where required.
3. Configure Site-to-Site VPN as backup or interim connectivity.
4. Create a Transit Gateway in the central network account.
5. Attach Shared Services and workload VPCs.
6. Create TGW route tables for production, non-production, shared services, and inspection as required.
7. Deploy Route 53 Resolver inbound endpoints in at least two subnets/AZs.
8. Deploy Route 53 Resolver outbound endpoints.
9. Create forwarding rules for on-premises DNS namespaces.
10. Configure on-premises DNS conditional forwarding for AWS private zones.
11. Associate Resolver rules with authorized VPCs.
12. Enable Route 53 Resolver query logging.
13. Create interface VPC endpoints for supported AWS services.
14. Create endpoint services/PrivateLink patterns for private producer-consumer applications.
15. Restrict endpoint security groups to approved consumer networks.

## Security
- Treat DNS as security-relevant telemetry.
- Restrict Resolver endpoint security groups to known DNS sources.
- Use least-privilege endpoint policies where supported.
- Segment TGW routing to prevent unintended east-west reachability.
- Avoid broad `0.0.0.0/0` propagation between trust zones.

## Privacy
DNS query logs can reveal sensitive internal hostnames and application relationships. Apply access controls, retention limits, and centralized monitoring accordingly.

## Validation
- Resolve an on-premises name from an AWS workload.
- Resolve an AWS private hosted-zone name from on premises.
- Fail the primary hybrid path and verify VPN routing.
- Confirm a PrivateLink consumer can reach only the published service.
- Verify unrelated VPCs cannot use restricted endpoints.

## Failure Modes
- Resolver endpoint security-group errors.
- Routing asymmetry across DX/VPN.
- Overlapping CIDRs.
- Incorrect conditional forwarding loops.
- Excessively broad TGW route propagation.

## Well-Architected Review
Hybrid DNS and routing should be designed as shared platform capabilities with clear ownership, change control, observability, and tested failover procedures.
