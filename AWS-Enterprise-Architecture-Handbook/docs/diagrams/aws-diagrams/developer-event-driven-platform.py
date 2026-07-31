from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Dynamodb
from diagrams.aws.integration import Eventbridge, SQS, SNS
from diagrams.aws.management import Cloudwatch
from diagrams.aws.network import APIGateway

OUT = "AWS-Enterprise-Architecture-Handbook/docs/diagrams/rendered/developer-event-driven-platform"

with Diagram("Developer Event-Driven Platform", filename=OUT, outformat="png", show=False, direction="LR"):
    api = APIGateway("API Gateway")
    command = Lambda("Command handler")
    bus = Eventbridge("EventBridge bus")
    queue = SQS("Worker queue")
    topic = SNS("Notification topic")
    store = Dynamodb("DynamoDB")
    worker = Lambda("Async worker")
    monitor = Cloudwatch("CloudWatch")

    api >> command >> store
    command >> bus
    bus >> [queue, topic]
    queue >> worker >> Edge(label="update state") >> store
    [command, bus, queue, worker, store] >> monitor
