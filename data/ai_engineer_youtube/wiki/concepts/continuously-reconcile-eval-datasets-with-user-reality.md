# Continuously reconcile eval datasets with user reality

Summary: Eval datasets are not fixed truth; they should be maintained against real user experience and product intent. The useful capability is the team's ability to identify important feedback, add representative cases, and keep the dataset aligned with reality.

Use when:
- Turning production complaints, thumbs-down feedback, or support findings into regression cases.
- Deciding whether an eval set has become stale, synthetic, or detached from user-visible failures.

Details:
- Goyal argues that for most real-world use cases, a dataset created ahead of time will not fully represent what users actually experience, 02:26-03:00.
- One sign of eval competence is a clear path from user complaint to eval case so product learning is not lost, 01:10-01:35.
- The Q&A cautions against blindly adding every feedback item. A human with product taste should choose interesting user datapoints and decide whether the attempted task should obviously work, 15:37-16:07.
- The overfitting risk is worse when the team overfits to a static dataset that lacks user feedback than when it deliberately reconciles the dataset with desired product reality, 14:55-15:30.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Connect production observability to offline eval loops](connect-production-observability-to-offline-eval-loops.md)
- [Replay production failures before promoting prompt fixes](replay-production-failures-before-promoting-prompt-fixes.md)
- [Product engineers need direct customer context](product-engineers-need-direct-customer-context.md)

Sources:
- [Five hard earned lessons about Evals - Ankur Goyal, Braintrust](../sources/20250823_a4BV0gGmXgA.md), 01:10-03:08, 14:55-16:07
