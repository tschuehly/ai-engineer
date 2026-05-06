# Neural weather models can target operational forecast variables directly

Summary: Neural weather models can learn from decades of global weather data to produce operational forecasts that compete with physics simulation. The model target matters: general atmospheric state, probabilistic weather tails, and direct cyclone prediction call for different architectures and evaluation criteria.

Use when:
- A prediction problem has rich historical sensor or simulation data and expensive physics-based baselines.
- The operational need is a specific phenomenon, such as cyclone trajectory, rather than a broad intermediate state.

Details:
- The source says weather prediction became tractable for neural networks because roughly 40 years of global weather data was available, 10:30-10:55.
- GraphCast predicts global atmospheric state up to 15 days out across many variables using a spherical graph neural network and autoregressive prediction, 10:58-11:39.
- In a Hurricane Lee example, GraphCast predicted landfall nine days out while gold-standard physics models were described as accurate six days out, making the extra three days operationally meaningful, 11:42-12:38.
- GenCast is described as probabilistic, more accurate, and more efficient; probabilistic forecasting matters because chaotic weather requires tail-risk information, 12:45-13:12.
- FGN directly predicts cyclone categorization, trajectory, wind speed, and other cyclone behavior instead of forecasting weather first and adding a detector as post-processing, 13:44-14:12.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)
- [Models](../topics/models.md)

Related concepts:
- [Compare models by task, thinking budget, cost, and latency](compare-models-by-task-thinking-budget-cost-and-latency.md)
- [Use golden data sets and mixed scoring functions for AI application confidence](use-golden-data-sets-and-mixed-scoring-functions-for-ai-application-confidence.md)

Sources:
- [How Google DeepMind is researching the next Frontier of AI for Gemini - Raia Hadsell, VP of Research](../sources/20260418_zZsTVBXcbow.md), 10:30-14:12
