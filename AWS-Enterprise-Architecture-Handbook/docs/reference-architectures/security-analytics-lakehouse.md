# Security Analytics Lakehouse with Streaming, SIEM, and ML

<!-- GENERATED_ARCHITECTURE_DIAGRAM:START -->

## Rendered Architecture Diagram

![Security Analytics Lakehouse](rendered/security-analytics-lakehouse.png)

[Central rendered asset](../../architecture-diagrams/rendered/security-analytics-lakehouse.png) · [Editable Python source](../../architecture-diagrams/sources/security-analytics-lakehouse.py)

<!-- GENERATED_ARCHITECTURE_DIAGRAM:END -->


Architecture: `../diagrams/aws-icon/security-analytics-lakehouse.puml`

## Case Study
A global enterprise needs to consolidate cloud, application, network, identity, and security telemetry for threat hunting, compliance reporting, anomaly detection, and incident response.

## Business Objective
Create a scalable evidence and analytics platform that supports near-real-time detection and long-term investigation without forcing every workload to send raw data directly to a single SIEM tier.

## Technical Approach
Use Kinesis for AWS-native event streaming and Amazon MSK/Kafka for high-volume application or cross-platform feeds. Normalize security data into Security Lake and S3. Use Glue for cataloging and ETL, EMR/Spark for large-scale feature engineering, SageMaker or Spark-based KNN/ensemble models for anomaly scoring, OpenSearch for investigation, Security Hub for normalized finding aggregation, and Detective for relationship-based investigation.

## Configuration Steps
1. Inventory telemetry sources and classify data sensitivity and retention requirements.
2. Enable organization-level CloudTrail, VPC Flow Logs, GuardDuty, WAF, EKS audit logs, and other approved sources.
3. Configure Security Lake for supported AWS security sources and selected Regions.
4. Create Kinesis streams for near-real-time event feeds requiring AWS-native streaming.
5. Create Amazon MSK clusters for Kafka-compatible producers and consumers where required.
6. Land raw and normalized events in encrypted S3 prefixes with lifecycle policies.
7. Register datasets in Glue Data Catalog and define partitioning by source, Region, account, and time.
8. Use Glue or EMR/Spark to normalize, enrich, and derive features.
9. Train or calibrate KNN and ensemble anomaly models only on approved, representative data.
10. Write anomaly scores and investigation fields to OpenSearch.
11. Convert high-confidence detections into Security Hub custom findings where operationally useful.
12. Use Detective and graph context to investigate entities and related activity.
13. Send pipeline health, lag, failure, and cost telemetry to CloudWatch.

## Detection Principles
ML anomaly scores are prioritization signals, not proof of compromise. Combine model output with deterministic detections, threat intelligence, asset criticality, identity context, and analyst judgment.

## Validation
- Confirm each required source arrives with expected latency.
- Measure Kafka/Kinesis consumer lag.
- Validate schema and partition completeness.
- Test failed-record handling and dead-letter paths.
- Measure model false-positive and false-negative behavior with labeled scenarios.
- Confirm Security Hub findings contain source provenance.

## Security and Privacy
Apply data minimization before central ingestion. Tokenize or redact unnecessary PII. Restrict query access by role and dataset. Encrypt data at rest and in transit. Separate raw evidence retention from derived analytical features. Document lawful retention and deletion requirements.
