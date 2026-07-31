from diagrams import Diagram, Cluster, Edge
from diagrams.aws.network import TransitGateway, VPC, NATGateway, NetworkFirewall
from diagrams.aws.management import Cloudwatch
from diagrams.aws.storage import S3

OUT = "AWS-Enterprise-Architecture-Handbook/docs/diagrams/rendered/transit-gateway-inspection-vpc"
with Diagram("Transit Gateway Inspection VPC", filename=OUT, outformat="png", show=False, direction="LR"):
    with Cluster("Spoke VPCs"):
        prod = VPC("Production VPC")
        data = VPC("Data VPC")
    tgw = TransitGateway("Transit Gateway")
    with Cluster("Central Inspection VPC"):
        inspection = VPC("Inspection VPC")
        firewall = NetworkFirewall("AWS Network Firewall")
        nat = NATGateway("Controlled Egress")
    telemetry = Cloudwatch("Network Telemetry")
    logs = S3("Firewall Log Archive")
    [prod, data] >> tgw >> inspection >> firewall >> nat
    firewall >> Edge(label="metrics") >> telemetry
    firewall >> Edge(label="logs") >> logs
