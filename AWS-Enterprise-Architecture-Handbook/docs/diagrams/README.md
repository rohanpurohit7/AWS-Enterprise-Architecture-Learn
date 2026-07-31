# AWS Architecture Diagram Gallery

The canonical root library is [AWS Architecture-as-Code Library](../../architecture-diagrams/README.md).

## How GitHub Actions Builds and Publishes the Diagrams

```mermaid
flowchart TD
    A[Push to master or workflow_dispatch] --> B[Checkout repository]
    B --> C[Install Python 3.12, Graphviz, diagrams]
    C --> D[Discover diagram Python files across handbook subfolders]
    D --> E[Copy sources into architecture-diagrams/sources]
    E --> F[Validate every Python and AWS icon import]
    F --> G[Run scripts/render_aws_diagrams.py]
    G --> H[Execute each root source with runpy]
    H --> I[Graphviz generates AWS-icon PNGs]
    I --> J[Promote images into architecture-diagrams/rendered]
    J --> K[Find matching architecture Markdown documents]
    K --> L[Copy PNG into each document folder/rendered]
    L --> M[Insert managed diagram links in each article]
    M --> N[Generate catalog and gallery]
    N --> O[Validate central and local publication coverage]
    O --> P[github-actions bot commits generated assets]
```

### Source and command map

| Stage | Source or command | Result |
|---|---|---|
| Discovery | `AWS-Enterprise-Architecture-Handbook/**/diagrams/**/*.py` | Architecture source inventory |
| Root consolidation | `architecture-diagrams/sources/*.py` | Canonical editable definitions |
| Renderer | `python AWS-Enterprise-Architecture-Handbook/scripts/render_aws_diagrams.py` | Executes all definitions |
| Central publication | `architecture-diagrams/rendered/*.png` | Root diagram library |
| Compatibility publication | `docs/diagrams/rendered/*.png` | Existing gallery paths remain valid |
| Local publication | `<architecture-document-folder>/rendered/<name>.png` | Diagram beside the article/runbook |
| Inventory | `architecture-diagrams/catalog.json` | Source-to-document-to-image traceability |


## Advanced Networking Hybrid Connectivity

![advanced-networking-hybrid-connectivity](rendered/advanced-networking-hybrid-connectivity.png)

[Root source](../../architecture-diagrams/sources/advanced-networking-hybrid-connectivity.py) · [Root rendered asset](../../architecture-diagrams/rendered/advanced-networking-hybrid-connectivity.png)

## Bedrock Multi Agent Operations

![bedrock-multi-agent-operations](rendered/bedrock-multi-agent-operations.png)

[Root source](../../architecture-diagrams/sources/bedrock-multi-agent-operations.py) · [Root rendered asset](../../architecture-diagrams/rendered/bedrock-multi-agent-operations.png)

## Bedrock Rag Agent Security

![bedrock-rag-agent-security](rendered/bedrock-rag-agent-security.png)

[Root source](../../architecture-diagrams/sources/bedrock-rag-agent-security.py) · [Root rendered asset](../../architecture-diagrams/rendered/bedrock-rag-agent-security.png)

## Developer Event Driven Platform

![developer-event-driven-platform](rendered/developer-event-driven-platform.png)

[Root source](../../architecture-diagrams/sources/developer-event-driven-platform.py) · [Root rendered asset](../../architecture-diagrams/rendered/developer-event-driven-platform.png)

## Edge Global Delivery

![edge-global-delivery](rendered/edge-global-delivery.png)

[Root source](../../architecture-diagrams/sources/edge-global-delivery.py) · [Root rendered asset](../../architecture-diagrams/rendered/edge-global-delivery.png)

## Global Multi Region Active Active

![global-multi-region-active-active](rendered/global-multi-region-active-active.png)

[Root source](../../architecture-diagrams/sources/global-multi-region-active-active.py) · [Root rendered asset](../../architecture-diagrams/rendered/global-multi-region-active-active.png)

## Honeypot Security Lake

![honeypot-security-lake](rendered/honeypot-security-lake.png)

[Root source](../../architecture-diagrams/sources/honeypot-security-lake.py) · [Root rendered asset](../../architecture-diagrams/rendered/honeypot-security-lake.png)

## Hybrid Dns Private Connectivity

![hybrid-dns-private-connectivity](rendered/hybrid-dns-private-connectivity.png)

[Root source](../../architecture-diagrams/sources/hybrid-dns-private-connectivity.py) · [Root rendered asset](../../architecture-diagrams/rendered/hybrid-dns-private-connectivity.png)

## Networking Private Service Access

![networking-private-service-access](rendered/networking-private-service-access.png)

[Root source](../../architecture-diagrams/sources/networking-private-service-access.py) · [Root rendered asset](../../architecture-diagrams/rendered/networking-private-service-access.png)

## Sa Pro Disaster Recovery

![sa-pro-disaster-recovery](rendered/sa-pro-disaster-recovery.png)

[Root source](../../architecture-diagrams/sources/sa-pro-disaster-recovery.py) · [Root rendered asset](../../architecture-diagrams/rendered/sa-pro-disaster-recovery.png)

## Sa Pro Multi Account Landing Zone

![sa-pro-multi-account-landing-zone](rendered/sa-pro-multi-account-landing-zone.png)

[Root source](../../architecture-diagrams/sources/sa-pro-multi-account-landing-zone.py) · [Root rendered asset](../../architecture-diagrams/rendered/sa-pro-multi-account-landing-zone.png)

## Secure Multi Az Application

![secure-multi-az-application](rendered/secure-multi-az-application.png)

[Root source](../../architecture-diagrams/sources/secure-multi-az-application.py) · [Root rendered asset](../../architecture-diagrams/rendered/secure-multi-az-application.png)

## Security Analytics Lakehouse

![security-analytics-lakehouse](rendered/security-analytics-lakehouse.png)

[Root source](../../architecture-diagrams/sources/security-analytics-lakehouse.py) · [Root rendered asset](../../architecture-diagrams/rendered/security-analytics-lakehouse.png)

## Security Data Platform

![security-data-platform](rendered/security-data-platform.png)

[Root source](../../architecture-diagrams/sources/security-data-platform.py) · [Root rendered asset](../../architecture-diagrams/rendered/security-data-platform.png)

## Security Specialty Central Soc

![security-specialty-central-soc](rendered/security-specialty-central-soc.png)

[Root source](../../architecture-diagrams/sources/security-specialty-central-soc.py) · [Root rendered asset](../../architecture-diagrams/rendered/security-specialty-central-soc.png)

## Security Zero Trust Identity

![security-zero-trust-identity](rendered/security-zero-trust-identity.png)

[Root source](../../architecture-diagrams/sources/security-zero-trust-identity.py) · [Root rendered asset](../../architecture-diagrams/rendered/security-zero-trust-identity.png)

## Serverless Data Lake Analytics

![serverless-data-lake-analytics](rendered/serverless-data-lake-analytics.png)

[Root source](../../architecture-diagrams/sources/serverless-data-lake-analytics.py) · [Root rendered asset](../../architecture-diagrams/rendered/serverless-data-lake-analytics.png)

## Transit Gateway Inspection Vpc

![transit-gateway-inspection-vpc](rendered/transit-gateway-inspection-vpc.png)

[Root source](../../architecture-diagrams/sources/transit-gateway-inspection-vpc.py) · [Root rendered asset](../../architecture-diagrams/rendered/transit-gateway-inspection-vpc.png)
