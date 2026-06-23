# Tune Coding-Agent Harnesses Per Model Family

Summary: A low eval score is usually a harness problem, not a model problem — measured gains for a coding agent come from container resources, timeouts, thinking-budget tuning, and prompt-engineering techniques, and those prompt techniques are model-family-specific (what helps Anthropic models does not transfer to Codex or Gemini), so supporting each new family is its own hill-climb that unlocks that family's user base.

Use when:
- A coding agent scores poorly with one model and you assume you need a better/newer model.
- Deciding what to change to raise an agent eval score: model swap vs harness and prompt tuning.
- Adding support for a new model family and wondering why your existing prompt tricks stop working.

Details:
- Cline raised its Terminal Bench score from an original 43% not by switching models but by harness levers: changing container CPU and memory, raising timeouts, and tuning thinking behavior — and asking the model to think *more* sometimes *interferes*, sending it into loops ("I am a model. I am a model." for ~2,000 tokens). (14:51-15:40)
- The most critical "nuance" lever is prompt engineering that is specific to a model family: techniques that apply to Anthropic model families "straight up would not apply to" the Codex model family and are "very different from" the Gemini family. This is why a model everyone calls great can fail for your specific harness. (16:03-16:53)
- The same model can behave very differently across coding agents (Claude models may work with Cursor or Droid but for some harnesses "just seems to work so much better with Claude Code"), so a benchmark run is partly testing whether *your harness* is leveraging the best of the model. (14:10-14:38)
- Business consequence: Cline was "very decent on Anthropic model families, not so much on" Gemini/Kimi families; deliberately hill-climbing to support a new family unlocks "entire swaths of people who love these models," so per-family tuning is a market-access decision, not just a score. (17:36-18:00)
- Nuance vs the stability claim: a maintained harness is still the right boundary against API/tool-surface churn, but it does not remove model-specific prompt tuning — that tuning is the per-family work that lives *inside* the harness boundary. (16:03-16:53)
- Validate the gains both ways: a higher number must also pass the vibe check (does the product actually feel good to use on that model). (16:54-17:21)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Models](../topics/models.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Portfolio-Allocate Eval Failures With a Triage Agent](portfolio-allocate-eval-failures-with-a-triage-agent.md)
- [Use Stable Agent Harnesses as Model-Evolution Boundaries](use-stable-agent-harnesses-as-model-evolution-boundaries.md)
- [Agent Harnesses Combine Model, Tools, Prompts, Filesystem, Skills, Hooks, and Memory](agent-harnesses-combine-model-tools-prompts-filesystem-skills-hooks-and-memory.md)
- [Fix Tool Discipline Before Reaching for a Bigger Model](fix-tool-discipline-before-reaching-for-a-bigger-model.md)

Sources:
- [Evals Are Broken, Use Them Anyway — Ara Khan, Cline](../sources/20260606_QuuIywMG4s8.md), 14:10-18:00
