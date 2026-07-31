from diagrams import Diagram, Cluster
from diagrams.aws.network import APIGateway
from diagrams.aws.compute import Lambda
from diagrams.aws.integration import Eventbridge, SQS, StepFunctions
from diagrams.aws.database import Dynamodb
from diagrams.aws.storage import S3
from diagrams.aws.management import Cloudwatch

OUT = "AWS-Enterprise-Architecture-Handbook/docs/diagrams/rendered/serverless-data-lake-analytics"
with Diagram("Serverless Data Lake Analytics", filename=OUT, outformat="png", show=False, direction="LR"):
    api = APIGateway("Data Ingestion API")
    with Cluster("Serverless Ingestion and Processing"):
        processor = Lambda("Validation & Enrichment")
        events = Eventbridge("Data Events")
        queue = SQS("Processing Queue")
        workflow = StepFunctions("Data Workflow")
    with Cluster("Governed Data Lake"):
        lake = S3("Raw & Curated Data Lake")
        metadata = Dynamodb("Pipeline Metadata")
    telemetry = Cloudwatch("Pipeline Telemetry")
    api >> processor >> events >> queue >> workflow
    workflow >> [lake, metadata]
    processor >> telemetry
