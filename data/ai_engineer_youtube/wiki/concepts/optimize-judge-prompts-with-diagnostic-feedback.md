# Optimize Judge Prompts With Diagnostic Feedback

Summary: Prompt optimization for LLM judges needs more than output labels. The optimizer should see the candidate judge prompt, the judge verdict, the human ground truth, and diagnostic reasoning so it can repair the rubric that caused false approvals or false rejections.

Use when:
- Applying GEPA or another optimizer to an LLM-as-judge prompt.
- Debugging why an optimized evaluator is not learning from labeled traces.

Details:
- GEPA's `optimize_anything` API is presented as taking a candidate configuration, such as a judge prompt or prompt plus temperature, and an evaluator that runs the candidate system. 19:55-21:16
- For judge optimization, the evaluator should log diagnostics beyond the judge output, including error information and reasoning. 21:16-21:36
- The workshop improved GEPA optimization by writing a reflection template that sees the judge verdict, human ground truth annotation, and domain prior, then proposes clearer policy rules for the judge rubric. 29:13-31:15
- The optimized rubric learned parts of the airline policy criteria and improved accuracy from 69% to 74%, mainly by reducing a bias toward compliant labels and improving non-compliance precision/recall. 32:23-33:07
- The source cautions that the data was small, complex, unevenly distributed, and partly AI-generated, so the numbers demonstrate the workflow rather than a production-ready benchmark. 13:21-14:29

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Calibrate LLM Judges Like Binary Classifiers](calibrate-llm-judges-like-binary-classifiers.md)
- [Connect Production Observability to Offline Eval Loops](connect-production-observability-to-offline-eval-loops.md)

Sources:
- [Judge the Judge: Building LLM Evaluators That Actually Work with GEPA - Mahmoud Mabrouk, Agenta AI](../sources/20260410_X4dEHRzBLmc.md), 13:21-14:29, 19:55-21:36, 29:13-33:07
