# Thread Every Outcome Back to the Decision That Caused It

Summary: An automation becomes a self-improving system only when each action it takes is written down as a decision and each observed outcome is attributed to the decision that produced it. The attribution is what lets the decision layer itself continue, advance, or pivot, instead of leaving the improvement to an analyst reading aggregate output quality.

Use when:
- Building the fourth layer of an act-on-the-world system and the current plan is a dashboard.
- Deciding how engagement, conversion, or acceptance data should re-enter an agent's decision process.
- Diagnosing why an automated sequence keeps repeating a step that never works.

Details:
- The requirement is stated as a pair: "every action is a decision log and every outcome threads back to the decision that caused it," which is what "turns this automation into a system that self-improves." ([Liu](../sources/20260826_L4I7WgiEquo.md), 14:53-15:03)
- **The contrast names the thing most teams actually build.** "The naive version of this is a data analyst coming in and trying to understand if the output of this could be better. The rebuilt version of this is wiring our engagement history back into the decision layer." The difference is not more analysis; it is who consumes the analysis. (15:03-15:16)
- The consuming decision has three explicit branches: "the system decides whether or not to continue a thread, advance to the next step, or pivot" — and the same treatment is applied to "lifecycle message performance history," so both the sales and marketing paths feed the same layer. (15:16-15:31)
- The purpose is stated as reliability rather than optimization: "these verification loops are really critical so that the system can self-heal and continuously improve." (15:31-15:37)
- The decomposition places this as the fourth question, "did it work," feeding back into the second, "what should happen next," which is why the loop is drawn as a loop rather than a pipeline. (05:47-06:25)
- Step-level tracing is a separate mechanism serving a different purpose: "every LLM step is traced so that we can evaluate quality and improve over time" is about the quality of a workflow's internals, while outcome threading is about whether the decision to run that workflow was right. Both are needed and they are not the same instrumentation. (14:46-14:52)
- **Limit.** This is the least demonstrated layer in the source. No worked example of a pivot, no metric, no attribution window, and no description of how an outcome is matched to a decision is given, and the two outcome figures reported are system-level results, not evidence that the loop closed. (14:53-15:37, 18:48-19:14)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)
- [Go To Market](../topics/go-to-market.md)

Related concepts:
- [Reduce Every Workflow to Know, Decide, Act, and Learn](reduce-every-workflow-to-know-decide-act-and-learn.md)
- [Close the Eval-to-Action Loop So Signal Survives the Dashboard](close-the-eval-to-action-loop-so-signal-survives-the-dashboard.md)
- [Operational Outcomes Are Eval Labels You Only See If You Own the Operation](operational-outcomes-are-eval-labels-you-only-see-if-you-own-the-operation.md)
- [Reverse-Engineer AI App Evals From User Outcomes](reverse-engineer-ai-app-evals-from-user-outcomes.md)
- [Emit Owner-Assigned Tasks From Signals, With a Marketing Default When None Fire](emit-owner-assigned-tasks-from-signals-with-a-marketing-default-when-none-fire.md)
- [Use Decision Logs to Keep Uncertain Agents Moving](use-decision-logs-to-keep-uncertain-agents-moving.md)

Sources:
- [AI in GTM at Notion — Flora Liu](../sources/20260826_L4I7WgiEquo.md), 05:47-06:25, 14:46-15:37, 18:48-19:14
