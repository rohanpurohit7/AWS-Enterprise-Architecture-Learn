# Centralized Transit Gateway and Inspection VPC

<!-- GENERATED_ARCHITECTURE_DIAGRAM:START -->

## Rendered Architecture Diagram

![Transit Gateway Inspection Vpc](rendered/transit-gateway-inspection-vpc.png)

[Central rendered asset](../../architecture-diagrams/rendered/transit-gateway-inspection-vpc.png) · [Editable Python source](../../architecture-diagrams/sources/transit-gateway-inspection-vpc.py)

<!-- GENERATED_ARCHITECTURE_DIAGRAM:END -->


![Source diagram](../diagrams/aws-icon/transit-gateway-inspection-vpc.puml)

## Case Study

A regulated enterprise operates multiple workload accounts and requires centralized east-west and north-south inspection without exposing application VPCs directly to the internet.

## Business Objective

- standardize egress controls
- isolate production, development, and data environments
- provide centralized firewall policy and evidence
- simplify onboarding of new VPCs
- preserve route symmetry for stateful inspection

## Technical Approach

Workload VPCs attach to an AWS Transit Gateway. Segmented TGW route tables forward approved traffic through an inspection VPC. AWS Network Firewall or a supported NGFW inspects flows before NAT Gateway and Internet Gateway egress. Firewall, VPC Flow Log, and Transit Gateway telemetry are centralized.

## Configuration Steps

1. Create a dedicated network account.
2. Create a Transit Gateway and segmented route tables.
3. Build an inspection VPC with firewall endpoints in each AZ.
4. Enable appliance mode on the inspection attachment.
5. Add one NAT Gateway per AZ in dedicated egress subnets.
6. Attach workload VPCs and propagate only approved routes.
7. Route default egress from workload TGW route tables to inspection.
8. Route inspected traffic to the correct AZ-local NAT Gateway.
9. Configure firewall stateful and stateless rule groups.
10. Send firewall logs to S3, CloudWatch, Security Lake, or SIEM.
11. Validate symmetric return paths.

## Validation

```bash
aws ec2 describe-transit-gateways
aws ec2 describe-transit-gateway-route-tables
aws network-firewall describe-firewall --firewall-name <name>
aws logs describe-log-groups
```

## Security and Privacy

Keep production and nonproduction routes separated. Deny unapproved inter-VPC connectivity. Redact sensitive fields before downstream analytics and restrict firewall-log access.

## Failure Scenarios

Test firewall endpoint failure, NAT Gateway failure, route-table mistakes, asymmetric routing, DNS failure, and capacity limits.
