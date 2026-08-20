# Validate a Research Report by Building the Thing It Recommends

Summary: A deep-research report comparing tools or vendors reads as authoritative at exactly the moment it is least verified — it can confidently attribute product features that do not exist. The cheap correction is instantiation: build a small proof of concept against the real product for each finalist before committing. Agents can compress the search from months to days, but the POC step is the one that must survive the compression.

Use when:
- Selecting a framework, orchestrator, database, or vendor with an agent-assisted research process.
- A long generated comparison document is about to become an architecture decision.
- Designing an agentic version of an evaluation process that previously ran manually against a criteria list.

Details:
- **The named failure mode.** "It's very easy to undergo AI psychosis, where you look at a deep research report that's 20 pages long and you say, 'Wow, this looks good.' And then those features don't actually exist in the product, and you've set yourself back." The report's length and coherence are what make it persuasive, and neither is evidence about the product. ([Denys Linkov](../sources/20260808_7vn4WpqNpck.md), 04:42-05:01)
- **The process being replaced, with its cost.** WiseDocs spent "around 2 months evaluating orchestrators for our AI pipeline. We looked at five open-source projects," working "before deep research came out as part of Google and OpenAI, so that web search capability to do a comprehensive analysis was still not there" — manual review compiled into a Confluence doc and scored against "17 different criteria that we came up with," then validated by "proof of concepts with a team of three to make sure that we actually got the right results." ([Denys Linkov](../sources/20260808_7vn4WpqNpck.md), 03:46-04:26)
- **The agentic redesign, and what it keeps.** "Nowadays, we could build a much more agentic workflow to do that, starting off with deep research, making sure that we match that against the problem statements that we have, creating sub-agents for each of these criteria and products, and then finally building POCs and evaluating." Three structural properties carry over from the manual version: an explicit criteria list written before the search, a fan-out that is one agent per criterion per product rather than one prompt for the whole comparison, and a build step at the end. The estimate is "90% faster" — with the quality bar held. ([Denys Linkov](../sources/20260808_7vn4WpqNpck.md), 04:12-04:41)
- **The criteria list is what makes the report checkable.** Seventeen criteria fixed in advance turn a comparison into a set of specific claims that a POC can falsify one at a time, instead of an overall impression that can only be agreed or disagreed with. It also produces an honest calibration number afterwards: "we got 15 out of 17 requirements right when we were going ahead with the refactor." ([Denys Linkov](../sources/20260808_7vn4WpqNpck.md), 15:59-16:15)
- **The specific claim class a POC catches.** In the Q&A, the example of a hidden assumption is exactly this shape: "you thought an open-source library had this feature, but it was actually in a beta." Documentation, changelogs, and blog posts — the corpus a research agent reads — describe intended and announced capability. Only running the thing distinguishes shipped from announced, GA from beta, and supported from technically-possible. ([Denys Linkov](../sources/20260808_7vn4WpqNpck.md), 17:25-17:35)
- **The same pattern one layer down.** The talk's zero-shot experiment fails the identical way in code: GPT 5.5 extra high declared the whole refactor complete in "10 minutes and 22 seconds," and the tell was volume against expectation — "it only wrote 2,000 lines of code, which was a little bit fishy. So I dug deeper. Um and it actually just implemented a bunch of scaffolding and didn't implement the models." The disclaimer was already in the model's own output, unread: "I did not add a Ray Serve deployment or bootstrap command yet." A fluent artifact asserting completion, a cheap size sanity check, and a confession nobody read — the research report and the finished refactor are the same failure at different stages. ([Denys Linkov](../sources/20260808_7vn4WpqNpck.md), 11:44-12:13)
- **Caveats.** The "90% faster" figure is an estimate of a counterfactual, not a re-run; the agentic workflow is described as buildable rather than as something executed and measured. The 15-of-17 result is given without saying which two requirements were wrong or what being wrong about them cost. And the talk does not describe how much POC work is enough — "a team of three" building proofs of concept is a real expense that the compressed version still has to pay.

Related topics:
- [Workflows](../topics/workflows.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Review research and plans before they multiply into code](review-research-and-plans-before-they-multiply-into-code.md)
- [Silent Web-Access Failure Produces Confident Hallucination](silent-web-access-failure-produces-confident-hallucination.md)
- [Wrap Agent Completion in an Automatic Deterministic Verification Gate](wrap-agent-completion-in-an-automatic-deterministic-verification-gate.md)
- [Audit a Refactor Against Having Waited for Better Models](audit-a-refactor-against-having-waited-for-better-models.md)

Sources:
- [Benchmarking Coding Agents on New vs Legacy Codebases — Denys Linkov, Wisedocs](../sources/20260808_7vn4WpqNpck.md), 03:46-05:01, 11:44-12:13, 15:59-16:15, 17:25-17:35
