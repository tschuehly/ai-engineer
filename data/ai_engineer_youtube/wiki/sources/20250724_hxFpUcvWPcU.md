# How to build Enterprise Aware Agents - Chau Tran, Glean

Source: [How to build Enterprise Aware Agents - Chau Tran, Glean](https://www.youtube.com/watch?v=hxFpUcvWPcU)
Uploaded: 2025-07-24
Transcript: `raw/20250724_hxFpUcvWPcU/hxFpUcvWPcU.en-orig.vtt`

## Summary

Chau Tran frames enterprise-aware agents as systems that combine agent flexibility with workflow predictability by discovering, retrieving, evaluating, and reusing company-specific task workflows. The talk argues that fine-tuning works for stable generalized behavior, while dynamic prompting through workflow search is more flexible for fast-changing or personalized enterprise practices.

## Extracted Concepts

- [Workflow Search Retrieves Enterprise Practice at Runtime](../concepts/workflow-search-retrieves-enterprise-practice-at-runtime.md) - this source introduces task-to-workflow retrieval as a way to guide agents with relevant company-specific process examples.
- [Golden Workflows Evaluate Agent Trajectories](../concepts/golden-workflows-evaluate-agent-trajectories.md) - this source distinguishes judging an agent's steps against a known workflow from judging only the final response.
- [Dynamic Workflow Prompting Fits Changing Enterprise Behavior](../concepts/dynamic-workflow-prompting-fits-changing-enterprise-behavior.md) - this source compares dynamic search-time prompting with fine-tuning for enterprise workflow adaptation.

## Topic Links

- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Retrieval](../topics/retrieval.md)
- [Workflows](../topics/workflows.md)

## Notes

- Workflows provide structure, predictability, lower latency, and debuggability for repetitive or known business processes, while agents provide open-ended planning and tool selection for less predictable work (02:03-04:27).
- An agent's execution trace can be interpreted as a generated workflow: given a task, the agent plans steps, executes actions, observes results, and leaves a sequence that can be compared, saved, or reused (05:20-06:16).
- A library of "golden workflows" can evaluate whether an agent found the right intermediate steps for a task, not just whether its final answer sounded plausible (06:18-07:10).
- Agents can also discover workflows: when users successfully complete a new task with an agent, the resulting trace can be saved as a company-specific workflow for later training or retrieval (08:49-09:20).
- Enterprise-aware agents need onboarding into company practices such as who to ask, which protocols to follow, and which executive metrics matter; general intelligence alone does not supply that internal context (09:31-11:03).
- Fine-tuning can generalize across many task/workflow examples, but it forks from the frontier model, requires retraining when tools or business priorities change, and is less suited to team or employee-specific workflows (11:18-13:16).
- Dynamic prompting through workflow search retrieves similar tasks and feeds their workflow representations as examples at runtime, creating a spectrum from creative agent behavior when no match exists to deterministic imitation when a high-confidence match exists (13:18-14:20).
- Workflow search needs more than textual similarity: enterprise systems may have many similar-looking documents or workflows, so authoritativeness signals such as creator relationship, success rate, and Slack discussion can help rank the right workflow (16:24-18:18).
