# Edge and Global Delivery Validation Runbook

<!-- GENERATED_ARCHITECTURE_DIAGRAM:START -->

## Rendered Architecture Diagram

![Edge Global Delivery](rendered/edge-global-delivery.png)

[Central rendered asset](../../architecture-diagrams/rendered/edge-global-delivery.png) · [Editable Python source](../../architecture-diagrams/sources/edge-global-delivery.py)

<!-- GENERATED_ARCHITECTURE_DIAGRAM:END -->


Architecture: `../diagrams/aws-icon/edge-global-delivery.puml`

## Build Validation
```bash
aws route53 list-hosted-zones
aws cloudfront list-distributions
aws wafv2 list-web-acls --scope CLOUDFRONT --region us-east-1
aws elbv2 describe-load-balancers
aws eks list-clusters
aws globalaccelerator list-accelerators --region us-west-2
```

## Functional Tests
1. Resolve the production DNS name and confirm expected routing.
2. Request a cacheable asset twice and compare cache headers.
3. Verify the origin is not directly public where CloudFront is intended to be the only path.
4. Trigger a controlled WAF test rule and confirm the request is blocked and logged.
5. Remove one regional target from service and verify health-based routing behavior.
6. Confirm the ALB reaches only private application targets.

## Monitoring
Track:
- CloudFront 4xx/5xx rates and cache hit ratio.
- ALB target response time and unhealthy host count.
- WAF blocked and allowed requests.
- Route 53 health-check status.
- Global Accelerator endpoint health.

## Security Validation
- Confirm S3 public access block is enabled for static origins.
- Confirm ALB security groups accept only required ingress.
- Confirm application security groups accept only ALB traffic.
- Confirm TLS policies meet organizational standards.
- Confirm access logs do not expose unnecessary sensitive fields.

## Failure Exercise
1. Mark Region A application targets unhealthy.
2. Observe Route 53 or Global Accelerator shift traffic.
3. Confirm alarms and incident notifications.
4. Restore Region A and verify controlled recovery.
5. Record recovery time and user-visible impact.
