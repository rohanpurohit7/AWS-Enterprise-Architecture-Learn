from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import Lambda
from diagrams.aws.network import CloudFront, Route53
from diagrams.aws.security import WAF
from diagrams.aws.storage import S3

OUT = "AWS-Enterprise-Architecture-Handbook/docs/diagrams/rendered/edge-global-delivery"

with Diagram("Edge and Global Delivery", filename=OUT, outformat="png", show=False, direction="LR"):
    dns = Route53("Route 53")
    cdn = CloudFront("CloudFront global edge")
    waf = WAF("AWS WAF")
    edge_logic = Lambda("Lambda@Edge logic")

    with Cluster("Regional Origins"):
        origin_a = S3("Static origin")
        origin_b = S3("Secondary origin")

    dns >> cdn >> waf >> edge_logic
    edge_logic >> Edge(label="origin routing") >> [origin_a, origin_b]
