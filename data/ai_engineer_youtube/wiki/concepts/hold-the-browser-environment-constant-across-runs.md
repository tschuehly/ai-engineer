# Hold the Browser Environment Constant Across Runs

Summary: A browser agent's substrate — viewport, layout, browser build, network path — should render the same page identically on every run, because an environment that varies underneath the agent makes its successes and failures unattributable. The corollary is that the developer-machine setups teams reach for (a Mac mini at home, SSH'd into, clearing CAPTCHAs off a residential IP) are not a small version of production infrastructure; they fail on scale and on compliance.

Use when:
- A browser agent passes a task on one run and fails the same task on the next, and the diff is not in the prompt or the model.
- Choosing between a laptop/self-hosted browser, a rented desktop, and a managed browser fleet for agent runs.
- Writing the reliability requirements for an agent platform, where "works everywhere, every time" has to become a concrete list.

Details:
- The failure mode, stated concretely: "when your agent is running across a website multiple times, you want it to see the same inputs and outputs, the same page layout, the same size. If your infrastructure renders a page in a mobile layout one time and then in a desktop layout the second time, it's going to have inconsistent results." Responsive sites make this easy to hit — a viewport difference changes which elements exist, not just where they sit. ([Paul Klein IV](../sources/20260814_GqoNrUz8hEU.md), 09:50-10:09)
- Layering: consistency is the base, not a nicety — "consistency in the infrastructure is the nice base layer on top of your harness and on top of your models to actually get good results." A harness improvement measured on an inconsistent substrate cannot be trusted, because the substrate contributes variance that nothing in the experiment records. (09:50-10:09)
- The named anti-pattern is instructive because it *works* at n=1. When OpenClaw shipped, "everyone started buying Mac minis… because that's the best way to run macOS that you can SSH into and then end up solving the CAPTCHAs because of your home IP address." The residential IP is doing real work — it is why the CAPTCHAs are easy — which is exactly what makes the setup feel like a solution. (09:14-09:33)
- Two independent walls stop it from scaling: throughput ("that is not something you can do when you're building thousands of agents for customers in production") and audit ("I've yet to see a SOC 2 compliant Mac mini setup at scale"). The compliance wall is the one that cannot be engineered around incrementally, since a home machine has no path to an attestable control environment. (09:33-09:50)
- Boundary against eval-side advice, which asks for the opposite. [PRISM-style environments](design-eval-environments-to-the-prism-principles.md) deliberately vary data, theme, and starting screen, and [flight-simulator training](train-computer-use-agents-in-a-flight-simulator-not-on-exams.md) deliberately injects layout shift and focus stealing, because an agent that only works on one rendering has memorized a path. Both are compatible with this page: vary the *task and the site's behavior* as a designed input you record, and hold the *substrate* fixed so it does not inject variance you never chose. An unrecorded viewport flip is not robustness testing — it is noise that inflates the environment variance term in any [confidence interval you compute](compute-confidence-intervals-over-both-action-and-environment-variance.md).
- Practical consequence for observability: run-to-run comparison is only meaningful once the substrate is pinned, which is what makes screen recordings, logs, and network captures diagnostic rather than merely descriptive. See [Expose Observability As Agent-Readable Feedback](expose-observability-as-agent-readable-feedback.md). (14:35-15:10)

- **The constancy requirement extends across pipeline stages, not just across runs.** Šteimantas' shopping agent verified stock and sizes with one fetch path and transacted with another, and because only the second was geolocated, "items ended up being unavailable at checkout." Nothing was non-deterministic in the sense this page addresses; the two stages were simply pinned differently. The generalization worth carrying: an environment is a set of parameters — exit location, fingerprint, proxy pool, render engine — and holding them constant across *runs* while letting them vary across *stages within a run* produces reproducible pipelines that still contradict themselves. It is also the cost of the swappability argued for in [Keep a Protocol Boundary So the Browser Backend Stays Swappable](keep-a-protocol-boundary-so-the-browser-backend-stays-swappable.md): a drop-in replacement is wiring-compatible, not environment-equivalent. ([Šteimantas](../sources/20260826_XsvUhpnHepE.md), 06:08-06:30, 11:07-13:20)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Ground Agents With Managed Web-Access Infrastructure](ground-agents-with-managed-web-access-infrastructure.md)
- [Fix the Browser-Agent Runtime Interface Before Reaching for a Better Model](fix-the-browser-agent-runtime-interface-before-reaching-for-a-better-model.md)
- [Design Eval Environments to the PRISM Principles](design-eval-environments-to-the-prism-principles.md)
- [Train Computer-Use Agents in a Flight Simulator, Not on Exams](train-computer-use-agents-in-a-flight-simulator-not-on-exams.md)
- [Compute Confidence Intervals Over Both Action and Environment Variance](compute-confidence-intervals-over-both-action-and-environment-variance.md)
- [Measure Agent Robustness per Variation Axis, Not Just Average Success](measure-agent-robustness-per-variation-axis-not-just-average-success.md)
- [Keep Geolocation Consistent Across Pipeline Stages](keep-geolocation-consistent-across-pipeline-stages.md)
- [Keep a Protocol Boundary So the Browser Backend Stays Swappable](keep-a-protocol-boundary-so-the-browser-backend-stays-swappable.md)

Sources:
- [Bringing agents onto the world wide web — Paul Klein IV, Browserbase](../sources/20260814_GqoNrUz8hEU.md), 08:54-10:09, 14:35-15:10
- [The Missing Layer in Agentic AI — Giedrius Šteimantas, Oxylabs](../sources/20260826_XsvUhpnHepE.md), 06:08-06:30, 11:07-13:20
