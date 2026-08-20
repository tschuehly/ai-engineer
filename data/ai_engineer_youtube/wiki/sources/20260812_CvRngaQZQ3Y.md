# Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain

Source: [Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain](https://www.youtube.com/watch?v=CvRngaQZQ3Y)
Uploaded: 2026-08-12
Transcript: `raw/20260812_CvRngaQZQ3Y/CvRngaQZQ3Y.en-orig.vtt`

## Summary

Vivek Trivedy leads applied research at LangChain and argues that continuously improving an agent is a data-mining problem over the traces the agent already produces. His recipe is four steps — ship the agent so it operates in real environments, collect every trace, mine that corpus, then run data-driven experiments to check whether a new prompt, tool, orchestration, or loop actually improved things against what the traces showed. The framing claim underneath it is that observability and continual learning are the same problem wearing different clothes: an agent acting in an environment produces trace data, and continual learning — for agents as for humans — is doing things in the world, thinking about what you did, and updating yourself in response. "If you're a continual learning company, you need traces." The reason traces rather than code carry the answer is that agent behavior is not readable off the source: agents have prompts, tools, skills, hooks, middlewares, and other agents they orchestrate in swarms, so a human cannot reason about how a prompt change will affect behavior at scale, and the effect differs between the medical and the legal domain anyway. Over four years "we've started trading determinism for autonomy," and the systems that recover understanding have to read the record.

Reading that record is where the engineering is. Two constraints dominate. Reading traces at scale is expensive and the cost is a simple product — input token price × number of traces × average trace size — and a single long session with a coding agent (Claude Code, Codex, deep agents) does not fit in the reading agent's context at all, so "it's no longer as simple as just feeding the data into context"; the trace has to be treated as an external object queried into, with agents built to mine data from other agents. Working with Harvey on their legal benchmark, LangChain matched Opus's trace-judging capability with an open, cheaper model at one to two orders of magnitude lower cost, and the route there was harness engineering informed by reading the frontier model's own traces — seeing how Opus reasons and giving the weaker model the guidance it needs to reach the same level. That fits their general practice of starting with Opus or GPT-5.5 only to establish that a task is possible ("the minimum level of intelligence that I need to do any given task"), then looking back at those traces to see whether an open model can do the same. Past the harness ceiling comes fine-tuning on a narrow vertical, since customers "don't really care about the entire variance of tasks," and past that a second economic switch: for very high inference workloads, move from token costs to hardware costs, run a cluster with unlimited inference, and spin it down when idle.

The mined traces have three outputs LangChain has productized: distillation and SFT datasets built from the good traces of a larger model to make a 9B or 13B mimic it; generated evals and environments; and prepared content for humans, who remain in the loop in high-trust domains like legal and medical but "can't read it all." Two hot takes carry the argument. The first is that you can describe an agent's behavior just by showing the evals it was measured against, because it hill-climbs them and "the purpose of evals is roughly to try to make them pass." The second, from his scikit-learn-era PhD, is "model harness task fit" — the same fit function as classical ML, now over data, a harness, and a model, which makes the two remaining jobs finding good fit functions (auto research, RL methods) and finding good data. Agents are good at making a score go up and "might cheat a little bit, and you need to check them on some stuff." The rule for sequencing is feedback speed: harness engineering answers in about two minutes, so exhaust that ceiling, fine-tune to break through it, then return to harness engineering. He closes on dense feedback — a benchmark that returns only pass or fail gives an agent nothing to act on, while traces are "the substrate that hold that feedback" — and on updating agent state across three axes: training data, the harness (which looks the way it does because models were trained in it and because of the tasks it does in the real world), and memory, which "cannot just append everything to a really big file and then search over it" and instead wants sleep-time compute reading the whole lifecycle.

## Extracted Concepts

- [Observability and Continual Learning Are the Same Problem](../concepts/observability-and-continual-learning-are-the-same-problem.md) - The talk's thesis: an agent acting in an environment produces the only real record of what happened, and that record is the substrate both disciplines are built on.
- [Mine Trace Corpora With Agents Because They Do Not Fit in Context](../concepts/mine-trace-corpora-with-agents-because-they-do-not-fit-in-context.md) - Names the two constraints — a multiplicative token cost and a single trace that exceeds the reader's context — and the response of querying the trace as an external object.
- [Ask Traces the Behavioral Questions Code Cannot Answer](../concepts/ask-traces-the-behavioral-questions-code-cannot-answer.md) - Supplies a concrete question catalog including the compaction-degradation question and model counterfactuals.
- [Read the Frontier Model's Traces to Harness-Engineer Its Cheap Replacement](../concepts/read-frontier-traces-to-harness-engineer-a-cheap-replacement.md) - The Harvey legal-benchmark result: open-model trace judging matched Opus at one to two orders of magnitude lower cost via trace-informed harness engineering.
- [Sequence Harness Engineering and Fine-Tuning by Feedback Speed](../concepts/sequence-harness-engineering-and-finetuning-by-feedback-speed.md) - The ~2-minute feedback loop as the decision criterion, plus the harness → fine-tune → harness sandwich.
- [An Agent's Eval Suite Describes Its Behavior](../concepts/an-agents-eval-suite-describes-its-behavior.md) - The hot take that evals are a behavioral description because the agent hill-climbs them.
- [Densify Agent Feedback Because Pass/Fail Is Not Actionable](../concepts/densify-agent-feedback-because-pass-fail-is-not-actionable.md) - A single terminal bit gives an agent no signal about what to do next; traces already hold the fine-grained record.
- [Treat Agent Improvement as Model-Harness-Task Fit](../concepts/treat-agent-improvement-as-model-harness-task-fit.md) - The scikit-learn `fit()` analogy and the two jobs it implies: find fit functions, find data.

## Topic Links

- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)
- [Models](../topics/models.md)
- [Workflows](../topics/workflows.md)
- [Inference](../topics/inference.md)

## Notes

### The four-step recipe (01:11-02:21)

Ship the agent first, because only a shipped agent operates in environments and produces feedback. Collect a ton of traces — "agents operate in the environment every single time they operate, they do tool calls, they have output messages, they call APIs, they use CLIs. All of that generates data and we want to store all of that." Mine that corpus, which may run to gigabytes or terabytes depending on how many agents are shipping. Then run the experiments in a data-driven way to check whether "this new prompt, or this new tool, or this new orchestration, or this new loop" is actually improving things "based on the previous traces that I've seen."

### Observability and continual learning are the same problem (02:21-03:06)

Flagged as "maybe a bit of a hot take." The coupling is causal: agents that operate in environments produce trace data, and continual learning for agents and for humans is the same shape — "I do a bunch of stuff in the world, I think about what I did, and then I need to update my definition, like my knowledge, stuff I write down, in order to respond to the feedback from the environment." The operational consequence is stated bluntly: "if you're a continual learning company, you need traces, and if you have traces, then you can try to do continual learning over your agents."

### Why agents are harder to reason about than code (03:31-04:19)

With a Python code block on screen he can read the functions, see how they call each other, and roughly understand the logic. "That doesn't exactly exist in agent world because agents have prompts, they have tools, they have skills, they have hooks, they have middlewares, some agents call other agents and I orchestrate them in swarms. It's really really hard for humans to reason about how certain prompts that they change are actually going to affect agent behavior at scale." The effect is also domain-conditional: "a prompt change you're using for the medical domain is going to be like completely different than a prompt change that you want to do for the law domain."

### Trading determinism for autonomy (04:19-04:40)

"Over the last four years since the ChatGPT moment, we've started trading determinism for autonomy. And in that shift, sort of what we need to do is create tools and create systems to still understand agents when they're autonomously operating in environments."

### Sending agents to read other agents' traces (04:40-05:57)

The mechanics at LangChain: centralize data into a tracing project, either per agent or across all agents, "and then what we do is we send agents to read traces from other agents." Three question shapes are named.

- Sentiment and outcome mining: "find a bunch of like good and bad interactions where like users got upset or like users are like really happy."
- A technical question the code cannot answer: "Agents now run for millions of tokens. Does the agent get really dumb after the first compaction? After the second compaction? Does it never get dumb? Like how do we actually answer these questions? We need to do it by actually looking at the traces."
- Counterfactuals: "I ran GPT 5.5 for this and I heard like GLM is really good. What happens if I run GLM 5.2 for this task and how do I compare them?" He notes that the trace level "captures the actual behavior that users see," which makes it useful for seeing behavior at fine-grained scales.

### Today's data is the least we will ever have (05:59-06:35)

"The data that we see today is going to be the smallest that humans have ever seen in their entire lives because we're in this massive exponential shift to our agents are doing more and more work in the economy." He expects the volume humans produced across a lifetime to be eclipsed by agents running on year scales, then 6-month, 3-month, and eventually daily scales.

### Two constraints on reading traces (06:35-07:36)

Cost is multiplicative and easy to compute: "think of it as like an input token cost. You can like literally multiply the input token cost times the number of traces times like how big each trace is on average," and the problem bites with millions of traces at millions of tokens per trace.

Capacity is the harder one. "If I have a super long interaction with a coding agent like Claude Code or Codex or like deep agents, I can't even read that trace with another agent because that context like doesn't fit in memory." The response: "we need to develop systems so I can sort of treat that context as like an external object and then I can sort of query into it… we need to build agents to efficiently mine data from other agents and it's no longer as simple as just feeding the data into context."

### Not reaching for a frontier model every time (07:36-08:16)

"One of the things that I think is really really cool in the last 6 months is that open models have basically hit an inflection point in intelligence that we at LangChain don't reach for the frontier models for every single use case. We're quite conscious about what is the minimum level of intelligence that I need to do any given task."

The workflow that follows is a waterline: "practically speaking, honestly, yes, we start with Opus, we start with 5.5 because we just want to know if the task is even possible. But then once we reach that sort of like waterline, then we like look back at those traces and we see, 'Hey, can we use an open model to do the same thing?'"

### Matching frontier trace judging with an open model (08:16-08:58)

The measurement is from work with Harvey on their legal benchmark: "can I match the trace judging capability of Opus with an open cheaper model? And the answer is roughly yes at like an order or like two orders of magnitude cheaper."

The method: try a bunch of models plus "a bunch of like harness engineering, and the harness engineering is informed by a bunch of the traces that we read. So it's like, 'Hey, like Opus reasons about things in this way. Maybe that's because of the prompt. Maybe Opus is just smarter, which it is, than a bunch of the open models, but that might mean I need to give it a little bit more guidance so it can reach the sort of same intelligence level at like a much much lower cost.'"

### Where harness engineering stops paying (08:58-09:48)

"Harness engineering is amazing. You get instant feedback and you can sort of like run on your evals, but eventually what we find is you hit a threshold of intelligence where it's like 'If I keep tweaking this prompt, I'm not going to get too much more out of it.'"

Then fine-tuning on a narrow vertical: "if we take like base models and we tune them on like very specific vertical tasks, which is what a lot of our customers do, they don't really care about the entire variance of tasks. Like they care about what their customers care about. So, if we focus on that narrow set of tasks, then we can fine-tune base models to sort of like reach and then also go beyond frontier performance."

### Trading token costs for hardware costs (09:48-10:27)

"Another sort of like economic decision is that you can move from token costs to hardware costs. And this is like can be a really big change… you're very used to hey, like a million tokens cost this much, not as much like this cluster sort of costs this much. But for like very high inference workloads, we find it to be way cheaper just to like run a cluster and I get like unlimited inference on that cluster. I don't have to worry about tokens… and then I can spin it down when I don't need it."

### The product (10:27-11:08)

Explicitly flagged as a product pitch — "I won't shill it too much." The transcribed name is "LangSplat engine"; the exact product name is not recoverable from the captions (see Caption Artifacts). What it does is the automated version of the loop: given any volume of trace data, if you are looking for something in it, want to generate evals from it, or want to generate feedback for humans to read, "it will go read all of it, it'll like find issues, it'll agentically search over it, and they can like prepare data sets for you to do something after."

### Three outputs of trace mining (11:08-12:46)

1. **Distillation and fine-tuning.** "Let's say I'm running GLM 5.2. It's doing great, but I think that I can run this task like way cheaper with like a 9B or 13B model. Then what I'll do is like I'll take the good traces and the good examples from the GLM 5.2 runs, I'll prepare them in a data set, and then I'll try to fine-tune a small model on that data set to like mimic behavior… this is like distillation, SFT."
2. **Generating evals and environments.** "Maybe another slightly hot take, I think you can basically define agent behavior by showing the evals that you ran on it. Like, if someone showed me all the things that they're trying to test their agent on, I think I would have a rough idea about how that agent is going to behave because it literally like hill climbs those evals, and you alter the behavior of the agent to make the evals pass. Like, the purpose of evals is roughly to try to make them pass."
3. **Preparing content for humans.** "Humans are still in the loop. Like, I need to know that customers are happy. I also want to know what my agents are doing. I just don't have the bandwidth to read a bunch of traces. So, preparing content for humans is still like really, really valuable today, especially in like high-trust domains like legal and medical. Like, some human needs to review this, but they can't read it all, so we try to make it easy for them to process all that data."

### What scikit-learn has to do with any of this (12:46-14:07)

His PhD added algorithms to scikit-learn, which "at an abstract level, it's a bunch of helpers to fit learning systems to data." He argues the same principles apply to what he calls "this agent-first world," under the name **model harness task fit**: "we still have this sort of like fit function that I'm going to try to like take my data, take a harness, take a model, and I'm going to try to fit it all together to make sure that all of my tasks pass. The algorithms look slightly different, but the overall process of machine learning doesn't really look that different."

### Finding fit functions and finding data (14:07-15:24)

"A couple of our main jobs now are find good fit functions. So, these are like auto research. This is tons of great work that's being done in RL on different methods…" (the method names are garbled in the captions; see Caption Artifacts). "And also find good data. If you put those two things together, then that is basically the applied or just overall research question that every team has to make their agents better."

Auto research in practice: "if you have some sort of score that you can make number go up, agents are pretty good at making that number go up. They might cheat a little bit and you need to like check them on some stuff. Um, but this sort of like general feedback loop of do something, read the results, read the traces, and then do an update ends up being pretty useful." The worked example predates the term: "terminal bench is like really hard. What would happen if an agent just like read its traces, proposed experiments, and then tried to do fixes?"

### Why dense feedback matters (15:21-15:58)

"Like terminal bench, the output is just a number, right? Like, did you pass or did you not pass? That's like kind of helpful, but if I give you like a super random task, like you just did a bunch of stuff, and then I just said like you failed or you passed — if you failed, like you wouldn't really have a good signal to figure out what you should do next. So, densifying feedback is a really good way to improve agents, and like traces are the substrate that hold that feedback. And then agents are very good at reading those traces and then figuring out like what to do next."

### Harness engineer, fine-tune, harness engineer again (15:58-16:51)

The decision rule is feedback latency, not capability: "if you need to do something for improving your agent, the best thing that you can do is collect feedback as quickly as possible, like either from humans labeling or just letting the agents run. So, like harness engineering gives you feedback in maybe 2 minutes."

"Once you sort of saturate the harness engineering ceiling, then you can maybe try to do like fine-tuning after that, but we find a lot of teams are happy with harness engineering and it solves their customer use case, so we always sort of recommend it. And then we have this like sort of sandwich, which is like try harness engineering, try to do fine-tuning to sort of like break through that ceiling, and then do more harness engineering again if you need to."

### Updating agent state across three axes (16:51-18:08)

The loop restated: "there's an agent taking actions in the environment, and then it needs to use that information to update information about itself." Two examples of what an update looks like: "I did a bunch of these tasks, and I need to update my prompts to make sure I do them more efficiently," or "users keep asking to search for these types of things, I should maybe tell my creator that they're doing this sort of stuff."

"What that looks like today, slightly unclear, but we think that you're going to have to do it across all three axes":

1. **Training data** — "observational data from agents taking actions."
2. **Harness updates** — "the Codex harness and the Claude Code harness and like our harness and everyone's harness, like they look a certain way because like models are trained in them and they look a certain way because of the tasks that they do in the real world, and we think evolving those over time is going to be super important in order to make them work."
3. **Memory** — see below.

### Sleep-time compute and memory that is not append-only (18:08-18:49)

"We humans are like really good at remembering stuff over time, but we are not append-only logs of information. And if agents are going to be working with us over like year, 5-year, decade, lifetime time scales, we cannot just append everything to a really big file and then search over it. There's a ton of stuff that needs to happen with updating those files over time and then just making memory like really efficient. But, we think a lot of that actually comes from this idea of scaling sleep time compute and dreaming generally. So, it's like read all of the traces over the entire agent life cycle and then do things to update agent state."

### Takeaways (18:49-19:40)

"Mining traces gives you signals to hill climb on. If you have an agent, just turn on tracing and point an agent at it and that's like the easiest thing that you can do to basically understand what your agents are doing." Plus the vendor line — LangChain is "very excited about open models," wants to help teams fine-tune them, and provides them as a service — and the closing frame: "continual learning is about operating environments and then integrating that data back into agent state," in a world where "we have systems that are going to produce more data than we ever have before."

## Provenance Caveats

- The speaker leads applied research at LangChain, and the talk ends on a product pitch (a trace-mining product) plus an offer to help teams fine-tune open models "as a service." The workflow he describes runs on his employer's tracing product. He flags the pitch himself ("I won't shill it too much").
- The Harvey one-to-two-orders-of-magnitude figure is a single customer engagement reported by the vendor, with no published methodology, no baseline table, and no named open model. The structural claim it illustrates — that trace judging is a bulk workload where harness engineering can substitute for model capability — is separable from the number.
- "An order or like two orders of magnitude cheaper" is itself a 10× band of uncertainty, stated as such.
- He does not claim the fine-tuning path is generally necessary: "a lot of teams are happy with harness engineering and it solves their customer use case, so we always sort of recommend it."

## Caption Artifacts

Resolved with reasonable confidence:

- "Cloud Code" → Claude Code (07:07, 17:51).
- "e-vals" → evals (10:47).
- "harness Enge" → harness engineering (16:03-16:07).
- "psych" → scikit (12:53); "trySFT" in the RL-method list is at minimum "try SFT" or a garbled method name.
- "5.5" spoken once as "55" (08:03), consistent with the "GPT 5.5" said earlier.

Left unresolved, with no claim in this note depending on either:

- The product name transcribed as "LangSplat engine" (10:34). The speaker works at LangChain and is describing a trace-mining product built on their tracing stack, so the first word is very likely a mis-transcription of LangSmith, but the exact shipped product name is not recoverable from the captions and is not asserted here.
- The RL method list at 14:17-14:22, transcribed as "OPD, OPSD, trySFT." These are almost certainly abbreviations of known post-training methods, but which ones cannot be determined from the captions, so no method names are attributed.
- "A bit of a leader" (11:01) reads as "a bit of a lead-in"/teaser for the next section; nothing depends on it.

Model versions are recorded as spoken (Opus, GPT 5.5, GLM 5.2) without independent verification.
