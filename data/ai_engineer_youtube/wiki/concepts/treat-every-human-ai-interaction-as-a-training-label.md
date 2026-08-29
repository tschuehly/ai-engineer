# Treat Every Human-AI Interaction as a Training Label

Summary: The human-AI loop is not linear (model → human → decision) but a cyclical flywheel: model output → interaction → human behavior → data → evals → next model. Every interaction is already a label, so design the interaction to produce honest, structured signals — and capture the *diff* the human actually made, not just a yes/no — instead of bolting on a separate annotation step later.

Use when:
- Instrumenting an AI product or agent to generate its own training/eval data.
- A review UI only records accept/reject and you're wondering why the model isn't improving.
- Deciding what to log at each human touch point in a copilot, agent, or review tool.

Details:
- Reframe the loop as cyclical: models produce output → an interaction → human behavior → data for your evals → later your model. You can't change how a human behaves unless you *are* that human, but you *can* tweak the interaction to elicit different behavior, "and that data is golden" — better analytics, model improvements, and the next generation of the model or a new product. ([source](../sources/20260707_CDqzWpwkSls.md), 09:11-10:00)
- The flywheel compounds only if the interaction is structured intentionally: designed interactions yield labeled signals that become training data and evals for a better model, which enables better interactions — so treat structured interactions as a *system property* that yields high-quality data, avoiding days spent cleaning data or hunting for insights. Frictionless rubber-stamp interfaces instead log false positives as truth (the vicious cycle). (10:00-11:56)
- **Capture the diff, not the click.** Approved/accepted means you matched the user's intent; modified or overridden means something was wrong — but only if you measure it. A human who clicks "yes" and then silently edits or erases the output logs a *false* positive that pollutes the dataset. Most systems don't capture that diff; the model falls short because the recorded decision was a yes/no while the real signal was the edit. Follow-up questions and explanation requests are also signals (low trust, or a wrong AI) — track their sentiment. (21:31-22:58)
- Split conflated judgments so each label is honest: one yes/no that hides "was the detection correct?" and "is this a violation?" forces reviewers to give a wrong answer to one to protect the other (a hearing aid is a true detection but not a violation) — splitting yields more and better-quality data without harming the model. (11:56-13:23)
- Design the interaction *for the label you'll need*: stop asking how to evaluate the model after building it. Proactively define what success means, what concrete metrics measure it, and what data you need — and let those decisions shape the interaction so you have hard evidence for the next iteration. Collect explicit feedback at the correct touch points with nuance, not a global thumbs up/down. (22:58-23:40, 25:41-25:51)
- Structured surfaces make richer labels: a coding agent that acts like a junior partner (plans, states assumptions, breaks work into reviewable PRs) captures nuanced structured decisions — bad assumptions, tradeoffs made, stylistic preferences — about specific parts of the development cycle, versus a giant-diff or ping-per-file agent that only yields skewed binary accept/reject on a code block. (15:41-18:50)

- **The coverage argument for preferring behaviour over solicited response, with numbers.** Uber posts about 25,000 review comments a week; "we get 10% of them actually get some feedback. And only 4% of the PRs actually get some negative feedback." A survey, a form, or a thumbs-up widget therefore labels roughly a tenth of the interactions and a self-selected tenth at that, while the label already sitting in the workflow — did the developer change the code — is available on all of them. Two cautions carry with it: the two figures quoted have different denominators (comments versus PRs) and cannot be converted into each other, and a behavioural label is a proxy whose validity the source never checks. ([Bond and Ketkar](../sources/20260828_EL123UNokkI.md), 10:12-10:47)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Automation Bias Turns Human-in-the-Loop Into a Rubber Stamp](automation-bias-turns-human-in-the-loop-into-a-rubber-stamp.md)
- [Engineer the Interaction, Not the Model, for Discernment](engineer-the-interaction-not-the-model-for-discernment.md)
- [Connect Production Observability to Offline Eval Loops](connect-production-observability-to-offline-eval-loops.md)
- [Domain Expert Review Tools Convert Judgment Into Deployable Knowledge](domain-expert-review-tools-convert-judgment-into-deployable-knowledge.md)
- [Measure a Review Bot by Whether the Comment Changed the Code](measure-a-review-bot-by-whether-the-comment-changed-the-code.md)

Sources:
- [Build AI Systems for Discernment, Not Approval - Angel Ortmann Lee, Duolingo](../sources/20260707_CDqzWpwkSls.md), 09:11-25:51
- [Building uReview, Uber's Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber](../sources/20260828_EL123UNokkI.md), 10:12-10:47
