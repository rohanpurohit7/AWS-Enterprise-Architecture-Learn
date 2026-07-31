from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.network import PrivateLink, VPC
from diagrams.aws.security import KMS
from diagrams.aws.storage import S3

OUT = "AWS-Enterprise-Architecture-Handbook/docs/diagrams/rendered/networking-private-service-access"

with Diagram("Private Service Access with AWS PrivateLink", filename=OUT, outformat="png", show=False, direction="LR"):
    with Cluster("Consumer VPC"):
        consumer = EC2("Consumer workload")
        endpoint = PrivateLink("Interface endpoint")
        consumer >> endpoint

    with Cluster("Provider VPC"):
        service = EC2("Private service")
        provider_vpc = VPC("Provider network")
        service >> provider_vpc

    endpoint >> Edge(label="PrivateLink") >> provider_vpc
    service >> S3("Service data")
    service >> KMS("KMS encryption")
