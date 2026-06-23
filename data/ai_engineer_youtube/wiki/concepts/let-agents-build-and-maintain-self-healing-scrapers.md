# Let an Agent Build and Maintain Self-Healing Scrapers

Summary: Writing a scraper is no longer the hard part — maintaining it is, because sites constantly change selectors and structure. An agent with managed web access can do the whole loop: explore the site, understand the data, write a reusable parser script, run it, and repair it on a schedule when it breaks, so collection becomes a self-healing pipeline instead of a 2am page.

Use when:
- Standing up a recurring data-collection or monitoring pipeline (price tracking, listings, market research) against sites that change their HTML over time.
- Deciding whether to LLM-parse every page or have the agent build a deterministic scraper once and run that.
- Tempted to babysit brittle scrapers manually instead of letting the agent own build-and-maintain.

Details:
- The cost reframe: you write a scraper and then maintain it, and "sometimes you maintain it more than it takes you to write it," especially when the site changes selectors or is a React app; breakage means missing data and waking up in the middle of the night for clients. (01:35-01:47, 01:25-01:33)
- The agent owns the full loop — explore the site with the MCP, understand what data is needed, write the scraper, run/execute it, and maintain it — and the speaker's closing logic is "if it can build a scraper, it can maintain the scraper." (01:50-02:02, 22:19-22:23)
- Self-healing schedule: every ~30 minutes (e.g. a Claude Code schedule) an LLM spools up, runs collection, checks the data against a validation, and shuts down if everything is fine; if a data point is missing it re-explores and fixes the scraper in ~5 minutes with no human paged. Always set a data validation so the loop knows when to repair. (02:03-02:27, 15:03-15:08)
- The mechanism that makes this cheap is building a reusable parser script instead of pouring pages through the LLM: building the scraper for three pages can save ~a million tokens versus parsing everything with an LLM, and the demo measured ~62% token savings on a structured site (more on messier HTML). (05:12-05:23, 14:43-14:47)
- Once the script exists, the agent runs it rather than re-parsing: executing the built script costs ~60-100 tokens versus ~10,000 tokens to walk the JSON with the LLM — "literally pennies compared to what it would be to actually scrape it." The speaker's standing rule is "build a script that can later on be used by it… it's using its own script to save tokens." (17:23-17:39, 21:10-21:21, 20:52-20:59)
- A "skills" page (a Bright Data GitHub repo of scraper-building best practices) bootstraps the agent: it pulls the skill set first, then uses the MCP to extract a page's HTML and find the selectors it needs before writing the parser. (01:03-01:14, 02:48-03:05, 04:08-04:25)
- The same pipeline serves personal automation, not just enterprise scale — a scheduled "listener" can watch a marketplace for an apartment under a price or auto-book a hard-to-get restaurant table the moment a slot opens. (08:05-08:24, 22:33-22:55)

Related topics:
- [Tools](../topics/tools.md)
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Ground Agents With Managed Web-Access Infrastructure](ground-agents-with-managed-web-access-infrastructure.md)
- [Start Expensive With Agents, Then Collapse Proven Steps](start-expensive-with-agents-then-collapse-proven-steps.md)
- [Validation Errors Can Drive Agent Self-Repair Loops](validation-errors-can-drive-agent-self-repair-loops.md)
- [Compile Natural Language Analytics Into Reusable Deterministic Widgets](compile-natural-language-analytics-into-reusable-deterministic-widgets.md)
- [Move Mandatory Brittle Tool Steps Outside the Agent Loop](move-mandatory-brittle-tool-steps-outside-the-agent-loop.md)

Sources:
- [From MCP to Scale: Pipelines That Build Themselves — Rafael Levi, Bright Data](../sources/20260607_zTZ0qunQXnM.md), 01:25-02:27, 04:08-05:23, 14:43-15:08, 17:23-22:55
