# Replay Production Failures Before Promoting Prompt Fixes

Summary: Prompt fixes should be validated by replaying the triggering production failure and rerunning the broader regression set before the change is trusted.

Use when:
- A production trace reveals a bad AI decision or missing business nuance.
- A prompt patch appears to fix one case but may regress others.

Details:
- The workshop warns against a pattern where a system fails in production, someone patches the prompt, and the team waits until the next failure mode appears without durable tracking, 07:13-07:46.
- In the remediation example, a customer says an issue is not urgent, but the CFO and board-meeting context make it business-critical; the workflow treats this as a failure mode to identify and remediate, 01:19:27-01:20:10.
- The replay loop is to run the failure from a data set, apply a specific evaluation, tighten the prompt, rerun it, and then check the entire test suite for regressions, 01:20:18-01:20:41.
- The closing summary says the team picked a production failure, inspected its trace, modified the prompt, reran the evaluation, and verified the score returned to the target level, 01:34:17-01:34:33.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use golden data sets and mixed scoring functions for AI application confidence](use-golden-data-sets-and-mixed-scoring-functions-for-ai-application-confidence.md)
- [Apply online scoring to production traces with cost-aware sampling](apply-online-scoring-to-production-traces-with-cost-aware-sampling.md)

Sources:
- [Shipping complex AI applications - Braintrust & Trainline](../sources/20260501_ZdheJTfLu-s.md), 07:13-07:46, 01:19:27-01:20:41, 01:34:17-01:34:33
