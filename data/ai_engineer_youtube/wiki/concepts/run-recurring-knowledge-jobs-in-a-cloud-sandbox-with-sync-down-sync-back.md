# Run Recurring Knowledge Jobs in a Cloud Sandbox With Sync-Down/Sync-Back

Summary: When an agent job is too slow to wait for and must run on a cadence, move it off the laptop: stand up a cloud sandbox on a schedule, sync the Markdown corpus down, run the skill, sync it back up. A local automation is simpler but silently depends on the laptop being awake.

Use when:
- An enrichment, synthesis, or digest pass takes long enough that you would not sit through it interactively.
- You want overnight or daily agent work on a corpus that lives on your own machine.
- Choosing between a local scheduler (cron, a desktop app's automations) and a cloud runner for a personal or team agent job.

Details:
- Latency is the reason to schedule at all, not convenience: "it's really nice that you can ask an agent to generate these on demand, but as we can see with our little agent running in the background, it can take time for an agent to go generate these things. So ideally we have a flow that will sort of do this in the background for us. maybe while we sleep, maybe on an automated schedule," daily or weekly. ([LLM Knowledge Bases](../sources/20260812_I3bpdgFJCUY.md), 13:31-14:10)
- The local-automation constraint, named concretely on a competitor's feature: the Codex app's automations "spin up tasks to run on your machine every day, but it means your laptop has to be cracked open when it runs because it's a local automation." A daily job whose reliability depends on a closed lid is not a daily job. (14:10-14:24)
- The architecture is four steps and no persistent server: "we create an automation that takes our folder of markdown, syncs it into a box, maybe like a cloud sandbox powered by Docker if you need it… and then sync it back up when the agent's done." (14:56-15:11)
- Sync mechanism and the alternative he considered and rejected: the Obsidian headless CLI "lets you take a bunch of markdown on your computer and sync it somewhere else and then pull it back down. You could also just do like a git clone too if you want to be a little bit less creative, put all of your notes in a GitHub folder so that way a cloud agent could pull it down and do it for you. I prefer using Obsidian CLI for this just because it avoids having to like push and pull your notes. No one has time for that. I just want it to sync in the background." The decision axis is whether the human is in the sync loop, not capability. (15:11-15:42)
- What runs inside: install the sync CLI into the sandbox, pull the corpus, "instruct the agent run enriched note across [n] notes that are not enriched yet and then let it do all of its tool calls and code diffs and then by the time it's done it'll sync it back up. That's really the flow. It's super simple." The work selection depends entirely on [state stamped into the artifacts](stamp-processing-state-in-the-artifact-to-make-agent-passes-resumable.md), because the sandbox itself keeps nothing between runs. (15:44-16:10)
- The scheduled prompt is short and names the environment affordance rather than the procedure: "I gave you the Obsidian CLI in your environment. Use that, pull down that wiki, go ahead and update it, and I put in some special instructions for my own setup, and then sync it back up." Two schedules run — one for the wiki pass, one for `enrich note`. (16:13-16:47)
- The output is a review artifact rather than a notification: "when I come back to my computer in the morning, I wake up to a perfectly fresh wiki that I can review. It's like the daily paper, but it's your own." Runs remain viewable in the browser afterward, which is what makes a silent failure detectable. See [Start the workday by reviewing and dispatching agent work](start-the-workday-by-reviewing-and-dispatching-agent-work.md). (16:35-17:25)
- Triggers need not be time-based: the scheduler he uses (Warp's oz.dev / warp.dev/os — first-party, and the talk's main product pitch) also supports "other triggers like maybe a Slack message, iMessage, whatever you want to set up." (14:24-14:42)
- Unaddressed by the source, and worth designing before adopting: conflict handling when the human edits a note on the laptop while the sandbox is editing the same file, credentials for the sync CLI inside a sandbox that is torn down daily, and what a failed or half-finished run leaves behind on sync-back.

Related topics:
- [Workflows](../topics/workflows.md)
- [Infrastructure](../topics/infrastructure.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Stamp Processing State in the Artifact to Make Agent Passes Resumable](stamp-processing-state-in-the-artifact-to-make-agent-passes-resumable.md)
- [Ambient Agents Need Self-Maintenance and Memory Hygiene](ambient-agents-need-self-maintenance-and-memory-hygiene.md)
- [Start the workday by reviewing and dispatching agent work](start-the-workday-by-reviewing-and-dispatching-agent-work.md)
- [Generate an Entity Wiki Over Your Own Notes](generate-an-entity-wiki-over-your-own-notes.md)
- [Agent-native runtimes provide fast, API-controlled sandboxes](agent-native-runtimes-provide-fast-api-controlled-sandboxes.md)
- [Automate a Nightly Generate-and-Publish Media Pipeline With Sampled QA](automate-a-nightly-generate-and-publish-media-pipeline-with-sampled-qa.md)

Sources:
- [LLM Knowledge Bases: a practical guide — Ben Holmes, Warp](../sources/20260812_I3bpdgFJCUY.md), 13:31-17:25
