from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import EKS
from diagrams.aws.database import Aurora
from diagrams.aws.management import Cloudwatch
from diagrams.aws.network import Route53
from diagrams.aws.storage import S3

OUT = "AWS-Enterprise-Architecture-Handbook/docs/diagrams/rendered/sa-pro-disaster-recovery"

with Diagram("SA Pro Disaster Recovery", filename=OUT, outformat="png", show=False, direction="LR"):
    dns = Route53("Route 53 failover routing")

    with Cluster("Primary Region"):
        app_primary = EKS("Primary application")
        db_primary = Aurora("Primary database")
        backup_primary = S3("Backup vault")
        mon_primary = Cloudwatch("Primary monitoring")
        app_primary >> db_primary
        [app_primary, db_primary] >> mon_primary
        db_primary >> backup_primary

    with Cluster("Recovery Region"):
        app_dr = EKS("Warm standby application")
        db_dr = Aurora("Cross-Region replica")
        backup_dr = S3("Replicated backups")
        mon_dr = Cloudwatch("DR monitoring")
        app_dr >> db_dr
        [app_dr, db_dr] >> mon_dr

    dns >> [app_primary, app_dr]
    db_primary >> Edge(label="cross-Region replication") >> db_dr
    backup_primary >> Edge(label="replication") >> backup_dr
