# You Cannot Iterate on Output You Cannot Judge

Summary: In a vertical domain, an engineering team reaches the ability to *build* the agent long before it reaches the ability to tell whether the agent is any good — and that gap, not model capability, is where vertical AI projects quietly die. An LLM judge cannot close it, because the domain has no answer key and the judge has no idea what a good answer looks like.

Use when:
- Building an AI product for a domain nobody on the team practices (finance, pharma, law, real estate, clinical, actuarial).
- The demo looks finished, the team is ready to ship, and nobody can articulate why the output is good.
- Deciding whether LLM-as-judge is a legitimate substitute for domain evaluation or a way of skipping it.

Details:
- The failure is stated as a personal one: "I could build it, but I just could not tell if it worked cuz I'm not a trader. I'm not someone who has a PhD in biology or chemistry. I just don't understand what the model is saying, what the output of my AI agent is." ([Trading Desks to Clinical Trials](../sources/20260819_Yphdry8ttAQ.md), 07:44-08:12)
- The reason engineers underestimate it is that they already have the instinct for their own domain: "you can instantly tell that Sonnet 5 sucks because you have your own training… you've been trained for this for life. You have a mental model to judge these things." That mental model took years, and the team simply does not have the equivalent for a trade thesis or a drug candidate. (08:12-08:38)
- Why it is a *silent* project killer rather than a loud one: "on the surface it looks like you have made it, you have built it, let's put this into production and start selling it. But no one would buy it the same way you won't use an inferior coding model." Nothing errors; the product is merely unbuyable, and the signal arrives from the market rather than from the eval suite. (08:43-08:58)
- The build steps that precede this — narrow problem formulation, sourcing data, writing a prompt modeled on the practitioner, wiring observability — "fit one screen. The mythical 10x engineers can do this stuff in minutes… that's why it's not the moat." Cheap upstream steps are exactly what makes the judgment gap arrive fast and unannounced. (07:11-07:29)
- LLM-as-judge as the escape hatch is rejected from experience: "I thought I could LLM as a judge my way out of it… this was a really, really stupid mistake." The model is "predicting the next probable word… it's just like jargoning its way out. It does not understand what alpha means. It does not understand how to actually create value unless you have taught it some way." (09:00-09:35)
- The generalizable boundary is the answer key: "reinforcement learning via verifiable rewards is really good at math and code because you have answer keys, you can verify your code is compiling or not… but in these fields, there is just no way to model it. And if any error gets in, it just compounds." Domains that self-verify are the exception, not the template. (09:42-10:10)
- A corollary about the shipping bar: reaching production proves nothing. Against the Stanford AI Index claim that 89% of enterprise AI agents never reach production, the counter-framing is that "every AI reaches production, but it just fails to work or justify its own cost" — in finance and pharma, "if it does not make money, it's shown the door," with no credit for "maybe it'll work in 2 years." (16:22-17:05)
- The unblock is staffing, not tooling: the sequencing rule is to build the first four steps and then *not* iterate until the domain expert is on the team (see the related concept). (17:06-17:42)
- **The same gap named from inside a domain the team does practice.** Fox is a medical doctor working on clinical notes, so the missing mental model is not the one this page's remedy supplies — he already has it, and still cannot get it into a judge. His formulation is that the deciding property is "taste, effectively. Not aesthetic taste, but essentially judgment," and that it is tacit ("your domain experts have it, but they can't fully write it down"), contextual, and moving. That extends this page's diagnosis rather than contradicting it: hiring the practitioner puts the judgment in the building, and there is a second, separate transfer problem getting it out of their head and into a scoring system. His answer is to stop trying to state it and start collecting instances of it. See [Keep a Moving Standard in Examples, Not in a Rubric or the Weights](keep-a-moving-standard-in-examples-not-in-a-rubric-or-the-weights.md). ([Fox](../sources/20260822_yqF6XhzbWBk.md), 06:49-07:34, 11:36-11:56)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Hire the User to Own the Judgment Loop](hire-the-user-to-own-the-judgment-loop.md)
- [High-Value Vertical Data Is Withheld by Design](high-value-vertical-data-is-withheld-by-design.md)
- [Domain Evals Need Expert-Built Environments](domain-evals-need-expert-built-environments.md)
- [Use Verifiable Rewards for Language-Model RL](use-verifiable-rewards-for-language-model-rl.md)
- [Last-Mile Domain Context Beats Model Chasing](last-mile-domain-context-beats-model-chasing.md)
- [Keep a Moving Standard in Examples, Not in a Rubric or the Weights](keep-a-moving-standard-in-examples-not-in-a-rubric-or-the-weights.md)
- [Verification Is Cheap for Detection and Expensive for Materiality](verification-is-cheap-for-detection-and-expensive-for-materiality.md)

Sources:
- [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI — Ayush Bhardwaj, Allos AI](../sources/20260819_Yphdry8ttAQ.md), 07:11-10:10, 16:22-17:42
- [Inside 847 Production Clinical AI Notes — Sebastian Fox, Composo](../sources/20260822_yqF6XhzbWBk.md), 06:49-07:34, 11:36-11:56
