# Lab Eval Vocabulary Does Not Transfer to Application Teams

Summary: "Eval" names two unrelated activities. Labs evaluate general-purpose models against benchmarks; product teams verify a specific system carrying company-specific domain knowledge for users with a specific amount of responsibility. Borrowing the vocabulary imports the wrong success criteria along with it.

Use when:
- A team is building an internal benchmark modeled on a lab's published one.
- A conversation about "evals" keeps producing agreement that dissolves on contact with the work.
- Deciding how much of a published eval methodology applies to your product.
- Explaining why a competitor's or a lab's eval approach should not be copied wholesale.

Details:
- The vocabulary complaint: "the terms are really confused… the word eval is like more or less a meaningless word. It literally is just like you're evaluating something… It's like a test in some cases." ([Hylak](../sources/20260812_jHMiYtjoJfA.md), 08:08-08:31)
- The mechanism of the mistake: "companies start borrowing like the language that like labs are using and like even copying similar benchmarks, but they're doing completely different things… they have completely different tools at their disposal… the companies that are downstream of models just have very, very different responsibilities than labs." (08:38-08:56)
- The asymmetry in what each side is building. Labs "are trying to make these super general purpose things," and an API-level mistake is diffuse. Companies "are trying to like imbue all this like company specific domain knowledge. Like, oh, here's the shape of the data and here's what all this data means and here's like how to access it" — none of which any lab benchmark measures. (08:57-09:18)
- **The axis that actually sets your eval design is how much responsibility sits with the user**, and it varies enormously across products that all call themselves agents. Tab complete: "if it gets something wrong like you can just delete it." A coding CLI: "it does do things wrong all the time," and much of what goes wrong is environmental — "it could be that like you don't have something installed correctly on your computer. There's a lot more like user error… you leave a lot more up to the users to get correctly." Devin is "more interesting"; AI doctors are "a very very different shape of responsibility as far as like how much responsibility a user has in actually getting things correctly." (09:42-10:23)
- A related diagnostic he uses: "are your users like domain experts in the thing they're doing?… is it almost like replacing someone or is it augmenting them?" An augmenting product can rely on the user as the last check; a replacing product cannot, and its floor has to be raised by the system ([Raise the Floor Before Maxing the Benchmark](raise-the-floor-before-maxing-the-benchmark.md)). (09:23-09:40)
- Practical consequence: the transferable part of a lab's eval work is methodology (controls, sample sizing, contamination hygiene), not the tasks or the score. Copying the task set imports a measurement of general capability into a place where the question was whether *this* system, holding *your* data model, does the right thing for *your* users.
- The wiki carries the positive form of the same idea from several directions: evals are where domain knowledge should live ([Treat Evals as the Home of Domain Knowledge](treat-evals-as-the-home-of-domain-knowledge.md)), domain evals need expert-built environments ([Domain Evals Need Expert-Built Environments](domain-evals-need-expert-built-environments.md)), and a single leaderboard is not a model-selection instrument ([Do Not Trust a Single Leaderboard for Model Selection](do-not-trust-a-single-leaderboard-for-model-selection.md)). This page names why the borrowing happens anyway: one word covers both activities.
- Caveat: the argument is asserted rather than demonstrated, with no example of a company that copied a lab benchmark and was misled. It is also self-serving for a vendor selling production issue detection rather than benchmarks — though the responsibility-spectrum observation stands independently of that.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Product Strategy](../topics/product-strategy.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Raise the Floor Before Maxing the Benchmark](raise-the-floor-before-maxing-the-benchmark.md)
- [Treat Evals as the Home of Domain Knowledge](treat-evals-as-the-home-of-domain-knowledge.md)
- [Domain Evals Need Expert-Built Environments](domain-evals-need-expert-built-environments.md)
- [Do Not Trust a Single Leaderboard for Model Selection](do-not-trust-a-single-leaderboard-for-model-selection.md)
- [Match the Quality Method to Your User Count](match-the-quality-method-to-your-user-count.md)
- [Map Application Evals to the Product Court](map-application-evals-to-the-product-court.md)

Sources:
- [Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop](../sources/20260812_jHMiYtjoJfA.md), 08:08-10:23
