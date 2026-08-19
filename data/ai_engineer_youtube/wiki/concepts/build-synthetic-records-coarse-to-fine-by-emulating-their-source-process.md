# Build Synthetic Records Coarse to Fine by Emulating How They Were Produced

Summary: Long, structured documents should not be generated in one shot. Layer them coarse to fine along the real-world process that produced them — invariants, then a timeline of the events that generate documentation, then a plan per event, then the documents themselves — and reconcile the parallel branches with a consistency eval. The layering is what keeps prompts token-efficient and lets the artifact grow past any single context window.

Use when:
- Synthesizing documents long enough that one-shot generation degrades (hundreds of pages, whole-history records, multi-document bundles).
- A generated artifact must be internally consistent across parts produced by parallel calls.
- Deciding how to make synthetic data realistic rather than merely plausible.
- Choosing what format synthetic documents should live in for downstream evaluation.

Details:
- The one-shot failure is stated as an analogy: real records "are over 300 pages long," and "you wouldn't ask an LLM to write a novel for you in one shot … it's the same reason why you wouldn't use an LLM to just one shot a synthetic record." Diversity and realism both degrade, and worse at scale. (03:52-04:31)
- The organizing principle is to emulate the generating process, not the artifact. In this domain, documentation "is really generated" only during provider encounters, so the pipeline models exactly that rather than emitting an undifferentiated pile of pages. The talk's takeaway version: "emulate the process in which data was actually generated." (08:58-09:11, 15:38-15:53)
- The concrete layering: patient invariants (biological sex, birth date, blood group) → an ordered list of events and providers, called the *patient journey*, expressed in natural language → a document plan per encounter → a fan-out that generates each document and hydrates it, conditioned on the plan and the preceding patient history. (08:10-09:25)
- The layering is an efficiency mechanism, not only a modelling one: it keeps "the different prompt payloads in the pipeline very token efficient … from both input and output perspective," and lets a much longer journey be covered by fanning out further "without overloading the context windows of your LLMs." (09:26-09:50)
- Parallel fan-out is what makes a reconciliation step mandatory. A refinement loop at the end runs a set of evals that feed back into specific parts of the documents; one is "an LLM based check for consistency between all documents," ensuring no "contradictions or inaccuracies or conflicting information," precisely because the documents were generated independently. (09:55-10:24)
- Do not render to the source file format without a reason. Generation stays in plain text and markdown: rendering to PDF is possible but "we don't really see much value" because "we have state of the art PDF parsers today … available to everyone" that convert complex PDFs back to markdown, so "all of this synthetic generation [and] evaluation happens in the text domain." Fidelity is spent on content structure, not on reproducing scan artifacts. (11:04-11:31)
- Reported fidelity of the layered pipeline: in a blind review, clinicians separated synthetic records from real ones "about 60% of the time." (14:29-14:45)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Generate Eval Data by Reversing the Inference Workflow](generate-eval-data-by-reversing-the-inference-workflow.md)
- [Hand Domain Experts the Pipeline as Skills](hand-domain-experts-the-pipeline-as-skills.md)
- [Validate the Simulated User and the Judge Before Trusting a Simulation](validate-the-simulated-user-and-the-judge.md)

Sources:
- [Don't be data poor — Anuj Iravane, Anterior](../sources/20260819_XAsb7MIAzm8.md), 03:52-04:31, 08:10-11:31, 14:29-14:45, 15:38-15:53
