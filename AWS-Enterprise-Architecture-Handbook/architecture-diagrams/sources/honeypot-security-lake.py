from diagrams import Cluster, Diagram, Edge
from diagrams.aws.analytics import KinesisDataFirehose
from diagrams.aws.compute import EC2
from diagrams.aws.integration import Eventbridge
from diagrams.aws.management import Cloudwatch
from diagrams.aws.security import Guardduty, SecurityHub
from diagrams.aws.storage import S3
from aws_diagram_nodes import OpenSearchService

OUT = "AWS-Enterprise-Architecture-Handbook/docs/diagrams/rendered/honeypot-security-lake"

with Diagram("Honeypot and Security Lake", filename=OUT, outformat="png", show=False, direction="LR"):
    with Cluster("Deception VPC"):
        honeypot = EC2("Instrumented honeypot")
        telemetry = Cloudwatch("Logs and metrics")
        honeypot >> telemetry

    firehose = KinesisDataFirehose("Kinesis Data Firehose")
    lake = S3("Security data lake")
    detect = Guardduty("GuardDuty")
    hub = SecurityHub("Security Hub")
    events = Eventbridge("EventBridge")
    search = OpenSearchService("OpenSearch analytics")

    telemetry >> firehose >> lake
    lake >> [detect, search]
    detect >> hub >> events
    events >> Edge(label="triage and response") >> search
