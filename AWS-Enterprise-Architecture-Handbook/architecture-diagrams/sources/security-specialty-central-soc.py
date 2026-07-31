from diagrams import Cluster, Diagram
from diagrams.aws.integration import Eventbridge, SQS
from diagrams.aws.management import Cloudtrail, Cloudwatch
from diagrams.aws.security import Guardduty, Inspector, SecurityHub
from diagrams.aws.storage import S3
from aws_diagram_nodes import OpenSearchService

OUT = "AWS-Enterprise-Architecture-Handbook/docs/diagrams/rendered/security-specialty-central-soc"

with Diagram("Central Security Operations Center", filename=OUT, outformat="png", show=False, direction="LR"):
    with Cluster("Member Accounts"):
        trail = Cloudtrail("CloudTrail")
        logs = Cloudwatch("CloudWatch Logs")
        guard = Guardduty("GuardDuty")
        inspect = Inspector("Inspector")

    hub = SecurityHub("Delegated Security Hub")
    bus = Eventbridge("EventBridge")
    queue = SQS("Investigation queue")
    archive = S3("Immutable evidence archive")
    search = OpenSearchService("SOC analytics")

    [trail, logs, guard, inspect] >> hub
    hub >> bus >> queue
    hub >> archive
    [archive, queue] >> search
