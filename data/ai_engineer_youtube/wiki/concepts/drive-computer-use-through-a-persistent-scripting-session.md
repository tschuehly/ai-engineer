# Drive Computer Use Through a Persistent Scripting Session

Summary: Computer use began as a fixed action vocabulary the harness had to implement and the model had to emit one step at a time. Replacing it with code execution against a REPL that persists across turns lets the model automate the environment instead of operating it — inspect one page, then script the remaining hundred.

Use when:
- Building browser, desktop, or GUI automation for an agent and choosing between a typed action tool and a scripting sandbox.
- An agent's per-step screenshot-click-screenshot loop is too slow or too expensive for a repetitive task.
- Deciding whether environment state should live in the harness or in a session the model can reference by name.

Details:
- The old shape and its costs: computer use in the responses API "was fairly limited. It only allowed you to do one action at a time and… you had to basically declare that you wanted it to do computer use and from there you were up to actually implementing specifically the type of actions that were exposed to that tool." Two burdens — one action per round trip for the model, and an action-type implementation for the harness author. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 08:12-08:35)
- The new shape: "the recent models and the recent API shapes allow you to use code execution instead to actually do computer use, which means that the agent can script its own interactions with… whatever computer implementation you want to have. You can choose the language like JavaScript or Python and… you have a much more flexible harness." The action vocabulary becomes whatever the library exposes, so the harness stops being the bottleneck on capability. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 08:42-09:04)
- **Persistence across turns is the part that changes behavior.** Codex's browser use "interacts with a persistent node repl that gets persisted throughout… the turns. And then it writes JavaScript… essentially Playwright code to interact with that… browser instance in the node repl." Variables, page handles, and open tabs from turn one are still addressable on turn five. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 09:04-09:28)
- What that buys, in the source's own example: the first turn writes code to check status and pull up the right tab; later turns reference the new tabs and script actions, so the agent can "look at for example one page, understand the structure, and then write a script to perform like scraping for example on subsequent pages more easily." The expensive part — understanding the DOM — is paid once and then compiled into a loop. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 09:28-10:07)
- **This is the code-mode argument arriving in a third domain.** The wiki already carries it for large API surfaces ([Expose Large APIs Through Typed Code Mode](expose-large-apis-through-typed-code-mode.md)) and for trace classification ([Run Trace Classifiers as Code Mode in a Sandbox](run-trace-classifiers-as-code-mode-in-a-sandbox.md)). The distinguishing element here is statefulness: those uses run a script and take the output, while a GUI session has to be *held*, so the sandbox becomes a long-lived resource with a lifecycle rather than a per-call execution.
- The security position inherits from that: a persistent scripting session against a live browser is strictly more capability than a fixed action enum, which is why the wiki's [browser agents sit in the prompt-injection lethal trifecta](browser-agents-sit-in-the-prompt-injection-lethal-trifecta.md) warning applies more sharply here, not less. The source does not discuss confinement of the REPL itself.
- **Provenance.** Demonstrated live against a Chromium instance in a vendor talk. No comparison against the action-enum approach on task success, cost, or wall-clock; the speed claim ("that… speeds up these actions significantly") is qualitative, and the caption for that sentence is partly garbled. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 09:28-10:07, Caption Artifacts)

Related topics:
- [Tools](../topics/tools.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Expose Large APIs Through Typed Code Mode](expose-large-apis-through-typed-code-mode.md)
- [Run Trace Classifiers as Code Mode in a Sandbox](run-trace-classifiers-as-code-mode-in-a-sandbox.md)
- [Use Browser UI Control When APIs Are Absent](use-browser-ui-control-when-apis-are-absent.md)
- [Fix the Browser-Agent Runtime Interface Before Reaching for a Better Model](fix-the-browser-agent-runtime-interface-before-reaching-for-a-better-model.md)
- [Browser agents sit in the prompt-injection lethal trifecta](browser-agents-sit-in-the-prompt-injection-lethal-trifecta.md)
- [Model Async Agent Work as Spawn, Send, Wait, Shut Down](model-async-agent-work-as-spawn-send-wait-shut-down.md)

Sources:
- [Codex, Behind the Harness — Dominik Kundel, OpenAI](../sources/20260810_shRR1e2HXMk.md), 08:12-10:07
