from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import EKS
from diagrams.aws.database import Aurora
from diagrams.aws.management import Cloudwatch
from diagrams.aws.network import CloudFront, Route53
from diagrams.aws.security import WAF

OUT = "AWS-Enterprise-Architecture-Handbook/docs/diagrams/rendered/global-multi-region-active-active"

with Diagram("Global Multi-Region Active-Active", filename=OUT, outformat="png", show=False, direction="LR"):
    users = Route53("Route 53 health-based routing")
    cdn = CloudFront("CloudFront")
    waf = WAF("AWS WAF")

    with Cluster("Region A"):
        app_a = EKS("EKS service A")
        db_a = Aurora("Aurora Global DB primary")
        mon_a = Cloudwatch("CloudWatch A")
        app_a >> db_a
        [app_a, db_a] >> mon_a

    with Cluster("Region B"):
        app_b = EKS("EKS service B")
        db_b = Aurora("Aurora Global DB secondary")
        mon_b = Cloudwatch("CloudWatch B")
        app_b >> db_b
        [app_b, db_b] >> mon_b

    users >> cdn >> waf >> [app_a, app_b]
    db_a >> Edge(label="cross-Region replication") >> db_b
