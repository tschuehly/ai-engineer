# Steer agents with leading words that surface in reasoning traces

Summary: A "leading word" is a dense-meaning phrase placed in a skill or prompt that the agent repeats back into its own reasoning traces and output, thereby triggering an existing prior and changing its behavior — and you can verify the technique worked by watching for the phrase in the traces.

Use when:
- A skill specifies a behavior clearly but the agent still doesn't do it.
- Compressing verbose behavioral instructions into a few reusable tokens.

Details:
- The failure it fixes: you specify something in a skill, think you were clear, and the agent just doesn't do the thing. Matt Pocock's main claim is that this usually means you aren't using leading words. 11:54-12:20
- Mechanism: certain words pack a lot of meaning into a very small space; put the leading word in the skill text and the agent re-emphasizes it in its thinking tokens and its output to you, and because the word describes what you want, that re-emphasis changes behavior. 12:00-12:45
- Concrete example: agents tend to "code layer by layer" (all the DB, then all the schemas, then all the endpoints, then the frontend) instead of building a small end-to-end slice first. Rather than "don't code layer by layer, build a small slice," use the leading word *vertical slice* — a well-known dev term that triggers the agent's prior. You aren't limited to a two-word skill; you pack the meaning into a short phrase and repeat it consistently throughout the skill. 12:45-14:10
- Verification: you can tell it worked because the phrase shows up in the reasoning traces ("we're going to do this as a thin vertical slice"), and you should get better implementation plans. 14:10-14:35
- Tuning: if the agent still isn't complying, make leading words more consistent, more powerful, and look for others — "English is a pretty wide API in terms of different functions you can call," and agents are themselves good at helping brainstorm leading-word candidates. 14:35-14:55
- This is a naming/steering lever distinct from progressive disclosure and pruning: it changes *how instructions are phrased* to exploit the model's priors, not how much context is loaded.
- **The same lever exists at the weights layer, and it works even when the target action is absent from the training data.** Applied Compute distilled a submit-tool behavior into a model using traces that "never basically never called this task complete tool," so the teacher "doesn't force the tool call. It just starts to force the reasoning path towards the tool call without ever actually changing the tool call" ([A Teacher Can Install a Tool Call by Moving the Reasoning Path](move-the-reasoning-path-not-the-target-tokens.md)). Tool-call rate went from about 22% to 60% with the base task metric flat. Same causal story as leading words — intervene on the reasoning and the action follows — with the intervention persisted into parameters rather than repeated in the prompt. ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 12:22-13:38)
- The verification advice on this page transfers unchanged and is worth applying to a training run too: watch for the effect in the reasoning trace, not only in the outcome metric. A behavior-rate change with no corresponding shift in how the model deliberates is a sign something else moved.

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [A Teacher Can Install a Tool Call by Moving the Reasoning Path, Never the Call Tokens](move-the-reasoning-path-not-the-target-tokens.md)
- [Split skills to hide future steps and force more leg work per step](split-skills-to-hide-future-steps-and-force-leg-work.md)
- [Agent skills package progressive-disclosure context for repeatable workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md)
- [Prompt coding agents around learned model habits](prompt-coding-agents-around-learned-model-habits.md)
- [Maintain ubiquitous language for AI coding](maintain-ubiquitous-language-for-ai-coding.md)

Sources:
- [Building Great Agent Skills: The Missing Manual - Matt Pocock](../sources/20260629_UNzCG3lw6O0.md), 11:54-14:55
- [Bringing Continual Learning into Enterprises — Samuel Denton, Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 12:22-13:38
