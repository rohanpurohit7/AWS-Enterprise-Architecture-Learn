# Private Service Access with AWS PrivateLink

<!-- GENERATED_ARCHITECTURE_DIAGRAM:START -->

## Rendered Architecture Diagram

![Networking Private Service Access](rendered/networking-private-service-access.png)

[Central rendered asset](../../architecture-diagrams/rendered/networking-private-service-access.png) · [Editable Python source](../../architecture-diagrams/sources/networking-private-service-access.py)

<!-- GENERATED_ARCHITECTURE_DIAGRAM:END -->


Architecture: `../diagrams/aws-icon/networking-private-service-access.puml`

## Case Study
A platform team operates a shared internal fraud-scoring API. Multiple business VPCs must consume the service without internet exposure, broad VPC peering, or transitive network access.

## Business Objective
Provide scalable private service consumption while minimizing routing complexity and limiting consumers to the exact service they are authorized to use.

## Technical Approach
Expose the provider service through a Network Load Balancer and VPC endpoint service. Consumers create interface VPC endpoints in selected subnets and use private DNS. Security groups constrain endpoint access.

## Configuration Steps
1. Deploy the provider service in private subnets across at least two Availability Zones.
2. Create a Network Load Balancer targeting healthy provider workloads.
3. Create an endpoint service backed by the NLB.
4. Configure allowed principals or acceptance requirements.
5. In each consumer VPC, create interface endpoints in private application subnets.
6. Attach restrictive endpoint security groups.
7. Enable private DNS only after validating domain ownership and naming requirements.
8. Configure Route 53 private hosted zones where custom internal names are needed.
9. Enable NLB, application, and VPC Flow Log telemetry.
10. Monitor endpoint connections and remove stale consumers.

## Validation
```bash
aws ec2 describe-vpc-endpoint-services
aws ec2 describe-vpc-endpoints
aws elbv2 describe-load-balancers
```

From a consumer workload, resolve the private name and call the service. Confirm no internet gateway or NAT path is required for the request.

## Security and Privacy
PrivateLink reduces network exposure but does not replace application authentication or authorization. Encrypt application traffic when confidentiality requires it, and avoid logging sensitive request payloads.
