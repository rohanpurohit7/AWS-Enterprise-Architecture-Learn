from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Lambda
from diagrams.aws.integration import StepFunctions
from diagrams.aws.storage import S3
from diagrams.aws.analytics import ElasticsearchService
from diagrams.aws.management import Cloudwatch
from diagrams.aws.network import APIGateway

OUT = "AWS-Enterprise-Architecture-Handbook/docs/diagrams/rendered/bedrock-rag-agent-security"
with Diagram("Bedrock RAG Agent Security", filename=OUT, outformat="png", show=False, direction="LR"):
    api = APIGateway("Governed RAG API")
    with Cluster("AI Application Boundary"):
        orchestrator = Lambda("Bedrock RAG Orchestrator")
        approval = StepFunctions("Human Approval")
    with Cluster("Approved Knowledge Plane"):
        knowledge = S3("Approved Knowledge Corpus")
        index = ElasticsearchService("Retrieval Index")
    telemetry = Cloudwatch("Model & App Telemetry")
    api >> orchestrator
    orchestrator >> [knowledge, index, approval]
    knowledge >> index
    [orchestrator, approval] >> Edge(label="audit") >> telemetry
