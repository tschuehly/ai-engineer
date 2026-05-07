# Normalize Network Telemetry Into Agent-readable Schemas

Summary: Operational graph agents need heterogeneous infrastructure data normalized into a schema they can reason over. For network operations, that means turning controller, device, telemetry, SIEM, and configuration data into a shared graph representation before agents plan tests or assess changes.

Use when:
- Building graph-backed agents over heterogeneous production infrastructure.
- Choosing a canonical schema for operational data that agents and humans can inspect.

Details:
- The source frames network environments as multi-vendor and multi-device: firewalls, switches, routers, controllers, device agents, and configuration-management systems all emit data in different formats. 03:40-04:49
- Input formats include YANG, JSON, streaming telemetry, configuration files, and other network data feeds, so the graph ingestion pipeline must consolidate both source systems and data shapes. 04:51-05:14
- Product requirements for the graph included multimodel flexibility, instant node lookup, one schema framework, vector indexing for semantic search, low customer integration burden, and multi-vendor support. 05:19-06:25
- The implemented ingestion service performs ETL from production controllers, Splunk/SIEM, traffic telemetry, and related sources into an OpenConfig-oriented schema; the speaker notes that public OpenConfig documentation makes it easier for LLMs to understand. 07:23-08:15
- The graph is layered so an agent can query only raw configuration for configuration drift, or include configuration, data-plane, and control-plane layers for reachability tests. 08:15-09:07

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Knowledge graphs make agent memory traversable and explainable](knowledge-graphs-make-agent-memory-traversable-and-explainable.md)
- [Treat ontology and triplet quality as GraphRAG bottlenecks](treat-ontology-and-triplet-quality-as-graphrag-bottlenecks.md)

Sources:
- [Multi Agent AI and Network Knowledge Graphs for Change — Ola Mabadeje, Cisco](../sources/20250822_m0dxZ-NDKHo.md), 03:40-09:07
