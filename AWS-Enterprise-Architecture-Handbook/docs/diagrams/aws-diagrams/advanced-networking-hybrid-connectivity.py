from diagrams import Cluster, Diagram, Edge
from diagrams.aws.network import DirectConnect, TransitGateway, VpnGateway, Route53Resolver
from diagrams.aws.security import NetworkFirewall
from diagrams.onprem.network import Internet
from diagrams.onprem.compute import Server

OUT = "AWS-Enterprise-Architecture-Handbook/docs/diagrams/rendered/advanced-networking-hybrid-connectivity"

with Diagram("Advanced Networking Hybrid Connectivity", filename=OUT, outformat="png", show=False, direction="LR"):
    with Cluster("On-Premises"):
        users = Server("Enterprise applications")
        edge = Internet("WAN edge")
        users >> edge

    dx = DirectConnect("Direct Connect")
    vpn = VpnGateway("Site-to-Site VPN")
    tgw = TransitGateway("Transit Gateway")
    firewall = NetworkFirewall("Inspection VPC")
    dns = Route53Resolver("Route 53 Resolver")

    with Cluster("AWS Spoke VPCs"):
        prod = Server("Production VPC")
        shared = Server("Shared services VPC")
        dev = Server("Development VPC")

    edge >> [dx, vpn] >> tgw >> firewall >> [prod, shared, dev]
    dns >> Edge(label="hybrid DNS") >> [shared, users]
