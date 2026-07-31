"""Stable AWS icon aliases for Python diagrams 0.24.4.

Architecture sources import semantic service names from this module so a
library node rename is fixed once rather than in every diagram.
"""

from diagrams.aws.analytics import ElasticsearchService
from diagrams.aws.network import NetworkFirewall, Route53, VPC

# Semantic aliases used by the handbook architecture sources.
Route53Resolver = Route53
OpenSearchService = ElasticsearchService
PrivateLink = VPC

__all__ = [
    "Route53Resolver",
    "NetworkFirewall",
    "OpenSearchService",
    "PrivateLink",
]
