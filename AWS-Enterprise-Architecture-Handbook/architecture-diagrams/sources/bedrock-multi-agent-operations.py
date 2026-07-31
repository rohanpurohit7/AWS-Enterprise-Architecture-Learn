from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Lambda
from diagrams.aws.integration import Eventbridge, SQS, StepFunctions
from diagrams.aws.database import Dynamodb
from diagrams.aws.storage import S3
from diagrams.aws.management import Cloudwatch
from diagrams.aws.network import APIGateway

OUT = "AWS-Enterprise-Architecture-Handbook/docs/diagrams/rendered/bedrock-multi-agent-operations"
with Diagram("Bedrock Multi-Agent Operations", filename=OUT, outformat="png", show=False, direction="LR"):
    api = APIGateway("Governed Agent API")
    with Cluster("Agent Orchestration"):
        supervisor = Lambda("Bedrock Supervisor Adapter")
        events = Eventbridge("Security & Ops Events")
        queue = SQS("Agent Work Queue")
        workflow = StepFunctions("Approval Workflow")
    with Cluster("Governed Knowledge and State"):
        state = Dynamodb("Case & Approval State")
        runbooks = S3("Approved Runbooks")
    telemetry = Cloudwatch("Agent Telemetry")
    api >> supervisor >> events >> queue >> workflow
    workflow >> [state, runbooks]
    [supervisor, workflow] >> Edge(label="audit") >> telemetry
