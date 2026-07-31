from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import EKS
from diagrams.aws.database import Aurora
from diagrams.aws.management import Cloudtrail, Cloudwatch
from diagrams.aws.network import ALB, CloudFront, InternetGateway, NATGateway, Route53
from diagrams.aws.security import KMS, SecurityHub, WAF

OUT = "AWS-Enterprise-Architecture-Handbook/docs/diagrams/rendered/secure-multi-az-application"

with Diagram(
    "Secure Multi-AZ Application",
    filename=OUT,
    outformat="png",
    show=False,
    direction="LR",
    graph_attr={"splines": "spline", "nodesep": "0.7", "ranksep": "1.0"},
):
    dns = Route53("Route 53")
    edge = CloudFront("CloudFront")
    waf = WAF("AWS WAF")

    with Cluster("AWS Region"):
        igw = InternetGateway("Internet Gateway")
        alb = ALB("Application Load Balancer")

        with Cluster("VPC 10.20.0.0/16"):
            with Cluster("Availability Zone A"):
                with Cluster("Public Subnet"):
                    nat_a = NATGateway("NAT Gateway A")
                with Cluster("Private App Subnet"):
                    eks_a = EKS("EKS workloads A")
                with Cluster("Isolated Data Subnet"):
                    db_a = Aurora("Aurora writer")

            with Cluster("Availability Zone B"):
                with Cluster("Public Subnet"):
                    nat_b = NATGateway("NAT Gateway B")
                with Cluster("Private App Subnet"):
                    eks_b = EKS("EKS workloads B")
                with Cluster("Isolated Data Subnet"):
                    db_b = Aurora("Aurora reader")

        kms = KMS("KMS")
        cloudtrail = Cloudtrail("CloudTrail")
        cloudwatch = Cloudwatch("CloudWatch")
        security_hub = SecurityHub("Security Hub")

    dns >> edge >> waf >> alb
    alb >> [eks_a, eks_b]
    eks_a >> Edge(label="private DB") >> db_a
    eks_b >> Edge(label="private DB") >> db_b
    db_a >> Edge(label="replication") >> db_b
    eks_a >> Edge(label="egress") >> nat_a >> igw
    eks_b >> Edge(label="egress") >> nat_b >> igw
    [eks_a, eks_b, db_a, db_b] >> kms
    [alb, eks_a, eks_b, db_a, db_b] >> cloudwatch
    [cloudtrail, cloudwatch] >> security_hub
