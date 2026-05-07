# #define AI Engineer - Greg Brockman, OpenAI (ft. Jensen Huang)

Source: [#define AI Engineer - Greg Brockman, OpenAI (ft. Jensen Huang)](https://www.youtube.com/watch?v=avWhreBUYF0)
Uploaded: 2025-08-10
Transcript: `raw/20250810_avWhreBUYF0/avWhreBUYF0.en-orig.vtt`

## Summary

Greg Brockman frames AI engineering as the work of turning model and research ideas into real systems: fast feedback loops, first-principles removal of obsolete constraints, research-engineering partnership, codebases shaped for model strengths, and infrastructure that supports both long-running agent work and realtime interactions.

## Extracted Concepts

- [Research Engineering Partnership](../concepts/research-engineering-partnership.md) - supports treating engineering systems and research ideas as coequal dependencies for model progress.
- [Model-Shaped Codebase Architecture for Coding Agents](../concepts/model-shaped-codebase-architecture-for-coding-agents.md) - explains why smaller tested modules and fast tests let coding agents do more useful work.
- [Agentic Coding Transforms Existing Software](../concepts/agentic-coding-transforms-existing-software.md) - distinguishes flashy greenfield demos from the deeper value of migrating and improving legacy applications.
- [Dual-Mode AI Infrastructure](../concepts/dual-mode-ai-infrastructure.md) - describes infrastructure pressure from long compute-heavy workloads and low-latency realtime workloads.

## Topic Links

- [Coding Agents](../topics/coding-agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Models](../topics/models.md)
- [Workflows](../topics/workflows.md)

## Notes

- Early Stripe customer work used constant chat contact and compressed a bank integration cycle by pairing implementation with top-down and bottom-up test-script work, showing how first-principles process changes can remove weeks of inherited organizational latency. 05:28-07:09
- Brockman cautions that not every constraint can be ignored; the useful move is to identify overhead tied to constraints that no longer apply to the specific situation, especially as AI changes productivity assumptions. 07:22-07:55
- Independent study compounded when motivation, exploration, and direct building let him advance faster than the default curriculum; he describes self-study as building things and experiencing them in the world, not only reading. 08:14-10:17
- Deep learning became compelling when people were making computers do materially new things, and the practical entry point was building a GPU rig and working through Kaggle-style problems. 10:43-11:54
- The research-engineering partnership is presented through AlexNet: fast GPU convolution kernels plus the idea of applying them to ImageNet made the result work; at current scale, engineering includes systems for 100,000 GPUs and complex RL orchestration. 16:23-18:05
- OpenAI's engineering/research interface problem is never fully solved; each scale level introduces new coordination problems between interface abstraction and researcher's need to understand implementation details. 18:44-19:24
- Future coding-agent work is expected to move beyond interactive vibe coding toward cloud-resident coworker-like agents that can keep working while the user's laptop is closed. 24:10-24:48
- The deeper coding-agent transformation is not joke websites from scratch but changing existing applications, migrations, library upgrades, and legacy language transitions that are hard and unpleasant for humans. 24:57-25:49
- Codebase structure determines how much Codex-style agents can help: smaller modules, quick tests, and clear architecture let the model fill in details and rerun checks repeatedly. 26:37-27:52
- AI infrastructure has at least two workload shapes: compute-intensive long-running work such as test-time scaling and low-latency realtime work; the hard part is balancing fleet ratios so one accelerator pool does not become useless. 32:25-34:06
