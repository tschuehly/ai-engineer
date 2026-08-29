# Schema-First Classification Turns LLMs Into Enterprise Categorization Tools

Summary: LLM structured outputs can turn enterprise categorization into a schema- and taxonomy-driven workflow rather than a bespoke ML classifier project. The pattern still needs business validation, taxonomy context, and quality checks before it becomes a reliable workflow step.

Use when:
- Classifying tickets, vendors, spend records, company names, or other enterprise text into a known taxonomy.
- Replacing one-off text-classification pipelines with a reusable structured-output workflow.

Details:
- The source contrasts older classification workflows such as stemming, stop-word removal, SVMs, and Naive Bayes with LLM structured outputs against a target taxonomy. (08:02-08:25)
- Their vendor-classification example uses a business taxonomy such as NAICS codes, including code descriptions, and can add tool calls such as web queries when the company is not likely to be in the base model's knowledge. (08:25-09:02)
- The talk reports 95% accuracy across 10,000 vendor categorizations, with the work completed in minutes at much lower cost than manual review. (10:20-10:32)
- The workflow is not "unchecked" unsupervised learning: business partners helped validate accuracy, and business context embedded in the taxonomy was necessary for useful classification. (09:13-09:56)
- Robust classification steps can later be daisy-chained into larger agentic workflows, but the individual step must be made accurate before it becomes a reliable building block. (09:56-10:10)
- **A production application of the same pattern, aimed at a product's own question log.** Izmit's team classifies 1.2 million assistant questions — ~40,000 a week — into a hierarchical topic taxonomy with categories, subcategories, and example questions per category, and treats doing it "at scale without breaking the bank" as the interesting engineering problem. The output is a demand map used to rank the roadmap and to find missing enablement content. Nothing is reported about the taxonomy's design, the sampling rate, or whether the assigned labels were ever validated against what users meant, which is the check this page's schema-first framing exists to enable. ([Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 14:17-15:00)

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Type-Safe Agent Schemas Make Refactoring and Validation Easier](type-safe-agent-schemas-make-refactoring-and-validation-easier.md)
- [Keep Fixed Business Logic Outside the Model](keep-fixed-business-logic-outside-the-model.md)
- [Classify the Assistant Question Log to Find Feature and Content Gaps](classify-the-assistant-question-log-to-find-feature-and-content-gaps.md)

Sources:
- [The Billable Hour is Dead; Long Live the Billable Hour - Kevin Madura + Mo Bhasin, Alix Partners](../sources/20250723_Wv1tAxKYLeE.md), 07:27-10:32
- [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 14:17-15:00
