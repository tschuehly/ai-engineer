# Map Expert Decision Taxonomies Into Knowledge Graphs

Summary: Advisory systems can model expert judgment as a graph of decision concepts rather than only a pile of retrieved documents. The useful graph captures how knowledge, experience, insight, current situation, and decisions feed back into reusable wisdom.

Use when:
- Building an AI advisor that should recommend actions, not only answer factual lookup questions.
- Converting expert interviews or domain workflows into structured context for retrieval and generation.

Details:
- The talk defines a knowledge graph as a network of relationships that represents a domain's thought process and taxonomy, then frames KAG as using that graph so the model can return advice instead of only retrieved database content. 01:22-02:19
- The proposed decision taxonomy includes wisdom, decision making, situation, knowledge, experience, and insight; the "wisdom" node is not static because situation, experience, and insight should feed back into future advice. 02:21-06:18
- In the competitive-analysis example, the taxonomy maps to market data, past campaigns, industry insight, current product status, competitor weakness, strategy generation, and a wisdom engine. 06:21-08:37
- This pattern is strongest when the domain has recurring expert decision structure that can be interviewed, named, and connected before the model is asked for advisory output. 02:21-02:40, 16:46-17:12

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Knowledge graphs make agent memory traversable and explainable](knowledge-graphs-make-agent-memory-traversable-and-explainable.md)
- [Choose HybridRAG when relationship structure matters](choose-hybridrag-when-relationship-structure-matters.md)

Sources:
- [Wisdom-Driven Knowledge Augmented Generation at Scale - Chin Keong Lam, Patho AI](../sources/20250822_9AQOvT8LnMI.md), 01:22-08:37, 16:46-17:12
