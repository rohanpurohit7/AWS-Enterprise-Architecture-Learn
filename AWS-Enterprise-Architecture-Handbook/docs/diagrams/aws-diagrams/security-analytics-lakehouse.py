from diagrams import Cluster, Diagram, Edge
from diagrams.aws.analytics import Athena, Glue, KinesisDataFirehose
from diagrams.aws.compute import Lambda
from diagrams.aws.security import SecurityHub
from diagrams.aws.storage import S3
from aws_diagram_nodes import OpenSearchService

OUT = "AWS-Enterprise-Architecture-Handbook/docs/diagrams/rendered/security-analytics-lakehouse"

with Diagram("Security Analytics Lakehouse", filename=OUT, outformat="png", show=False, direction="LR"):
    hub = SecurityHub("Security Hub findings")
    firehose = KinesisDataFirehose("Firehose ingestion")

    with Cluster("Security Data Lake"):
        raw = S3("Raw security data")
        curated = S3("Curated lakehouse")
        catalog = Glue("Glue catalog and ETL")
        raw >> catalog >> curated

    enrich = Lambda("Normalization and enrichment")
    query = Athena("Athena investigations")
    search = OpenSearchService("OpenSearch detections")

    hub >> firehose >> raw
    raw >> enrich >> curated
    curated >> [query, search]
    search >> Edge(label="prioritized findings") >> hub
