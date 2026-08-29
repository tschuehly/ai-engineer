# High-Value Vertical Data Is Withheld by Design

Summary: In some verticals the reasoning data a model would need is not merely scarce — it is deliberately kept off the internet, because publishing it destroys the value of holding it. That makes the gap structural rather than temporary: no frontier lab has the data either, and you cannot buy your way to it through annotation.

Use when:
- Estimating whether a future frontier model will eventually be good enough at your domain without you.
- Deciding whether to invest in proprietary data curation versus waiting for the next base model.
- Explaining to stakeholders why a general model "jargons" convincingly in your field but is not actually competent.
- Choosing between hiring annotators and hiring practitioners.

Details:
- The finance mechanism is a disclosure penalty. Any institutional manager holding over $100 million in qualifying US equities must publicly file its long holdings every quarter, and once a fund does, returns decrease "because everyone just sees those, reverse engineers, and takes away their moat." Funds therefore publish the legal minimum and keep the reasoning private. ([Trading Desks to Clinical Trials](../sources/20260819_Yphdry8ttAQ.md), 10:27-10:47)
- The pharma mechanism is non-compliance. Disclosure of "every clinical trial, pass or failure" is required by law, but "30% of the funds, which is nearly 1/3 of firms, never do," and in 2026 the FDA "had to publicly remind… about 2,000 sponsors" that withholding unfavorable results does an injustice. A legal mandate is not the same as an available dataset. (10:48-11:14)
- The withheld material is specifically the *reasoning*, not the outcomes: it is "the exact data which helps your LLM actually reason through these complex and niche industries. And they hide it because for them, it's like a chicken laying golden eggs. Why would they sell their chicken?" (11:14-11:33)
- The consequence for model choice: "naturally, neither OpenAI nor Anthropic has this data because it's gatekeeper." Waiting for capability to arrive from the labs is not a strategy in a domain whose corpus was never published. (11:14-11:33)
- The consequence for data ops: annotation cannot substitute, because the people who hold the judgment are contractually and economically out of reach — "you just cannot hire a trader for $100 an hour and have them annotate that stuff because there's lots of NDAs and they definitely earn more." (11:33-11:41)
- The same asymmetry names what to curate. In finance the proprietary asset is the trade thesis, "what trade work and why it worked"; in pharma it is the data for *failed* experiments, since successful-experiment data is obtainable and failure data is not. Both are the private half of a publicly visible outcome. (05:58-06:18)
- The cheap first move is internal rather than external: an organization three years old "already have a lot of data. It's just unstructured," and in the age of LLMs converting it to structured form is tractable — "an LLM workflow could do it overnight." Public sources everyone shares (news, sell-side reports from JP Morgan or Morgan Stanley, arXiv, PubChem) are explicitly not the differentiator. (05:06-05:57)
- The strategic conclusion this supports: "Model, infra, ecosystem… is just commodity. Everyone has it… what is moat, and no one will come and sell it to you, you will have to curate it on your own, is the domain expertise. You need your data. You need other people's data. That is just not out there on the internet." (19:03-19:34)
- **What an operator sees that a data buyer cannot: the outcome, not just the corpus.** Shenoy's version of the withheld-data problem is the same — "the most valuable tasks are not on the internet," and the knowledge lives "in people's heads, in 20-year-old software, in the way that one senior person on one of these teams just knows how to do it" — but his answer is positional rather than curatorial. Long Lake buys the businesses, so it observes whether the roof got repaired and whether the books got closed, which is an eval label the world produces for free and that no annotation budget can reconstruct. He reports post-training internally on operational data "completely out of distribution for most frontier labs." That extends this page's argument: the moat is not only the private reasoning corpus but the position from which outcomes are visible. ([Shenoy](../sources/20260828_B0fjR3yaZFU.md), 04:16-04:31, 10:13-12:40)

Related topics:
- [Product Strategy](../topics/product-strategy.md)
- [Models](../topics/models.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [You Cannot Iterate on Output You Cannot Judge](you-cannot-iterate-on-output-you-cannot-judge.md)
- [Hire the User to Own the Judgment Loop](hire-the-user-to-own-the-judgment-loop.md)
- [Target High-Value AI Verticals as Capability Matures](target-high-value-ai-verticals.md)
- [Build domain-specific workflow wrappers around models](build-domain-specific-workflow-wrappers-around-models.md)
- [Customize Open Benchmark Harnesses With Proprietary Task Data](customize-open-benchmark-harnesses-with-proprietary-task-data.md)
- [Operational Outcomes Are Eval Labels You Only See If You Own the Operation](operational-outcomes-are-eval-labels-you-only-see-if-you-own-the-operation.md)

Sources:
- [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI — Ayush Bhardwaj, Allos AI](../sources/20260819_Yphdry8ttAQ.md), 05:06-06:18, 10:27-11:41, 19:03-19:34
- [How do you diffuse AI into the real world? — Varun Shenoy, Long Lake](../sources/20260828_B0fjR3yaZFU.md), 04:16-04:31, 10:13-12:40
