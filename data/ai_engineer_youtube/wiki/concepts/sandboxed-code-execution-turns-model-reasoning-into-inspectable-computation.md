# Sandboxed Code Execution Turns Model Reasoning Into Inspectable Computation

Summary: Giving a model a sandboxed execution tool lets it use computation and libraries for concrete work while keeping the user's local environment isolated.

Use when:
- A model needs to analyze data, transform artifacts, or verify a generated result with actual computation.
- Tool access should be useful without letting generated code affect the user's workstation or repository.

Details:
- AI Studio code execution gives Gemini a sandboxed Python environment with preinstalled data science libraries, which the model can invoke as tools for arbitrary data science tasks.
- The sandbox boundary is presented as the reason the user does not risk the generated code affecting their local environment.
- Code execution is available through the API and can be combined with compare mode to evaluate model variants under the same computational tool surface.

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Agent tool loops turn model-required actions into executable results](agent-tool-loops-turn-model-required-actions-into-executable-results.md)
- [Hackable agent runtimes need tight safety boundaries](hackable-agent-runtimes-need-tight-safety-boundaries.md)

Sources:
- [Build & deploy AI-powered apps - Paige Bailey, Google DeepMind](../sources/20260429_G_bHFmEAarM.md), 13:18-13:54, 46:09-46:26
