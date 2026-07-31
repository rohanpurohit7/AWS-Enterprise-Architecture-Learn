# Serverless Data Lake and Analytics Reference Architecture

<!-- GENERATED_ARCHITECTURE_DIAGRAM:START -->

## Rendered Architecture Diagram

![Serverless Data Lake Analytics](rendered/serverless-data-lake-analytics.png)

[Central rendered asset](../../architecture-diagrams/rendered/serverless-data-lake-analytics.png) · [Editable Python source](../../architecture-diagrams/sources/serverless-data-lake-analytics.py)

<!-- GENERATED_ARCHITECTURE_DIAGRAM:END -->


Architecture source: `../diagrams/aws-icon/serverless-data-lake-analytics.puml`

## Case Study
A regulated enterprise wants to ingest application, operational, and security events at variable scale, preserve raw evidence, create governed curated datasets, and support interactive analytics without maintaining a large always-on cluster.

## Business Objective
- Decouple ingestion from analytics.
- Retain immutable raw data for investigation and replay.
- Reduce operational overhead with managed and serverless services.
- Enforce encryption, retention, and access boundaries.
- Support both ad hoc SQL and near-real-time search.

## Technical Approach
Kinesis Data Streams and EventBridge receive streaming and event-driven inputs. Lambda performs lightweight validation and enrichment before writing immutable objects to an S3 raw zone. AWS Glue catalogs data and performs scheduled or event-driven transformation into curated S3 prefixes. Athena supports serverless SQL, while OpenSearch provides indexed operational and security exploration.

## Data Zones
- `raw/`: append-only source records with limited write principals.
- `validated/`: schema-checked and normalized events.
- `curated/`: analytics-ready datasets partitioned for common access patterns.
- `quarantine/`: malformed or policy-violating records for investigation.

## Configuration Steps
1. Create dedicated analytics and logging accounts where organizational separation is required.
2. Create S3 buckets or prefixes for raw, validated, curated, and quarantine zones.
3. Enable versioning, encryption, lifecycle policies, and object ownership controls.
4. Create KMS keys with key policies that separate producers, processors, and analysts.
5. Create Kinesis streams sized for expected throughput and shard scaling strategy.
6. Configure EventBridge buses and rules for discrete application or security events.
7. Deploy Lambda validation/enrichment functions with least-privilege execution roles.
8. Configure dead-letter handling for failed events.
9. Register datasets in the Glue Data Catalog.
10. Create Glue jobs or workflows for transformations that exceed Lambda execution needs.
11. Partition curated S3 data by time and high-value query dimensions.
12. Create Athena workgroups with query-result encryption and cost controls.
13. Index selected operational data into OpenSearch rather than duplicating all lake data.
14. Send service logs, errors, throttles, and pipeline lag metrics to CloudWatch.
15. Apply Lake Formation or equivalent governance controls when centralized fine-grained data permissions are required.

## Security and Privacy
- Minimize PII before ingestion where feasible.
- Tokenize or hash identifiers used only for correlation.
- Restrict raw-zone access to investigation and engineering roles.
- Apply S3 Block Public Access and explicit bucket policies.
- Use VPC endpoints for private access from VPC-based processors.
- Define retention by data class rather than keeping all telemetry indefinitely.

## Scalability
Kinesis scales streaming ingestion, S3 decouples storage from compute, Glue scales transformation jobs, and Athena scales per query. OpenSearch capacity should be sized only for datasets requiring indexed search.

## Validation
- Replay a known event through the pipeline.
- Verify raw evidence is preserved unchanged.
- Confirm transformed data appears in the expected curated partition.
- Query the curated dataset through Athena.
- Confirm a selected event is searchable in OpenSearch.
- Test malformed input and verify quarantine/DLQ behavior.

## Cost Controls
- Use S3 lifecycle transitions.
- Partition Athena datasets to reduce scanned bytes.
- Avoid indexing low-value bulk data in OpenSearch.
- Right-size Kinesis capacity mode and retention.
- Monitor Glue DPU usage and Lambda duration.

## Well-Architected Review
The architecture favors loose coupling and managed services. The main design decisions are data retention, schema governance, encryption/key ownership, replay strategy, and deciding which data genuinely needs low-latency indexed search.
