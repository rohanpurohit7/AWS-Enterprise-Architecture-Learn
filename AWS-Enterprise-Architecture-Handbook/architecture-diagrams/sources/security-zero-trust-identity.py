from diagrams import Diagram, Cluster, Edge
from diagrams.aws.network import APIGateway, VPC
from diagrams.aws.compute import Lambda
from diagrams.aws.integration import Eventbridge, SQS, StepFunctions
from diagrams.aws.database import Dynamodb
from diagrams.aws.storage import S3
from diagrams.aws.management import Cloudwatch

OUT = "AWS-Enterprise-Architecture-Handbook/docs/diagrams/rendered/security-zero-trust-identity"
with Diagram("Zero Trust Identity and Access", filename=OUT, outformat="png", show=False, direction="LR"):
    entry = APIGateway("Identity-Aware Entry")
    with Cluster("Policy Enforcement"):
        auth = Lambda("Authorization Service")
        events = Eventbridge("Access Events")
        review = SQS("Access Review Queue")
        approval = StepFunctions("Approval Workflow")
    with Cluster("Private Application Boundary"):
        app = VPC("Private Application VPC")
        state = Dynamodb("Access Decision State")
        evidence = S3("Audit Evidence")
    telemetry = Cloudwatch("Access Telemetry")
    entry >> auth >> events >> review >> approval
    approval >> [app, state, evidence]
    [auth, approval] >> Edge(label="audit") >> telemetry
