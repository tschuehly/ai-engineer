# Use neural debugging to fill code by simulated execution

Summary: A code world model can act like a neural debugger when it completes partial code by simulating how the surrounding program would execute. The interface lets developers express desired program shape in code, then lets the model infer missing pieces from execution dynamics rather than only natural-language instructions.

Use when:
- Designing code-assistance tools where partial code structure is more precise than prose.
- Evaluating whether a code model understands local variables, loop dynamics, and state changes.

Details:
- CWM is described as tracing functions line by line with high accuracy and reporting local variable values at specific points. 12:01-12:38
- The neural-debugger framing contrasts prose-only prompting with inline code sketches: a developer can leave holes in a loop or condition, and the model can use simulated execution to infer what the missing variables or assignments should be. 12:39-13:37
- This workflow is not just generating code; it helps the user compose with code side by side while expressing semantics loosely through structure and precisely through executable context. 13:37-13:57
- The talk speculates that the same implicit execution model could approximate expensive reasoning about halting behavior or distributed-system debugging, but presents this as an approximation and research direction rather than a decidability guarantee. 14:01-15:39

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Models](../topics/models.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Train code models on execution traces, not only syntax](train-code-models-on-execution-traces-not-only-syntax.md)
- [Use AI to scale codebase understanding against code slop](use-ai-to-scale-codebase-understanding-against-code-slop.md)
- [Sandboxed code execution turns model reasoning into inspectable computation](sandboxed-code-execution-turns-model-reasoning-into-inspectable-computation.md)

Sources:
- [Code World Model: Building World Models for Computation - Jacob Kahn, FAIR Meta](../sources/20251217_sYgE4ppDFOQ.md), 12:01-15:39
