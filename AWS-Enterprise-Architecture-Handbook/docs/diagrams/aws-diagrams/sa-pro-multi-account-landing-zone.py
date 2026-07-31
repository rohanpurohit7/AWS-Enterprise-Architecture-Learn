from diagrams import Cluster, Diagram
from diagrams.aws.management import Organizations, ControlTower, Cloudtrail, Config
from diagrams.aws.security import SecurityHub, Guardduty
from diagrams.aws.network import TransitGateway
from diagrams.aws.storage import S3

OUT = "AWS-Enterprise-Architecture-Handbook/docs/diagrams/rendered/sa-pro-multi-account-landing-zone"

with Diagram("SA Pro Multi-Account Landing Zone", filename=OUT, outformat="png", show=False, direction="TB"):
    org = Organizations("AWS Organizations")
    tower = ControlTower("AWS Control Tower")

    with Cluster("Security OU"):
        log = S3("Log archive account")
        audit = SecurityHub("Audit account")
        guard = Guardduty("GuardDuty admin")

    with Cluster("Infrastructure OU"):
        network = TransitGateway("Network account")
        shared = Config("Shared services account")

    with Cluster("Workload OUs"):
        prod = Cloudtrail("Production accounts")
        nonprod = Cloudtrail("Non-production accounts")
        sandbox = Cloudtrail("Sandbox accounts")

    org >> tower
    tower >> [log, audit, guard, network, shared, prod, nonprod, sandbox]
    [prod, nonprod, sandbox] >> log
    [prod, nonprod, sandbox] >> audit
    network >> [prod, nonprod, sandbox]
