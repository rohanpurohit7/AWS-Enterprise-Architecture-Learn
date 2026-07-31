from diagrams import Diagram, Cluster, Edge
from diagrams.aws.security import Guardduty, SecurityHub
from diagrams.aws.integration import Eventbridge, SNS
from diagrams.aws.compute import Lambda
from diagrams.aws.storage import S3
from diagrams.aws.analytics import ElasticsearchService
from diagrams.aws.management import Cloudtrail, Cloudwatch

OUT = "AWS-Enterprise-Architecture-Handbook/docs/diagrams/rendered/security-data-platform"
with Diagram("Security Data Platform", filename=OUT, outformat="png", show=False, direction="LR"):
    with Cluster("Security Telemetry Sources"):
        trail = Cloudtrail("CloudTrail")
        threats = Guardduty("GuardDuty")
    with Cluster("Detection and Enrichment"):
        hub = SecurityHub("Security Hub")
        bus = Eventbridge("Finding Router")
        enrich = Lambda("Enrichment & Triage")
    with Cluster("Security Analytics Plane"):
        lake = S3("Security Data Lake")
        search = ElasticsearchService("SIEM / Investigation")
    alerts = SNS("SOC Alerts")
    health = Cloudwatch("Pipeline Health")
    trail >> lake >> search
    threats >> hub >> bus >> enrich >> alerts
    hub >> search
    enrich >> Edge(label="metrics") >> health
