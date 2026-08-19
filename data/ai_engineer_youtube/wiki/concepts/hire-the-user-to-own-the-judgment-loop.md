# Hire the User to Own the Judgment Loop

Summary: When nobody on the team can judge the product's output, the fix is a hire, not a tool: bring the person you are selling to onto the team and make them the owner of prompts, source curation, decision procedure, and judgment. Then climb a cost-ordered ladder of ways to capture that judgment, starting at error analysis before touching any weights.

Use when:
- An AI product for a domain your team does not practice has stalled at "it looks done but we can't tell if it's good."
- Sequencing a vertical AI build: deciding what must be in place before iteration is worth starting.
- Choosing between prompt work, rubrics, fine-tuning, and RLHF as the next investment.
- Staffing a small engineering team that is about to sell into an expert buyer.

Details:
- The rule is blunt and reported as hard-won: "you hire the person who you want to sell it to cuz there is, to be honest, no other way around. I have tried a lot of stuff. You just need to hire the user." ([Trading Desks to Clinical Trials](../sources/20260819_Yphdry8ttAQ.md), 11:53-12:06)
- Its difficulty is asymmetric by setting. At the hedge fund the user was already colocated — "the user was kind of like my boss, the trader. We worked together." At the pharma-tech startup it took a deliberate, uncomfortable decision by "a bunch of young engineers" to hire a senior scientist to tell them what to do. (12:06-12:25)
- The observed payoff was commercial, not just technical: "that someone actually changed the trajectory of our tools. Our tools started making sense. When we pitched to the other pharma companies, the big ones… they started liking our tools because it kind of spoke their language versus the normal jargonish LLM language." (12:25-12:41)
- The expert's work has four rungs, in order. **Prompts** — narrow the ask ("let's not ask the LLM to do this, let's ask a very specific query"). **Source curation** — "a pharma expert or a trader knows which sources are more reliable than the other," the same way an engineer knows which conferences and paper venues are credible and who is a leader versus an influencer. **Thinking models** — encode the ordering, because "if you follow five steps to solve a problem, you just cannot do it in any random order. There has to be a logical flow," so they decompose the problem and gradually refine it. **Judgment** — the expert is the evaluator. The summary line: the person "who has lived through the complete of the industry… their judgment is now turning into agents." (12:42-13:58)
- The prompt is written as a transcription of a practitioner: model it "after the person who you are trying to replace… encode how a person would solve this job into multiple steps." (06:23-06:48)
- The methods for capturing that judgment form a cost-ordered ladder, and the recommendation is to start at the bottom. **Error analysis** is "the cheapest of all, and I think the highest ROI" — read the logs from the observability step, find where the model goes wrong, correct it, touch no weights. **Rubrics as a reward** (he calls it "reinforcement learning from AI feedback") lets a human write the rubric and the AI grade itself, with the caveat that "there is a slight chance that you might run into an echo chamber with rubrics as rewards." **Supervised fine-tuning** has the model mimic human demonstrations. **RLHF** trains a reward model on human preferences and is "kind of the golden standard these days." Climb gradually, only once the cheaper rung stops paying. (13:58-15:32)
- The standing cost of the top rungs is a treadmill, not a one-time bill: fine-tune GLM 5.2 and then "Alibaba Cloud or let's say DeepSeek will release a newer model, then you have to fine-tune that too as well. So there is a cost. It's not cheap." (15:33-15:48)
- The loop compounds into the asset the company lacked at the start: hire one user, then more; they ask more queries, scope and data grow, and "at this point you're kind of generating your own data… that exercise itself is generating a crazy data set of what works and what does not work. And this loop never stops." (15:49-16:21)
- The sequencing matters enough to be stated as a step of its own — build the narrow problem, the data, the prompt, and observability, then "you don't iterate yet, you hire the user," and only ship when the product delivers "that alpha over let's say Claude and ChatGPT." (17:06-17:42)

Related topics:
- [Workflows](../topics/workflows.md)
- [Evaluation](../topics/evaluation.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [You Cannot Iterate on Output You Cannot Judge](you-cannot-iterate-on-output-you-cannot-judge.md)
- [High-Value Vertical Data Is Withheld by Design](high-value-vertical-data-is-withheld-by-design.md)
- [Keep the Expert as Decider With AI in Their Loop](keep-the-expert-as-decider-with-ai-in-their-loop.md)
- [Domain Expert Review Tools Convert Judgment Into Deployable Knowledge](domain-expert-review-tools-convert-judgment-into-deployable-knowledge.md)
- [Hand Domain Experts the Pipeline as Skills](hand-domain-experts-the-pipeline-as-skills.md)
- [Prefer Model-Portable Agentic Prompts Before Fine-Tuning](prefer-model-portable-agentic-prompts-before-fine-tuning.md)
- [Decide When to Fine-Tune From Three Business Signals](decide-when-to-fine-tune-from-three-signals.md)

Sources:
- [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI — Ayush Bhardwaj, Allos AI](../sources/20260819_Yphdry8ttAQ.md), 06:23-06:48, 11:53-16:21, 17:06-17:42
