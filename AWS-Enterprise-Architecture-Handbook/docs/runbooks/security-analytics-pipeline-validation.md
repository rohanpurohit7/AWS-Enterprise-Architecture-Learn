# Security Analytics Pipeline Validation Runbook

<!-- GENERATED_ARCHITECTURE_DIAGRAM:START -->

## Rendered Architecture Diagram

![Security Analytics Lakehouse](rendered/security-analytics-lakehouse.png)

[Central rendered asset](../../architecture-diagrams/rendered/security-analytics-lakehouse.png) · [Editable Python source](../../architecture-diagrams/sources/security-analytics-lakehouse.py)

<!-- GENERATED_ARCHITECTURE_DIAGRAM:END -->


Visual architecture: `../diagrams/aws-icon/security-analytics-lakehouse.puml`

## Pipeline Checks
1. Confirm source telemetry arrives in Kinesis, MSK, Security Lake, or S3.
2. Measure event latency and Kafka/Kinesis consumer lag.
3. Validate Glue catalog partitions and schema versions.
4. Run Spark/EMR transformations against a synthetic test window.
5. Confirm anomaly-scoring jobs produce bounded numeric scores and source references.
6. Verify OpenSearch receives searchable fields and timestamps.
7. Confirm Security Hub custom findings use valid schema and severity mapping.
8. Confirm Detective or investigation tooling can pivot to related entities.

## Example CLI Checks
```bash
aws kinesis list-streams
aws kafka list-clusters-v2
aws glue get-databases
aws s3 ls s3://<security-data-bucket>/
aws opensearch list-domain-names
aws securityhub get-findings --max-results 10
```

## Model Validation
- Compare anomaly scores against labeled benign and attack simulations.
- Track false positives and false negatives.
- Do not auto-contain based solely on KNN distance or ensemble score.
- Version features, training data, thresholds, and model artifacts.

## Exit Criteria
Data is complete, timely, queryable, attributable to its source, and governed by retention policy. Detection outputs are explainable enough for analyst review and do not bypass human judgment for high-impact response.
