from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.network import DirectConnect, TransitGateway, VpnGateway
from diagrams.onprem.compute import Server
from diagrams.onprem.network import Internet
from aws_diagram_nodes import Route53Resolver

OUT = "AWS-Enterprise-Architecture-Handbook/docs/diagrams/rendered/hybrid-dns-private-connectivity"

with Diagram("Hybrid DNS and Private Connectivity", filename=OUT, outformat="png", show=False, direction="LR"):
    with Cluster("On-Premises"):
        apps = Server("Enterprise applications")
        dns_onprem = Server("On-prem DNS")
        edge = Internet("Enterprise edge")
        [apps, dns_onprem] >> edge

    dx = DirectConnect("Direct Connect")
    vpn = VpnGateway("VPN backup")
    tgw = TransitGateway("Transit Gateway")

    with Cluster("AWS Shared Services VPC"):
        inbound = Route53Resolver("Resolver inbound endpoint")
        outbound = Route53Resolver("Resolver outbound endpoint")
        private_app = EC2("Private AWS workloads")

    edge >> [dx, vpn] >> tgw >> private_app
    dns_onprem >> Edge(label="AWS private zones") >> inbound >> private_app
    private_app >> Edge(label="on-prem zones") >> outbound >> dns_onprem
