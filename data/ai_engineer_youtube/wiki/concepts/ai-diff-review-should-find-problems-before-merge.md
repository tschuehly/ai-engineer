# AI Diff Review Should Find Problems Before Merge

Summary: AI-generated diffs need defect-finding checks before humans either inspect every line or merge on trust. A useful reviewer system asks what is wrong with a diff and turns that answer into immediate feedback while code is still being shaped.

Use when:
- Designing review loops for agent-generated pull requests or local diffs.
- Choosing quality gates for coding agents that can emit more code than humans can inspect.

Details:
- Imbue's Sculptor work is framed around the production-code gap: coding agents can produce prototypes, but larger codebases need tools that make generated changes trustworthy (00:18-01:23).
- The useful domain-specific question is not another generic model wrapper, but "what is wrong with this diff?" because model progress may solve many generic parsing and inference annoyances while code-quality review remains application-specific (01:53-02:38).
- A second AI system can give reviewers a third option between line-by-line inspection and blind merge by checking for concrete issues such as race conditions or leaked API keys (02:38-03:21).
- Sculptor aims to surface defects synchronously when code is generated or a line changes, rather than waiting for a late pull-request review pass (03:26-04:28).

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Make code review the bottleneck skill for AI-generated code](make-code-review-the-bottleneck-skill-for-ai-generated-code.md)
- [Separate generation and verification prompts or models](separate-generation-and-verification-prompts-or-models.md)
- [AI review gates turn standards into executable feedback](ai-review-gates-turn-standards-into-executable-feedback.md)

Sources:
- [Beyond the Prototype: Using AI to Write High-Quality Code - Josh Albrecht, Imbue](../sources/20250725_x_1EumTaXeE.md), 00:18-04:28
