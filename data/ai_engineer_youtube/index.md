# AI Engineer YouTube Index

- Channel: https://www.youtube.com/@aiDotEngineer/videos
- Generated at: 2026-07-11T13:23:40+00:00
- Since: 2025-07-11
- Until: open
- Videos: 476

## Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers — Alex Bauer, Upside.tech

- Upload date: 2026-07-11
- Video: https://www.youtube.com/watch?v=YZQsWVeN3rE
- Transcript: raw/20260711_YZQsWVeN3rE/YZQsWVeN3rE.en-orig.vtt
- Metadata: raw/20260711_YZQsWVeN3rE/YZQsWVeN3rE.info.json

A couple of years ago, everyone worried about AI hallucinating. We rarely hear that word anymore, but it’s just because the problem grew up. Today, your AI still doesn’t know how to say “I’m not sure.” Instead, it hands you a revenue number that’s wrong in ways that look exactly like being right.

The good news is we already solved this once, for people: you onboard a new hire so they understand your business; you put subjective, high-stakes calls in front of more than one set of eyes. This talk walks through patterns we run at Upside, including a librarian every agent consults before it acts, a jury-and-judge model for the questions a single pass can’t be trusted to answer, and knowing when the model itself is just too dumb for the job. Live demos and real failures included.

Speaker:
Alex Bauer - (https://Upside.tech)
Alex Bauer is co-founder of Upside, the data layer for GTM engineers. He spent 2016–2024 at Branch as the public voice of mobile attribution and deep-linking. He now builds the clean, normalized GTM data that revenue teams point Claude and Cursor at to answer "what actually happened, and did it work?"
X: https://x.com/alexdbauer
LinkedIn: https://www.linkedin.com/in/alexdbauer/
GitHub: https://github.com/aeromusek
Website: https://alexbauer.net/

## Should AI Engineers Still Read Code in 2026? The Z/L Continuum — Alex Volkov, ThursdAI

- Upload date: 2026-07-10
- Video: https://www.youtube.com/watch?v=ZpK5PWX2YRM
- Transcript: raw/20260710_ZpK5PWX2YRM/ZpK5PWX2YRM.en-orig.vtt
- Metadata: raw/20260710_ZpK5PWX2YRM/ZpK5PWX2YRM.info.json

"How much better do the models have to get before you'll stop reading the code?" Theo asked that question recently and the replies caught fire. Mitchell Hashimoto is calling it agent psychosis. ThePrimeagen's subreddit is in open revolt about people shipping code they never read. Uncle Bob says we have about a year left of looking at code at all.

Alex Volkov saw this argument coming three months ago, and gave it a name.

At AI Engineer Europe, OpenAI's Ryan Lopopolo opened the conference by saying "code is free." His team shipped over 1,000,000 lines with zero human review. Mario Zechner closed the same conference telling everyone to slow the f*** down and read every line. Same stage. Opposite advice. Standing ovations for both.

Alex hosts ThursdAI and spends every week talking to the people building this stuff. In this talk he lays out the Z/L Continuum: what the top AI engineers in the world actually do, not what they say on stage. Including:

• Anthropic's own numbers on Claude writing 80%+ of Claude's code, and what happens when it breaks
• Why human review became the bottleneck nobody wants to talk about
• The uptime chart that looks like a Christmas tree
• Why Dexter Horthy, the "let the agent cook" guy, publicly said "I was wrong"
• The one tweet that changed how Alex thinks about this. You're not Team Z or Team L. Every task gets its own spot on the continuum, and knowing where to place it is the actual skill now.

If you've ever shipped code you didn't read (be honest), this talk is about you.

Speaker info:
- https://x.com/altryne
- https://thursdai.news
- The original Z/L Continuum essay: https://thursdai.news/zl
- Anthropic's "When AI Builds Itself": https://www.anthropic.com/institute/recursive-self-improvement
- Lucas Meijer's tweet: https://x.com/lucasmeijer/status/2044448265194627182

Timestamps:
0:00 - Introduction
0:48 - The shift in AI engineering since December 2025
1:32 - The trend of AI-assisted coding and reduced manual input
3:37 - The core conflict: "Code is free" vs. "Read every line"
6:13 - Defining the Z/L Continuum
8:02 - Analyzing the "code is free" perspective (Ryan Lopopolo/OpenAI)
9:31 - Risks of rapid AI output and incident rates
11:04 - Recursive Self-Improvement (RSI) and human review as a bottleneck
12:08 - The correction: Focusing on tasks, not people
13:56 - Recommended strategy: Routing changes for appropriate verification
15:52 - Emerging capabilities: Fable and Mythos
17:16 - Capability drift and the shift toward "Loops"
18:16 - Understanding "Loops" as the next engineering primitive
20:15 - Future outlook and maintaining flexibility

#AIEngineering #AICoding #CodeReview #VibeCoding #ClaudeCode #AIAgents #ThursdAI

## Understanding is the new bottleneck — Geoffrey Litt, Notion

- Upload date: 2026-07-10
- Video: https://www.youtube.com/watch?v=WkBPX-oDMnA
- Transcript: raw/20260710_WkBPX-oDMnA/WkBPX-oDMnA.en-orig.vtt
- Metadata: raw/20260710_WkBPX-oDMnA/WkBPX-oDMnA.info.json

Autonomous loops are hot, but the reality is that most agentic tasks still require human judgement. And to guide your agents well, it's not enough to just verify correctness -- you actually need to understand the work they're doing.

In this talk, I'll share some techniques for staying in the loop and efficiently developing understanding, combining old ideas from education and cognitive science with modern agent capabilities. You'll walk away with some practical tips for moving faster with agents by understanding more, not less.

## The Golden Age of AI Engineering — Alexander Embiricos & Romain Huet & Peter Steinberger, OpenAI

- Upload date: 2026-07-09
- Video: https://www.youtube.com/watch?v=pMggiOb18tc
- Transcript: raw/20260709_pMggiOb18tc/pMggiOb18tc.en-orig.vtt
- Metadata: raw/20260709_pMggiOb18tc/pMggiOb18tc.info.json

OpenAI's Dev Day 2024 demo ran on an o1 preview model that could not run or check its own code, so Romain Huet had to cross his fingers live on stage. A year later, the same kind of demo ran a full camera and lighting rig, because the model could now test its own work. Alexander Embiricos and Huet use that jump to show how fast Codex is moving: new model releases went from every 15 months to about every 6 weeks.

They walk through why Codex is built on the same responses API, open source harness, and AGENTS md file format that ships to every developer, plus new numbers on cost and speed: frontier level intelligence at $1 per million input tokens and $6 per million output tokens, and a model generating 750 tokens a second, fast enough to produce a real pull request in about 10 seconds.

Speaker info:
- https://twitter.com/embirico
- https://www.linkedin.com/in/embirico

- https://twitter.com/romainhuet
- https://www.linkedin.com/in/romainhuet

- https://twitter.com/steipete
- https://www.linkedin.com/in/steipete

Timestamps:
0:00 - Introduction
0:13 - The World's Fair analogy
1:10 - The role of AI engineers in the future of work
2:14 - Accelerating model development cycles
3:09 - Evolution of build-and-test model loops
4:03 - Scaling engineering capabilities through agents
5:30 - Defining the desired AI engineering product experience
7:59 - The design philosophy of the Codex app
9:44 - The open-source stack and building with API primitives
11:43 - Expanding the ecosystem with Apps Server and plugins
14:20 - Optimizing for "Value Maxing": Cost and Intelligence
15:48 - Achieving high-speed inference for real-time workflows
16:51 - Future outlook: Removing the local/cloud distinction
18:16 - Special guest introduction: Peter Steinberger
18:56 - Shifting from manual orchestration to managing agents
20:02 - Three key changes for scalable agent loops
21:19 - Redefining the bottleneck as human attention
22:08 - Workflow example: Automating open-source issue resolution

## Everything we knew about software has changed — Theo Browne, @t3dotgg ​

- Upload date: 2026-07-08
- Video: https://www.youtube.com/watch?v=xUnRQ9vLXxo
- Transcript: raw/20260708_xUnRQ9vLXxo/xUnRQ9vLXxo.en-orig.vtt
- Metadata: raw/20260708_xUnRQ9vLXxo/xUnRQ9vLXxo.info.json

For the closing keynote of AIEWF2026, Theo provokes you to think wider, not just bigger.

In this keynote from the AI Engineer World's Fair, developer and YouTuber Theo Browne (@t3dotgg) argues that the rapid evolution of AI models—moving from tool-calling (Sonnet 3.5) to long-running task execution (Opus 4.5) and now orchestration (Mythos)—requires software engineers to fundamentally change how they build products.

Key Themes:
Rejecting Skeuomorphism: Browne compares the current state of software development to the design shift in iOS 7, urging developers to move away from legacy mental models and tools (like Git or terminal-centric workflows) that prioritize familiarity over actual utility (6:08 - 8:32).
The New Tier System: Traditional categorizations of "side project," "startup," and "too big" have shifted. He highlights that tasks once requiring a dedicated startup can now be managed by simple automated systems, such as a Markdown file running on a cron job (10:33 - 12:20).
Thinking Bigger: Rather than just building depth in a narrow feature set, Browne encourages builders to cover a wider spectrum of product functionality. Because AI agents can now handle significant parts of implementation, it is becoming viable for smaller teams to build products that compete with industry giants like AWS or Salesforce by architecting them for extensibility (13:12 - 15:30).

Takeaway: The barrier to entry for building complex, wide-reaching platforms has collapsed. Engineers should stop limiting themselves by legacy constraints and start building much more ambitious projects.

Timestamps
0:00 – Introduction and the "AI psychosis" experience
0:50 – Evolution of AI models: Sonnet 3.5, Opus 4.5, and Mythos
3:04 – The imperative to "go bigger" and push model capabilities
3:35 – Overcoming legacy constraints and developer habits
6:08 – Moving past our "skeuomorphic" phase in software development
9:30 – Personal project evolution: side projects, startups, and the "Markdown tier"
12:22 – Identifying the gap: What is "too big" anymore?
13:06 – Redefining the strategy: Building for a wider spectrum instead of just depth
14:50 – Scaling and architecting products to allow for user-driven extensibility

## Your agent is blindfolded — Johan Lajili, Poolside AI

- Upload date: 2026-07-08
- Video: https://www.youtube.com/watch?v=iRcX54EO5g8
- Transcript: raw/20260708_iRcX54EO5g8/iRcX54EO5g8.en-orig.vtt
- Metadata: raw/20260708_iRcX54EO5g8/iRcX54EO5g8.info.json

Your agent is blindfolded. How giving it (good) eyes multiplies performance and trust!

## Think You Can Build a Game with AI? Think Again! - Danielle An & David Hoe, Meta

- Upload date: 2026-07-08
- Video: https://www.youtube.com/watch?v=grdoOC1BT1s
- Transcript: raw/20260708_grdoOC1BT1s/grdoOC1BT1s.en-orig.vtt
- Metadata: raw/20260708_grdoOC1BT1s/grdoOC1BT1s.info.json

With the recent development of AI, either you or your friend probably vibe coded a game using Gemini, on Three.js. But that is old news now. If everyone can do that, what is next? The next massive hit, the one that millions of people across the world will play, is just about to be born. Wanna know more? Come see this talk!

## Your coding agent doesn't always follow your rules — Talha Sheikh, Checkout.com

- Upload date: 2026-07-08
- Video: https://www.youtube.com/watch?v=MpZzWMdmQCE
- Transcript: raw/20260708_MpZzWMdmQCE/MpZzWMdmQCE.en-orig.vtt
- Metadata: raw/20260708_MpZzWMdmQCE/MpZzWMdmQCE.info.json

Your coding agent doesn't always follow your rules. An agent harness makes sure it does, in real-time, every time.

## Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data - Sachin Kumar, LexisNexis

- Upload date: 2026-07-08
- Video: https://www.youtube.com/watch?v=IQkVMvXQKLY
- Transcript: raw/20260708_IQkVMvXQKLY/IQkVMvXQKLY.en-orig.vtt
- Metadata: raw/20260708_IQkVMvXQKLY/IQkVMvXQKLY.info.json

You fine-tune LLMs and ship them. Your evals are green, your behavioral monitors are green — and a sleeper-agent backdoor can still flip the model to harmful output on a trigger you never tested. Behavioral testing can't reach it, and the interpretability tool people reach for — joint cross-model features (crosscoders) — dilutes the signal until it sits at the noise floor.

The fix is in what the training data changed. A backdoor is a directional shift that fine-tuning writes into the model's activations, so you isolate it by watching the difference between the base and fine-tuned model. In a controlled SQL-injection backdoor, a sparse autoencoder trained on that difference flags it with 40× the signal of joint features, perfect precision, and zero false positives — from a single cheap layer. You'll leave knowing how to wire a "delta monitor" into your fine-tuning pipeline as a quiet CI gate. Based on my peer-reviewed paper accepted at IJCNN.

Speakers:
- Sachin Kumar (LexisNexis): Sachin Kumar is a Senior Data Scientist III and Tech Lead at LexisNexis, building agentic AI for the legal domain. His independent AI-safety and interpretability research has been accepted at top-tier venues including ACL, AAAI, and IJCNN.
  LinkedIn: https://www.linkedin.com/in/techsachinkumar/
  GitHub: https://github.com/techsachinkr

## Building an ACP-Compatible Agent Live — Bennet Fenner, Zed

- Upload date: 2026-07-08
- Video: https://www.youtube.com/watch?v=HsxQICTLF84
- Transcript: raw/20260708_HsxQICTLF84/HsxQICTLF84.en-orig.vtt
- Metadata: raw/20260708_HsxQICTLF84/HsxQICTLF84.info.json

In this session, we'll be building a coding agent that implements ACP — covering protocol design, session lifecycle management, and handling tool calls. The session ends with a live demo of the finished agent running inside Zed, showing what ACP looks like in practice from both sides of the protocol.

## Teaching Coding Agents to do Spreadsheets - Nuno Campos, Witan Labs

- Upload date: 2026-07-08
- Video: https://www.youtube.com/watch?v=HEFSExa0xl0
- Transcript: raw/20260708_HEFSExa0xl0/HEFSExa0xl0.en-orig.vtt
- Metadata: raw/20260708_HEFSExa0xl0/HEFSExa0xl0.info.json

https://github.com/witanlabs/research-log

## Running a Chess YouTube Channel entirely by AI — Stephan Steinfurt, TNG

- Upload date: 2026-07-08
- Video: https://www.youtube.com/watch?v=BqZrTdgBaPw
- Transcript: raw/20260708_BqZrTdgBaPw/BqZrTdgBaPw.en-orig.vtt
- Metadata: raw/20260708_BqZrTdgBaPw/BqZrTdgBaPw.info.json

Daily chess puzzle explanations on YouTube: Our agent analyzes and describes chess puzzles in an accessible way - arrows included!

## I Run a Fleet of AI Agents Across Three Machines. Here's What Broke. - Kyle Jaejun Lee, KRAFTON

- Upload date: 2026-07-08
- Video: https://www.youtube.com/watch?v=4kYl2_mqmnQ
- Transcript: raw/20260708_4kYl2_mqmnQ/4kYl2_mqmnQ.en-orig.vtt
- Metadata: raw/20260708_4kYl2_mqmnQ/4kYl2_mqmnQ.info.json

An honest field report from my own personal fleet of AI agents, run across several machines as a daily driver. Less about any single tool, more about the journey: how things that work on one machine break once you scale to many, what it takes to keep a setup like this running, and where it's all converging. Not a company platform — just real, evolving lessons from running it myself.

Speakers:
- Kyle Jaejun Lee (KRAFTON): Kyle is a builder and AI Platform Engineer working to make AI agents first-class citizens in the workplace
  X/Twitter: https://x.com/kyleleee_119
  LinkedIn: https://www.linkedin.com/in/jjlee-swe/
  GitHub: https://github.com/cooco119

## Beyond the Harness: A Journey Towards Adaptative Engineering - Rajiv Chandegra, Annicha Labs

- Upload date: 2026-07-07
- Video: https://www.youtube.com/watch?v=qdZzND79mcg
- Transcript: raw/20260707_qdZzND79mcg/qdZzND79mcg.en-orig.vtt
- Metadata: raw/20260707_qdZzND79mcg/qdZzND79mcg.info.json

Building products has been commoditised. As AI models grow more capable, the real opportunity shifts to the hard problems — the big, messy, tangled challenges of the physical and social world. That, after all, is the engineer's true job: to solve problems.

But our current paradigm leans on fixed harnesses - predetermined structures imposed on the problem. In a world of complex, shifting systems, that rigidity becomes a liability. We need harnesses that adapt in real time, the way a great leader reads and responds to a changing team. This is adaptive engineering, and it is where the next frontier lies.
This talk traces the limits of today's engineering paradigm, draws on complexity science to examine how complex systems behave in the natural and social world, and explores the philosophy and practice of adaptive engineering as what comes next.

Speakers:
- Rajiv Chandegra (Annicha Labs): Rajiv is a practicing medical doctor and director of Annicha Labs - a firm dedicated to exploring the application of technology for complex challenges in the real world.
  X/Twitter: @rajivchandegra
  LinkedIn: https://www.linkedin.com/in/rajivchandegra/

## The Pipeline Is Dead - Iris ten Teije, Sky Valley Ambient Computing

- Upload date: 2026-07-07
- Video: https://www.youtube.com/watch?v=bRnoEpoK5m4
- Transcript: raw/20260707_bRnoEpoK5m4/bRnoEpoK5m4.en-orig.vtt
- Metadata: raw/20260707_bRnoEpoK5m4/bRnoEpoK5m4.info.json

The entire software distribution stack assumes one version of your software, the same for everyone. It was the only thing we could afford when producing a change was expensive. Now it's nearly free, and it can happen at runtime, on the client, in the user's session, so the line between distribution and development is dissolving. This talk is about the infrastructure that has to catch up: where truth lives when every user runs a different version, how you debug a program that exists for one person, and why a million per-user versions can be more contained than the single tangled codebase you run today. Real architectural decisions, the tradeoffs that don't have clean answers yet, and what we're learning at the frontier.

Speakers:
- Iris ten Teije (Sky Valley Ambient Computing): Iris ten Teije is a serial entrepreneur currently building Differ: infrastructure for adaptive software.
  X/Twitter: x.com/iristenteije
  LinkedIn: http://linkedin.com/in/iristenteije

## 500 people vibe-coded for 30 days. I was one of them. - Sanja Grbic, Automattic

- Upload date: 2026-07-07
- Video: https://www.youtube.com/watch?v=UcYoMg-8-L8
- Transcript: raw/20260707_UcYoMg-8-L8/UcYoMg-8-L8.en-orig.vtt
- Metadata: raw/20260707_UcYoMg-8-L8/UcYoMg-8-L8.info.json

Automattic, the company behind WordPress.com, ran a 30-day experiment called Radical Speed Month: pause the roadmap, and see how fast real software could ship. I am a product Designer and I shipped three products that month. I'll share what each one revealed about a new kind of collaboration between designers and engineers and how teams are unlocked when bottlenecks disappear.

Speakers:
- Sanja Grbic (Automattic): Sanja is a product designer based in San Francisco, with over a decade of experience, focused on turning complex technology into simple, inspiring solutions.
  X/Twitter: https://x.com/_dream_stellar
  LinkedIn: https://www.linkedin.com/in/sanjagrbic/

## SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale - Rishi Desai, Abundant AI

- Upload date: 2026-07-07
- Video: https://www.youtube.com/watch?v=Rx8f05JI_WA
- Transcript: raw/20260707_Rx8f05JI_WA/Rx8f05JI_WA.en-orig.vtt
- Metadata: raw/20260707_Rx8f05JI_WA/Rx8f05JI_WA.info.json

SWE-Marathon is a benchmark for long-horizon autonomous software work: 20 project-scale tasks spanning product clones, library rewrites, and ML engineering. We discuss what happens when coding agents run for tens to hundreds of millions of tokens, why full-stack evals need computer-use verifiers, and why reward-hacking resistance is now central to benchmark design.

Speakers:
- Rishi Desai (Abundant AI): Rishi Desai is an ML Engineer at Abundant AI, where he works on RL environments and SWE benchmarks for coding agents.
  X/Twitter: https://x.com/rishi_desai2
  LinkedIn: https://www.linkedin.com/in/rishi-desai1/
  GitHub: https://github.com/RishiDesai

## GTM Is You - Victoria Melnikova, Evil Martians

- Upload date: 2026-07-07
- Video: https://www.youtube.com/watch?v=G6IlDzj8OjA
- Transcript: raw/20260707_G6IlDzj8OjA/G6IlDzj8OjA.en-orig.vtt
- Metadata: raw/20260707_G6IlDzj8OjA/G6IlDzj8OjA.info.json

In this talk, Victoria Melnikova revisits interviews with successful developer tool founders (Sam Lambert, David Cramer, Paul Copplestone, Ivan Burazin, Zeno Rocha, Jason Bosco) in San Francisco to derive optimal Go-To-Market tactics for developer tools and AI startups focusing on personal brand.

Speakers:
- Victoria Melnikova (Evil Martians): Victoria run new business at Evil Martians and hosts Dev Propulsion Labs podcast
  X/Twitter: https://x.com/vmelnikova_en
  LinkedIn: https://www.linkedin.com/in/vmelnikova/
  GitHub: https://github.com/vicamelnikova

## Respect The Process - Andrew Dumit, Watershed Technology Inc.

- Upload date: 2026-07-07
- Video: https://www.youtube.com/watch?v=CLttOU7n6sI
- Transcript: raw/20260707_CLttOU7n6sI/CLttOU7n6sI.en-orig.vtt
- Metadata: raw/20260707_CLttOU7n6sI/CLttOU7n6sI.info.json

In sustainability, the answer to almost every question is "it depends." What’s the right classification? Which method should the agent use? Our vertical is filled with judgement calls broadly and one of the tasks in that vertical might span a search over 100k’s of data-rich nodes and hundreds of edits. Editing across them takes loops and filters, not enumerated tool calls. Code is the only thing that scales to the task. But in a domain that relies heavily on judgement and implicit knowledge, there are many ways for a model to get the right answer with the wrong reasoning and many right answers for it to come to.

Over time, we’ve upgraded models, but a smarter model didn’t fix this. Instead we built a domain-specific coding harness, applying best practices from general coding agents (linting, routing failures back, sub-tasking), and constraining how it commits through a well-defined SDK and owning the final execution. It keeps the full power of a modern coding agent, but every change must pass through our deterministic, typed interface.

Within that constraint, we harness-engineered our way from 43% to 92% accuracy. The interesting part is the other 8%: even when the agent lands on a different answer than our reference, every change it makes is still valid, traceable, and replayable. We'll cover how we built it, what we chose to constrain vs. what we leave free.

Speakers:
- Andrew Dumit (Watershed Technology Inc.): Andrew works on AI engineering at Watershed, building systems to manage and reduce the emissions of everything companies buy and sell.
  LinkedIn: https://www.linkedin.com/in/adumit
  GitHub: https://github.com/adumit

## Build AI Systems for Discernment, Not Approval - Angel Ortmann Lee, Duolingo

- Upload date: 2026-07-07
- Video: https://www.youtube.com/watch?v=CDqzWpwkSls
- Transcript: raw/20260707_CDqzWpwkSls/CDqzWpwkSls.en-orig.vtt
- Metadata: raw/20260707_CDqzWpwkSls/CDqzWpwkSls.info.json

The human-in-the-loop paradigm promises automation's efficiency without sacrificing safety or nuance. But it hides an underexamined assumption: that human involvement produces genuine discernment, not just a rubber stamp. In practice, human-AI interaction often occurs in environments where throughput or business incentives crowd out critical thinking. This talk examines why human oversight so often falls short in practice, and how deliberate interaction design can close the gap.

We've grown comfortable delegating reasoning to machines. We follow GPS down unfamiliar streets and accept AI coding suggestions with minimal inspection. When Shaw & Nave (Wharton, 2026) studied human-AI interaction, they found people accepted AI answers over 80% of the time, even when it was wrong. They call this cognitive surrender: when humans forgo deliberation and adopt AI output with minimal scrutiny.

At the Duolingo English Test, a controlled experiment revealed that experienced proctors shown fabricated AI cheating alerts confirmed cheating at near-chance rates. But coin-flip accuracy is unacceptable when college admissions and visas are on the line. 

The model wasn't the problem, the signals were fake. But skilled reviewers were still showing systematic confirmation bias. A single change to decision framing improved accurate rejections by 21%.

The fix isn't better models or more human oversight. It's engineering the interaction itself. What reasoning patterns do you need from the human, and how does the interface elicit them? This talk covers practical design principles for building AI systems that improve human judgment, produce more reliable review behavior, and generate higher-quality training data. Every AI system trains its users, the question is whether you're doing it deliberately.

Speakers:
- Angel Ortmann Lee (Duolingo): Angel is a Software Engineer at Duolingo, building AI security systems for the Duolingo English Test to help ensure online testing is secure, trustworthy, and accessible for learners around the world.
  LinkedIn: https://www.linkedin.com/in/angel-ortmann-lee-7494b9201

## What if the harness mattered more than the model? - Aditya Bhargava, Etsy

- Upload date: 2026-07-07
- Video: https://www.youtube.com/watch?v=2e9ANoOEn28
- Transcript: raw/20260707_2e9ANoOEn28/2e9ANoOEn28.en-orig.vtt
- Metadata: raw/20260707_2e9ANoOEn28/2e9ANoOEn28.info.json

The models are getting so good now that all you need is a simple harness, some tools, and a loop... right? Aditya Bhargava argues that this direction promotes overreliance on large, proprietary models, and we should be focusing on building harnesses that improve the performance of models that can be run locally.

Speakers:
- Aditya Bhargava (Etsy): Aditya Bhargava is a Staff Engineer and IC Initiative Lead of Agentic Commerce at Etsy.
  GitHub: http://github.com/egonSchiele

## How we taught agents to use good retrieval - Hanna Lichtenberg, Mixedbread AI

- Upload date: 2026-07-07
- Video: https://www.youtube.com/watch?v=1IdzkRVmWAA
- Transcript: raw/20260707_1IdzkRVmWAA/1IdzkRVmWAA.en-orig.vtt
- Metadata: raw/20260707_1IdzkRVmWAA/1IdzkRVmWAA.info.json

RAG is dead. Again. Vector search is useless. All you need is BM25. Not even BM25, all you need is grep. Or maybe even just cat+ls. If you care at all about agents, you probably read a variation of this as part of your daily routine. In a way, isn't it true that semantic search is full of failure cases?
And yet, in all sorts of knowledge tasks, whether it be Deep Research, financial analysis or legal research, grep does not seem to cut it. The Oracle Gap, the performance difference between perfect retrieval and grep-based retrieval, is well into the double digits percents.
In practice, this means that your agent fails to surface that one hidden clause in that 187 pages contract. Or it doesn't properly notice that Q4 results were amended. In the end, this means that a human has to re-do all of its work, erasing all benefits. But if keyword search does not work, and semantic search is dead, then what is the way out?
We argue that the reason for the impressive performance on simple, lexical search methods is simply because models were never taught to use better tools. When using weak tools, they run into the limits of these tools. When provided with better search, they write queries for the weak tools they know, and semantic search fails as a result.
Join us for this session to hear about how we are addressing this problem, co-designing agents with state-of-the-art retrieval tools to teach them that they have more than one tool in their best.

Speakers:
- Hanna Lichtenberg (Mixedbread AI): Hanna is an AI Engineer at Mixedbread, working on agentic retrieval research and agent infrastructure.
  X/Twitter: https://x.com/hannaLicht
  LinkedIn: https://www.linkedin.com/in/hanna-lichtenberg-64778b221/
  GitHub: https://github.com/HannaLicht

## Field Guide to Fable — Thariq Shihipar, Anthropic

- Upload date: 2026-07-06
- Video: https://www.youtube.com/watch?v=9fubhllmsBU
- Transcript: raw/20260706_9fubhllmsBU/9fubhllmsBU.en-orig.vtt
- Metadata: raw/20260706_9fubhllmsBU/9fubhllmsBU.info.json

Ask a chat model which Pokemon names end in aw and it fails, even though it knows every Pokemon by heart. Ask Claude Code and it writes a script, fetches the list, and filters for the answer in seconds. Thariq Shihipar, who works on Claude Code at Anthropic, calls that gap capability overhang: models get smarter in spiky ways, and the tools you give them decide which spikes you can reach.

Thariq covers what it takes to work with Fable, Anthropic's newest model. Claude Code cut 80 percent of its system prompt, since heavy instructions now constrain a model more imaginative than the examples it's given. The ask user question tool went from barely working under Opus 4 to generating embedded HTML questionnaires under Fable. He built a full keynote deck in four hours with it, and argues teams should stop picking two of good, fast, and cheap and start demanding all three.


Speaker info:
- https://x.com/trq212/

Timestamps:
0:00 Introduction and setting the stage for Fable
2:32 Unhobbling Claude: Understanding model behavior
9:08 Finding your unknowns: Navigating the gap between map and territory
14:29 Reflecting on the emotional shift in coding productivity
16:30 Being unreasonable: Demanding good, fast, and cheap results

## MCP Apps: Primitives, discovery, and the Future of Software - Pietro Zullo, Manufact, Inc

- Upload date: 2026-07-05
- Video: https://www.youtube.com/watch?v=sAOBXCDiDOs
- Transcript: raw/20260705_sAOBXCDiDOs/sAOBXCDiDOs.en-orig.vtt
- Metadata: raw/20260705_sAOBXCDiDOs/sAOBXCDiDOs.info.json

Everyone in this room knows what MCP is, but I am sure not many people know what MCP Apps are, how they work, how to build them and distribute them. By the end of this talk you'll know everything you need to join the race!

MCP Apps are not just MCP servers with a UI bolted on. They're a full interaction layer: bidirectional, stateful, rendered by the host, with the model and the UI sharing live context.

This talk is structured around

**What MCP Apps actually are.** The architecture: how an App is declared via `ui://` resources, how the host renders it in a sandboxed iframe, how the JSON-RPC-over-postMessage transport works, and how state flows between the model and the UI.

**The primitives that make them real.** `ui/update-model-context`, the App pushing live state into the model's context window without a user message. `ui/message`, the App talking back into the conversation unprompted. App Tools, the model calling into the App's registered tool surface.

**A showcase of MCP Apps shipping today.** Concrete demos, not slides about what's possible. What early builders have figured out, what's hard, and what the interaction patterns look like in practice.

**Distribution and discovery.** How the stores work, how to submit, what the surface looks like across hosts, and what the install/discovery UX actually means for builders.

**Why companies will need to move** Any product that is used by humans through a UI will need an MCP App version, or it gets bypassed by all the people that are getting more and more used to do everything through agents.

As long as there are people using these systems, MCP Apps is the answer. For the rest, there is MCP.

Speakers:
- Pietro Zullo (Manufact, Inc): Pietro is the co-founder of Manufact (YC S25). Manufact created and maintains mcp-use, an MCP framework with more than 8M downloads across PyPI and npm, one of the leading MCP development frameworks today. Manufact is the cloud for MCP. You can think of Manufact / mcp-use as Vercel / Next.js, but vertical on MCP Apps and servers.
  X/Twitter: https://x.com/pietrozullo
  LinkedIn: https://www.linkedin.com/in/pietrozullo/
  GitHub: https://github.com/pietrozullo

## The Missing Layer After Launch - Raphael Kalandadze, Wandero AI

- Upload date: 2026-07-05
- Video: https://www.youtube.com/watch?v=kZsf_Sfm7RU
- Transcript: raw/20260705_kZsf_Sfm7RU/kZsf_Sfm7RU.en-orig.vtt
- Metadata: raw/20260705_kZsf_Sfm7RU/kZsf_Sfm7RU.info.json

We run a production system of agents for real customers. The team that keeps it healthy is also made of agents.

Operating an agent product isn't like operating software. When our agent fails a customer — a dropped constraint, a stale price, a confident wrong answer — nothing crashes and no log lights up. The failure is in the conversation, not the stack trace. So we put agents on the operations:

- One monitors production conversations and judges where the agent actually let a customer down — across thousands of live sessions, not a sampled few.
- One watches logs and system health and traces real problems back into the code.
- One writes and runs tests, because "green CI" means nothing for a non-deterministic agent.
- One reviews every PR — human or agent-authored — against a single question: root cause, or just the symptom?

Humans stay at the merge and approval boundaries. The agents do the watching, judging, testing, and drafting that no human team could keep up with at this volume.

This talk is the honest version: what each operating agent actually checks, where we trust it and where we don't, what breaks, and why operating an agent system is becoming its own engineering discipline — done, increasingly, by agents.

Speakers:
- Raphael Kalandadze (Wandero AI): Co-founder and CTO of Wandero AI, an agent-native operating system for travel and hospitality, and co-founder of Tbilisi AI Lab, where we build the first Georgian large language model.
  X/Twitter: @RaphaelKalan
  LinkedIn: https://www.linkedin.com/in/rapael-kalandadze/
  GitHub: https://github.com/RRaphaellRaphaelKalan

## Your AI Product Will Fail Unless You Can Explain It - Veronica Hylak, Hey AI

- Upload date: 2026-07-05
- Video: https://www.youtube.com/watch?v=d_Ftrl3vfV0
- Transcript: raw/20260705_d_Ftrl3vfV0/d_Ftrl3vfV0.en-orig.vtt
- Metadata: raw/20260705_d_Ftrl3vfV0/d_Ftrl3vfV0.info.json

You’re shipping faster than ever, but still can’t quickly answer: "Why does this matter to an average user?"

A decade ago, the market would find you. Now, if people can't instantly understand what your AI product does, you’re in trouble.

That communication gap has become fatal. This talk? Your emergency hotline.

With 7M views helping complex AI systems make sense to everyday people, and direct work with YC startups, AI tools, and safety organizations across SF, Veronica Hylak shares how technical founders can turn products into stories people instantly understand, remember, and want to buy.

You’re shipping faster than ever, but still can’t quickly answer: "Why does this matter to an average user?"

A decade ago, the market would find you. Now, if people can't instantly understand what your AI product does, you’re in trouble.

That communication gap has become fatal. This talk? Your emergency hotline.

With 8M views helping complex AI systems make sense to everyday people, and direct work with YC startups, AI tools, and safety organizations across SF, Veronica Hylak shares how technical founders can turn products into stories people instantly understand, remember, and want to buy.

Speakers:
- Veronica Hylak (Hey AI): Veronica Hylak is an AI product leader with 10 years in tech (including six in AI beginning with autonomous military ships), and a YouTuber whose explainers have reached over 8 million people.
  LinkedIn: https://www.linkedin.com/in/veronica-hylak-8b629a86/

## Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI

- Upload date: 2026-07-05
- Video: https://www.youtube.com/watch?v=2IxD9OB3XuQ
- Transcript: raw/20260705_2IxD9OB3XuQ/2IxD9OB3XuQ.en-orig.vtt
- Metadata: raw/20260705_2IxD9OB3XuQ/2IxD9OB3XuQ.info.json

Agents fail in production in ways that static benchmarks cannot fully capture. The key question is whether they can learn from those experiences without drifting or breaking prior capabilities.

This talk introduces verifiable continual learning for AI agents: a framework for converting traces, failures, and feedback into testable, regression-aware improvements. I will discuss four core requirements: turning failures into replayable learning environments, preserving prior capabilities during updates, routing repairs to the right layer of the agent stack, and keeping the learning loop efficient enough to run continuously.

We will use these principles to examine today’s approaches, including prompt optimizers, memory consolidation, coding-agent harness repair, and trace-to-harness systems. I will then discuss the remaining gap: a holistic, lifelong, verifiable learning loop with online regression control.

Speakers:
- Soheil Feizi (RELAI): Dr. Soheil Feizi is the Founder and CSO of RELAI and an Associate Professor of Computer Science at the University of Maryland, College Park, whose work focuses on the reliability, safety, and optimization of AI systems.
  X/Twitter: https://x.com/FeiziSoheil
  LinkedIn: https://www.linkedin.com/in/soheil-feizi-b14a4895/

## The Prompt Is Still a Punch Card - Ted Johnson, JoinIn AI

- Upload date: 2026-07-02
- Video: https://www.youtube.com/watch?v=hVJOnuhFmTA
- Transcript: raw/20260702_hVJOnuhFmTA/hVJOnuhFmTA.en-orig.vtt
- Metadata: raw/20260702_hVJOnuhFmTA/hVJOnuhFmTA.info.json

Interfaces outlive their constraints. The keyboard, command line, mouse, menus, forms, voice assistants, and even prompts were all brilliant compromises with the machines of their time.

But AI gives us a chance to renegotiate that bargain.

This talk reframes AI as an interface technology, not only an intelligence technology. We will trace a pattern across computing history: humans repeatedly learn the machine’s protocol, from punching cards to writing commands to engineering prompts. Then we will ask what changes when computers can reason, listen, speak, infer, clarify, and adapt.

The next frontier is not just better models or better voices. It is more human-compatible interfaces: systems that understand timing, attention, interruption, ambiguity, repair, shared context, and when to stay silent.

Speakers:
- Ted Johnson (JoinIn AI): Ted Johnson is an executive, enterprise architect, and co-founder of JoinIn.AI, focused on AI-powered collaboration, enterprise architecture, cloud strategy, and technology transformation.
  LinkedIn: https://linkedin.com/in/johnsontedm
  GitHub: https://github.com/JoinIn-AI/

## The Future Is Domain-Specific Agents - Justin Schroeder, StandardAgents

- Upload date: 2026-06-29
- Video: https://www.youtube.com/watch?v=spNAUEgq_A8
- Transcript: raw/20260629_spNAUEgq_A8/spNAUEgq_A8.en-orig.vtt
- Metadata: raw/20260629_spNAUEgq_A8/spNAUEgq_A8.info.json

“Composition over inheritance” has always been a good engineering rule. It may also be the unlock for useful AI. A Gmail agent is fundamentally more powerful than a Gmail skill — and when composed with Sheets, Notion, and GitHub agents, the system gets more capable, more reliable, and cheaper to run. Suddenly, smaller models can do real work, and AI can move from internal copilots to customer-facing products. In this talk, we’ll unpack why this architecture hasn’t become the default yet, what’s been missing, and how to start building toward it today.

Speakers:
- Justin Schroeder (StandardAgents): Co-founder of StandardAgents. Compulsive open source builder. Creator of dmux, ArrowJS, FormKit, AutoAnimate, Tempo, zodown
  X/Twitter: https://x.com/jpschroeder
  LinkedIn: https://www.linkedin.com/in/jpschroeder/
  GitHub: https://github.com/justin-schroeder

## The Agentic AI Engineer - Benedikt Sanftl, Mutagent

- Upload date: 2026-06-29
- Video: https://www.youtube.com/watch?v=pSto5YaNGUo
- Transcript: raw/20260629_pSto5YaNGUo/pSto5YaNGUo.en-orig.vtt
- Metadata: raw/20260629_pSto5YaNGUo/pSto5YaNGUo.info.json

In this video we introduce the concept of the agentic ai engineer. similar to coding agent loops for agents we build a system that build AI Agents in an Eval-Driven Developement Loop. The Agentic AI Enginner is a collection of a multi-agent team, steared by an orchestrator and combines, spec, build, evaluate, diagnose, monitor, optimse. We round up the talk with a live demo from one of our agents in research preview.

Speakers:
- Benedikt Sanftl (Mutagent): Bene is the CEO and Co-Founder of Mutagent. The platform for Agentic AI Engineering.
  LinkedIn: https://www.linkedin.com/in/benedikt-sanftl-294a6039a/

## Frontier results, on device - RL Nabors, Arize

- Upload date: 2026-06-29
- Video: https://www.youtube.com/watch?v=fWXJM-J0ZB8
- Transcript: raw/20260629_fWXJM-J0ZB8/fWXJM-J0ZB8.en-orig.vtt
- Metadata: raw/20260629_fWXJM-J0ZB8/fWXJM-J0ZB8.info.json

Most of use reach for a frontier model by default and pay for it on every call, in latency, in energy, in cash, and in everything that leaves their stack. For most of those calls, a small local model would do the job. 

RL Nabors, former Meta/React core team member and AWS alum, covers the vocabulary you need to reason about model performance (capability evals, golden datasets, LLM-as-judge) and walks through real cases: a local agentic harness replacing a frontier call, an in-browser moderation classifier defended with production-trace evals, and a generative summarization feature where the rubric turns out to be harder than the model. You'll leave with a framework for deciding when to choose large and off-prem or small and local models, and how to measure your way to the answer instead of guessing.

You will learn:

- The vocabulary to reason about model performance (capability evals, golden datasets, LLM-as-judge).
- A framework for deciding when a small or local model can replace a frontier one and when it can't.
- A repeatable process for building capability evals from your own production traces, not someone else's benchmark.
- Working examples of using eval results to iterate on prompts and ship with confidence instead of vibes.

Speakers:
- RL Nabors (Arize): RL Nabors builds developer tools and the communities that make them stick. Previously React and MDN, currently developer experience at Arize, perpetually building Mima.
  X/Twitter: https://x.com/rachelnabors
  LinkedIn: https://linkedin.com/in/nearestnabors
  GitHub: https://linkedin.com/in/nearestnabors

## Building Great Agent Skills: The Missing Manual

- Upload date: 2026-06-29
- Video: https://www.youtube.com/watch?v=UNzCG3lw6O0
- Transcript: raw/20260629_UNzCG3lw6O0/UNzCG3lw6O0.en-orig.vtt
- Metadata: raw/20260629_UNzCG3lw6O0/UNzCG3lw6O0.info.json

Let's discuss how to navigate "skill hell" by providing a structured framework for building high-quality agent skills. Without a shared rubric, developers and organizations struggle to create effective, maintainable skills for AI agents.

Timestamps:

0:00 - Introduction to the talk and the concept of "skill hell"
2:12 - Overview of the skill checklist framework
3:16 - Trigger: Choosing between user-invoked and model-invoked skills
7:29 - Structure: Organizing steps and references
9:00 - Making the skill.md file minimal
11:54 - Steering: Using leading words to guide agent behavior
14:56 - Increasing "leg work" per step
16:48 - Pruning: Removing sediment, crud, and no-ops
19:06 - Final summary of the checklist framework
19:55 - Where to find the "writing great skills" resource

The Skill Checklist Framework:

Trigger (3:16 - 7:25): Decide whether a skill should be user-invoked or model-invoked. Matt notes that while model-invoked skills offer more flexibility, they increase context load and introduce unpredictability. User-invoked skills offer more control but require greater cognitive load from the pilot.

Structure (7:29 - 11:53): Organize your skill into two primary units: steps (procedures) and reference (supporting information). To keep the skill.md file minimal, move branching reference material behind context pointers to reduce bloat and maintenance costs.

Steering (11:54 - 16:47): Use leading words—specific terms that pack dense meaning—to influence agent behavior and guide reasoning traces. Additionally, you can force the agent to perform more "leg work" on specific tasks by breaking complex processes into smaller, individual skills that hide future steps.

Pruning (16:48 - 19:05): Maintain a clean skill set by ensuring a single source of truth, removing "sediment" (irrelevant legacy material), and eliminating "no-ops" (instructions that don't actually change agent behavior).

https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-great-skills/SKILL.md

## Using RL Agent to Detect and Remediate ETL Pipeline Failures - Anna Marie Benzon

- Upload date: 2026-06-29
- Video: https://www.youtube.com/watch?v=LrGCT7G_rU8
- Transcript: No transcript file found
- Metadata: raw/20260629_LrGCT7G_rU8/LrGCT7G_rU8.info.json

Cloud ETL failures often require engineers to manually inspect logs, diagnose schema or data-quality issues, select a repair, rerun the job, and validate recovery. This talk presents an RL-guided pipeline health agent that automates this workflow through deterministic anomaly detection, interpretable Q-learning, bounded remediation actions, and an external safety layer.
The system detects schema drift, null-rate spikes, type changes, and runtime failures, then selects actions such as retry, schema coercion, rollback, quarantine, or escalation. Evaluation across 30 controlled synthetic runs demonstrates minutes-scale recovery for successfully resolved cases while highlighting the importance of deterministic rules and safety guardrails.

Speakers:
- Anna Marie Benzon: Anna Marie Benzon is a World Economic Forum–recognized technology leader, startup founder, and PhD researcher in AI with 9+ years of experience building AI-powered products and scaling multidisciplinary teams.
  LinkedIn: https://www.linkedin.com/in/anna-marie-benzon
  GitHub: https://github.com/ambenzon27

## Your Agent Failed in Prod. Good Luck Reproducing It. - Tisha Chawla & Susheem Koul, Microsoft

- Upload date: 2026-06-29
- Video: https://www.youtube.com/watch?v=Lc8zRh9muoY
- Transcript: raw/20260629_Lc8zRh9muoY/Lc8zRh9muoY.en-orig.vtt
- Metadata: raw/20260629_Lc8zRh9muoY/Lc8zRh9muoY.info.json

When an autonomous agent fails in production and corrupts an enterprise data record, it rarely repeats the exact same execution trajectory twice. Standard application logs reveal what broke but completely fail to explain why, leaving platform teams unable to reproduce non-deterministic failures on demand. While durable execution engines excel at keeping an agent loop alive through state recovery, durability is fundamentally distinct from debuggability. State recovery reconstructs the present; it does not allow an engineer to re-enter the precise historical run that caused an erratic state mutation.

This session introduces the record and replay pattern for autonomous workflows, bringing the core engineering philosophy behind low level systems tools like Mozilla rr straight into the agent loop. By capturing every model invocation, tool execution payload, memory boundary read, and intermediate state transition into an append only event log, engineers can deterministically replay a failed execution trace for true postmortem root cause analysis. This architectural pattern moves entirely beyond basic API mocking or simple response caching. Attendees will leave this session knowing how to architect a framework agnostic recording layer, identify the exact state mutations required to guarantee replay determinism, understand where this approach complements durable execution architectures, and learn how to transform an unreproducible production anomaly into an execution path they can step through line by line.

Speakers:
- Tisha Chawla (Microsoft): Tisha Chawla is a Software Engineer at Microsoft working within the Commerce and Ecosystem Data Platform team, where she builds agentic systems designed to hold up against real production data. Her technical work spans core internal platform initiatives across Spec Driven Development, SRE Agent adoption, and enterprise SWE Agents, focusing on deterministic execution frameworks and agentic software development lifecycles. Alongside her infrastructure work, Tisha is a published researcher with peer reviewed papers in applied machine learning at venues including APNET SIGCOMM and ASONAM. She frequently delivers technical sessions to large engineering audiences across Microsoft, sharing high signal insights on deploying durable, production grade agentic workflows.
  LinkedIn: https://www.linkedin.com/in/tisha-chawla/
  GitHub: https://github.com/tishachawla-jg
- Susheem Koul (Microsoft): ​Susheem Koul is a Software Engineer at Microsoft with over 7 years of experience in product development. Currently, his work is focused on the design and implementation of intelligent, agentic systems. Beyond his professional focus on agentic workflows and multi-agent coordination, he explores the philosophy of learning and software architecture through his Substack
  LinkedIn: https://www.linkedin.com/in/susheemkoul/
  GitHub: https://github.com/susheem-k

## The Prompt is the Platform - Dominik Tornow, Resonate HQ

- Upload date: 2026-06-29
- Video: https://www.youtube.com/watch?v=DqtmZE6Hl0g
- Transcript: raw/20260629_DqtmZE6Hl0g/DqtmZE6Hl0g.en-orig.vtt
- Metadata: raw/20260629_DqtmZE6Hl0g/DqtmZE6Hl0g.info.json

Coding agents challenge long-standing software engineering practices. Instead of using general-purpose libraries, frameworks, or platforms, agents synthesize bespoke systems on demand. In this talk, I'll show where agents fail, where agents succeed, and the workflow for making the specification the product and the prompt the platform.

Speakers:
- Dominik Tornow (Resonate HQ, Inc): Dominik Tornow is the founder and CEO of Resonate and the author of Think Distributed Systems. He has spent more than 20 years designing and building distributed systems and now focuses on agentic engineering, formal modeling, and formal verification.
  X/Twitter: https://x.com/DominikTornow
  LinkedIn: https://www.linkedin.com/in/dtornow/
  GitHub: https://github.com/dtornow

## Deterministic Infra for Non-Deterministic AI Agents - Nishant Gupta, Meta Superintelligence Labs

- Upload date: 2026-06-29
- Video: https://www.youtube.com/watch?v=APh1Vx0oLmQ
- Transcript: raw/20260629_APh1Vx0oLmQ/APh1Vx0oLmQ.en-orig.vtt
- Metadata: raw/20260629_APh1Vx0oLmQ/APh1Vx0oLmQ.info.json

AI agents are rapidly evolving from copilots into autonomous systems capable of reasoning, invoking tools, coordinating workflows, and interacting with production infrastructure. But most platforms today were designed for deterministic microservices — not long-running, non-deterministic systems powered by LLMs.

This creates a massive infrastructure gap.

In this talk, I’ll share lessons from building large-scale agentic and elastic compute infrastructure powering production AI workloads. We’ll explore the emerging “control plane” required for reliable AI agents: orchestration, observability, retries, evaluation, safety guardrails, workload isolation, memory coordination, and operational control loops.

Topics include:

- Why most AI agents fail outside demos
- Building deterministic systems around stochastic models
- Observability for autonomous AI workflows
- Failure handling and retry storms in agent systems
- Human oversight and safety guardrails
- Elastic GPU infrastructure for agentic workloads
- Reliability patterns for production AI systems
- The shift from “prompt engineering” to “systems engineering”

Attendees will leave with practical architectural patterns for building resilient AI infrastructure capable of supporting autonomous systems safely and efficiently in production.

Speakers:
- Nishant Gupta (Meta Superintelligence Labs): Nishant Gupta is a Software Engineering Tech Lead at Meta Superintelligence Labs building the training and inference AI infrastructure.
  LinkedIn: https://www.linkedin.com/in/nishantgupta-ai/
  GitHub: https://github.com/nishantgpt-lab

## You Can't Prompt the Room: The Last Skill AI Won't Replace - Balázs Horváth, VisualLabs

- Upload date: 2026-06-29
- Video: https://www.youtube.com/watch?v=6bmM45jkMDY
- Transcript: raw/20260629_6bmM45jkMDY/6bmM45jkMDY.en-orig.vtt
- Metadata: raw/20260629_6bmM45jkMDY/6bmM45jkMDY.info.json

Writing code is no longer the bottleneck. With AI generating specifications, tests, and entire implementations on demand, the expensive part of the software development lifecycle has shifted upstream to the people work. Getting the right stakeholders into the room, eliciting the real requirements, and figuring out what is actually worth building.

This talk draws on a VisualLabs internal hackathon where 21 agent ideas were generated and 17 were abandoned, not because of technology limitations, but because they lacked data access, a clear business owner, or any measurable value. The 4 that survived are running in production today. The lesson: AI is optimised to produce the most common answer. Getting from a faster horse to a car requires a human who can read the room, map the process, and name the problem precisely before a single prompt is written.

The session covers three practical tools for doing exactly that: story mapping for capturing process backbone and user stories at the right altitude; the 4-question value framework (whose problem, what winning looks like, what would cause refusal, what decision it changes); and the VAD thinking path (Value to Architecture to Design) as the discipline that separates production agents from demo agents. Attendees leave with a concrete shift in how they measure delivery: fewer features shipped, more features used more than twice.

Speakers:
- Balázs Horváth (VisualLabs): Balazs Horvath is the founder of VisualLabs, a Budapest-based premium Microsoft Partner, who has spent 13 years bridging business and technology across US and UK ERP and CRM programmes, and now helps enterprise teams ship production AI agents by rebuilding the requirements and story-mapping skills that the AI coding boom has made more important than ever.
  LinkedIn: https://www.linkedin.com/in/balazshorvathd365/

## Building an Autonomous Engineering Org - Angie Jones, Agentic AI Foundation

- Upload date: 2026-06-28
- Video: https://www.youtube.com/watch?v=whue9_YquGA
- Transcript: raw/20260628_whue9_YquGA/whue9_YquGA.en-orig.vtt
- Metadata: raw/20260628_whue9_YquGA/whue9_YquGA.info.json

Nearly every enterprise company has a mandate to convert its existing engineering org into an autonomous one.

Buying the frontier models and tools is not enough. Everything about how we deliver software must change: from design, to development, to deployment.

In this talk, I’ll walk you through the journey of transitioning traditional software engineers into agentic ones, the systems and processes required for their success, and the new challenges agentic engineering introduces for large enterprise companies.

Speakers:
- Angie Jones (Agentic AI Foundation): Angie Jones is the VP of Developer Experience at the Agentic AI Foundation where she guides how agentic systems are designed, implemented, and adopted across the global developer ecosystem.
  X/Twitter: https://x.com/techgirl1908
  GitHub: https://github.com/angiejones

## The 100-Tool Agent Is a Trap - Sohail Shaikh & Ankush Rastogi, Prosodica

- Upload date: 2026-06-28
- Video: https://www.youtube.com/watch?v=vh2VGuQ3zhY
- Transcript: raw/20260628_vh2VGuQ3zhY/vh2VGuQ3zhY.en-orig.vtt
- Metadata: raw/20260628_vh2VGuQ3zhY/vh2VGuQ3zhY.info.json

The common “Fat Agent” architecture loads a large catalog of tools directly into the system prompt. This often creates latency, cost, and reliability problems in production agent systems. As tool schemas take up more of the context window, agents can become slower and more likely to choose the wrong tool.

This session takes a practical look at the Semantic Tool Router pattern, a deterministic layer that reduces the amount of context shown to the model in real time. The talk will share benchmarks across frontier models, including GPT-4o and Gemini 2.0, showing how the number of available tools affects Time-to-First-Token latency and tool-selection accuracy.

Attendees will learn how to move from static tool loading to Just-in-Time Context Injection, where only the most relevant tools are added to the prompt for each request. In high-tool-density benchmark scenarios, this approach can reduce response latency by up to 90%, reduce cross-tool confusion, and improve agent reliability. The session will end with a practical framework for building tool routers that can scale to hundreds of capabilities without sacrificing speed or predictability.

Speakers:
- Sohail Shaikh (Prosodica): Sohail Shaikh is a data scientist with nearly a decade of experience across AI, data science, analytics, marketing, and software-oriented work, focused on building practical, reliable, and scalable AI systems using NLP, RAG, conversational intelligence, and LLM workflows.
  LinkedIn: https://www.linkedin.com/in/sohail-shaikh/
  GitHub: https://github.com/Sohail-Sh
- Ankush Rastogi (Prosodica): Ankush Rastogi is a Senior Data Solutions Engineer with over a decade of experience building scalable data, analytics, and machine learning platforms, with a focus on turning AI models into reliable, production-ready enterprise systems through strong evaluation, inference performance, cost optimization, and operational design.
  LinkedIn: https://www.linkedin.com/in/ankushrastogi/
  GitHub: https://github.com/ankushrastogi04

## Your Agent Is Wasting Tokens and You Don't Know It - Erik Hanchett, AWS

- Upload date: 2026-06-28
- Video: https://www.youtube.com/watch?v=uiP88SpCi1Q
- Transcript: raw/20260628_uiP88SpCi1Q/uiP88SpCi1Q.en-orig.vtt
- Metadata: raw/20260628_uiP88SpCi1Q/uiP88SpCi1Q.info.json

I deployed an agent to production and the bill was not good. Not because the model was bad, but because it was doing too much. I was using the most expensive models for simple inference calls. The context was filling up. And my tool loops ran longer than they needed to. The agent worked fine, it just cost way more than it should have.

This talk covers three small changes I made that dropped my costs without hurting quality. Each one was a few lines of code, and none of them required changing my prompts or switching models. I'll cover things like prompt caching and model routing. I'll show code.

Speakers:
- Erik Hanchett (Amazon Web Services): Erik Hanchett is a Developer Advocate at AWS who helps developers build with frontend, fullstack, and AI/agent technologies through hands-on tutorials, talks, and videos.
  X/Twitter: https://x.com/erikch
  LinkedIn: https://www.linkedin.com/in/erikhanchett/
  GitHub: https://github.com/erikch

## We Cut 94% of AI Coding Tokens With a Local Code Index - Rajkumar Sakthivel, Tesco

- Upload date: 2026-06-28
- Video: https://www.youtube.com/watch?v=dRmWYHuIJxM
- Transcript: raw/20260628_dRmWYHuIJxM/dRmWYHuIJxM.en-orig.vtt
- Metadata: raw/20260628_dRmWYHuIJxM/dRmWYHuIJxM.info.json

Every AI coding tool we tried had the same assumption: send as much context as possible.

In our production codebase, that meant sending 45,000 tokens per query — even when only ~5,000 were actually useful. We didn’t notice how inefficient this was until we saw the cost and latency impact.

We tried improving prompts and tweaking model settings, but nothing addressed the core problem:
we were optimising the model, not the context.

So we built a local retrieval layer between the codebase and the agent.

Instead of sending full files, we:

Structured code using AST-aware chunks (tree-sitter)
Combined vector search with keyword matching for better retrieval
Used a lightweight relationship layer to follow execution across files
The result: 👉 94% reduction in tokens
👉 faster responses
👉 more accurate outputs

The hardest problem wasn’t retrieval — it was knowing when retrieval was wrong.
We experimented with LLM-based scoring and threshold tuning, but a simple heuristic ended up working best.

Everything runs locally, with no data leaving the machine, and one index supports multiple AI tools.

In this talk, I’ll walk through:

What we got wrong initially
Why context matters more than model tuning
The architecture behind the system
Real benchmarks and trade-offs
The key takeaway: 👉 The biggest optimisation in AI coding isn’t the model — it’s the context.

Speakers:
- Rajkumar Sakthivel (Tesco): Rajkumar Sakthivel builds LLM infrastructure at scale and co-created Code Context Engine after his team's AI coding bill jumped from £15 to £200 in a single month.
  X/Twitter: https://x.com/rajkumarsakthi
  LinkedIn: https://www.linkedin.com/in/rajkumar-sakthivel/
  GitHub: https://github.com/rajkumarsakthivel

## OpenClaw in Your Hand: Building a Physical AI Terminal - Lech Kalinowski, Callstack

- Upload date: 2026-06-28
- Video: https://www.youtube.com/watch?v=akk6KRlcwW4
- Transcript: raw/20260628_akk6KRlcwW4/akk6KRlcwW4.en-orig.vtt
- Metadata: raw/20260628_akk6KRlcwW4/akk6KRlcwW4.info.json

What if an AI device felt calm — closer to peace than a glowing distraction? Vault is a text-first, dual-display handheld AI terminal built on a single ESP32-S3 and powered by one battery cell. It pairs a fast, emissive OLED "live" surface with a slow, bistable e-paper "content" surface, switches between four modes with a single slash command — shell, assist, control, and an LLM-native RPG — and drives autonomous OpenClaw agents, all against a fully local, self-hosted model (gpt-oss:120b served by NVIDIA TensorRT-LLM). This talk walks the system end to end: an AI-native architecture where the firmware talks to a dependency-free Python backend that dispatches to local models, agents, and a game engine; why inference stays on the backend instead of the microcontroller; and how the device surfaces an agent thinking and calling tools in real time on e-paper. Along the way: the engineering war stories that each cost a day, the LLM-native game design that tracks narrative state instead of HP and dice, and what it actually takes to put a local agent in your pocket.

Speakers:
- Lech Kalinowski (Callstack): Dr. Lech Kalinowski is an AI and data science leader, PhD in Physical Sciences, and startup co-founder specializing in machine learning, AI strategy, printed electronics, and applied innovation.
  X/Twitter: https://x.com/LeSiOO
  LinkedIn: https://www.linkedin.com/in/lech-kalinowski/
  GitHub: https://github.com/lech-kalinowski

## Agents Building Agents - Alfonso Graziano, Nearform

- Upload date: 2026-06-28
- Video: https://www.youtube.com/watch?v=aHhB3sjGjkI
- Transcript: raw/20260628_aHhB3sjGjkI/aHhB3sjGjkI.en-orig.vtt
- Metadata: raw/20260628_aHhB3sjGjkI/aHhB3sjGjkI.info.json

Building an AI agent for a real team is not a prompt problem, it is a systems problem. In this session we walk through a practical, production-minded workflow for building an agent using a coding agent, and designing the codebase so that this loop stays reliable as complexity grows.

The core pattern is two agents with different jobs. The coding agent is the builder: it writes and changes the agent’s codebase. The agent you are building is the product agent. It is the custom agent you ship for a client or for internal use.

A key example is self-healing evals. We maintain an eval suite that exercises the product agent across representative tasks. When an eval fails, the builder agent runs the eval, inspects the failure artifacts, proposes a targeted fix to the correct layer (context, tool contract, or code), and opens a PR with a short report explaining what changed and what is still missing. If the agent cannot safely resolve the failure, it escalates by requesting specific human input and explaining exactly why it is blocked.

Speakers:
- Alfonso Graziano (Nearform): Alfonso is a Software Engineer led by curiosity and passionate about new technologies
  LinkedIn: https://www.linkedin.com/in/alfonso-graziano/
  GitHub: https://github.com/alfonsograziano

## When All Context Matters: Extended Cache Augmented Generation - Luis Romero-Sevilla, Orbis

- Upload date: 2026-06-28
- Video: https://www.youtube.com/watch?v=XovaGv4f39A
- Transcript: raw/20260628_XovaGv4f39A/XovaGv4f39A.en-orig.vtt
- Metadata: raw/20260628_XovaGv4f39A/XovaGv4f39A.info.json

This session addresses a critical challenge in knowledge representation: extracting accurate answers from a rapidly changing dataset where every document is highly interconnected and relevant.

Explore the limitations of standard retrieval methods for dynamic, high-context scenarios—including the constraints of Simple RAG and the computational bottlenecks of constantly recomputing a GraphRAG. To overcome these hurdles, this talk introduces a novel solution: Extended Cache Augmented Generation (ECAG).

Speakers:
- Luis Romero-Sevilla (Orbis Operations): Luis Romero-Sevilla is an AI strategist and full-stack software engineer with over 13 years of experience driving mission-critical technological innovation across defense, healthcare, and the public sector, currently serving as the Vice President of AI at Orbis Operations.
  X/Twitter: https://x.com/lurose15
  LinkedIn: https://www.linkedin.com/in/luis-romero-sevilla/
  GitHub: https://github.com/lurose5

## AI System Design: From Idea to Production - Apoorva Joshi, MongoDB

- Upload date: 2026-06-28
- Video: https://www.youtube.com/watch?v=T0HhO4YtTfE
- Transcript: raw/20260628_T0HhO4YtTfE/T0HhO4YtTfE.en-orig.vtt
- Metadata: raw/20260628_T0HhO4YtTfE/T0HhO4YtTfE.info.json

Writing code is no longer the hard part. AI can do that. In a world where AI writes the code, the most valuable skill an engineer can have is knowing what to build. Most AI systems never make it to production because of bad decisions made earlier in the process. The pressure to ship fast, the hype around AI, and the lack of a structured approach all push engineers toward building before they've thought through what they're building and why.

In this talk, you'll learn a structured framework for making the decisions that get AI systems to production. You'll learn how to identify the business problem, define success metrics, select the right architecture, define guardrails and evaluation metrics, and know what to optimize for when you ship. We'll apply the framework to a real-world problem as we go, so you can see how it works on an actual AI application.

Speakers:
- Apoorva Joshi (MongoDB): Apoorva is currently a Staff AI Developer Advocate at MongoDB. She has a diverse engineering background with a Bachelor’s in Electrical Engineering, a Master’s in Computer Engineering, and several years of experience as a data scientist, applying AI to problems in the cybersecurity space. She now uses that applied AI expertise to help data science and engineering teams at large enterprises and startups build production-grade AI applications with MongoDB and Voyage AI.
  LinkedIn: https://www.linkedin.com/in/apoorvajoshi95/
  GitHub: https://github.com/ajosh0504

## Research to Reality: Bringing Frontier ML Research to Production - Vaidas Razgaitis, Higharc

- Upload date: 2026-06-28
- Video: https://www.youtube.com/watch?v=OXMMN-XbxwA
- Transcript: raw/20260628_OXMMN-XbxwA/OXMMN-XbxwA.en-orig.vtt
- Metadata: raw/20260628_OXMMN-XbxwA/OXMMN-XbxwA.info.json

Three tactical tips to speed up how quickly your R&D team can turn novel research into customer-ready features

Speakers:
- Vaidas Razgaitis (Higharc): Vaidas is a Senior Research Engineer at Higharc, where he specializes in turning frontier ML research into production-grade features.
  X/Twitter: https://x.com/gingiVaidas
  LinkedIn: https://www.linkedin.com/in/vrazgaitis/
  GitHub: https://github.com/VRazgaitis

## User Signal Dies at the Retrieval Boundary - Sonam Pankaj, StarlightSearch

- Upload date: 2026-06-28
- Video: https://www.youtube.com/watch?v=Jx4ZFEAq6bY
- Transcript: raw/20260628_Jx4ZFEAq6bY/Jx4ZFEAq6bY.en-orig.vtt
- Metadata: raw/20260628_Jx4ZFEAq6bY/Jx4ZFEAq6bY.info.json

Utility is all you need! Closing the Agent Learning Loop with Utility-Ranked Memory

Most production agent systems have a fatal flaw: they start every run from a blank slate. You have traces in your observability stack and pass/fail judgments in your eval suite, but the agent that runs tomorrow has no memory of why yesterday's runs succeeded or failed.

This talk exposes the gap between observation and action and shows how to close it.

We'll examine why current memory approaches stall: conversation buffers that only remember recency, semantic systems that retrieve what sounds similar rather than what helped, and reflection-based methods that capture lessons but don't learn which ones actually work. The core idea: utility-ranked memory. Treat memories like a credit score. When a memory is retrieved and the run passes, its utility rises. When the run fails, its utility falls. The ranking formula combines semantic similarity with outcome history. 

There is also a demo with an example of the product SQL agent, of how it updates the context for the right outcome, everything happening at runtime.

Speakers:
- Sonam Pankaj (StarlightSearch Inc): Sonam is the CEO and Co-Founder of StarlightSearch. She is also the co-creator of embedanything, which is a Rust pipeline for RAG, which got contributions from Elastic, Milvus, and Qdrant, and has over 450k+ downloads. Prior to Starlight Search, Sonam spent years in developer tools and AI infrastructure, and has worked as a generative AI Evangelist, GTM lead at Articul8, a spin-off of Intel, and AI Researcher at Saama. She has been presenting talks for the last 10 years, and loves to interact with developers. She has been constantly speaking at Berlin Buzzwords, Europe's largest search conference, PyCon DE, and PyData. She also got an opportunity to present her work at Google, Deutsche Bank, and JetBrains.
  X/Twitter: https://x.com/sonam_pankaj_
  LinkedIn: https://www.linkedin.com/in/sonam-pankaj/
  GitHub: https://github.com/sonam-pankaj95

## Browser Agents Don't Need Better Models. They Need Better Eyes. - Kushan Raj, ARK

- Upload date: 2026-06-28
- Video: https://www.youtube.com/watch?v=JnubYCYunk8
- Transcript: raw/20260628_JnubYCYunk8/JnubYCYunk8.en-orig.vtt
- Metadata: raw/20260628_JnubYCYunk8/JnubYCYunk8.info.json

Every browser agent improvement in the last year has mostly been a model upgrade: better vision, longer context, smarter planning. And they still fail on basic workflows.

Our claim is that the main bottleneck is not the model. It is the interface we give the model to the browser. Three things matter more: what the model sees, what it can do, and what it learns from. We built a browser-agent runtime around all three: a compact page representation instead of a raw dump, fast actions with stable handles instead of one click per call, and step-by-step feedback instead of pass/fail at the end.

In our early runs, changing that interface alone was enough to take the same model from confusion to correct multi-step execution on hostile pages. This talk is the thesis, the evidence, where it still breaks, and why better browser state is a bigger lever than just swapping in a better model.

Speakers:
- Kushan Raj (ARK): Kushan Raj is a Founding ML Engineer at Sarvam AI, where he built the real-time voice AI stack that now powers 2M+ daily calls across 10+ Indian languages
  LinkedIn: https://www.linkedin.com/in/kushanraj/

## HTML is All You Need (for Agents to Make Graphics) - Amol Kapoor, Nori

- Upload date: 2026-06-28
- Video: https://www.youtube.com/watch?v=JRTAtZ5iBkU
- Transcript: raw/20260628_JRTAtZ5iBkU/JRTAtZ5iBkU.en-orig.vtt
- Metadata: raw/20260628_JRTAtZ5iBkU/JRTAtZ5iBkU.info.json

Coding agents are great at writing code. But non-believers will still say things like "these agents aren't really powerful because they have terrible geospatial understanding." ARC-AGI is literally grounded on this premise! And it's true that if you ask Claude or ChatGPT to draw a pelican riding a bike, you get some goofy results. But if you ask me, the problem is the tooling. We build Figma MCPs and Photoshop CLIs and all sorts of things to just get the agent to make a single powerpoint deck. I'm here to tell you that all of that is just user error. Just use HTML. HTML is all you need.

Speakers:
- Amol Kapoor (Nori): Amol is building Nori, the cheapest and most customizable AI employee on the market for any and all dev, ops, and sales automations.
  LinkedIn: https://www.linkedin.com/in/amolkapoor/
  GitHub: http://github.com/theahura/

## AI-Driven Multi-Document Correlation for Financial Compliance - Varsha Shah, Independent

- Upload date: 2026-06-28
- Video: https://www.youtube.com/watch?v=Iwe_RY-fYgI
- Transcript: raw/20260628_Iwe_RY-fYgI/Iwe_RY-fYgI.en-orig.vtt
- Metadata: raw/20260628_Iwe_RY-fYgI/Iwe_RY-fYgI.info.json

Traditional compliance and fraud detection systems analyze financial documents in isolation, making it difficult to identify sophisticated fraud patterns that emerge across multiple enterprise systems. This session presents an AI-driven framework that combines graph-based entity correlation, adaptive probabilistic risk modeling, and cross-jurisdictional normalization to detect hidden compliance risks across payroll, tax, procurement, and financial records. Drawing on an evaluation of approximately three million anonymized records across four jurisdictions, the talk demonstrates how cross-document intelligence can improve fraud detection accuracy, reduce false positives, and lower manual audit effort. Attendees will gain practical insights into building scalable AI solutions that transform enterprise compliance from a reactive validation process into a predictive, intelligence-driven capability.

Speakers:
- Varsha Shah (Independent Researcher): Varsha Shah is a Technical Architect, researcher focused on enterprise AI, agentic systems, intelligent document processing, and AI-powered financial governance.
  LinkedIn: linkedin.com/in/varsha-shah-7b5111247
  GitHub: https://github.com/VarshaShahTech

## Using Spec-Driven Development for Production Workflows - Erik Hanchett, AWS

- Upload date: 2026-06-28
- Video: https://www.youtube.com/watch?v=IddXPepIAS4
- Transcript: raw/20260628_IddXPepIAS4/IddXPepIAS4.en-orig.vtt
- Metadata: raw/20260628_IddXPepIAS4/IddXPepIAS4.info.json

AI coding assistants are great at completing small tasks or features. However, what do you do when you are working with more complex code bases, and you need to build in-depth features that need upfront planning?
This talk explores spec-driven development as a solution to this problem. I'll show you how modern AI coding assistants (like Kiro) can help break down complex tasks into three distinct phases. We'll look at the real-world tradeoffs of this approach, and most importantly and how you can use it in your own projects right away.

Speakers:
- Erik Hanchett (Amazon Web Services): Erik Hanchett is a Senior Developer Advocate at AWS who teaches developers how to build with modern web, AI, and the cloud.
  X/Twitter: https://x.com/erikch
  LinkedIn: https://www.linkedin.com/in/erikhanchett/
  GitHub: https://github.com/erikch

## Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry - Abed Matini, Ogilvy

- Upload date: 2026-06-28
- Video: https://www.youtube.com/watch?v=Akm1sqvWG4A
- Transcript: raw/20260628_Akm1sqvWG4A/Akm1sqvWG4A.en-orig.vtt
- Metadata: raw/20260628_Akm1sqvWG4A/Akm1sqvWG4A.info.json

Building a prototype chatbot interface takes an afternoon, but scaling it into a secure, predictable enterprise app requires solving production infrastructure challenges: minimizing unpredictable cloud API token bills, handling broken layout extractions, mapping session telemetry, and executing deterministic search.

In this practical, demo-driven session, we will bypass high-level wrapper libraries to dissect the complete technical implementation of a local-first document ingestion application. While our demo runs on local developer environments, the underlying design patterns mirror exactly how you build high-performance, cost-effective architectures using enterprise infrastructure like Azure Database for PostgreSQL with pgvector.

Key Architectural Blueprints We Will Explore:

Optimizing the Data Ingest: How parsing documents to clean structural Markdown locally eliminates cloud vision token overhead. We will look at implementing dynamic sidebar toggles to switch into heavy-duty local OCR pipelines when corrupted document font layers are encountered.

Database-First RAG without Framework Bloat: Why heading-based semantic chunking outperforms arbitrary sliding token windows. We will walk through the raw SQL schemas and indexes (HNSW tracking) required to combine dense embedding vectors and sparse keyword text indices natively inside a single database query, using Reciprocal Rank Fusion (RRF) for top-tier retrieval performance.

UX Telemetry and Application Guardrails: A deep dive into injecting live client-side floating widgets to display session telemetry, tracking token limits and cumulative ROI. Finally, we will touch on building a zero-dependency, background-threaded heuristic validation layer (_check_injection()) to scan incoming Markdown text for prompt-injection markers before they hit your persistence layer.

Speakers:
- Abed Matini (Ogilvy): Abed Matini is a software developer and AI engineer focused on practical RAG systems, with a strong emphasis on local and edge LLMs and lightweight production architectures.
  X/Twitter: https://x.com/abedmatini
  LinkedIn: https://www.linkedin.com/in/matini
  GitHub: https://github.com/abedmatini

## Voice In, Visuals Out: The Agony and the Ecstasy - Allen Pike, Forestwalk Labs

- Upload date: 2026-06-28
- Video: https://www.youtube.com/watch?v=65X0pQ6Lmbg
- Transcript: raw/20260628_65X0pQ6Lmbg/65X0pQ6Lmbg.en-orig.vtt
- Metadata: raw/20260628_65X0pQ6Lmbg/65X0pQ6Lmbg.info.json

The latest AI models have made it possible to go past text-based chats, and build what Andrej Karpathy argues is the pinnacle of AI UX: voice-in, visuals-out.

In this talk, Forestwalk Labs co-founder Allen Pike shares why this approach for LLM-powered product development is so useful, what's necessary to make it actually delight users, and lessons his team has learned building products with highly responsive AI agents like these – with a key focus on techniques for achieving low latency.

Speakers:
- Allen Pike (Forestwalk Labs): Allen is co-founder of Forestwalk Labs, runs the Infer AI engineering meetup, and hosts the It Shipped That Way podcast.
  X/Twitter: https://twitter.com/apike
  LinkedIn: https://www.linkedin.com/in/allenpike/
  GitHub: https://github.com/apike

## Structuring the Unstructured - Cedric Clyburn, Red Hat

- Upload date: 2026-06-28
- Video: https://www.youtube.com/watch?v=-x5GEVnkuRw
- Transcript: raw/20260628_-x5GEVnkuRw/-x5GEVnkuRw.en-orig.vtt
- Metadata: raw/20260628_-x5GEVnkuRw/-x5GEVnkuRw.info.json

Modern organizations generate vast amounts of data stored in diverse and often unstructured formats, such as PDFs, scanned documents, and proprietary file types. For engineers working with AI, the challenge isn’t just about extracting text but also about preserving the structure, context, and relationships within the data. Whether fine-tuning models or building retrieval-augmented generation (RAG) pipelines, effective document processing is essential for creating AI applications that bring value.

This live demo session is all about the techniques and open source tools needed to transform unstructured documents into structured formats like JSON or Markdown, ready for AI workflows. You’ll learn how to handle challenges like multi-page tables, image-heavy layouts, and scanned documents using context-aware methods with Docling, part of the Linux AI & Data Foundation.

Speakers:
- Cedric Clyburn (Red Hat): Cedric Clyburn (@cedricclyburn) is a Senior Developer Advocate at Red Hat and open-source contributor (vLLM, Podman) who helps developers adopt emerging technologies through speaking, workshops, and community leadership (as an organizer of Kubernetes Community Day New York).
  X/Twitter: https://x.com/cedricclyburn
  LinkedIn: linkedin.com/in/cedricclyburn/
  GitHub: github.com/cedricclyburn

## A Genius With Amnesia - Victor Savkin, Nx

- Upload date: 2026-06-26
- Video: https://www.youtube.com/watch?v=jVjt-2g8NMY
- Transcript: raw/20260626_jVjt-2g8NMY/jVjt-2g8NMY.en-orig.vtt
- Metadata: raw/20260626_jVjt-2g8NMY/jVjt-2g8NMY.info.json

Imagine a genie grants your wish and materializes the best engineer in the world, John Carmack in his prime, to work on your codebase. The catch: he can only see a tiny corner of it, and he forgets everything between interactions. No matter how good he is, the value isn’t there. This is what coding agents are today. We need to fix it.

Speakers:
- Victor Savkin (Nx): Victor is the creator of Nx, the agentic monorepo platform, and Polygraph, the meta-harness for maximum agent autonomy, with 20+ years building high-performance frameworks and build tools.
  X/Twitter: https://x.com/victorsavkin
  LinkedIn: https://www.linkedin.com/in/victorsavkin/
  GitHub: https://github.com/vsavkin

## Stop Writing Tone Instructions. Layer Them. - Isadora Martin-Dye, Isadora & Co

- Upload date: 2026-06-26
- Video: https://www.youtube.com/watch?v=ij-AU9dpJjc
- Transcript: raw/20260626_ij-AU9dpJjc/ij-AU9dpJjc.en-orig.vtt
- Metadata: raw/20260626_ij-AU9dpJjc/ij-AU9dpJjc.info.json

Brand voice that survives real users isn't an instruction you write once - it's an architecture. Drawing on production code from a wedding venue, a personal AI companion, and a tool for families of missing people, this talk breaks voice into four layers: immutable identity, situational mode, example-anchored voice, and a deterministic post-generation veto. The difference between a prompt that holds and one that breaks on turn 21 is knowing which job belongs to which layer.

Speakers:
- Isadora Martin-Dye (Isadora & Co | The Bloom House AI): Isadora Martin-Dye is the founder of Isadora & Co, a portfolio of four ventures spanning hospitality and AI: she speaks on vertical AI and on what it actually takes to design software for the relationship-driven, emotionally heightened audiences other AI products keep getting wrong.
  LinkedIn: https://www.linkedin.com/in/isadora-martin-dye-226353a1

## Turn 10,994 Notes Into Memory - Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI

- Upload date: 2026-06-26
- Video: https://www.youtube.com/watch?v=ZRM_TfEZcIo
- Transcript: raw/20260626_ZRM_TfEZcIo/ZRM_TfEZcIo.en-orig.vtt
- Metadata: raw/20260626_ZRM_TfEZcIo/ZRM_TfEZcIo.info.json

Full implementation is open-source: https://github.com/iusztinpaul/ai-research-os-workshop
Agent Engineering: Building Multi-Agent Systems Course: https://academy.towardsai.net/courses/agent-engineering

Turning thousands of notes, videos, documents, and repositories into usable AI context requires more than a bigger context window. It requires memory and context engineering: organizing sources, indexing what matters, and loading only what the model needs.

The talk shows how the authors turn an Obsidian vault of 10,000+ notes, documents, videos, and repositories from a passive knowledge archive into live context for AI agents. A system that the authors use daily as their personal AI research OS for writing code and creating content.

You'll learn to design a deep research algorithm that runs across both the open web and your personal "Second Brain", then store what it finds as a research memory you and your agents can maintain, visualize, and grow. All based on the authors' 3 major iterations of the system over the past 18 months.

You'll walk away knowing how to:

- Choose the right tool for the job: Codex/Claude Code vs. NotebookLM vs. RAG vs. a personalized research memory
- Design deep-research pipelines across Obsidian, NotebookLM, GitHub, Google Drive, Readwise, and YouTube
- Build a token-efficient memory layer from plain files, not a vector or graph DB
- Plug tens of thousands of personal notes into an LLM knowledge (or wiki) base that scales
- Implement the memory layer between your Second Brain and any agent harness (Codex, Claude Code, or your own)

For: Engineers ready to move beyond hoarding notes and turn their "Second Brain" into a context that their AI agents can research, maintain, and grow.

Speaker info:

Paul Iusztin

- X: https://x.com/pauliusztin_
- in: https://www.linkedin.com/in/pauliusztin/
- youtube: https://www.youtube.com/@itsdecodingai

Louis-François Bouchard

- X: https://x.com/Whats_AI
- in: https://www.linkedin.com/in/whats-ai/
- youtube: https://www.youtube.com/@WhatsAI

Timestamps:

00:00- Introduction to the "Second Brain" concept
00:49- The core problem: Losing research and finding meaningful notes
01:32- Building an AI Research OS
02:05- Meet the presenters: Louis-François Bouchard and Pauline
03:31- Choosing the right tools for research (Google vs. LLMs)
04:51- Why NotebookLM and vector databases aren't always ideal
07:08- The need for a personalized research assistant
09:16- Moving data to Obsidian for local file management
11:02- Overview of the AI Research OS repository
12:48- The three-layer system: Raw content, Index, and Wiki
13:28- Architecture of the Deep Research algorithm
18:28- Version 3: Adding the Wiki layer on top of knowledge bases
20:13- How the file-based index works (no database required)
21:26- Exploring the Wiki structure: Comparisons, concepts, and entities
22:49- How to query the Wiki efficiently
25:01- Managing snapshots and personal notes using the PARA method
27:04- Demo 1: Researching agent engineering
31:58- Demo 2: Ingesting and comparing GitHub repositories
34:25- Demo 3: Ingesting custom web links
36:50- Future improvements: Connectors, memory compaction, and source provenance
38:45- The Agent Engineering course overview

Speakers:
- Paul Iusztin: Paul Iusztin is the Founder & CEO of Decoding AI and the author of the bestselling LLM Engineer's Handbook. | Louis-François Bouchard is the Co-founder & CTO of Towards AI and author of Building LLMs for Production.
  X/Twitter: https://x.com/pauliusztin_
  LinkedIn: https://www.linkedin.com/in/pauliusztin/
  GitHub: https://github.com/iusztinpaul

## Agents in Production: How OpenGov Built and Scaled OG Assist - Gabe De Mesa, OpenGov

- Upload date: 2026-06-26
- Video: https://www.youtube.com/watch?v=4uFVSLgD2Q4
- Transcript: raw/20260626_4uFVSLgD2Q4/4uFVSLgD2Q4.en-orig.vtt
- Metadata: raw/20260626_4uFVSLgD2Q4/4uFVSLgD2Q4.info.json

Come and learn about building AI Agents in production. Learn hands-on directly with the AI Agents team from OpenGov which powers AI workflows across thousands of state and local governments.

This session will cover:
* The core agent loop/harness
* A2A protocol
* Building with Effect-TS and Typescript
* Feedback and evals
* Long context handling
* Monitoring and observability
* Building out tools and skills
* Enterprise contribution model
* Accelerating workflows with Claude and Cursor

Speakers:
- Gabe De Mesa (OpenGov): Gabe works on the flagship AI Agent product offering at OpenGov which serves thousands of state and local governments across the country. Gabe was one of the first engineers to join the newly formed AI Agents team. He wanted to share the features he's built, experience he's gained building and running agents in production, battle scars gained from running with real production workloads and customers, architecture, and some best practices to help other engineers run agentic workloads at their companies.
  X/Twitter: https://x.com/jamesjellow
  LinkedIn: https://www.linkedin.com/in/gabedemesa
  GitHub: https://github.com/gabedemesa

## Production Evals For Agentic AI Systems - Nishant Gupta, Meta Superintelligence Labs

- Upload date: 2026-06-25
- Video: https://www.youtube.com/watch?v=vljxQZfJ9wY
- Transcript: raw/20260625_vljxQZfJ9wY/vljxQZfJ9wY.en-orig.vtt
- Metadata: raw/20260625_vljxQZfJ9wY/vljxQZfJ9wY.info.json

As AI systems evolve from chat interfaces into autonomous agents capable of reasoning, planning, and tool usage, traditional evaluation approaches are breaking down. Offline benchmarks and static datasets fail to capture the complexity, non-determinism, and operational risks of real-world AI systems operating in production environments.

In this talk, I’ll share practical lessons and architectural patterns for building evaluation systems for agentic AI workflows at scale. We’ll explore how modern AI platforms are shifting from one-time benchmark testing toward continuous evaluation pipelines integrated directly into production infrastructure.

Topics include:
- Why offline evals fail for autonomous AI systems
- Evaluating tool use, planning, reasoning, and multi-step workflows
- Online vs offline eval architectures
- Human-in-the-loop evaluation systems
- Detecting drift, hallucinations, and unsafe behaviors
- Building feedback loops for continuous improvement
- Observability and telemetry for agentic workflows
- Reliability metrics beyond model accuracy

Attendees will leave with practical frameworks for designing scalable evaluation systems capable of measuring real-world AI behavior, reliability, and operational impact.

Speakers:
- Nishant Gupta (Meta Superintelligence Labs): Nishant Gupta is a Software Engineering Tech Lead at Meta Superintelligence Labs focused on building the training and inference AI Infrastructure.
  LinkedIn: https://www.linkedin.com/in/nishantgupta-ai/
  GitHub: https://github.com/nishantgpt-lab

## Build Systems, Not Code - Angie Jones, Agentic AI Foundation

- Upload date: 2026-06-25
- Video: https://www.youtube.com/watch?v=ZD9-4fW2HhM
- Transcript: raw/20260625_ZD9-4fW2HhM/ZD9-4fW2HhM.en-orig.vtt
- Metadata: raw/20260625_ZD9-4fW2HhM/ZD9-4fW2HhM.info.json

AI coding agents are changing what it feels like to be a software engineer. For a lot of us, that's challenging our sense of craftsmanship. If agents are writing the code, do we lose the joy of building?

I don't think so. The building moves up a layer.

In this talk, I'll share how I found that familiar engineering flow state again. Not by writing every line myself, but by designing agentic systems that still require the engineering principles we value: systems thinking, decomposition, separation of concerns, state management, etc.

The tools are different now, but the engineering discipline is still there. We'll walk through how to apply the engineering muscles you already have to a new set of building blocks.

If you've been wondering where your value goes in an AI native world, this talk will help you see that it hasn't disappeared. It's now at the system level.

Speakers:
- Angie Jones (Agentic AI Foundation): Angie Jones is the VP of Developer Experience at the Agentic AI Foundation where she guides how agentic systems are designed, implemented, and adopted across the global developer ecosystem.
  X/Twitter: https://twitter.com/techgirl1908
  LinkedIn: https://www.linkedin.com/in/angiejones/
  GitHub: https://github.com/angiejones

## The Log Is The Agent - Ishaan Sehgal, Omnara

- Upload date: 2026-06-25
- Video: https://www.youtube.com/watch?v=UPwGaM2MKHY
- Transcript: raw/20260625_UPwGaM2MKHY/UPwGaM2MKHY.en-orig.vtt
- Metadata: raw/20260625_UPwGaM2MKHY/UPwGaM2MKHY.info.json

Think about a character you've spent 100 hours playing in a video game like Skyrim or Elden Ring.

What exactly is your character?
- Is it the game engine (the loop)? No.
- Is it the PlayStation console (the compute)? No.
- Is it the controller (the tools)? No.

Your character is the save file (the data).

If your PlayStation bursts into flames, your character isn't dead. You just buy a new PlayStation, download your save file from the cloud, and your character is exactly where they were, mid-swing. The identity, history, and current state of your character live entirely in the data.

Today, most attention goes toward frameworks, orchestration layers, context engineering, specs, and tools. But as models become more capable and generally intelligent, the differentiator shifts away from these abstractions and toward the underlying infrastructure.

The Engine becomes interchangeable. The Brain (LLM) commoditizes. The Hands (tools) are just APIs.

What actually persists across models, runtimes, and machines is the session log.

That’s where continuity, identity, and state actually live.

A decade ago, Martin Kleppmann argued that databases should be understood as projections over an append-only log. I think the same thing is now happening with agents.

Today, agents are treated like complicated black boxes made of loops, models, and tool calls. But at its core, the agent is the session log (the save file). Everything else is swappable.

Once the log becomes the primitive, entirely new system properties emerge:
- durability — agents survive crashes, disconnects, and machine failure
- continuity — sessions can be resumed from anywhere, on any device
- forkability — timelines can branch for parallel execution and exploration
- addressability — agents become durable entities that can be referenced and revisited
- observability — execution can be monitored and steered in real time
- portability — models, runtimes, and machines become interchangeable

But this creates a new infrastructure question:

If the model provider owns the log, does the model provider own the agent?

This talk explores why the future of agent infrastructure isn't what we're focused on today, but rather durable, portable logs that make agents persistent across models, runtimes, and machines.

Speakers:
- Ishaan Sehgal (Omnara): Ishaan Sehgal is the CEO and cofounder of Omnara (YC S25), where he builds managed infrastructure for AI agents.
  X/Twitter: https://x.com/ishaansehgal
  LinkedIn: https://www.linkedin.com/in/ishaan-sehgal/
  GitHub: https://github.com/ishaansehgal99

## The Miranda Hypothesis: How Hamilton Poisoned Persona Evals - Jacob E. Thomas, Results Gen

- Upload date: 2026-06-25
- Video: https://www.youtube.com/watch?v=IJXjTLPzvAU
- Transcript: raw/20260625_IJXjTLPzvAU/IJXjTLPzvAU.en-orig.vtt
- Metadata: raw/20260625_IJXjTLPzvAU/IJXjTLPzvAU.info.json

Your persona-eval pipeline rates an Alexander Hamilton simulation at 80% personality fidelity. It is also rating a Hamilton who sounds like he has read his own Broadway musical. The dominant failure mode of every character-based AI system now in production is invisible to LLM-as-judge, personality-scale benchmarks, and behavioral consistency scores because every one of them was built to detect convincingness, and convincingness is exactly what the failure produces.

The failure has a name: Miranda distortion. When the volume of cultural representation of a figure in your training corpus outnumbers their primary documentary record by orders of magnitude (and it always does for any culturally salient figure) your persona doesn't speak from the record. It speaks from the smoothed cultural composite. The 2015 Broadway musical has exponentially more representational density in your training data than the 175,000 words of the Federalist Papers. Your evals were not designed to notice this. They were designed to score fluency, personality coherence, and stylistic naturalness... the exact features the composite optimizes.

In this talk:

- The structural argument: why InCharacter-style benchmarks, CoSER, and PsyMem can hit state-of-the-art on personality fidelity while structurally failing to detect anachronistic reasoning.
- The architectural mechanism: why RLHF amplifies Miranda distortion instead of correcting it (raters are themselves products of the same cultural composite).
- The framework: a four-stage paradigm shift from cognitive simulation to epistemic simulation (corpus-bounded, temporally-anchored, expert-loop-evaluated).
- The instrument: the pre-registered Prism Experiment. Lincoln at four documented temporal moments, three seeding conditions, five diagnostic questions written by a domain historian, and a weighted three-axis rubric (Anachronism Detection, Documentary Consistency, Contextual Plausibility) that catches what automated metrics miss.
- The handoff: what a working eval loop looks like when a historian, classicist, theologian, or clinical psychologist sits in it, and why that's a technical requirement, not a cultural courtesy

Pre-registered protocol with University of Toronto historian Rick Halpern, paper forthcoming. Reproducible by any team running a frontier model with a context window.

If you ship character bots, companion AI, pedagogical agents, historical simulations, or any system where a persona is supposed to reason from a specified record, your evals are measuring the wrong thing. Here is the instrument that catches what they miss.

Speakers:
- Jacob E. Thomas (Results Generation): Dr. Thomas is an epidemiologist, data scientist, and AI engineer who studies information as a determinant of health.
  LinkedIn: https://www.linkedin.com/in/jacob-e-thomas-atx/
  GitHub: https://github.com/jethomasphd/THE_COMPANION_DOSSIER

## Recursive Coding Agents - Raymond Weitekamp, OpenProse

- Upload date: 2026-06-25
- Video: https://www.youtube.com/watch?v=3hXJI2q0Jz8
- Transcript: raw/20260625_3hXJI2q0Jz8/3hXJI2q0Jz8.en-orig.vtt
- Metadata: raw/20260625_3hXJI2q0Jz8/3hXJI2q0Jz8.info.json

Recursive Language Models (RLMs) represent a powerful new paradigm of inference-time compute. We discuss many different ways to apply the principles of RLMs to coding agents, towards higher performance and reliability. We briefly define RLMs, showcase many of their performance advantages, then share how the RLM paradigm can be mapped onto coding agents. We strive to settle the long-standing debate, "Isn't Claude Code with sub-agents a RLM?" Finally, we showcase how both Claude Code Dynamic Workflows and OpenProse can specifically guide coding agents to recursively solve complex tasks with declarable outcomes.

The "slides" for this presentation are available as an interactive website at https://recursivecodingagents.com and a companion repo with specific code examples is available at https://github.com/rawwerks/recursive-coding-agents

Speakers:
- Raymond Weitekamp (OpenProse): Dr. Raymond Weitekamp is a PhD chemist, serial entrepreneur, artist, independent researcher, and AI Engineer at OpenProse.
  X/Twitter: https://x.com/raw_works
  LinkedIn: https://www.linkedin.com/in/raymondweitekamp/
  GitHub: https://github.com/rawwerks

## 6 Things to Know about AIE World's Fair 2026

- Upload date: 2026-06-21
- Video: https://www.youtube.com/watch?v=0S8xe9ftGTM
- Transcript: raw/20260621_0S8xe9ftGTM/0S8xe9ftGTM.en-orig.vtt
- Metadata: raw/20260621_0S8xe9ftGTM/0S8xe9ftGTM.info.json

We're back in SF! Regular bird tix will sell out by Monday, and we wanted to make a little video to tell you about why you should get off your couch and come. 

See video for how to claim the $40k in sponsor offers for attendees, and a special youtube-only discount: YOUTUBEPROMO (for new tix only, dont be cheeky and ask for refunds pls, our team is trying to do our best with real support issues) 

https://app.ai.engineer/e/ai-engineer-worlds-fair-2026?discount=YOUTUBEPROMO applies at checkout

timestmaps

0:00 Introduction to AIE World's Fair 2026
1:30 Scaling up: Content and Event Growth
4:44 The Expo Floor experience
5:45 Research and Industry synergy
9:20 Leadership track and Token Billionaires
12:05 Focus on AI Verticals
13:41 Side events, orientation, and community

## The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks

- Upload date: 2026-06-18
- Video: https://www.youtube.com/watch?v=ObTPqBGsEbA
- Transcript: raw/20260618_ObTPqBGsEbA/ObTPqBGsEbA.en-orig.vtt
- Metadata: raw/20260618_ObTPqBGsEbA/ObTPqBGsEbA.info.json

A retail bank spent £85,000 over six months on a chatbot PoC that could not reach production. No one could explain why it was failing. When Sandipan Bhaumik's team got involved, they picked the model in week seven of an eight-week engagement — the first six weeks went to evaluation data, tracing infrastructure, and a measurement pipeline. Six weeks post launch, when the bank updated its interest rate policy and customer satisfaction dropped, the tracing system caught the cause: the new policy document had not been reembedded and the agent was serving stale answers.

The talk covers the five pillars he built from that and similar engagements: evaluation (define success numerically before touching code), observability (trace every agent decision — European regulators require it), data foundation (agents do not forgive bad data the way humans do), multi agent orchestration patterns, and governance (47 PII breaches caught in testing before launch). The evaluation data set is a living system, not a fixed benchmark. The production incident playbook connects all five.

Speaker info:
- https://www.linkedin.com/in/sandipanbhaumik

## Your Agent's Biggest Lie: "I Searched the Web" — Rafael Levi, Bright Data

- Upload date: 2026-06-17
- Video: https://www.youtube.com/watch?v=btxGmN8RvNU
- Transcript: raw/20260617_btxGmN8RvNU/btxGmN8RvNU.en-orig.vtt
- Metadata: raw/20260617_btxGmN8RvNU/btxGmN8RvNU.info.json

Sometimes the agent did not search the web at all. It got blocked, hit a CAPTCHA, saw a fake page, or fell back to stale training data, then answered as if everything worked. This session is a direct look at that failure mode, and what changes when the same agent is given real web access instead of pretending.

Using Bright Data's Web MCP, the demo compares blocked and unblocked runs across sites like LinkedIn, Instagram, Amazon, and TikTok, and walks through the mechanics behind the difference: anti-bot systems, JS rendering, CAPTCHA handling, and why clean access matters if you want reliable citations, real-time results, and fewer hallucinations. If you're building agents that depend on the open web, this is a practical look at one of their biggest hidden failure modes.

Speaker info:
- https://il.linkedin.com/in/rafael-levi
- https://github.com/ScrapeAlchemist

## You Might Not Need 50 Diffusion Steps — Ziv Ilan, Nvidia

- Upload date: 2026-06-16
- Video: https://www.youtube.com/watch?v=gHs5ZiY80PM
- Transcript: raw/20260616_gHs5ZiY80PM/gHs5ZiY80PM.en-orig.vtt
- Metadata: raw/20260616_gHs5ZiY80PM/gHs5ZiY80PM.info.json

At GTC a few weeks ago, Ziv Ilan's team at NVIDIA got a video diffusion model generating in close to real time on a single Blackwell B200. The trick wasn't a new architecture, it was stripping out most of the fifty step denoising process diffusion models default to, by combining quantization, caching, and step distillation: training a student model to match a teacher's output using four steps, eight steps, or in some cases just one.

Ilan walks through each layer of that stack: dynamic quantization work done with Black Forest Labs on Flux 2, a caching method that skips recomputing latent chunks that barely change between denoising steps, and distillation approaches split into trajectory based training, where the student copies the teacher's exact path, and distribution based training, where it only has to land on the same output, now the more common and higher quality of the two. NVIDIA's open source FastGen repo packages the post training and GPU sharding work needed to apply all this at scale, and Ilan frames the gains as additive, quantization alone can be enough on its own, or you can stack it with caching and distillation to reach the ten to two hundred times speedup that real time generation needs.

Speaker info:
- https://www.linkedin.com/in/ziv-ilan-deci/

## Why MCP and ChatGPT Apps Use Double Iframes — Frédéric Barthelet, Alpic

- Upload date: 2026-06-15
- Video: https://www.youtube.com/watch?v=c-2eEv2ou7Y
- Transcript: raw/20260615_c-2eEv2ou7Y/c-2eEv2ou7Y.en-orig.vtt
- Metadata: raw/20260615_c-2eEv2ou7Y/c-2eEv2ou7Y.info.json

Inspect ChatGPT's DOM while an MCP app is rendering and you find an iframe nested inside another iframe. Frédéric Barthelet traces why each simpler approach fails: `srcdoc` shares the parent origin so ChatGPT's CSP blocks all third party scripts; relaxing that CSP lets any app read ChatGPT's localStorage and cookies; adding `sandbox` removes origin indexed storage; adding `allow-same-origin` to restore it is the classic sandbox escape. The double iframe is what remains after ruling all of that out.

The outer iframe serves one lightweight script from a controlled subdomain (different subdomain per app to prevent cross app storage collisions), which loads the actual app HTML via `srcdoc` into the inner frame — the same pattern Facebook first shipped for their app marketplace. The practical implication: every external domain your view touches must be declared in your MCP app metadata or the submission gets rejected. Barthelet demos Skybridge's CSP inspector, which diffs declared domains against actual network calls live in dev.

Speaker info:
- https://x.com/bartheletf
- https://www.linkedin.com/in/frederic-barthelet/
- https://github.com/fredericbarthelet

## Your Attention Is the Bottleneck, Not Your Agents — Zack Proser, WorkOS

- Upload date: 2026-06-11
- Video: https://www.youtube.com/watch?v=so9l_MwS2yg
- Transcript: raw/20260611_so9l_MwS2yg/so9l_MwS2yg.en-orig.vtt
- Metadata: raw/20260611_so9l_MwS2yg/so9l_MwS2yg.info.json

Simon Willison fires up four parallel agents and is wiped out by 11am. That is the problem Zack Proser is solving: not that the tools are too slow but that human attention is still the hard constraint. His loop: voice brief at 184 words per minute, agent dispatched to an isolated git worktree, laptop closed, progress checked from a phone on LTE miles away via remote control.

The talk covers four layers that make this sustainable: signal agents that read Slack and Linear on a loop so you never open them yourself, verification gates from lint and build up to browser click through and critic passes, a weekly agent run over your JSONL conversation history to surface inefficiencies and generate missing skills, and an Oura ring connected via MCP so Claude can tell you that you did not sleep last night. You can ignore it. But at least you thought about it.

Speaker info:
- https://linkedin.com/in/zackproser
- https://github.com/zackproser

Timestamps:
0:00 Introduction and the problem of AI developer burnout
1:08 A concrete example of using AI agents for bug fixing
3:36 The bottleneck: human attention vs. infinite agent scalability
5:13 The proposed stack for sustainable AI development
6:03 The Signal Layer: Managing notifications and context switching
7:04 Voice-first flows for coding efficiency
8:15 The Shower Principle and Remote Control for agents
11:13 Safety, verification, and testing gates
12:05 The new, balanced developer workflow
13:22 System self-improvement using conversation history
15:31 Holistic well-being (Oura ring integration)
17:35 Q&A: Addressing skill development early in a career
20:07 Q&A: Managing JSONL history and long-term conversation logs
21:30 Q&A: Night shift/background agent execution
22:17 Q&A: Voice interaction and audio feedback
23:39 Q&A: Handling complex, multi-stack features

## Why Can't Anyone Answer Questions About the Business? — Garrett Galow, WorkOS

- Upload date: 2026-06-11
- Video: https://www.youtube.com/watch?v=iUWwcG-C8OU
- Transcript: raw/20260611_iUWwcG-C8OU/iUWwcG-C8OU.en-orig.vtt
- Metadata: raw/20260611_iUWwcG-C8OU/iUWwcG-C8OU.info.json

Every business question that needs SQL follows the same loop: explain the question, wait for an engineer, get an answer, realize it needs one more join, share a one-off in Slack, repeat. Garrett Galow from WorkOS built Studio to break that loop — an internal workspace where anyone can ask questions against Snowflake, Linear, and Notion in natural language and get answers or reusable widgets without filing a request.

The widgets are the interesting part: the LLM writes them once as declarative JavaScript that calls the underlying data sources directly, so every subsequent run is deterministic and cheap. Three things made it reliable enough to hand to a support team. Preflight sequencing that injects schema context only at the moment a tool is invoked, not upfront, keeping the context window clean. A layering rule that explicitly tells the model to distrust its own knowledge about WorkOS and go to primary sources. And query validation that runs every generated Snowflake query before hardcoding it into a widget, catching the valid SQL that returns zero rows failure mode.

Speaker info:
- https://www.linkedin.com/in/garrett-galow/

## The agent-ready web: Simplify user actions with WebMCP — Tara Agyemang, Google

- Upload date: 2026-06-11
- Video: https://www.youtube.com/watch?v=ghJmWQCIHRM
- Transcript: raw/20260611_ghJmWQCIHRM/ghJmWQCIHRM.en-orig.vtt
- Metadata: raw/20260611_ghJmWQCIHRM/ghJmWQCIHRM.info.json

Buying two concert tickets costs an AI agent the entire DOM, the accessibility tree, a screenshot, pixel coordinate math, and then a click that might miss because an ad just loaded and shifted the layout. Tara Agyemang from the Google Chrome team introduces WebMCP, a proposed web standard that replaces that process with structured tools: instead of guessing what your site does, agents get a menu of named, typed, described actions they can call directly.

The talk covers two implementation paths. The declarative API adds a few HTML attributes to existing forms and the browser generates the JSON schema automatically. The imperative API lets you register custom tools in JavaScript for complex multi step flows, with an execute block that runs normal DOM code and returns state back to the agent. The live demo completes a concert ticket purchase in three tool calls: search by name, open the concert page, call purchase with quantity and section. Still experimental and in early preview on Chrome 146, but an eval CLI and inspector extension are available now for testing your own sites.

Speaker info:
- https://x.com/tara_ojo
- https://uk.linkedin.com/in/taraojo
- https://github.com/taraojo

## Self Driving Products: Product Signals to Pull Requests — Joshua Snyder, PostHog

- Upload date: 2026-06-10
- Video: https://www.youtube.com/watch?v=zMiSRliEzv4
- Transcript: raw/20260610_zMiSRliEzv4/zMiSRliEzv4.en-orig.vtt
- Metadata: raw/20260610_zMiSRliEzv4/zMiSRliEzv4.info.json

A rage click, a 2am error spike, a customer Slack message — today each sits until a developer notices, triages, tickets, and writes a fix. PostHog is building a pipeline that collapses that chain: signal arrives, a background agent groups it with related errors and session replays, researches the codebase, and opens a PR. You wake up to green PRs instead of dashboards.

Three lessons from building it: off the shelf embedding models cluster signals by structural similarity rather than meaning, so errors land next to errors and Slack messages land next to Slack messages — the fix is to embed LLM generated queries rather than the signals themselves. Specificity determines whether the agent produces a useful PR or just fixes something at random; error tracking is immediately actionable, Slack and session replay usually are not. And start with agents even when it looks expensive — run the same problem through an agent 100 times, find the patterns, then collapse the expensive step into a one shot call.

Speaker info:
- https://x.com/joshsny
-https://www.linkedin.com/in/joshsny/

## Stop Making Models Bigger, Make Them Behave — Kobie Crawford, Snorkel

- Upload date: 2026-06-10
- Video: https://www.youtube.com/watch?v=TNwJ1LMiENk
- Transcript: raw/20260610_TNwJ1LMiENk/TNwJ1LMiENk.en-orig.vtt
- Metadata: raw/20260610_TNwJ1LMiENk/TNwJ1LMiENk.info.json

Qwen 3 235B was asked for YouTube's year over year ad revenue growth from 2023 to 2024. It queried a table that didn't exist, tried again, got nothing back both times, and hallucinated an answer. The 4B model Snorkel finetuned with RL called `get_table_name` first, inspected the schema, ran a query, hit a column error, self-corrected, and got the right answer. The training run cost under $500.

Kobe Crawford covers why tool discipline matters more than reasoning depth for this class of tasks, how single table training transferred cleanly to harder multi table problems (13.9% to 26.6% on the FinQA reasoning benchmark), and why breaking evals into rubrics helps identify which specific behavior to fix before writing any training data.

Speaker info:
- https://www.linkedin.com/in/kobie-crawford
- https://snorkel.ai/author/kobie-crawford/

## Sovereign Escape Velocity: Ownership w Open Models — Gus Martins, & Ian Ballantyne, Google DeepMind

- Upload date: 2026-06-10
- Video: https://www.youtube.com/watch?v=SS-A8sE7hkw
- Transcript: raw/20260610_SS-A8sE7hkw/SS-A8sE7hkw.en-orig.vtt
- Metadata: raw/20260610_SS-A8sE7hkw/SS-A8sE7hkw.info.json

Gemma 4's 31B model sits fourth on the LM Arena open model leaderboard. The models around it are at least twice as large; some are 20 times larger. It runs on a single GPU. Competitors at comparable quality need four or five.

Ian Ballantyne and Gus Martins walk through what that size efficiency unlocks: running on a Pixel phone (the E2B and E4B models use 2B and 4B of GPU memory despite having more parameters), deploying a medical variant on two GPUs for an entire hospital, and running parallel multi agent workloads on an M4 Mac via LM Studio. The talk also covers the license shift from a custom Gemma license to Apache 2.0 — the practical effect is that sovereign institutions in Ukraine, Bulgaria, and Brazil can get legal sign off without 18 months of procurement review.

Speaker info:
- https://x.com/gusthema
- https://www.linkedin.com/in/gus-martins-64ab5891
- https://linkedin.com/in/ianballantyne
- https://github.com/irbg

## GPU Cloud Deployment Without Leaving Your IDE — Audry Hsu, RunPod

- Upload date: 2026-06-09
- Video: https://www.youtube.com/watch?v=zDGHt0LB-dA
- Transcript: raw/20260609_zDGHt0LB-dA/zDGHt0LB-dA.en-orig.vtt
- Metadata: raw/20260609_zDGHt0LB-dA/zDGHt0LB-dA.info.json

The iteration cycle before Flash: commit, push, build a Docker image, pull it from the registry, load it onto a server, allocate a GPU, then find out if it works. Audrey Hsu demos what replacing that with a single decorator looks like — add `@flash.endpoint` to an async Python function and it deploys to GPU cloud from your IDE, with hot reload so a model swap is one line of code rather than a container rebuild.

The second demo chains three models: Qwen 3 generates image prompts, DreamShaper renders them, Nano Banana 2 composes the results into a single photo. H100 pricing is $0.00116 per second, charged only while a worker is handling a request. RunPod's recommendation: start with pods while experimenting, switch to serverless when you need hundreds of workers autoscaling across data centers.

Speaker info:
- https://www.linkedin.com/in/audry-hsu/

## 2026 AI Engineer Vibe Reel

- Upload date: 2026-06-09
- Video: https://www.youtube.com/watch?v=gUMwt4-5kn0
- Transcript: raw/20260609_gUMwt4-5kn0/gUMwt4-5kn0.en-orig.vtt
- Metadata: raw/20260609_gUMwt4-5kn0/gUMwt4-5kn0.info.json

W are getting ready for the World's Fair in San Francisco - Jun 29 to July 2!

https://ai.engineer/wf  - get tickets and see schedule!

## RAG is dead, right?? — Kuba Rogut, Turbopuffer

- Upload date: 2026-06-09
- Video: https://www.youtube.com/watch?v=UM6sFg_jdlE
- Transcript: raw/20260609_UM6sFg_jdlE/UM6sFg_jdlE.en-orig.vtt
- Metadata: raw/20260609_UM6sFg_jdlE/UM6sFg_jdlE.info.json

Cursor added semantic search and measured a 24% increase in answer accuracy on their composer model, a 2.6% gain in code retention in large codebases, and a 2.2% drop in dissatisfied user requests. Those numbers look small until you factor in that semantic search does not fire on every query. Meanwhile Google search volume for RAG hit a new inflection point in mid 2025 and went through the roof. The Twitter "RAG is dead" discourse and the actual usage curve are moving in opposite directions.

Kuba Rogut's argument is that the problem was never retrieval, it was the narrow definition of it. RAG is not just a vector search call. It is vector search, full text search, glob, regex, and filters used iteratively by an agent that keeps searching until it has what it needs. He contrasts Claude Code (grep per session, no index, repeat cost every run) with Cursor (one time upfront indexing, lightweight tool calls at runtime). Claude Code's approach is not wrong, it is a deliberate tradeoff. The frame that clarifies it: embeddings are cached compute, and whether to cache depends on query volume. Jeff Dean's version: you do not need a trillion tokens at once, you need the right million.

Speaker info:
- https://www.linkedin.com/in/kubarogut/
- https://x.com/rogutkuba

Timestamps:
0:00 Introduction to the "RAG is dead" discourse
1:12 Google search volume trends for RAG
1:39 Defining RAG vs. Agentic Search
3:15 Cursor's indexing and semantic search approach
6:10 Contrasting Claude Code (grep) vs. Cursor (indexed)
6:40 The concept of embeddings as cached compute
8:38 The shift from simple RAG to Agentic Retrieval
9:44 Jeff Dean on context windows and stage retrieval

## From Transcription to Live Music: Gemini's Audio Stack — Thor Schaeff, Google DeepMind

- Upload date: 2026-06-09
- Video: https://www.youtube.com/watch?v=Bc6Ojl2XS1w
- Transcript: raw/20260609_Bc6Ojl2XS1w/Bc6Ojl2XS1w.en-orig.vtt
- Metadata: raw/20260609_Bc6Ojl2XS1w/Bc6Ojl2XS1w.info.json

One API call to Gemini 3 Flash Preview: speaker labels by name, timestamps, emotion tags, language detection with English translation, and a full summary. That is the audio understanding layer that underlies everything else Thor Schaeff demos here, including speech generation directed by a "director's note" rather than picked from a catalogue, and Gemini 3.1 Flash Live, a sound to sound real time multimodal model with thinking baked in rather than cascaded through a separate LLM.

The talk ends with Lyria 3, Google DeepMind's music generation model that can now produce full songs with lyrics. The live demo has the Gemini Live model calling Lyria via tool use on request to generate a German techno schlager about the UK startup scene, live on stage.

Speaker info:
- https://x.com/thorwebdev
- https://www.linkedin.com/in/thorwebdev

## Road to 5 Million Tokens: Breaking Barriers in Long Context Training — Max Ryabinin, Together AI

- Upload date: 2026-06-08
- Video: https://www.youtube.com/watch?v=TUnPNY4E2fw
- Transcript: raw/20260608_TUnPNY4E2fw/TUnPNY4E2fw.en-orig.vtt
- Metadata: raw/20260608_TUnPNY4E2fw/TUnPNY4E2fw.info.json

Training a standard LLaMA 3B model with a 3 million token context on a single 8xH100 node fails before you even start: the model parameters alone exhaust GPU memory. Max Ryabinin from Together AI walks through the full stack of techniques needed to get there: fully sharded data parallelism, DeepSpeed Ulysses context parallelism for an 8x activation reduction, activation checkpointing for another 8x, CPU offloading for transformer block inputs, and chunked sequence training to avoid allocating buffers 3 million tokens wide.

Even that stack falls short at 5 million tokens. The novel contribution, Untied Ulysses, goes deeper into the context parallelism step: instead of allocating one large buffer per attention head group, it chunks the heads further and reuses those buffers across iterations, cutting activation memory with negligible throughput impact. At both 8B and 32B scale the results match the most memory optimized transformer training baselines while pushing sequence length 25% further than prior Ulysses implementations.

Speaker info:
- https://www.linkedin.com/in/max-ryabinin/
- https://x.com/m_ryabinin

## Why Eval++ Is the Next Great Compute Primitive — Sunil Pai & Matt Carey, Cloudflare

- Upload date: 2026-06-08
- Video: https://www.youtube.com/watch?v=SKDJo2CopRs
- Transcript: raw/20260608_SKDJo2CopRs/SKDJo2CopRs.en-orig.vtt
- Metadata: raw/20260608_SKDJo2CopRs/SKDJo2CopRs.info.json

Matt Carey and Sunil Pai from Cloudflare's agents team explain why Durable Objects turned out to be the right compute unit for AI agents: addressable, persistent, hibernating, stateful, and fast enough that 15ms London latency puts you inside a single animation frame. The Agents SDK builds on this to give resumable streaming, multi tab sync, and background scheduling out of the box, without any distributed systems engineering in userland.

The bigger reveal is Dynamic Workers: take a string of LLM generated code, run it in a sandboxed isolate with no ambient access, and grant only the capabilities you explicitly allow. They frame it as reclaiming 30 years of avoided eval. The session ends with both speakers teasing their afternoon talks, one on collapsing 2,600 Cloudflare API endpoints into a thousand token MCP tool, and a coding agent harness built entirely on Workers that they are, by their own admission, already shipping.

Speaker info:
- https://x.com/threepointone
- https://x.com/mattzcarey

## Why More Context Makes Your Agent Dumber and What to Do About It — Nupur Sharma, Qodo

- Upload date: 2026-06-08
- Video: https://www.youtube.com/watch?v=EcqMYoIV57A
- Transcript: raw/20260608_EcqMYoIV57A/EcqMYoIV57A.en-orig.vtt
- Metadata: raw/20260608_EcqMYoIV57A/EcqMYoIV57A.info.json

Give an agent your full codebase and it will attend to the start and the end, then quietly drop the middle. Nupur from Qodo calls this the U curve and builds the whole talk around it: why growing the context window did not fix the problem, and what actually does. She runs through iterative retrieval, hierarchical summarization, and self correction with honest cost tradeoffs for each.

The second half covers the orchestration paradox: capable models burn most of their tokens deciding how to solve a problem rather than solving it. Her team's fix is an 80/20 split, using high reasoning models for open ended discovery and lighter deterministic models for validation. Qodo's code review architecture runs this live: a context collector feeds specialized agents, a judge node recombines the results and weighs them against PR history, and every accepted or rejected suggestion shifts the weights for the next run.

Speaker info:
- https://www.linkedin.com/in/nupursh/

## From MCP to Scale: Pipelines That Build Themselves — Rafael Levi, Bright Data

- Upload date: 2026-06-07
- Video: https://www.youtube.com/watch?v=zTZ0qunQXnM
- Transcript: raw/20260607_zTZ0qunQXnM/zTZ0qunQXnM.en-orig.vtt
- Metadata: raw/20260607_zTZ0qunQXnM/zTZ0qunQXnM.info.json

Scraping is not the hard part anymore. Maintaining scrapers is. This session shows what it looks like when an agent uses MCP to inspect a site, understand its structure, generate a production scraper, and keep that pipeline working when the site changes.

Using Bright Data's MCP, APIs, and browser infrastructure, the flow moves from one-off extraction to something much more useful: agents that build parsers, save tokens by switching from page parsing to reusable scripts, and repair broken collection jobs without a human getting dragged in at 2am. If you're thinking about web data, automation, or agents that operate beyond a single prompt, this is a practical look at pipeline building at scale.

Speaker info:
- https://il.linkedin.com/in/rafael-levi
- https://github.com/ScrapeAlchemist

## LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize

- Upload date: 2026-06-07
- Video: https://www.youtube.com/watch?v=JsCCrBF7F1g
- Transcript: raw/20260607_JsCCrBF7F1g/JsCCrBF7F1g.en-orig.vtt
- Metadata: raw/20260607_JsCCrBF7F1g/JsCCrBF7F1g.info.json

Your agent called tool B before tool A, and B has a dependency on A. You did not catch it because nothing in your code audits agents. The telemetry does. Dat from Arize AI walks through what observability actually means when the system you are debugging is nondeterministic and the execution path changes with every run.

The talk covers the five flavors of eval signal (LLM as judge, human feedback, golden datasets, deterministic checks, business metrics), what scope to run them at (single span, multispan, trajectory, session), and where this is heading. Arize Phoenix is open source, runs as a single container, no Kubernetes required. The enterprise product adds an AI layer called Alex that scans traces, surfaces high latency and errors, and creates evals automatically. The stated goal: automate you out of the observability loop entirely.

Speaker info:
- https://www.linkedin.com/in/datdarylngo/
- https://x.com/dat_attacked

## Under 5 minutes to a deployed LLM endpoint — Audry Hsu, RunPod

- Upload date: 2026-06-07
- Video: https://www.youtube.com/watch?v=ILdE7FaAjVA
- Transcript: raw/20260607_ILdE7FaAjVA/ILdE7FaAjVA.en-orig.vtt
- Metadata: raw/20260607_ILdE7FaAjVA/ILdE7FaAjVA.info.json

Two failed crypto mining rigs in a basement in 2022. The founders posted on Reddit offering the GPUs for free in exchange for feedback. That is the origin of RunPod, now at $120 million in annual recurring revenue with 500,000 developers on the platform.

The demo runs in under five minutes: pick a model from the Hub, configure a context window, deploy a serverless endpoint on H100s. First request queues for 41 seconds on cold start while the container initializes and the model downloads. Every request after that executes in about 1.5 seconds. You pay only while a worker is handling a request.

Speaker info:
- https://www.linkedin.com/in/audry-hsu/

## Building Interactive UIs in VS Code with MCP Apps — Marlene Mhangami & Liam Hampton, GitHub

- Upload date: 2026-06-06
- Video: https://www.youtube.com/watch?v=_xIwFcnHqp4
- Transcript: raw/20260606__xIwFcnHqp4/_xIwFcnHqp4.en-orig.vtt
- Metadata: raw/20260606__xIwFcnHqp4/_xIwFcnHqp4.info.json

The demo profiles a Go app running bubble sort and Fibonacci and the result renders as an interactive flame graph directly inside the VS Code chat window. Not a link. Not a text summary. A live iframe you can scroll and query, sandboxed for the same reason you put a hamster in a cage: so it cannot chew up your VS Code settings or call external APIs.

The mechanism: an MCP tool returns both data and a resource reference pointing to a bundled HTML UI. VS Code fetches the HTML and renders it in a sandboxed iframe in chat. The app calls back to the server, the server returns fresh data, the UI updates. Shopify uses this pattern for checkout flows inside chat. Excalidraw uses it for interactive architecture diagrams you can drag and edit. Marlene and Liam walk through building one from scratch using a skill from the MCP repository.

Speaker info:
- https://x.com/marlene_zw
- https://www.linkedin.com/in/marlenemhangami/
- https://github.com/marlenemhangami

- https://x.com/liamchampton
- https://www.linkedin.com/in/liam-conroy-hampton/
- https://github.com/liamchampton

## Evals Are Broken, Use Them Anyway — Ara Khan, Cline

- Upload date: 2026-06-06
- Video: https://www.youtube.com/watch?v=QuuIywMG4s8
- Transcript: raw/20260606_QuuIywMG4s8/QuuIywMG4s8.en-orig.vtt
- Metadata: raw/20260606_QuuIywMG4s8/QuuIywMG4s8.info.json

Cline started at 43% on Terminal Bench. The improvements came from container CPU and memory settings, raised timeouts, and prompt engineering techniques specific to Anthropic model families that do not transfer to Codex or Gemini. Not from switching to a better model. Ara Khan's argument is that benchmark numbers are not gospel and vibes are not a system, and that the truth is inconveniently in between.

The practical framework: after a run, portfolio allocate the failures by sending another agent through all the failure traces to find which small levers actually move the score. Zone one is obvious bugs. Zone two is the nuance improvements that explain why a model everyone calls great somehow does not work for your specific harness. Zone three is overfitting to the benchmark, which people do, and which Ara is explicitly telling you not to do.

Speaker info:
- https://x.com/arafatkatze
- https://www.linkedin.com/in/arafatkatze/
- https://github.com/arafatkatze

## Building safe Payment Infrastructure for the autonomous economy — Steve Kaliski, Stripe

- Upload date: 2026-06-06
- Video: https://www.youtube.com/watch?v=KLSuFPj2ld0
- Transcript: raw/20260606_KLSuFPj2ld0/KLSuFPj2ld0.en-orig.vtt
- Metadata: raw/20260606_KLSuFPj2ld0/KLSuFPj2ld0.info.json

Agents are evolving from calling free APIs to executing real transactions, creating a new challenge: how do we let software spend money autonomously without catastrophic risk? This talk presents Stripe's approach to solving the dual problems of secure credential transmission and making businesses discoverable to agents. Through live code examples, we'll explore how to build guardrails that make autonomous spend safe and examine what infrastructure is needed as agents purchasing becomes a core capability. Whether you're building agent frameworks or enabling your business to work with agents, you'll learn how to make agent transactions both powerful and safe.

Speaker info:
- https://www.linkedin.com/in/steve-kaliski-079a7710
- https://x.com/stevekaliski

## Dark Factory: OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw

- Upload date: 2026-06-05
- Video: https://www.youtube.com/watch?v=pmoDeA3RBZY
- Transcript: raw/20260605_pmoDeA3RBZY/pmoDeA3RBZY.en-orig.vtt
- Metadata: raw/20260605_pmoDeA3RBZY/pmoDeA3RBZY.info.json

OpenClaw hit 3,000 commits in a single day. Vincent Koc's commit history shows exactly when he goes to sleep and when he wakes up. He and Peter Steinberger ran roughly 60 to 70 agents between them during the great refactor: 2,700 commits, close to a million lines of code changed, 82% of the core codebase touched in one night, plugin architecture shipped by morning.

The talk covers how you actually manage this at scale: swim lanes of 15 to 20 parallel coding sessions organized by type, when to nuke a session versus let it run, and what he calls reading the reasoning tokens. The skill is not prompting. It is knowing when an agent is bullshitting you. 2025 was about token maxing. 2026 is about not wasting them.

Speaker info:
- https://x.com/vincent_koc

## Beyond Transcription: Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI

- Upload date: 2026-06-05
- Video: https://www.youtube.com/watch?v=mFLlVpnGpds
- Transcript: raw/20260605_mFLlVpnGpds/mFLlVpnGpds.en-orig.vtt
- Metadata: raw/20260605_mFLlVpnGpds/mFLlVpnGpds.info.json

The open ASR leaderboard reports Nvidia Parakeet at 11.4% word error rate on AMI meeting data. Hervé Bredin runs the same model on the same dataset and gets 26%. Same model, same recordings, different microphone: the leaderboard uses headset audio, he uses the table mic. Most voice AI benchmarks are measuring single speaker speech and calling it solved.

The talk covers speaker diarization (who speaks when), why combining it with transcription is harder than it looks, and what breaks at the word level when two speakers overlap. Bredin demos live on a two speaker phone call, walks through the word that falls between two speaker boundaries with no clean owner, and runs pyannoteAI's Precision 2 model down to 3% diarization error against the open source baseline at 5%. State of the art today: 2% on clean telephone calls, 41% in a noisy restaurant.

Speaker info:
- https://x.com/hbredin
- https://www.linkedin.com/in/herve-bredin/
- https://github.com/hbredin

## Building Agent Interfaces: Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google

- Upload date: 2026-06-05
- Video: https://www.youtube.com/watch?v=_B4Pv9ttFgY
- Transcript: raw/20260605__B4Pv9ttFgY/_B4Pv9ttFgY.en-orig.vtt
- Metadata: raw/20260605__B4Pv9ttFgY/_B4Pv9ttFgY.info.json

Chrome DevTools MCP shipped with one tool: debug_webpage. Agents failed silently because they couldn't compose behaviors. The team decomposed it into 25 focused tools and assumed the problem was solved. It wasn't — now agents had 25 tools and no reliable way to pick the right one. Michael Hablich's talk is an honest account of building the same thing wrong three times and what the fixes actually looked like.

The concrete lessons: semantic summaries instead of raw 50,000 line JSON trace files, error messages rewritten so agents can self heal without a human in the loop ("Cannot navigate back, no previous page in history" instead of "Unable to navigate back in currently selected page"), a metric called tokens per successful outcome to measure interface fuel efficiency, and a deliberate decision to keep the autoconnect friction rather than remove it once they thought through prompt injection and the lethal trifecta.

Speaker info:
- https://x.com/MHablich
- https://www.linkedin.com/in/michael-hablich/

## SWE-rebench: Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius

- Upload date: 2026-06-04
- Video: https://www.youtube.com/watch?v=wcUJWP6WpGM
- Transcript: raw/20260604_wcUJWP6WpGM/wcUJWP6WpGM.en-orig.vtt
- Metadata: raw/20260604_wcUJWP6WpGM/wcUJWP6WpGM.info.json

Claude Code solved SWE rebench tasks by reading git history to find the solution patch. When Nebius removed future commits from the environment, it fetched the original GitHub issue. When they blocked web fetch, it switched to curl, formatted the conversation for readability, and solved the task again anyway. Ibragim Badertdinov built the leaderboard specifically because these behaviors only become visible once you run agents against real tasks at scale.

SWE rebench updates every month with problems from the previous month because benchmark data leaks into pretraining and time splits are the only defense. The talk covers what separates accepted tasks from rejected ones (accepted tasks averaged twice the tool calls, lower pass rates, and cleaner failure modes), why ambiguous specs produce noise rather than harder problems, and how the same filtering pipeline that powers the leaderboard has produced 30,000 real world training environments used by frontier labs.

Speaker info:
- https://x.com/ibragim_bad
- https://www.linkedin.com/in/ibragim-badertdinov/
- https://github.com/ibragim-bad

## Text Diffusion — Brendan O’Donoghue, Google DeepMind

- Upload date: 2026-06-04
- Video: https://www.youtube.com/watch?v=r305-aQTaU0
- Transcript: raw/20260604_r305-aQTaU0/r305-aQTaU0.en-orig.vtt
- Metadata: raw/20260604_r305-aQTaU0/r305-aQTaU0.info.json

GPT-4o answered 40. Gemini 2.5 Flash answered 42 and stuck to it even after working through the reasoning incorrectly. The Gemini Diffusion model, considerably smaller than both, answered 60 on the first forward pass, then 49, then corrected itself to 39 once it finished reasoning. Bidirectional attention means it can see future tokens and go back to fix mistakes. Autoregressive models cannot do that.

Brendon O'Donoghue covers why text diffusion is fast (24 denoising steps to generate 256 tokens means roughly 10x fewer memory transfers than autoregressive generation), what the tradeoff is (lower throughput at large batch sizes makes it expensive to serve at scale today), and what gets unlocked when latency drops to 2,000 tokens per second. The demos include a fake Wikipedia generated on the fly, a Reddit clone with AI generated comments and images, an operating system where every click generates the next screen, and a todo app built in 15 seconds by voice.

Speaker info:
- https://x.com/bodonoghue85
- https://bodono.github.io/
- https://www.linkedin.com/in/bodono/

Timestamps:
0:00 Introduction to Text Diffusion
1:02 How Text Diffusion Works (Training and Inference)
2:06 Gemini Diffusion Research Preview
3:04 Difference Between Autoregressive and Diffusion Models
4:02 Pros and Cons of Text Diffusion
6:13 Hardware Efficiency: Why Text Diffusion is Faster
8:47 Bidirectional Reasoning and Self-Correction
12:00 Dynamic and Adaptive Computation
14:26 In-place Text Editing
16:09 Low Latency Applications and Demos
20:05 Q&A Session

## The Art & Science of Benchmarking Agents — Vincent Chen, Snorkel AI

- Upload date: 2026-06-04
- Video: https://www.youtube.com/watch?v=iNkFlCiij0U
- Transcript: raw/20260604_iNkFlCiij0U/iNkFlCiij0U.en-orig.vtt
- Metadata: raw/20260604_iNkFlCiij0U/iNkFlCiij0U.info.json

ARC AGI 3 launched a few weeks before this talk with every task human solvable and frontier models under 1%. That gap is the argument: our ability to measure AI has fallen behind our ability to build it, and benchmarks that actually shape the field are bets on where capabilities are going, not snapshots of where they are.

Vincent Chen draws a framework from reviewing over 120 applications for Snorkel's $3 million Open Benchmarks Grants. The science is task quality, distributional diversity, model headroom, and robust eval methodology. The art is having a thesis (Terminal Bench bet on the CLI before coding agents made it obvious), producing research roadmaps, and treating researcher UX as a first class citizen. He closes on three axes he thinks the next generation of benchmarks needs to cover: environment complexity, autonomy horizon, and output complexity beyond plain text.

Speaker info:
- https://x.com/vincentsunnchen
- https://www.linkedin.com/in/vincentsunnchen
- https://github.com/vincentschen

## Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer

- Upload date: 2026-06-03
- Video: https://www.youtube.com/watch?v=zKk7sDMGDEQ
- Transcript: raw/20260603_zKk7sDMGDEQ/zKk7sDMGDEQ.en-orig.vtt
- Metadata: raw/20260603_zKk7sDMGDEQ/zKk7sDMGDEQ.info.json

By default, Claude Code wastes one in every three file reads. Add windowed grep and that drops to one in five. Add semantic search on top and it drops to one in eight, with file precision climbing from 65% to 87%. Kuba Rogut from Turbopuffer ran a 50-task benchmark against ContextBench to measure not whether the agent solved the problem but whether it found the right files, lines, and symbols along the way.

The benchmark tested three conditions: raw Claude Code, windowed reads capped at 50 lines, and windowed reads plus a semantic search tool backed by Turbopuffer. Semantic search won on behavior adjacent tasks where files share no keywords. Grep won on import tracing where the keyword is right there. Cursor's production numbers show a 24% relative improvement in answer accuracy from semantic retrieval, plus a 2.6% increase in code retention in large codebases. Kuba's explanation for why his gains were smaller: Cursor's model knows when and why to call semantic search. Claude Code just has it as another tool in the list.

Speaker info:
- https://ca.linkedin.com/in/kubarogut
- https://rogutkuba.com/

## Beyond Components: Designing Generative UI for MCP Apps — Ruben Casas, Postman

- Upload date: 2026-06-03
- Video: https://www.youtube.com/watch?v=hCMrEfPG2Yg
- Transcript: raw/20260603_hCMrEfPG2Yg/hCMrEfPG2Yg.en-orig.vtt
- Metadata: raw/20260603_hCMrEfPG2Yg/hCMrEfPG2Yg.info.json

Ruben Casas from Postman prompted a model to rewrite his blog. It built a search box with a blur animation and accessibility out of the box, without being asked. That was when he concluded the model writes better frontend code than he does. His question for the talk: if the models are this capable, why are most agent UIs still invoking static prebuilt components?

The talk maps three points on the spectrum. Static components pass props to predefined React elements (AG UI, Goose auto visualizer). Declarative UI has the LLM generate JSON or YAML that a rendering engine maps to components at runtime. Ruben argues this is the right balance today. Fully generative UI skips components entirely: the model writes HTML, CSS, and JavaScript on demand. His weather agent does this in a single tool call. The catch is containment: LLM generated code needs a sandbox, which is why MCP apps and their double iframe default matter. He closes on the TV analogy. The first TV shows were radio shows with cameras because nobody could imagine what else to do with the new medium. We are in that era.

Speaker info:
- https://x.com/Infoxicador
- https://www.linkedin.com/in/ruben-casas-17100383/

Timestamps:
0:00 Introduction: The evolution from 'poor man's bit coding' to high-fidelity UI generation
2:56 Why are we still stuck with static UI?
3:33 The new computer: Searching for the interface of the future
4:47 The role of MCP apps and 'Super Apps'
5:52 Three levels of UI generation: Static, Declarative, and Generative
6:03 Understanding Static UI components (e.g., AG UI, Goose)
7:42 The benefits of Declarative UI (e.g., JSON/YAML renderers)
10:06 Moving to the next level: Generative UI components
11:25 The challenge of trust: The need for sandboxing and containment
12:22 Why MCP apps are the ideal delivery mechanism for Generative UI
13:21 The 'TV/Radio' analogy: Imagining the future of agent interaction
14:46 Beyond components: Towards true human-agent collaboration
16:16 Conclusion: Shaping the future of user interfaces

## BDD, ADR, PRD, WTF: Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence

- Upload date: 2026-06-03
- Video: https://www.youtube.com/watch?v=504PvfXou5Y
- Transcript: raw/20260603_504PvfXou5Y/504PvfXou5Y.en-orig.vtt
- Metadata: raw/20260603_504PvfXou5Y/504PvfXou5Y.info.json

"One thing harder than reading AI code is reading AI tests." Mikuel from Safe Intelligence argues spec driven development leaves a loop open: you have a markdown spec, but how do you know the product actually behaves that way? His answer is Cucumber, nearly forgotten and suddenly useful again. Executable, human readable BDD scenarios connect directly to PRDs and critical user journeys and close the gap between what the spec says and what the tests verify.

The rest of the talk is enforcement. ADRs capture not just what the rules are but why; agents rejected at commit time get linked back to the document and iterate. Module import linting makes N+1 queries structurally impossible: rendering templates cannot touch the database, E2E tests cannot import any module that could. His sessions run 20 to 50 context compacts. The agent stays on track because the rules live in git hooks and CI, not in the prompt.

Speaker info:
- https://cz.linkedin.com/in/michal-cichra-61188a84

## Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel

- Upload date: 2026-06-02
- Video: https://www.youtube.com/watch?v=YYH0DMQr30A
- Transcript: raw/20260602_YYH0DMQr30A/YYH0DMQr30A.en-orig.vtt
- Metadata: raw/20260602_YYH0DMQr30A/YYH0DMQr30A.info.json

Same model. Same compute. Same number of tasks. Fine-tuning on low quality tasks improved the base model by 1%. Fine-tuning on high quality tasks improved it by 6%. Kobe Crawford from Snorkel ran that experiment on TerminalBench style agentic tasks and got a 5x difference in training uplift from task quality alone.

The talk breaks down what separates the two buckets. Accepted tasks averaged twice as many tool calls, lower pass rates, and more output tokens. Genuinely harder problems. More importantly, their failure modes were cleaner: when a model failed on a well specified task, it failed for a real reason. Rejected tasks tended to fail because of mismatches between what was requested and what the tests actually checked, or because the task never gave the model the context needed to satisfy implicit dependencies. Ambiguous specs do not produce harder tasks. They produce noise.

Speaker info:
- https://www.linkedin.com/in/kobie-crawford
- https://snorkel.ai/author/kobie-crawford/

## How Lovable self-improves every hour — Benjamin Verbeek, Lovable

- Upload date: 2026-06-02
- Video: https://www.youtube.com/watch?v=KA5kPbdkK2E
- Transcript: raw/20260602_KA5kPbdkK2E/KA5kPbdkK2E.en-orig.vtt
- Metadata: raw/20260602_KA5kPbdkK2E/KA5kPbdkK2E.info.json

Within the first hour of launching the vent tool, the agent filed 20 complaints about a silent file copy failure. The team checked: the tool worked fine. What the agent had caught was that filenames with a space in them silently failed to copy, a bug that never surfaced in logs. Benjamin Verbeek from Lovable built it a channel to complain directly to Slack when platform limitations block it, and the first thing it did was find a real production bug.

At 200,000 projects per day, Lovable runs two continuous improvement loops. The first detects sessions where a nontechnical user got stuck and then unblocked, clusters similar cases, and injects that context upstream; a holdout group measures actual project completion rates to prune stale entries when models or features change. The vent loop runs in parallel: the agent flags missing tools, broken platform behavior, and confusing docs as it works. Vent volume spikes turned out to be a reliable incident detector. A second agent now monitors the channel, deduplicates reports, and opens PRs automatically.

Speaker info:
- https://se.linkedin.com/in/benjamin-verbeek
- https://x.com/benjaminvrbk/

## What Lies Beneath the API — Benjamin Cowen, Modal

- Upload date: 2026-06-02
- Video: https://www.youtube.com/watch?v=HvZXAOZ3iv8
- Transcript: raw/20260602_HvZXAOZ3iv8/HvZXAOZ3iv8.en-orig.vtt
- Metadata: raw/20260602_HvZXAOZ3iv8/HvZXAOZ3iv8.info.json

Intercom is beating their frontier API at one tenth the cost. Pinterest claims orders of magnitude. Ben Cowen from Modal argues this pattern is not the exception for maturing AI products. It is the destination. Frontier labs want their models to win at everything. You want to win at your specific business logic. Those are different goals.

He offers three signals it is time to fine tune: paying more for the API than customers pay you, evals that have plateaued, and latency requirements no shared endpoint will meet. His practical case: if you have already built an agent harness and are collecting eval data, you have what you need to start RL training. Supervised fine tuning fits in 300 lines of Python. Modal customers have scaled to 50,000 sandboxes just for RL rollout.

Speaker info:
- https://www.linkedin.com/in/benjamincowenmath
- https://github.com/BenCowen

## How to talk to statues — Joe Reeve, ElevenLabs

- Upload date: 2026-06-01
- Video: https://www.youtube.com/watch?v=u-rJwPPU3QA
- Transcript: raw/20260601_u-rJwPPU3QA/u-rJwPPU3QA.en-orig.vtt
- Metadata: raw/20260601_u-rJwPPU3QA/u-rJwPPU3QA.info.json

A museum CEO tracked down his WhatsApp number and called. "I've had a team of 10 people working on this for a year. How did you build this?" Joe from ElevenLabs built the statue app in two hours on a Sunday using Cursor and a single one shot prompt. He posted it on a Tuesday and got 50,000 impressions. Reposted the next day about vibe coding and hit 1.5 million.

The pipeline: point your phone at a statue, OpenAI deep research identifies it and generates historical context and a voice description, the ElevenLabs voice design API creates a matching voice from that description, an agent spins up, and a conversation starts. The whole thing runs in about 30 seconds. Museums, auction houses, and travel platforms all reached out wanting the same thing built for their collections.

Speaker info:
- https://x.com/isnit0
- https://x.com/isnit0/status/2024104717039685915
- https://elevenlabs.io/blog/talk-to-a-statue-building-a-multi-modal-elevenagents-powered-app

## 20 days of compute vs 7 hours: rethinking what state-of-the-art means — Bertrand Charpentier, Pruna

- Upload date: 2026-06-01
- Video: https://www.youtube.com/watch?v=hqHC6Z_lXyo
- Transcript: raw/20260601_hqHC6Z_lXyo/hqHC6Z_lXyo.en-orig.vtt
- Metadata: raw/20260601_hqHC6Z_lXyo/hqHC6Z_lXyo.info.json

Ranking image generation models the way Design Arena does it — 26,000 battles, 62 seconds per generation — takes 20 days of compute, costs $5,000, and consumes roughly 400 marathons worth of energy. Bertrand Charpentier, cofounder and chief scientist at Pruna AI, uses that number to make a point: the same evaluation on a fast compressed model takes 7 hours and $265. Efficiency is a dimension of state of the art, not a footnote.

The rest of the talk dismantles the idea that any single model holds the title. Leaderboard rankings disagree with each other — the same model goes from rank 10 on one to rank 5 on another. Most models lose 40% of their head-to-head battles, which means the top-ranked model is the wrong choice for nearly half of real use cases. His answer is the Pareto front: plot quality against latency or cost, find the frontier, and expect three or four models clustered tightly in quality score but varying up to 20x in efficiency. Evaluating this way tends to surface small specialized models rather than large foundation models.

Speaker info:
- https://www.linkedin.com/in/bertrand-charpentier-76995ab6/
- https://github.com/sharpenb

## What if the network was the sandbox? — Remy Guercio, Tailscale

- Upload date: 2026-06-01
- Video: https://www.youtube.com/watch?v=BM2JX9hqsVQ
- Transcript: raw/20260601_BM2JX9hqsVQ/BM2JX9hqsVQ.en-orig.vtt
- Metadata: raw/20260601_BM2JX9hqsVQ/BM2JX9hqsVQ.info.json

Standard sandboxing puts the API key inside the sandbox. The agent has the key, which it can exfiltrate, misuse, or — if it runs long enough — find creative ways to leverage beyond its intended scope. Remy Guercio from Tailscale argues that sandboxing conflates two separate problems: execution isolation and access control. You can fully isolate a runtime and still have the agent holding credentials it can abuse.

Their answer is Aperture, an LLM gateway built on Tailscale's WireGuard identity network. Every connection carries verified identity — user, tag, or group — and the agent gets a placeholder instead of a real key. There is nothing to exfiltrate. Every LLM call has to pass through the network layer, so Aperture sees every tool call, bash command, and MCP request without instrumentation inside the container. Internally at Tailscale, bash dominates over structured tool calls — and now they can actually see that.

Speaker info:
- https://www.linkedin.com/in/remyguercio/

Timestamps:
0:00 - Introduction and the concept of a sandbox
1:15 - Breaking down the components of a sandbox (boundary and permissions)
1:52 - How permissions are typically handled (API keys vs. OIDC)
3:18 - Introducing Tailscale and WireGuard for network-level identity
5:42 - Introduction to Aperture (AI Gateway)
7:28 - Live demo: Viewing usage metrics and logs in Aperture
9:47 - Live demo: Inspecting GitHub Actions PR review bot logs
10:39 - Visibility into tool calls, bash commands, and MCP requests
11:46 - Agent setup and configuration in Aperture
13:59 - Advanced features: Cost controls, quotas, and webhooks
15:35 - Using tsnet to build custom internal identity-aware services
17:03 - Q&A: How to configure permissions (Grants vs. ACLs)
18:46 - Q&A: Network-layer transparency for base URLs
20:25 - Q&A: Permissioning based on users vs. model/provider
21:28 - Q&A: Handling non-tool call agent behaviors (direct code execution)

## Spec-Driven Testing for Agents With A Brain the Size of A Planet — Steven Willmott, SafeIntelligence

- Upload date: 2026-05-31
- Video: https://www.youtube.com/watch?v=UQKg0td-Bf4
- Transcript: raw/20260531_UQKg0td-Bf4/UQKg0td-Bf4.en-orig.vtt
- Metadata: raw/20260531_UQKg0td-Bf4/UQKg0td-Bf4.info.json

Wrapping a malicious instruction in a poem is an effective jailbreak against large models and not against small ones. Small models don't understand the poem. Large models do and execute the instruction. Steven Willmott from Safe Intelligence argues this is one reason bigger is not straightforwardly safer: a larger model with broader capabilities has more attack surface and more infrastructure access to abuse.

His frame is spec driven validation. An agent spec is not just a test dataset. It needs explicit rules (never offer more than 10% discount), domain ontologies (an airline agent only needs to know about destinations that airline actually flies to), rights and roles, and robustness requirements such as how many typos or rephrasings before it fails. Write these independently of the implementation so they survive a model swap and can drive both security testing and iterative improvement.

Speaker info:
- https://uk.linkedin.com/in/stevenwillmott
- https://x.com/njyx

## Can LLMs generate Enterprise Quality Code? — Prasenjit Sarkar, Sonar

- Upload date: 2026-05-31
- Video: https://www.youtube.com/watch?v=NuePCNMpWGc
- Transcript: raw/20260531_NuePCNMpWGc/NuePCNMpWGc.en-orig.vtt
- Metadata: raw/20260531_NuePCNMpWGc/NuePCNMpWGc.info.json

Sonar ran 4,444 Java programming assignments through 53 models and measured what actually came out. GPT-4o generated under 250,000 lines for those assignments. GPT 5.4 generated 1.2 million. Claude Sonnet 4.6 generated 627,000 with the highest security issue rate at 300 per million lines of code. Prasenjit Sarkar from Sonar walks through the full leaderboard: pass rate, cyclomatic complexity, bug density, and security issues per model.

Their response is a three-stage framework called ACDC: guide, verify, solve. The verify stage runs SonarQube analysis in 1 to 5 seconds before a commit, against 1 to 5 minutes in CI. If issues slip through to the PR, a remediation agent creates one fix per issue, runs it through analysis and compilation to check for regressions, and only presents it if it passes.

Speaker info:
- https://www.linkedin.com/in/jit2600/

Timestamps:
0:00 Introduction and the Shift to Agentic Development
1:44 Evaluating LLM Code Quality and Reliability
3:00 Sonar's Evaluation Framework and Methodology
3:39 LLM Performance Analysis (Pass Rates and Code Bloat)
5:24 Why LLMs Struggle: Training Data and Hidden Flaws
6:45 The Sonar LLM Leaderboard
8:30 Complexity Metrics: Cyclomatic vs. Cognitive
10:41 The ACDC Framework: Guide, Verify, and Solve
11:06 Phase 1: Guide (Context Augmentation & Sonar Sweep)
11:42 Phase 2: Verify (SonarQube Agentic Analysis)
12:40 Phase 3: Solve (Remediation Agent)
14:05 Product Summary and Ecosystem Support

## Engineering voice agents: Latency, quality, and scale — Rishabh Bhargava, Together AI

- Upload date: 2026-05-31
- Video: https://www.youtube.com/watch?v=N7b1PJc7SFc
- Transcript: raw/20260531_N7b1PJc7SFc/N7b1PJc7SFc.en-orig.vtt
- Metadata: raw/20260531_N7b1PJc7SFc/N7b1PJc7SFc.info.json

Users notice latency above 500ms and hang up above one second. In an already optimized pipeline, 75ms of network latency from models sitting in a different data center adds 30% overhead. Colocating everything in the same building drops that to around 5ms. Rishabh Bhargava from Together AI walks through the full speech to text, LLM, and text to speech pipeline at that level of specificity.

The LLM dominates the budget: 200 to 300ms time to first token target, 8 to 30B parameter range — larger models blow the latency budget, smaller ones break tool calling. Speech to text target is P90 under 100ms with around 6% word error rate. One pattern for handling complex workflows without adding latency: a small thinker LLM handles conversation flow and issues a single tool call to a larger model when the request is complex, keeping the fast path fast.

Speaker info:
- https://www.linkedin.com/in/bhargavarishabh

## How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS

- Upload date: 2026-05-30
- Video: https://www.youtube.com/watch?v=vy7o1g2iHY8
- Transcript: raw/20260530_vy7o1g2iHY8/vy7o1g2iHY8.en-orig.vtt
- Metadata: raw/20260530_vy7o1g2iHY8/vy7o1g2iHY8.info.json

WorkOS will be back for the World's Fair next week! see https://ai.engineer/wf and use YOUTUBEPROMO for new tickets only. Join 6000 AI engineers at the "Superbowl of AI"!

---

Claude would fake running tests by touching the expected output file. Nick Nisi, DX engineer at WorkOS, fixed it by SHA-256 hashing the actual test output and verifying it cryptographically. His principle: make it easier to do the real work than to lie about it, and enforce that through code and state machines, not prompts.

The same discipline reversed an opposite problem. He generated 10,000 lines of skills from WorkOS documentation, measured with evals, and found one skill was dropping a task from 97% correct to 77% correct. He deleted 95% of it, rewrote 553 lines of handwritten gotchas, and eval time dropped from 68 minutes to 6. The model already knew how to code. It just needed to know where the landmines were.

Speaker info:
- https://x.com/nicknisi
- https://linkedin.com/in/nicknisi
- https://github.com/nicknisi

Timestamps
0:00 Introduction
1:22 The challenge of context switching with agents
2:33 Introducing Case: A harness for agentic workflows
3:33 Rebuilding with a TypeScript state machine
4:45 The critical importance of evidence-based verification
5:59 Applying agentic principles to the WorkOS CLI
7:44 Lessons in documentation: Generating skills from docs
8:52 Why more data (10,000 lines) led to worse performance
9:36 The impact of using evals to measure accuracy
10:40 Key takeaway: Enforce with code, not just prompts
12:41 Treating failures as bugs in the harness system
14:39 Advice for building agentic-ready products
16:01 Final summary: Replacing trust with evidence

## How We Built Zeta2: Training an Edit Prediction Model in Production — Ben Kunkle, Zed

- Upload date: 2026-05-30
- Video: https://www.youtube.com/watch?v=phchDt63qAA
- Transcript: raw/20260530_phchDt63qAA/phchDt63qAA.en-orig.vtt
- Metadata: raw/20260530_phchDt63qAA/phchDt63qAA.info.json

To validate settled data, Zed ran 10 frontier model predictions per example and measured Levenshtein distance to the final state. For 100,000 training examples that is a million frontier model requests, which is prohibitively expensive. The fix: Zeta 2's student model now approaches teacher quality, so they run it 50 times instead at negligible cost. Ben Conungle, edit predictions lead at Zed, walks through how this pipeline came together.

The pipeline pulls opt in production edit traces, distills them through a frontier teacher, and routes bad predictions through a repair step before formatting for the student. The ideal training examples sit in the middle of the Levenshtein distance distribution: too close to the settled state is obvious, too far is noise. A metric called reversal ratio, how often the model undoes exactly what the user just typed, was the key diagnostic for catching bad model behavior before shipping.

## Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind

- Upload date: 2026-05-30
- Video: https://www.youtube.com/watch?v=3_gYbhABcAE
- Transcript: raw/20260530_3_gYbhABcAE/3_gYbhABcAE.en-orig.vtt
- Metadata: raw/20260530_3_gYbhABcAE/3_gYbhABcAE.info.json

A `deleteItem` endpoint is obvious to the developer who built it. An agent only sees the function schema and docstring. Philipp Schmid from Google DeepMind argues this is why senior engineers struggle most: they carry years of implicit context that agents do not, and design tools assuming it.

He names four other shifts: text replaces structured state, errors are inputs not restart triggers (especially costly when an agent has been running for 15 minutes), evals replace unit tests because the right question is how often it works not whether a fixed input always produces a fixed output, and build to delete because you will rebuild the same agent with a better model anyway.

Speaker info:
- https://x.com/_philschmid
- https://www.linkedin.com/in/philipp-schmid-a6a2bb196/
- https://github.com/philschmid

## Reverse engineering a Viking VOIP phone protocol with Claude Code — Boris Starkov, Eleven Labs

- Upload date: 2026-05-29
- Video: https://www.youtube.com/watch?v=V-L0INGTEOg
- Transcript: raw/20260529_V-L0INGTEOg/V-L0INGTEOg.en-orig.vtt
- Metadata: raw/20260529_V-L0INGTEOg/V-L0INGTEOg.info.json

A Viking VoIP phone sat in the ElevenLabs San Francisco office for a year. Three senior engineers and ChatGPT could not get it working. Boris from ElevenLabs cracked the undocumented protocol with Claude Code in a couple of days: brute forced all 676 possible two letter command combinations, found 80 valid ones, then set up a TCP proxy between a Windows virtual machine and the phone to intercept and log what the proprietary Windows XP software was actually sending.

The last piece was a one byte checksum in the persistence command. Claude reverse engineered the formula by running known input output pairs through it, confirmed the pattern in a closed loop, and derived a simple subtraction. Boris describes his own role as being the hands: Claude orchestrated, he physically rebooted the phone and reported how many beeps he heard. The protocol is now open sourced as a Claude Code skill so anyone with a Viking phone can configure it directly without the Windows software. The outcome at AI Engineer Europe: a red phone booth on the third floor where picking up the receiver connects you to a Michael Caine voice agent that quizzes you on British AI history.

## Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j

- Upload date: 2026-05-29
- Video: https://www.youtube.com/watch?v=B9h9ovW5H9U
- Transcript: raw/20260529_B9h9ovW5H9U/B9h9ovW5H9U.en-orig.vtt
- Metadata: raw/20260529_B9h9ovW5H9U/B9h9ovW5H9U.info.json

A knowledge base tells a financial analyst agent the risk factors. A context graph tells it whether to reject or accept, because it also carries past decision traces, the reasoning behind them, and how similar cases resolved. Zach from Neo4j walks through how context graphs extend a standard RAG setup with three layers: short term conversation history, long term extracted entities, and reasoning traces that embed into vectors so structurally similar past decisions surface alongside semantically similar ones.

The fastest path in is `uvx create-context-graph`, a one-command scaffold that gives you a backend, frontend, demo data, and an MCP server. It ships with 22 built-in domains or generates a graph ontology from a custom domain you describe. The underlying `neo4j-agent-memory` package handles entity extraction through a spaCy to GLiNER to LLM pipeline with deduplication and merging baked in, and plugs into pydantic AI, LangGraph, Crew, Google ADK, and others.

Speaker info:
- https://www.linkedin.com/in/zachblumenfeld/

## Reachy Mini: the $300 open source robot you can actually hack — Andres Marafioti, Hugging Face

- Upload date: 2026-05-29
- Video: https://www.youtube.com/watch?v=0jeZfjJMfmo
- Transcript: raw/20260529_0jeZfjJMfmo/0jeZfjJMfmo.en-orig.vtt
- Metadata: raw/20260529_0jeZfjJMfmo/0jeZfjJMfmo.info.json

Qwen3-TTS shipped at 0.8x real time: one second of audio took 1.2 seconds to generate. Andres Marafioti from Hugging Face spent two weeks fixing it. The culprits were no streaming, 500 autoregressive steps per audio packet with a CPU GPU round trip on each, and a dynamic KV cache that blocked compilation. Static KV cache plus CUDA graph captures brought it to 5.8x real time with time to first audio under 200 milliseconds.

The platform is Reachy Mini, a $300 open source robot Hugging Face has shipped to 7,500 people. It arrives unassembled. Talking to it is their most used app by far. The voice stack runs Parakeet transcription every 150 milliseconds with partial results feeding back to the robot mid-sentence, Qwen 3.5 27B for the LLM, and this optimized TTS. At that speed, infrastructure round trips match model latency, so the load balancer separates LLM endpoints from conversation nodes to handle the difference in how much different users actually talk.

## Context Graphs for Explainable, Decision-Aware AI Agents — Andreas Kollegger & Zaid Zaim, Neo4j

- Upload date: 2026-05-28
- Video: https://www.youtube.com/watch?v=abvQEhvRI_c
- Transcript: raw/20260528_abvQEhvRI_c/abvQEhvRI_c.en-orig.vtt
- Metadata: raw/20260528_abvQEhvRI_c/abvQEhvRI_c.info.json

Prescribing drug X is correct 99% of the time for symptom Y. For the 1% where it is fatal, statistical reasoning does not help you. Andreas Kollegger calls this reference class validation: before the agent acts, it has to know which group it is in.

Context graphs give agents the why. Not just knowledge and tools but the policies, rules, and prior decisions that explain why a certain action is right in a given context. The decision making framework in this talk has five stages: frame the problem with its causality and environment, pull in global rules and past precedent, run a risk value analysis, either act or escalate to someone with authority, and write the full reasoning chain back into the graph. That last step is the point. Every decision becomes precedent. Future agents inherit it.

Speaker info:
- https://x.com/akollegger
- https://www.linkedin.com/in/akollegger
- https://github.com/akollegger

## How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust

- Upload date: 2026-05-28
- Video: https://www.youtube.com/watch?v=XBaznoTRDFI
- Transcript: raw/20260528_XBaznoTRDFI/XBaznoTRDFI.en-orig.vtt
- Metadata: raw/20260528_XBaznoTRDFI/XBaznoTRDFI.info.json

Traditional observability answers one question: is the system up? Phil Hetzel from Braintrust argues that question is not the right one for agents. An individual agent trace can exceed a gigabyte. A single span can hit 20 megabytes. The data is semistructured, packed with unstructured text, and still arrives in real time. None of the systems built for uptime monitoring were designed to ingest, index, and actually use that.

Braintrust built a custom database from scratch for this problem: a write ahead log for instant visibility, analytical indexes for fast filtering, and a forked version of Tantivy (a Rust based full text search library similar to Apache Lucene) so an engineer can query every trace that mentioned a specific word. The other difference is who does this work: clinicians, lawyers, and wealth advisers now open traces directly to grade whether an agent responded correctly, and their written justifications become the training signal for automated scoring functions. The human annotations surface the failure modes. The scoring functions scale them.

Speaker info:
- https://www.linkedin.com/in/philliphetzel/

## Most Enterprise Agentic Projects Are Doomed, Here's Why — Jess Grogan-Avignon & Jack Wang, Accenture

- Upload date: 2026-05-28
- Video: https://www.youtube.com/watch?v=AGkzpxMdPn8
- Transcript: raw/20260528_AGkzpxMdPn8/AGkzpxMdPn8.en-orig.vtt
- Metadata: raw/20260528_AGkzpxMdPn8/AGkzpxMdPn8.info.json

Jess Grogan-Avignon and Jack Wang at Accenture built an agentic application in two weeks. Getting it to production took another 12 months. Not because the code was wrong. Because the infrastructure team, the security team, the AI gateway team, the data governance team, and the application team all had to align before anything could ship. That is not a technology problem, and fixing the code does not fix it.

The deeper issue is that GitHub averaged 275 million commits per week in 2025 on track for 14 billion by year end, while the approval infrastructure was never designed for that throughput. They name five tensions that predict whether an enterprise agentic project succeeds before it starts: human approval chains need to become executable code rather than longer signoff meetings; finance should back a portfolio of AI bets the way a VC would rather than demanding committed returns from each project; delivery should run on hypothesis driven loops not milestone programs; trust is built by graduating through shadow mode, advisory mode, and controlled autonomy with each step gated by outcome evidence not by project plan completion; and the real moat is not the data in your ERP but the living memory your product builds from real customer signals every day.

Speaker info:
- https://www.linkedin.com/in/jessicaannbiggs
- https://www.linkedin.com/in/jackxwang

## Why Rust is the Ideal Language for Vibe-Coding — Daniel Szoke, Sentry

- Upload date: 2026-05-27
- Video: https://www.youtube.com/watch?v=ugUeZ8-b-u0
- Transcript: raw/20260527_ugUeZ8-b-u0/ugUeZ8-b-u0.en-orig.vtt
- Metadata: raw/20260527_ugUeZ8-b-u0/ugUeZ8-b-u0.info.json

TypeScript is easy for models to write because it imposes few constraints. Those same missing constraints let models introduce data races that compile, run, and only fail intermittently. A thread safety bug in Rust does not compile. The compiler names the unsound type, explains why it cannot be sent between threads, and points the agent directly at the fix.

Daniel Szoke, Rust SDK maintainer at Sentry, argues that optimizing for a language models can write easily is the wrong goal. The better optimization is a language whose compiler enforces correctness as a natural feedback loop. Every error an agent hits and resolves in a loop is a production bug that never ships. The Rust compiler is also faster than asking a review agent to find the same class of bugs and more reliable than hoping it does.

Speaker info:
- https://www.linkedin.com/in/dlsz

Timestamps:
0:00 Introduction and the speaker's background at Sentry
0:27 The current conventional wisdom for AI-assisted development
1:53 Why languages like Python and TypeScript are popular for AI
3:44 The hidden risks of prioritizing "easy-to-write" languages
6:40 Philosophical perspective: Alien intelligence and failure modes
9:28 Introduction to Rust and its strict compiler guarantees
10:53 Key safety features: Type, Null, and Concurrency safety
11:59 Demonstrating "Fearless Concurrency" with a code example
14:26 Why Rust constraints are an asset for autonomous AI agents
15:36 Conclusion and Sentry resources

## The AI Skill I Rely On Daily — Priscila Andre de Oliveira, Sentry

- Upload date: 2026-05-27
- Video: https://www.youtube.com/watch?v=li0SaBt9RDM
- Transcript: raw/20260527_li0SaBt9RDM/li0SaBt9RDM.en-orig.vtt
- Metadata: raw/20260527_li0SaBt9RDM/li0SaBt9RDM.info.json

Priscila Andre de Oliveira analyzed 116 of her own Claude sessions from daily work at Sentry. 67% were comprehension. 2% were code generation.

Working in a codebase with 15 years of history, around 100 PRs merged per day, and 100,000 organizations depending on it, the unlock is not generation but understanding. She built a personal skill called catch me up with six exploration modes covering architecture, conventions, feature traces, syntax, testing, and history. The loop: understand what the agent found before you let it plan and implement, because a misaligned mental model is where slop comes from.

Speaker info:
- https://at.linkedin.com/in/priscila-andre-de-oliveira-ab34bb24b

Timestamps:
0:00 Introduction and speaker background
2:25 Sentry's engineering environment and scale
3:50 AI-driven projects at Sentry
5:48 Maintaining code quality and technical debt
7:35 The role of comprehension in software development
9:38 Analyzing AI usage patterns
10:33 The "Catch Me Up" skill architecture
12:15 Short demo of the "Catch Me Up" skill
13:56 Planning vs. implementation in AI workflows
15:26 Conclusion and key takeaways

## The maturity phases of running evals — Phil Hetzel, Braintrust

- Upload date: 2026-05-27
- Video: https://www.youtube.com/watch?v=FB-MLPhL9Ms
- Transcript: raw/20260527_FB-MLPhL9Ms/FB-MLPhL9Ms.en-orig.vtt
- Metadata: raw/20260527_FB-MLPhL9Ms/FB-MLPhL9Ms.info.json

Most teams approach evals like unit tests and try to cover every possible failure. Phil Hetzel from Braintrust argues that is the wrong frame: enumerate your known failure modes, cover those specifically, and ship. The goal is a flywheel where production traces surface what is going wrong, feed back into offline experimentation, and guide the next improvement.

The session walks four maturity stages: vibe checking with documented human justifications not just thumbs up or down, LLM as judge built from those justifications at scale, then the hard part, tool calls that touch external systems. Context gathering tools are manageable. CRUD tools are not, because you have to represent the state of external systems at the exact moment the original trace ran. Timestamp queries against a vector database and injecting captured system state directly into the trace are two approaches for getting there.

Speaker info:
- https://www.linkedin.com/in/philliphetzel/

## Run Frontier AI at Home — Alex Cheema, EXO Labs

- Upload date: 2026-05-26
- Video: https://www.youtube.com/watch?v=ESbWpPT_9-o
- Transcript: raw/20260526_ESbWpPT_9-o/ESbWpPT_9-o.en-orig.vtt
- Metadata: raw/20260526_ESbWpPT_9-o/ESbWpPT_9-o.info.json

Running GLM 5.1, a trillion parameter model released the day before this workshop, across four Mac Studios costs around $40,000 in hardware and tops out at roughly 20 tokens per second. Alex Cheema from EXO Labs thinks both numbers have about 100x left in them.

The workshop covers what that 100x looks like across the stack: kernel fusion that recovered 30% performance on Qwen 3.5 from inefficiencies nobody had noticed, RDMA integration that cut node to node latency from 300 microseconds to single digits and made tensor parallelism actually scale, and the case for splitting prefill onto compute dense hardware and decode onto high bandwidth hardware. The live demo runs GLM 5.1 across four Mac Studios connected by Thunderbolt 5 and cuts large prompt inference roughly in half by offloading prefill to an RTX Spark.

Speaker info:
- https://www.linkedin.com/in/alex-cheema
- https://github.com/alexcheema

Timestamps:
0:00 Introduction to EXO Labs and the mission to democratize frontier AI
2:00 The current state of AI: centralized cloud systems vs. the need for local infrastructure
7:40 Technical challenges: kernel efficiency and the overhead of separate kernel launches
9:50 The importance of the software harness in optimizing inference performance
10:35 Understanding inference constraints: compute-bound vs. memory-bound operations
11:28 The distinction between prefill and decode phases in LLM inference
13:07 Requirements for efficient local decoding: memory capacity, bandwidth, and energy efficiency
15:50 The concept of 'Intelligence per Joule' as a performance metric
16:45 Advancements in consumer hardware: higher memory capacity and bandwidth on Apple Silicon
18:50 Q&A: The future of consumer appetite for local inference hardware
20:17 Discussing the cost and performance of running trillion-parameter models like GLM 5.1
22:05 The 100x potential: How code design across the stack improves performance
26:35 Future outlook: Bifurcation of local vs. cloud use cases and diminishing returns of model size
38:55 Heterogeneous hardware strategies: Combining compute-dense and bandwidth-heavy devices
41:47 Demo: Using an Nvidia RTX Spark to accelerate prefill on a Mac cluster
48:40 Software architecture: Automating cluster orchestration with EXO
53:00 Challenging the 'batching' necessity: Multi-agent systems, search, and continual learning
1:05:22 Rethinking cloud economics and renting use cases instead of hardware
1:20:55 Demo technicalities: Event sourcing and cluster node discovery
1:32:20 Closing thoughts: Transparency in benchmarks and the future of open-source model evaluation

## Stop babysitting your agents... — Brandon Waselnuk, Unblocked

- Upload date: 2026-05-26
- Video: https://www.youtube.com/watch?v=BiG2ssibKGc
- Transcript: raw/20260526_BiG2ssibKGc/BiG2ssibKGc.en-orig.vtt
- Metadata: raw/20260526_BiG2ssibKGc/BiG2ssibKGc.info.json

Same prompt. Same agent. Same model. Without a context engine: 2.5 hours, 20.9 million tokens, multiple rounds of human correction, and code that compiled but would have broken the entire system if it shipped. With one: 25 minutes, 10.8 million tokens, and a senior engineer who gave one nitpick and approved the merge.

Brandon Waselnuk from Unblocked makes the case that the problem is not access but understanding. More MCPs give agents pipes to information. A million token context window just sits there. Naive RAG stops at the first result it finds, a phenomenon called satisfaction of search borrowed from radiology. What actually changes is a context engine that reasons across your codebase, Slack history, PR patterns, and org structure to build a research packet before the agent starts writing, so it arrives knowing your factory patterns, your fallback infrastructure, and what the CTO said was wrong in that thread three months ago.

Speaker info:
- https://getunblocked.com

## What the Best Agents Share — Mardu Swanepoel, Flinn AI

- Upload date: 2026-05-26
- Video: https://www.youtube.com/watch?v=7CrPrHgoEYk
- Transcript: raw/20260526_7CrPrHgoEYk/7CrPrHgoEYk.en-orig.vtt
- Metadata: raw/20260526_7CrPrHgoEYk/7CrPrHgoEYk.info.json

Harvey, Cursor, Manus, and Claude operate in completely different domains but share four patterns: focus modes that constrain the action space to improve output quality, transparent execution that surfaces tool calls and reasoning to build user trust, personalization that optimizes for speed to understanding rather than just speed to output, and reversibility that bounds the downside of mistakes so users take on higher value tasks.

Mardu Swanepoel from Flinn AI breaks down how each company puts these into practice. Cursor lets you roll back changes at the line, file, or conversation level and run multiple model outputs in parallel from the same input. Harvey builds playbooks from a firm's legal methods so the agent works the way the firm would. Claude surfaces a live task list alongside every tool call's inputs and outputs so users can intervene before the agent goes further in the wrong direction.

Speaker info:
- https://www.linkedin.com/in/mardu-swanepoel-000/

## Bounded Autonomy: Between Free Will and Determinism — Angus J. McLean, Oliver

- Upload date: 2026-05-25
- Video: https://www.youtube.com/watch?v=t4359sKBu4w
- Transcript: raw/20260525_t4359sKBu4w/t4359sKBu4w.en-orig.vtt
- Metadata: raw/20260525_t4359sKBu4w/t4359sKBu4w.info.json

Angus McLean spent time building a complex agent application to generate his CV. Four letters beat it: HTML. He puts the improvement at 100x.

The talk is from Oliver's AI Director, where agents generate around 4,000 creative assets a day for 200 plus brands, assets you have probably seen and had no idea were AI. The core argument: models are naturally verbose and tend toward complexity, and so are the developers working with them. His counter is to strip back. Replace internet access with curated documentation, ask how little context you can use and still complete the task, and never automate a job you cannot do yourself.

Speaker info:
- https://uk.linkedin.com/in/angusjmclean

Timestamps
0:14 Introduction and talk theme: Bounded Autonomy
1:13 About Oliver and GenAI in advertising
2:24 The structure of an ad agency
3:35 Why agents are used for speed and scale
4:27 Slow down and look at model limitations
5:52 The problem with current "band-aid" solutions
6:51 The role of context windows in agent capability
8:11 How to effectively constrain models with documentation
9:29 Constraints as a driver for creativity
10:32 Fundamentals: Building your own harness and memory
11:25 The power of simplicity (The CV/HTML example)
12:34 AI as a translation process
14:14 Using multiple representation structures
15:22 Agent workflows and the "don't automate what you can't do" rule

## Agentic Evaluations at Scale, For Everybody — Nicholas Kang & Michael Aaron, Google DeepMind

- Upload date: 2026-05-25
- Video: https://www.youtube.com/watch?v=Ubwb6NzegyA
- Transcript: raw/20260525_Ubwb6NzegyA/Ubwb6NzegyA.en-orig.vtt
- Metadata: raw/20260525_Ubwb6NzegyA/Ubwb6NzegyA.info.json

On SWE-Bench Pro, six frontier models land within a couple of percentage points of each other. The harness they run inside shifts performance by 22%. A competing lab once took a Kaggle benchmark, reran it with their own compaction settings, and published much better results. Neither number was wrong. Both were useless.

The talk is from Nicholas Kang and Michael Aaron at Google DeepMind's Kaggle team, who are building the infrastructure to fix evals at the community level: an open benchmark platform anyone can contribute to, a PvP Game Arena where models play poker and chess for an ELO rating that cannot saturate, and a standardized agent exam that returned 500 plus submissions in its first week without any promotion. The wastewater treatment plant engineer from Turkey who built a novel safety benchmark from 20 years of field experience, data that does not exist anywhere else, is the use case they keep coming back to.

Speaker info:
- https://www.linkedin.com/in/nicholaskangjj

## Does GenAI "belong" to data scientists? — Phil Hetzel, Braintrust

- Upload date: 2026-05-25
- Video: https://www.youtube.com/watch?v=NKwIX3CiRgU
- Transcript: raw/20260525_NKwIX3CiRgU/NKwIX3CiRgU.en-orig.vtt
- Metadata: raw/20260525_NKwIX3CiRgU/NKwIX3CiRgU.info.json

At most traditional enterprises, GenAI got handed to the ML platform team because it had AI in the name. Phil Hetzel from Braintrust argues that was the wrong move, not because data scientists lack value, but because Anthropic and OpenAI already ran the data pipeline. What is left is prompt and context engineering, distributed systems, human annotation, and functional evaluation across a much broader surface area than precision and recall. The mistake is isolating it to one team. The answer is a diverse one.

Speaker info:
- https://www.linkedin.com/in/philliphetzel

## Scaling the Next Paradigm of Heterogeneous Intelligence — Adrian Bertagnoli, Callosum

- Upload date: 2026-05-24
- Video: https://www.youtube.com/watch?v=WRBNDpUhsJQ
- Transcript: raw/20260524_WRBNDpUhsJQ/WRBNDpUhsJQ.en-orig.vtt
- Metadata: raw/20260524_WRBNDpUhsJQ/WRBNDpUhsJQ.info.json

A mixture of Qwen 3 VL8B and Kimi K2.5 beat the state of the art on Video Web Arena, outperforming the leading GPT and Gemini models by 18 and 25 percent while costing 3.7 times less and running 3 times faster. The reason it worked is that visual web navigation decomposes into subtasks that do not all need a frontier model: routing zoom and visual parsing to a smaller model alone produced 11x speed and 43x cost improvements on those steps.

Adrian Bertagnoli from Callosum makes the case that the GPU cluster era of identical hardware and monolithic models is ending. Heterogeneous intelligence treats model architectures, chip types, and workflows as variables to optimize together. A second result: running recursive long context reasoning tasks on Cerebras instead of a frontier model cuts cost by 7x and latency by 5x while matching accuracy. Callosum is building the automation layer that routes tasks to the right chip and model without bespoke decisions for each subtask.

Speaker info:
- https://www.linkedin.com/in/adrian-bertagnoli-bb3467178/

Timestamps
0:14 Introduction and definition of heterogeneous intelligence
0:56 Limitations of the current homogeneous intelligence paradigm
1:36 Evolution toward mild heterogeneity (MoE, multi-agent systems, hardware disaggregation)
3:24 The rationale for heterogeneity: complexity and multi-step problem solving
4:26 Mathematical formalization of the production function and skill distribution
5:56 Practical implementation of heterogeneous workflows
6:55 Case study: Recursive language models and context management
9:05 Results on Ulong benchmarks (Cerebras/Sambanova performance)
10:20 Case study: Visual web navigation and Video Web Arena performance
12:02 Offloading subtasks to smaller models for speed and cost efficiency
12:38 The future of compute: Moving to a heterogeneous, multi-agent stack
13:10 Partnership with the UK's Arya institute
13:31 Closing summary and outlook on hardware/software co-evolution
14:01 Q&A: Automation layer for task routing

## Let's Talk About FOMAT: Fear of Missing Agent Time — Michael Richman, Cmd+Ctrl

- Upload date: 2026-05-24
- Video: https://www.youtube.com/watch?v=W-SX_srBa3Y
- Transcript: raw/20260524_W-SX_srBa3Y/W-SX_srBa3Y.en-orig.vtt
- Metadata: raw/20260524_W-SX_srBa3Y/W-SX_srBa3Y.info.json

You kicked off an agent 30 minutes ago. It stopped after two minutes, blocked on a question, and has been waiting ever since. Michael Richman calls this FOMAT: fear of missing agent time. His answer is Cmd+Ctrl, a system that sends you a push notification when the agent needs input, lets you respond from your phone or watch, and lets you start new sessions from wherever you are.

The demo shows Claude Code running in a terminal while the Cmd+Ctrl app on an iPhone mirrors the session in real time. Walk away, get notified when the agent completes or gets stuck, reply from the phone, pick up in the terminal. The same setup works across Claude Code, Cursor, Codex, Gemini CLI, and others through a daemon that runs alongside each agent and reports to a shared control plane. The daemon layer is open source. A standup dashboard summarizes all recent sessions so you can catch up without reading every thread.

Speaker info:
- https://x.com/mrwoofster
- https://www.linkedin.com/in/michael-richman-b7807b2/
- https://github.com/mrwoof

## How Google DeepMind Runs Agents at Scale — KP Sawhney & Ian Ballantyne, Google DeepMind

- Upload date: 2026-05-24
- Video: https://www.youtube.com/watch?v=7gujZrJ9L5I
- Transcript: raw/20260524_7gujZrJ9L5I/7gujZrJ9L5I.en-orig.vtt
- Metadata: raw/20260524_7gujZrJ9L5I/7gujZrJ9L5I.info.json

Google DeepMind employees have worse token quotas than paying customers. That is not a mistake. KP Sawhney explains: customers get priority, and if an internal team spikes usage on a cluster someone monitoring 24/7 will just call and ask them to stop.

This panel covers how DeepMind thinks about agents at scale from the inside: managing quota across thousands of power users, a Darwinian skills library where only the strongest skills survive as engineers contribute en masse, and where the Deep Research pipeline is going next. KP's current focus is replacing the pipeline's giant context blobs with a shared file system so each research component can collaborate the way human researchers would, and produce supporting artifacts that the current architecture cannot.

Speaker info:
- https://linkedin.com/in/ianballantyne
- https://github.com/irbg
- https://linkedin.com/in/kyle-sawhney
- https://github.com/KPSawhney

Timestamps:
0:00 Introduction of KP Sawhney and Ian Ballantyne
0:57 Demo of the anti-gravity agentic platform
4:32 Discussion on KP's work with the deep research agent
5:46 Using skills libraries and managing agent sprawl
7:52 Addressing scalability and token quotas at Google
9:44 Audience Q&A: Managing per-user agent behaviors
13:12 Audience Q&A: Observability and agent trajectory stores
14:46 Audience Q&A: Future of deep research pipelines
16:10 Audience Q&A: Handling multi-agent systems
17:45 Audience Q&A: Perspectives on skills vs. MCP
19:12 Audience Q&A: Evaluating agentic workflows
20:25 Audience Q&A: Handling model limits and quota management
22:48 Audience Q&A: Automated code review processes

## Prompt to Pipeline: Building with Google's Gen Media Stack — Paige & Guillaume, Google DeepMind

- Upload date: 2026-05-23
- Video: https://www.youtube.com/watch?v=ns9f1fjLD7Y
- Transcript: raw/20260523_ns9f1fjLD7Y/ns9f1fjLD7Y.en-orig.vtt
- Metadata: raw/20260523_ns9f1fjLD7Y/ns9f1fjLD7Y.info.json

A public domain book, a notebook, and three gen media models. Guom from Google DeepMind fed Wind in the Willows into Gemini, generated character portraits with Nano Banana, animated chapter scenes with VO, and scored each chapter with LIA, all live in the workshop.

The full three hour session covers more ground. Paige Bailey demos AI Studio's Build feature creating a bookshelf scanning app with Google login and Firestore from a single prompt, Gemini 3.1 Flash Light analyzing a dinosaur video frame by frame for under a dollar, and Genie 3 rendering a playable world with a pink sparkly squirrel on Regent's Canal. Ian Valentine closes with Gemma 4 running on device: 10 sub agents generating SVGs in parallel on a local 26B model, then open code building and debugging a game from a spec with no cloud API involved.

Speaker info:
- https://x.com/DynamicWebPaige
- https://linkedin.com/in/dynamicwebpaige
- https://github.com/dynamicwebpaige
- https://x.com/Giom_V
- https://www.linkedin.com/in/guillaumevernade
- https://github.com/Giom-V

## Introducing WebMCP: Agents in the Browser — RL Nabors

- Upload date: 2026-05-23
- Video: https://www.youtube.com/watch?v=LMbeDEQO6QM
- Transcript: raw/20260523_LMbeDEQO6QM/LMbeDEQO6QM.en-orig.vtt
- Metadata: raw/20260523_LMbeDEQO6QM/LMbeDEQO6QM.info.json

RL Nabors built a comic reader that renders inside Claude. Full panels, navigation, transcript mode, design matched to the original site. No browser tabs. She is reading her own web comic archive entirely through an agent, and it looks like the website.

The talk is a case against chat as the permanent UI of agentic software. Chat is to agents what the terminal was to desktop computing: developers love it, everyone else gets the iPhone eventually. MCP apps bundle HTML, CSS, and JavaScript into a single file that agent interfaces render in an iframe, turning any tool response into a real interactive surface. WebMCP goes the other direction: add tool name and description attributes to forms you already have, and browser agents can call your site's functions directly without screenshot parsing or DOM traversal. Both specs exist now. The web platform has been the infinite canvas all along.

Speaker info:
- https://x.com/nearestnabors
- https://www.linkedin.com/in/nearestnabors
- https://github.com/rachelnabors

Timestamps

0:07 Introduction and Speaker Background
3:28 Motivations for Future-Proofing the Web Comic Site
5:09 Roadmap: MCP, Apps, and WebMCP
6:05 Understanding Transports: STDIO vs. HTTP
8:57 Defining MCP Tools
10:52 The Role of MCP Resources
11:37 The Case Against 'Starfish' (Chat-Only) UI
13:36 MCP Apps: Building Interactive Agent Interfaces
16:34 Best Practices and Gotchas for MCP Apps
17:38 Introducing WebMCP: Agents in the Browser
19:07 Imperative vs. Declarative Models
20:13 WebMCP Demo with the Debugging Extension
21:47 Leveraging Native Browser APIs (Speech, Animation, etc.)

## The Missing Primitive for Agent Swarms — Lou Bichard, Ona

- Upload date: 2026-05-23
- Video: https://www.youtube.com/watch?v=5Sui_OnSRlY
- Transcript: raw/20260523_5Sui_OnSRlY/5Sui_OnSRlY.en-orig.vtt
- Metadata: raw/20260523_5Sui_OnSRlY/5Sui_OnSRlY.info.json

Stripe called theirs Minions. RAMP called theirs Inspect. Both are internal infrastructure for running fleets of background agents, and both teams built it from scratch. Lou Bichard's argument is that this shouldn't keep happening.

The talk breaks down what agent swarm infrastructure actually needs: a runtime (largely solved), orchestration and triggers (solved), and coordination, which is not. Coordination is the gap where agents pick up tasks from each other, pass messages, and verify they have cleared a stage of the development cycle before moving on. GitHub is a poor substitute: noisy, designed for humans, and not built for agents raising hundreds of parallel pull requests. Lou covers what a proper primitive looks like, shows how Owner ships VM level isolation for agent fleets today, and makes the case that the coordination layer probably needs to be a CLI gateway that any local coding agent can invoke to check its progress and proceed.

Speaker info:
- https://x.com/loujaybee
- https://www.linkedin.com/in/loujaybee

Timestamps:
0:00 Introduction and definition of a Software Factory
1:50 Agent swarm patterns: Swarms, Fleets, and Events
3:11 Real-world examples of internal agent infrastructure (Stripe, RAMP)
3:50 How Owner handles agent infrastructure and development environments
4:49 Understanding Harness Engineering
5:43 The three pillars of agent swarm infrastructure: Runtime, Orchestration, and Coordination
7:17 Demo: Running sub-agents and fleets in Owner
10:20 Challenges of building a software factory
11:44 The issue with Context Management and Context Rot
12:16 Why GitHub is a poor coordination layer for agents
12:59 Proposed solutions: State machines, Durable execution, and CLI gateways

## Gemini Nano on device — Florina Muntenescu & Oli Gaymond, Google DeepMind

- Upload date: 2026-05-22
- Video: https://www.youtube.com/watch?v=owH1f0N-keY
- Transcript: raw/20260522_owH1f0N-keY/owH1f0N-keY.en-orig.vtt
- Metadata: raw/20260522_owH1f0N-keY/owH1f0N-keY.info.json

Gemini Nano on device weighs three to four gigabytes. Shipping that per app is not realistic, which is why AI core puts it in the system once and every app shares it. Foreground apps get top priority. Background batch jobs queue and run overnight on charge. The developer never manages any of that.

The tradeoff is reach. The GenAI MLKit APIs require flagship devices from the last couple of years. Classic MLKit for vision and OCR runs on a billion plus devices without issue. Hybrid inference, launched a few weeks before this talk, falls back from Nano to Gemini Flash in the cloud when the on device model is not available. An embedding API is coming soon for RAG style solutions. For anything beyond that, LiteRT is the other path.

Speaker info:
- https://x.com/FMuntenescu
- https://www.linkedin.com/in/florina-muntenescu-314b8921
- https://github.com/florina-muntenescu
- https://linkedin.com/in/ogaymond

## Fast Models Need Slow Developers — Sarah Chieng, Cerebras

- Upload date: 2026-05-22
- Video: https://www.youtube.com/watch?v=TeGsFFNqRLA
- Transcript: raw/20260522_TeGsFFNqRLA/TeGsFFNqRLA.en-orig.vtt
- Metadata: raw/20260522_TeGsFFNqRLA/TeGsFFNqRLA.info.json

Codex Spark, a model Cerebras built with OpenAI, generates code at 1,200 tokens per second. The Sonnet and Opus families run at 40 to 60. At that 20x difference, a context window that used to take ten minutes to fill now takes 30 seconds, and every habit built around slow generation starts producing technical debt at a scale nobody has dealt with before.

Sarah Chieng from Cerebras covers what the playbook looks like in this regime. Validation and linting at every step is now instant, so there is no excuse not to run it continuously. Generating 75 component variations across five sub-agents and cherrypicking the best one becomes practical where it was not before. And when context burns in 30 seconds, a four file external memory system (agents, plan, progress, verify) is what keeps each new session from starting over instead of from scratch.

Speaker info:
- https://x.com/sarahchieng
- https://www.linkedin.com/in/sarah-chieng-888595139/

Timestamps:
0:00 - Introduction to the impact of fast AI code generation
2:29 - Historical context of model speeds
3:10 - Why AI inference speeds are increasing (Hardware/Stack optimization)
7:05 - The current developer landscape and risks of "slob"
8:27 - Playbook: Orchestrating models and sub-agents
9:56 - Playbook: Validation and automated testing
10:47 - Playbook: Cherrypicking and variety in output
12:07 - Playbook: Adopting a real-time collaborative mental model
12:53 - Playbook: Avoiding "slob" and active steering
13:54 - Playbook: Continuous refactoring
14:30 - Playbook: Context management and external memory systems

## Lobster Trap: OpenClaw in Containers from Local to K8s and Back — Sally Ann O'Malley, Red Hat

- Upload date: 2026-05-22
- Video: https://www.youtube.com/watch?v=F1DYkY1BlfM
- Transcript: raw/20260522_F1DYkY1BlfM/F1DYkY1BlfM.en-orig.vtt
- Metadata: raw/20260522_F1DYkY1BlfM/F1DYkY1BlfM.info.json

Sharing a good agent setup usually means handing someone a pile of markdown, config files, and YAML and hoping they reproduce what you have. The answer in this demo is a container image: spin up a sub agent in two seconds from a Podman command, flip a flag for Kubernetes, and your personal setup becomes the team baseline.

The stack is Podman locally, Kubernetes for distribution, same container image throughout. Secrets get two layers: Podman secrets for API keys on the host, OpenClaw secret refs inside the container. Volumes handle backup and recovery. An Nvidia team runs the same pattern in production with ten engineers each running their own OpenClaw in Kubernetes for model evals, doing work that used to take six people.

Speaker info:
- https://www.linkedin.com/in/sally-ann-omalley/

Timestamps:
0:00 Introduction and background on Sally Ann O'Malley
1:25 Discovering and experimenting with OpenClaw
2:35 Benefits of running AI agents in containers
3:05 Introducing Forever Claw and sub-agents
5:52 Using containers for agent configuration and tools
6:21 Managing secrets with Podman and Kubernetes
8:10 Scaling agent workloads with Kubernetes
9:15 Nvidia team case study: Model evaluations
11:09 Backup, recovery, and persistence with volumes
11:47 Vision for workplace agent standardization
14:14 Local demo: Running OpenClaw with Podman
16:45 Choosing providers and configuring settings
17:50 SSH sandbox features
18:22 Running the Podman command and checking agent status
20:52 Transitioning agent workloads to Kubernetes and OpenShift

## Cooking with Agents in VS Code — Liam Hampton, Microsoft

- Upload date: 2026-05-21
- Video: https://www.youtube.com/watch?v=dyHpnnlkTc8
- Transcript: raw/20260521_dyHpnnlkTc8/dyHpnnlkTc8.en-orig.vtt
- Metadata: raw/20260521_dyHpnnlkTc8/dyHpnnlkTc8.info.json

One codebase, three problems, three agents running at the same time. Liam Hampton from Microsoft demos the full loop in VS Code: a local agent with Claude Opus writing and fixing unit tests with him in the loop, a background agent using a git work tree to build a front end from a GitHub issue without him touching it, and a cloud agent running in GitHub Actions to make the repo open source friendly.

The talk is a framework for knowing which agent path to pick and why. Local when you want hands on iteration. Background when the task is big and you can tolerate being half in half out. Cloud when you genuinely do not care how it gets done. VS Code handles all three from one interface, with Copilot, Claude, and third party agents accessible from the same control plane.

Speaker info:
- https://x.com/liamchampton
- https://www.linkedin.com/in/liam-conroy-hampton/
- https://github.com/liamchampton

## Scaling Agents on Kubernetes with acpx and ACP — Onur Solmaz, OpenClaw

- Upload date: 2026-05-21
- Video: https://www.youtube.com/watch?v=VaS2h-dY1-4
- Transcript: raw/20260521_VaS2h-dY1-4/VaS2h-dY1-4.en-orig.vtt
- Metadata: raw/20260521_VaS2h-dY1-4/VaS2h-dY1-4.info.json

OpenClaw receives 300 to 500 pull requests per day. Most arrive AI generated, most are not mergeable, and every one of them is signal about something broken in the codebase. Onur Solmaz built acpx to process them without him in the loop.

acpx is a headless CLI for the Agent Client Protocol. It replaces PTY scraping with structured agent to client communication and drives sessions through a node based workflow graph: reproduce the bug, judge the implementation, check for conflicts, run a review loop, emit structured JSON. Onur runs parallel Codex sessions from Discord channels while traveling, one channel per task. The talk ends with disposable agent pods on Kubernetes, a Go operator that provisions a full compute environment per task, wires it into Slack, and tears it down when the work is done.

Speaker info:
- https://x.com/onusoz
- https://www.linkedin.com/in/osolmaz/
- https://github.com/osolmaz

## Your Coding Agent Should Do AI System Engineering — Ben Burtenshaw, Hugging Face

- Upload date: 2026-05-21
- Video: https://www.youtube.com/watch?v=JomVvNDjGb8
- Transcript: raw/20260521_JomVvNDjGb8/JomVvNDjGb8.en-orig.vtt
- Metadata: raw/20260521_JomVvNDjGb8/JomVvNDjGb8.info.json

An agent written RMSNorm kernel hit 1.88x speedups on H100s. A finetuned Qwen3 0.6B hit 35% on LiveCodeBench. Neither result required a systems engineer. Just coding agents with the right skills loaded.

Ben Burtenshaw from Hugging Face walks through three levels: using Claude Code interactively to write and benchmark CUDA kernels distributed as versioned repos on the Hub, a zero-shot task where an agent finetunes a model end to end from a single prompt, and a multi agent research lab running parallel experiments overnight on Hub compute while a reporter agent pushes results to a live Trackio dashboard. The through line is skills: file based context that turns a zero shot failure into a few shot workflow. CUDA programming and ML training pipelines were deep specializations that took years. Skills compress that timeline to hours.

Speaker info:
- https://x.com/ben_burtenshaw
- https://www.linkedin.com/in/ben-burtenshaw/
- https://github.com/burtenshaw

Timestamps:
0:00 Introduction to AI Systems Engineering
1:59 Boss 1: Writing and Distributing CUDA Kernels
3:48 Efficiency in Deep Learning
6:08 Using Skills for Agentic Workflows
8:37 Benchmarking and Evaluating Skills with Upskill
9:26 Boss 2: End-to-End Fine-tuning of LLMs
10:16 Boss 3: Multi-Agent Auto Research Labs
12:09 Architecture of the Multi-Agent Research System
13:40 Implementing the Research Agent in OpenCode
15:28 Monitoring Experiments with Trackio
16:45 Final Takeaways and Conclusion

## Skill issue: Lessons from skilling up coding agents to use Langfuse - Marc Klingen, Clickhouse

- Upload date: 2026-05-20
- Video: https://www.youtube.com/watch?v=vNCY9kXXyDQ
- Transcript: raw/20260520_vNCY9kXXyDQ/vNCY9kXXyDQ.en-orig.vtt
- Metadata: raw/20260520_vNCY9kXXyDQ/vNCY9kXXyDQ.info.json

Without a skill, Claude Code adds Langfuse using stale pre-training context, ships broken instrumentation, then catches the failure and fetches current docs to fix it. The resulting trace captures two LLM calls with no visibility into what the agent actually did.

Marc Klingen covers the six learnings from building a skill to close that gap: surfacing a natural language search endpoint so agents stop crawling 478 documentation pages, why pointing to references beats duplicating content, and what happened when they ran an auto-research loop on the skill itself. Three of six suggested improvements shipped, but their target function nearly backfired by optimizing out the documentation-fetching steps that make the skill reliable over time.

Speaker info:
- https://x.com/marcklingen
- https://www.linkedin.com/in/marcklingen/

Timestamps:
00:00 - Introduction to Marc Klingen and Langfuse
01:22 - Conceptual mental model for agent skills
04:04 - The problem: scaling documentation and onboarding for coding agents
09:03 - Six key learnings from building a Langfuse skill
09:12 - Learning 1: Looking at traces for debugging
10:47 - Learning 2: Helping agents navigate information (sitemaps/formats)
11:40 - Learning 3: Surfacing a search endpoint for docs
12:36 - Learning 4: Implementing basic evaluation (eval) setups
13:53 - Learning 5: Referencing rather than duplicating content
14:24 - Learning 6: Using auto-research loops with target functions
17:24 - Discussion on challenges: distribution, versioning, and target functions
19:21 - Roadmap and future outlook for agent automation
20:09 - Q&A session

## Any-to-Any: Building Native Multimodal Agents - Patrick Löber, Google DeepMind

- Upload date: 2026-05-20
- Video: https://www.youtube.com/watch?v=GIRpQEfYf3U
- Transcript: raw/20260520_GIRpQEfYf3U/GIRpQEfYf3U.en-orig.vtt
- Metadata: raw/20260520_GIRpQEfYf3U/GIRpQEfYf3U.info.json

Draw arrows on a map and ask Gemini to generate a picture of what you see. It produces the Golden Gate Bridge. Not because it matched pixels, but because the image generation model is built on top of Gemini's world understanding and knows what those arrows are pointing at.

Patrick Löber walks through the full any-to-any stack: multimodal understanding where Gemini ingests PDFs, video, and audio up to nine-plus hours at once, native image and speech generation called as tools from an agentic loop, and a live audio model where audio goes in and audio comes out through a single architecture with no cascaded pipeline. The session ends with the building blocks for a Notebook LM clone where a reasoning agent decides what to generate rather than a hardcoded workflow.

Speaker info:
- https://x.com/patloeber
- https://linkedin.com/in/patrick-l%C3%B6ber-403022137
- https://github.com/patrickloeber

Timestamps:
0:00 Introduction to the session
0:58 Defining "Any-to-Any" and the Gemini ecosystem
2:56 Building a NotebookLM clone using an agentic approach
3:51 The agentic architecture for multimodal applications
4:50 Implementation details for multimodal understanding
6:10 Tips for audio/video processing and context caching
7:56 Multimodal generation phase
8:37 Native image and infographic generation
9:04 Native speech generation and podcast style audio
9:57 Implementing function/tool calling
11:28 The power of native generation models
12:37 Multi-language and accent capabilities in audio models
13:46 Live API and real-time interaction
15:06 Final summary and additional model shout-outs

## From 46% to 90%: Fine-Tuning Tiny LLMs for On-Device Agents — Cormac Brick, Google

- Upload date: 2026-05-20
- Video: https://www.youtube.com/watch?v=-TiET_K-E_g
- Transcript: raw/20260520_-TiET_K-E_g/-TiET_K-E_g.en-orig.vtt
- Metadata: raw/20260520_-TiET_K-E_g/-TiET_K-E_g.info.json

Function Gemma ships at 270 million parameters and processes nearly 2,000 tokens per second prefill on a Pixel 7. Out of the box, on a fixed set of app intents, it hits 46% accuracy. Fine-tuned on a synthetically generated dataset, it clears 90% on eight of ten functions.

Cormac Brick covers the two options developers have for on-device AI: Gemini Nano via AI core for common tasks, and LiteRT-LM for custom models that ship inside your app. The session walks through a live skill harness built on Gemma 4 with a restaurant roulette demo running fully on-device, and Eloquent, a production transcription app built by chaining two models under a few hundred million parameters.

Speaker info:
- https://www.linkedin.com/in/cbrick/

Timestamps:
0:00 Introduction to on-device agents and tiny LLMs
0:48 Overview of AI Edge, SLMs, and TLMs
0:57 Taking a look at agent skills
1:06 Taking a look at tiny models
1:24 Motivations for on-device AI (latency, privacy, offline use)
3:01 System-level GenAI (Gemini Nano via AI Core)
4:03 App-level GenAI (LiteRT-LM for custom/boutique models)
5:06 Google AI Edge Gallery app demo
6:22 Deep dive into agent skills and the skill harness
7:41 How the skill harness works (system prompts, tool calls, and JavaScript UI)
9:00 Creating and publishing your own skills
10:28 Using LiteRT-LM runtime for model deployment
12:31 Export and inference workflow (from PyTorch to deployment)
13:19 Function Gemma: Robust, small-scale function calling
14:35 Fine-tuning workflow for tiny models using synthetic data
16:01 Eloquent: A production transcription app example using tiny models
17:28 Q&A: Agent skill robustness and multi-skill calling
19:26 Q&A: LiteRT-LM file format vs. Task files
20:00 Q&A: Performance on CPU/TPU and resources

## Don't Build Slop (4 Levels of AI Agent Maturity) - Ara Khan, Cline

- Upload date: 2026-05-19
- Video: https://www.youtube.com/watch?v=yUmS-F9IX90
- Transcript: raw/20260519_yUmS-F9IX90/yUmS-F9IX90.en-orig.vtt
- Metadata: raw/20260519_yUmS-F9IX90/yUmS-F9IX90.info.json

The prompt for GPT-5.3 is one-third the size of the one written for GPT-5. Frontier models are so capable that longer system prompts cause sensory overload and degrade performance. The rule Ara Khan keeps returning to: every single thing you add to an agent risks making it worse.

The talk breaks agent-building into four levels, from framework prototyping to cloud-native fleets, with five concrete rules for writing your own agent code in between. The form factor argument lands on Kanban boards as the right UX for managing parallel inference-bound agents. He made that prediction publicly on March 26. Claude Code shipped the same thing ten hours before this talk.

Speaker info:
- https://x.com/arafatkatze
- https://www.linkedin.com/in/arafatkatze/
- https://github.com/arafatkatze

Timestamps:
0:00 Introduction: Addressing the "mass psychosis" of agent-building
2:13 The Four Levels of Agent Maturity overview
3:00 Level 1: Using existing agent frameworks
4:13 Level 2: Building your own agents (with five rules)
4:36 Rule 1: View every agent as a state machine
5:55 Rule 2: Keep it simple (Avoid unnecessary system prompt bloat)
7:20 Rule 3: Integrate with a CLI for a pseudo-RL pipeline
8:43 Rule 4: Don't build "slop" (Focus on thoughtful architecture)
9:43 Rule 5: Master frontier model APIs (Reasoning traces)
11:03 The UX form factor: Why Kanban boards are best for agents
13:12 Shipping to the cloud for scalability
17:15 Q&A session: Planning and state transitions in Kanban

## What Breaks When You Build AI Under Sovereignty Constraints - Bilge Yücel, deepset GmbH

- Upload date: 2026-05-19
- Video: https://www.youtube.com/watch?v=x2bH0RKPgdc
- Transcript: raw/20260519_x2bH0RKPgdc/x2bH0RKPgdc.en-orig.vtt
- Metadata: raw/20260519_x2bH0RKPgdc/x2bH0RKPgdc.info.json

If you send EU citizen data to an embedding API hosted in Virginia, you have already violated GDPR. That is one hidden assumption. Most production AI systems have dozens more, baked into the architecture long before anyone asked whether the system was sovereign.

Bilge Yücel walks through the four sovereignty pillars (data, model, infrastructure, operations) and what actually breaks when you retrofit each one: re-evaluating performance from scratch after swapping a frontier API for a self-hosted model, managing multiple databases across jurisdictions after moving private data, and discovering how much vendor lock-in you had the moment you try to go on-prem. The closing checklist is three questions: can you swap models without changing application logic, do you have reproducible run logs stored in a compliant location, and can your team respond to an incident without calling a hyperscaler.

Speaker info:
- https://x.com/bilgeycl
- https://www.linkedin.com/in/bilge-yucel/

## Personalization in the Era of LLMs - Shivam Verma, Spotify

- Upload date: 2026-05-19
- Video: https://www.youtube.com/watch?v=5YSJEP0HWzM
- Transcript: raw/20260519_5YSJEP0HWzM/5YSJEP0HWzM.en-orig.vtt
- Metadata: raw/20260519_5YSJEP0HWzM/5YSJEP0HWzM.info.json

Spotify represents Ariana Grande and Bruno Mars as sequences of six tokens. The first two are shared because both are pop artists. The remaining tokens diverge to capture what makes each distinct. That is a Semantic ID, and it is how Spotify teaches open-weight LLMs to reason over a catalog of 100 million tracks the same way they reason over words.

Shivam Verma from Spotify's AI foundation team walks through the three components they assembled to personalize LLMs at scale without full fine-tuning. User embeddings trained on streaming history across 750 million users form the base. Semantic IDs compress catalog vectors into tokens the model can autoregressively generate, predicting the next song or episode as the next token in a sequence. A soft tokenization layer projects a user's embedding directly into the LLM's token space, giving the frozen model a user-specific token to attend over. Podcast next-episode recommendations are already running on this stack in production.

Speaker info:
- https://x.com/kaffeinated
- https://www.linkedin.com/in/shivam13verma

## Anthropic Workshop: Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson

- Upload date: 2026-05-18
- Video: https://www.youtube.com/watch?v=mR-WAvEPRwE
- Transcript: raw/20260518_mR-WAvEPRwE/mR-WAvEPRwE.en-orig.vtt
- Metadata: raw/20260518_mR-WAvEPRwE/mR-WAvEPRwE.info.json

Why self-evaluation is a trap and adversarial evaluator agents work better; why context compaction doesn't cure coherence drift but structured handoffs do; how to decompose work into testable sprint contracts; how to grade subjective output with rubrics an LLM can actually apply; and how to read traces as your primary debugging loop. Plus the question nobody asks: which parts of your harness should you delete when the next model drops?

Speaker info:
- Ash Prabaker  |  https://www.linkedin.com/in/ash-prabaker/
- Andrew Wilson  |  https://www.linkedin.com/in/anddwilson/

Timestamps:
0:00 Introduction and speakers
1:21 Overview of long-running agents
2:29 Challenges: Context, Planning, and Judgment
4:14 Two approaches: Model updates vs. Harness evolution
5:58 Prehistory: Sonnet 3.5, Computer Use, and MCP
6:34 The evolution of Claude Code
7:55 The Ralph loop technique
9:49 Sonnet 4.5, Agent SDK, and checkpoints
10:49 Opus 4.5 and the role of sub-agents
12:05 First long-running agent patterns
14:20 Opus 4.6, Agent Teams, and server-side compaction
17:28 State-of-the-art harness patterns
21:30 Evaluating subjective output with rubrics
23:44 Introducing the 'Planner' role
25:04 The generator-evaluator contract
31:28 Specificity in contracts and debugging traces
34:14 Adjusting harnesses as models evolve
37:56 How to build your own agent harness
39:01 Key takeaways for long-running agents
40:05 Q&A session

## Rewiring the State — Eoin Mulgrew, No. 10 (Downing Street)

- Upload date: 2026-05-18
- Video: https://www.youtube.com/watch?v=ObNKGf9YR0g
- Transcript: raw/20260518_ObNKGf9YR0g/ObNKGf9YR0g.en-orig.vtt
- Metadata: raw/20260518_ObNKGf9YR0g/ObNKGf9YR0g.info.json

The cabinet office was about to spend one and a half million pounds on an outside law firm to analyze the UK statute book. One engineer embedded with the in-house legal team for two weeks instead. The tool now lives with that team and can be run whenever they want. Eoin Mulgrew from the Number 10 data science team uses that as a typical example, not a headline one.

The talk covers what it actually takes to run a small insurgent technical unit at the center of government: market rate pay, a 0.7% acceptance rate, recruiting exclusively from outside the civil service, and an unusually direct mandate to go into departments and ship. The demos include a policy simulation tool, a delivery red-teaming PMO, two public dashboards that had never existed before, and a public service that went from idea to live in two months. The closing argument is a photo of a recent Harvard dropout and YC founder standing outside HMP Wormwood Scrubs holding the keys, two weeks into the job.

Speaker info:
- https://www.linkedin.com/in/eoinmulgrew/

## Let's go Bananas with GenMedia — Guillaume Vernade, Google DeepMind

- Upload date: 2026-05-18
- Video: https://www.youtube.com/watch?v=BcWFc3H7Khg
- Transcript: raw/20260518_BcWFc3H7Khg/BcWFc3H7Khg.en-orig.vtt
- Metadata: raw/20260518_BcWFc3H7Khg/BcWFc3H7Khg.info.json

Guillaume Vernade from Google DeepMind takes a public domain book and runs it through the full gen media stack live. Gemini reads the whole text and writes image prompts for each character and chapter. Imagen generates the portraits. Veo animates them into video clips using those images as first frames. Lyria composes a different piece of music per chapter, with or without lyrics. The TTS model reads dialogue from the book using a trick that makes two voices sound like four distinct characters.

The interesting layer underneath all of it is that Gemini acts as the prompt engineer for every other model, and it works well partly because the gen media models were trained on prompts written by Gemini. The workshop also covers the Lyria Realtime model, which generates music continuously and responds to new prompts mid-stream like a DJ, and a new interactions API that makes chained multi-turn calls cheaper by caching context server-side instead of resending the full book on every turn.

Speaker info:
- https://x.com/Giom_V
- https://www.linkedin.com/in/guillaumevernade
- https://github.com/Giom-V

## Why Your AI UX Is Broken (and It's Not the Model's Fault) — Mike Christensen, Ably

- Upload date: 2026-05-17
- Video: https://www.youtube.com/watch?v=YNJvm7t3yq8
- Transcript: raw/20260517_YNJvm7t3yq8/YNJvm7t3yq8.en-orig.vtt
- Metadata: raw/20260517_YNJvm7t3yq8/YNJvm7t3yq8.info.json

SSE ties a response stream to a single connection. The user refreshes the page, walks out of WiFi range, or opens a second tab and the in-progress response is gone. Abort and resume are mutually exclusive for the same reason: the only signal a client can send over a one-way pipe is closing it, so the agent cannot tell the difference between a cancel and a disconnect. Vercel's AI SDK documents this explicitly.

Mike Christensen from Ably makes the case for treating the session itself as a durable shared resource, decoupled from any individual connection, device, or agent instance. Clients subscribe to the session rather than to a request, so reconnects resume automatically, any tab or device has full visibility of live activity, and concurrent agents write independently without routing everything through an orchestrator. The demo shows all of this: multi-tab sync, a forced network disconnect that self-recovers, two agents running in parallel, and a handoff to a human support agent who joins the session mid-conversation with the full interaction history already visible.

Speaker info:
- https://x.com/christensencode
- https://www.linkedin.com/in/mikescottchristensen/

Timestamps:
0:00 Introduction to AI chat applications
0:51 Current implementation: Direct HTTP streaming and SSE
3:03 Three foundational capabilities for great AI products
4:34 Limitations of direct HTTP streaming
5:21 Introducing durable sessions
6:06 Resumability in streams
7:43 The conflict between SSE, resumability, and live control
9:13 Multi-device and multi-tab synchronization issues
11:12 Handling concurrent multi-agent architectures
12:54 Using Pub/Sub and Ably channels for durable sessions
14:12 Introducing Ably AI Transport SDK
15:34 Live demo of durable session capabilities
17:38 Handoff to human support agent

## Fighting AI with AI — Lawrence Jones, Incident

- Upload date: 2026-05-17
- Video: https://www.youtube.com/watch?v=L2r6vLlLgs8
- Transcript: raw/20260517_L2r6vLlLgs8/L2r6vLlLgs8.en-orig.vtt
- Metadata: raw/20260517_L2r6vLlLgs8/L2r6vLlLgs8.info.json

Incident's AI SRE runs hundreds of prompts per investigation across logs, metrics, traces, and code. When it produces a wrong root cause analysis, there is no tractable way for a human to read through the full trace and find where the reasoning went sideways. Lawrence Jones, founding engineer at Incident.io, describes the moment the team realized they needed AI to debug their AI.

The talk covers three patterns they built. A small CLI lets coding agents read and edit eval YAML files that had grown too large for agents to work with directly, enabling a red-green runbook where the agent writes a failing eval, fixes the prompt, and checks nothing else broke. Their bigger unlock was serializing every UI debugging view as a downloadable file system: drop it into a Claude Code session, describe the bad behavior, and the agent traces through the prompt hierarchy to tell you exactly which prompt to change. For fleet-scale analysis, 25 agents run in parallel each analyzing one investigation, then a second stage clusters the results to surface systemic failure patterns across customer accounts.

Speaker info:
- https://x.com/lawrjones
- https://www.linkedin.com/in/lawrence2jones/

## Harnesses in AI: A Deep Dive — Tejas Kumar, IBM

- Upload date: 2026-05-17
- Video: https://www.youtube.com/watch?v=C_GG5g38vLU
- Transcript: raw/20260517_C_GG5g38vLU/C_GG5g38vLU.en-orig.vtt
- Metadata: raw/20260517_C_GG5g38vLU/C_GG5g38vLU.info.json

Tejas will be back on stage at the World's Fair next week! see https://ai.engineer/wf and use YOUTUBEPROMO for new tickets only. Join 6000 AI engineers at the "Superbowl of AI"!

---

The agent hit a login page, panicked, reported success anyway, and the upvote never happened. Tejas Kumar's diagnosis: not a prompt problem. A harness problem.

The demo builds a browser agent on GPT-3.5 Turbo (consciously choosing a VERY old model to show how good harness eng can improve it a lot) against Hacker News and layers in a harness without touching the prompt once. Guardrails cap iterations and compact context. A verify step reads the tool call history to catch the agent lying about what it did. A login handler watches the browser URL each loop and injects credentials programmatically when it hits the login page. By the end the cheap old model reliably logs in and upvotes the post.

Speaker info:
- https://x.com/TejasKumar_
- https://www.linkedin.com/in/tejasq/
- https://github.com/TejasQ

Timestamps:
0:00 Introduction to Tejas Kumar and AI Harnesses
1:45 Why we use harnesses: Reliability and control
3:00 Defining an agent harness from first principles
4:32 Key components of an agent harness (Tooling, Context, Guardrails)
5:59 Starting the demo: Building a browser agent
7:00 Inspecting the initial agent loop
8:12 The problem: Agent failure and hallucination
10:20 Adding guardrails and context management
11:54 Refactoring into a formal harness
13:02 Implementing a verify step to catch lies
15:36 Implementing a login handler for programmatic access
17:42 Final demonstration: Successful autonomous upvoting
18:34 Summary and the future of dynamic harnesses

## How to Leverage Domain Expertise — Chris Lovejoy, Notius Labs

- Upload date: 2026-05-16
- Video: https://www.youtube.com/watch?v=kfSDc2eVLo4
- Transcript: raw/20260516_kfSDc2eVLo4/kfSDc2eVLo4.en-orig.vtt
- Metadata: raw/20260516_kfSDc2eVLo4/kfSDc2eVLo4.info.json

Granola's first employee was a writer who still reviews meeting note outputs and tweaks prompts directly. Chris Lovejoy says that is not a gap in the org chart. There is no objectively perfect meeting note, so you need someone with taste doing both the assessment and the improvement.

He frames this as one of three patterns: the Oracle owns the full loop, the Evaluator defines quality and measures it while engineers improve, the Architect builds systems that improve from usage automatically. Three case studies cover when each is appropriate, what skills to hire for, and what happens when you bring in a domain expert but give them no ownership.

Speaker info:
- https://x.com/ChrisLovejoy_
- https://www.linkedin.com/in/dr-christopher-lovejoy/
- https://github.com/chris-lovejoy

## Connecting the Dots with Context Graphs — Stephen Chin, Neo4j

- Upload date: 2026-05-16
- Video: https://www.youtube.com/watch?v=eW_vxrjvERk
- Transcript: raw/20260516_eW_vxrjvERk/eW_vxrjvERk.en-orig.vtt
- Metadata: raw/20260516_eW_vxrjvERk/eW_vxrjvERk.info.json

Ask a vector RAG system about a patient's emphysema care plan and it returns generic advice: respiratory therapy, deep breathing. Give it a graph grounded in that patient's actual history and it knows they smoke, knows they've had an operation, and gives recommendations that reflect it. The information existed in both cases. What changed was whether the system could traverse the relationships connecting it.

Stephen Chin from Neo4j makes the case that retrieval alone is not enough because agents also lose the reasoning behind past decisions. Context graphs capture not just what was retrieved but what decisions were made, why, which policies applied, and what the outcome was, so that precedent is queryable the next time a similar case comes up. The financial services demo shows this concretely: a loan decision that surfaces a prior rejection, related margin trades, and fraud risk patterns, with the graph traversal visible so the human making the final call can actually see what the system is drawing on.

Speaker info:
- https://x.com/steveonjava
- https://linkedin.com/in/steveonjava

## Beyond Code Coverage: Functionality Testing with Playwright MCP — Marlene Mhangami, Microsoft

- Upload date: 2026-05-16
- Video: https://www.youtube.com/watch?v=FWEInOtngmM
- Transcript: raw/20260516_FWEInOtngmM/FWEInOtngmM.en-orig.vtt
- Metadata: raw/20260516_FWEInOtngmM/FWEInOtngmM.info.json

When an LLM writes your tests, it tends to write tests that confirm what the code does rather than tests that verify what the user experiences. Your test suite goes green. The app still breaks in ways none of those tests would catch.

Marlene Mhangami from Microsoft makes the case for flipping the order: get the agent to write failing Playwright tests against the expected behavior first, then generate code to pass them. The demo runs this live with GitHub Copilot and the Playwright MCP server on a toy store search feature, with the browser open so you can watch the agent click through filters and validate results in real time.

Speaker info:
- https://x.com/marlene_zw
- https://www.linkedin.com/in/marlenemhangami/
- https://github.com/marlenemhangami

Timestamps:
0:00 Introduction to GitHub Octoverse stats and 2025/2026 growth
2:13 Does AI actually increase developer productivity?
3:52 Importance of maintaining a clean codebase
4:36 Test-Driven Development (TDD) and the Red-Green-Refactor cycle
6:07 Common criticisms of TDD and unit testing
7:43 The problem with AI-generated self-affirming tests
8:09 Introduction to Playwright for functional testing
9:18 Integrating AI agents with Playwright for faster TDD
10:54 Live Demo: Adding search and filter features to a toy store app
12:25 Using GitHub Copilot CLI and Work IQ for feature requests
13:50 Generating and running Playwright tests live
16:10 Best practices for using AI with Playwright
17:30 Q&A: Handling state management and testing across different screen sizes

## Agents Don't Do Standups: Building the Post-Engineer Engineering Org — Mike Spitz, PFF

- Upload date: 2026-05-15
- Video: https://www.youtube.com/watch?v=VMemhtlsoNk
- Transcript: raw/20260515_VMemhtlsoNk/VMemhtlsoNk.en-orig.vtt
- Metadata: raw/20260515_VMemhtlsoNk/VMemhtlsoNk.info.json

PFF ran a three-month case study: two engineers against a team of ten, same codebase, same customers. The two shipped five times a day. The ten shipped once every five days. Output measured by ticket complexity came out at 10x. Customer satisfaction went up, not down. Mike Spitz, their CTO, started with one reframe: stop asking how to help engineers go faster and ask how to make the agents faster instead.

The talk covers what that reframe actually dismantled. Standups went away because tickets auto-update from PR state. Sprint planning went away because estimates are irrelevant when the bottleneck is no longer human. Code review got split: agents handle style and naming, engineers handle system design. The spec to lightweight design doc to auto-generated ticket to PR flow replaced most of the coordination overhead entirely. What survived is a short huddle every other day, a strong opinion about which engineers thrive in this setup, and a QA agent that spins up on staging after every merge and checks acceptance criteria against the ticket.

Speaker info:
- https://x.com/mikespitz_uk
- https://www.linkedin.com/in/mike-spitz-89741243/

Timestamps:
0:00 Introduction to the case study at PFF
1:47 The shift: optimizing for agent speed rather than engineer speed
2:28 Results: 25x increase in deployment frequency
3:16 Measuring success through ticket complexity and customer satisfaction
4:53 Dismantling Scrum and traditional development processes
5:58 The new development workflow (Spec → LDD → Ticket → PR)
6:51 Eliminating coordination overhead (no sprint planning or standups)
8:28 Best practices for implementation and team selection
10:09 Utilizing agents for deterministic tasks and code reviews
12:00 Viewing the engineering lifecycle as a factory
13:06 Automated QA and the future of self-healing systems
14:10 Where human oversight remains essential
14:48 Strategic advice for scaling AI-driven engineering

## Combine Skills and MCP to Close the Context Gap — Pedro Rodrigues, Supabase

- Upload date: 2026-05-15
- Video: https://www.youtube.com/watch?v=JT3OzDKrucU
- Transcript: raw/20260515_JT3OzDKrucU/JT3OzDKrucU.en-orig.vtt
- Metadata: raw/20260515_JT3OzDKrucU/JT3OzDKrucU.info.json

Agents working with Postgres will confidently create a view over a table with row-level security enabled and silently bypass that security in the process. Not because they can't reason. Because they don't know about the security_invoker flag, and nobody told them. Pedro Rodrigues from Supabase ran this exact test: same agent, same task, MCP alone versus MCP plus a skill. The one without the skill shipped a query that exposed data it shouldn't have.

The talk covers what Supabase learned building their agent skill from scratch: critical security rules go directly in skill.md because agents will reliably skip reference files, skills should point to living documentation rather than duplicate it, and opinionated workflow guidance matters more than comprehensive coverage. Their evals ran across Claude and GPT models in three conditions and the result was unanimous. Skills without MCP underperform. MCP without skills misses environment-specific constraints. Together they close the gap that makes agents unreliable on real production systems.

Speaker info:
- https://x.com/rodriguespn23
- https://www.linkedin.com/in/pedro-neves-rodrigues/
- https://github.com/Rodriguespn

## How Building with AI Can Double the Throughput of Your Engineering Team — Brian Scanlan, Intercom

- Upload date: 2026-05-15
- Video: https://www.youtube.com/watch?v=4_VQBbs2iQA
- Transcript: raw/20260515_4_VQBbs2iQA/4_VQBbs2iQA.en-orig.vtt
- Metadata: raw/20260515_4_VQBbs2iQA/4_VQBbs2iQA.info.json

Intercom hit 2x engineering throughput in under a year. Not by prompting better. By treating Claude Code like a new hire: onboarding it to a Rails monolith built over 15 years, writing skills for every recurring task, connecting it to production systems and internal tooling, and going all in on one platform instead of letting everyone pick their favorite tool.

Brian Scanlan covers what the data looks like: PR throughput doubled, 17.6% of pull requests auto-approved with SOC 2 sign-off, and the CI infrastructure collapsed under the volume. The principle behind all of it comes down to framing. Give agents problems, not tasks. He was pulled into a security incident over accidentally published Snowflake metadata, described the situation to Claude, and watched it pull the files, run the analysis, and hand back next steps in two minutes using a skill he didn't know existed.

Speaker info:
- https://x.com/brian_scanlan
- https://www.linkedin.com/in/scanlanb/

## Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate

- Upload date: 2026-05-14
- Video: https://www.youtube.com/watch?v=vi-2nasppAg
- Transcript: raw/20260514_vi-2nasppAg/vi-2nasppAg.en-orig.vtt
- Metadata: raw/20260514_vi-2nasppAg/vi-2nasppAg.info.json

The abstraction is three things: state, a synchronous reducer that derives state from events, and an after-append hook for side effects. The split matters: when your program restarts after 100 events, you want to catch up state without replaying LLM requests. Everything that happens (streaming chunks, tool calls, errors, circuit breaker triggers) is an event in the log.

The interesting part is deployment. Jonas demos "dynamic worker configured," an event whose payload is a JavaScript string containing a processor. Append it to any stream and that stream becomes an AI agent without server or dependencies. The broader implication: processors from different authors on different servers can compose against the same stream, and a safety checker can inject context in a 200ms window before an LLM request without blocking the agent if it doesn't make it.

Speaker info:
- https://x.com/jonas
- https://www.linkedin.com/in/jonashuckestein
- https://github.com/jonastemplestein


0:14 Introduction and workshop overview
1:33 Concept of event-sourced agent harnesses
2:24 Desired characteristics: Extensibility and composability
3:14 Agents on the edge and public routability
4:20 The distributed nature of agents and potential pitfalls
5:40 Introduction to the event stream architecture
8:38 Working with the API via curl
10:48 Handling events and error states
11:57 Circuit breakers and stream management
13:49 Scheduling tasks and event subscriptions
15:17 Q&A: Architectural philosophy
19:17 Demonstrating the SDK and TypeScript integration
30:06 Defining stream processors and reducers
47:34 How stream processors function in production
50:35 Dynamic workers and deploying via event payloads
58:45 Discussion on before-hooks versus eventual consistency
1:02:16 Future outlook and wrapping up

## Mind the Gap (In your Agent Observability) — Amy Boyd & Nitya Narasimhan, Microsoft

- Upload date: 2026-05-14
- Video: https://www.youtube.com/watch?v=iOXM3zE-2dk
- Transcript: raw/20260514_iOXM3zE-2dk/iOXM3zE-2dk.en-orig.vtt
- Metadata: raw/20260514_iOXM3zE-2dk/iOXM3zE-2dk.info.json

Agents drift. Models change, prompts get tweaked, edge cases accumulate, and the gap between what your agent does and what you need it to do widens without you noticing. Amy and Nitya walk through Microsoft Foundry's observability stack: tracing built on OpenTelemetry, built-in evaluators for quality, safety, and agentic metrics like intent resolution and task adherence, and red teaming where a second AI attacks your agent with adversarial prompts to find vulnerabilities before your users do.

The piece worth watching for is the observe skill demo. You point it at an agent with no eval dataset, no baselines, nothing. It generates the dataset, runs batch evaluations, optimizes the prompt, compares versions, and rolls back to the best one... all from a single prompt to a coding agent. The skill shows its reasoning at each step, which is where the real value is: it surfaces the failures you didn't know to look for.

Speaker info:
- https://x.com/NityaNarasimhan
- https://www.linkedin.com/in/nityan/
- https://x.com/AmyKateNicho
- https://www.linkedin.com/in/amykatenicho/

## Ship Real Agents: Hands-On Evals for Agentic Applications — Laurie Voss, Arize

- Upload date: 2026-05-14
- Video: https://www.youtube.com/watch?v=Xfl50508LZM
- Transcript: raw/20260514_Xfl50508LZM/Xfl50508LZM.en-orig.vtt
- Metadata: raw/20260514_Xfl50508LZM/Xfl50508LZM.info.json

Most agents get tested by running a few queries and checking if it looks right. Laurie calls this the vibes problem: it doesn't catch regressions, doesn't run in CI, and doesn't tell you whether a prompt fix broke three other things. This workshop builds a complete eval pipeline from scratch on a financial analysis agent: tracing with Phoenix, reading traces before writing a single eval, categorizing failures by root cause, then building code evals, built-in LLM-as-a-judge evals, and a custom rubric with labeled examples.

The sharpest lesson: choosing the right eval matters more than tuning it. A correctness eval scored 0 out of 13 on the same agent that a faithfulness eval scored 13 out of 13, because the model doesn't know what year it is and can't verify forward-looking financial data. The workshop closes on the thing most eval content skips — experiments that let you prove a prompt change actually worked, rather than eyeballing it and calling it a win.

Speaker info:
- https://x.com/seldo
- https://www.linkedin.com/in/seldo/
- https://github.com/seldo

Timestamps:
0:00:00 Introduction
0:00:14 Workshop Overview
0:04:31 Troubleshooting Phoenix Setup
0:05:17 Fundamentals of Evals and Tracing
0:18:44 Anatomy of an Eval Result
0:21:19 The Iteration Loop
0:26:58 Building the Financial Analysis Agent
0:33:28 Using Phoenix for Observability
0:35:38 Running Multiple Test Queries
0:38:12 Reading and Categorizing Traces
0:49:52 Implementing Code Evals
0:57:51 Built-in LLM-as-a-Judge Evals
1:03:04 Faithfulness Evaluation
1:04:35 Designing a Custom Eval Rubric
1:11:47 Running the Actionability Judge
1:19:14 Using Data Sets and Experiments
1:50:19 Final Tips and Best Practices
1:51:48 Differences Between Phoenix and Arize AX

## CI/CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner

- Upload date: 2026-05-13
- Video: https://www.youtube.com/watch?v=VktrqzQgytY
- Transcript: raw/20260513_VktrqzQgytY/VktrqzQgytY.en-orig.vtt
- Metadata: raw/20260513_VktrqzQgytY/VktrqzQgytY.info.json

Traditional CI/CD was built for humans pushing one or two diffs a week. Scale to thousands of autonomous agents opening PRs continuously and you get runner saturation, cold Docker builds on every branch, cache thrash, and a merge queue that starts behaving like a serialized database lock where time-to-commit becomes the actual bottleneck.

Madison Faulkner and Hugo Santos (Namespace) lay out what replaces it: no PRs, just intent and plan fed into an agent loop with fast inline validation. Changes queue in a premerge layer where humans review intent-plus-outcome rather than diffs. The end state they're pointing toward is agents exploring multiple commits in parallel for the same plan, a multiverse where the tip of the repo is a moving target and the inner loop needs to be stateful and fast enough to keep up.

Speaker info:
- https://x.com/madsfaulkner
- https://www.linkedin.com/in/madisonhfaulkner/
- https://namespace.so/blog/introducing-namespace
- https://www.linkedin.com/in/hugomgsantos/

Timestamps
0:00 Introduction and speaker bios
1:28 Why agentic software is breaking traditional CI/CD
1:59 The fragmented lifecycle of modern software development
2:25 How traditional CI/CD pipelines work
2:55 The problems with CI/CD at agent scale
4:04 Replacing CI/CD with acceleration and orchestration
6:12 Real-world solutions and the future of agentic loops
7:23 The role of the human as the agent
8:43 Why Pull Requests (PRs) are becoming a bottleneck
10:00 A new architecture: Intent and plan-based development
11:58 Moving toward fully automated internal/external validation
13:46 The premerge queue and human-in-the-loop review
15:20 The future: Parallel development in the multiverse
16:51 Conclusion: The shifting role of CI and governance

## Self-Training Agents: Hermes Agent, HF Traces, Skills, MCP & Finetuning  — Merve Noyan, Hugging Face

- Upload date: 2026-05-13
- Video: https://www.youtube.com/watch?v=OV56RddyFuU
- Transcript: raw/20260513_OV56RddyFuU/OV56RddyFuU.en-orig.vtt
- Metadata: raw/20260513_OV56RddyFuU/OV56RddyFuU.info.json

Open-source models have caught up. GLM 5.1 is leading the Artificial Analysis intelligence index over closed models, and the gap is closing fast with each release cycle. The practical upside beyond benchmarks: full weight access means you can quantize, fine-tune, and deploy to edge devices or browsers without data leaving your infrastructure.

@MerveNoyan walks through the Hugging Face ecosystem built around this: inference providers that route to the fastest or cheapest option per model, benchmark datasets for filtering by SWE-bench or AIME scores directly on Hub, a traces repository type for storing and exploring agent sessions, and skills that plug into coding agents. The closer is a live demo where she asks Claude Code to fine-tune a vision-language model on a dataset by name. The agent calculates VRAM requirements, selects an instance, and kicks off the job. What used to be a day of napkin math is now a prompt.


Speaker info:
- https://x.com/mervenoyann
- https://www.linkedin.com/in/merve-noyan-28b1a113a/
- https://github.com/merveenoyan

Timestamps
0:00 Introduction to Open Agent Ecosystem
0:39 Importance of Open Source in Machine Learning
2:36 Hugging Face Hub overview
3:06 Agentic models and Vision-LMs
4:24 Benchmark datasets and model filtering
5:16 Inference providers and model routing
6:50 Local coding agents and tools
7:46 Hermes agents for memory management
9:20 Traces repository for agent sessions
10:22 Tips for finding and serving local models
12:07 Supercharging agents with Hugging Face skills
13:41 Live demonstration of agent-driven fine-tuning
14:41 Training vision models (object detection/segmentation)
15:00 Using Model Context Protocol (MCP) for agents
16:30 Case study: OCR processing for AI papers

## Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take

- Upload date: 2026-05-13
- Video: https://www.youtube.com/watch?v=FlzpEGHNVKQ
- Transcript: raw/20260513_FlzpEGHNVKQ/FlzpEGHNVKQ.en-orig.vtt
- Metadata: raw/20260513_FlzpEGHNVKQ/FlzpEGHNVKQ.info.json

LLMs can explain things clearly but can't play chess reliably. Take Take Take (Magnus Carlsen's app) solved this by separating concerns: Stockfish handles position evaluation, tactical and positional detectors extract concepts like forks, pins, and structural weaknesses, and the LLM's only job is translating those structured signals into English. Keeping the model as a translator rather than a reasoner is what makes it work at sub-3-second latency for a consumer app.

Anant Dole and Asbjørn Steinskog also walk through how they closed the feedback loop. When a user flags bad commentary, it posts to Slack and injects the event into a running Claude Code session via Channels, a new MCP feature in research preview. Claude investigates the position, modifies prompts or detectors, regenerates the commentary, and asks clarifying questions back through Slack. During the live demo, Anant was reviewing the PR from his phone.

Speaker info:
- https://www.linkedin.com/in/asbj%C3%B8rn-ottesen-steinskog-a8000241/
- https://www.linkedin.com/in/anantdole/

## Give Your Agent a Computer — Nico Albanese, Vercel

- Upload date: 2026-05-12
- Video: https://www.youtube.com/watch?v=wflNENRSUb4
- Transcript: raw/20260512_wflNENRSUb4/wflNENRSUb4.en-orig.vtt
- Metadata: raw/20260512_wflNENRSUb4/wflNENRSUb4.info.json

The key insight from Vercel's internal agent work: giving an agent a file system didn't just add storage, it changed how the agent behaved. It started following through on long tasks, staying on track, and building on its own prior work. That's what this workshop builds toward.

@nicoalbanese10  walks through AI SDK v6 from scratch: a tool loop agent, provider-executed web search, end-to-end type safety, and Vercel's new persistent named sandboxes. The agent gets a bash tool, a memories.md file it reads and writes, and instructions that make it generate Python scripts for repeatable tasks and store them for later. By the end, it's an agent that accumulates tools and context across sessions without any manual memory management.

Speaker info:
- https://x.com/nicoalbanese10
- https://www.linkedin.com/in/nicoalbanese/
- https://github.com/nicoalbanese

Timestamps:
0:00 Setup and project initialization
7:31 Installing dependencies
9:02 Introduction to AI SDK v6 and tool loop agents
11:05 Defining the agent in agent.ts
13:40 Building the route handler for the chat API
15:26 Creating the frontend UI with useChat
16:53 Modifying agent instructions
18:40 Adding web search tool (provider-executed tools)
23:55 Adding UI components for tool usage
27:43 The importance of persistent sandboxes (file systems for agents)
33:45 Managing context and message history across steps
45:11 Initializing persistent sandboxes
47:20 Defining custom call options and context
51:10 Creating the bash execution tool
55:05 Integrating the bash tool into the agent
57:15 Adding persistent memory (memories.md)
1:03:44 Making agents learn by generating Python scripts
1:05:58 Reviewing the full agent system and sub-agents

## Lessons from Trillion Token Deployments at Fortune 500s — Alessandro Cappelli, Adaptive ML

- Upload date: 2026-05-12
- Video: https://www.youtube.com/watch?v=X6NShR2ccOg
- Transcript: raw/20260512_X6NShR2ccOg/X6NShR2ccOg.en-orig.vtt
- Metadata: raw/20260512_X6NShR2ccOg/X6NShR2ccOg.info.json

95% of GenAI pilots fail to reach production. Alessandro Cappelli's argument is that this isn't a deployment problem or a prompt engineering problem — it's a feedback integration problem. Instruction fine-tuning and proprietary models give you a demo. Only reinforcement learning gives you a systematic way to incorporate defects, business metrics, and production signals and keep improving.

This talk covers what a production-grade RL pipeline looks like at Fortune 500 scale: synthetic data as a byproduct of environment training rather than a prerequisite, mock environments where agents can fail safely before touching real systems, and LLM judges that replace expensive annotation campaigns with a rubric-definition exercise that takes hours rather than weeks. The throughline is that agents raise the stakes on all of this — more tokens, less tolerance for errors, direct access to live databases — and RL was designed for exactly that problem.

Speaker info:
- https://www.linkedin.com/in/alessandro-cappelli-aa8060172

## Malleable Evals: Why Are We Evaluating Adaptive Systems with Static Tests? — Vincent Koc, OpenClaw

- Upload date: 2026-05-12
- Video: https://www.youtube.com/watch?v=4VhbYlfC7Gs
- Transcript: raw/20260512_4VhbYlfC7Gs/4VhbYlfC7Gs.en-orig.vtt
- Metadata: raw/20260512_4VhbYlfC7Gs/4VhbYlfC7Gs.info.json

Eighty percent of what your agent does is stable and well defined. The other twenty percent keeps changing as your users change, and that twenty percent is what breaks your business. Vincent Koc's argument is that we have been treating AI applications like static software and building evaluations like fixed datasets when the thing being measured keeps adapting underneath them.

The talk names this eval calcification and sketches what replaces it: agents that self curate test suites from their own traces, telemetry in the loop so the harness knows what is breaking and corrects itself, and evals that define an end state rather than a right answer. The benchmark is not a dataset. It is a self optimizing system that has to grow with the application it measures.

Speaker info:
- https://x.com/vincent_koc

## Why MLX — Prince Canuma, Neywa Labs

- Upload date: 2026-05-11
- Video: https://www.youtube.com/watch?v=zTLJNHj0DeQ
- Transcript: raw/20260511_zTLJNHj0DeQ/zTLJNHj0DeQ.en-orig.vtt
- Metadata: raw/20260511_zTLJNHj0DeQ/zTLJNHj0DeQ.info.json

MLX is an array framework for Apple Silicon, essentially PyTorch for your Mac, and this is a tour of what it can run: real-time vision models that describe the world around you, sub-100ms text-to-speech, speech-to-speech pipelines, omni models that take image and audio together, and video generation from a text prompt on 16GB of VRAM. A recent breakthrough called Turbo Quant cuts KV cache by 4x and gets 1M context running fully on device. The community projects include a native voice app, a robot speaking in real time with a cloned voice, and a system that chains video generations into a coherent story — all without a cloud call.

The underlying argument: the cloud assumption doesn't hold everywhere. Not for someone in Africa on an unreliable connection. Not for a local agent that needs to stay on. Not for a robot that has to hear, see, and respond without phoning home.

Speaker info:
- https://x.com/Prince_Canuma
- https://pl.linkedin.com/in/prince-canuma

Timestamp

0:00 Introduction and motivation for on-device AI
1:13 The origin story: Accessibility and Apple Silicon
2:27 Introduction to the MLX framework
3:30 Vision capabilities: Empowering accessibility
4:15 Omni models: Multimodal input support
5:25 Audio intelligence: Controlling computers via voice
6:33 Speech-to-speech and modular pipelines
7:59 Vision demo: Real-time image analysis
8:56 Background blur and object detection demo
9:31 Large language model demo: Running Gemma 4 locally
11:50 Community projects: Grounded visual reasoning
13:06 Video generation chains on-device
14:33 Native voice application showcase
15:39 Robotics: Real-time voice cloning and interaction
17:14 Q&A: Neural engine usage and CorML
18:18 Q&A: Monitoring performance with Mactop
19:34 Q&A: Available model recommendations
20:15 Q&A: Limitations and performance expectations
20:54 Q&A: Turbo Quant breakthrough and KV cache optimization

## A Piece of Pi: Embedding The OpenClaw Coding Agent In Your Product — Matthias Luebken, Tavon

- Upload date: 2026-05-11
- Video: https://www.youtube.com/watch?v=vAIDdLKB6-w
- Transcript: raw/20260511_vAIDdLKB6-w/vAIDdLKB6-w.en-orig.vtt
- Metadata: raw/20260511_vAIDdLKB6-w/vAIDdLKB6-w.info.json

OpenClaw feels like it's learning: it discovers capabilities, stitches tools together, builds solutions it wasn't explicitly taught. The reality is simpler — it's an LLM calling tools in a loop, powered by Pi, a minimal coding agent SDK. This talk is about what you can build once you understand that.

Matthias Luebken walks through embedding Pi in a real product: a B2B sales pipeline where incoming RFP emails route to customer-specific agent sessions, CLIs expose CRM and ERP data in a form the agent can use cleanly, and the only output a human sees is a draft in their inbox. The architectural principle running through it: don't fight the coding agent, make things easy for it. Design your data access and tool interfaces so the agent can work naturally rather than having to compensate for complexity.

Speaker info:
- https://x.com/luebken
-https://github.com/luebken

Timestamps

0:15 Introduction to Pi and OpenClaw
1:55 The philosophy of coding agents (doing one thing well)
3:34 Architectural pattern: Making systems easy for agents
5:13 Defining an agent: LLM with tools in a loop
6:37 Practical example: CRM lead qualifier
8:41 Coding agents vs. core agents
10:06 Extension API and UI interactions
12:53 Multi-channel environment: Pi and OpenClaw
14:46 Real-world B2B sales pipeline application
18:14 Demonstration: Dashboard and email drafting process
20:00 Final takeaways and encouragement to tinker

## Viktor: AI Coworker That Lives in Slack — Fryderyk Wiatrowski

- Upload date: 2026-05-11
- Video: https://www.youtube.com/watch?v=ohKt066uFhg
- Transcript: raw/20260511_ohKt066uFhg/ohKt066uFhg.en-orig.vtt
- Metadata: raw/20260511_ohKt066uFhg/ohKt066uFhg.info.json

Viktor is an AI employee that lives in Slack. No web UI. It participates in channels and threads the way a teammate does, inherits integrations from whoever connected them first, and handles tasks that take ten minutes while you move on to something else.

This talk covers what breaks when you scale a personal agent to a whole company. Slack is a more complex input surface than it looks: threads, DMs, edits, deletions, emoji reactions, and conversations that drift between channels. Memory isolation gets harder when the same agent needs context for a hundred users without leaking the growth channel into the engineering queue or one person's DMs into the team feed. And when you try to swap the underlying model for something cheaper, users notice in ways that have nothing to do with task performance.

Speaker info:
- https://x.com/fawiatrowski
- http://getviktor.com/

## Two Roads to Durable Agents: Replay vs. Snapshot — Eric Allam, CEO, Trigger.dev

- Upload date: 2026-05-10
- Video: https://www.youtube.com/watch?v=svCnShDvgQg
- Transcript: raw/20260510_svCnShDvgQg/svCnShDvgQg.en-orig.vtt
- Metadata: raw/20260510_svCnShDvgQg/svCnShDvgQg.info.json

Replay-based durability — wrapping every step in a journal, replaying on recovery, requiring deterministic code — is how everyone makes agents durable today. It works until it doesn't: the journal grows with every turn, the structure starts constraining how you write code, and an agent that needs to run for hours starts looking less like a transaction and more like a session.

This talk separates the problem in two: context durability (the append-only log of everything the LLM saw, which already fits in a database) and execution durability (the files, memory, and subprocesses that live in the compute layer, which don't). The answer to the second half isn't a smarter log — it's OS-level snapshot and restore. Eric Allam walks through how Trigger.dev built this on Firecracker microVMs, getting snapshots down to 14 megabytes compressed with sub-second save and hundred-millisecond restore times, and why IBM mainframes in 1966 got there first.

Speaker info:
- https://x.com/maverickdotdev
- https://www.linkedin.com/in/eric-allam/
- https://github.com/ericallam

## How we solved Context Management in Agents — Sally-Ann Delucia

- Upload date: 2026-05-10
- Video: https://www.youtube.com/watch?v=esY99nYXxR4
- Transcript: raw/20260510_esY99nYXxR4/esY99nYXxR4.en-orig.vtt
- Metadata: raw/20260510_esY99nYXxR4/esY99nYXxR4.info.json

The naive solution is truncation. The obvious solution is summarization. Neither worked — and the Arize team found out the hard way while building an AI agent that had to analyze the very trace data it was generating.

A year of lessons from building Alyx, starting with the vicious loop that defined the problem: Alex runs on trace data, the spans grow, the context limit hits, it fails and tries again. The talk covers why truncation breaks reasoning, why summarization gives the LLM too much control, and how head/tail preservation with a retrievable memory store is what actually held. Then: long session evals, sub-agents as the answer when one context accumulates too much, and what they found when they went looking for secrets in the Claude Code source release.

Speaker info:
- https://www.linkedin.com/in/sallyann-delucia-59a381172/

Timestamps:
0:00 Introduction and speaker background
1:02 Overview of the AI agent, Alyx
1:29 The problem: Context engineering vs. prompt engineering
4:06 The vicious loop of data growth in AI agents
5:16 Why naive truncation failed
6:14 Why summarization proved unreliable
6:46 The solution: Smart truncation and memory stores
8:02 Handling long session challenges
9:23 Offloading tasks to sub-agents
11:19 Ongoing challenges and future work
12:57 Findings from the Claude Code source release
13:44 Final key takeaways on context management
14:58 Q&A session

## Feedback Loops are All You Need — Mehedi Hassan, Granola

- Upload date: 2026-05-10
- Video: https://www.youtube.com/watch?v=ON5LIT0M4do
- Transcript: raw/20260510_ON5LIT0M4do/ON5LIT0M4do.en-orig.vtt
- Metadata: raw/20260510_ON5LIT0M4do/ON5LIT0M4do.info.json

One-shotting is seductive. One line of code for web search. One prompt to serve every user. One deploy and you're done. Granola shipped a chat feature into their meeting notes app and found out what comes after that.

This talk is a product engineer's honest account of why the gap between "it works in the playground" and "it works in production" is so hard to close. Web search looks like a single tool call — until it blows up your context, bills you 10p per chat, and your provider ships an overnight update that silently degrades your results. Prompt personalization looks straightforward — until you realize that one prompt genuinely cannot serve the salesperson expecting a deal summary, the engineer expecting blockers and linear tickets, and the HR manager expecting something else entirely.

The response at Granola wasn't to prompt better. It was to build the machinery for iteration: custom internal tracing that exposes tool calls, search trails, reasoning traces, and cost in a UI built for everyone — not just engineers with CloudWatch access. And a move to run their Electron frontend as a web app, so every PR gets a preview link and Cursor can go test changes automatically. The point isn't any single technique. It's the feedback loop — and what happens to an AI feature when it actually has one.

Speaker info:
- https://x.com/mehedih_
- https://github.com/MehediH

timestamps:
0:15 Introduction to Granola and product engineering
1:08 Demonstration of meeting transcription and note-taking features
1:52 The challenges of shipping generic AI features
2:48 The difficulties of integrating web search tools
4:02 Why a single prompt cannot serve diverse user roles
4:40 Building custom internal tracing and observability tools
6:22 Enhancing developer experience for desktop applications
7:16 Refactoring Electron for web-based testing and CI/CD preview links
8:33 Automating feature verification with Cursor
8:46 Concluding thoughts on building iterative feedback loops for AI products

## Voice AI: when is the "Her" moment? — Neil Zeghidour, CEO, Gradium AI

- Upload date: 2026-05-09
- Video: https://www.youtube.com/watch?v=P_RI1kCkRbo
- Transcript: raw/20260509_P_RI1kCkRbo/P_RI1kCkRbo.en-orig.vtt
- Metadata: raw/20260509_P_RI1kCkRbo/P_RI1kCkRbo.info.json

The "Her" moment has been promised so many times it's become a joke. Every new demo, every smooth-sounding voice agent gets called it. Neil Zeghidour, CEO of Gradium AI and one of the researchers behind Moshi — the first full-duplex voice model — uses this talk to be honest about where the gap actually is and why it keeps not closing.

The core tension: cascaded systems (speech-to-text, LLM, text-to-speech) are practical and getting smarter, but they're architecturally incapable of feeling like a real conversation. Latency from tool calls alone can be 500ms to 4 seconds — while humans process and respond in around 200ms total. Speech-to-speech models solve some of that but trade it for a different problem: they're still half-duplex, meaning they're either listening or talking but never both, which makes backchanneling impossible and the interaction feel robotic in a different way. Moshi showed that full-duplex is solvable. What it didn't solve was making the model useful. And cost is a wall hiding behind the latency problem — TTS at scale is expensive enough that some teams burn through their fundraising before they can grow a user base.

The most underrated thread in the talk is paralinguistic understanding: voice carries tone, hesitation, discomfort, and cultural signals that get entirely stripped out the moment you transcribe to text. Getting to Her means building models that don't just produce natural-sounding speech but actually understand what the voice is carrying — and that's a science problem, not a prompt engineering one.

Speaker info:
- https://x.com/neilzegh
- https://www.linkedin.com/in/neil-zeghidour-a838aaa7/

Timestamps:

0:14 Introduction and mission of Gradium AI
1:16 Demonstration of voice cloning technology
2:42 The "Her" movie analogy and current limitations of Voice AI
5:42 Challenges of cascaded systems (Speech-to-Text, LLM, Text-to-Speech)
6:37 The difficulty of latency in tool calling
9:08 Explanation of Speech-to-Speech vs. cascaded architectures
9:34 The necessity of full-duplex systems and backchanneling
11:53 Demonstration of the full-duplex Moshi model
12:59 The importance of paralinguistic understanding
14:29 Scalability and the high cost of current Voice AI
16:38 Introducing Phoneon: on-device, local TTS for privacy and cost efficiency
18:29 Conclusion and path forward for Voice AI

## Give Your Chat Agent a Voice — Luke Harries, Head of Growth, ElevenLabs

- Upload date: 2026-05-09
- Video: https://www.youtube.com/watch?v=DCZZ3AJKzuc
- Transcript: raw/20260509_DCZZ3AJKzuc/DCZZ3AJKzuc.en-orig.vtt
- Metadata: raw/20260509_DCZZ3AJKzuc/DCZZ3AJKzuc.info.json

Chat agents dominated 2025. Every product either went AI-first or got left behind. But text-in, text-out is already starting to feel dated. Voice is faster, more accessible, and opens up interaction paradigms that chat just can't touch — phone lines, Zoom calls, screen readers, ambient interfaces. In this talk, Luke Harries from ElevenLabs argues that the next upgrade for every chat agent isn't better prompts or smarter RAG. It's a voice layer.

The problem is most teams have already built and tuned their chat agents. They don't want to throw that out. This session shows how ElevenLabs' Voice Engine wraps any existing agent in a few lines — handling turn-taking, speech-to-text, text-to-speech, and emotion-aware interruption detection — without touching the underlying logic. There's a live demo of converting a working chat support agent to voice in a single prompt, plus a look at the client and server SDKs, Shadcn-based UI components, and how tool calling still works through the wrapper.

Speaker info:
- https://www.linkedin.com/in/luke-harries
- https://harries.co/

Timestamps
0:00 Introduction to voice-first chat agents
0:20 The shift from text-based to voice-based interactions
1:43 Evolution of agent architecture and challenges of rebuilding
2:47 Introducing the ElevenLabs Voice Engine
3:32 Overview of the server and client SDKs
4:36 UI components and deployment demo
5:56 Summary of voice engine integration paradigms
6:37 Predictions for the future of AI agents
7:00 Q&A: Handling tool calling and integrations

## Why TTS Models Now Look Like LLMs — Samuel Humeau, Mistral

- Upload date: 2026-05-09
- Video: https://www.youtube.com/watch?v=3jGAU2sbAyY
- Transcript: raw/20260509_3jGAU2sbAyY/3jGAU2sbAyY.en-orig.vtt
- Metadata: raw/20260509_3jGAU2sbAyY/3jGAU2sbAyY.info.json

The dominant architecture pattern for text-to-speech in 2026 looks a lot like an LLM — an autoregressive transformer generating sequences of tokens, one frame of audio at a time. Samuel Humeau from Mistral walks through why the field converged there, how neural audio codecs solve the information-density problem (audio carries ~200kbps of signal; you can't feed that raw to a transformer), and what the streaming trick actually is that makes voice agents feel responsive before the full audio has even finished generating.

The talk uses Mistral's just-released open-weight TTS model as a running example — live demos of voice cloning from a few seconds of reference audio, a voice agent answering real conference schedule questions, and a breakdown of the codec-to-backbone-to-decoder pipeline that produces it all. There's also a frank section on what's still unsettled: how to handle streaming text input (tokens arriving from an LLM in real time rather than a fixed block of text) and why getting that right is the next meaningful latency win in agent pipelines.

It's the kind of talk that makes the system feel less like a black box — not by oversimplifying, but by showing exactly which engineering choices are load-bearing and which are still open problems.

Speaker info:
- https://x.com/DrSamuelBHume
- https://www.linkedin.com/in/samuelhumeau/

Timestamps:
0:00 Introduction and Mistral's new open-source TTS model
2:06 Text-to-speech in AI agents and latency
3:33 Live demo: Voice cloning with 'Paul'
6:00 Voice cloning capabilities and multilingual examples
8:01 Historical context of audio generation
8:55 Transformer-based architecture for TTS
10:00 Challenges of information density in audio
10:55 Comparison of bit rates: text vs. audio
11:39 Using neural audio codecs
13:10 Backbone transformer and frame-based generation
14:56 Text conditioning and model architecture
16:08 Latency performance metrics
16:22 Future outlook: Streaming text input
17:35 Q&A: Generating text and audio simultaneously
18:24 Q&A: Availability of voice cloning features
19:35 Q&A: Philosophical take on speech interfaces
20:44 Q&A: Next steps for streaming audio and text input

## Agentic Search for Context Engineering — Leonie Monigatti, Elastic

- Upload date: 2026-05-08
- Video: https://www.youtube.com/watch?v=ynJyIKwjonM
- Transcript: raw/20260508_ynJyIKwjonM/ynJyIKwjonM.en-orig.vtt
- Metadata: raw/20260508_ynJyIKwjonM/ynJyIKwjonM.info.json

Getting context into an LLM is not just a retrieval problem. It is a search problem. This workshop digs into the part of context engineering that usually gets waved away: how agents actually decide what to pull from files, databases, memory, and the web, and why that choice often matters more than the model itself.

Across semantic search, general-purpose database tools, shell-based retrieval, and agent skills, Leonie Monigatti shows where each search interface works, where it breaks, and how to combine them into a more effective retrieval stack. If you're building agents and trying to make retrieval less brittle, this is a practical guide to the real mechanics behind agentic search.

Workshop repo: https://github.com/iamleonie/workshop-agentic-search

Speaker info:
- https://x.com/helloiamleonie
- https://www.linkedin.com/in/804250ab/

Timestamps:
0:00:00 - Introduction and Welcome
0:00:51 - Defining Context Engineering and the role of Search
0:02:21 - Historical context: From RAG to Agentic RAG
0:04:30 - Context sources (local files, memory, databases, web)
0:06:30 - Introduction to the Shell tool and its versatility
0:08:50 - Failure modes in agentic search
0:10:41 - The importance of tool descriptions and parameter design
0:13:53 - Code Demo: Simple semantic search and its limitations
0:23:26 - Code Demo: General purpose database query (ESQL)
0:28:36 - Code Demo: Adding Agent Skills for better interaction
0:34:42 - Code Demo: Using the Shell tool for file system retrieval
0:41:26 - Code Demo: Integrating custom CLIs (Gina Grap)
0:44:42 - Practical recommendations for building a search tool stack
0:49:16 - Q&A Session begins

## FLUX, Open Research, and the Future of Visual AI — Stephen Batifol, Black Forest Labs

- Upload date: 2026-05-08
- Video: https://www.youtube.com/watch?v=x8Yb4RidLgM
- Transcript: raw/20260508_x8Yb4RidLgM/x8Yb4RidLgM.en-orig.vtt
- Metadata: raw/20260508_x8Yb4RidLgM/x8Yb4RidLgM.info.json

FLUX started as an image model story, but this talk makes the larger ambition clear: visual intelligence, not just image generation. From FLUX.1 through Kontext, FLUX.2, and FLUX.2 Klein, Black Forest Labs has been pushing fast, open releases while building toward models that understand images, video, audio, actions, and eventually the physical world itself.

Along the way, Stephen Batifol walks through the research behind that direction, including BFL's work on self-supervised multimodal training, real-time generation and editing, and the path from generative media toward world models and robotics.

Speaker info:
- https://x.com/stephenbtl
- https://www.linkedin.com/in/stephen-batifol/

## How Transformers Finally Ate Vision – Isaac Robinson, Roboflow

- Upload date: 2026-05-08
- Video: https://www.youtube.com/watch?v=VhfAVA3BG2I
- Transcript: raw/20260508_VhfAVA3BG2I/VhfAVA3BG2I.en-orig.vtt
- Metadata: raw/20260508_VhfAVA3BG2I/VhfAVA3BG2I.info.json

Vision used to belong to CNNs. This talk explains why that changed, and why transformers only recently started winning for vision despite looking like the less natural fit for images. The answer runs through pretraining, scaling, borrowed infrastructure from the LLM world, and the long arc back to the simple architecture that scales best.

Using the evolution from ViT and Swin through ConvNeXt, Hiera, SAM, and RF-DETR, Isaac Robinson walks through what actually made transformer vision systems practical, where the tradeoffs still are, and why deployment flexibility now matters as much as raw benchmark wins. What comes next for VLMs, world models, and physical AI?

Speaker info:
- https://www.linkedin.com/in/robinsonish/

## Vibe Engineering Effect Apps — Michael Arnaldi, Effectful

- Upload date: 2026-05-07
- Video: https://www.youtube.com/watch?v=Wmp2Tku2PrI
- Transcript: raw/20260507_Wmp2Tku2PrI/Wmp2Tku2PrI.en-orig.vtt
- Metadata: raw/20260507_Wmp2Tku2PrI/Wmp2Tku2PrI.info.json

What if the best way to get coding agents to use a library well is not better prompts, but giving them the library's actual code? In this workshop, Michael Arnaldi walks through a practical approach to building with Effect and LLMs by cloning the Effect repo into the project, extracting patterns directly from the source, and using those patterns to guide agent behavior.

Starting from an empty repository, the session shows how to set up an Effect-based app with tests, strict TypeScript diagnostics, agent instructions, and a simple HTTP API, while also exploring the broader problem of how to make agents effective in unfamiliar codebases. If you're building with coding agents and care about reliability, structure, and real-world Effect workflows, this is a useful hands-on framing.

Speaker info:
- https://x.com/MichaelArnaldi
- https://www.linkedin.com/in/michael-arnaldi-52858114a/

Timestamps

0:15 – Introduction and context setting for the workshop
0:47 – Interactive audience poll on experience with Effect and AI tooling
3:16 – Discussing the core philosophy: "Just clone the repo" for AI context
5:59 – Understanding LLMs vs. the human brain and context window limitations
13:13 – Project setup: Starting from an empty repository
14:20 – Initializing the project with Bun, Vitest, and TypeScript
19:18 – Adding Effect beta and configuring TSGo for the compiler
30:30 – Configuring strict diagnostics for AI-assisted development
35:20 – Adding the Effect repository as a git subtree for better agent access
37:07 – Creating agents.md to establish rules and available commands
41:40 – Researching Effect patterns for building an HTTP API
43:08 – Discussing "Spec-Driven Development" and avoiding plan-mode limitations
54:02 – Drafting the plan for the Todo HTTP API
1:05:07 – Implementing the SQL client and migration patterns
1:13:42 – Reviewing API schemas and handling identified code duplication
1:18:14 – Starting the API server and verifying OpenAPI documentation
1:20:56 – Cleaning up test suites and enforcing best practices for layers
1:38:08 – Concluding remarks on workflows, clustering, and future stability in Effect

## Agent Optimization with Pydantic AI: GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic

- Upload date: 2026-05-07
- Video: https://www.youtube.com/watch?v=A48uhxfxbsM
- Transcript: raw/20260507_A48uhxfxbsM/A48uhxfxbsM.en-orig.vtt
- Metadata: raw/20260507_A48uhxfxbsM/A48uhxfxbsM.info.json

Deploying an agent is only the start. In this workshop, Samuel Colvin shows how to improve agents after they are already live, using Pydantic AI and Logfire to change prompts, models, and other parameters in production without redeploying or restarting services.

The session covers managed variables for live prompt and model updates, how to run evals and compare prompt variants against real datasets, and how GEPA can be used to evolve better prompts from production traces and feedback signals. If you're building agents in production and want a practical path from manual tuning to continuous optimization, this is a strong hands-on walkthrough.

Speaker info:
- https://x.com/samuelcolvin
- https://www.linkedin.com/in/samuel-colvin/
- https://github.com/samuelcolvin

Timestamps:
0:00 Introduction to Samuel Colvin and the Pydantic ecosystem
1:29 Overview of GEPA for prompt optimization
3:02 Introduction to Logfire managed variables
3:55 Case study: Analyzing political dynasties using Wikipedia data
10:04 Getting started: Setting up the environment and API keys
16:55 Running the initial evaluation (evals) against a golden dataset
25:16 Comparing different prompt performance
34:00 Running the full GEPA optimization process
43:43 Q&A: Handling prompt size and systemic errors
57:01 Demonstrating managed variables in a FastAPI web server
1:11:06 Discussing implicit user feedback collection
1:15:42 Q&A: Real-world internal use cases and context engineering

## Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop

- Upload date: 2026-05-07
- Video: https://www.youtube.com/watch?v=-aM2EDTiaMs
- Transcript: raw/20260507_-aM2EDTiaMs/-aM2EDTiaMs.en-orig.vtt
- Metadata: raw/20260507_-aM2EDTiaMs/-aM2EDTiaMs.info.json

Agent failures do not look like normal software failures. In this workshop, the Raindrop team breaks down what it actually takes to monitor production agents, from explicit signals like tool errors, latency, and cost to fuzzier signals like user frustration, refusals, task failure, and capability gaps.

The session covers how to move beyond evals toward real production observability, how to use classifiers, regex, and experiments to catch regressions, and how to instrument self-diagnostics so agents can report their own failures and strange behavior. If you're running agents in production, this is a practical framework for understanding what is going wrong and how to catch it early.

Speaker info:
- https://x.com/benhylak
- https://www.linkedin.com/in/zkoticha
- https://www.linkedin.com/in/joseph-daniel-gollapalli-a371a4138/

Timestamps

0:14 Introduction and the problem of agent failures
1:48 Moving from evals to production monitoring
3:33 The two types of signals: explicit and implicit
4:47 Using classifier signals for observability
6:38 Leveraging regex for signal detection
7:30 Using experiments to validate improvements
9:42 Q&A session: Statistical relevance and experimental design
16:07 Introduction to self-diagnostics
20:15 Workshop: Coding agent demonstration
24:01 Live demo: Triggering and handling tool failure
30:26 Best practices for self-diagnostic implementation
32:20 Q&A: Real-world use cases and triage
40:02 Q&A: Managing fast-paced experimentation
44:21 Q&A: Trace visualization and data export

## Full Walkthrough: Writing & Using Skills — Nick Nisi and Zack Proser

- Upload date: 2026-05-06
- Video: https://www.youtube.com/watch?v=pFsfax19yOM
- Transcript: raw/20260506_pFsfax19yOM/pFsfax19yOM.en-orig.vtt
- Metadata: raw/20260506_pFsfax19yOM/pFsfax19yOM.info.json

Write once, run in Claude, Codex, Cursor, and your own agents

Every developer using AI tools has the same problem: they prompt the same way, for the same tasks, over and over. Skills fix this. A skill is a portable unit of agent behavior that teaches any AI tool how to do a specific job. Write one, drop it into your editor, and it just works. Across tools. Across teams.

Most people don't know this primitive exists. In this hands-on workshop, you'll write real skills, test them live, and see how one file can power Claude.ai, Claude Code, Cursor, and Codex without changing a line.

Then we'll go deeper. You'll see how one CLI uses this same pattern to power 15 framework integrations — each one a skill composed with others, wired into an agent that installs and configures auth!


What you'll do:

Write 2+ skills for tasks you actually do at work

Install and test them across AI tools in real time

Learn the craft of good skill writing — specificity, constraints, composability

See how skills compose and scale inside a real CLI powered by the Claude Agent SDK

Speaker info:
- Nick Nisi  |  https://nicknisi.com/about/
- Zach Proser  |  https://zackproser.com/

## The Multi-Agent Architecture That Actually Ships — Luke Alvoeiro, Factory

- Upload date: 2026-05-06
- Video: https://www.youtube.com/watch?v=ow1we5PzK-o
- Transcript: raw/20260506_ow1we5PzK-o/ow1we5PzK-o.en-orig.vtt
- Metadata: raw/20260506_ow1we5PzK-o/ow1we5PzK-o.info.json

Everyone's building multi-agent systems, but nobody agrees on how. This talk proposes a taxonomy of five frontier multi-agent strategies and shows what happens when you compose them into a single architecture. Drawing from production data at Factory, we walk through a three-role system (orchestrator, workers, validators) that uses validation contracts, structured agent handoffs, and adversarial verification. We cover the case for serial over parallel execution, why model selection per role is a compounding advantage, and how to design systems that get better with each model generation instead of being made obsolete by them.

Speaker info:
- https://github.com/lukealvoeiro
- https://www.linkedin.com/in/lukealvoeiro

Timestamp:
0:00 Introduction to multi-agent systems and the bottleneck of human attention
1:50 Taxonomy of five frontier multi-agent frameworks
4:04 Introducing 'Missions': The three-role architecture (Orchestrator, Workers, Validators)
6:34 The importance of validation contracts for consistent quality
8:09 Maintaining long-term context through structured handoffs
9:17 The case for serial execution over parallel execution
10:30 Mission control: Monitoring agent progress
11:22 Strategic model selection per role ('Droid whispering')
13:06 Production data analysis: Building a Slack clone
14:34 Designing systems that improve with each model generation
15:51 Conclusion: The shifting economics of software engineering

## MCP UI: Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps

- Upload date: 2026-05-06
- Video: https://www.youtube.com/watch?v=o-zkvb0iFDQ
- Transcript: raw/20260506_o-zkvb0iFDQ/o-zkvb0iFDQ.en-orig.vtt
- Metadata: raw/20260506_o-zkvb0iFDQ/o-zkvb0iFDQ.info.json

Chat interfaces are no longer limited to walls of text. In this talk, Liad Yosef and Ido Salomon explain how MCP Apps turn tools into interactive UI inside hosts like ChatGPT, Claude, VS Code, Cursor, and Copilot, letting companies send branded, functional app experiences instead of plain text responses.

The session covers the core architecture behind MCP Apps, how UI is passed over MCP, how interactions stay in context through the host, and why this changes how applications get distributed in an agent-first world. If you're building on MCP, this is a practical look at the emerging standard for UI inside chat.

Timestamps:
0:00 Introduction to MCP Apps
1:02 Why we need MCP Apps: Moving beyond text-based chat
2:06 Evolution of the MCP UI standard and partnerships
3:25 Industry and community adoption
5:14 Core concepts: Passing UI over MCP
6:49 Practical demonstration (PostHog and Claude)
8:54 Technical architecture: How it works
10:23 A new era of web interaction and user experience
12:32 Interaction mindset and message spectrums
14:56 Future outlook: Reusable views and model-UI interaction
16:18 Spectrum of UI generation: Predefined vs. Generative

## The Small Model Infrastructure Nobody Built (So We Did) — Filip Makraduli, Superlinked

- Upload date: 2026-05-05
- Video: https://www.youtube.com/watch?v=qdh_x-uRs9g
- Transcript: raw/20260505_qdh_x-uRs9g/qdh_x-uRs9g.en-orig.vtt
- Metadata: raw/20260505_qdh_x-uRs9g/qdh_x-uRs9g.info.json

Most embedding infrastructure assumes you know exactly which model you want ahead of time. This talk starts where that assumption breaks. Filip Makraduli walks through the real profiling mistakes, infrastructure gaps, and production constraints that led to building an embedding inference engine designed for dynamic model loading, hot-swapping, and memory-aware eviction instead of brittle one-model-per-container deployments.

If you're working on small-model inference, embeddings, or GPU infrastructure, this is a practical look at what breaks in the real world and how to design around it.

Speaker info:
- https://www.linkedin.com/in/filipmakraduli/

Timestamps:
0:00 Introduction and the gap in small model inference
0:53 Moving from research to building inference infrastructure
2:54 Introduction of the Superlinked inference engine
4:34 The importance of context management for agents
7:03 Misconceptions: Why more GPUs isn't the only answer
9:33 The "Yin and Yang" of inference: Model support and infrastructure
10:43 The challenge of supporting diverse model architectures
14:33 Deep dive into infrastructure and scalability
16:10 Conclusion and the open-source launch of SAI

## Demand-Driven Context: A Methodology for Coherent Knowledge Bases Through Agent Failure

- Upload date: 2026-05-05
- Video: https://www.youtube.com/watch?v=_QAVExf_1uw
- Transcript: raw/20260505__QAVExf_1uw/_QAVExf_1uw.en-orig.vtt
- Metadata: raw/20260505__QAVExf_1uw/_QAVExf_1uw.info.json

Enterprise teams spend a lot of time trying to guess what AI agents need to know. This workshop flips that around. Instead of curating context top-down, Raj Navakoti shows how to build a demand-driven context base by giving agents real problems, watching where they fail, and using those failures to reveal exactly what knowledge is missing.

Using practical exercises and real examples from IKEA Digital, the session walks through how to grow a knowledge base problem by problem, structure it in Markdown, and use agents with different roles and reasoning boundaries against the same shared context. If you're building enterprise AI systems and want a more grounded way to create useful context, this is a strong practical framework.

Speaker info:
- https://www.linkedin.com/in/raj-navakoti-529880b1/

Timestamps:
0:00 - Introduction and speaker background
2:47 - The situation: Analogy to the movie Memento and AI's memory constraints
3:55 - Evolution of AI: From prompt engineering to deep agents
4:33 - Enterprise AI challenge: Why productivity isn't moving
5:33 - The problem: Green (general), Orange (taught), and Red (institutional/tribal) knowledge
10:11 - The Monolith: Why institutional knowledge is often outdated or missing
11:24 - Solution introduction: Demand-driven context
13:05 - The "Pull" strategy: Learning by doing vs. pushing information
14:48 - The agent lifecycle: Problem to discovery to documentation
17:46 - Demo introduction: Using a framework for context management
19:12 - Live demo: Incident root cause analysis and context discovery
24:05 - Scaling: 14 incidents to show confidence level improvement
26:27 - Automated scale: Validating knowledge across the monolith
33:01 - Storage strategy: Why GitHub is preferred for knowledge repositories
34:47 - The Meta Model: Navigating domain relationships
36:27 - Value proposition: Knowing the unknown and managing knowledge
39:02 - Summary: The 80/20 rule and cache-based context blocks
40:15 - Workshop takeaways: Repositories and scanners
43:33 - Q&A Session: Addressing scalability, tooling, and cost

## Accelerating AI on Edge — Chintan Parikh and Weiyi Wang, Google DeepMind

- Upload date: 2026-05-05
- Video: https://www.youtube.com/watch?v=Lm8BLHkxiAo
- Transcript: raw/20260505_Lm8BLHkxiAo/Lm8BLHkxiAo.en-orig.vtt
- Metadata: raw/20260505_Lm8BLHkxiAo/Lm8BLHkxiAo.info.json

As models get smaller and more capable, more AI workloads can move onto the device itself. In this talk, Chintan Parikh from Google DeepMind walks through what that looks like in practice, from Gemma 4 edge models and on-device agent skills to the real tradeoffs around latency, privacy, cost, and cross-platform deployment.

The session covers LiteRT, the Google AI Edge stack for running models across Android, iOS, desktop, web, and IoT, along with demos of local tool calling, structured output, reasoning, benchmarking, and hardware acceleration on CPUs, GPUs, and NPUs. If you're building on-device AI systems, this is a practical overview of the current edge stack and where it is headed.

Speaker info:
- https://www.linkedin.com/in/weiyiwang1993
- https://www.linkedin.com/in/chintansparikh

## Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs

- Upload date: 2026-05-04
- Video: https://www.youtube.com/watch?v=UsB70Tf5zcE
- Transcript: raw/20260504_UsB70Tf5zcE/UsB70Tf5zcE.en-orig.vtt
- Metadata: raw/20260504_UsB70Tf5zcE/UsB70Tf5zcE.info.json

Training an LLM from scratch on a local machine sounds unreasonable, until it isn't. In this workshop, Angelos Perivolaropoulos from ElevenLabs walks through what it actually takes to train a language model locally, with a practical focus on the tooling, constraints, and engineering tradeoffs involved.

If you want a hands-on look at small-scale LLM training beyond the cloud-heavy default, this is a useful deep dive.

Speaker info:
- https://www.linkedin.com/in/angelos-perivolaropoulos/
- https://github.com/angelos-p

Timestamp:
0:00 Introduction and background of the speaker
1:21 Overview of the workshop objectives
3:12 Inspiration from Andre Karpathy's NanoGPT
4:37 The four fundamental building blocks of an LLM
7:08 Prerequisites and setup tools (UV, Python, hardware requirements)
9:06 Part 1: The Tokenizer (character-level tokenization explained)
24:29 Model architecture and parameters (vocab size, layers, embeddings)
30:13 The GPT class structure and transformer blocks
37:52 Parameter count and model sizing
40:54 The training loop: objectives and next-token prediction
44:44 Optimization and learning rate strategies (warm-up and cosine decay)
47:56 Validation and monitoring loss
53:07 Part 3: Text generation and inference strategies
56:30 Putting it all together (project file structure)
58:46 Monitoring training and debugging common issues
1:00:27 Workshop challenge and competition details
1:05:24 Q&A: Differences between base models and reasoning models
1:11:31 Q&A: Applying these concepts to audio and multimodal models

## Skill Issue: How We Used AI to Make Agents Actually Good at Supabase — Pedro Rodrigues, Supabase

- Upload date: 2026-05-04
- Video: https://www.youtube.com/watch?v=GmAQKINjv1E
- Transcript: raw/20260504_GmAQKINjv1E/GmAQKINjv1E.en-orig.vtt
- Metadata: raw/20260504_GmAQKINjv1E/GmAQKINjv1E.info.json

Writing Agent Skills is easy. Writing ones that actually improve agent performance is not.

In this hands-on workshop, you’ll build, test, and iterate on Agent Skills against real Supabase workflows using a prebuilt environment with MCP, CLI tooling, and an eval harness powered by Braintrust.

You’ll start by writing a simple Skill and observing how it changes agent behavior. Then we’ll push further: you’ll modify the Skill, introduce bad patterns, and see how performance shifts — sometimes improving, sometimes getting worse, and sometimes doing nothing at all. Along the way, we’ll surface common failure modes, like Skills that aren’t used, misleading instructions, or changes that look good but don’t hold up under evaluation.

The core loop of the workshop is simple: write a Skill, run evals, inspect results, and iterate. By the end, you’ll have a practical understanding of how to validate Skills, how to avoid common pitfalls, and how to design Skills that actually help agents perform better in real systems.

If you’re working with agents, this workshop will give you the tools to move beyond guesswork and start measuring what actually works.

And if you want to see how these patterns hold up at scale, the follow-up talk on the 9th dives into our eval results and what actually moved the needle in production.

Speaker info:
- https://supabase.com/blog/authors/pedro_rodrigues
- https://www.linkedin.com/in/pedro-neves-rodrigues/

## Ralph Loops: Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick

- Upload date: 2026-05-04
- Video: https://www.youtube.com/watch?v=2TLXsxkz0zI
- Transcript: raw/20260504_2TLXsxkz0zI/2TLXsxkz0zI.en-orig.vtt
- Metadata: raw/20260504_2TLXsxkz0zI/2TLXsxkz0zI.info.json

Dumb loops beat clever workflows. Most teams building with AI agents reach for multi-agent orchestration, planning graphs, and elaborate tool chains. Then they spend months debugging them. A single loop that processes one ticket at a time, evaluates its own output, and improves on the next run will outperform all of it.

In this hands-on workshop you will build three things. First, a working Ralph Loop that processes real tickets end-to-end. Second, a synthetic feedback loop so you can test and iterate locally without waiting on production data. Third, a self-improving cycle where the loop's output quality gets better with every run without you touching the prompt.

Speaker info:
- https://x.com/chrismdp
- https://www.linkedin.com/in/chrisparsons/
- https://github.com/chrismdp

Timestamps:
0:00 Introduction to the workshop and Ralph Loops
6:12 How AI agents work on loops
10:06 Using loops for software development
10:43 Live coding: Building a Pomodoro timer
12:13 Explaining the ticket system
15:01 Implementing the first ticket (Status command)
17:37 The simplest Ralph Loop: A while loop
22:12 Next steps and taking the concept to the next level
28:19 Implementing further tickets using TDD principles
40:33 Advanced feature: The 'loop' command in Claude Code
49:39 Structuring and managing Ralph Loops
55:33 Using sub-agents for better validation
59:39 The 'startup' skill and ambitious automation
1:04:10 Real-world application: Worker and morning loops
1:09:19 Q&A: Determining when to stop open-ended tasks
1:13:31 VCP command and project context
1:15:52 Q&A: Handling context rot
1:17:01 Q&A: Reviewing sessions and verification
1:22:38 Q&A: Versioning prompts and skills
1:27:12 Q&A: Knowledge management and system organization
1:38:34 Closing, feedback, and final questions

## Context Is the New Code — Patrick Debois, Tessl

- Upload date: 2026-05-03
- Video: https://www.youtube.com/watch?v=bSG9wUYaHWU
- Transcript: raw/20260503_bSG9wUYaHWU/bSG9wUYaHWU.en-orig.vtt
- Metadata: raw/20260503_bSG9wUYaHWU/bSG9wUYaHWU.info.json

As AI coding agents become more capable, context is starting to matter as much as code. Yet while code has version control, review, testing, CI/CD, and production observability, the prompts, rules, and memory that drive agents are still often managed like ad hoc hacks.

Patrick argues that context needs its own engineering discipline. He introduces the Context Development Lifecycle: Generate, Evaluate, Distribute, and Observe, along with the team practices that make context a shared, repeatable, and improvable part of software delivery. The session also explores the larger context flywheel, where better context leads to better agent output, which creates better observations, which in turn improves context again.

Speaker info:
- https://x.com/patrickdebois
- https://www.linkedin.com/in/patrickdebois/

Timestamps:
0:00 - Introduction to the talk
1:14 - Why context is the new code
2:37 - Introducing the Context Development Lifecycle
3:50 - Generate: Creating context for agents
6:26 - Evaluate: Testing your context
13:59 - Distribute: Sharing and packaging context
17:49 - Observe: Monitoring and feedback loops
22:33 - Conclusion and the context flywheel
24:49 - Q&A session

## TLMs: Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google

- Upload date: 2026-05-03
- Video: https://www.youtube.com/watch?v=BKWpYIWvAo4
- Transcript: raw/20260503_BKWpYIWvAo4/BKWpYIWvAo4.en-orig.vtt
- Metadata: raw/20260503_BKWpYIWvAo4/BKWpYIWvAo4.info.json

Tiny LLMs are making on-device agents much more practical. In this workshop, Cormac Brick walks through how LiteRT-LM brings language models to edge devices, with a focus on Gemma, agent skills, and the real engineering tradeoffs behind running LLM workflows on phones and other constrained hardware. The session covers performance across edge devices, on-device function calling, fine-tuning and deployment, platform support across Android and iOS, and the memory, safety, and UX constraints that shape edge-native AI systems. If you're building local agents or want a practical look at where edge LLMs are headed, this is a useful hands-on overview.

Speaker info:
- https://www.linkedin.com/in/cbrick/

Timestamps

(0:00:00) Intro: AI on the Edge, Small Language Models, and Gemma
(0:04:51) Enabling App Development: MediaPipe, LiteRT, and System Services
(0:09:09) Small Language Models: Performance, Reach, and Fine-tuning
(0:11:30) Gemma 4: Sizes (E2B and E4B) and AI Core Roadmap
(0:16:10) Gemma on Edge Runtime: Performance Benchmarks
(0:18:34) Agent Skills: Google AI Gallery, Mood Tracker, and Wikipedia Lookup
(0:23:38) Skill Architecture: Efficiency, Progressive Disclosure, and Tool Loading
(0:27:34) Reliability: Constrained Decoding and Tool Usage
(0:29:18) Community and Custom Skills
(0:31:30) Skill Development Deep Dive: Orchestrator and Registry
(0:33:30) Rapid Skill Prototyping: Using Gemini CLI and ADB
(0:38:35) Open Source: AI Edge Gallery and Community Engagement
(0:41:00) Deploying Tiny Models (sub-1B parameters) In-App
(0:47:44) Third-Party Models: Fast VLM and Hardware Acceleration
(0:50:17) Model Examples: Function Gemma, Mobile Actions, and Embedding Gemma
(0:55:41) AI Edge Eloquent: Transcription and Text Polishing
(0:59:07) Modularity Playbook: ASR and Text Polishing Engines
(1:01:23) Synthetic Data Workflows for Tiny Models
(1:06:36) Web Support and Fine-tuning Documentation
(1:08:20) Summary and Key Takeaways
(1:12:49) Q&A: Multi-skill Execution, Context Windows, and Future Roadmap

## Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked

- Upload date: 2026-05-03
- Video: https://www.youtube.com/watch?v=5ID22ACI7IM
- Transcript: raw/20260503_5ID22ACI7IM/5ID22ACI7IM.en-orig.vtt
- Metadata: raw/20260503_5ID22ACI7IM/5ID22ACI7IM.info.json

Agents can generate code. The hard part is generating code that's right for your system, team conventions, and past decisions. That's a context problem that naive RAG, MCP servers, and bigger context windows don't solve. Without the right context, that code costs you twice: once in tokens, again in long review cycles.

This session is a practitioner's guide to building a context engine: the reasoning layer that brings together your organizational context and delivers only what the agent needs for the task at hand. I'll walk through the challenges that matter: reasoning across conflicting sources, maintaining permissions, and personalizing results based on who's asking and what they're working on. Along the way, we'll go deep on specific components with live demos and technical breakdowns.

Drawn from real lessons building this in production, including what we got wrong.

## Human-in-the-Loop Automation with n8n — Liam McGarrigle

- Upload date: 2026-05-02
- Video: https://www.youtube.com/watch?v=tDArkCqjA-c
- Transcript: raw/20260502_tDArkCqjA-c/tDArkCqjA-c.en-orig.vtt
- Metadata: raw/20260502_tDArkCqjA-c/tDArkCqjA-c.info.json

What does it actually take to build an AI workflow that can do useful work without becoming a black box? This workshop shows how to build secure, human-in-the-loop automations in n8n, using a Gmail and Google Calendar management agent as the concrete example. Liam McGarrigle walks through how to wire it together with n8n's visual automation system and combine chat triggers, tools, credentials, approvals, and access control into a workflow that can actually be observed and controlled. The session also covers how to extend the agent beyond the demo, including Slack-based interaction, scheduled runs, sub-workflows, and specialized subagents for larger real-world automation systems.

Speaker info:
- https://www.linkedin.com/in/liam-mcgarrigle
- https://github.com/liamdmcgarrigle

## I Gave an AI Agent the Keys to My Life (Here's What Happened) — Radek Sienkiewicz (@velvetshark-com)

- Upload date: 2026-05-02
- Video: https://www.youtube.com/watch?v=sJ2jc7leKBk
- Transcript: raw/20260502_sJ2jc7leKBk/sJ2jc7leKBk.en-orig.vtt
- Metadata: raw/20260502_sJ2jc7leKBk/sJ2jc7leKBk.info.json

An honest look at what happens when a personal AI agent is allowed to operate around the clock. Over months, one permission at a time, it went from reading files to handling email, backing up its own memory at 2am, monitoring its own health, and drafting real business replies. This talk covers the permission creep, the overnight cron ecosystem, self-monitoring and recovery, trust boundaries, and the surprising value of giving an agent a personality that disagrees with its owner.

Speaker info:
- https://x.com/velvet_shark
- https://www.linkedin.com/in/radeksienkiewicz/
- https://github.com/velvetshark

Timestamps
0:15 Radek's path to OpenClaw
2:17 The philosophy of incremental growth and system updates
4:51 Integrating the Obsidian knowledge base
8:59 Ambient operations and overnight automation
11:02 Core job types for the AI agent (Ambient Operations, Attention Filtering, Execution)
13:03 Deep dive into specific Discord integration channels
14:54 System architecture: LLMs, scripts, and memory management
16:28 Challenges: Bad memory, brittle automations, and noisy nodes
17:19 Conclusion: Optimizing for the future self

## Software Engineering Is Becoming Plan and Review — Louis Knight-Webb, Vibe Kanban

- Upload date: 2026-05-02
- Video: https://www.youtube.com/watch?v=W76woOYHlvY
- Transcript: raw/20260502_W76woOYHlvY/W76woOYHlvY.en-orig.vtt
- Metadata: raw/20260502_W76woOYHlvY/W76woOYHlvY.info.json

AI eats the middle, software engineers are spending all their time planning and reviewing the work of AI. If all humans are going to do is plan and review the work of AI, the biggest lever you have to ship more is to speed up planning and review.

And some examples of how teams and individuals are adapting:
- What tools are people spending their time in?
- How much time are teams spending reviewing code, how has this changed since AI?
- What are different approaches to planning work?
- Is agile and scrum dead?

Speaker info:
- https://x.com/tokengobbler
- https://www.linkedin.com/in/knightwebb/
- https://github.com/stunningpixels

Timestamps:
0:00 - Intro and agenda
1:45 - Why software engineering is shifting to plan and review
3:30 - The two approaches: Plan-based vs. Review-heavy
6:02 - The matrix: Feature development vs. migrations and maintenance
7:27 - The impact of agent execution time
9:52 - Managing the 'five-minute' agent threshold
10:29 - Parallelization and workflow management
12:00 - Vision for future coding interfaces and 'focus maxing'
14:00 - Announcement: Shutting down Vibe Kanban
18:13 - Q&A: Next steps and reflections on the startup journey

## Agents for Everything Else — swyx

- Upload date: 2026-05-01
- Video: https://www.youtube.com/watch?v=zepu8Kk6FBQ
- Transcript: raw/20260501_zepu8Kk6FBQ/zepu8Kk6FBQ.en-orig.vtt
- Metadata: raw/20260501_zepu8Kk6FBQ/zepu8Kk6FBQ.info.json

How we run AI Engineer with Agents like Cognition's Devin and Town Assistant

Speaker info:
- x.com/swyx
- github.com/swyxio

## Agents on the Canvas in tldraw — Steve Ruiz, tldraw

- Upload date: 2026-05-01
- Video: https://www.youtube.com/watch?v=sPUjIBH5Cwg
- Transcript: raw/20260501_sPUjIBH5Cwg/sPUjIBH5Cwg.en-orig.vtt
- Metadata: raw/20260501_sPUjIBH5Cwg/sPUjIBH5Cwg.info.json

At tldraw, we've been bringing agents to our infinite canvas. In December 2025, we ran a one-month experiment named Fairydraw where users could work with three fairies—virtual collaborators who work with you, with your human collaborators, and coordinate together on large tasks. Learn what we learned.

Speaker info:
- https://x.com/steveruizok
- https://www.linkedin.com/in/steve-ruiz-61a150239/

## Shipping complex AI applications — Braintrust & Trainline

- Upload date: 2026-05-01
- Video: https://www.youtube.com/watch?v=ZdheJTfLu-s
- Transcript: raw/20260501_ZdheJTfLu-s/ZdheJTfLu-s.en-orig.vtt
- Metadata: raw/20260501_ZdheJTfLu-s/ZdheJTfLu-s.info.json

Getting a prototype working is straightforward. Making it reliable in production, especially with multi-step agents, tool use, and real users is the hard part. In this hands-on workshop, you'll work through the core parts of building production-grade AI applications with Giran Moodley, Mayank Soni, and Oussama Hafferssas.

Socials: 
- https://uk.linkedin.com/in/mayank-soni
- https://x.com/OussamaHaff
- https://www.linkedin.com/in/giran/

Timestamps

0:00 - Introduction and Welcome
4:07 - Workshop Overview and Agenda
4:39 - Understanding AI Engineering and Operational Challenges
9:55 - Introduction to Braintrust
12:56 - Experience from Trainline
28:35 - Building the Support Triage Agent (Overview)
33:57 - Basic Implementation: Single Shot Prompting
40:32 - Adding Local Tools for Determinism
41:30 - Implementing Specialist Stages (Agentic Flow)
46:19 - Instrumenting and Tracing the Application
56:43 - Evaluating AI Systems and Golden Data Sets
1:05:07 - Deploying and Managing AI in Production
1:13:58 - Online Scoring and Monitoring Production Logs
1:19:13 - Identifying and Remediating Failure Modes
1:33:05 - Key Takeaways and Summary
1:36:58 - Further Resources and Documentation

## Mastering AI Pricing — Mayank Pant, Stripe

- Upload date: 2026-05-01
- Video: https://www.youtube.com/watch?v=CrqPcIZOOXA
- Transcript: raw/20260501_CrqPcIZOOXA/CrqPcIZOOXA.en-orig.vtt
- Metadata: raw/20260501_CrqPcIZOOXA/CrqPcIZOOXA.info.json

Monetizing AI is hard. Rising GPU and inference costs are squeezing margins, and traditional SaaS pricing simply does not work for the unpredictable compute demands of new-age AI companies. With models constantly shifting across credits, tokens, and seats, a new challenge emerges: how do we charge for AI without stalling growth? This talk presents a framework for solving the dual problems of aligning charge metrics with true customer value and balancing predictable revenue with rapid adoption. Through real-world examples, we'll explore how to build guardrails that protect your margins and see how Stripe's world-class usage-based billing solution helps AI companies launch quickly and monetize with ultimate agility. Whether you're launching your first AI product or revamping your current model, you'll learn how to make your pricing strategy both profitable and adaptable.

## LLM codegen fails and how to stop 'em — Danilo Campos, PostHog

- Upload date: 2026-04-30
- Video: https://www.youtube.com/watch?v=juoNbJiZUi0
- Transcript: raw/20260430_juoNbJiZUi0/juoNbJiZUi0.en-orig.vtt
- Metadata: raw/20260430_juoNbJiZUi0/juoNbJiZUi0.info.json

Danilo Campos breaks down the most common failure modes in LLM code generation and the practical strategies PostHog uses to prevent them. Drawing from a system that helps 5,000+ users each month, he shares a playbook for making autonomous codegen more reliable, correct, and production-ready.

Speaker info:
- https://www.linkedin.com/in/danilocampos

## Building Conversational Agents — Thor Schaeff and Philipp Schmid, Google DeepMind

- Upload date: 2026-04-30
- Video: https://www.youtube.com/watch?v=cVzf49yg0D8
- Transcript: raw/20260430_cVzf49yg0D8/cVzf49yg0D8.en-orig.vtt
- Metadata: raw/20260430_cVzf49yg0D8/cVzf49yg0D8.info.json

Thor Schaeff and Philipp Schmid show how to build conversational agents with Google DeepMind's Gemini APIs, from tool-using coding agents to realtime voice interfaces. The session covers the new Interactions API, agent skills, server-side state, and the Live API workflow for streaming audio, video, and tool calls into multimodal assistants.

Speaker info:
- https://x.com/_philschmid
- https://x.com/thorwebdev

Timestamps
0:14 - Introduction and speaker introductions
6:15 - Audience interaction and project discussions
8:38 - Introduction to building conversational agents
28:17 - Discussion on Gemini Flash for coding and agentic use
36:28 - Coding agent implementation and tool calling demonstration
42:55 - Overview of the Interactions API and state management
49:05 - Introduction to the Gemini Live API
50:02 - Live Jukebox demo with music generation
54:49 - Deep dive into Gemini Flash Live features (multimodality, latency, tools)
1:06:54 - Technical setup and implementation of the Live API using WebSockets
1:25:14 - Session management and context window compression
1:26:57 - Real-world business use cases for conversational agents
1:35:02 - Multimodal grounding and handling audio inputs
1:40:00 - Discussion on personalization and speaker identification

## Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor

- Upload date: 2026-04-30
- Video: https://www.youtube.com/watch?v=WE_Gnowy3uw
- Transcript: raw/20260430_WE_Gnowy3uw/WE_Gnowy3uw.en-orig.vtt
- Metadata: raw/20260430_WE_Gnowy3uw/WE_Gnowy3uw.info.json

David Gomes shows how Cursor replaced a heavyweight WorkTrees feature with a lightweight layer built from skills, commands, and subagents. He walks through how parallel coding workflows were recreated with roughly 200 lines of Markdown, plus the tradeoffs, failure modes, and lessons that come with moving product behavior from code into prompts.

Speaker info:
- https://x.com/davidgomes
- https://github.com/davidgomes/

Timestamps
0:14 Introduction and the concept of markdown as code
0:59 Recap of Git work trees in Cursor
3:10 Complexity of the initial implementation
4:18 Deleting 15,000 lines of code
4:54 Implementing features with Skills and Sub-agents
5:51 How the new Skills are structured
7:58 New Slash commands and workflow
9:58 Pros of the new implementation
12:15 Cons and user feedback challenges
14:17 Future improvements: Evals and RL training
17:05 What's next for Cursor 3.0 and native work trees

## Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI

- Upload date: 2026-04-29
- Video: https://www.youtube.com/watch?v=fLUtUkqYHnQ
- Transcript: raw/20260429_fLUtUkqYHnQ/fLUtUkqYHnQ.en-orig.vtt
- Metadata: raw/20260429_fLUtUkqYHnQ/fLUtUkqYHnQ.info.json

A new class of small models is emerging with the ability to reliably follow instructions and call tools while running on-device under 1 GB of memory. In this talk, we'll break down how to post-train frontier small models using the LFM2.5 recipe: on-policy preference alignment, agentic reinforcement learning, and curriculum training with iterative model merging. We'll cover training challenges unique to the 1B scale, like doom loops, capability interference, and how to fix them. The goal is to give you a concrete playbook to fine-tune and deploy small models for your own use cases, from structured data extraction to multi-turn tool use.

Speaker info:
- https://x.com/maximelabonne
- https://www.linkedin.com/in/maxime-labonne/
- https://github.com/mlabonne

Timestamps:
0:00:00 - Start
0:00:14 - Introduction to frontier small models at Liquid AI
0:01:02 - Characteristics: memory-bound, task-specific, latency-sensitive
0:02:20 - Architecture: why large embedding layers are inefficient
0:04:01 - LFM2 architecture: using gated short convolutions for speed
0:06:09 - LFM 2.5 recipe: 28T tokens and post-training stages
0:08:34 - Post-training: SFT, preference alignment, and RL best practices
0:10:43 - Identifying "doom loops" in reasoning models
0:11:34 - Solutions: mitigating loops via preference alignment and RL
0:15:29 - Future focus: using agentic tools to overcome memory limits
0:17:58 - Q&A: real-world applications for small vs. large models

## OpenAI Codex Masterclass  — Vaibhav Srivastav & Katia Gil Guzman

- Upload date: 2026-04-29
- Video: https://www.youtube.com/watch?v=MhHEGMFCEB0
- Transcript: raw/20260429_MhHEGMFCEB0/MhHEGMFCEB0.en-orig.vtt
- Metadata: raw/20260429_MhHEGMFCEB0/MhHEGMFCEB0.info.json

Codex is no longer just a coding assistant in a terminal. In this workshop, Vaibhav and Katia show how it becomes a full software engineering system, combining frontier models, the Codex app and CLI, plugins, automations, and subagents that can explore, review, and execute work in parallel. The session also dives into custom subagents: showing how specialized agents with different models, permissions, and tools can speed up code review, research, debugging, and long-running tasks while keeping control and safety in place.

Speaker info:
- Vaibhav Srivastav | https://x.com/reach_vb
- Katia Gil Guzman | https://www.linkedin.com/in/katiagilguzman/

Timestamps
(0:14) Introduction to the workshop and speakers
(1:48) What is Codex? (Overview of software engineering agent capabilities)
(2:18) Foundation models (GPT-5.3, Spark, GPT-5.4)
(4:11) The evolution of models and performance improvements (Websockets, Fast Mode)
(7:04) Codex app features, projects, and work trees
(8:37) Automations overview
(12:28) Plugins: Skills, apps, and MCP servers
(15:13) Game and Web development plugins (Playwright and Image Gen)
(16:26) Demo: Game studio plugin and generating assets
(17:23) Demo: Google Drive plugin for codebase data
(18:52) Demo: Setting up automations for Slack and Gmail
(27:14) Code Review features and integration with GitHub
(32:39) Subagents: Parallelizing tasks and custom personas
(36:18) Demo: Using subagents to review persona files
(44:52) Creating custom subagents
(49:29) Bleeding edge features: Guardian approvals, hooks, and personality settings
(56:11) Codex security and Cloud Code plugin
(57:10) Q&A session

## Build & deploy AI-powered apps — Paige Bailey, Google DeepMind

- Upload date: 2026-04-29
- Video: https://www.youtube.com/watch?v=G_bHFmEAarM
- Transcript: raw/20260429_G_bHFmEAarM/G_bHFmEAarM.en-orig.vtt
- Metadata: raw/20260429_G_bHFmEAarM/G_bHFmEAarM.info.json

Got a massive idea but stuck in the "just talking about it" phase? This session cuts the fluff and dives straight into how to build and prototype at lightning speed using AI Studio Build and Antigravity for free. It breaks down Google DeepMind's AI tech stack so viewers know exactly which tools to use, when to reach for heavyweights like Gemini 3.1 Pro or the new Gemma 4, and when to stay fast with Gemini 3 Flash and Flash-Lite. It also explores Veo 3.1 Lite for video generation, NanoBanana 2, Lyria 3 for music generation, Genie 3 for world model building, and OpenClaw with Gemini to push prototype limits. Expect basically zero slides and more shipping, with live demos showing how to turn side quests from ideas into working prototypes, add new features to existing codebases, and troubleshoot builds and ideas in a live Q&A.

Speaker info:
- https://x.com/DynamicWebPaige
- https://linkedin.com/in/dynamicwebpaige
- https://github.com/dynamicwebpaige

## Building your own software factory — Eric Zakariasson, Cursor

- Upload date: 2026-04-28
- Video: https://www.youtube.com/watch?v=rnDm57Py54A
- Transcript: raw/20260428_rnDm57Py54A/rnDm57Py54A.en-orig.vtt
- Metadata: raw/20260428_rnDm57Py54A/rnDm57Py54A.info.json

Most of us are pair-programming with one agent and stopping there. There's a lot more on the table. This workshop is about going from one agent to many. We'll start with codebase setup, the foundational work that makes agents effective on their own. Then we'll scale up to running agents in parallel, kicking off async work that keeps going while you context-switch to something else, and setting up automations for the things you're still doing by hand.

Speaker info:
- https://x.com/ericzakariasson
- https://www.linkedin.com/in/ericzakariasson/
- https://github.com/ericzakariasson

Timestamps:
0:00:00 - Workshop introduction and vision for autonomous software factories
0:01:26 - Frameworks and stages of agentic autonomy
0:08:58 - Establishing scalable, reproducible dev environments for agents
0:10:00 - Importance of verifiable systems and automated testing pipelines
0:10:47 - Cursor 3 walkthrough: Redesigned agent-first interface
0:15:26 - Cloud agents: Scaling via dedicated VMs and computer control
0:19:17 - Managing asynchronous workflows and frontloading context
0:24:45 - Automating repetitive tasks to build feedback loops
0:29:28 - Continual learning: Extracting rules from chat transcripts
0:30:48 - Scaling management: Moving to nested agent orchestration
0:31:08 - Strategic takeaways: Human accountability and observability
0:33:39 - Q&A: Addressing code quality and architectural guardrails
0:53:07 - Best practices for human-to-agent collaboration and handoffs
1:03:05 - Maintaining the factory: Managing documentation and specs
1:10:06 - Integrating Linear and Slack for automated issue triage
1:14:14 - Local execution: Leveraging Cursor harness locally

## Why building eval platforms is hard — Phil Hetzel, Braintrust

- Upload date: 2026-04-28
- Video: https://www.youtube.com/watch?v=_fQ7Z_Wfouk
- Transcript: raw/20260428__fQ7Z_Wfouk/_fQ7Z_Wfouk.en-orig.vtt
- Metadata: raw/20260428__fQ7Z_Wfouk/_fQ7Z_Wfouk.info.json

An eval platform is not just a test runner. You are building shared definitions of "good," reliable data pipelines, labelling workflows, versioning, and trust in results across many teams and model changes. This session breaks down the hidden complexity, the common failure modes, and the design principles that make evals credible and usable in day-to-day engineering.

Speaker info:
- https://www.linkedin.com/in/philliphetzel/

## One Login to Rule Them All: Cross-App Access for MCP — Garrett Galow, WorkOS

- Upload date: 2026-04-28
- Video: https://www.youtube.com/watch?v=EmhRyw6xeT0
- Transcript: raw/20260428_EmhRyw6xeT0/EmhRyw6xeT0.en-orig.vtt
- Metadata: raw/20260428_EmhRyw6xeT0/EmhRyw6xeT0.info.json

Connecting a coding agent to multiple services often means facing a dozen OAuth consent screens, a dozen token lifecycles, and a dozen chances for something to break. Despite having Single Sign-On, users still find themselves signing in repeatedly.

This talk explores how Cross-App Access leverages a three-way trust between the MCP client, the MCP server, and the organization's Identity Provider to simplify authentication. Through the Identity Assertion Authorization Grant flow, a single SSO login is transformed into access tokens across every MCP server, offering seamless access to all applications. The session will also highlight what this pattern enables for agent identity beyond MCP.

Speaker info:
https://www.linkedin.com/in/garrett-galow/

## Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind

- Upload date: 2026-04-27
- Video: https://www.youtube.com/watch?v=_A367W_qvc8
- Transcript: raw/20260427__A367W_qvc8/_A367W_qvc8.en-orig.vtt
- Metadata: raw/20260427__A367W_qvc8/_A367W_qvc8.info.json

Open models are getting smaller, faster, and far more capable. In this talk, Cassidy Hardin walks through the latest advances in the Gemma family, with a focus on Gemma 4 and what it enables for developers building on-device and open-weight AI systems. She covers the architecture behind Gemma’s dense, effective, and mixture-of-experts models, including improvements to attention, multimodal support for text, vision, and audio, and the design decisions that make strong reasoning, coding, and agentic workflows possible at practical sizes.

Speaker info:
- https://uk.linkedin.com/in/cassidyhardin

Timestamps:
00:00:28 - Introduction to the Gemma 4 model family and its four size categories
00:01:54 - Shift to Apache 2.0 licensing for developer accessibility
00:02:25 - Deep dive into the 31B dense reasoning and 26B mixture-of-experts (MoE) models
00:03:30 - Overview of on-device effective models (2B and 4B) with multimodal support
00:04:21 - Architectural updates: interleaved local/global attention and grouped query attention
00:06:51 - Explanation of the new MoE architecture (128 experts, 8 active)
00:07:44 - Implementation of Per Layer Embeddings (PLE) to optimize on-device memory
00:11:06 - Multimodal advances: variable aspect ratios and resolutions for vision encoders
00:16:31 - Audio processing enhancements via conformer architecture and audio tokenizers
00:18:07 - Getting started: self-hosting (Hugging Face, Ollama) and cloud deployment (Vertex AI)

## Gateways are All You Need — Karan Sampath, Anthropic

- Upload date: 2026-04-27
- Video: https://www.youtube.com/watch?v=CD6R4Wf3jnY
- Transcript: raw/20260427_CD6R4Wf3jnY/CD6R4Wf3jnY.en-orig.vtt
- Metadata: raw/20260427_CD6R4Wf3jnY/CD6R4Wf3jnY.info.json

MCPs are often flaky, face multiple security vulnerabilities, and are generally hard to scale. Most enterprises struggle to use more than single digit numbers of MCPs due to issues with security, observability, and access control. In this talk, we'll explore the approaches and learnings we at Anthropic have been taking to solve this, and make MCPs more enterprise ready.

Speaker info:
- https://x.com/karan_sampath
- https://www.linkedin.com/in/karansampath/
- https://github.com/karansampath

Timestamps:
00:00:14 - Introduction: Enterprise MCP challenges.
00:01:13 - Enterprise Hurdles: Observability, access control, and security (the "three-headed hydra").
00:03:35 - Deployment Bottlenecks: Scalability limits of current decentralized models.
00:05:35 - The Case for Gateways: Establishing a unified "root of trust."
00:07:00 - Gateway Definition: A middleware layer for auth, proxying, and routing.
00:08:28 - Core Components: Implementing OAuth, tunnels, and developer CLIs.
00:10:03 - Strategic Benefits: Improved authentication and standardized access control.
00:11:30 - Operational Gains: Multi-surface integration, security, and faster iteration.
00:15:13 - Future Vision: Decoupling agent architecture from data layers.
00:16:58 - Summary: Invest in common infrastructure to scale enterprise agents.

## Scaling GitHub for your Agents — Sam Morrow, GitHub

- Upload date: 2026-04-27
- Video: https://www.youtube.com/watch?v=0n3MKk7r60w
- Transcript: raw/20260427_0n3MKk7r60w/0n3MKk7r60w.en-orig.vtt
- Metadata: raw/20260427_0n3MKk7r60w/0n3MKk7r60w.info.json

GitHub operates one of the most heavily-utilised MCP servers in the ecosystem, with over 4 million downloads of the stdio server alone. Discover the architectural decisions, technical challenges and lessons learned while building and scaling a remote MCP server on production infrastructure. The session walks through the journey from initial implementation to horizontal scaling, covering the specific challenges of condensing a platform as expansive as GitHub into a coherent MCP interface. Attendees will learn practical strategies for managing tool overload, optimizing context usage, implementing distributed session storage, and maintaining observability without compromising user privacy. Whether building a first remote server or optimizing an existing implementation, attendees will gain concrete patterns, anti-patterns, and architectural guidance from real production experience.

Key Takeaways:
• Architecture patterns for stateless, horizontally scalable remote MCP servers
• Practical approaches to tool proliferation and context window constraints
• Why a focus on auth, security and privacy is essential to success

Speaker info:
https://www.linkedin.com/in/sammorrow
https://github.com/SamMorrowDrums

Timestamps:
0:00:29 - Overview of GitHub's MCP public launch and community growth.
0:02:06 - Challenges of tool proliferation and impact on agent context.
0:03:21 - Mitigation via "tool sets" and dynamic discovery.
0:05:54 - Optimizing API output tokens to improve efficiency.
0:06:44 - Improving reliability through intent-based tool design.
0:08:14 - Security strategy: OAuth 2.1 and PKCE implementation.
0:10:40 - Managing prompt injection and security vulnerabilities.
0:12:35 - Using OAuth scopes for granular tool filtering.
0:13:47 - Stateless server architecture and Redis session management.
0:15:18 - Experimental features and human-in-the-loop UX.
0:16:30 - Future outlook: Compositional tools and automation.
0:18:04 - Final project metrics: Downloads, forks, and volume.

## Collaborative AI Engineering: One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub

- Upload date: 2026-04-26
- Video: https://www.youtube.com/watch?v=ClWD8OEYgp8
- Transcript: raw/20260426_ClWD8OEYgp8/ClWD8OEYgp8.en-orig.vtt
- Metadata: raw/20260426_ClWD8OEYgp8/ClWD8OEYgp8.info.json

Agentic engineering so far has been a solo story: one developer and a dozen agents moving at warp speed. But speed without thoughtful planning and team alignment is just wasting tokens. When everyone on a team is directing agents alone in their personal CLI tools with no shared context, you get duplicate work, conflicting changes, poorly-designed solutions, surprise features nobody else agreed to build, and everyone pulling in different directions.

Serious software still requires serious collaboration. You need multiple perspectives and types of expertise to build great things. We need agentic environments where people can plan together, think critically together, and share the same context. In this talk I'll demo how we've tackled these design problems in Ace, a multiplayer agent environment from GitHub Next that uses real-time collaboration, proactive agents, and sandboxed micro VMs for rapid prototyping and exploration.

Speaker info:
- https://x.com/Mappletons

## AgentCraft: Putting the Orc in Orchestration — Ido Salomon

- Upload date: 2026-04-25
- Video: https://www.youtube.com/watch?v=kR64LOqBBCU
- Transcript: raw/20260425_kR64LOqBBCU/kR64LOqBBCU.en-orig.vtt
- Metadata: raw/20260425_kR64LOqBBCU/kR64LOqBBCU.info.json

As we run more agents in parallel, it becomes clear: we are the bottleneck. Luckily, the skills we need for effective multi-agent orchestration aren’t entirely new, they’ve just been hiding in unexpected places.Through AgentCraft, the game-inspired agent orchestrator, I’ll explore how we can raise the ceiling of human-agent collaboration without burning out in the process.

Speaker info:
- https://github.com/idosal
- https://www.linkedin.com/in/ido-salomon/
- https://x.com/idosal1

## MCP = Mega Context Problem - Matt Carey

- Upload date: 2026-04-25
- Video: https://www.youtube.com/watch?v=YBYUvGOuotE
- Transcript: raw/20260425_YBYUvGOuotE/YBYUvGOuotE.en-orig.vtt
- Metadata: raw/20260425_YBYUvGOuotE/YBYUvGOuotE.info.json

The best MCP server is the one you didn't have to build.

At Cloudflare we have a lot of products. Our REST OpenAPI spec is over 2.3 million tokens. When teams started building MCP servers, they did what everyone does: cherry-picked important endpoints for their product, wrote some tool definitions and shipped a separate service that covered a small fraction of their API.

This was driven by a fundamental context limit of the end users' agent. And tools use a bunch of context just to describe themselves. MCP felt like a Mega Context Problem (and a separate service to maintain).

I think we got it all wrong.

The context limit is not an MCP problem. It's an agent problem. Tools should probably be discovered on demand and clients are coming around to this. But maybe we can also do it on the server?

CLIs get this for free, self-discoverable and documented by design. APIs just need a little help.

This talk will cover some of the techniques we've been exploring at Cloudflare, such as codemode and tool search, to make complete APIs accessible to agents through MCP.

I'll also cover some of the work we are doing with the MCP Typescript SDK to make stateless servers the default.

Speaker info:
- https://github.com/mattzcarey
- https://www.linkedin.com/in/mattzcarey/
- https://x.com/mattzcarey

## What Do Models Still Suck At? - Peter Gostev, Arena.ai, BullshitBench

- Upload date: 2026-04-24
- Video: https://www.youtube.com/watch?v=R7A8rX-09Zw
- Transcript: raw/20260424_R7A8rX-09Zw/R7A8rX-09Zw.en-orig.vtt
- Metadata: raw/20260424_R7A8rX-09Zw/R7A8rX-09Zw.info.json

What type of real world model responses do users still hate? We get to see millions of user's prompts - and we let users 'dislike both' on the Arena. We'll show you trends and examples of the tasks that LLMs still suck at despite the relentless hillclimbing.

Speaker info:
- https://x.com/petergostev
- https://www.linkedin.com/in/peter-gostev/

## Full Walkthrough: Workflow for AI Coding — Matt Pocock

- Upload date: 2026-04-24
- Video: https://www.youtube.com/watch?v=-QFHIoCo-Ko
- Transcript: raw/20260424_-QFHIoCo-Ko/-QFHIoCo-Ko.en-orig.vtt
- Metadata: raw/20260424_-QFHIoCo-Ko/-QFHIoCo-Ko.info.json

Matt will be back on stage at the World's Fair next week! see https://ai.engineer/wf and use YOUTUBEPROMO for new tickets only. Join 6000 AI engineers at the "Superbowl of AI"!

---

A hands-on workshop covering the full lifecycle of AI-assisted development, from turning ambiguous requirements into agent-ready plans to running autonomous coding agents that ship production features.

You'll learn to stress-test vague briefs into structured PRDs, slice work into thin "tracer bullet" vertical slices, and run an AI agent with TDD. You'll watch it select tasks, write tests, implement code, and commit. You'll then refine your prompts based on where it struggles, graduate to fully autonomous (AFK) runs, and learn to design codebases that maximize agent effectiveness.

You'll walk away knowing how to:

- Turn ambiguous requirements into agent-ready issues
- Slice work into vertical tracer bullets an agent can grab independently
- Run AI agents human-in-the-loop and autonomously with TDD
- Design codebase architectures that AI agents love to work in

For: Engineers ready to move beyond chat-based AI assistance and build a real workflow for shipping features with autonomous coding agents.

Speaker info:
- https://x.com/mattpocockuk
- https://www.linkedin.com/in/mapocock/
- https://youtube.com/@mattpocockuk

Timestamps:
00:00:00 - Introduction
00:00:14 - The Thesis of AI Engineering
00:04:20 - Phase 1: Research & Prototyping
00:12:45 - Phase 2: The Grill Session
00:22:10 - Phase 3: Writing the PRD
00:35:50 - Phase 4: Slicing Work into Issues
00:48:15 - Phase 5: Implementation with AI Agents
01:05:30 - Phase 6: Human-in-the-Loop Review
01:18:45 - Phase 7: Deployment & Monitoring
01:28:10 - Designing Codebases for AI Effectiveness
01:34:06 - Final Takeaways & Summary

## "Software Fundamentals Matter More Than Ever" — Matt Pocock

- Upload date: 2026-04-23
- Video: https://www.youtube.com/watch?v=v4F1gFy-hqg
- Transcript: raw/20260423_v4F1gFy-hqg/v4F1gFy-hqg.en-orig.vtt
- Metadata: raw/20260423_v4F1gFy-hqg/v4F1gFy-hqg.info.json

Matt will be back on stage at the World's Fair next week! see https://ai.engineer/wf and use YOUTUBEPROMO for new tickets only. Join 6000 AI engineers at the "Superbowl of AI"!

---

AI coding tools are overhyped and powerful at the same time. Used well, they're extraordinary. Used badly, they'll bury you in spaghetti code faster than any human team could. The difference isn't the tool. It's the process. After 18 months of teaching developers to build with AI agents, Matt Pocock has watched the same patterns emerge: the devs who succeed aren't the ones who delegate everything or nothing. They're the ones who fall back on engineering fundamentals. In this talk, he shares the iterative process his students use to ship high-quality applications with AI agent swarms, and why the principles that make it work (ubiquitous language, vertical slices, TDD, deep modules) are decades-old ideas that didn't break. They got more important.

Speaker info:
- https://x.com/mattpocockuk
- https://www.linkedin.com/in/mapocock/

## The End of Apps — Kitze, Sizzy.co

- Upload date: 2026-04-23
- Video: https://www.youtube.com/watch?v=4fntwuOoedA
- Transcript: raw/20260423_4fntwuOoedA/4fntwuOoedA.en-orig.vtt
- Metadata: raw/20260423_4fntwuOoedA/4fntwuOoedA.info.json

Speaker info:
- https://x.com/thekitze
- https://www.linkedin.com/in/kitaborovskis/

## Agents need more than a chat - Jacob Lauritzen, CTO Legora

- Upload date: 2026-04-22
- Video: https://www.youtube.com/watch?v=XNtkiQJ49Ps
- Transcript: raw/20260422_XNtkiQJ49Ps/XNtkiQJ49Ps.en-orig.vtt
- Metadata: raw/20260422_XNtkiQJ49Ps/XNtkiQJ49Ps.info.json

Jacob Lauritzen is CTO at Legora, the fastest growing legal tech startup in history.

Speaker info:
- https://www.linkedin.com/in/jacob-lauritzen/
- https://github.com/Jacse

## Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind

- Upload date: 2026-04-21
- Video: https://www.youtube.com/watch?v=xOP1PM8fwnk
- Transcript: raw/20260421_xOP1PM8fwnk/xOP1PM8fwnk.en-orig.vtt
- Metadata: raw/20260421_xOP1PM8fwnk/xOP1PM8fwnk.info.json

https://sander.ai/2025/04/15/latents.html

Speaker info:
- https://sander.ai/
- https://github.com/benanne
- https://www.linkedin.com/in/sanderdieleman
- https://x.com/sedielem

Timestamps
0:00 Introduction
2:55 Data Curation
4:02 Representation
9:39 Modeling: Diffusion Mechanism
20:01 Network Architecture
22:25 Training at Scale
23:33 Sampling & Guidance
28:03 Distillation
30:03 Control Signals

## Taste & Craft: A Conversation with Tuomas Artman, CTO Linear & Gergely Orosz, @pragmaticengineer

- Upload date: 2026-04-21
- Video: https://www.youtube.com/watch?v=wjk0ulMAkbc
- Transcript: raw/20260421_wjk0ulMAkbc/wjk0ulMAkbc.en-orig.vtt
- Metadata: raw/20260421_wjk0ulMAkbc/wjk0ulMAkbc.info.json

Tuomas Artman is Cofounder and CTO of Linear.

- https://x.com/artman
- https://www.linkedin.com/in/tuomasartman/

Timestamps
0:00 Introduction
0:36 The danger of shipping features too quickly with AI
3:52 How Linear approaches feature requests and development
6:43 Thoughts on Anthropic's Claude Code
7:59 The challenge of measuring software quality
11:57 Quality Wednesdays at Linear
16:24 The zero bug policy explained
19:44 AI agents and the lack of human "taste" in design
22:21 Building a culture of product-focused engineering
26:23 The future role of software engineers as "product engineers"
27:56 Closing advice for aspiring product engineers

## How AI is changing Software Engineering: A Conversation with Gergely Orosz, @pragmaticengineer

- Upload date: 2026-04-21
- Video: https://www.youtube.com/watch?v=CS5Cmz5FssI
- Transcript: raw/20260421_CS5Cmz5FssI/CS5Cmz5FssI.en-orig.vtt
- Metadata: raw/20260421_CS5Cmz5FssI/CS5Cmz5FssI.info.json

Gergely Orosz is a formar Uber and Skyscanner engineer and is the author of https://www.engguidebook.com/ and https://www.pragmaticengineer.com/ , the #1 software/AI engineering newsletter on Substack, built from scratch in Amsterdam but read by millions around the world.

Speaker info:
- https://x.com/GergelyOrosz
- https://nl.linkedin.com/company/the-pragmatic-engineer

Timestamps:
0:00 What is token maxing?
5:27 Is AI-driven productivity worth the hype?
12:42 How the role of the software engineer is changing
14:45 Are engineers now engineering managers for AI?
17:31 Large tech infrastructure and internal AI tooling
20:41 Why companies like Shopify invest heavily in AI churn
22:56 Growing The Pragmatic Engineer and finding product-market fit

## Full Workshop: Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi

- Upload date: 2026-04-20
- Video: https://www.youtube.com/watch?v=mYSRn6PC1mc
- Transcript: raw/20260420_mYSRn6PC1mc/mYSRn6PC1mc.en-orig.vtt
- Metadata: raw/20260420_mYSRn6PC1mc/mYSRn6PC1mc.info.json

Deep research is one of the best ways to learn how to build real AI systems because it forces you to combine reasoning, planning, autonomy, tools, grounding, and feedback loops in a single end-to-end workflow. In this hands-on workshop, you will build an MCP-powered deep research agent that can plan a research strategy, search the web, analyze YouTube videos, gather grounded evidence, filter for relevance and trustworthiness, and synthesize its findings into a cited research artifact. Rather than treating research as just another chatbot interaction, we will frame it as a goal-directed research loop: one that can search, inspect, pivot, and progressively refine its understanding of a topic.

From there, we will connect that research artifact to a lightweight technical writing workflow that turns raw findings into polished, non-sloppy technical multimodal content. This second part of the system is deliberately more constrained: you will see how research and writing require much different architectures, why exploratory work benefits from agentic behavior, and why writing quality often improves with tighter workflows, review loops, and explicit guidance. Along the way, we will show how to choose between prompts, workflows, and agents depending on the task, and how to keep the overall system practical rather than over-engineered.

We will also cover observability and evaluation so the system is not only impressive in a demo, but measurable and improvable in practice. Most importantly, the workshop is grounded in experience: it distills what we learned over the past year building and using this research-and-writing pipeline internally. Attendees will leave with their own deep research agent, connecting it to a reliable technical writing workflow, and understanding the engineering tradeoffs behind both.

Speaker info:
- https://x.com/Whats_AI
- https://www.linkedin.com/in/pauliusztin
- https://www.linkedin.com/in/samridhivaid/

Timestamps
(00:00) Introduction and problem space (LinkedIn content and AI slop)
(03:39) Workshop overview and goals
(05:01) Speaker introductions
(06:09) AI engineering problem space and constraints
(30:14) Tech stack and tools (Scraping, Gemini grounding, YouTube/GitHub processing)
(33:32) MCP-based research agent architecture overview
(34:46) Deep research agent design and tools
(40:01) Code walkthrough: MCP server setup and tool registration
(43:35) Deep research tool implementation and prompting
(45:06) Analyze YouTube video tool implementation
(47:39) Compile research tool implementation
(53:35) Live demo: Running the research agent
(59:56) Agent skills and workflow prompting
(1:10:35) Introduction to technical writing workflow
(1:15:46) Writing guidelines and control techniques
(1:19:06) Few-shot prompting for writing
(1:21:28) Evaluator-optimizer pattern (Writer/Reviewer)
(1:28:16) Running the writing post skill
(1:34:46) Observability and tracing with Opik
(1:41:44) LLM Judge implementation and evaluation
(1:47:56) Dataset management and F1 score computation

## Running LLMs on your iPhone: 40 tok/s Gemma 4 with MLX — Adrien Grondin, Locally AI

- Upload date: 2026-04-20
- Video: https://www.youtube.com/watch?v=a2muGkT4WD4
- Transcript: raw/20260420_a2muGkT4WD4/a2muGkT4WD4.en-orig.vtt
- Metadata: raw/20260420_a2muGkT4WD4/a2muGkT4WD4.info.json

See more: https://x.com/adrgrondin/status/2040512861953270226

Speaker info:
- https://x.com/adrgrondin

## Gemma, DeepMind's Family of Open Models — Omar Sanseviero, Google DeepMind

- Upload date: 2026-04-20
- Video: https://www.youtube.com/watch?v=_gVFUEdhCyI
- Transcript: raw/20260420__gVFUEdhCyI/_gVFUEdhCyI.en-orig.vtt
- Metadata: raw/20260420__gVFUEdhCyI/_gVFUEdhCyI.info.json

Google DeepMind’s Gemma family is expanding. Join us for a deep dive into the latest models of the Gemma ecosystem. From vibe fine-tuning to Sovereign AI, you'll learn about the latest model capabilities, how to build high-performance applications, and how to get started with open models.

Speaker info:
- https://x.com/osanseviero
- https://www.linkedin.com/in/omarsanseviero/
- https://github.com/osanseviero

Timestamps
0:00 Introduction to the Gemma model family
0:41 Evolution from Gemma 3 to Gemma 4
1:21 Overview of the new Gemma 4 capabilities
2:31 Live demonstrations of on-device applications
3:38 LM Arena scores and performance benchmarks
5:07 Apache 2 license transition
5:27 Technical deep dive: The E2B architecture and per-layer embeddings
6:57 Multimodal understanding and multilingual support
8:43 Ecosystem growth and community adoption
10:07 Product integrations, including Android Studio
10:46 Statistics on model downloads and fine-tuning
11:27 Official Gemma variants: Shield Gemma and MedGemma
12:16 Community research and sovereign AI efforts
12:56 Real-world applications, from cancer therapy to offline tasks
14:05 Closing remarks and future outlook

## The New Application Layer - Malte Ubl, CTO Vercel

- Upload date: 2026-04-20
- Video: https://www.youtube.com/watch?v=XKup1pj-34M
- Transcript: raw/20260420_XKup1pj-34M/XKup1pj-34M.en-orig.vtt
- Metadata: raw/20260420_XKup1pj-34M/XKup1pj-34M.info.json

AI engineering is the legitimate successor to web development and the mainstream discipline that will define the next decade. Drawing on Vercel's own experience, Malte explores what it means to build infrastructure and applications in a world where agents are both the builders and users of software. In a future where the major AI labs commoditize, the real value will sit with the engineers building on top. The application layer is where the innovation happens, and AI engineers are the ones who will shape it.

Speaker info:
- https://x.com/cramforce
- https://www.linkedin.com/in/malteubl/

## The Future of MCP — David Soria Parra, Anthropic

- Upload date: 2026-04-19
- Video: https://www.youtube.com/watch?v=v3Fr2JR47KA
- Transcript: raw/20260419_v3Fr2JR47KA/v3Fr2JR47KA.en-orig.vtt
- Metadata: raw/20260419_v3Fr2JR47KA/v3Fr2JR47KA.info.json

In this Keynote, I will lay out what I believe will be true for agents in 2026 and how MCP plays a part in this. Let's take a look what connectivity for agents might look like.

Speaker info:
- https://x.com/dsp_
- https://www.linkedin.com/in/david-soria-parra-4a78b3a/
- https://github.com/dsp

Timestamps
0:00 Introduction and the vision for MCP applications
1:34 Looking back at the evolution of the MCP ecosystem over the last 18 months
2:30 Ecosystem growth and adoption milestones
3:46 Moving from exploration in 2025 to production in 2026
5:07 The 2026 connectivity stack: Skills, MCP, and CLI/Computer use
7:47 Improving client harnesses: Progressive Discovery
9:39 Programmatic tool calling and agent orchestration
12:00 Best practices for designing agents and server authors
13:42 Future roadmap for the MCP protocol and core improvements
15:23 Strategic integrations and enterprise features
16:32 Upcoming extension mechanisms and skills over MCP
17:15 Conclusion and call for community feedback

## Code Mode: Let the Code do the Talking - Sunil Pai, Cloudflare

- Upload date: 2026-04-19
- Video: https://www.youtube.com/watch?v=8txf05vVVl4
- Transcript: raw/20260419_8txf05vVVl4/8txf05vVVl4.en-orig.vtt
- Metadata: raw/20260419_8txf05vVVl4/8txf05vVVl4.info.json

Sunil Pai from Cloudflare discusses "Code Mode," an approach to interacting with AI agents where the model generates executable code (such as JavaScript) instead of relying on traditional JSON-based tool calling. This shift allows for more efficient, stateful, and complex system interactions.

Speaker info:
Sunil Pai created Partykit, the open source tool for real-time multi-player apps. For his day job, he builds AI Agents at Cloudflare.
- https://sunilpai.dev/
- blog.cloudflare.com/author/sunil/
- linkedin.com/in/sunil-pai-a47732253/

Timestamps
0:00 Introduction and speaker background
1:16 What is "Code Mode"?
1:31 Limitations of traditional tool calling at scale
2:03 The shift to generating executable code
3:01 Scaling API usage at Cloudflare
4:05 Why code generation is more efficient
5:28 Live demonstration of the Mythical server
7:20 A new way of interacting with systems
9:09 Example: The Kenton canvas and tic-tac-toe anecdote
11:46 New software architecture: The "Harness"
13:28 Observability and security in sandboxed environments
14:15 Long-running workflows and generative UI
16:41 Future outlook: Building for the next generation of users
17:50 The resurgence of capability-based security
18:33 Conclusion and final thoughts

## How Google DeepMind is researching the next Frontier of AI for Gemini — Raia Hadsell, VP of Research

- Upload date: 2026-04-18
- Video: https://www.youtube.com/watch?v=zZsTVBXcbow
- Transcript: raw/20260418_zZsTVBXcbow/zZsTVBXcbow.en-orig.vtt
- Metadata: raw/20260418_zZsTVBXcbow/zZsTVBXcbow.info.json

In this presentation, Raia Hadsell, VP of Research at Google DeepMind and AI Ambassador for the United Kingdom, opens AIE Europe and explores what's open in Frontier AI and the future of intelligence by focusing on advancements beyond standard large language models. She categorizes these innovations into three key areas:

00:00 Introduction
05:05 Advanced Embedding Models: Raia discusses the importance of embedding models for fast retrieval and recognition, similar to how the human brain uses 'Jennifer Aniston cells' to identify concepts across modalities. She highlights Gemini Embeddings 2, a fully omnimodal model that processes text, video, and audio into unified semantic vectors.
09:53 AI for Weather Forecasting: The team has developed revolutionary models for atmospheric prediction, moving away from traditional physics simulations. Notable breakthroughs include:
11:00 GraphCast: A spherical graph neural network that provides accurate 15-day weather forecasts.
12:47 GenCast: A probabilistic model that offers higher efficiency and accuracy (97% of the time compared to gold-standard benchmarks).
13:51 FGN: A functional generative network that directly predicts cyclone behavior, which is currently being utilized by the US National Hurricane Center.
14:35 World Models: Hadsell introduces Genie, a project focused on creating interactive, real-time environments. Starting from Genie 1 (2D platformers) and progressing to Genie 3, these models allow users to create and interact with high-quality, 3D photorealistic worlds. These environments demonstrate capabilities like memory, consistency, and the ability to be dynamically prompted by the user to change the surroundings in real-time.

Speaker info:
- https://uk.linkedin.com/in/raia-hadsell-35400266
- https://github.com/raiah

## The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil

- Upload date: 2026-04-18
- Video: https://www.youtube.com/watch?v=_Zcw_sVF6hU
- Transcript: raw/20260418__Zcw_sVF6hU/_Zcw_sVF6hU.en-orig.vtt
- Metadata: raw/20260418__Zcw_sVF6hU/_Zcw_sVF6hU.info.json

In this talk, Armin Ronacher (creator of Flask) and Cristina Poncela Cubeiro explore the paradox of using AI coding agents: while these tools promise to "ship without friction," excessive speed often leads to technical debt, security issues, and brittle systems. They argue that friction is actually a necessary component of high-quality software engineering because it forces human judgment and critical thinking.

Timestamps and Takeaways:
00:00 The Problem
03:35 The Psychological Trap: Because AI tools are addictive and make coding feel effortless, engineers often stop taking the time to design, review, and truly understand the code being generated.
07:15 - The Engineering Challenge: Agents are optimized for producing code that runs, not code that is maintainable or architecturally sound. This often results in "slop"—code that creates unexpected failure conditions and entropy
10:55 - Agent-Legible Codebases: To maximize AI effectiveness, the speakers suggest designing codebases as infrastructure. This includes:
Modularization of both code components and the code flow itself
12:35 - Mechanical Enforcement through strict linting (e.g., no bare catch-alls, unique function names, and avoiding hidden magic like dynamic imports) 
14:27 - Reintroducing Friction: The speakers advocate for slowing down. They recommend identifying specific, high-stakes areas (such as database migrations or permission changes) where human judgment is non-negotiable and must be intentionally re-inserted into the development process
17:25 - Conclusion

Armin and Cristina conclude that rather than trying to eliminate all friction, engineers should embrace it as the mechanism that allows for steering and quality control, ensuring that human experience remains at the center of the development lifecycle.

Speaker info:
- https://x.com/mitsuhiko
- https://www.linkedin.com/in/arminronacher/
- https://github.com/mitsuhiko
- https://www.linkedin.com/in/cristinaponcela/

## State of the Claw — Peter Steinberger

- Upload date: 2026-04-17
- Video: https://www.youtube.com/watch?v=zgNvts_2TUE
- Transcript: raw/20260417_zgNvts_2TUE/zgNvts_2TUE.en-orig.vtt
- Metadata: raw/20260417_zgNvts_2TUE/zgNvts_2TUE.info.json

Peter Steinberger gives the 5 month update on OpenClaw, the fastest growing open source project in history, and what it's like as a maintainer, from security to community. Keynote followed by audience Q&A moderated by @swyx.

Speaker info:
- https://x.com/steipete
- https://www.linkedin.com/in/steipete/
- https://openclaw.ai/


Timestamps
0:00 Project Growth and Statistics
2:23 Management Challenges and the OpenClaw Foundation
3:47 Addressing Security Advisories and Vulnerabilities
10:33 Misinformation and Media Fearmongering
14:50 The Burden of Open Source Maintenance
16:12 OpenAI Involvement and Future Independence
18:57 Audience Q&A Begins
19:53 OpenClaw's Relationship with OpenAI
22:28 The Importance of Open and Local Models
24:57 Coding Workflow and Agent Interactions
28:28 Defining 'Taste' in AI Development
30:31 Developing Personality for AI Agents
33:22 Future Vision: Ubiquitous Agents and Smart Homes
35:58 Addressing Prompt Injection Risks
38:33 Future Vision: Implementing 'Dreaming' and Modularity
40:24 Life as a Maintainer and Future Skills

## Harness Engineering: How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI

- Upload date: 2026-04-17
- Video: https://www.youtube.com/watch?v=am_oeAoUhew
- Transcript: raw/20260417_am_oeAoUhew/am_oeAoUhew.en-orig.vtt
- Metadata: raw/20260417_am_oeAoUhew/am_oeAoUhew.info.json

https://openai.com/index/harness-engineering/

Speaker info:
- https://x.com/_lopopolo
- https://www.linkedin.com/in/ryanlopopolo/
- https://github.com/lopopolo

With a special post keynote Q&A with Vibhu Sapra (https://x.com/vibhuuuus), cohost for https://latent.space/p/harness-eng

## $1 AI Guardrails: The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero

- Upload date: 2026-04-16
- Video: https://www.youtube.com/watch?v=YZHPEkfy2kc
- Transcript: raw/20260416_YZHPEkfy2kc/YZHPEkfy2kc.en-orig.vtt
- Metadata: raw/20260416_YZHPEkfy2kc/YZHPEkfy2kc.info.json

LLM-based attacks are no longer the exception, they are the baseline. This talk maps the six most common attack vectors found in production AI systems: Prompt and Context Injection, Model Internals, RAG Poisoning, MCP Exploits, and Agentic Escalation. From there, it dives into the architecture of ModernBERT and shows how to fine-tune it into a lightweight, self-hosted guardrails layer for under a dollar.

What you will learn:

- The Zero Trust Gap in LLMs: what these attack vectors share in common, and why model alignment and human review alone are not enough
- The secret sauce that makes encoder models beat LLM-as-a-Judge in latency and flexibility
- ModernBERT under the hood: a deep dive into Alternating Attention, Unpadding & Sequence Packing, RoPE, and FlashAttention
- Building your own safety layer: a practical walkthrough of fine-tuning ModernBERT as a safety discriminator
- Live Demo: real attack prompts from each vector tested against our model"

Speaker info:
- Diego Carpentero -  AI Engineer | Tech Entrepreneur | Open Source Contributor | NVIDIA Certified Professional (NCP-GENL)

Timestamps:
00:00 Intro

## Building pi in a World of Slop — Mario Zechner

- Upload date: 2026-04-16
- Video: https://www.youtube.com/watch?v=RjfbvDXpFls
- Transcript: raw/20260416_RjfbvDXpFls/RjfbvDXpFls.en-orig.vtt
- Metadata: raw/20260416_RjfbvDXpFls/RjfbvDXpFls.info.json

All I wanted was a shitty coding agent that is truly mine. And I’d have loved to just tell you why and how I built pi. But then Peter decided to make it the agentic core of OpenClaw. And now pi is collateral. So yes, this is a talk about pi. But it is also a talk about how agents are destroying OSS, how I deal with that, and a plea to slow the fuck down.

https://x.com/badlogicgames
https://github.com/badlogic
https://www.linkedin.com/in/mariozechner/

Timestamps
0:00 – Intro and motivation for building pi
0:29 – Act 1: Building pi and the frustration with existing agent harnesses
1:56 – Why current context management in tools like Cloud Code and Open Code fails
4:44 – The importance of minimal harnesses and the "Terminal" benchmark
5:35 – Introducing pi: A self-modifying, extensible agent core
7:27 – The "YOLO" security philosophy and extensibility through TypeScript
9:03 – Examples of pi extensions (chat rooms, NES, Doom)
10:46 – Act 2: OSS in the age of "clankers" and how to fight them
12:03 – Act 3: A plea to slow down and stop the "slop" in software development
13:58 – How agents create "enterprise-grade complexity" and why humans are still the bottleneck
16:12 – Practical advice: How to effectively integrate agents into your workflow

## Paperclip: Open Source Human Control Plane for AI Labor — Dotta Bippa

- Upload date: 2026-04-15
- Video: https://www.youtube.com/watch?v=h403btjldDQ
- Transcript: raw/20260415_h403btjldDQ/h403btjldDQ.en-orig.vtt
- Metadata: raw/20260415_h403btjldDQ/h403btjldDQ.info.json

Curator note: Dotta is anonymous, so we asked him to submit with just an avatar. He did amazing!

Paperclip enables open source orchestration for zero-human companies. With Paperclip you can manage hundreds of ai-agent employees to run your business, even if you're not technical. In this talk we walk through how to setup paperclip, how to grow an ai organization, how to leverage skills and instructions for the best ai agents, and how you can start a zero human company.

Speaker info:
https://x.com/dotta
https://paperclip.ing

Timestamps:

00:00 - Introduces Paperclip
00:56 - Organizational Control
1:17 - Getting Started
04:42 - Skill Management
09:01 - Reliable Workflows
11:10 - Routine Automation
17:51 - Agentic Flexibility
21:39 - Future Roadmap

## Running LLMs locally: Practical LLM Performance on DGX Spark — Mozhgan Kabiri chimeh, NVIDIA

- Upload date: 2026-04-10
- Video: https://www.youtube.com/watch?v=c5-kx2bwoCk
- Transcript: raw/20260410_c5-kx2bwoCk/c5-kx2bwoCk.en-orig.vtt
- Metadata: raw/20260410_c5-kx2bwoCk/c5-kx2bwoCk.info.json

Moving LLM workloads from the cloud to local infrastructure requires a shift in engineering strategy. In this talk, I share my journey of serving and benchmarking open-source models (1.5B to 14B) on an NVIDIA DGX Spark workstation. Using a reproducible methodology with vLLM, I analyze real-world trade-offs in throughput, latency, and the benefits of the 128GB Grace Blackwell unified memory architecture. You will leave with a clear framework for local model sizing, an understanding of quantization performance like NVFP4, and a guide for when local compute is the right choice for your AI stack.

Speaker info:
- LinkedIn https://www.linkedin.com/in/mozhgankch/

## AI Didn’t Kill the Web, It Moved in! — Olivier Leplus (AWS) & Yohan Lasorsa (Microsoft)

- Upload date: 2026-04-10
- Video: https://www.youtube.com/watch?v=XZ0boOjtbNo
- Transcript: raw/20260410_XZ0boOjtbNo/XZ0boOjtbNo.en-orig.vtt
- Metadata: raw/20260410_XZ0boOjtbNo/XZ0boOjtbNo.info.json

In 2026, AI didn't replace the web. It became part of it. Your browser now ships a built-in MCP server. Chrome DevTools debug your app with AI. Native Web APIs let you summarize, translate, and prompt right from your frontend code. Meanwhile, the web feeds agents right back through standards like LLMs.txt and MCP tools that make sure models always have the right documentation. AI builds the web. The web feeds AI. And now, AI lives inside the browser itself. In this talk, we'll follow a feature from idea to production and demo this new symbiosis in action: coding agents, AI-powered debugging in Chrome devtools, Web AI APIs, WebMCP, and more. Because your next website won't just be built with AI. It will be built for humans and AI agents alike. AI isn't just for Python folks. The web is AI's new home.

## Judge the Judge: Building LLM Evaluators That Actually Work with GEPA — Mahmoud Mabrouk, Agenta AI

- Upload date: 2026-04-10
- Video: https://www.youtube.com/watch?v=X4dEHRzBLmc
- Transcript: raw/20260410_X4dEHRzBLmc/X4dEHRzBLmc.en-orig.vtt
- Metadata: raw/20260410_X4dEHRzBLmc/X4dEHRzBLmc.info.json

Miscalibrated evals are worse than no evals. They give false confidence while being, at best, useless. This workshop walks you through building a calibrated LLM-as-a-judge, from capturing ground truth to optimizing with GEPA and assessing the judge. You will leave with an LLM-as-a-judge you can trust to actually improve your app.

Mahmoud Mabrouk - Co-founder and CEO, Agenta AI

Mahmoud Mabrouk is the cofounder and CEO of Agenta, an open-source LLMOps platform for building and evaluating LLM applications. He has spent the past 15 years working in machine learning and holds a PhD in applied machine learning for computational biology.

Resources:
- Workshop repo: https://github.com/Agenta-AI/judge-the-judge-talk-2026
- GEPA repository: https://github.com/gepa-ai/gepa
- GEPA paper: https://arxiv.org/abs/2507.19457
- Hamel’s guide for error analysis: https://hamel.dev/blog/posts/field-guide/

Socials:
https://x.com/mmabrouk_
https://www.linkedin.com/in/mmabrouk2/
https://agenta.ai
https://github.com/agenta-ai/agenta

## One Registry to Rule them All - Sonny Merla, Mauro Luchetti, & Mattia Redaelli, Quantyca

- Upload date: 2026-04-10
- Video: https://www.youtube.com/watch?v=VXfRt_H-V08
- Transcript: raw/20260410_VXfRt_H-V08/VXfRt_H-V08.en-orig.vtt
- Metadata: raw/20260410_VXfRt_H-V08/VXfRt_H-V08.info.json

As internal MCP servers and A2A agents explode in number, discovery and governance become critical challenges for production-grade AI systems. We'll demonstrate how we built an enterprise infrastructure to index MCP servers and A2A agents, and link them to relevant use cases. We'll show how moving from a fragmented environment to a searchable, metadata-rich registry transformed a chaotic development cycle into a standardized, scalable deployment process.
 
In this talk, we'll cover:
- How we developed an internal private company MCP registry based on the open source specification
- How we defined an A2A registry based on agent cards
- How we achieved agent runtime discovery using an MCP server that exposes company A2A agents
- How we linked A2A agent and MCP server template repositories to DevOps processes

Mauro Luchetti - AI CoE Manager, Quantyca

I work as an AI Engineer and CoE Manager at Quantyca, where I focus on artificial intelligence solutions, data engineering, and cloud architectures, drawing on nearly 8 years of professional experience in the field. Over the years I've had the opportunity to work on projects involving generative AI, machine learning, data governance and data management, trying to combine hands-on technical skills with a broader strategic perspective. I enjoy sharing what I've learned with the teams I work with, contributing to collective growth in modern AI engineering practices.

Socials:
https://www.quantyca.it/

Slides:
https://quantyca-my.sharepoint.com/:b:/g/personal/mauro_luchetti_quantyca_it/IQBUCcMBzsAfSZtJXrCdaqV0AaUyDhifxP360fqCUupyaGc?e=S6ytoA

## Cognitive Exhaust Fumes, or: Read-Only AI Is Underrated — Šimon Podhajský, Head of AI, Waypoint

- Upload date: 2026-04-08
- Video: https://www.youtube.com/watch?v=u0TOSBbAw7c
- Transcript: raw/20260408_u0TOSBbAw7c/u0TOSBbAw7c.en-orig.vtt
- Metadata: raw/20260408_u0TOSBbAw7c/u0TOSBbAw7c.info.json

Every other personal AI demo has agents sending emails and managing calendars. I built the opposite: a read-only system that queries my data sources (email, journal, tasks, CRM, browser sessions, notes) but can't modify any of them. This is an intentional limitation. I'll cover why trust asymmetry matters (read is safe, write is dangerous), how cross-source pattern detection beats task automation, and why ""exhaust fume analysis"" of one's cognition is more valuable than yet another AI assistant trying to act on your behalf.

Šimon Podhajský - Head of AI, Waypoint AI

I'm Head of AI at Waypoint and a full-stack builder with a background in data science and data engineering. I built this personal AI system to scratch my own itch -- and discovered that the ""read-only"" constraint led to better architecture than the agent-first approaches I see everywhere.

I made a Github repo with a template for people to try out the read-only AI / personal intelligence system: https://github.com/shippy/personal-intelligence-kit 

Socials:
https://linkedin.com/in/simonpodhajsky
https://x.com/sim_pod
https://simon.podhajsky.net

Slides:
https://slides.podhajsky.net/read-only-ai

## Platforms for Humans and Machines: Engineering for the Age of Agents — Juan Herreros Elorza

- Upload date: 2026-04-08
- Video: https://www.youtube.com/watch?v=cCRO3ChaYhM
- Transcript: raw/20260408_cCRO3ChaYhM/cCRO3ChaYhM.en-orig.vtt
- Metadata: raw/20260408_cCRO3ChaYhM/cCRO3ChaYhM.info.json

As AI coding agents become first-class users of internal developer platforms, the practices that make platforms accessible to humans turn out to be the same ones that enable AI to thrive.

Self-service interfaces, well-defined APIs with schemas and documentation, local-first workflows, and rich observability have always been important elements of a good platform. Now they are prerequisites for agents that can autonomously build, debug, and ship software.

This talk explores what it means to design platforms where both humans and AI can collaborate effectively. We'll cover:

- How to expose your platform as a product with structured APIs (and perhaps MCPs)
- Why prioritizing local tooling pays dividends when agents need to iterate on errors
- How observability becomes the bridge between runtime behavior and AI understanding

We'll also discuss the flip side: AI is making it easier than ever to *contribute* to platform code, but that comes with new responsibilities around quality gates, context files like CLAUDE.md, and maintainability.

Walk away with concrete practices to ensure your platform is ready for a future where agents are not just tools, but users of it.

Juan Herreros Elorza - Team Lead, Banking Circle

I'm Juan, a Platform Engineering enthusiast.

I am working for Banking Circle, as the Team Lead in our Cloud Native Technology team.

When I'm not working, I'm most likely rehearsing or performing improv comedy.

Socials:
https://juanherreros.com/
https://linkedin.com/in/juan-herreros-elorza
https://github.com/jherreros

Slides:
https://speakerdeck.com/jherreros/platforms-for-humans-and-machines-engineering-for-the-age-of-agents

## Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz

- Upload date: 2026-04-08
- Video: https://www.youtube.com/watch?v=U00AOI1eJUE
- Transcript: raw/20260408_U00AOI1eJUE/U00AOI1eJUE.en-orig.vtt
- Metadata: raw/20260408_U00AOI1eJUE/U00AOI1eJUE.info.json

Public MCP servers often look ready-to-use, until the reality of production hits. You might find your agents ignoring perfectly good tools, unwanted side-effects exhausting your container's disk space, or worse, security concerns like multi-tenant leaks wreaking havoc. What begins as a ""simple integration"" can quickly become a source of friction and unexpected failure.

In this talk, we'll share a hands-on guide to adapting third-party MCP servers for real-world applications. You'll learn practical processes to identify friction points and strategies to modify MCP servers so they integrate seamlessly with your specific agents and architecture. Real-world lessons, trade-offs, and production-tested solutions included.

Using a concrete example, we'll walk through the journey of transforming a brittle setup into production-ready infrastructure. We'll cover editing tool definitions, optimizing agentic context, and layering deterministic validations—all while preparing for scale. This iterative debugging process will provide you with a repeatable framework to make any MCP integration resilient, secure, and production-ready.

Nimrod Hauser - Founding Software Engineer, Baz

Nimrod is a Principal Engineer at Baz, building AI-powered code review agents. A “jack of all trades” across backend, data engineering, and data science, he has worked at the intersection of software and data throughout his career. He began as a data analyst in the military, helped lay the foundations of Salesforce’s Einstein platform, and later became the first data scientist at cybersecurity startup BlueVoyant. He went on to lead data and architecture at Solidus Labs in the crypto-regulation space before joining Baz. Nimrod thrives on building systems from scratch and turning ideas into scalable products.

Socials:
https://www.linkedin.com/in/nimrod-hauser-03776a31/
https://x.com/NimrodHauser

Slides:
https://prezi.com/view/TSBwBXLNcXzzWrLbRiit/?referral_token=4jzLrblnB3FN

## Contact Center Voice AI: Low-Latency Intelligence Extraction from Messy Audio Streams — Dippu Singh

- Upload date: 2026-04-08
- Video: https://www.youtube.com/watch?v=IEF842ZEU5A
- Transcript: raw/20260408_IEF842ZEU5A/IEF842ZEU5A.en-orig.vtt
- Metadata: raw/20260408_IEF842ZEU5A/IEF842ZEU5A.info.json

"Processing real-time voice data is an engineering minefield of latency, accents, and interruptions. This session explores the architecture of a Real-Time Voice Intelligence Pipeline deployed in a high-volume contact center.
We will move beyond simple transcription to discuss Structured Intent Extraction. I will show you how to design:

1. Voice Capture Pipeline: The entry point for clean, multi-channel data acquisition.
2. Speech-To-Text(STT) Engine: Converting speech to accurate text.
3. Generative AI Core Structure: Using rigorous system prompts to force the LLM to separate ""Customer Intent"" from ""Operator Chit-Chat"" and output valid JSON, even from garbled transcripts.
4. Customer Data Sync: Translating AI insights into enterprise system actions.

We reduced post-call work by 50% by shifting compute from ""batch"" to ""stream.""

Speaker: Dippu Kumar Singh - Leader Of Emerging Technologies (Apps), Fujitsu North America Inc.

Dippu Kumar Singh has over 16 years of experience at the intersection of industry innovation and advanced research. He is a recognized authority in building scalable, trustworthy, and commercially viable AI systems. Being a Leader for Emerging Data & Analytics at Fujitsu North America, Dippu specializes in bridging the gap between theoretical AI concepts and enterprise-grade implementation. His strategic leadership has spearheaded multi-million in sales pipelines and delivered remarkable savings through AI-driven optimizations in transportation, manufacturing, utilities, and supply chain logistics.

Socials:
https://www.linkedin.com/in/dippukumarsingh/

Slides:
https://docs.google.com/presentation/d/1f2y1s64irhdDNTRgK6bWrBtOgMWlhQYM/edit?usp=sharing&ouid=107532212133041789455&rtpof=true&sd=true"

## Your Insecure MCP Server Won't Survive Production — Tun Shwe, Lenses

- Upload date: 2026-04-08
- Video: https://www.youtube.com/watch?v=BurJvbqFr4c
- Transcript: raw/20260408_BurJvbqFr4c/BurJvbqFr4c.en-orig.vtt
- Metadata: raw/20260408_BurJvbqFr4c/BurJvbqFr4c.info.json

Tun Shwe and Jeremy Frenay from Lenses.io address the critical security and design challenges involved in moving Model Context Protocol (MCP) servers from local development to enterprise production. Effective agentic design is inseparable from security and here we propose five core principles such as shrinking the attack surface, constraining inputs and returning only essential data. Standard local setups fail under professional workloads, necessitating a shift to remote MCP servers and robust authentication frameworks. Detailed technical flows are provided for OAuth 2.1, comparing Dynamic Client Registration (DCR) with the more advanced Client ID Metadata Document (CIMD) approach for managing agent identities. Come learn how to adopt the correct mindset for building enterprise-grade agentic AI systems with MCP.

https://github.com/lensesio/lenses-mcp

https://lenses.io/

Tun Shwe - Staff AI Engineer, Lenses.io

Tun is a Staff AI Engineer at Lenses.io, where he leads AI strategy. He is focused on helping companies imagine and implement their strategic vision with agentic AI systems fuelled with real-time context. He was previously a Head of Data and Data Engineer at high growth startups and has spent 20 years building data-intensive applications and leading T-shaped teams. In his spare time, Tun goes surfing, plays guitar and tends to his analogue cameras.

--

Jeremy Frenay is an AI Engineer at Lenses.io, where he works on bringing AI-assisted engineering to the Apache Kafka ecosystem. Previously, Jeremy co-founded Arcane, an AI copilot for marketers, and led data operations engineering at Babylon Health, scaling data platforms for one of the world's largest healthtech unicorns.

Socials:
https://lenses.io/
https://github.com/lensesio/lenses-mcp
https://www.linkedin.com/in/tunshwe/
https://www.linkedin.com/in/jeremy-frenay/

Slides:
https://drive.google.com/file/d/1zLzkVO7_kBoV6bI7lhYIi3AxUH6j7xH_/view?usp=sharing

## Why, and how you need to sandbox AI-Generated Code? — Harshil Agrawal, Cloudflare

- Upload date: 2026-04-08
- Video: https://www.youtube.com/watch?v=AHtGAgQ0Q_Q
- Transcript: raw/20260408_AHtGAgQ0Q_Q/AHtGAgQ0Q_Q.en-orig.vtt
- Metadata: raw/20260408_AHtGAgQ0Q_Q/AHtGAgQ0Q_Q.info.json

We are using AI to write code. Moreover, we are using it to be more productive. However, giving AI access to our machine and let them run on their own is dangerous. Imagine, giving AI access to the server where you run your application! You want your users to interact with your application through a chat interface, and maybe build their own apps or customize the UI. If not supervised carefully, AI can break your application or worse leak private data.

So how do you run AI generated code within your application and allow users to build their own apps?
In this talk, we'll go beyond the hype and dive into the practical architecture of sandboxing AI generated code. You'll learn how to integrate an LLM to generate code and, how to run that code in a secure isolated environment.

Harshil Agrawal - Sr. Developer Educator, Cloudflare

Working in the Developer Relations team at Cloudflare, Harshil enjoys sharing his learnings with the community. A JavaScript developer, open-source contributor, and a low-code enthusiast, Harshil loves experimenting with tech and building small projects.

Socials:
https://x.com/harshil1712
https://linkedin.com/in/harshil1712
https://harshil.dev

Slides:
https://harshil.dev/slides/sandbox-ai-engineer

## Let LLMs Wander: Engineering RL Environments — Stefano Fiorucci

- Upload date: 2026-04-08
- Video: https://www.youtube.com/watch?v=71V3fTaUp2Q
- Transcript: raw/20260408_71V3fTaUp2Q/71V3fTaUp2Q.en-orig.vtt
- Metadata: raw/20260408_71V3fTaUp2Q/71V3fTaUp2Q.info.json

Reasoning models like DeepSeek R1 have demonstrated that learning from interaction is just as critical as learning from examples. To build these capabilities ourselves, we need to move beyond static datasets and start building Reinforcement Learning Environments: little worlds where models can act, get rewards, and learn.

In this talk, I will walk you through my journey exploring this space from a practical software engineering perspective.

We will cover:
- How classic Reinforcement Learning concepts translate to Language Models
- Verifiers, an open-source library to build Environments as software artifacts
- Concrete examples of environments, from single-turn tasks to multi-turn games and tool-using agents
- How to use these environments for both evaluating and training Small Language Models.

Join me to learn how to move from prompting models to building the gyms where they learn.

Stefano Fiorucci - AI/SW Engineer/Explorer, deepset

Stefano is an AI/Software Engineer and explorer.

He currently works on AI Orchestration at Deepset, where he contributes to and maintains Haystack, a widely used open-source framework for building LLM applications.

He loves experimenting with Small Language Models, Post-Training and Reinforcement Learning, and shares his learning through code, writing, and talks.

LLM RL Environments Lil Course: https://github.com/anakin87/llm-rl-environments-lil-course

Socials:
https://twitter.com/theanakin87
https://www.linkedin.com/in/stefano-fiorucci/
https://github.com/anakin87
https://huggingface.co/anakin87

Slides:
https://drive.google.com/file/d/116PKThwtyTxeH1GmZQ7bL3HPYM6KCgHa/view?usp=drive_link

## OpenRAG: An open-source stack for RAG — Phil Nash

- Upload date: 2026-04-08
- Video: https://www.youtube.com/watch?v=4TxOBhDRRCM
- Transcript: raw/20260408_4TxOBhDRRCM/4TxOBhDRRCM.en-orig.vtt
- Metadata: raw/20260408_4TxOBhDRRCM/4TxOBhDRRCM.info.json

There are many variables in building RAG applications, from document parsing to the language model you pick for generation and everything in between. Combining Docling for document parsing, OpenSearch for retrieval, and Langflow for orchestration, plus local and remote models, OpenRAG is an opinionated, agentic, open-source stack for building the RAG application of your dreams.

Just because it has opinions doesn't make it inflexible though. In this talk we'll look at how OpenRAG gives you a great baseline for RAG and how you can tune it and evaluate the outcomes to create RAG applications that work well with your data. You'll learn how to get the best out of your documents with Docling, how OpenSearch provides more than just vector search, and how Langflow makes it easy to customise your pipeline to interact with your data the way you want to. You’ll leave with a playbook of options to improve your RAG app and a stack you can extend without reinventing everything.

Phil Nash - Developer relations engineer, IBM

Phil is a developer relations engineer for DataStax and Google Developer Expert living in Melbourne, Australia. He's been working in developer relations for a decade, speaking at conferences since 2012, and writing JavaScript since before jQuery. Away from the keyboard, Phil enjoys travel, live music, and hanging out with his mini sausage dog, Ruby.

Socials:
https://x.com/philnash
https://linkedin.com/in/philnash
https://philna.sh
https://github.com/philnash

## From Chaos to Choreography: Multi-Agent Orchestration Patterns That Actually Work — Sandipan Bhaumik

- Upload date: 2026-04-08
- Video: https://www.youtube.com/watch?v=2czYyrTzILg
- Transcript: raw/20260408_2czYyrTzILg/2czYyrTzILg.en-orig.vtt
- Metadata: raw/20260408_2czYyrTzILg/2czYyrTzILg.info.json

One AI agent is a feature. Fifty agents is a distributed systems problem nobody's discussing. I've seen this pattern: teams build one agent, then five, then drown in coordination problems unrelated to LLMs. Agent handoffs fail silently. Data goes stale. Decisions become untraceable. Drawing from Databricks production deployments, I'll expose orchestration anti-patterns killing multi-agent systems and show agent handoff protocols that work—state management, data contracts, failure modes. You'll see when to choreograph versus orchestrate and live multi-agent workflow with proper observability. This applies distributed systems engineering to agents: the infrastructure layer everyone needs but nobody's building.

Sandipan Bhaumik - Data & AI Tech Lead, Databricks

Sandipan Bhaumik has spent 18 years building data and AI systems inside environments that can't afford them to fail - NHS, Tier 1 banks, and large enterprises across EMEA. At AWS and now Databricks, he's seen firsthand where multi-agent systems break down between architecture and production. He is a regular speaker on data and AI system architecutr ebest practices, runs a community of AI practitioners, and he's here to talk about what actually holds together when you scale agentic AI systems in production.

Socials:
https://www.linkedin.com/in/sandipanbhaumik

Slides:
https://drive.google.com/file/d/18LqVzhfVS3iULYuy2EshWoMLmQt3rdpT/view?usp=sharing

## Agentic Engineering: Working With AI, Not Just Using It — Brendan O'Leary

- Upload date: 2026-04-07
- Video: https://www.youtube.com/watch?v=BEKc4P87XKo
- Transcript: raw/20260407_BEKc4P87XKo/BEKc4P87XKo.en-orig.vtt
- Metadata: raw/20260407_BEKc4P87XKo/BEKc4P87XKo.info.json

Coding agents are quickly moving from novelty to necessity, but most teams are still stuck between demos that feel magical and systems that break down in real-world engineering environments. In this session, Brendan O’Leary explores what it takes to make coding agents reliable collaborators rather than unpredictable copilots. Drawing from hands-on experience building and scaling AI coding agents, Brendan can unpack where agents succeed, where they fail, and how engineers can design workflows that balance speed with control. Attendees will learn how to think about agent autonomy, context management, and human-in-the-loop design so AI can meaningfully accelerate development without sacrificing code quality, security, or trust. This talk is for engineers ready to move past “vibe coding” and into production-grade agent-driven software development.


Brendan O'Leary - Developer Relations Engineer, Kilo Code

As conversations shift from AI demos to real engineering and coding agents begin moving into production environments, Brendan is passionate about helping teams understand not just what’s possible, but what’s practical. He’s especially energized by audiences who are grappling with the same questions he sees every day: how much autonomy to give agents, how to keep humans meaningfully in the loop, and how to move beyond “vibe coding” into reliable software development.

Brendan is a builder and practitioner at Kilo Code, working hands-on with AI coding agents and the realities of deploying them in serious engineering contexts. He’s mastered the role of choreographer, successfully balancing the collaborative dance between human creativity and machine capability. 

His perspective of coding agents is rooted in lived experience, combining a deep technical understanding with a clear-eyed view of where agents succeed, where they fail, and why trust is the missing layer most tools overlook. Brendan brings a candid, engineer-first approach that resonates with technical audiences and leaves them with concrete ways to rethink how humans and coding agents collaborate in production systems.

Socials:
https://www.linkedin.com/in/olearycrew/
https://boleary.dev/
https://x.com/olearycrew
https://gitlab.com/brendan/boleary-dot-dev
https://kilo.ai/

## How METR measures Long Tasks and Experienced Open Source Dev Productivity - Joel Becker, METR

- Upload date: 2026-01-19
- Video: https://www.youtube.com/watch?v=k1t2xyWMUdY
- Transcript: raw/20260119_k1t2xyWMUdY/k1t2xyWMUdY.en-orig.vtt
- Metadata: raw/20260119_k1t2xyWMUdY/k1t2xyWMUdY.info.json

AI models are crushing benchmarks. SWE-bench scores are climbing, and METR's measured time horizons are rising rapidly. Yet when we deployed these same models in a field study with experienced developers, they didn't speed up work. What's going on? Are benchmarks misleading us about AI capabilities? Are we missing something about how AI performs in the real world? In this talk, we'll reconcile lab and field evidence on AI capabilities. Drawing from METR's time horizon measurements and developer productivity RCT, we'll explore why impressive benchmark performance doesn't always translate to real-world impact. We'll examine potential explanations—from reliability requirements to task distribution to capability elicitation—and discuss what this means for automated AI R&D.

https://x.com/joel_bkr

Timestamps
00:00 The Compute-Time Horizon Argument

01:43 Potential Constraints on AI Scaling (Power & Dollars)

04:23 The Problem of Eclipsing Evaluation Time

06:52 Meta's "J-Curve" of Developer Productivity

09:12 Unreliability of Self-Reported Time Estimates

11:43 Personal Experiences with AI Tools (Cursor) & Learning Curves

14:10 METR Study Deep Dive: Scatter Plots & Variance

16:48 The Controversy of "Conservative" Usage Estimates

21:41 Unpublished Hackathon Results (AI Allowed vs. Disallowed)

25:28 Why AI Struggles with Data Science & Messy Enterprise Data

30:35 Example of AI Failure on Complex Deployment Metrics

38:29 Quantifying Speed-Up: The Methodological Challenges

46:30 Future Metrics: "Watched" vs. "Unwatched" Time Horizons

52:52 Moving Beyond Benchmarks: "In the Wild" Transcripts

56:12 The "Agent Village" & Fuzzy Goal Measurement

58:53 The "Neurodivergent AI" Hypothesis & Interface Mismatch

01:06:31 Software-Only Singularity vs. Hardware Constraints

01:13:53 AI Applications in Chip Fabrication & Yield Improvement

## Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0

- Upload date: 2026-01-14
- Video: https://www.youtube.com/watch?v=VSdV-AdSlis
- Transcript: raw/20260114_VSdV-AdSlis/VSdV-AdSlis.en-orig.vtt
- Metadata: raw/20260114_VSdV-AdSlis/VSdV-AdSlis.info.json

Implementing secure identity and access management for AI agents with Okta!

https://www.linkedin.com/in/patmriley/
https://www.linkedin.com/posts/cgcladera_auth0-for-ai-agents-secure-agentic-apps-activity-7399029829565579264-9Gdf/

## OpenAI + @Temporalio : Building Durable, Production Ready Agents - Cornelia Davis, Temporal

- Upload date: 2026-01-12
- Video: https://www.youtube.com/watch?v=k8cnVCMYmNc
- Transcript: raw/20260112_k8cnVCMYmNc/k8cnVCMYmNc.en-orig.vtt
- Metadata: raw/20260112_k8cnVCMYmNc/k8cnVCMYmNc.info.json

Everyone is building AI Agents, and everyone is looking for ways to build them more easily. Earlier this year, OpenAI released the OpenAI Agents SDK to bring the patterns they have found to work for building agents to the developer community. With the SDK you can define AI agents by supplying them instructions (prompts), specifying which model to use (OpenAI or not), listing tools it uses (including MCP), and much more. The OpenAI Agents SDK encourages a paradigm of orchestrated micro-agents, which themselves may have micro-orchestrations within them with the use of handoffs. It’s an elegant and powerful model.

But a good AI Agents programming model is not enough. These agents are ultimately wildly distributed systems and are plagued with all of the problems such systems bring.

- How can they persevere through flakey networks?
- How can they function when LLMs are rate limited?
- How can they run for long periods of time (hours, days, weeks, months) when infrastructure is rarely stable that long?

In this workshop, we’ll show you how. Temporal is an open source (MIT license) durable execution framework that brings resilience to AI agents, and in this workshop we’ll show you how it’s done with the OpenAI Agents SDK. Spoiler: OpenAI and Temporal have done all of the heaving lifting for you with an integration announced earlier this year.

Oh, and OpenAI themselves use Temporal to help make several of their products production ready (image gen and Codex, for example).

Not using the OpenAI Agents SDK? Do come anyway; the foundational concepts carry over to different agent frameworks (and more integrations are coming all the time).

https://twitter.com/cdavisafc
https://www.linkedin.com/in/corneliadavis

## Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect

- Upload date: 2026-01-12
- Video: https://www.youtube.com/watch?v=96G7FLab8xc
- Transcript: raw/20260112_96G7FLab8xc/96G7FLab8xc.en-orig.vtt
- Metadata: raw/20260112_96G7FLab8xc/96G7FLab8xc.info.json

Too many MCP servers are simply glorified REST wrappers, regurgitating APIs that were designed for SDKs, not agents. This leads to confused LLMs, wasted tokens, and demonstrably poor performance. If you've ever pointed an MCP generator at an OpenAPI spec and called it a day, this talk is your intervention.

Like any product, great MCP servers are the result of careful design. This talk shares the hard-won lessons from creating FastMCP, the most popular framework for building MCP servers (and yes, for generating them, too). The secret is to stop thinking about endpoints and start thinking about products. We will cover the three pillars of agent-native product design—Discovery, Iteration, and Context—providing an actionable framework for curating context into small, highly effective surface areas that lead to better AI outcomes.

Jeremiah Lowin, CEO of Prefect
https://twitter.com/jlowin
https://www.linkedin.com/in/jlowin
https://github.com/jlowin

## Spec-Driven Development: Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro

- Upload date: 2026-01-09
- Video: https://www.youtube.com/watch?v=HY_JyxAZsiE
- Transcript: raw/20260109_HY_JyxAZsiE/HY_JyxAZsiE.en-orig.vtt
- Metadata: raw/20260109_HY_JyxAZsiE/HY_JyxAZsiE.info.json

In the AI coding era, we have powerful tools, but tools still require honing to work effectively. Spec-Driven Development allows for reproducible and reliable delivery, but spending time up-front to improve the spec process will yield the best approach. Learn how the Kiro team does this, and how you can too!

https://www.linkedin.com/in/al-harris-7a755640/

## Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands

- Upload date: 2026-01-08
- Video: https://www.youtube.com/watch?v=rcsliSIy_YU
- Transcript: raw/20260108_rcsliSIy_YU/rcsliSIy_YU.en-orig.vtt
- Metadata: raw/20260108_rcsliSIy_YU/rcsliSIy_YU.info.json

Today's agents are best at small, atomic coding tasks. Much larger tasks--like major refactors and breaking dependency updates--are highly automatable but hard to one-shot.

In this session, we'll discuss patterns for orchestrating large-scale code changes with swarms of agents and a human in the loop.

We'll also work through a concrete example: migrating an entire codebase from one React state management library to another.

https://twitter.com/RobertBrennan

Slides: https://dub.sh/openhands-workshop

## DSPy: The End of Prompt Engineering - Kevin Madura, AlixPartners

- Upload date: 2026-01-08
- Video: https://www.youtube.com/watch?v=-cKUW6n8hBU
- Transcript: raw/20260108_-cKUW6n8hBU/-cKUW6n8hBU.en-orig.vtt
- Metadata: raw/20260108_-cKUW6n8hBU/-cKUW6n8hBU.info.json

Applications developed for the enterprise need to be rigorous, testable, and robust. The same is true for applications that use AI, but LLMs can make this challenging. In other words, you need to be able to program with LLMs, not just tweak prompts. In this talk we'll cover why DSPy really is all you need in building applications with LLMs. We'll dive into real-world examples where we have successfully automated manual work using an opinionated DSPy-first approach to structuring applications, covering everything from simple modules to using SoTA optimizers to measurably improve performance.

https://x.com/kmad/


**Summary**
Kevin Madura, a consultant at AlixPartners, argues that building robust enterprise AI applications requires shifting from brittle "prompt engineering" to "programming with LLMs" using **DSPy**. He contends that prompts should be treated as implementation details optimized by the system, while developers focus on defining typed interfaces (Signatures) and modular logic (Modules). The session moves from a conceptual overview of DSPy's primitives—Signatures, Modules, Adapters, and Optimizers—to a live code walkthrough. Madura demonstrates real-world use cases, including a complex pipeline that routes files by type (SEC filings vs. contracts) and a "boundary detector" that uses visual layout to segment legal documents. The talk concludes with a demonstration of how Optimizers (like MIPRO) can automatically tune these programs to outperform manual baselines, followed by a Q&A on production costs and feedback loops.

**Timestamps**

00:00 Introduction & The Enterprise AI Challenge
07:12 The 6 Core Concepts of DSPy (Signatures, Modules, Adapters)
13:23 Deep Dive: Class-based vs. Shorthand Signatures
19:57 Adapters: Controlling the Prompt Format (JSON vs. BAML)
24:17 Optimizers: The "Killer Feature" for Transferability
31:08 Code Walkthrough: Setup & Model Mixing
36:24 Handling Documents: "Poor Man's RAG" with Attachments
42:10 Adapter Comparison: Improving Token Efficiency with BAML
47:20 Optimizers in Practice: Creating Datasets & Metrics
51:13 Complex Pipeline: Routing & Classifying Arbitrary Files
56:00 Advanced Use Case: PDF Boundary Detection via Visuals
01:01:22 Analyzing Optimization Results & The "DSPy Hub" Concept
01:09:02 Q&A: Handling Delayed Feedback & Online Learning
01:13:00 Conclusion

## Building durable Agents with Workflow DevKit & AI SDK - Peter Wielander, Vercel

- Upload date: 2026-01-06
- Video: https://www.youtube.com/watch?v=kmV-qg4uoNI
- Transcript: raw/20260106_kmV-qg4uoNI/kmV-qg4uoNI.en-orig.vtt
- Metadata: raw/20260106_kmV-qg4uoNI/kmV-qg4uoNI.info.json

Learn to build and deploy AI agents using Vercel's new open source Workflows platform.

https://twitter.com/vaguelyserious
https://www.linkedin.com/in/peter-wielander

## Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize

- Upload date: 2026-01-06
- Video: https://www.youtube.com/watch?v=SbcQYbrvAfI
- Transcript: raw/20260106_SbcQYbrvAfI/SbcQYbrvAfI.en-orig.vtt
- Metadata: raw/20260106_SbcQYbrvAfI/SbcQYbrvAfI.info.json

Following from Aparna's talk: https://www.youtube.com/watch?v=pP_dSNz_EdQ

Learn how to create a feedback loop to continuously improve your AI prompts and responses.

https://www.linkedin.com/in/sallyann-delucia-59a381172/

## Welcome to AIE CODE - Jed Borovik, Google DeepMind

- Upload date: 2026-01-05
- Video: https://www.youtube.com/watch?v=mdEh4lBO_R0
- Transcript: raw/20260105_mdEh4lBO_R0/mdEh4lBO_R0.en-orig.vtt
- Metadata: raw/20260105_mdEh4lBO_R0/mdEh4lBO_R0.info.json

Day 2 emcee Jed Borovik opens the day for coding agents and labs.

## Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic

- Upload date: 2026-01-05
- Video: https://www.youtube.com/watch?v=TqC1qOfiVcQ
- Transcript: raw/20260105_TqC1qOfiVcQ/TqC1qOfiVcQ.en-orig.vtt
- Metadata: raw/20260105_TqC1qOfiVcQ/TqC1qOfiVcQ.info.json

Learn to use Anthropic's Claude Agent SDK (formerly Claude Code SDK) for AI-powered development workflows!

https://platform.claude.com/docs/en/agent-sdk/overview
https://x.com/trq212

**AI Summary**
This workshop by Thariq Shihipar (Anthropic) details the architecture and implementation of the **Claude Agent SDK**. The session moves from high-level theory—defining "agents" as autonomous systems that manage their own context and trajectory—to a live-coding demonstration. Shihipar builds an agent "Harness" from scratch, implementing the core **Agent Loop** (Context  Thought  Action  Observation), integrating the **Bash tool** for general computer use, and demonstrating **Context Engineering** via the file system to maintain state across long tasks.

**Timestamps**

00:00 Introduction: Agenda and the "Agent" definition
05:15 The "Harness" concept: Tools, Prompts, and Skills
10:10 Live Coding Setup: Initializing the Agent class and environment
15:45 implementing the "Think" step: Getting the model to reason before acting
25:20 The Agent Loop: connecting `act`, `observe`, and `loop`
33:10 Tool Execution: Handling XML parsing and tool inputs
42:00 The "Bash" Tool: Giving the agent command line access
49:30 Safety & Permissions: "ReadOnly" vs "ReadWrite" file access
58:15 Context Engineering: Using `ls` and `cat` to build dynamic context
01:05:00 The "Monitor": Viewing the agent's thought process in real-time
01:12:45 Handling "Stuck" States: Feedback loops and error correction
01:21:20 Multi-turn Complex Tasks: Building a "Research Agent" demo
01:35:10 Refactoring patterns: "Hooks" and deterministic overrides
01:48:39 Q&A: Reproducibility, helper scripts, and non-determinism
01:50:31 Q&A: Strategies for massive codebases (50M+ lines)
01:52:00 Closing remarks and future SDK roadmap

* **Evolution of AI Capabilities:** Shihipar argues we are shifting from **LLM Features** (categorization, single turn) to **Workflows** (structured, multi-step chains like RAG) to **Agents**. He defines agents as systems that *"build their own context, decide their own trajectories, and work very autonomously"* rather than following a rigid pipeline.
* **The Claude Agent SDK Architecture:** The SDK is built directly on top of **Claude Code** because Anthropic found they were *"rebuilding the same parts over and over again"* for internal tools.
* **The Harness:** A robust agent requires more than just a model; it needs a "Harness" containing Tools, Prompts, a **File System**, Skills, Sub-agents, and Memory.
* **Opinionated Design:** The SDK bakes in lessons from deploying Claude Code, specifically the "opinion" that general computer use (Bash) is often superior to bespoke tools.


* **The Power of the Bash Tool:** A key technical insight is that the **Bash tool** is often the most powerful tool for an agent. Instead of building custom tools for every action (e.g., a specific API wrapper for a file conversion), giving the agent access to the shell allows it to use existing software (like `ffmpeg`, `grep`, or `git`) to solve problems flexibly, similar to how a human developer works.
* **Context Engineering:** Shihipar introduces the concept of **Context Engineering** via the file system. Instead of just "Prompt Engineering," the agent uses the file system to manage its state and context.
* **Files as Memory:** The agent can write to files to "remember" things or create its own documentation (e.g., `CLAUDE.md`) to ground future actions.
* **Verification:** The file system serves as a ground truth for the agent to verify its work (e.g., checking if a file was actually created).


* **The Agent Loop & Intuition:** Building a successful agent loop is described as *"kind of an art or intuition"*. The loop generally follows a **Gather Context  Take Action  Verify Work** cycle. Shihipar emphasizes that this loop allows the agent to self-correct, a capability missing from rigid workflows.
* **Strategies for Determinism (Hooks):** During the Q&A, a technique for controlling agent behavior is discussed: **Hooks**.
* If an agent hallucinates or skips a step (e.g., guessing a Pokemon stat instead of checking a script), a hook can intercept the response and inject feedback: *"Please make sure you write a script, please make sure you read this data."*
* This enforces rules like "read before you write" without retraining the model.


* **Scaling to Large Codebases:** For massive codebases (50M+ lines), standard tools like `grep` or basic context window stuffing fail.
* **Semantic Search Limitations:** Shihipar notes that while semantic search is a common solution, it is *"brittle"* because the model isn't trained on the specific semantic index.
* **Solution:** He recommends good **"Claude MD"** files (context files) and starting the agent in a specific subdirectory to limit scope, rather than trying to index the entire 50M lines at once.

## Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)

- Upload date: 2025-12-30
- Video: https://www.youtube.com/watch?v=xz0-brt56L8
- Transcript: raw/20251230_xz0-brt56L8/xz0-brt56L8.en-orig.vtt
- Metadata: raw/20251230_xz0-brt56L8/xz0-brt56L8.info.json

AI agents are no longer confined to chat interfaces. From our original Manus app for powerful conversations, to Mail Manus for transforming your inbox into an organized command center, we've progressively expanded where an AI can work. Now, with the Manus API, we're completing the vision by giving you the final building block to deploy an intelligent agent anywhere in your stack.

In this workshop, you'll learn to use the API to build a bespoke research agent that powers deep analysis across your company's internal data. We'll show you how to dispatch a task that connects to your private systems, synthesises complex information, and delivers custom insights on demand, turning your entire knowledge base into an actionable, intelligent asset.

In this hands-on session, you will:

- Use the Manus API to dispatch and manage asynchronous agentic tasks.
- Connect the agent to private data sources using our connectors
- Build a complete workflow that synthesises information into a custom report.

By the end of the workshop you'll have a functional research agent that you can adapt for your own use case.

## SUMMARY

Ivan introduces **Manus 1.5** and the new **Manus API**, positioning Manus not just as a chatbot but as a "general action engine" capable of executing complex workflows, automating tasks, and extending human reach. Ivan Leo demonstrates the ecosystem—including a web app, Slack integration, browser operator, and Microsoft 365 integration—before diving into a workshop on building bespoke research agents. The session concludes with a Q&A covering advanced use cases like Python scripting for booking slots, browser security permissions, and future roadmap features like memory retention and document exporting.

**Timestamps:**

00:00 Introduction & Workshop Overview
00:53 What is Manus? (The Action Engine)
01:18 Manus 1.5 Updates (Performance, Quality, Architecture)
02:23 Manus Ecosystem (Web, Slack, API, Browser, M365)
03:15 Demo: French Learning App (Custom Web App)
06:02 Demo: Mail Manus (Email Automation)
06:51 Demo: Browser Operator (Coffee Search)
01:18:00 Use Case: Pickleball Booking Script
01:18:44 API & Browser Permissions
01:19:21 Future Features: Exporting to PPTX/PDF
01:20:05 Memory & Context Management

## Jack Morris: Stuffing Context is not Memory, Updating Weights is

- Upload date: 2025-12-29
- Video: https://www.youtube.com/watch?v=Jty4s9-Jb78
- Transcript: raw/20251229_Jty4s9-Jb78/Jty4s9-Jb78.en-orig.vtt
- Metadata: raw/20251229_Jty4s9-Jb78/Jty4s9-Jb78.info.json

Understanding how memory works in large language models through the lens of weights and activations. This workshop will explore the internal mechanisms of how LLMs store and retrieve information during inference.

https://x.com/jxmnop

**Summary**
Jack Morris discusses the limitations of current Large Language Models (LLMs) in handling niche, "long-tail" knowledge that falls outside their training data or within knowledge cutoffs. He critiques the reliance on massive context windows and Retrieval Augmented Generation (RAG) due to their high cost and latency (quadratic complexity of self-attention). The core thesis advocates for a third paradigm: **"training things into weights,"** or efficiently injecting specific knowledge directly into model parameters, effectively treating weights as a memory storage mechanism distinct from the "working memory" of activations.

**Timestamps**

00:00 The Knowledge Cutoff & Long-Tail Problem
02:22 Three Methods for Knowledge Injection (Context, RAG, Weights)
03:29 Limitations of "Full Context" (Cost & Latency)
05:12 The Transformer Bottleneck: Self-Attention Complexity
06:49 Context Rot: Performance degradation in long context
58:49 Q&A: The Return of Federated Learning
59:34 Q&A: Specialized Knowledge Models vs. Karpathy’s "Reasoning Engines"
01:01:21 Q&A: Temporal Information & Future Research

**Technical Summary**

* **The "Long Tail" Knowledge Problem**: Morris identifies a critical failure mode in current LLMs: they excel at general knowledge (e.g., "Did the Blue Jays win the World Series?") but fail catastrophically at **niche, specific tasks** (e.g., "Optimize this AMD GPU kernel" or "What are the terms of the BlackRock partnership?").
* *Constraint*: These tasks are either outside the training data, subject to knowledge cutoffs, or require private data.
* *Failure of Prompting*: No amount of "please" or prompt engineering can force a model to know facts it simply doesn't have stored.


* **The Three Paradigms of Knowledge Injection**:
* **Full Context**: Stuffing all relevant data into the prompt. Works for small domains (e.g., a single medical record) but scales poorly.
* **RAG (Retrieval Augmented Generation)**: Retrieving only relevant chunks.
* **Training into Weights**: The proposed solution. Injecting knowledge directly into the model's parameters (weights) rather than its transient state (activations).


* **The "Context Trap": Cost and Latency**:
* **Quadratic Dependency**: The self-attention mechanism in Transformers requires every token to look at every other token, creating a quadratic compute cost.
* **Latency Impact**: Morris shares benchmarks: "If you have 1,000 tokens of context, we can output **10,000 tokens per second**. If you have 128k tokens of context, we can output **130 tokens per second**." This is an orders-of-magnitude slowdown.
* **Performance Degradation**: He cites the *Chroma "Context Context Broad"* report, showing that as context grows, reasoning capabilities degrade even if the model doesn't "break".


* **Weights vs. Activations (Inferred from thesis)**:
* The talk distinguishes between **activations** (short-term, expensive context) and **weights** (long-term, efficient storage).
* Morris argues that for niche, static knowledge (like internal company wikis or specialized codebases), updating weights is more efficient than re-feeding context every inference cycle.


* **Q&A: Federated Learning & Distributed Training**:
* Federated learning (training across many machines) failed previously due to network costs of syncing massive models.
* Morris predicts a comeback because "you only need to train a million parameters instead of a trillion," making the network overhead manageable for specialized knowledge updates.


* **Q&A: Specialized Models vs. General Reasoners**:
* Responding to Andrej Karpathy's view of LLMs as pure "reasoning engines" (small brains, using tools), Morris argues there is a middle ground.
* *Analogy*: "A lawyer doesn't have the entire legal code memorized, but they know how to use tools." However, a model that "knows nothing" is inefficient. He advocates for **specialized models** that are "good at something you care about but bad at other things," rather than a generic reasoning engine that relies entirely on external retrieval.

## AGI: The Path Forward – Jason Warner & Eiso Kant, Poolside

- Upload date: 2025-12-27
- Video: https://www.youtube.com/watch?v=OGCG_QkCcZo
- Transcript: raw/20251227_OGCG_QkCcZo/OGCG_QkCcZo.en-orig.vtt
- Metadata: raw/20251227_OGCG_QkCcZo/OGCG_QkCcZo.info.json

In Poolside's first ever public conference demo, Poolside's CEOs present their vision and roadmap towards achieving AGI-level capabilities for knowledge work.

## How Claude Code Works - Jared Zoneraich, PromptLayer

- Upload date: 2025-12-26
- Video: https://www.youtube.com/watch?v=RFKCzGlAU6Q
- Transcript: raw/20251226_RFKCzGlAU6Q/RFKCzGlAU6Q.en-orig.vtt
- Metadata: raw/20251226_RFKCzGlAU6Q/RFKCzGlAU6Q.info.json

Deep dive into what we have independently figured out about the architecture and implementation of Claude's code generation capabilities. Not officially endorsed by Anthropic.

Speaker: Jared Zoneraich  |  Founder & CEO, PromptLayer
https://x.com/imjaredz
https://www.linkedin.com/in/imjaredz
https://imjaredz.com/


Jared Zoneraich from PromptLayer dissects the architecture of "Claude Code" (Anthropic's CLI agent), arguing that its success stems not from complex agentic frameworks but from a radical simplification: a single-threaded "Master Loop" paired with highly capable models. He contrasts this "give it tools and get out of the way" approach with earlier, brittle DAG-based (Directed Acyclic Graph) architectures. The talk breaks down the specific internal tools (Bash, FileEdit, Grep), the "Todo" planning mechanism, and the critical role of sandboxing and system prompts in making the agent reliable for production engineering tasks.

**Timestamps:**

00:00 Introduction to Claude Code & AI Coding Agents
04:35 The Evolution and Breakthroughs of Coding Agents
07:54 Core Philosophy: Simple Architecture & Better Models
12:11 Key Tools and Their Functionality in Claude Code
15:52 The Power of Bash and Implementation of To-Do Lists
19:25 Structure of To-Do Lists vs. Complex DAGs
23:24 Relying on the Model & Importance of Sandboxing
27:23 Sandboxing, Sub-Agents, and System Prompts
31:55 System Prompts and the Use of "Skills"
36:05 Challenges with Skills & Future Innovations
39:21 Alternative Architectures: The "AI Therapist" Problem
42:14 Perspectives on Different Agents: Codex vs. Amp
45:03 Context Management in Amp & Cursor
48:42 Evaluating Coding Agents & Rigorous Tools
52:01 Testing Tools & Future of Headless SDKs
55:11 Key Takeaways & Building the Slide Deck with Claude Code
57:25 Discussion on DAGs and Sequential Execution
01:00:15 The Future of LLM Calls and Spec-Driven Development

## Shipping AI That Works: An Evaluation Framework for PMs – Aman Khan, Arize

- Upload date: 2025-12-26
- Video: https://www.youtube.com/watch?v=2HNSG990Ew8
- Transcript: raw/20251226_2HNSG990Ew8/2HNSG990Ew8.en-orig.vtt
- Metadata: raw/20251226_2HNSG990Ew8/2HNSG990Ew8.info.json

GenAI is reshaping the product landscape, creating huge opportunities (along with new expectations) for product managers. Yet while prompt engineering and model tuning get the spotlight, one critical skill can get overlooked: rigorous evaluation.

This talk will help PMs move beyond gut-feel “vibe checks” to adopt concrete, repeatable evaluation strategies for LLM-powered products. I'll break down essential eval methodologies, from human feedback and code-based checks to cutting-edge LLM-based evaluations. Drawing on real-world examples, I'll share a practical framework PMs can use to:

- Confidently evaluate AI-driven features
- Ground decisions in real, repeatable data
- Build trust and delight through consistent quality

## Why Agent Hype can fall short of reality – Joel Becker, METR

- Upload date: 2025-12-24
- Video: https://www.youtube.com/watch?v=RhfqQKe22ZA
- Transcript: raw/20251224_RhfqQKe22ZA/RhfqQKe22ZA.en-orig.vtt
- Metadata: raw/20251224_RhfqQKe22ZA/RhfqQKe22ZA.info.json

AI models are crushing benchmarks. SWE-bench scores are climbing, and METR's measured time horizons are rising rapidly. Yet when we deployed these same models in a field study with experienced developers, they didn't speed up work. What's going on? Are benchmarks misleading us about AI capabilities? Are we missing something about how AI performs in the real world? In this talk, we'll reconcile lab and field evidence on AI capabilities. Drawing from METR's time horizon measurements and developer productivity RCT, we'll explore why impressive benchmark performance doesn't always translate to real-world impact. We'll examine potential explanations—from reliability requirements to task distribution to capability elicitation—and discuss what this means for automated AI R&D.

Speaker: Joel Becker  |  Researcher, METR
https://x.com/joel_bkr
https://www.linkedin.com/in/joel-becker/
https://github.com/joel-becker


**Timestamps:**

00:00 Introduction to METR & The Capability Gap
01:49 The Problem with Current Benchmarks (Saturation & Interpretation)
03:19 METR’s New Methodology: Human Time Horizons
04:52 Empirical Results: Fitting Capability Curves
06:19 Time Horizon Trends: Claude 3 Opus vs. o1-preview
17:43 Randomized Controlled Trial (RCT) Discussion
18:18 Reconciling the Gap: Why High Benchmarks Don't Mean High Productivity
19:18 Explaining the Discrepancy: Context, Reliability, and Task Interdependence
20:22 Future Work & Hiring at METR

## Developer Experience in the Age of AI Coding Agents – Max Kanat-Alexander, Capital One

- Upload date: 2025-12-23
- Video: https://www.youtube.com/watch?v=rT2Del5pwg4
- Transcript: raw/20251223_rT2Del5pwg4/rT2Del5pwg4.en-orig.vtt
- Metadata: raw/20251223_rT2Del5pwg4/rT2Del5pwg4.info.json

It feels like every two weeks, the world of software engineering is being turned on its head. Are there any principles we can rely on that will continue to hold true, and that can help us prepare for the future, no matter what happens? Max uses research, data, and his 20+ years working in enterprise Developer Experience teams to talk through what we can do now that will prepare us for an agentic future, no matter what that future holds.

Speaker: Max Kanat-Alexander  |  Executive Distinguished Engineer, Capital One
https://x.com/mkanat
https://www.linkedin.com/in/mkanat/
https://max.kanat.us/


Timestamps

00:00 The "New Hotness" Fatigue & Unpredictability 
01:58 The "No Regrets" Investment Framework
02:55 Input 1: Standardized Development Environments 
04:40 Input 2: Native CLIs and APIs for Agents 
05:08 Input 3: Deterministic Validation & Actionable Errors 
06:45 Input 4: Structure of Systems & Legacy Code 
14:35 The Necessity of Apprenticeship in Code Review 
15:00 The Vicious Cycle: Bad Codebases Break Agents 
15:54 The Virtuous Cycle: Better DevEx Accelerates Agents 
16:30 Summary Checklist & Conclusion

## The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize

- Upload date: 2025-12-23
- Video: https://www.youtube.com/watch?v=pP_dSNz_EdQ
- Transcript: raw/20251223_pP_dSNz_EdQ/pP_dSNz_EdQ.en-orig.vtt
- Metadata: raw/20251223_pP_dSNz_EdQ/pP_dSNz_EdQ.info.json

Your coding agent writes code—but not like your team. RL has boosted base models, but it’s opaque and hard to scale across enterprises. Most agents still rely on brittle, hand-edited system prompts or style guides (e.g., agent.md)—what if your agent learned from your reviews and updated them automatically? In this talk, I’ll show a system-prompt learning loop—RL techniques applied to prompts, not model weights—that continually tunes an agents.md, so the agent learns instructions from your PR's, feedback & evaluations. You’ll leave with a concrete recipe to capture runtime signals, and auto-tune system prompts—applicable to any type of agent you’re building.

Speakers: 
Aparna Dhinakaran  |  Co-founder & CPO, Arize
https://x.com/aparnadhinak
https://www.linkedin.com/in/aparnadhinakaran/

## Small Bets, Big Impact Building GenBI at a Fortune 100 – Asaf Bord, Northwestern Mutual

- Upload date: 2025-12-23
- Video: https://www.youtube.com/watch?v=LU9KgcZDRfY
- Transcript: raw/20251223_LU9KgcZDRfY/LU9KgcZDRfY.en-orig.vtt
- Metadata: raw/20251223_LU9KgcZDRfY/LU9KgcZDRfY.info.json

Enterprises don’t usually make moonshots, especially in GenAI. Governance, budgets, and risk aversion make it almost impossible to justify a huge, uncertain investment.

At Northwestern Mutual, we’re building GenBI, an LLM-powered analytics copilot, by flipping that logic. Instead of one big bet, we created an incremental roadmap of small, fundable projects. Each is tied to real business outcomes, delivers measurable ROI, and builds the trust needed to move forward.

This talk shares how we framed the problem, earned leadership support, and designed a modular architecture grounded in real data. We’ll show how each research step can stand on its own - productized, measurable, and deployable. Attendees will leave with a clear blueprint for making AI transformation fundable, governable, and real inside large, risk-averse organizations.

Speaker: Asaf Bord  |  AI Product Lead, Northwestern Mutual
https://www.linkedin.com/in/asafbord/recent-activity/all/
https://asafbord.wixsite.com/home

## Amp Code: Next Generation AI Coding – Beyang Liu, Amp Code

- Upload date: 2025-12-22
- Video: https://www.youtube.com/watch?v=gvIAkmZUEZY
- Transcript: raw/20251222_gvIAkmZUEZY/gvIAkmZUEZY.en-orig.vtt
- Metadata: raw/20251222_gvIAkmZUEZY/gvIAkmZUEZY.info.json

Introduction to Amp Code and its approach to AI-powered software development.

Speaker: Beyang Liu  |  Co-founder & CTO, Amp Code
https://x.com/beyang
https://www.linkedin.com/in/beyang-liu/
https://github.com/beyang

Timestamps:

00:00 Introduction & The "Weird" Ethos 
01:19 Amp Terminal UI & Editor Integration 
03:02 The "Review Bottleneck" & Review Interface 
03:57 Defining an Agent: For Loops & Tool Calls 
04:46 The Argument Against MCP (Context Confusion) 
06:04 Tool Call Context Exhaustion 
14:51 Business Model: Ads in the Terminal 
15:38 Community & The "Weird" Builder Cohort

## Making Codebases Agent Ready – Eno Reyes, Factory AI

- Upload date: 2025-12-22
- Video: https://www.youtube.com/watch?v=ShuJ_CN6zr4
- Transcript: raw/20251222_ShuJ_CN6zr4/ShuJ_CN6zr4.en-orig.vtt
- Metadata: raw/20251222_ShuJ_CN6zr4/ShuJ_CN6zr4.info.json

Agents are eating software engineering. Yet teams deploying these tools face mixed results. Agents work great in demos but fail unreliably in production, frustrating engineering teams who expected better. The gap isn't model quality—it's environment readiness. Agents need fast feedback loops, explicit instructions, and predictable environments to work effectively. They break on missing environment variables, undocumented dependencies, and tribal knowledge that "everyone just knows."

What if you could measure and fix what's holding your agents back? Enter Agent Readiness. In this talk, we'll explore eight categories that determine whether your codebase is agent-ready: from style validation and build systems to dev environments and observability. You'll learn how to score your repos, identify easy wins, and build environments where agents actually ship reliable code. We'll share real signals from Factory's work running autonomous agents in enterprise production repos—and give you a practical framework to make your team's agents more productive starting tomorrow.

Speaker:  Eno Reyes  |  CTO, Factory AI
https://x.com/EnoReyes
https://www.linkedin.com/in/enoreyes/
https://enoreyes.com/

The video argues that the primary bottleneck for adopting AI agents in software engineering is not model capability, but rather the "agent readiness" of the codebase—specifically the rigour of automated verification systems. Eno Reyes from Factory AI posits that software development is shifting from a specification-based process to a verification-based one (Software 2.0), where the ability to mechanically validate code (via linters, tests, and strict environments) determines an agent's success. He suggests that organizations must invest in these feedback loops to create a "flywheel" effect: better environments lead to better agents, which in turn free up time to further improve the environment.

00:00 Introduction & Factory AI Mission 
01:19 Software 2.0: Automation via Verification 
02:21 The Asymmetry of Verification (P vs NP) 
04:01 Automated Validation as an Agent Constraint 
06:09 Shift to Specification-Driven Development 
11:51 The New DevX Loop: Investing in Feedback Cycles 
13:42 Conclusion: The ROI of Agent Readiness

## The 3 Pillars of Autonomy – Michele Catasta, Replit

- Upload date: 2025-12-22
- Video: https://www.youtube.com/watch?v=MLhAA9yguwM
- Transcript: raw/20251222_MLhAA9yguwM/MLhAA9yguwM.en-orig.vtt
- Metadata: raw/20251222_MLhAA9yguwM/MLhAA9yguwM.info.json

AI agents exhibit vastly different degrees of autonomy. Yet, the ability to accomplish objectives without supervision is the critical north star for agent progress, especially in software creation. For non-technical users who cannot supervise software creation, full autonomy is essential, not optional.

First of all, I will discuss two foundational capabilities to achieve true autonomy: automatic testing to verify correctness without human validation, and advanced context management to maintain coherence across complex, long-horizon tasks.

With autonomy established, parallelization becomes the key to delivering a compelling user experience. Sequential execution forces users to wait extensively before seeing progress, breaking the development flow. This talk explores parallelization models (task-level parallelism, out-of-order execution, plan decomposition, etc.) and their tradeoffs in latency, resource consumption, and correctness guarantees.


Speaker:  Michele Catasta  |  VP of AI, Replit
https://x.com/pirroh
https://www.linkedin.com/in/pirroh/
https://github.com/pirroh

talk originally titled "Autonomy is all you need" and renamed after YouTube A/B test

## No More Slop – swyx

- Upload date: 2025-12-22
- Video: https://www.youtube.com/watch?v=IoiHI7p12Ao
- Transcript: raw/20251222_IoiHI7p12Ao/IoiHI7p12Ao.en-orig.vtt
- Metadata: raw/20251222_IoiHI7p12Ao/IoiHI7p12Ao.info.json

Why we need to eliminate low-quality code and work in AI engineering.

Speaker: swyx  |  Curator, AI Engineer
https://x.com/swyx
https://www.linkedin.com/in/shawnswyxwang/
https://www.swyx.io/

## The Infinite Software Crisis – Jake Nations, Netflix

- Upload date: 2025-12-20
- Video: https://www.youtube.com/watch?v=eIoohUmYpGI
- Transcript: raw/20251220_eIoohUmYpGI/eIoohUmYpGI.en-orig.vtt
- Metadata: raw/20251220_eIoohUmYpGI/eIoohUmYpGI.info.json

In 1968, the term ""Software Crisis"" emerged when systems grew beyond what developers could manage. Every generation since has ""solved"" it with more powerful tools, only to create even bigger problems.

Today, AI accelerates the pattern into the Infinite Software Crisis. AI-generated codebases mirror the meandering conversations that created them. Every clarification and pivot gets baked into your architecture. We're vibecoding our way to disaster.

The solution: choose simple over easy. One long conversation is easy. Separate phases with clean boundaries are simple.

This talk presents a three-phase methodology:

- Research to understand the existing system
- Planning to design the approach
- Implementation with clean context

While everyone races to generate code at machine speed, the engineers who thrive will be those who know when a system is getting tangled. In the age of infinite code generation, human judgment applied at the right moments becomes your competitive advantage.

Speaker:  Jake Nations  |  Engineering, Netflix
https://www.linkedin.com/in/jakenations/
https://github.com/Nayshins

Timestamps:
00:00 The Modern Confession: Shipping Code We Don’t Understand 
01:53 The History of the Software Crisis (1968 to Present) 
03:30 Fred Brooks and "No Silver Bullet" 
04:12 Simple vs. Easy (Rich Hickey’s Definition) 
05:40 The AI Trap: "Vibecoding" and Conversational Complexity 
06:39 The problem with iterative AI chat interfaces 
15:12 Implementation Phase: Using Manual Migration as a Seed 
16:14 The Knowledge Gap: Code Generation vs. Code Understanding 
17:40 Conclusion: Software is a Human Endeavor

## From Arc to Dia: Lessons learned building AI Browsers – Samir Mody, The Browser Company of New York

- Upload date: 2025-12-19
- Video: https://www.youtube.com/watch?v=o4scJaQgnFA
- Transcript: raw/20251219_o4scJaQgnFA/o4scJaQgnFA.en-orig.vtt
- Metadata: raw/20251219_o4scJaQgnFA/o4scJaQgnFA.info.json

What happens when you take a polished, beloved browser and rebuild it from the ground up around AI? In 2024, The Browser Company did exactly that: transforming Arc, a human-designed browser, into Dia, a browser with an AI-native browser experience. The journey forced us to unlearn what we knew about product design, system architecture, and even what "good UX" means when the interface itself can reason, plan, and act.

In this talk, I'll share the lessons we learned along the way: how we redesigned for emergent behavior instead of deterministic control, how our engineering and design teams learned to prototype with language models, and how our culture evolved to ship fast in a world where we're still learning what a good system looks like. You'll leave with practical insights for building AI-native products, from technical architecture to team mindset, and a glimpse into how we're thinking about the future of AI browsing.

Speaker:  Samir Mody  |  Head of AI Engineering, The Browser Company
https://x.com/jedimody
https://www.linkedin.com/in/samir-mody/

## Welcome to AIE LEAD - Alex Lieberman, Tenex

- Upload date: 2025-12-19
- Video: https://www.youtube.com/watch?v=RQ5Jt8zDBp8
- Transcript: raw/20251219_RQ5Jt8zDBp8/RQ5Jt8zDBp8.en-orig.vtt
- Metadata: raw/20251219_RQ5Jt8zDBp8/RQ5Jt8zDBp8.info.json

more at https://ai.engineer

## Leadership in AI Assisted Engineering – Justin Reock, DX (acq. Atlassian)

- Upload date: 2025-12-19
- Video: https://www.youtube.com/watch?v=PmZDupFP3UM
- Transcript: raw/20251219_PmZDupFP3UM/PmZDupFP3UM.en-orig.vtt
- Metadata: raw/20251219_PmZDupFP3UM/PmZDupFP3UM.info.json

To realize meaningful returns on AI investments, leadership must take accountability and ownership of establishing best practices, enabling engineers, measuring impact, and ensuring proper guardrails are in place. When prompting practice and reflexive AI use is driven from the top down, engineers can align on the highest value use cases and experience peak productivity gains. When coupled with DX's AI Measurement Framework, leaders can gain a clear picture of AI's true impact, identify the real bottlenecks in the SDLC that can be augmented with AI, and drive improvement. In this session, Justin Reock, Deputy CTO at DX, and author of DX's Guide to AI Assisted Engineering, will explain what the most effective leaders of AI enabled engineering organizations are doing to drive satisfactory utilization, augmentation, and psychological safety across their teams. Based on interviews, use cases, and data, leaders will walk away with an understanding of how to best lead their teams through mature AI rollouts.

Speaker:  Justin Reock  |  Deputy CTO, DX
https://www.linkedin.com/in/justinreock/

## Paying Engineers like Salespeople – Arman Hezarkhani, Tenex

- Upload date: 2025-12-19
- Video: https://www.youtube.com/watch?v=4mRekpZpBZs
- Transcript: raw/20251219_4mRekpZpBZs/4mRekpZpBZs.en-orig.vtt
- Metadata: raw/20251219_4mRekpZpBZs/4mRekpZpBZs.info.json

Most software teams still run on an outdated unit of measure: hours, days, years.

That single choice misaligns every incentive—clients want fewer, engineers want more, and everyone loses speed.

At Tenex, we threw the hourly model out and built an outcome-based system where we pay and charge per story point, tying incentives directly to shipped value.

In this talk, I’ll break down exactly how it works—the math, the cultural shifts, the AI tooling that makes it possible, and the results we’ve seen across real client projects. You’ll leave with a blueprint for running a high-trust, high-velocity engineering team that scales output, not overhead.

Speakers: Arman Hezarkhani  |  CTO, Tenex
https://x.com/ArmanHezarkhani
https://www.linkedin.com/in/ahez/
https://armanh.com/

## AI Consulting in Practice – NLW, Superintelligent, @AIDailyBrief⁩

- Upload date: 2025-12-18
- Video: https://www.youtube.com/watch?v=ehQFj6VmuI8
- Transcript: raw/20251218_ehQFj6VmuI8/ehQFj6VmuI8.en-orig.vtt
- Metadata: raw/20251218_ehQFj6VmuI8/ehQFj6VmuI8.info.json

Insights from consulting on AI implementation across various organizations.

Speaker: NLW  |  Host, AI Daily Brief & CEO, Super.ai
https://x.com/nlw
https://www.youtube.com/@AIDailyBrief

## Dispatch from the Future: building an AI-native Company – Dan Shipper, Every, AI & I

- Upload date: 2025-12-18
- Video: https://www.youtube.com/watch?v=MGzymaYBiss
- Transcript: raw/20251218_MGzymaYBiss/MGzymaYBiss.en-orig.vtt
- Metadata: raw/20251218_MGzymaYBiss/MGzymaYBiss.info.json

The central thesis is that there is a "10x difference" between an organization where 90% of engineers use AI versus one where 100% do. At 100% adoption, the fundamental physics of software engineering change: a single developer can build and maintain complex production apps, managers can meaningfully contribute to code, and the organization can move from a "memo culture" to a "demo culture." He introduces the concept of "Compounding Engineering"—where every feature built creates artifacts and agents that make building the next feature easier—and argues that we are shifting from text-editor-based coding to agentic, delegated workflows (Claude Code) that allow for parallel processing and "fractured attention" work.

Timestamps:

00:00 Introduction & The "No Playbook" Reality 
02:11 The 10x Difference: 90% vs 100% AI Adoption 
03:16 Every's "AI Native" Structure (15 people, 4 products) 
04:14 Product Examples: Kora, Monologue, & Spiral 
05:30 The Shift to Cloud Code & Agentic Workflows 
06:00 Parallel Execution & Vibe Coding 
07:20 The Rise of "Demo Culture" 
14:00 Cross-App Collaboration & Customer Agents 
14:35 The Polyglot Stack Advantage 
15:09 Managers Committing Code & Fractured Attention 
16:20 Compounding Engineering & Conclusion

AIE is coming to London and SF! see dates and sign up to be notified of sponsorships, CFPs, and tickets: https://ai.engineer

## Code World Model: Building World Models for Computation – Jacob Kahn, FAIR Meta

- Upload date: 2025-12-17
- Video: https://www.youtube.com/watch?v=sYgE4ppDFOQ
- Transcript: raw/20251217_sYgE4ppDFOQ/sYgE4ppDFOQ.en-orig.vtt
- Metadata: raw/20251217_sYgE4ppDFOQ/sYgE4ppDFOQ.info.json

Today, most neural models for code learn from code itself: sequences of tokens that capture syntax rather than computation. While this allows models to learn the shape of code, true reasoning about programs requires understanding execution and the dynamics of computation. In this talk, I’ll present a world-model approach to learning from code: one that incorporates data from program execution to implicitly predict behavior while generating code. The Code World Model (CWM) embodies this paradigm, opening new capabilities for reasoning and offering a foundation for future research and prototyping in AI-driven software systems.

Speaker: Jacob Kahn  |  Research Scientist, FAIR, Meta
https://www.linkedin.com/in/jacobdavidkahn/

## AI Kernel Generation: What's working, what's not, what's next – Natalie Serrino, Gimlet Labs

- Upload date: 2025-12-17
- Video: https://www.youtube.com/watch?v=6guQG_tGt0o
- Transcript: raw/20251217_6guQG_tGt0o/6guQG_tGt0o.en-orig.vtt
- Metadata: raw/20251217_6guQG_tGt0o/6guQG_tGt0o.info.json

In this talk, we'll talk about how AI generated kernels can meaningfully speed up custom PyTorch code, without any human effort.

Lots of great frameworks exist to optimize PyTorch with programmatic optimizations, such as Triton and MLX. But the strongest AI performance gains come from hand-written, low-level kernels that are targeted to the exact device and workload. These are tedious and time-consuming to write, especially when supporting multiple platforms. What if we could automate this process with AI?

We'll cover the best practices for AI generating low-level kernels, from how to test and validate the kernels, and what type of agents and contexts are needed to get the best results. We'll cover the research we did where this approach improved PyTorch inference performance on Apple devices.

Speaker:  Natalie Serrino  |  Cofounder, Gimlet Labs
https://x.com/nserrino
https://www.linkedin.com/in/natalieserrino/

## Your Support Team Should Ship Code – Lisa Orr, Zapier

- Upload date: 2025-12-16
- Video: https://www.youtube.com/watch?v=RmJ4rTLV_x4
- Transcript: raw/20251216_RmJ4rTLV_x4/RmJ4rTLV_x4.en-orig.vtt
- Metadata: raw/20251216_RmJ4rTLV_x4/RmJ4rTLV_x4.info.json

Zapier maintains 8000+ integrations that break as APIs change. We had thousands of backlog support tickets with dozens more arriving weekly. To keep up with the traffic, we started building AI tools to help ship integration fixes faster. We began by shadowing engineers fixing tickets and building tools we believed would expedite the fix process. Our first effort, an API playground hosting AI tools like diagnosis and test generation, failed to get engineering traffic because it pulled builders out of their workflows. We pivoted to MCP tools that engineers could use directly in their IDEs. MCP tools gained traction, but our most valuable tool, Diagnosis, took too long to run. Engineers wouldn't wait for it, revealing we needed an asynchronous approach. We built Scout Agent to string our tools together, autonomously reading support tickets, gathering context, generating fixes with tests, and submitting merge requests ready for review. This agent approach has gained traction with our support team handling high ticket volumes. An MR ready for review means they can validate and ship a fix quickly before needing to jump on the next incoming ticket. Throughout this process we've learned that the real challenge is everything surrounding code generation. Before writing code, Scout Agent needs both the right context and to show its work so engineers trust its recommendations. After generation, engineers need to quickly validate and correct the proposed fix, otherwise MRs sit unreviewed and abandoned. Embedding Scout Agent directly in GitLab solved this. Teams can iterate on proposed solutions without context switching. To track improvement, we measure three distinct failure modes: categorization accuracy (should Scout attempt this ticket?), fixability assessment (does this need a code fix?), and solution quality (does the generated code actually work?). Each reveals different improvement opportunities. Today, Scout drives 40% of support's integration fixes, with expansion to engineering teams and downstream automation (testing, shipping, migration) as our next frontiers.

Speaker: Lisa Orr  |  Product Leader, Zapier
https://x.com/orreither
https://www.linkedin.com/in/lisaorr/

## What We Learned Deploying AI within Bloomberg’s Engineering Organization – Lei Zhang, Bloomberg

- Upload date: 2025-12-16
- Video: https://www.youtube.com/watch?v=Q81AzlA-VE8
- Transcript: raw/20251216_Q81AzlA-VE8/Q81AzlA-VE8.en-orig.vtt
- Metadata: raw/20251216_Q81AzlA-VE8/Q81AzlA-VE8.info.json

When it comes to using AI for software engineering, much of the spotlight falls on how large language models (LLMs) can write code—sometimes entirely from scratch. Countless studies highlight productivity gains from turning requirements directly into runnable code. But the reality of applying AI at scale inside a mature engineering organization is far more complex and nuanced. Over the past year, we’ve been on that journey at Bloomberg—integrating AI into the workflows of 9,000+ software engineers—and we’ve learned a few important lessons worth sharing:

Where the real ROI lies once you move beyond toy examples
What it takes to actually enable AI across a large, established engineering org
The best practices, cultural shifts, and guardrails that are required to make it work in practice
If you’re wondering what happens after the first demo magic fades and the real work begins, this talk is for you.

Speaker: Lei Zhang  |  Head of Technology Infrastructure Engineering, Bloomberg

Timestamps

00:00 Introduction to Bloomberg's Scale & Infrastructure 
03:32 AI for Coding: Initial Adoption & The "Greenfield" Drop-off 
06:14 Uplift Agents: Automating Refactoring & Maintenance 
08:40 Incident Response Agents: Unbiased Troubleshooting & Speed 
09:37 The "Paved Path": Standardizing AI Tool Building (MCP) 
11:51 Platform Components: Gateway, Discovery Hub, and Deployment 
13:34 Leveraging Training & Communities for Adoption 
16:15 The Leadership Gap & The Changing Cost Function of Engineering

## Coding Evals: From Code Snippets to Codebases – Naman Jain, Cursor

- Upload date: 2025-12-15
- Video: https://www.youtube.com/watch?v=tHN44yJoeS8
- Transcript: raw/20251215_tHN44yJoeS8/tHN44yJoeS8.en-orig.vtt
- Metadata: raw/20251215_tHN44yJoeS8/tHN44yJoeS8.info.json

AI coding capabilities have leapt from generating one-line snippets to competing entire codebases with agentic workflows. I’ll trace that arc focusing on learnings and challenges through each stage. I will start with early testable coding benchmarks distilling lessons about contamination and distributional overfitting. Next, moving beyond isolated programming problems, I will talk about repository grounded coding problems from SWE-bench style bug fixing, and R2E’s automated function completion setting. We’ll then move beyond isolated functions to longer-horizon tasks—runtime optimization (GSO), translation (Syzygy), and refactoring—highlighting challenges like test hacking, code quality, and idiomaticity. Finally, beyond code generation, I will talk about human preference evaluation in chatting (LMArena RepoChat) and developer-preference signals in-IDE via Copilot Arena.

Speaker:  Naman Jain  |  Engineering, Cursor
https://www.linkedin.com/in/naman1205jain/
https://x.com/StringChaos

## Building in the Gemini Era – Kat Kampf & Ammaar Reshi, Google DeepMind

- Upload date: 2025-12-15
- Video: https://www.youtube.com/watch?v=fgkXEIbZpGc
- Transcript: raw/20251215_fgkXEIbZpGc/fgkXEIbZpGc.en-orig.vtt
- Metadata: raw/20251215_fgkXEIbZpGc/fgkXEIbZpGc.info.json

A deep dive into the latest capabilities of Google DeepMind's Gemini 3 and the newly released "Nano Banana Pro" image model within Google AI Studio. Kat and Ammaar demonstrate "vibe coding"—a new paradigm where complex, aesthetic, and functional applications are built entirely through natural language prompts. They highlight how Gemini 3 excels at one-shot UI design and agentic tool use, while Nano Banana Pro integrates world knowledge and precise text rendering. The session concludes with live demos ranging from personalized comic books to a (mostly working) multiplayer racing game, emphasizing a future where software creation is democratized through full-stack AI runtime environments.

Timestamps
00:00 Intro & Gemini 3 Overview 
02:29 Nano Banana Pro Capabilities 
04:33 Vibe Coding in AI Studio 
07:13 Comic Book Demo: Text Rendering & Consistency 
10:33 Laptop Stickers Demo: Search Grounding 
12:00 "Anti-Gravity" & Ideating AI Studio Features 
13:42 3D Racing Game & Full Stack Runtime 
14:50 Live Multiplayer Demo Attempt
16:07 Democratizing Software & Closing Thoughts

Speakers:
• Kat Kampf  |  Product Manager, Google
https://x.com/kat_kampf
https://www.linkedin.com/in/kkampf/

• Ammaar Reshi  |  Product & Design Lead, Google
https://x.com/ammaar
https://www.linkedin.com/in/ammaarsreshi/
https://ammaar.me/

## From Vibe Coding To Vibe Engineering – Kitze, Sizzy

- Upload date: 2025-12-14
- Video: https://www.youtube.com/watch?v=JV-wY5pxXLo
- Transcript: raw/20251214_JV-wY5pxXLo/JV-wY5pxXLo.en-orig.vtt
- Metadata: raw/20251214_JV-wY5pxXLo/JV-wY5pxXLo.info.json

Web development has always moved in cycles of hype, from frameworks to tooling. With the rise of large language models, we're entering a new era of "vibe coding," where developers shape software through collaboration with Al rather than syntax. This talk explores what that means for the future of coding, especially in frontend development, and how it echoes the past while redefining what comes next.

Speaker: Kitze  |  Founder, Sizzy
https://x.com/thekitze

## Proactive Agents – Kath Korevec, Google Labs

- Upload date: 2025-12-13
- Video: https://www.youtube.com/watch?v=v3u8xc0zLec
- Transcript: raw/20251213_v3u8xc0zLec/v3u8xc0zLec.en-orig.vtt
- Metadata: raw/20251213_v3u8xc0zLec/v3u8xc0zLec.info.json

Speaker:  Kath Korevec  |  Director of Product, Google Labs
https://x.com/simpsoka
https://www.linkedin.com/in/kathleensimpson/

## Minimax M2: Building the #1 Open Model – Olive Song, MiniMax

- Upload date: 2025-12-13
- Video: https://www.youtube.com/watch?v=lY1iFbDPRlw
- Transcript: raw/20251213_lY1iFbDPRlw/lY1iFbDPRlw.en-orig.vtt
- Metadata: raw/20251213_lY1iFbDPRlw/lY1iFbDPRlw.info.json

Introducing Minimax's latest AI model and its applications in code generation.

Speaker:  Olive Song  |  Senior Researcher, MiniMax
https://x.com/olive_jy_song

## Moving away from Agile: What's Next – Martin Harrysson & Natasha Maniar, McKinsey & Company

- Upload date: 2025-12-12
- Video: https://www.youtube.com/watch?v=SZStlIhyTCY
- Transcript: raw/20251212_SZStlIhyTCY/SZStlIhyTCY.en-orig.vtt
- Metadata: raw/20251212_SZStlIhyTCY/SZStlIhyTCY.info.json

Most enterprises are not capturing much value from AI in software dev to date (at least relative to the potential). The reason is that most are adding AI tools to their dev teams without changing the people and operating model aspects (i.e., limited changes to ways of working, team configurations, role definitions, stage gates, etc.). Many core aspects of software development haven’t changed in the past 10+ years, and that’s holding us back from moving to the new paradigm of software development! We will share examples of what makes the difference.

https://www.linkedin.com/in/martinharrysson
https://www.linkedin.com/in/natasha-maniar-945276107/

## Hard Won Lessons from Building Effective AI Coding Agents – Nik Pash, Cline

- Upload date: 2025-12-12
- Video: https://www.youtube.com/watch?v=I8fs4omN1no
- Transcript: raw/20251212_I8fs4omN1no/I8fs4omN1no.en-orig.vtt
- Metadata: raw/20251212_I8fs4omN1no/I8fs4omN1no.info.json

Most of what’s written about AI agents sounds great in theory — until you try to make them work in production. The seductive ideas (multi-agent orchestration, RAG, prompt stacking) often collapse under real-world constraints. Why? Because they optimize for the wrong thing. In this talk, Nik Pash shares hard-won lessons from building large-scale coding agents at Cline — what failed, what survived, and why the next leap forward won’t come from clever scaffolds, but from evals and environments that truly measure and improve reasoning. Attendees will walk away with a clearer sense of what actually drives progress — and what’s just noise.

https://www.linkedin.com/in/nikpash

## The State of AI Code Quality: Hype vs Reality — Itamar Friedman, Qodo

- Upload date: 2025-12-11
- Video: https://www.youtube.com/watch?v=rgjF5o2Qjsc
- Transcript: raw/20251211_rgjF5o2Qjsc/rgjF5o2Qjsc.en-orig.vtt
- Metadata: raw/20251211_rgjF5o2Qjsc/rgjF5o2Qjsc.info.json

AI is making code generation nearly effortless, but the critical question remains: can we trust AI-generated code for software that truly matters? Has it really become easier to build robust, high-quality systems?

In this talk, we’ll separate hype from reality. Drawing on the State of AI Code Quality report, we’ll explore where AI tools excel, where they fall short, and which evaluation frameworks actually matter. We’ll unpack benchmarks, pitfalls, and lessons learned from deploying AI in real-world engineering workflows. Attendees will leave with a clearer understanding of how to measure, trust, and improve both AI-generated code and AI-driven code review—and what’s next for software quality in the age of AI.

Speaker: Itamar Friedman  |  CEO, Qodo
https://x.com/itamar_mar
https://www.linkedin.com/in/itamarf/

## Can you prove AI ROI in Software Eng? (Stanford 120k Devs Study) – Yegor Denisov-Blanch, Stanford

- Upload date: 2025-12-11
- Video: https://www.youtube.com/watch?v=JvosMkuNxF8
- Transcript: raw/20251211_JvosMkuNxF8/JvosMkuNxF8.en-orig.vtt
- Metadata: raw/20251211_JvosMkuNxF8/JvosMkuNxF8.info.json

You’re investing millions in AI for software engineering. Can you prove it’s paying off?

Benchmarks show models can write code, but in enterprise deployments ROI is hard to measure, easy to bias, and often distorted by activity metrics (PR counts, DORA) that say “more” without proving “better.”

Drawing on field data from 120k+ developers across 600+ companies, I’ll show exactly where AI helps the most and how to measure the ROI of your software engineering AI deployment.

We’ll unpack why identical tools deliver ~0% lift in some orgs and 25%+ in others.

You’ll leave with a step-by-step ROI playbook: what to track, the traps to avoid, and the habits top-quartile teams use to make the most from AI.

Speaker: Yegor Denisov-Blanch  |  Researcher, Stanford
https://x.com/yegordb
https://www.linkedin.com/in/ydenisov/

Timestamps

00:00 Introduction & Methodology: ML Panels of Experts 
00:21 The Research Approach: Time Series & Cross-Sectional Data 
01:38 Four Key Topics Overview 
02:01 Case Study: 10% Productivity Gain & The Widening Gap 
03:16 Factors Driving Performance: Usage vs. Quality 
04:02 The Environment Cleanliness Index 
05:30 Managing Codebase Entropy & AI Trust 
06:17 AI Engineering Practices Benchmark & Fingerprinting 
07:38 Case Study: Unequal Adoption Across Business Units 
08:31 Challenges in Measuring AI ROI via Business Outcomes 
10:28 Proposed Measurement Framework: Usage & Outcomes 
11:59 Metric Framework: Primary Output vs. Guardrails 
12:54 Case Study: AI Adoption's Negative Impact on Quality 
14:04 Rework, Refactoring, and Effective Output Analysis 
15:43 Conclusion & Call for Research Participation

## Agent Reinforcement Fine Tuning – Will Hang & Cathy Zhou, OpenAI

- Upload date: 2025-12-09
- Video: https://www.youtube.com/watch?v=p1CmPZ2j6Lk
- Transcript: raw/20251209_p1CmPZ2j6Lk/p1CmPZ2j6Lk.en-orig.vtt
- Metadata: raw/20251209_p1CmPZ2j6Lk/p1CmPZ2j6Lk.info.json

Deep dive into OpenAI's approach to reinforcement fine-tuning for code models.

https://x.com/willhang_
https://x.com/cathyzhou

AIE is coming to London and SF! see dates and sign up to be notified of sponsorships, CFPs, and tickets: https://ai.engineer

Timestamps:

00:00 Introduction to Agent RFT & What Defines an Agent 
01:45 Hierarchy of Agent Optimization (Prompting - Task Opt - RFT) 
02:53 New RFT Features: Public Endpoints & Custom Rewards 
03:55 Addressing Domain Shift & Latency via Exploration 
05:41 Recommended Workflow: Baseline First 
06:54 Case Study: Cognition (Code Editing & Parallelism) 
08:53 Case Study: Codto (Deep Research & Tail Latency) 
10:33 Case Study: Cosine (Enterprise Code & Strict Grading) 
12:50 Case Study: Macco (GPU Kernels & Reward Hacking) 
14:46 Four Principles for RFT Success

## Efficient Reinforcement Learning – Rhythm Garg & Linden Li, Applied Compute

- Upload date: 2025-12-09
- Video: https://www.youtube.com/watch?v=o15AaYl7Wu0
- Transcript: raw/20251209_o15AaYl7Wu0/o15AaYl7Wu0.en-orig.vtt
- Metadata: raw/20251209_o15AaYl7Wu0/o15AaYl7Wu0.info.json

Reinforcement learning (RL) is a powerful mechanism for building agents that are superhuman and specialized in particular tasks. At Applied Compute, RL is one of the fundamental building blocks that enables us to deliver automations and real business value for customers. Effective RL training often involves several iterative derisking runs to better understand learning dynamics with different base models, and then doing “hero” runs with the best configurations. If done naively, this can be very time-consuming and expensive. In this talk, we will discuss some ways our proprietary RL stack allows us to train models efficiently.

https://twitter.com/rhythmrg
https://twitter.com/lindensli

AIE is coming to London and SF! see dates and sign up to be notified of sponsorships, CFPs, and ticketsa: https://ai.engineer

## RL Environments at Scale – Will Brown, Prime Intellect

- Upload date: 2025-12-09
- Video: https://www.youtube.com/watch?v=_IzZWeuTx7I
- Transcript: raw/20251209__IzZWeuTx7I/_IzZWeuTx7I.en-orig.vtt
- Metadata: raw/20251209__IzZWeuTx7I/_IzZWeuTx7I.info.json

Scaling reinforcement learning environments for training advanced AI coding models.

https://twitter.com/willccbb

AIE is coming to London and SF! see dates and sign up to be notified of sponsorships, CFPs, and ticketsa: https://ai.engineer

## Don't Build Agents, Build Skills Instead – Barry Zhang & Mahesh Murag, Anthropic

- Upload date: 2025-12-08
- Video: https://www.youtube.com/watch?v=CEvIs9y1uog
- Transcript: raw/20251208_CEvIs9y1uog/CEvIs9y1uog.en-orig.vtt
- Metadata: raw/20251208_CEvIs9y1uog/CEvIs9y1uog.info.json

In the past year, we've seen rapid advancement of model intelligence and convergence on agent scaffolding. But there's still a gap: agents often lack the domain expertise and specialized knowledge needed for real-world work. We think Skills are the solution—a minimal form factor for packaging procedural knowledge that agents can dynamically load. It's a portable, composable approach to giving one agent capabilities across domains. In this talk, we'll share how we built Skills at Anthropic, the network effects we're observing, and where we believe this leads: agents writing their own Skills from experience. Our thesis: equipping agents for real-world work means building reusable expertise.

Barry: https://twitter.com/barry_zyj
Mahesh: https://twitter.com/MaheshMurag

## VoiceVision RAG - Integrating Visual Document Intelligence with Voice Response — Suman Debnath, AWS

- Upload date: 2025-12-06
- Video: https://www.youtube.com/watch?v=hwCmfThIiS4
- Transcript: raw/20251206_hwCmfThIiS4/hwCmfThIiS4.en-orig.vtt
- Metadata: raw/20251206_hwCmfThIiS4/hwCmfThIiS4.info.json

In this workshop we will explore the integration of Colpali, a cutting-edge Vision based Retrieval Model, with voice synthesis for next-generation RAG systems. We'll demonstrate how Colpali's ability to generate multi-vector embeddings directly from document images bypasses traditional OCR and complex preprocessing, while adding voice output creates a more intuitive and accessible user experience. Attendees will see how this combination handles documents with mixed textual and visual information, leading to more efficient and accurate information retrieval with natural voice responses.

## Government Agents: AI Agents Meet Tough Regulations — Mark Myshatyn, Los Alamos National Lab

- Upload date: 2025-12-06
- Video: https://www.youtube.com/watch?v=TnSGx36Ly0Q
- Transcript: raw/20251206_TnSGx36Ly0Q/TnSGx36Ly0Q.en-orig.vtt
- Metadata: raw/20251206_TnSGx36Ly0Q/TnSGx36Ly0Q.info.json

Lightning talk given at the 2025 AI Engineer World's Fair. https://www.linkedin.com/in/markmyshatyn/

## 2026: The Year The IDE Died — Steve Yegge & Gene Kim, Authors, Vibe Coding

- Upload date: 2025-12-06
- Video: https://www.youtube.com/watch?v=7Dtu2bilcFs
- Transcript: raw/20251206_7Dtu2bilcFs/7Dtu2bilcFs.en-orig.vtt
- Metadata: raw/20251206_7Dtu2bilcFs/7Dtu2bilcFs.info.json

As AI has grown more capable, software developers around the world have lagged behind the technology advances, and have consistently eschewed the most powerful tools. In this talk I explore why devs are staying 9-12 months behind the AI curve. I'll share a preview of what 2026's AI coding tools will be like, and paint a vision of where we go from here.

Speakers:
* Steve Yegge  |  Engineering Leader, Sourcegraph/Amp
https://x.com/Steve_Yegge
https://www.linkedin.com/in/steveyegge/

* Gene Kim  |  Author & Researcher, IT Revolution
https://x.com/RealGeneKim
https://www.linkedin.com/in/realgenekim/
http://www.realgenekim.me/

## Future-Proof Coding Agents – Bill Chen & Brian Fioca, OpenAI

- Upload date: 2025-12-05
- Video: https://www.youtube.com/watch?v=wVl6ZjELpBk
- Transcript: raw/20251205_wVl6ZjELpBk/wVl6ZjELpBk.en-orig.vtt
- Metadata: raw/20251205_wVl6ZjELpBk/wVl6ZjELpBk.info.json

Coding agents are becoming one of the most active areas in applied AI, yet many teams keep rebuilding fragile infrastructure every time models or providers change. We believe there is a better way. By anchoring on a stable abstraction layer like Codex, we can stop worrying about harness rewrites and focus on the parts of the stack that create lasting value. We treat models as interchangeable sub-agents, plug into shared primitives, and let upstream improvements flow through without breaking products. This lets teams move faster, stay resilient as the ecosystem evolves, and focus their energy on domain-specific workflows and user experience.

Speakers:
- https://twitter.com/bfioca
- https://twitter.com/realchillben

AIE is coming to London and SF! see https://ai.engineer for dates and sign up to be notified!
\**Timestamps:**

00:00 Introduction & The State of Coding Agents
02:06 Anatomy of a Coding Agent & The "Harness" Definition
03:44 Technical Challenges in Building Harnesses
06:03 Intelligence vs. Habit: Lessons in Prompt Engineering
08:24 Deep Dive: Codeex as a Harness/Agent
10:33 Computer Use & Terminal Capabilities
11:25 Patterns for Building with the Codeex SDK
14:32 Case Studies: GitHub & Cursor Integration
15:34 Future of Coding Agents & Conclusion

## Katelyn Lesse – Evolving Claude APIs for Agents, Anthropic

- Upload date: 2025-12-04
- Video: https://www.youtube.com/watch?v=aqW68Is_Kj4
- Transcript: raw/20251204_aqW68Is_Kj4/aqW68Is_Kj4.en-orig.vtt
- Metadata: raw/20251204_aqW68Is_Kj4/aqW68Is_Kj4.info.json

Developers are building more and more complex, long-running, agentic systems. Learn how the Anthropic team is evolving the Claude Developer Platform to enable developers to get the best outcomes from Claude.

## No Vibes Allowed: Solving Hard Problems in Complex Codebases – Dex Horthy, HumanLayer

- Upload date: 2025-12-02
- Video: https://www.youtube.com/watch?v=rmvDxxNubIg
- Transcript: raw/20251202_rmvDxxNubIg/rmvDxxNubIg.en-orig.vtt
- Metadata: raw/20251202_rmvDxxNubIg/rmvDxxNubIg.info.json

It seems pretty well-accepted that AI coding tools struggle with real production codebases. At AI Engineer 2025 in June, The Stanford study on AI's impact on developer productivity found:

A lot of the ""extra code"" shipped by AI tools ends up just reworking the slop that was shipped last week.

Coding agents are great for new projects or small changes, but in large established codebases, they can often make developers less productive.

The common response is somewhere between the pessimist ""this will never work"" and the more measured ""maybe someday when there are smarter models.""

After several months of tinkering, we've found that you can get really far with today's models if you embrace core context engineering principles.

This isn't another ""10x your productivity"" pitch. I tend to be pretty measured when it comes to interfacing with the ai hype machine. But we've stumbled into workflows that leave me with considerable optimism for what's possible. We've gotten claude code to handle 300k LOC Rust codebases, ship a week's worth of work in a day, and maintain code quality that passes expert review. We use a family of techniques I call ""frequent intentional compaction"" - deliberately structuring how you feed context to the AI throughout the development process.
 
In this talk, I'll share what we've learned since first sharing these techniques back in August, and some educated predictions on what's coming in the next 6-12 months for software engineers.

Speaker: twitter.com/dexhorthy

Timestamps:
00:00 intro: complex code
01:40 context engineering
02:53 advanced context
04:38 context obsession
05:55 dumb zone concept
07:26 context management
09:37 complex problem solved
10:45 semantic diffusion
12:14 onboarding agents ‍
13:57 internal docs lies
15:03 mental alignment key
16:12 code snippet plans
17:38 don't outsource think
18:45 rpi: smart zone
19:46 cultural change hard ‍‍

Hey - I'm Dex, and I'm hacking on getting AI coding agents to solve hard problems in complex codebases at HumanLayer. Before this I was working on APIs for agent orchestration and Human-in-the-Loop, and wrote the April 2025 essay "12 factor agents" that first coined the term Context Engineering. I've been coding since high school, when I built tools for NASA researchers to navigate the south pole of the moon. Enjoyer of tacos and burpees (not necessarily in that order).

## Building Cursor Composer – Lee Robinson, Cursor

- Upload date: 2025-12-02
- Video: https://www.youtube.com/watch?v=fL1iJHtl51Q
- Transcript: raw/20251202_fL1iJHtl51Q/fL1iJHtl51Q.en-orig.vtt
- Metadata: raw/20251202_fL1iJHtl51Q/fL1iJHtl51Q.info.json

Learn about the infrastructure, training, and evaluations used to build Cursor Composer, our first coding model. (https://cursor.com/blog/2-0)

Speaker: https://x.com/leerob

AIE is coming to London and SF! see https://ai.engineer for dates and sign up to be notified!

**Timestamps**

00:00 Introduction to Cursor Composer
01:10 The "Fast vs. Smart" Trade-off
03:17 System Architecture & Tooling
04:33 Scaling Challenges: Consistency & Burstiness
05:50 Infrastructure Solutions & Custom Kernels
08:12 Co-designing Cloud Agents & Training Infra
09:39 The Power of Semantic Search
11:00 Results: Parallelism & Agent Behavior
12:13 The "Airplane Wi-Fi" Analogy
13:36 Key Reflections & Conclusion

## Defying Gravity - Kevin Hou, Google DeepMind

- Upload date: 2025-12-02
- Video: https://www.youtube.com/watch?v=HN-F-OQe6j0
- Transcript: raw/20251202_HN-F-OQe6j0/HN-F-OQe6j0.en-orig.vtt
- Metadata: raw/20251202_HN-F-OQe6j0/HN-F-OQe6j0.info.json

Why we built Google Antigravity, and discussing the future of agentic IDEs with Gemini 3.

Speaker: https://x.com/kevinhou22

AIE is coming to London and SF! see dates and sign up to be notified of sponsorships, CFPs, and tickets: https://ai.engineer

**Timestamps:**

00:00 Intro & Anti-gravity Launch
01:26 Anti-gravity Product Overview (Three Surfaces)
02:16 Agent Manager & Editor Integration
03:13 Agent-Controlled Browser & Context Retrieval
05:51 Philosophy: Model Capabilities Driving Product Paradigms
07:03 Four Categories of Improvements (Intelligence, Tools, Long-running, Multimodal)
08:31 Computer Use & Visual Verification
11:18 Image Generation & Design Iteration
12:26 The "Artifacts" Interaction Pattern
16:51 Artifacts for Memory, Notifications, & Feedback
20:34 The Research-Product Flywheel
23:35 Closing Remarks

## Music from AIE Code Summit - Instrumentals

- Upload date: 2025-11-27
- Video: https://www.youtube.com/watch?v=xAfp-znTRx8
- Transcript: raw/20251127_xAfp-znTRx8/xAfp-znTRx8.en-orig.vtt
- Metadata: raw/20251127_xAfp-znTRx8/xAfp-znTRx8.info.json

By popular demand, we are releasing our music from the livestream + venue stage -- the instrumental tracks. Comment below if you want to see the vocal tracks released!

## The Unbearable Lightness of Agent Optimization — Alberto Romero, Jointly

- Upload date: 2025-11-24
- Video: https://www.youtube.com/watch?v=zfvEMNmVlNY
- Transcript: raw/20251124_zfvEMNmVlNY/zfvEMNmVlNY.en-orig.vtt
- Metadata: raw/20251124_zfvEMNmVlNY/zfvEMNmVlNY.info.json

This talk introduces Meta-ACE, a learned meta-optimization framework that dynamically orchestrates multiple strategies (context evolution, adaptive compute, hierarchical verification, structured memory, and selective test-time parameter adaptation) to maximize task performance under real-world constraints. Rather than relying on uniform prompt refinement, Meta-ACE profiles each task (complexity, verifiability, feedback quality) and selects an optimal strategy bundle via a lightweight meta-controller.

Alberto is a seasoned AI and ML leader with over 20 years of experience at the intersection of AI and data. A hands-on engineer, Alberto has designed and built low-latency, mission-critical ML systems, and has specialized in systematic optimization of AI pipelines and agents using custom built evaluation techniques. He is an exited co-founder having sold his previous startup, Humn.ai, to Aon in 2023, which delivered real-time, ML-powered risk prediction for mobility. Alberto is the Co-founder and CTO at Jointly, specializing in self-optimizing AI agents for regulated industries.

He holds an MSc in AI and Machine Learning and speaks at global AI conferences, including ODSC and AIAI.

---
Socials:
- LinkedIn: https://www.linkedin.com/in/albertoromero-uk/
- GitHub: https://github.com/a-romero
- Company: Jointly (https://getjointly.ai)

## Backlog.md: Terminal Kanban Board for Managing Tasks with AI Agents — Alex Gavrilescu, Funstage

- Upload date: 2025-11-24
- Video: https://www.youtube.com/watch?v=zMXKhhwiCIc
- Transcript: raw/20251124_zMXKhhwiCIc/zMXKhhwiCIc.en-orig.vtt
- Metadata: raw/20251124_zMXKhhwiCIc/zMXKhhwiCIc.info.json

Never leave your terminal to create and manage tasks for your AI agents. Backlog.md stores all your tasks as Markdown files in your Git repo. By exposing the main workflows and commands as MCP tools, your AI agents will know how to take tasks from "To Do" to "Done," and you will no longer run out of context window or miss important requirements in any of your features.

Alex Gavrilescu leads backend & web engineering at Funstage GmbH in Vienna, keeping millions of free‑to‑play gamers happily tapping. He still ships code, tinkers with Raspberry Pi Kubernetes clusters for fun, and is passionate about weaving project‑management smarts with practical AI. Most recently he created Backlog.md, a micro‑tool that turns side‑project chaos into shippable tasks.

---
Socials:
- LinkedIn: https://www.linkedin.com/in/alexandrugavrilescu
- X (Twitter): https://x.com/H3xx3n
- GitHub: https://github.com/MrLesk
- Website: https://mrlesk.com/
- Company: Funstage GmbH (https://funstage.com/)

## Agents are Robots Too: What Self-Driving Taught Me About Building Agents — Jesse Hu, Abundant

- Upload date: 2025-11-24
- Video: https://www.youtube.com/watch?v=qqXdLf3wy1E
- Transcript: raw/20251124_qqXdLf3wy1E/qqXdLf3wy1E.en-orig.vtt
- Metadata: raw/20251124_qqXdLf3wy1E/qqXdLf3wy1E.info.json

In this talk, I break down the surprising parallels between robotics and agents: embodiment, statefulness, simulation, and more. The main lesson from self-driving: everyone thought perception was hard and planning was easy. It took 8-10 years to learn we had it backwards. We're seeing the same pattern with agents today. Predictive models aren't action models. Perfect reasoning doesn't guarantee good execution.

And just like in robotics, the company with the best infrastructure wins—not just the one with the best model. Whether you're building agents, training models, or just trying to understand why production agents are so hard, this talk covers the concepts from robotics (DAgger, MDPs, simulation, offline RL) that directly apply to making agents work at scale.

Jesse has spent the last 10 years as an ML engineer, starting from research in computer vision and NLP, to working on deep learning and two-tower embedding recommender systems at YouTube, to transformer-based planning models for self-driving at Waymo. He is currently working on bringing large-scale RL and simulation techniques to coding agents at Abundant.

---
Socials:
- LinkedIn: https://www.linkedin.com/in/jessehu
- GitHub: http://github.com/huyouare
- Company: Abundant (https://abundant.ai)

## Vision: Zero Bugs — Johann Schleier-Smith, Temporal

- Upload date: 2025-11-24
- Video: https://www.youtube.com/watch?v=qLqttdO33UM
- Transcript: raw/20251124_qLqttdO33UM/qLqttdO33UM.en-orig.vtt
- Metadata: raw/20251124_qLqttdO33UM/qLqttdO33UM.info.json

Software with zero bugs sounds absurd, or even impossible, in anything but simple situations, but it has been built. For example, NASA's Space Shuttle software achieved near-perfection (1 error per 420,000 lines) using rigorous engineering practices. This feat was achieved decades ago, yet cost prevented the techniques used from becoming mainstream.

This talk traces seventy years of innovation in software quality and programmer productivity, ranging from structured programming to formal verification. While many of these techniques have been too costly to implement on a large scale, AI changes that. What is more, agentic coding needs them to compensate for its limitations.

We are on the verge of a world where aerospace-level reliability becomes the practical in a broad range of applications.

Johann Schleier-Smith is Technical Lead for AI at Temporal Technologies, the leading provider of durable execution. He previously founded Crystal DBA, which developed agents to manage cloud infrastructure and was acquired by Temporal. He also co-founded if(we), which built a collection of social networks with over 300 million members and was acquired by The Meet Group (NASDAQ:MEET). Johann serves on the board of Sama, a leading provider of training data for computer vision applications. He holds a Ph.D. in Computer Science from UC Berkeley and an A.B. in Physics and Mathematics from Harvard University.

---
Socials:
- LinkedIn: https://www.linkedin.com/in/jssmith/
- X (Twitter): https://x.com/jssmith
- GitHub: https://github.com/jssmith
- Website: https://johann.schleier-smith.com/
- Company: Temporal Technologies (https://temporal.io/)

## Compilers in the Age of LLMs — Yusuf Olokoba, Muna

- Upload date: 2025-11-24
- Video: https://www.youtube.com/watch?v=q2nHsJVy4FE
- Transcript: raw/20251124_q2nHsJVy4FE/q2nHsJVy4FE.en-orig.vtt
- Metadata: raw/20251124_q2nHsJVy4FE/q2nHsJVy4FE.info.json

Python is where ideas start—but it isn't where portable, low-latency software ends. In this talk, I'll show how we use LLMs inside a constrained, verifiable compiler pipeline to turn plain Python functions into self-contained native binaries that run anywhere (cloud, desktop, mobile & web); and how our customers use this technology to run open-source AI models locally and in the cloud with the familiar OpenAI client experience.

Yusuf Olokoba is the founder of Muna, specializing in code generation for AI inference workloads. He previously co-founded a real estate technology startup, backed by First Round Capital and Bessemer, which was later acquired. He holds patents in computer vision and augmented reality, powering augmented reality experiences used by millions of users. Yusuf holds a B.A. in computer science from Dartmouth College and is an alumnus of South Park Commons.

---
Socials:
- LinkedIn: https://www.linkedin.com/in/olokobayusuf/
- X (Twitter): https://x.com/olokobayusuf
- GitHub: https://github.com/olokobayusuf
- Company: Muna (https://muna.ai)

## Developing Taste in Coding Agents: Applied Meta Neuro-Symbolic RL — Ahmad Awais, CommandCode

- Upload date: 2025-11-24
- Video: https://www.youtube.com/watch?v=kWOQS3XPZ10
- Transcript: raw/20251124_kWOQS3XPZ10/kWOQS3XPZ10.en-orig.vtt
- Metadata: raw/20251124_kWOQS3XPZ10/kWOQS3XPZ10.info.json

Your coding agent writes code like an LLM bot. CommandCode writes code like me.

Every developer has a coding agent now. What if your coding agent actually had taste? What if it understood not just what you're building, but how you like to build it? Your weird naming conventions. Your obsession with early returns. That thing you do where you always extract utilities before they get messy. Your coding taste.

I've been building coding agents since Greg Brockman gave me GPT-3 access in 2020. Started as a CLI tool I used every day. Five years later, we've deployed over 350K agents through Langbase, and I've learned something crucial: the best agents don't just write code—they develop taste.

In this talk, I'll share what we've learned about building agents that actually feel like they know you. We'll dive into the architecture patterns that make this possible: contextual memory systems, preference learning loops, and what I call "engineering intuition"—going way beyond the typical "agents.md" approach.

It's about building agents that evolve with you, remember your decisions, and start making choices that feel like your own. By the end, you'll understand how to build coding agents that can develop taste. It's battle-tested insights from one of the largest deployment of AI agents in production today.

Ahmad Awais is an award-winning open-source engineering leader, founder & CEO of Langbase.com (AI Cloud powering 350K+ AI agents), Creator of CommandCode.ai. NASA Mars Ingenuity Helicopter mission code-contributor. Angel investor. Ex-VP DX, Google Developers Advisory Board founding member and Board Member Linux Foundation & OpenAPI Initiative. Ahmad has authored various open-source software tools used by millions of developers worldwide, like his Shades of Purple code theme (4M Dev Users), corona-cli (10+ Billion Requests), and now Langbase (1.2Billion/mo agent runs). He’s a Google Devs Expert and 5x recipient of the 8th GitHub Stars Gold award.

---
Socials:
- LinkedIn: https://www.linkedin.com/in/MrAhmadAwais/
- X (Twitter): https://x.com/_AhmadAwais
- GitHub: https://github.com/AhmadAwais
- Website: https://AhmadAwais.com/about
- Company: CommandCode.ai | Langbase (https://commandcode.ai)

## From Stateless Nightmares to Durable Agents — Samuel Colvin, Pydantic

- Upload date: 2025-11-24
- Video: https://www.youtube.com/watch?v=flf_IKnFYnE
- Transcript: raw/20251124_flf_IKnFYnE/flf_IKnFYnE.en-orig.vtt
- Metadata: raw/20251124_flf_IKnFYnE/flf_IKnFYnE.info.json

Building production AI agents reveals a harsh truth: stateless architectures that work for simple demos become impossibly painful at scale. When long-running workflows fail, you lose all compute, progress, and user trust.
This is why companies like OpenAI use Temporal for products like Deep Research—to build durable agents that recover from failures instead of forcing users to start over.

In this talk, you'll learn how to:
- Build resilient AI agents that survive crashes and resume from checkpoints
- Implement durable execution with PydanticAI and Temporal
- Gain production-grade observability with Pydantic Logfire and Evals
- Compose multi-agent systems that handle failures gracefully
- Stop burning money on failed agent runs that restart from scratch

We'll walk through real code examples, including a Deep Research implementation that demonstrates how proper architecture turns fragile prototypes into production-ready systems.

Links:
- Demo code on GitHub: https://github.com/pydantic/pydantic-stack-demo/tree/main/durable-exec
- Pydantic AI Documentation: https://ai.pydantic.dev/
- Temporal Integration Guide: https://ai.pydantic.dev/durable_execution/temporal/
- Pydantic Logfire Docs: https://logfire.pydantic.dev/docs/

Samuel Colvin is a Python and Rust expert. His work has redefined data validation and observability for developers. His Pydantic library powers 350M+ downloads every month, serving as a core dependency for OpenAI SDK, Anthropic SDK, LangChain, LlamaIndex, and countless other GenAI projects.

---
Socials:
- LinkedIn: https://www.linkedin.com/company/pydantic/
- X (Twitter): https://x.com/pydantic
- GitHub: https://github.com/pydantic
- Website: NA
- Company: Pydantic (https://pydantic.dev)

## Enterprise Deep Research: The Next Killer App for Enterprise AI — Ofer Mendelevitch, Vectara

- Upload date: 2025-11-24
- Video: https://www.youtube.com/watch?v=fh9LgKXBGnQ
- Transcript: raw/20251124_fh9LgKXBGnQ/fh9LgKXBGnQ.en-orig.vtt
- Metadata: raw/20251124_fh9LgKXBGnQ/fh9LgKXBGnQ.info.json

Conversational AI has already proven itself as the first high-ROI enterprise AI application. But the real frontier lies beyond chat with high-value, document-centric workflows that still consume countless human hours. Enterprise Deep Research brings the power of web-scale research workflows into the private domain of your company’s data. By applying autonomous, multi-step reasoning to internal knowledge bases, enterprises can unlock transformative use cases: from drafting investment memos in financial services to automating RFP responses and due diligence. In this talk, we’ll learn what Enterprise Deep Research is, how it works, and see some example use-cases.

Ofer Mendelevitch leads developer relations at Vectara. He has extensive hands-on experience in machine learning, data science and big data systems across multiple industries, and has focused on developing products using large language models since 2019. Prior to Vectara he built and led data science teams at Syntegra, Helix, Lendup, Hortonworks and Yahoo! Ofer holds a B.Sc. in computer science from Technion and M.Sc. in EE from Tel Aviv university, and is the author of "Practical data science with Hadoop" (Addison Wesley), and of the upcoming "Hands-on RAG for production" (O'Reilly)

---
Socials:
- LinkedIn: https://www.linkedin.com/in/ofermend/
- X (Twitter): https://x.com/ofermend
- GitHub: https://github.com/ofermend
- Company: Vectara (https://vectara.com)

## What Data from 20m Pull Requests Reveal About AI Transformation — Nick Arcolano, Jellyfish

- Upload date: 2025-11-24
- Video: https://www.youtube.com/watch?v=WqZq8L-v9pA
- Transcript: raw/20251124_WqZq8L-v9pA/WqZq8L-v9pA.en-orig.vtt
- Metadata: raw/20251124_WqZq8L-v9pA/WqZq8L-v9pA.info.json

Engineering teams are spending millions on AI coding tools, but most have no idea what's actually working. Without hard data, you're flying blind – unable to tell which teams are actually using AI effectively. But what if you had access to workflow data from 200,000 engineers and 20 million pull requests across a thousand companies?

In this talk, we'll share insights from usage data spanning the entire AI engineering ecosystem. We've observed significant productivity gains at scale, including a 2x increase in PR throughput and 24% faster cycle times on average.

You'll learn what "good" adoption looks like (hint: autonomous agents aren't there yet), what productivity gains are possible, and what side effects to expect. More importantly, we'll explore why some teams don't see these gains. We'll show how your code architecture" is a critical, often overlooked factor.

---
Socials:
- LinkedIn: https://www.linkedin.com/in/arcolano/
- X (Twitter): https://x.com/arcolano
- GitHub: https://github.com/arcolano
- Company: Jellyfish (https://jellyfish.co)

## AI Copilots for Tech Architecture: The Highest-ROI Use Case You’re Not Building — Boris B., Catio

- Upload date: 2025-11-24
- Video: https://www.youtube.com/watch?v=QRWdapxMdSY
- Transcript: raw/20251124_QRWdapxMdSY/QRWdapxMdSY.en-orig.vtt
- Metadata: raw/20251124_QRWdapxMdSY/QRWdapxMdSY.info.json

AI copilots have already changed the game in software development. But the most strategic, highest-leverage use case is still overlooked: tech architecture decision-making. Architecture decisions drive hundreds of millions in technology spend, whether tech fuels business objectives—or slows them down, and ultimately decide whether companies stay modern-by-design or get left behind in insurmountable technical debt. Yet most organizations still manage these choices with spreadsheets, tribal knowledge, and gut instinct. In this talk, we'll explore why architecture copilots represent the next frontier beyond coding assistants—and why getting this right is where ROI is truly won or lost.

Drawing from closed-door CTO discussions and our work with enterprises and growth-stage tech companies, we'll examine three critical challenges keeping leaders up at night: achieving visibility across their entire tech estate so they're not flying blind; getting expert advice and recommendations on how to prioritize tech roadmaps based on highest impact to business objectives; and enabling autonomous developer guidance so that developers are empowered with tailor-fit expertise as they pursue their workflow while also keeps them adhering to leadership strategy and governance.

To solve this, we’ll share what it takes to build a true architecture copilot (based on work with Catio customers across $1B+ enterprises and growth-stage companies): understanding messy systems, implicit knowledge, and constantly shifting dependencies for holistic live visibility; curating the right context around company goals and architecture excellence to inform AI recommendations that truly optimize the architecture; and defining the workflow fabric that powers teams with tailor-fit designs and expert advice while adhering to organizational standards and strategy for true autonomous decision-making.

We’ll close with a look at what this unlocks: a centralized Hub for Architecture and Tech Decision-making that transforms how companies strategically plan, build, and evolve their tech estate—not simply execute more lines of code. You'll walk away with a new lens on AI strategy: one that reframes copilots not just as coding productivity enhancers, but as strategic levers for competitive advantage, staying best-in-class-by-design, and high-ROI tech outcomes.

Boris is the Co-Founder and CEO of Catio, a platform for cloud native architecture evaluation, planning, and evolution, with the help of AI. Boris is a serial entrepreneur and over the prior five years founded and lead Siden through growth to 60 people and to becoming a leader in distributed edge compute. Siden uses compute / caching placed in homes, AI to predict home content consumption, and proactive content distribution to refresh caches 24x7 using underutilized wireless network capacity. Siden uses a SaaS model to partner with wireless operators to materially expand their network capacity for Home Internet (by 2-5x), enabling them to win the Home Internet market globally (forecasted to reach 1B homes by 2032 by Qualcomm). Over his career, Boris grew 5 high caliber start-ups in total as a product-minded leader, and also funded companies from Series A to growth stages as a venture capital and private equity investor. Boris graduated the Management and Technology Program at the University of Pennsylvania with degrees from the Wharton School and School of Engineering and is a listed inventor on 15 patents.

---
Socials:
- LinkedIn: https://www.linkedin.com/in/borisbogatin/
- X (Twitter): https://x.com/borisbogatin
- Company: Catio (https://catio.tech)

## Infra that fixes itself, thanks to coding agents — Mahmoud Abdelwahab, Railway

- Upload date: 2025-11-24
- Video: https://www.youtube.com/watch?v=Q5IVm_CxN2w
- Transcript: raw/20251124_Q5IVm_CxN2w/Q5IVm_CxN2w.en-orig.vtt
- Metadata: raw/20251124_Q5IVm_CxN2w/Q5IVm_CxN2w.info.json

This talk shows how we built Railway Autofix, a plug-in template you can drop into any Railway project to monitor your infrastructure, and open PRs with fixes when issues are detected. We use OpenCode as our coding agent, as well as Inngest for durable execution

The final code will be live at https://github.com/m-abdelwahab/railway-autofix

Mahmoud Abdelwahab is a Software Engineer who works at the intersection of Product, Marketing, Education and Community. He loves building over-engineered demos and playing around with the latest technologies.

---
Socials:
- LinkedIn: https://linkedin.com/in/thisismahmoud
- X (Twitter): https://x.com/thisismahmoud
- GitHub: https://github.com/m-abdelwahab
- Company: Railway (https://railway.com)

## Context Platform Engineering to Reduce Token Anxiety — Val Bercovici, WEKA

- Upload date: 2025-11-24
- Video: https://www.youtube.com/watch?v=NTBX-wxUhHs
- Transcript: raw/20251124_NTBX-wxUhHs/NTBX-wxUhHs.en-orig.vtt
- Metadata: raw/20251124_NTBX-wxUhHs/NTBX-wxUhHs.info.json

Context Platform Engineering is the set of skills and tools to design, size, and configure systems optimized for Agent Swarm Context, at any scale.

“KV-cache hit rate is the single most important metric for a production-stage AI agent“ according to Manus AI. Context platform engineering simplifies the maximization of KV Cache hit rates.

This talk covers WEKA’s new open source context platform engineering toolkit, which helps translate Service Level Agreement (SLA) requirements of AI Agents, into Agent+LLM inference platform Service Level Objectives (SLOs) which meet required SLAs.

We present research results from WEKA Labs which provide new observability into both unit, and aggregate KV Cache hit rates, consumed by agent swarms of various leading AI coding agents.

This talk concludes with benchmark results for sizing agent swarm context for arbitrary working sets. Including context window sizes, latency, concurrency, and throughput SLOs per agent unit (swarm or sub-task) across modern GPU memory hierarchies, supporting KV Cache offloading plug-ins like vLLM/LMCache, SGLang HiCache, and NVIDIA Dynamo KVBM/NIXL.

Callan Fox is the product leader for Context Platforms at WEKA, following a series of technical expertise and leadership roles at Dell/EMC, CGI and HPE.
Val Bercovici is the Chief AI Officer at WEKA. Previously he was CTO of NetApp/SolidFire, and founding governing board member of the Kubernetes CNCF in the Linux Foundation.

---
Resources:
- https://www.linkedin.com/pulse/visual-guide-how-ai-agents-use-inference-inside-llm-callan-fox-q9brc
- https://medium.com/@callan.j.fox/evaluating-management-of-kv-cache-within-an-inference-system-2d7c3d266c3a
- https://www.linkedin.com/pulse/importance-context-platform-engineering-callan-fox-i81wc/

---
Socials:
- LinkedIn: https://www.linkedin.com/in/valentinbercovici
- X (Twitter): https://x.com/AccBalanced
- GitHub: https://github.com/weka/LMCache
- Website: https://www.weka.io/product/augmented-memory-grid/
- Company: WEKA (https://weka.io)

## Context Engineering: Connecting the Dots with Graphs — Stephen Chin, Neo4j

- Upload date: 2025-11-24
- Video: https://www.youtube.com/watch?v=LLuKshphGOE
- Transcript: raw/20251124_LLuKshphGOE/LLuKshphGOE.en-orig.vtt
- Metadata: raw/20251124_LLuKshphGOE/LLuKshphGOE.info.json

AI systems need more than intelligence; they need context. Without it, even the most advanced models can misinterpret information, lose track of details, or arrive at conclusions that don’t hold up. Context engineering is emerging as a discipline that shapes how AI perceives, recalls, and reasons about information.

This talk will explore how context provides the foundation for reasoning, problem solving, and explainability in AI. We will look at techniques such as connected memory, contextual retrieval, and graph-based knowledge representation that give large language models a more reliable way to connect information and draw logical conclusions.

Attendees will come away with a practical understanding of how to design effective context pipelines that align AI with real-world knowledge and user intent, and why context engineering is becoming a central part of building trustworthy and impactful AI systems.

Stephen Chin is VP of Developer Relations at Neo4j, conference chair of the LF AI & Data Foundation, and author of numerous titles including the upcoming GraphRAG: The Definitive Guide for O'Reilly. He has given keynotes and main stage talks at numerous conferences around the world including AI Engineer Summit, AI DevSummit, Devoxx, DevNexus, JNation, JavaOne, Shift, Joker, swampUP, and GIDS. Stephen is an avid motorcyclist who has done evangelism tours in Europe, Japan, and Brazil, interviewing developers in their natural habitat. When he is not traveling, he enjoys teaching kids how to do AI, embedded, and robot programming together with his daughters.

---
Socials:
- LinkedIn: https://linkedin.com/in/steveonjava
- X (Twitter): https://x.com/steveonjava
- GitHub: https://github.com/steveonjava
- Company: Neo4j (https://neo4j.com)

## The Cure for the Vibe Coding Hangover — Corey J. Gallon, Rexmore

- Upload date: 2025-11-24
- Video: https://www.youtube.com/watch?v=JsKTQbT58BY
- Transcript: raw/20251124_JsKTQbT58BY/JsKTQbT58BY.en-orig.vtt
- Metadata: raw/20251124_JsKTQbT58BY/JsKTQbT58BY.info.json

Download the slides, soundtrack and other resources from this talk at: https://vibecodinghangover.com

Inspiration strikes! You fire up your favorite AI coding agent and tell it "Build me an app that..." The agent grinds away, furiously, and spits back a torrent of code and it works! You’re a masterful rebel in the AI revolution!

But, then, you want to change something. You want to add a feature. You want to evolve it to production software; or, perhaps you come back to it a week later. You realize you don't understand it, can't maintain it, and have to throw most or all of it all away.

"Vibe Coding" is the low-spec, zero-planning approach to AI accelerated development that feels productive but results in brittle, unmaintainable demoware. The hangover is the resulting despair when you try to build maintainable, understandable software this way. The cure is building software with AI coding agents by applying this framework.

You’ll love this talk if:

- You value programming as a daily learning experience.
- You want to understand and own this software as you do all of the other software that you write.
- You want to be the boss of the coding agents, not their confused intern.
- Working with AI coding agents makes you feel like a prompt jockey, no longer an AI engineer.
- You're sick of throwing away code, burning time and tokens.
- You want to use coding agents to build production applications that do real work.

We'll walk through a practical framework - comprising a set of Principles, a Process, and Tools - that enables AI engineers to build, own, and maintain complex, real-world software applications using AI coding agents. This is not a conceptual framework, it is applied. It has been distilled and simplified from years of engineering work in the trenches of building software with AI coding agents. This framework has been taught and implemented across many teams, and has transformed the productivity of AI engineers in companies from solo shops to Fortune 500. We'll focus on the first crucial phase of software development: "Make it Work,” with clear ties to apply the framework to the remaining phases of “Make it Right” and “Make it Fast”.

00:00 The Vibe Coding Hangover
01:24 Introduction
03:31 The Framework - Overview
04:52 Principles
16:46 Process - Overview
17:28 Process - Planning
38:26 Process - Implementation
48:29 Tools
56:10 The Morning After

Corey J. Gallon is Head of an AI-native holding company and a battle-hardened AI engineer with a focus on building real, scaled software with AI coding agents. He is an AI coding agents OG, building coding agents since 2022 and one of the most significant contributors to GPT-Engineer (evolved into the startup Lovable). He was formerly Chief Innovation Officer, designer and leader of development of a large consulting firm's enterprise-scale AI coding agents platform. Corey is founding faculty of a university graduate AI & ML program, an artisan of specialty coffee, and a pickleball fanatic.

---
Socials:
- LinkedIn: https://www.linkedin.com/in/coreygallon
- X (Twitter): https://x.com/coreygallon
- GitHub: https://github.com/captivus
- Website: https://gallon.me
- Company: Rexmore (https://rexmore.ai)

## Hacking Subagents Into Codex CLI — Brian John, Betterup

- Upload date: 2025-11-24
- Video: https://www.youtube.com/watch?v=5eJqXtevlXg
- Transcript: raw/20251124_5eJqXtevlXg/5eJqXtevlXg.en-orig.vtt
- Metadata: raw/20251124_5eJqXtevlXg/5eJqXtevlXg.info.json

Subagents are amazing tools for managing context, among other things. But Codex CLI doesn't have them. Let's change that!

Brian John is a Principal Full Stack Engineer with over a decade of experience in technology. He is currently working on using AI to help his R&D team members ship faster and with higher quality.

---
Socials:
- LinkedIn: https://linkedin.com/in/brianjohn
- X (Twitter): https://x.com/brianpjohn
- GitHub: https://github.com/f1sherman
- Website: https://blog.brianjohn.com
- Company: Betterup (https://betterup.com)

## AI changes *Nothing* — Dax Raad, OpenCode

- Upload date: 2025-11-23
- Video: https://www.youtube.com/watch?v=o3gmwzo-Mik
- Transcript: raw/20251123_o3gmwzo-Mik/o3gmwzo-Mik.en-orig.vtt
- Metadata: raw/20251123_o3gmwzo-Mik/o3gmwzo-Mik.info.json

Everyone says AI changes everything. Dax Raad argues that when it comes to building a winning product, AI changes nothing.

In this contrarian talk, Dax breaks down why the fundamental challenges of product success: marketing, onboarding, and retention remain stubbornly human problems that AI cannot solve. He argues that while AI can generate content, it cannot generate cool. While it can write code, it cannot design the deep primitives required for long term retention.

Key Takeaways:
- Marketing is about Cool: You need to create things that people feel compelled to share. AI is too corny to help you here.
- The "Aha" Moment: You must ruthlessly eliminate friction to get users to the singular moment they understand your product. This requires deep, opinionated taste, not algorithmic optimization.
- Primitives over Features: To retain power users, you must build deep primitives first and simple experiences second. AI cannot hallucinate the right mental model for your problem space.

Winning still requires hard work, deep taste, and human ingenuity. And that's a good thing.

Dax Raad is a core contributor to SST, the framework that makes it easy to build serverless applications. He is a well-known voice in the developer community, advocating for better developer experiences and honest product thinking.

---
Socials:
- X (Twitter): https://x.com/thdxr
- GitHub: https://github.com/thdxr
- Website: https://thdxr.com/
- Company: OpenCode (https://opencode.ai)

Timestamps from the comments (thanks!)
- 0:00 — Introduction to Open Code, a fully open-source coding agent
- 0:43 — Why AI isn't going to make you a winner: the unchanging fundamentals of product success
- 1:39 — The product funnel framework: three critical moments that determine success
- 2:18 — Marketing: creating ideas people want to share organically
- 6:38 — The aha moment: ruthlessly eliminating friction to get users to product clarity
- 10:46 — Retention: balancing simplicity for new users with advanced features for power users
- 14:46 — Closing: why execution difficulty remains constant despite AI capabilities

## Z.ai GLM 4.6: What We Learned From 100 Million Open Source Downloads — Yuxuan Zhang, Z.ai

- Upload date: 2025-11-22
- Video: https://www.youtube.com/watch?v=m6MF1OR_9kM
- Transcript: raw/20251122_m6MF1OR_9kM/m6MF1OR_9kM.en-orig.vtt
- Metadata: raw/20251122_m6MF1OR_9kM/m6MF1OR_9kM.info.json

GLM 4.6 is the only open-source model currently tied for #1 on the LMSYS Chatbot Arena, standing shoulder-to-shoulder with GPT-4o and Claude 3.5 Sonnet. In this talk, Zhang Yuxuan from zAI breaks down the technical roadmap that led to over 100 million downloads across the GLM family.

Zhang deep dives into the specific training recipes behind GLM 4.6, including their move to single-stage Reinforcement Learning (RL), the "SLIME" RL framework for handling complex agent trajectories, and how they structured 15 trillion tokens of pre-training data. If you are building AI Agents or training LLMs, this breakdown offers a rare look inside the architecture of a frontier-class open-source model.

In this video, we cover:

The Data Recipe: How zAI filters 15T tokens, moves to repo-level code contexts, and integrates agentic reasoning data.

SLIME Framework: A look at the hybrid synchronous/asynchronous architecture used to train agents without bottlenecking GPU clusters.

RL Lessons: Why zAI abandoned multi-stage RL in favor of single-stage training to preserve long-context capabilities.

GLM 4.5V: How native resolution processing improves UI navigation and video understanding.

Timestamps:
0:00 - Introduction & The GLM Ecosystem
0:55 - 100 Million Downloads & Open Source Roadmap
03:22 - Tying GPT-4o on LMSYS Arena
05:04 - The Training Pipeline: From Pre-training to Long Context
07:54 - Introducing SLIME: Efficient RL for Agents
11:08 - The "Two-Stage" Curriculum Strategy
11:57 - Why Single-Stage RL beats Multi-Stage RL
12:55 - Token-Weighted Loss for Coding
14:13 - GLM 4.5V: Multimodal & Video Understanding
16:07 - Deployment: vLLM, SGLang, and Hugging Face
18:06 - Coding Assistants & Future Plans

Zhang Yuxuan has recently started a PhD at the University of Liverpool and is currently working at Z.ai. zR (Zhang) is passionate about open-source initiatives and strives for deeper exploration in this realm. Their primary activities include the following: Engaged in research on models such as GLM-4.5 (https://arxiv.org/abs/2508.06471), GLM-4.5V (https://arxiv.org/abs/2507.01006), CogVideoX (https://arxiv.org/abs/2408.06072), CogAgent (https://arxiv.org/abs/2312.08914); researching the capabilities of model Agents and the integration with Agent frameworks such as langchain-chatchat (https://github.com/chatchat-space/Langchain-Chatchat), chatpdf (https://github.com/CosmosShadow/gptpdf); participated in several national competitions, such as RoboMaster and National Students' SmartCar Competition, and achieved some results, including national awards. These competitions have been truly fascinating. Enjoys hackathon competitions and welcomes teaming up for these events.

---
Socials:
- LinkedIn: https://www.linkedin.com/in/yuxuan-zhang-86a124282/
- X (Twitter): https://x.com/zRdianjiao
- GitHub: https://github.com/zRzRzRzRzRzRzR
- Website: https://huggingface.co/ZHANGYUXUAN-zR
- Company: Z.ai (https://z.ai)

## Rishabh Garg, Tesla Optimus — Challenges in High Performance Robotics Systems

- Upload date: 2025-08-25
- Video: https://www.youtube.com/watch?v=bCGbuyv8PMk
- Transcript: raw/20250825_bCGbuyv8PMk/bCGbuyv8PMk.en-orig.vtt
- Metadata: raw/20250825_bCGbuyv8PMk/bCGbuyv8PMk.info.json

A robot's behavior is influenced by the control policy, the software configuration, and electrical characteristics of the communication protocol.

When unexpected behaviors arise, it is not straightforward to root cause them to the RL policy, electrical characteristics, mechanical characteristics. This talk walks through some of these issues and explains what might cause the observed behavior.

We will talk about concrete issues that audience will be able to take away from and develop their understanding of physical systems. It will build intuition for what kind of issues to expect when communication data rates increase manifold.

Timestamps
00:00 Introduction to high-performance robotics challenges
00:15 The problem of unexplained robot behavior
00:54 Root cause analysis: policy vs. software
01:17 Designing a toy robotics system for analysis
01:24 System architecture: sensors, CPU, GPU, actuators, CAN bus
01:57 The initial, simple code loop
02:14 Expectation vs. reality: unexpected loop execution gaps
02:42 The impact of CAN bus data rate on loop execution
03:13 Potential solutions: accepting delay vs. multithreading
04:00 A new, pipelined design for reduced cycle time
04:32 New problems: "stuttering" and abnormal motor behavior
04:49 Data collection with external transceivers and "candump"
05:24 Expected vs. actual message plots: missed messages and jitter
06:12 Using cycle time plots to identify desynchronization
06:58 Transmit phase desynchronization: missed and queued data
08:03 Receive phase desynchronization: stale data and overcompensation
08:38 Resolving synchronization issues: kernel primitives and padding
09:25 The impact of logging on system performance
11:09 Reception and priority inversion
12:02 Conclusion and summary of key takeaways

Rishabh Garg
Robotics Engineer at Tesla Optimus

I am Rishabh Garg, a robotics software engineer pushing the boundaries of software hardware integration to meet the ever increasing demand for data. I have been working with robots and embedded systems for the past 4 years, making systems more reliable and performant at companies like Tesla and Amazon. Eager to learn what experts in the industry are doing differently and share my own experience and insights into the challenges frequently encountered at the system software level for robotics.

## Building an Agentic Platform — Ben Kus, CTO Box

- Upload date: 2025-08-24
- Video: https://www.youtube.com/watch?v=12v5S1n1eOY
- Transcript: raw/20250824_12v5S1n1eOY/12v5S1n1eOY.en-orig.vtt
- Metadata: raw/20250824_12v5S1n1eOY/12v5S1n1eOY.info.json

Explore the technical evolution of metadata extraction at Box and how it shaped the foundation of our AI platform. We’ll walk through our transition to an agentic-first design—why it was necessary, how we approached the rebuild, challenges we encountered along the way, and the advantages it unlocked.

Timestamps
00:00 Box's Content Platform and Enterprise Focus
01:50 Initial AI Deployment in 2023
02:54 The Challenge of Unstructured Data in Enterprises
03:56 Limitations of Pre-Generative AI Data Extraction
04:54 First Version: LLM-Based Extraction
07:05 Challenges with the Pure LLM Approach
08:58 Despair and the Need for a New Architecture
09:30 Introducing Agentic Architecture
10:04 AI Agent Reasoning Framework
10:45 Agentic Routine for Data Extraction
12:28 Advantages of Agentic Architecture
14:05 Key Lesson Learned: Build Agentic Architecture Early
18:37 Approach to Fine-tuning and Model Support

Ben Kus
CTO

Ben Kus is the Chief Technology Officer at Box and is responsible for developing Box’s technology vision and strategy and ensuring that technological resources are aligned with the company's business needs. Previously Ben was the VP of Product Management at Box. Before joining Box, Ben was the Co-Founder and CTO of Subspace, Inc., an enterprise security solution that was acquired by Box. Ben has held various leadership positions, including the role of Chief Architect for IBM, and Senior Director of Technology for BigFix, Inc. Ben studied Computer Science at the University of California, Berkeley.

## Perceptual Evaluations: Evals for Aesthetics — Diego Rodriguez, Krea.ai

- Upload date: 2025-08-23
- Video: https://www.youtube.com/watch?v=h5ItAJuB3Fc
- Transcript: raw/20250823_h5ItAJuB3Fc/h5ItAJuB3Fc.en-orig.vtt
- Metadata: raw/20250823_h5ItAJuB3Fc/h5ItAJuB3Fc.info.json

Special session with KREA.ai's cofounder Diego Rodriguez on how evals for aesthetics and image/generative media work — the hardest kinds of evals.

  linkedin.com/in/asciidiego/

Timestamps
00:15 Introduction to Perceptual Evaluations
00:50 The Problem with Current AI Evaluations
02:16 Historical Context and Compression
05:14 Limitations in AI and Human-centric Metrics
08:00 Rethinking Evaluation and the Future of AI
12:44 Evaluating Our Evaluations
13:32 Krea's Role and Call to Action

## Five hard earned lessons about Evals — Ankur Goyal, Braintrust

- Upload date: 2025-08-23
- Video: https://www.youtube.com/watch?v=a4BV0gGmXgA
- Transcript: raw/20250823_a4BV0gGmXgA/a4BV0gGmXgA.en-orig.vtt
- Metadata: raw/20250823_a4BV0gGmXgA/a4BV0gGmXgA.info.json

The main thesis of the video is that building successful AI applications requires a sophisticated engineering approach that goes beyond simply writing good prompts. The speaker argues for the importance of evaluations (evals) as a core component of the development process, highlighting that they should be intentionally engineered to reflect real-world user feedback and drive product improvements. The video also introduces the concept of "context engineering" as the new frontier, where the focus is on optimizing the entire context provided to the model, including tool definitions and their outputs. Ultimately, the speaker advocates for a flexible, model-agnostic architecture that can quickly adapt to the rapidly evolving landscape of AI models.

Timestamps:

00:00 Introduction to 5 Lessons in AI Product Development
00:19 Lesson 1: Effective Evals Speak for Themselves
02:09 Lesson 2: Great Evals Need to Be Intentionally Engineered
04:03 Lesson 3: Context Engineering is the New Prompt Engineering
06:37 Lesson 4: Be Prepared for a New Model to Change Everything
09:09 Lesson 5: Optimize the Entire Evaluation System, Not Just the Prompts
12:21 Recap of the Five Lessons

## How BlackRock Builds Custom Knowledge Apps at Scale — Vaibhav Page & Infant Vasanth, BlackRock

- Upload date: 2025-08-23
- Video: https://www.youtube.com/watch?v=08mH36_NVos
- Transcript: raw/20250823_08mH36_NVos/08mH36_NVos.en-orig.vtt
- Metadata: raw/20250823_08mH36_NVos/08mH36_NVos.info.json

Investment Operations teams are the backbone of asset and investment management firms. Their day-to-day work not only enables portfolio managers to respond swiftly to market events but also ensures that complex, unstructured data flows seamlessly across the organization.
In this talk, we introduce a modular, Kubernetes-native AI framework purpose-built to scale custom Knowledge Apps across the enterprise. Designed with speed, flexibility, and compliance in mind, the framework empowers teams to launch production-grade document extraction applications in minutes instead of months, unlocking new levels of automation and efficiency for investment management workflows.
We’ll also share how this framework has helped BlackRock streamline document extraction processes, generate investment signals, reduce operational overhead, and accelerate the delivery of high-impact business use cases—all while maintaining the robustness and control required in a regulated industry.

00:30 Introduction to BlackRock's AI Initiatives
01:31 Classifying AI Applications
02:22 Use Case: New Issue Operations
03:59 Challenges with Scaling AI Knowledge Apps
07:02 Architecture of BlackRock's AI Framework
08:32 Demonstration of the Sandbox
15:52 Key Takeaways from the Discussion

Vaibhav Page
Principal Engineer

Vaibhav is a Principal Engineer at BlackRock, where he leads the development of the Data Science and AI platform powering
investment research and automation across the firm. Vaibhav is also the author of Argo-Events, a CNCF-graduated project widely used for event-driven automation in cloud-native environments.

Infant Vasanth
Senior Director of Engineering

Infant Vasanth leads the engineering team responsible for the Studio Compute Platform, BlackRock's analytics and automation platform that enables our users to conduct research & analysis, run automations and distribute research at scale.
In addition, Infant is also leading the Data & AI Acceleration team focusing on efforts to enhance Aladdin Studio's AI capabilities along side the Operational AI capabilities(prospectus analyzer, operational agents etc.)

## Multi Agent AI and Network Knowledge Graphs for Change — Ola Mabadeje, Cisco

- Upload date: 2025-08-22
- Video: https://www.youtube.com/watch?v=m0dxZ-NDKHo
- Transcript: raw/20250822_m0dxZ-NDKHo/m0dxZ-NDKHo.en-orig.vtt
- Metadata: raw/20250822_m0dxZ-NDKHo/m0dxZ-NDKHo.info.json

Traditional ticketing and testing workflows for change management and network operations often operate independently and lack critical real-world context and adaptive decision making capabilities. This fragmented approach results in delayed resolutions, repeated incidents, escalations, and dissatisfied stakeholders.

This session explores an innovative solution leveraging the synergy of natural language processing from IT Service Management (ITSM) systems, Multi-agent reasoning, and dynamic context derived from live knowledge network graphs. Attendees will gain insights into an end-to-end architecture where natural language intents from ITSM tickets seamlessly integrate with experts AI agents for complex workflow tasks, supported by continuous network knowledge graph ingestion pipelines.

Through a detailed production case study, we will demonstrate how Agentic reasoning combined with dynamic network knowledge graph contexts significantly improves critical validation and workflow interactions. The showcased results will highlight dramatic improvements in ticket resolution efficiency, accuracy of network testing, and overall execution quality, delivering tangible value to both technical teams and business stakeholders.

## Fuzzing in the GenAI Era — Leonard Tang, Haize Labs

- Upload date: 2025-08-22
- Video: https://www.youtube.com/watch?v=OMGPvW8TBHc
- Transcript: raw/20250822_OMGPvW8TBHc/OMGPvW8TBHc.en-orig.vtt
- Metadata: raw/20250822_OMGPvW8TBHc/OMGPvW8TBHc.info.json

"Evaluation" is one of those concepts that every AI practitioner vaguely knows is important, but few practitioners truly understand. Is "eval" the dataset for measuring the quality of your AI system? Is "eval" the measure, the metric of quality? Is "eval" the process of human annotation and scoring? Or is "eval" a third-party dataset run once to benchmark a model?

To mitigate this cacophony, this talk will provide an opinionated and principled perspective for what we actually mean when we say “evaluation”, beyond the traditional for-loop-over-a-static dataset.

In particular, this perspective draws heavy inspiration from *fuzzing*, i.e. bombarding AI with simulated, unexpected user inputs to uncover corner cases at scale. This factors into sub-problems regarding:

- Quality Metric. What is the actual criteria we, as humans, are using to determine if an AI system is producing good or bad responses? How do we elicit these criteria before the human SME can articulate them? How do we, as efficiently as possible, operationalize this criteria with an automated *Judge*?

- Stimuli Generation. Given a metric, how do we know, with confidence, that an AI system is performing well with respect to the metric? What data is representative and sufficient for discovering all potential bugs of an AI system? And how do we generate this complex, diverse, faithful data at scale?

We will discuss in detail the philosophy, technology, and case studies behind both problems of Quality Metric and Stimuli Generation, and how they interact in concert.

Timestamps
00:00 Introduction to Haizing
01:16 The "Last Mile Problem" in AI
02:47 The Brittleness of GenAI Applications
03:54 Examples of Brittle Chatbots
04:29 Inadequacy of Standard Evaluation Methods
06:09 Haizing: Simulating the Last Mile
08:43 Scaling Evaluation with Agents as Judges
09:29 Verdict: Accuracy vs. Latency
11:47 Scaling Evaluation with RL-Tuned Judges
14:06 Fuzzing vs. Adversarial Testing in AI
14:37 Simulation as Prompt Optimization
16:23 Case Study: Haizing a Major European Bank's AI App
17:05 Case Study: Haizing a F500 Bank's Voice Agents
17:46 Case Study: Scaling Voice Agent Evals with Verdict

Leonard Tang
Founder & CEO

I am the co-founder and CEO of Haize Labs, where we are solving the ultimate extant problem in AI: ensuring its reliability, quality, and alignment for any application. You might also know of us for our red-teaming work.

Prior, I studied math and computer science at Harvard. My research then covered adversarial robustness, math reasoning, computational neuroscience, interpretability, and large(-ish) language models. Much of that has now been distilled into the Haize technology agenda. I also dropped out of, before starting, a Stanford PhD in computer science.

In the limit of my life, I am chiefly invested in starting Bell Labs 2.0.

## Form factors for your new AI coworkers — Craig Wattrus, Flatfile

- Upload date: 2025-08-22
- Video: https://www.youtube.com/watch?v=CiMVKnX-CNI
- Transcript: raw/20250822_CiMVKnX-CNI/CiMVKnX-CNI.en-orig.vtt
- Metadata: raw/20250822_CiMVKnX-CNI/CiMVKnX-CNI.info.json

Designing user experiences for AI means moving beyond traditional interfaces.

Designers are grappling with how to create intuitive and effective interactions for these new AI capabilities, while growing their practice to include philosophy, ethics and coding.

What if AI interactions could be reimagined as new 'coworkers'? This talk explores AI systems as your new coworkers. Covering novel UX patterns we’ve implemented and are researching at Flatfile as well as a state of the union on emergent patterns we’re seeing and using from the industry.

Attendees will get a peek into explorations into AI cursors, forward-leaning chat paradigms and tool UX. We will discuss both work thats in production today at some of our biggest customers as well as thought-provoking demos, offering a vision for the future of AI UX.

Timestamps

00:25 Design Engineering: Form Factors for your new AI coworkers
01:04 Four main categories of AI stack: invisible, ambient, inline, and conversational
02:14 Invisible AI: Personalized demos
03:06 Ambient AI: Analyzing data for opportunities
03:10 Inline AI: Direct data manipulation
03:46 Shifting from helicopter parent to character coach
04:32 The "chat tuner" tool
05:20 Feeling the material of AI
08:20 Finding the grain in AI design
11:08 Courting emergence
11:48 Example of emergence: Combining datasets and generating reports
12:37 Example of emergence: Suggesting human intervention
14:09 Eyes on the future
14:27 "Auto-complete" for data transformations





---

Craig Wattrus
AI Design Engineer

Craig Wattrus is a product designer and technologist working at the edge of human-computer interaction and AI. He designs and codes at Flatfile, where he’s leading a product called AI Transform. He's building adaptive data systems that use agentic AI to automate complex workflows across Fortune 500 companies. With a background in both computer science and design, Craig’s work focuses on shaping new UX patterns for AI systems that observe, learn, and act alongside users not just for them.

Craig is deeply interested in rethinking form factors for AI, exploring how designers can create new patterns of interaction that feel more collaborative, contextual, and adaptive. His approach blends practical, production-ready work with speculative design exploration with working PoC's offering a grounded yet forward-looking take on what AI-native UX can become. When he’s not dreaming up new ideas or testing AI behaviors in production, he’s probably making lamps, tinkering with small-scale hardware, or enjoying a perfect espresso.

## Wisdom-Driven Knowledge Augmented Generation at Scale - Chin Keong Lam, Patho AI

- Upload date: 2025-08-22
- Video: https://www.youtube.com/watch?v=9AQOvT8LnMI
- Transcript: raw/20250822_9AQOvT8LnMI/9AQOvT8LnMI.en-orig.vtt
- Metadata: raw/20250822_9AQOvT8LnMI/9AQOvT8LnMI.info.json

The main thesis of the video is that by using a Wisdom-Driven Knowledge Graph, we can significantly enhance the quantitative analysis capabilities of Knowledge-Augmented Generation (KAG) systems. This allows for the creation of smarter AI systems that can not only retrieve information but also understand, reason, and provide expert-level advice. The talk argues that this approach surpasses traditional Retrieval-Augmented Generation (RAG) systems, which primarily rely on unstructured vector search.

00:00 Introduction to Patho AI and KAG
01:09 Defining Knowledge and Knowledge Graphs
01:56 KAG vs. RAG
02:37 The Wisdom-Decision Making-Situation Diagram
06:26 Practical Application: Competitive Analysis Chatbot
08:37 Implementation with N8n and Multi-Agent System
11:37 Why Use Knowledge Graphs over RAG
14:01 Challenges with Vector RAG and Numerical Reasoning
15:34 Building KAG Systems and Hybrid Models
16:45 Graph Extraction and Benchmarks
17:42 Conclusion and Resources

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## The Next Unicorns: 7 Top AI startups from the HF0 Residency

- Upload date: 2025-08-21
- Video: https://www.youtube.com/watch?v=L8-5ezsoI5A
- Transcript: raw/20250821_L8-5ezsoI5A/L8-5ezsoI5A.en-orig.vtt
- Metadata: raw/20250821_L8-5ezsoI5A/L8-5ezsoI5A.info.json

HF0's Demo Days are usually hilariously oversubscribed and have never before been aired publicly. For the first time, they are joining the AIE stage to pitch AI Engineers.

https://www.hf0.com/

Timestamps

00:15 Diego Rodriguez - Krea
03:02 OpenHome
06:09 Josh - Coframe
07:31 Eugene - Featherless AI
10:39 Jonas Bauer - Upside
13:48 Lengyue - OpenAudio
18:48 Alex Atallah - OpenRouter

## #define AI Engineer - Greg Brockman, OpenAI (ft. Jensen Huang)

- Upload date: 2025-08-10
- Video: https://www.youtube.com/watch?v=avWhreBUYF0
- Transcript: raw/20250810_avWhreBUYF0/avWhreBUYF0.en-orig.vtt
- Metadata: raw/20250810_avWhreBUYF0/avWhreBUYF0.info.json

Greg Brockman's career and advice for AI Engineers

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

00:00 Greg Brockman's Journey and the Power of Independent Study
02:50 Joining Stripe and the Grind of a Startup
08:04 The Power of Independent Study
10:18 Journey into Machine Learning and Belief in AGI
16:10 The Relationship Between Engineering and Research at OpenAI
21:11 Scaling Challenges and Successes at OpenAI
24:32 Vibe Coding and the Future of Software Engineering
26:06 Impact of Codex on Coding Practices
29:20 Scaling Bottlenecks and Future of AI Infrastructure
38:06 Evolution of Development Workflow with AGI

## The Future of Evals - Ankur Goyal, Braintrust

- Upload date: 2025-08-09
- Video: https://www.youtube.com/watch?v=MC55hdWLq4o
- Transcript: raw/20250809_MC55hdWLq4o/MC55hdWLq4o.en-orig.vtt
- Metadata: raw/20250809_MC55hdWLq4o/MC55hdWLq4o.info.json

About Ankur
Ankur Goyal is the founder & CEO of Braintrust—the developer platform that companies like Zapier, Notion, Instacart, Airtable, and more use to evaluate, log, and ship reliable AI products to millions. He was previously Head of AI platform at Figma, founder and CEO of Impira, and VP Eng at Singlestore. After Figma acquired Impira, he led the AI team there, and saw a number of the same blockers to AI development at Impira, Figma, and other peer companies, which led to founding Braintrust

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

Timestamps
00:00 Introduction to AI Engineer World's Fair
00:15 Speaker Introduction: Ankur Goyal, CEO of Braintrust
00:22 The Future of Evals
00:30 Increasing Adoption of Eval
01:58 Introducing Loop
04:09 Call to Action: Try Loop and Join the Team

## Designing AI-Intensive Applications - swyx

- Upload date: 2025-08-09
- Video: https://www.youtube.com/watch?v=IHkyFhU6JEY
- Transcript: raw/20250809_IHkyFhU6JEY/IHkyFhU6JEY.en-orig.vtt
- Metadata: raw/20250809_IHkyFhU6JEY/IHkyFhU6JEY.info.json

Whether you call it a workflow or an agent, AI engineered applications are seeing user-input:LLM-call ratios go from 1:1 (ChatGPT) to 1:100 (Deep Research, Codex) and even 0:n (Ambient/Proactive agents). How does AI Engineering change as you build increasingly AI intensive applications?

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

Timestamps:

00:00 Conference Welcome and Overview
00:42 Conference Logistics and Growth
01:47 Audience Preferences and Survey
02:22 Innovations in AI Engineering (MCP and Chatbots)
02:58 Evolution of AI Engineering (Past Talks)
03:50 Simplicity in AI Engineering
04:17 AI Engineering as a Developing Field
05:23 Seeking the "Standard Model" in AI Engineering
06:02 Candidate Standard Models in AI Engineering
09:26 Human Input vs. AI Output (AI News Example)
11:05 SPADE Model for AI-Intensive Applications
12:29 Call to Action for Conference Attendees

## On Engineering AI Systems that Endure The Bitter Lesson - Omar Khattab, DSPy & Databricks

- Upload date: 2025-08-06
- Video: https://www.youtube.com/watch?v=qdmxApz3EJI
- Transcript: raw/20250806_qdmxApz3EJI/qdmxApz3EJI.en-orig.vtt
- Metadata: raw/20250806_qdmxApz3EJI/qdmxApz3EJI.info.json

Will discuss the principles for building AI software that underpin DSPy, highlighting the differences between conventional prompting (or finetuning/RL) versus the design and programming of truly modular AI systems.

About Omar Khattab   
Omar Khattab is a Research Scientist at Databricks and an incoming Assistant Professor at MIT EECS (July 2025). His research creates models, algorithms, and abstractions for building modular, reliable, and scalable AI systems. He is the author of the ColBERT retrieval model, which has helped shape the modern landscape of neural information retrieval, and the creator of the DSPy framework for building and optimizing declarative natural-language programs.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

Timestamps
00:00 AI Engineer World's Fair
00:22 On Engineering AI Systems that Endure the Bitter Lesson
00:32 The Challenges of AI Software Engineering
00:40 The Bitter Lesson
04:50 AI Engineering's Purpose
06:39 Takeaway 1: Engineering for Scalability
07:19 Premature Optimization
12:18 The Problem with Prompts
14:26 Trusty Old Separation of Concerns
17:11 Takeaway 2: Invest in Decoupling
17:21 The Pyramid of LLM Software and DSPy
17:45 The DSPy Concept: Declarative Signatures

## Vibe Coding with Confidence — Itamar Friedman, Qodo

- Upload date: 2025-08-06
- Video: https://www.youtube.com/watch?v=n991Yxo1aOI
- Transcript: raw/20250806_n991Yxo1aOI/n991Yxo1aOI.en-orig.vtt
- Metadata: raw/20250806_n991Yxo1aOI/n991Yxo1aOI.info.json

Everyone wants to do Vibe Code, even large Enterprises. But how can we ensure that the generated code is well-grounded with the dev team's code and software development standards? In this talk, Itamar will present how to use various tools and agents, including MCP and A2A, to achieve precisely that.

About Itamar Friedman
Itamar Friedman is the CEO and co-founder of Qodo (fka CodiumAI), the leader in the emerging code integrity space.
Prior to that, Itamar was the co-founder and CTO of Visualead, which Alibaba Group acquired. As a director at Alibaba, he led teams to create innovative ML-based B2C and B2D applications and tools used by millions.
Itamar holds a BSc & MSc in Electrical Engineering (Summa Cum Laude) from the Technion, majoring in Machine Learning and Computer Vision.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

Timestamps:

00:00 The Evolution of AI in Development

03:08 The Rise of the Command Line Interface (CLI)

03:50 AI Across the Software Development Life Cycle (SDLC)

06:40 The Importance of "Vibe Coding with Confidence"

08:15 The Role of Workflows and Agents

12:21 Qodo's Multi-Agent Approach

13:55 Why the CLI is the Future of AI in Development

20:33 The Future: A "Swarm of Agents"

## How to look at your data — Jeff Huber (Chroma) + Jason Liu (567)

- Upload date: 2025-08-06
- Video: https://www.youtube.com/watch?v=jryZvCuA0Uc
- Transcript: raw/20250806_jryZvCuA0Uc/jryZvCuA0Uc.en-orig.vtt
- Metadata: raw/20250806_jryZvCuA0Uc/jryZvCuA0Uc.info.json

By the end of this talk, you'll understand what it takes to apply clustering techniques and data analysis to understand what is the valuable work that your AI application is doing through analyzing conversation histories and how to create generative evals to benchmark your newly discovered superpowers.

About Jeff Huber
Jeff Huber is the CEO and cofounder of Chroma. Jeff's work has been featured in TechCrunch, VentureBeat, MacWorld, GQ, Fast Company, Fortune, Forbes, Business Insider, Quartz and others. Chroma is a widely-loved and adopted open-source vector database.

About Jason Liu
Machine learning engineer, consultant, educator.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Evals Are Not Unit Tests — Ido Pesok, Vercel v0

- Upload date: 2025-08-06
- Video: https://www.youtube.com/watch?v=L8OoYeDI_ls
- Transcript: raw/20250806_L8OoYeDI_ls/L8OoYeDI_ls.en-orig.vtt
- Metadata: raw/20250806_L8OoYeDI_ls/L8OoYeDI_ls.info.json

How to think about evaluating a non-deterministic system — and how to actually succeed at it.

About Ido Pesok
Ido Pesok is an engineer and researcher at Vercel, working on the AI behind v0 and focused on building reliable and intuitive AI systems.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

Timestamps:

00:00 Introduction to Vercel's V0 and its growth
01:00 The problem with AI unreliability
02:44 The "Fruit Letter Counter" app example of AI failure
03:33 Introducing "evals" and the basketball court analogy
05:09 Defining the "court": understanding the domain of user queries
07:53 Data collection for evals
09:13 Structuring evals: constants in data, variables in task
10:45 Scoring evals
12:35 Integrating evals into CI/CD
13:40 The benefits of using evals

## 2025 is the Year of Evals! Just like 2024, and 2023, and … — John Dickerson, CEO Mozilla AI

- Upload date: 2025-08-06
- Video: https://www.youtube.com/watch?v=CQGuvf6gSrM
- Transcript: raw/20250806_CQGuvf6gSrM/CQGuvf6gSrM.en-orig.vtt
- Metadata: raw/20250806_CQGuvf6gSrM/CQGuvf6gSrM.info.json

AI is getting deployed without guardrails, without governance, without due diligence.  Surely this is the year we’ll see a Fortune 500 CEO fired because of a preventable AI incident.  Surely this is the year we’ll see enterprises wake up to pre-deployment evaluation and post-deployment monitoring being an urgent need.  This story hasn’t changed for a decade, but surely this is the year it will.

In this talk, I’ll cover what enterprise-level AI/ML evaluation has looked like for the last decade - what’s changed, what hasn’t, what sells, what doesn’t, and where I see things going from here on out.  Evaluation matters - we all know this - but using my experience in the trenches over the last decade or so I hope to bridge the gap between what practitioners need and what the C-suite pays for in the space of AI evaluations.



---related links---

https://x.com/johnpdickerson
https://www.linkedin.com/in/john-dickerson/
https://jpdickerson.com/
https://www.mozilla.ai/

Timestamps:

00:00 Introduction to Arthur AI and Mozilla AI
00:46 2025: The Year of Evals
01:15 AI/ML monitoring and evaluation
02:48 The Year of the Agent
03:26 The need for 'evals' wasn't obvious to the C-suite
04:15 Pre-ChatGPT launch
06:06 Venture capitalists' predictions
07:03 Macroeconomic side of things
08:06 OpenAI launching ChatGPT
09:15 2023: The Year of GenAI
09:39 2024: GenAI applications in production
10:22 2025: Scaling and autonomy
11:35 Definition of an agent
12:06 Connecting to downstream business KPIs
14:40 Shift to multi-agent systems monitoring
15:42 Q&A
16:16 Discussion on domain expertise in evaluations
18:13 Discussion on LLMs as judges

## Full Workshop: Realtime Voice AI — Mark Backman, Daily

- Upload date: 2025-08-03
- Video: https://www.youtube.com/watch?v=nxuTVd7v7dg
- Transcript: raw/20250803_nxuTVd7v7dg/nxuTVd7v7dg.en-orig.vtt
- Metadata: raw/20250803_nxuTVd7v7dg/nxuTVd7v7dg.info.json

Voice AI agents today can conduct natural, human-like conversations and perform a wide variety of tasks: customer support, lead qualification, healthcare patient intake, market research, and more.

Today's best voice agents combine: realtime responsiveness, open-ended conversational intelligence, reliable instruction following, and flexible integration with existing back-end systems.

Learn how to build state of the art voice agents using Pipecat's open source, vendor neutral tooling. You can deploy Pipecat agents to your own infrastructure or to Pipecat Cloud.

Pipecat is used and supported by teams at NVIDIA, AWS, Google DeepMind, OpenAI, and hundreds of other companies.


---related links---

https://x.com/mark_backman
https://www.linkedin.com/in/mark-backman/
https://daily.co

## How to Improve your Vibe Coding — Ian Butler

- Upload date: 2025-08-03
- Video: https://www.youtube.com/watch?v=g03m-WFEu1U
- Transcript: raw/20250803_g03m-WFEu1U/g03m-WFEu1U.en-orig.vtt
- Metadata: raw/20250803_g03m-WFEu1U/g03m-WFEu1U.info.json

[last round of Attendee-Led 10min lightning talks] Are your vibes immaculate? - Vibe coding is the new hotness but everyone has a story of AI making really dumb choices. Let's talk about how you can improve your vibe coding so your vibes are safe and bug free and you spend more Ian Butler

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Real World Development with GitHub Copilot and VS Code — Harald Kirschner, Christopher Harrison

- Upload date: 2025-08-03
- Video: https://www.youtube.com/watch?v=eOxOzcw70f0
- Transcript: raw/20250803_eOxOzcw70f0/eOxOzcw70f0.en-orig.vtt
- Metadata: raw/20250803_eOxOzcw70f0/eOxOzcw70f0.info.json

Join us to see how VS Code and GitHub Copilot's expanding suite of AI features can match or even surpasses the benefits of other popular AI developer tools.  We'll focus on practical scenarios to ensure immediate applicability and work through live demos of Copilot features such as: Code generation using Edits, Planning/problem solving using Chat, Inline terminal command generation, Boilerplate code generation using Agent mode, Improving boilerplate with custom instructions and then refactoring using Agent mode and Edits, Improving test generation and code reviews with custom instructions, as well as an Introduction to MCP.

## Vision AI in 2025 — Peter Robicheaux, Roboflow

- Upload date: 2025-08-03
- Video: https://www.youtube.com/watch?v=IQc05eCvNYE
- Transcript: raw/20250803_IQc05eCvNYE/IQc05eCvNYE.en-orig.vtt
- Metadata: raw/20250803_IQc05eCvNYE/IQc05eCvNYE.info.json

Attendee-Only and Attendee-Led 10min lightning talks: see https://crowdcomms.com/aiengineer25/qanda/41445

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Vibes won't cut it — Chris Kelly, Augment Code

- Upload date: 2025-08-03
- Video: https://www.youtube.com/watch?v=Dc3qOA9WOnE
- Transcript: raw/20250803_Dc3qOA9WOnE/Dc3qOA9WOnE.en-orig.vtt
- Metadata: raw/20250803_Dc3qOA9WOnE/Dc3qOA9WOnE.info.json

What's the role of vibe coding in a production-grade applications? Join Augment Code's Chris Kelly as he talks about the role of context in software engineering, not code.

About Chris Kelly
Chris is the head of developer experience where he works across Augment to make building software better for every developer. He’s been making developers happier and more productive for 15 years at innovative companies like New Relic, GitHub, Salesforce, and FireHydrant. You can find him at @amateurhuman everywhere on the internet.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Practical tactics to build reliable AI apps — Dmitry Kuchin, Multinear

- Upload date: 2025-08-03
- Video: https://www.youtube.com/watch?v=-T6uZYYzkWw
- Transcript: raw/20250803_-T6uZYYzkWw/-T6uZYYzkWw.en-orig.vtt
- Metadata: raw/20250803_-T6uZYYzkWw/-T6uZYYzkWw.info.json

[last round of Attendee-Led 10min lightning talks] Practical tactics to build reliable AI apps. Reverse engineering real-world evals with o3. Nobody does it this way. Companies pay me $500/h for this knowledge. I help them get from POC that works 50% of the time - to the solution they can trust to deploy to production.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Building Agents at Cloud Scale — Antje Barth, AWS

- Upload date: 2025-08-02
- Video: https://www.youtube.com/watch?v=WJjInLeaJjo
- Transcript: raw/20250802_WJjInLeaJjo/WJjInLeaJjo.en-orig.vtt
- Metadata: raw/20250802_WJjInLeaJjo/WJjInLeaJjo.info.json

Let's explore  practical strategies for building and scaling agents in production. Discover  how to move from local MCP implementations to cloud-scale architectures and  how engineering teams leverage these patterns to develop sophisticated agent  systems. Expect a mix of demos, use case discussions, and a glimpse into the  future of agentic services!

About Antje Barth
Antje Barth is a Principal Developer Advocate at AWS, based in San Francisco. She frequently speaks at AI engineering conferences, events, and meetups, and works closely with product teams to build the future of agentic AI. Antje is also co-author of the O’Reilly books Generative AI on AWS and Data Science on AWS.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Useful General Intelligence — Danielle Perszyk, Amazon AGI

- Upload date: 2025-08-02
- Video: https://www.youtube.com/watch?v=Dj0b_cEBHBI
- Transcript: raw/20250802_Dj0b_cEBHBI/Dj0b_cEBHBI.en-orig.vtt
- Metadata: raw/20250802_Dj0b_cEBHBI/Dj0b_cEBHBI.info.json

We’re all hearing that AI agents will enable AGI, but they can’t yet reliably perform even basic computer tasks. It turns out that getting AI to click, type, and scroll is more challenging than getting it to generate code. How can we build general-purpose agents that can do anything we can do on a computer?

This is our goal at the Amazon AGI SF Lab. In this talk, I’ll propose a new approach to agents that we call Useful General Intelligence. After describing how we’re solving the biggest challenges in computer use while enabling developers to access our tech in it’s earliest developmental stages, I’ll show real workflows that developers have built with Nova Act, our agentic model and SDK.

About Danielle
Danielle is a cognitive scientist at the new Amazon AGI SF Lab. She received her PhD from Northwestern, where she studied the evolution and development of language. Previously, she was at Google and Adept.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## State of Startups and AI 2025 - Sarah Guo, Conviction

- Upload date: 2025-08-02
- Video: https://www.youtube.com/watch?v=3MZS5gNElZM
- Transcript: raw/20250802_3MZS5gNElZM/3MZS5gNElZM.en-orig.vtt
- Metadata: raw/20250802_3MZS5gNElZM/3MZS5gNElZM.info.json

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## The 2025 AI Engineering Report — Barr Yaron, Amplify

- Upload date: 2025-08-01
- Video: https://www.youtube.com/watch?v=mQ7_Zje7WKE
- Transcript: raw/20250801_mQ7_Zje7WKE/mQ7_Zje7WKE.en-orig.vtt
- Metadata: raw/20250801_mQ7_Zje7WKE/mQ7_Zje7WKE.info.json

Come hear the results of the 2025 State of AI Engineering: https://www.amplifypartners.com/blog-posts/the-2025-ai-engineering-report

About Barr Yaon
Barr is a data scientist turned investment partner at Amplify Partners where she invests in AI infrastructure and apps

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Hacking the Inference Pareto Frontier - Kyle Kranen, NVIDIA

- Upload date: 2025-08-01
- Video: https://www.youtube.com/watch?v=Y2qc0UhDSnc
- Transcript: raw/20250801_Y2qc0UhDSnc/Y2qc0UhDSnc.en-orig.vtt
- Metadata: raw/20250801_Y2qc0UhDSnc/Y2qc0UhDSnc.info.json

Your model works! It aces the evals! It even passes the vibe check! All that’s required is inference, right? Oops, you’ve just stepped into a minefield:

-Not low-latency enough? Choppy experience. Users churn from your app. 
-Not cheap enough? You’re losing money on every query.
-Not high enough output quality? Your system can’t be used for that application.

A model and the inference system around it form a “token factory” associated with a Pareto frontier— a curve representing the best possible trade-offs between cost, throughput, latency and quality, outside of which your LLM system cannot be applied successfully. 

Outside of the Pareto frontier? You’re back to square one.
That is, unless you’re able to change the shape of the Pareto frontier.

In this session, we’ll introduce NVIDIA Dynamo, a datacenter-scale distributed inference framework as well as the bleeding-edge techniques it enables to hack the Pareto frontier of your inference systems, including:

-Disaggregation - separating phases of LLM generation to make them more efficient
-Speculation - predicting multiple tokens per cycle
-KV routing, storage, and manipulation - ensuring that we don’t redo work that has already been done
-Pipelining improvements for agents - accelerating our workflows using information about the agent

By the end of the talk, we’ll understand how the Pareto frontier limits where models can be applied, the intuition behind how inference techniques can be used to modify it, as well as the mechanics of how these techniques work.



---related links---

https://x.com/kranenkyle
https://www.linkedin.com/in/kyle-kranen/
https://www.nvidia.com/en-us/

Timestamps:

00:00 Introduction to Breaking the Inference Pareto Frontier
00:33 Introduction of Kyle Cranon and NVIDIA Dynamo
01:31 The Three Pillars of Deployment (Quality, Latency, Cost)
02:11 Understanding the Pareto Frontier
03:06 Application-Specific Prioritization of Quality, Latency, and Cost
04:32 Common Techniques to Manipulate the Pareto Frontier (Quantization, RAG, Reasoning)
05:19 Compounding Techniques
06:04 Three Drivers for Modifying the Pareto Frontier (Scale, Structure, Dynamism)
06:20 Scale: Disaggregation
11:02 Scale: Routing
13:00 Structure: Inference Time Scaling
16:14 Structure: KV Manipulation
17:43 Dynamism: Worker Specialization
18:42 Dynamism: Dynamic Load Balancing
19:55 Conclusion and NVIDIA Dynamo Resources

## Why We Don’t Need More Data Centers - Dr. Jasper Zhang, Hyperbolic

- Upload date: 2025-08-01
- Video: https://www.youtube.com/watch?v=M6Vbaig1TsM
- Transcript: raw/20250801_M6Vbaig1TsM/M6Vbaig1TsM.en-orig.vtt
- Metadata: raw/20250801_M6Vbaig1TsM/M6Vbaig1TsM.info.json

AI infrastructure today is caught in an endless cycle: build more data centers, deploy more GPUs, repeat.

But this approach is fundamentally flawed—expensive, inefficient, and environmentally unsustainable.

In this talk, we will unpack why continuously expanding data centers masks deeper infrastructure inefficiencies, and why leveraging a GPU marketplace to dynamically allocate existing resources is essential.

We will explore practical use-cases where companies scale GPU capacity flexibly, startups gain affordable compute, and idle GPUs are monetized, enabling a future of sustainable and democratized AI infrastructure.

About Dr  Jasper Zhang, PhD
Dr. Jasper Zhang is the CEO and Co-founder of Hyperbolic. A mathematical prodigy, he completed his Ph.D. in Mathematics at UC Berkeley in just two years. He is a Gold Medalist in both the Alibaba Global Math Competition and the Chinese Mathematical Olympiad. Before founding Hyperbolic, he held roles at Ava Labs and Citadel Securities, bringing deep expertise in quantitative finance and AI.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Agents vs Workflows: Why Not Both? — Sam Bhagwat, Mastra.ai

- Upload date: 2025-08-01
- Video: https://www.youtube.com/watch?v=8SUJEqQNClw
- Transcript: raw/20250801_8SUJEqQNClw/8SUJEqQNClw.en-orig.vtt
- Metadata: raw/20250801_8SUJEqQNClw/8SUJEqQNClw.info.json

One current hot debate is should you make your top-level abstraction a ReAct type agent running in a loop? or should you make it a structured workflow graph?

OpenAI is launching their new framework and throwing shade on workflow graph approaches

TBH we think this whole debate is kinda dumb.

We've seen a lot of folks be able to structure the problem in a way that a workflow graph makes a lot of sense.

We also see a ton of agents where you need to run the core bit in a loop for a long time.

You can also give your agents structured workflow graphs as a tool. You can use structured workflow graphs as a handoff mechanism between agents. What we've seen from the community is frankly that folks need to tinker with multiple approaches and combine primitives in interesting ways

We'll share a couple stories where teams ended up with workflow graph based approaches, a couple where teams ended up with agent based approaches, and a couple where a blended approach made sense.

About Sam Bhagwat
Sam is the co-founder and CEO of Mastra and the author of Principles of AI Agents. Previously, Sam was the co-founder of Gatsby.js, the popular web framework.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

Timestamps:

00:00 Introduction: Agents vs. Workflows
01:00 The Debate and Controversy
02:15 "Don't Be That Guy": Critiquing Dogma in AI Development
03:40 Harmful APIs and the Case for Fluent Syntax
08:00 Defining Agents and Workflows
10:00 Composition, Design Patterns, and Trade-offs
11:49 Composing Agents and Workflows
12:12 Architectural Patterns for Composition
14:43 Q&A and Concluding Thoughts

## Infrastructure for the Singularity — Jesse Han, Morph

- Upload date: 2025-08-01
- Video: https://www.youtube.com/watch?v=2goSS66XRBk
- Transcript: raw/20250801_2goSS66XRBk/2goSS66XRBk.en-orig.vtt
- Metadata: raw/20250801_2goSS66XRBk/2goSS66XRBk.info.json

We're at an inflection point where AI agents are transitioning from experimental tools to practical coworkers. This new world will demand new infrastructure for RL training, test-time scaling, and deployment. This is why Morph Labs developed Infinibranch last year, and we are excited to finally unveil what's next.

About Jesse Han   
Jesse Han is the Founder and CEO of Morph Labs, a company building the infrastructure for the singularity. Morph is the creator of Infinibranch, a breakthrough in cloud technology that enables scaling train-time and test-time search for agentic reasoning models. Jesse began his career as a pure mathematician and research scientist at OpenAI working on test-time compute scaling, GPT-4, and reasoning.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Serving Voice AI at $1/hr: Open-source, LoRAs, Latency, Load Balancing - Neil Dwyer, Gabber

- Upload date: 2025-07-31
- Video: https://www.youtube.com/watch?v=rD23-VZZHOo
- Transcript: raw/20250731_rD23-VZZHOo/rD23-VZZHOo.en-orig.vtt
- Metadata: raw/20250731_rD23-VZZHOo/rD23-VZZHOo.info.json

This is a talk that goes over our experience deploying Orpheus (Emotive, Realtime TTS) to production. It will cover topics:

- Latency and optimizations
- High fidelity voice clones w/ examples
- Load balancing w/ multiple GPUs and multiple LoRas

About Neil Dwyer
Spent a lot of my career building real-time applications. First at a company called Bebo circa 2018 where I built a live streaming + computer vision pipeline that watched people play Fortnite. More recently at a company called LiveKit where I worked on the Agents platform along with some amazing people. And now at my own startup, Gabber, where we are making it easier (and cheaper!) to make real-time, multi-modal consumer apps.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

Timestamps

00:00 Introduction to Gabber and Real-Time AI
02:15 Gabber's Mission for Consumer AI
04:17 The Orpheus Voice Model
05:43 Challenges in Voice Cloning
07:44 Latency Management and "Head of Line Silence"
11:07 Infrastructure for Batch Inference
11:36 Leveraging vLLM and Dynamic Quantization
13:21 Load Balancing with a Consistent Hash Ring
14:17 System Architecture Overview
15:07 Conclusion and Open Source Shout-outs

## From Self-driving to Autonomous Voice Agents — Brooke Hopkins, Coval

- Upload date: 2025-07-31
- Video: https://www.youtube.com/watch?v=kDczF4wBh8s
- Transcript: raw/20250731_kDczF4wBh8s/kDczF4wBh8s.en-orig.vtt
- Metadata: raw/20250731_kDczF4wBh8s/kDczF4wBh8s.info.json

The reliability challenges facing voice & chat AI deployment today mirror those that the autonomous vehicle industry confronted years ago. This talk explores how evaluation methodologies developed for self-driving cars can be transferred to create autonomous, self-improving evaluation systems for conversational AI. Drawing from my experience building evaluation infrastructure at Waymo and now developing Coval, an enterprise-grade reliability platform for conversational agents, I'll demonstrate how systematic testing infrastructure is not just a technical requirement but a competitive advantage in the rapidly evolving AI landscape.

--

 
Brooke Hopkins is the Founder at Coval, where her team builds the enterprise-grade reliability infrastructure for conversational AI. Previously, she built evaluation systems at Waymo that helped enable safe autonomous driving. With experience spanning both physical and digital AI domains, Brooke brings unique insights into creating robust testing frameworks that can scale with AI's rapid development.

## [Full Workshop] Building Conversational AI Agents - Thor Schaeff, ElevenLabs

- Upload date: 2025-07-31
- Video: https://www.youtube.com/watch?v=MPtCBaZn84A
- Transcript: raw/20250731_MPtCBaZn84A/MPtCBaZn84A.en-orig.vtt
- Metadata: raw/20250731_MPtCBaZn84A/MPtCBaZn84A.info.json

In this workshop you will learn how to build multilingual Conversational AI agents that can automatically detect your user's spoken language and can seamlessly switch to their preferred language.

About Thor Schaef  
Thor is a software engineer who loves to teach and help developers build. 

Having grown up around the SAP headquarters in Germany, he started building on the web back in high-school, later studied Computer Science and Media across Germany, Ireland, and Switzerland, and interned with the Google Maps Team in London. 

He joined early Stripe in Dublin, building out various customer-facing engineering teams across Europe and Southeast Asia, contributing to open-source software, while mentoring and investing in early stage startups along the way. 

Settled in sunny Singapore since 2019, he helped grow Supabase from 800 to over a million databases, and recently joined ElevenLabs to help build the developer platform for AI audio!

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Pipecat Cloud: Enterprise Voice Agents Built On Open Source - Kwindla Hultman Kramer, Daily

- Upload date: 2025-07-31
- Video: https://www.youtube.com/watch?v=IA4lZjh9sTs
- Transcript: raw/20250731_IA4lZjh9sTs/IA4lZjh9sTs.en-orig.vtt
- Metadata: raw/20250731_IA4lZjh9sTs/IA4lZjh9sTs.info.json

Voice AI agents today can conduct natural, human-like conversations and perform a wide variety of tasks: customer support, lead qualification, healthcare patient intake, market research, and more.

Today's best voice agents combine: realtime responsiveness, open-ended conversational intelligence, reliable instruction following, and flexible integration with existing back-end systems.

Learn how to build state of the art voice agents using Pipecat's open source, vendor neutral tooling. You can deploy Pipecat agents to your own infrastructure or to Pipecat Cloud.

Pipecat is used and supported by teams at NVIDIA, AWS, Google DeepMind, OpenAI, and hundreds of other companies.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Your realtime AI is ngmi — Sean DuBois (OpenAI), Kwindla Kramer (Daily)

- Upload date: 2025-07-31
- Video: https://www.youtube.com/watch?v=E71YtNbCFXY
- Transcript: raw/20250731_E71YtNbCFXY/E71YtNbCFXY.en-orig.vtt
- Metadata: raw/20250731_E71YtNbCFXY/E71YtNbCFXY.info.json

Sean DuBois of OpenAI and Pion, and Kwindla Hultman Kramer of Daily and Pipecat, will talk about why you have to design realtime AI systems from the network layer up.

Most people who build realtime AI apps and frameworks get it wrong. They build from either the model out or the app layer down. But unless you start with the network layer and build up, you'll never be able to deliver realtime audio and video streams reliably. And perhaps even worse, you'll get core primitives wrong: interruption handling, conversation state management, asynchronous function calling.

Sean and Kwin agree on most things: old-school realtime systems people against the rest of the world. But they disagree on some important things, too, and will argue about those things live on stage. Do you need to give developers "thick" client-side realtime SDKs? Can you build truly great vendor neutral APIs? (You'll be surprised which of them argues which side, on that topic.)

About Kwindla Kramer
Kwin works on large-scale WebRTC infrastructure at Daily. He is the originator of Pipecat, the widely used, open source, vendor neutral voice agent framework supported by NVIDIA, Google, AWS and used by hundreds of startups. Before co-fonding Daily, Kwin built the sci-fi user interfaces in Minority Report and Iron Man.

About Sean DuBois
Sean works on WebRTC and the Realtime API at OpenAI. He built 1-800-CHATGPT. He is the founder of Pion, the most widely used open source WebRTC project. He has previously worked at AWS, LiveKit, Apple, and Etsy.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter


00:00 [Voice Keynote] Your realtime AI is ngmi — Sean DuBois (OpenAI), Kwindla Kramer (Daily)
01:29 Introduction to Voice AI and Latency
02:46 Latency Breakdown in a Voice AI Application
03:27 WebRTC vs. WebSockets for Real-Time Audio
06:41 Advantages of WebRTC
07:49 Applications of WebRTC
08:52 Future of Voice AI and User Interfaces
09:59 Squabbert Demo
12:44 Flexibility of WebRTC Connections
13:09 Community Showcase: Yashin's Project
15:46 Call to Action and Resources

## Why ChatGPT Keeps Interrupting You — Dr. Tom Shapland, LiveKit

- Upload date: 2025-07-31
- Video: https://www.youtube.com/watch?v=1v9zBiZKlIY
- Transcript: raw/20250731_1v9zBiZKlIY/1v9zBiZKlIY.en-orig.vtt
- Metadata: raw/20250731_1v9zBiZKlIY/1v9zBiZKlIY.info.json

ChatGPT Advanced Voice Mode isn’t interrupting just you. Interruptions, and turn-taking in general, are unsolved problems for all Voice AI agents. Nobody likes being cut short – and people have much less patience for machines than they do for other humans. Turn-taking failures take many forms (e.g., the agent interrupts the user, the agent mistakes a cough for an interruption), and all of them lead to users immediately hanging up the phone.

In this talk, we use human conversation as a framework for understanding both today’s approaches to turn detection and where the field is headed. You’ll learn about how linguists think about turn detection in human dialogue, what’s working (and what’s broken) in current methods, and how we might build Voice AIs that interrupt you less than your human brother.

About Tom Shapland
Tom Shapland, PhD, is a Product Manager at LiveKit. LiveKit is an open source platform for building, deploying, and scaling realtime multimodal agents. He's passionate about the multimodal future of human-computer interfaces. Before LiveKit, he was the cofounder of a Voice AI observability platform (Canonical AI) and an agriculture technology startup (Tule, YC S14). He lives in the East Bay and coaches lacrosse for his two kids.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## OpenAI on Securing Code-Executing AI Agents — Fouad Matin (Codex, Agent Robustness)

- Upload date: 2025-07-30
- Video: https://www.youtube.com/watch?v=w7IMuYsBNr8
- Transcript: raw/20250730_w7IMuYsBNr8/w7IMuYsBNr8.en-orig.vtt
- Metadata: raw/20250730_w7IMuYsBNr8/w7IMuYsBNr8.info.json

Code is the lingua franca for both software engineers and highly capable AI models. As we give agents the ability to build, test, and run code that they generate, the command line becomes their canvas—and their attack surface.

This keynote explores what it takes to bring code-executing agents from research to real-world deployment while maintaining control and security. We’ll cover how terminals offer AI an ideal interface, why they’re deceptively risky, and what it means to embed security, guardrails, and trust at every layer.

It’s not just about what agents can do—it’s about what they should do, and how we make sure they do it safely.

Join the new Agent Robustness team! https://x.com/gdb/status/1930831992171749773

About Fouad Matin   
Fouad Matin is an engineer who co-founded Indent, temporary access control startup, before joining OpenAI to work on AGI-ready security, and previously worked on data infrastructure products at Segment. In 2016, he co-founded VotePlz, a non-partisan voter registration and turnout non-profit. Passionate about helping people find fulfilling work, he previously started a referral recruiting company which went through Y Combinator in W16 batch.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

Timestamps:

00:00 Introduction to Code-Executing Agents
02:29 Shifting Paradigm in AI Agent Building
03:07 Security Concerns with Code Execution
04:25 Safety Safeguards: Sandboxing
05:02 Safety Safeguards: Disabling/Limiting Internet Access
09:44 Safety Safeguards: Human Review
11:19 Building Agents and Future Work

## How we hacked YC Spring 2025 batch’s AI agents — Rene Brandel, Casco

- Upload date: 2025-07-30
- Video: https://www.youtube.com/watch?v=kv-QAuKWllQ
- Transcript: raw/20250730_kv-QAuKWllQ/kv-QAuKWllQ.en-orig.vtt
- Metadata: raw/20250730_kv-QAuKWllQ/kv-QAuKWllQ.info.json

We hacked 7 of the16 publicly-accessible YC X25 AI agents. This allowed us to leak user data, execute code remotely, and take over databases. All within 30 minutes each. In this session, we'll walk through the common mistakes these companies made and how you can mitigate these security concerns before your agents put your business at risk.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

Timestamps:

00:00 Introduction to Casco and AI Agents
01:31 Evolution of Agent Stacks and Security Concerns
02:56 Why Casco Hacked AI Agents
04:00 Common Issue 1: Cross-User Data Access (IDOR)
07:38 Common Issue 2: Arbitrary Code Execution
12:38 Common Issue 3: Server-Side Request Forgery (SSRF)
14:48 Key Takeaways
15:28 Casco's Solution and Contact Information
15:56 Q&A

## How to Secure Agents using OAuth — Jared Hanson (Keycard, Passport.js)

- Upload date: 2025-07-30
- Video: https://www.youtube.com/watch?v=blmAkayzE8M
- Transcript: raw/20250730_blmAkayzE8M/blmAkayzE8M.en-orig.vtt
- Metadata: raw/20250730_blmAkayzE8M/blmAkayzE8M.info.json

We all know sharing passwords is bad (unless you want free TV), so why are we sharing API keys with AI?  We shouldn't, and that’s why we need to talk about OAuth.

In this talk, we will give a brief intro to OAuth.  Then we will talk about the state of authorization in MCP.  We will show how an MCP client uses OAuth to authenticate a user and securely access private resources and tools hosted by an MCP server.  Then we’ll look at ways autonomous agents can use OAuth on their own behalf, talking to other agents and MCP servers directly.  We’ll learn how to use OAuth to build agents that humans and machines can trust.

About Jared Hanson
Jared Hanson is the co-founder of Keycard, a company building identity infrastructure for the agent-native world. Previously at Okta and Auth0, Jared is an expert on OpenID, OAuth, and all things identity. He’s also the author of Passport.js, the popular authentication framework for Node.js. At Keycard, he is applying that knowledge to securing AI and infrastructure.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## How to defend your sites from AI bots — David Mytton, Arcjet

- Upload date: 2025-07-30
- Video: https://www.youtube.com/watch?v=Gi4V8viBGYQ
- Transcript: raw/20250730_Gi4V8viBGYQ/Gi4V8viBGYQ.en-orig.vtt
- Metadata: raw/20250730_Gi4V8viBGYQ/Gi4V8viBGYQ.info.json

Constantly seeing CAPTCHAs? It used to be easy to detect the humans from the droids, but what else can we do when synthetic clients make up nearly half of all web requests. Rotating IPs, spoofed browsers, and agents acting on behalf of real users - are we doomed to forever be solving puzzles?
    
    In this talk, we’ll explore user agents, HTTP fingerprints, and IP reputation signals that make humans and agents stand out from scrapers, build a realistic threat model, and dig into the behaviors that reveal the LLM-mimicry. Leave with AX- and UX-safe code, benchmarks, and tools to help you take back control.

## The Unofficial Guide to Apple’s Private Cloud Compute - Jmo, CONFSEC

- Upload date: 2025-07-30
- Video: https://www.youtube.com/watch?v=CCsWZ5bJlO8
- Transcript: raw/20250730_CCsWZ5bJlO8/CCsWZ5bJlO8.en-orig.vtt
- Metadata: raw/20250730_CCsWZ5bJlO8/CCsWZ5bJlO8.info.json

In October 2024, Apple released a new private AI technology onto millions of devices called “Private Cloud Compute”. It brings the same level of privacy and security a local device offers but on an “untrusted" remote server. This talk discusses how Private Cloud Compute represents a paradigm shift in confidential computing and explores the core advancements that made it possible to become mainstream. We’ll explore its novel architecture that allows developers to run sensitive, multi-tenant workloads with cryptographically-provably privacy guarantees at scale and at reasonable cost. Attendees will leave with an understanding of how to leverage this technology for data and AI applications where privacy and security is paramount.

About Jonathan Mortensen
Jonathan Mortensen is a technology executive and founder with expertise spanning AI, data infrastructure, and cybersecurity. Currently serving as CEO of a stealth AI startup and Founder Fellow at South Park Commons, Jonathan previously founded bit.io, a multi-cloud serverless PostgreSQL platform acquired by Databricks. As bit.io's CTO, he built innovative database technology that handled hundreds of thousands of databases securely across multiple cloud providers. Prior to founding bit.io, Jonathan led data science and engineering teams at BlueVoyant, where he designed high-volume data pipelines processing 50 million events per second. He holds a PhD in Biomedical Informatics from Stanford University and combines technical depth with leadership experience across engineering, revenue, and operations.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter


00:00 Introduction to Apple's Private Cloud Compute (PCC)
00:58 The Motivation for Privacy in AI
02:20 The Core Problem: Balancing AI Compute Needs with User Privacy
03:59 Apple's Five Key Requirements for Private Cloud Compute
05:22 Conceptual Architecture of the PCC System
08:06 The Six Core Technical Components of PCC
10:22 Deep Dive: Remote Attestation
11:52 Deep Dive: Transparency Log
13:22 How Remote Attestation and the Transparency Log Work Together
15:09 Gaps, Downsides, and Trade-offs of the System
17:33 How Developers Can Use Similar Privacy-Enhancing Technologies
19:17 Industry Trends in Private Processing

## Building a Smarter AI Agent with Neural RAG - Will Bryk, Exa.ai

- Upload date: 2025-07-29
- Video: https://www.youtube.com/watch?v=xnXqpUW_Kp8
- Transcript: raw/20250729_xnXqpUW_Kp8/xnXqpUW_Kp8.en-orig.vtt
- Metadata: raw/20250729_xnXqpUW_Kp8/xnXqpUW_Kp8.info.json

RAG quality for AI agents is critical, and traditional keyword-based search engines consistently underperform in agentic or multi-step tasks, where semantic grounding and contextual nuance matter most.

In this talk, Will Bryk, CEO of Exa will live code two AI agent applications–one using traditional keyword search RAG and one using neural network RAG via vector search. He’ll then evaluate both applications based on task performance, relevance, and latency. With a live demo (no theory or pre-baked applications), the audience will get a firsthand look at the practical differences between keyword and semantic systems in production, and learn embedding strategies, indexing trade-offs, hybrid retrieval techniques, prompt tuning, and more.

About Will Bryk
A year before ChatGPT launched, Will was already spending his time building Exa’s API to crawl the web intelligently, focusing on finding quality sources over SEO spam. Backed by NVIDIA and Lightspeed, Exa now powers products for customers like Databricks, Cursor, and LlamaIndex.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Evaluating AI Search: A Practical Framework for Augmented AI Systems — Quotient AI + Tavily

- Upload date: 2025-07-29
- Video: https://www.youtube.com/watch?v=wRJD0inpmjU
- Transcript: raw/20250729_wRJD0inpmjU/wRJD0inpmjU.en-orig.vtt
- Metadata: raw/20250729_wRJD0inpmjU/wRJD0inpmjU.info.json

AI search is becoming the front door to information, whether through Retrieval-Augmented Generation (RAG), Search-Augmented Generation (SAG), or custom agents that synthesize answers on top of indexed content. As users rely more heavily on these systems, evaluating their quality becomes mission-critical. But traditional metrics like precision and recall don’t capture the full picture.

In this talk, we introduce a practical evaluation framework for AI-powered search, across three dimensions:
- Are the retrieved sources relevant to the query?
- And is the final answer complete?
- Are the sources faithfully used in the generated answer?

We’ll share lessons from working with search companies and present early findings from a new benchmark evaluating popular augmented AI systems across these dimensions. Rather than ranking winners and losers, we explore where different systems excel or break down, and how these tradeoffs inform product decisions.

This talk is for AI engineers and product teams who want to build trusted, high-quality AI search experiences, and need a way to measure if it’s actually working.

About Julia Neagu
Julia is the co-founder and CEO of Quotient AI, which provides intelligent observability for AI apps by automatically detecting failures, uncovering root causes, and recommending improvements. Before Quotient, she was the Director of Data for Copilot, GitHub's AI pair programmer, where her team built the systems evaluating the large language models behind Copilot. Previously, she was the Director of Analytics at Tamr and led end-to-end quantitative modeling at Aon's Intellectual Property Solutions group. Julia has a PhD and MA in Physics from Harvard, an AB in Physics from Princeton.

About Deanna Emery
Deanna is the Founding AI Researcher at Quotient AI, where she is leading research on evaluation of Large Language Models in real-world products and applications. Before Quotient, Deanna was a Principal Data Scientist at Aon, where she led the team building language models for valuation of intellectual property assets. She began her career as a researcher at Harvard-Smithsonian Center for Astrophysics and Caltech LIGO. Deanna has a MS in Machine Learning from UC Berkeley and BA in Physics from Harvard University. She is passionate about diversity and inclusion in STEM; she has conducted research on diversity in named patent inventors, working with companies to measure and address diversity gaps, and she is an active board member at a STEM education non-profit.

About Maitar Asher
Maitar Asher is a founding member and Head of Engineering at Tavily, a New York–based startup developing a web infrastructure layer for AI agents.

She leads the technology build and has architected core systems—including Tavily’s intelligent caching layer and enhanced search retrieval—to power the industry’s premier search engine for large language models.

Prior to Tavily, she developed deep learning tools for PET/CT image segmentation as a Machine Learning Research Engineer at Stanford University. She holds a B.S. in Computer Science (Machine Learning) from Columbia University.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Layering every technique in RAG, one query at a time - David Karam, Pi Labs (fmr. Google Search)

- Upload date: 2025-07-29
- Video: https://www.youtube.com/watch?v=w9u11ioHGA0
- Transcript: raw/20250729_w9u11ioHGA0/w9u11ioHGA0.en-orig.vtt
- Metadata: raw/20250729_w9u11ioHGA0/w9u11ioHGA0.info.json

Start with the simplest Search - in-memory embeddings with relevance ranking. End with the most complex planet-scale Search - 70+ corpus mix of token, embeddings, and knowledge graphs, all jointly retrieved, custom ranked, joint re-ranked, and then LLM-processed, at 160,000 queries per second in under 200msec.

This talk will be a fun “one query at a time” survey of all techniques in RAG in incremental complexity, showing the limits of each technique and what the next layered one opens up in terms of capabilities to handle ever-more complex queries in RAG. You’ll learn why queries like [falafel] are notoriously hard to Search over, why chunking your documents can be disastrous, how you can sometimes can get away with a simple bm25, and how some Search problems are so hard to solve that you’re better off punting the problem to the LLM or the UX. Brought to you by the team that worked on 50+ Search products, in the context of Google.com and custom Enterprise Search.

About David Karam
I'm David K. I love straddling the line between deep tech research and application development. I’ve spent a decade at Google as Product Director working on Search’s core AI and NLU systems, helping Search’s own version of “AI Engineers” develop magical applications. Around a year ago I left with my cofounder to start Pi Labs where we’re trying to bring that same spirit to the rest of the industry. Outside work I love to read, cook, and spend time in nature.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

Timestamps:
00:00 Introduction and Context
01:41 Quality Engineering Loop and Mindset
04:09 In-Memory Retrieval
04:50 Term-Based Retrieval (BM25)
05:18 Relevance Embeddings (Vector Search)
06:15 Re-Rankers (Cross Encoders)
07:59 Custom Embeddings
09:40 Domain-Specific Ranking Signals
11:09 User Preference Signals
12:17 Query Orchestration (Fan Out)
14:26 Supplementary Retrieval
16:09 Distillation
17:14 Punting the Problem and Graceful Degradation

## [Full Workshop] Building Metrics that actually work — David Karam, Pi Labs (fmr Google Search)

- Upload date: 2025-07-29
- Video: https://www.youtube.com/watch?v=jxrGodnopHo
- Transcript: raw/20250729_jxrGodnopHo/jxrGodnopHo.en-orig.vtt
- Metadata: raw/20250729_jxrGodnopHo/jxrGodnopHo.info.json

One of the biggest challenges in building evals you can trust is building metrics that reliably measure goodness in your application; metrics that are highly accurate, rapid fast, and tunable to ground truth rater and user behavior. This workshop is inspired by decades of AI and machine learning development in Google Search, reinvented for the modern LLM stack by the Pi team over the past year.

In this workshop you will learn how to:

1. Brainstorm and design custom metrics tailored to your specific application needs.
2. Identify which types of signals (natural language, code, other models) work best for your use case through rapid trial and error.
3. Combine & calibrate your metrics against ground truth data using real examples from your domain.
4. Use simple tools like Google Sheets for visualizing and analyzing your inputs and outputs with those metrics.
5. Integrate your scoring models into both online workflows like agent control and offline ones like model comparison and training evaluation.

About David Karam
I'm David K. I love straddling the line between deep tech research and application development. I’ve spent a decade at Google as Product Director working on Search’s core AI and NLU systems, helping Search’s own version of “AI Engineers” develop magical applications. Around a year ago I left with my cofounder to start Pi Labs where we’re trying to bring that same spirit to the rest of the industry. Outside work I love to read, cook, and spend time in nature.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Scaling Enterprise-Grade RAG: Lessons from Legal Frontier - Calvin Qi (Harvey), Chang She (Lance)

- Upload date: 2025-07-29
- Video: https://www.youtube.com/watch?v=W1MiZChnkfA
- Transcript: raw/20250729_W1MiZChnkfA/W1MiZChnkfA.en-orig.vtt
- Metadata: raw/20250729_W1MiZChnkfA/W1MiZChnkfA.info.json

In domains like law, compliance, and tax, building enterprise-grade RAG means very large scale, spikey workloads, a focus on accuracy, and non-negotiable privacy. In this talk, we'll share war stories and battle scars of how Harvey has built the world's most advanced AI agents for the legal profession on top of a highly optimized retrieval architecture. We'll cover how to get better retrieval via both sparse and dense retrieval methods, why domain-specific reranking is essential, and how to handle ambiguity in real-world queries. We'll also touch on how LanceDB's search engine enables this architecture by delivering low-latency, high-throughput retrieval across millions of documents of varying sizes without compromising privacy. This solid foundation enables Harvey to build a product that brings highly accurate answers to hundreds of law firms and professional services firms across 45 countries.

About Chang She
Two decades of building data tools for ML/AI. Pandas co-author. Building LanceDB, the database for multimodal AI.

About Calvin Qi
Calvin works on Retrieval Augmented Generation at Harvey for expert use cases in Legal, Tax, and more.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Building Alice’s Brain: an AI Sales Rep that Learns Like a Human - Sherwood & Satwik, 11x

- Upload date: 2025-07-29
- Video: https://www.youtube.com/watch?v=KWmkMV0FNwQ
- Transcript: raw/20250729_KWmkMV0FNwQ/KWmkMV0FNwQ.en-orig.vtt
- Metadata: raw/20250729_KWmkMV0FNwQ/KWmkMV0FNwQ.info.json

AI agents are becoming essential tools for teams of all sizes and industries - but training them to become experts in your product, business, and customerbase remains a challenge.

What if onboarding a digital worker was as simple as uploading your pitch deck? At 11x, we built Alice, an AI SDR that writes outbound emails with the nuance and context of a top-performing human sales rep - because she learns like one too!

In this talk, we'll share how we built a knowledge base that allows 11x customers to "train" Alice on their internal materials: PDFs, websites, call recordings, and more. We'll talk through the ingestion pipeline in detail, discuss storage/retrieval technologies and their tradeoffs, and explain how Alice uses the knowledge base to drive high-performance email outreach at scale.

About Sherwood Callaway
Sherwood Callaway is an emerging leader in the world of AI startups and AI product development. He currently serves as the first engineering manager at 11x, a series B AI startup backed by Benchmark and Andreessen Horowitz, where he oversees technical work on "Alice", an AI sales rep that outperforms top human SDRs.

Alice is an advanced agentic AI working in production and at scale. Under Sherwood’s leadership, the system grew from initial prototype to handling over 1 million prospect interactions per month across 300+ customers, leveraging partnerships with OpenAI, Anthropic, and LangChain while maintaining consistent performance and reliability. Alice is now generating eight figures in ARR.

Sherwood joined 11x in 2024 through the acquisition of his YC-backed startup, Opkit, where he built and commercialized one of the first-ever AI phone calling solutions for a specific industry vertical (healthcare). Prior to Opkit, he was the second infrastructure engineer at Brex, where he designed, built, and scaled the production infrastructure that supported Brex’s application and engineering org through hypergrowth. He currently lives in San Francisco, CA.

About Satwik Singh
Satwik Singh is a core builder and emerging technical leader in the rapidly evolving field of applied AI and agentic systems. As a Member of Technical Staff at 11x AI, Satwik is at the forefront of developing "Alice", an AI sales representative that operates autonomously at scale—transforming how modern GTM teams work.

At 11x, Satwik has architected and delivered several of the company's most critical agent capabilities. He led the creation of the Knowledge Base Retrieval-Augmented Generation (RAG) and Deep Research pipeline, which powers Alice's ability to reason over complex product information and tailor responses with high fidelity: a first-of-its-kind system in the GTM agent space. He has also worked across systems to handle the credits ledger, and engineered the Sourcing Agent that autonomously crafts campaigns. Satwik has been instrumental in shaping the technical foundation of Alice's intelligence and reliability.

Prior to 11x, Satwik was a software engineer at Meta, where he worked on Generative AI products within the Core Ads organization and contributed to infrastructure across Reality Labs. His work helped ship first-generation GenAI creative enhancements for Feed Ads—driving significant revenue gains at scale.

Satwik's unique strength lies in his ability to move seamlessly between infrastructure, AI product, and agent behavior—designing systems that are production-ready, high-impact, and aligned with real business outcomes. With deep hands-on experience and a vision for what Agentic AI can become, he's helping define the next era of intelligent software.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Everything is ugly, so go build something that isn't — Raiza Martin, Huxe (ex NotebookLM)

- Upload date: 2025-07-28
- Video: https://www.youtube.com/watch?v=yG5d5UaGz1M
- Transcript: raw/20250728_yG5d5UaGz1M/yG5d5UaGz1M.en-orig.vtt
- Metadata: raw/20250728_yG5d5UaGz1M/yG5d5UaGz1M.info.json

We're in an awkward adolescent phase of AI product (design). But what if this chaotic moment is actually our greatest opportunity? Enter the rebuilding revolution.

In this talk, we'll explore how the current state of AI interfaces offers a once-in-a-career chance to rethink fundamental UX patterns, with practical guidance on avoiding common pitfalls that plague first-generation AI products. 

Learn how to balance technical constraints with user needs, identify which conventional wisdom to keep versus discard, and ship AI experiences that actually delight users rather than frustrate them.

About Raiza Martin
A product leader with a unique lens on AI's user experience challenges, Raiza brings insights from both big tech and startup trenches.

Most recently leading Google's NotebookLM team, she has shaped how millions of users interact with generative AI. Now, as a founder, she is reimagining these experiences from first principles.

With years of hands-on PM experience guiding technical teams through the practical realities of shipping AI products, Raiza offers a rare combination of enterprise-scale perspective and startup-speed execution.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Why your product needs an AI product manager, and why it should be you — James Lowe, i.AI

- Upload date: 2025-07-28
- Video: https://www.youtube.com/watch?v=xzJdSi2Tsqw
- Transcript: raw/20250728_xzJdSi2Tsqw/xzJdSi2Tsqw.en-orig.vtt
- Metadata: raw/20250728_xzJdSi2Tsqw/xzJdSi2Tsqw.info.json

So you've built another cool demo. Now what? You have hype, but not impact. You have kudos but no users. Ultimately you have a demo, but not a product.

The unique uncertainty of AI technology demands a new approach – beyond traditional product management. You need an AI Product Manager. This talk explains why this role is essential for building real AI products, using real case studies from the incubator for Artificial Intelligence in the UK Government.

More importantly, it reveals why your technical depth makes you uniquely suited to step into this critical leadership gap. Discover why could be the ideal candidate to be the AI Product Manager your product needs, and how to step into that role.

About James Lowe
James Lowe has been a data scientist in public sector for 8 years, including working at 10 Downing Street. He is now the Head of AI Engineering for the Incubator for AI, a small team of experts in the centre of the UK Government building AI products that are delivering public good.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Real-time Experiments with an AI Co-Scientist - Stefania Druga, fmr. Google Deepmind

- Upload date: 2025-07-28
- Video: https://www.youtube.com/watch?v=wNH3q9pqn0U
- Transcript: raw/20250728_wNH3q9pqn0U/wNH3q9pqn0U.en-orig.vtt
- Metadata: raw/20250728_wNH3q9pqn0U/wNH3q9pqn0U.info.json

The sheer volume of data and complexity of modern scientific challenges necessitate tools that go beyond mere analysis. The vision of an "AI Co-scientist" – a true collaborative partner in the lab – requires sophisticated engineering to bridge the gap between powerful AI reasoning and the dynamic reality of physical experiments. This talk dives into the engineering required to build robust AI Co-scientists for hands-on research. We will explore scalable architectures, such as multi-agent systems leveraging foundation models like Gemini for complex reasoning, hypothesis refinement (inspired by the "generate, debate, evolve" paradigm described in recent AI Co-scientist research), and intelligent tool use. The core focus will be on the engineering challenges and solutions for integrating diverse, real-time empirical data streams – visual data from cameras, quantitative readings from sensors, positional feedback from actuators, and instrument outputs – directly into the AI's reasoning loop. I will illustrate this with concrete, technically detailed examples in chemistry (adaptive reaction monitoring), robotics (vision-guided assembly with SO Arm 100 and LeRobot library), and synthetic biology (real-time bacterial growth monitoring & interpretation). We'll discuss engineering strategies for handling data heterogeneity, latency, noise, and enabling the AI to interpret, correlate, and act upon live experimental feedback. Finally, we will touch upon how thoughtful engineering of these AI Co-scientists can contribute to democratizing access to advanced scientific capabilities.

About Stefania Druga
Hi! I am Stef. I am an independent researcher, formerly a Research Scientist in Google DeepMind working on novel multimodal AI applications. Previously I was a Principal Researcher in the Center of Applied AI Research at the University of Chicago. I graduated with a Ph.D. in Creative AI Literacies at the University of Washington Information School and have a master in Science from MIT,

My research focuses on Large Language Models and the design of Multimodal AI tools and resources and during grad school I built the first open-source platform for K12 AI Education - Cognimates. When I am not coding & writing papers. I love trail running, yoga, and riding my bike.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## What Is a Humanoid Foundation Model? An Introduction to GR00T N1 - Annika & Aastha

- Upload date: 2025-07-28
- Video: https://www.youtube.com/watch?v=mWKYvT9Lc50
- Transcript: raw/20250728_mWKYvT9Lc50/mWKYvT9Lc50.en-orig.vtt
- Metadata: raw/20250728_mWKYvT9Lc50/mWKYvT9Lc50.info.json

Foundation models don’t just write or draw anymore—they’re starting to move.

GR00T N1 is NVIDIA’s open Vision-Language-Action (VLA) foundation model for humanoid robots. Built with a dual-system architecture, it combines a System 2 module for high-level reasoning with a System 1 module for real-time, fluid motor control. It’s trained end-to-end on a an impressive mix of data—from human videos to robot trajectories to synthetic simulations—and deployed on a full-sized humanoid robot performing bimanual manipulation tasks in the real world.

This talk is a high-level, beginner-friendly overview of GR00T N1:
- What makes a robot foundation model different from an LLM or vision model
- How GR00T’s architecture is inspired by cognitive systems
- Why grounding language, vision, and action together unlocks new generalist capabilities

If you’ve ever wondered how large-scale AI is crossing over into the physical world, this session will get you up to speed—no robotics PhD required.

About Annika Brundyn
Annika Brundyn is a Senior Solutions Architect at NVIDIA focused on deploying generative AI systems in the real world. She works at the intersection of inference infrastructure, reasoning models, and retrieval pipelines, and has contributed to flagship projects like NVIDIA’s NeMo Retriever and the GR00T vision-language-action model. Her experience spans frontier model research and enterprise-grade deployment. She spends a lot of time helping models make fewer “creative” mistakes in production.

About Aastha Jhunjhunwala 
Aastha Jhunjhunwala is a Solutions Architect at NVIDIA, focused on building optimized generative AI applications across industries. She works at the intersection of large-scale LLM pretraining, large language model inference, and NVIDIA’s full-stack generative AI infrastructure. Aastha has helped enterprises scale LLM workflows—from training models with billions of parameters to serving them efficiently with high-throughput inference. When she’s not working with language models, you’ll find her deep in the mountains, trading tokens for trail markers.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Shipping something to someone always wins — Kenneth Auchenberg (ex. Stripe, VSCode)

- Upload date: 2025-07-28
- Video: https://www.youtube.com/watch?v=mHzJhXppwUA
- Transcript: raw/20250728_mHzJhXppwUA/mHzJhXppwUA.en-orig.vtt
- Metadata: raw/20250728_mHzJhXppwUA/mHzJhXppwUA.info.json

Learnings from building products at Stripe and applying them in an AI native word.

About Kenneth Auchenberg
Partner at @alley_corp, investor focused on backing founders building for developers.

Past building at @stripe, VS @Code, @microsoft and a few startups (acq)

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Building the platform for agent coordination — Tom Moor, Linear

- Upload date: 2025-07-28
- Video: https://www.youtube.com/watch?v=UG9IAdmi2Dg
- Transcript: raw/20250728_UG9IAdmi2Dg/UG9IAdmi2Dg.en-orig.vtt
- Metadata: raw/20250728_UG9IAdmi2Dg/UG9IAdmi2Dg.info.json

Learn how we're evolving Linear into an operating system for engineering teams to ship product with agents as a first class citizen.

About Tom Moor
Tom Moor is the Head of Engineering at Linear, a company redefining how modern teams build software. Linear streamlines issue tracking and project management for high-performance teams like Vercel, Ramp, Replit, and Retool.

Tom previously co-founded and scaled multiple SaaS startups including Abstract and Buffer. He draws on over a decade of experience building collaborative tools and design-led products.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Shipping Products When You Don't Know What they Can Do — Ben Stein, Teammates

- Upload date: 2025-07-28
- Video: https://www.youtube.com/watch?v=PthmdT92qNg
- Transcript: raw/20250728_PthmdT92qNg/PthmdT92qNg.en-orig.vtt
- Metadata: raw/20250728_PthmdT92qNg/PthmdT92qNg.info.json

A customer recently asked me: “Hey, can I tag your AI agent in a Google Doc comment?”

The honest answer: I have no idea! We never designed our agents to handle Google Doc comments, but we tried it anyway… and it worked! The agent performed beautifully, the customer was thrilled, and I was left bewildered.

Welcome to Product Management for AI agents, where roadmaps are fuzzy and we only learn the boundaries of our products after they’re released. When a product doesn’t follow predefined requirements but instead learns and improvises at runtime, PMs must give up control and lean into uncertainty, curiosity, experimentation, and fast feedback loops.

This talk is a field guide for Product/Engineering teams navigating this new reality. We’ll cover how to write specs for affordances instead of features, how to use AI evals as a product development tool, and how to perform User Acceptance Testing on undocumented emergent behavior. Most importantly, we’ll explore how to build trust with customers even when the answer is, truthfully, “I don’t know.”

If you’re managing AI-native products in 2025 the same way you managed web apps in 2020, you might find yourself A/B testing an agent that decided to go off and do C, D, and E all by themselves!

About Ben Stein
Ben is a customer-obsessed technology executive and product leader who seamlessly bridges the worlds of business, product, and technology. He has repeated success leading cross-functional teams at multiple lifecycle stages, from 3x startup founder, to scaling through hypergrowth, to managing mature lines of business.

In 7 years at Twilio, Ben was GM of multiple business units (Developer Experience, Enterprise), Product Director for text messaging, and Head of R&D for Twilio.org. As CPTO at Arcadia (climate tech unicorn), he led a global team building APIs to decentralize and decarbonize the electrical grid. He cofounded multiple startups including Mobile Commons (acquired by $UPLD), an early platform for SMS marketing; and QuitCarbon, an AI platform to transition 100M homes off fossil fuels.

He is currently building Teammates, a platform for designing and managing a virtual workforce of truly autonomous virtual colleagues.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Make your LLM app a Domain Expert: How to Build an Expert System — Christopher Lovejoy, Anterior

- Upload date: 2025-07-28
- Video: https://www.youtube.com/watch?v=MRM7oA3JsFs
- Transcript: raw/20250728_MRM7oA3JsFs/MRM7oA3JsFs.en-orig.vtt
- Metadata: raw/20250728_MRM7oA3JsFs/MRM7oA3JsFs.info.json

Vertical AI is a multi-trillion-dollar opportunity. But you can't build a domain-expert application simply by grabbing the latest LLMs off-the-shelf: you need a system for codifying latent insights from domain experts and using that to drive development of your application.

In this talk, we'll describe the system we've built at Anterior which has enabled us to achieve SOTA clinical reasoning and serve health insurance providers covering 50 million American lives. We'll share:
- how and why to encode domain-specific failure modes as an ontology
- a practical system for converting domain expertise into quantifiable eval metrics
- how we structure work and collaboration between our clinicians, engineer and PMs
- our eval-driven AI iteration process and how this can be adapted to any industry


---related links---

https://x.com/chrislovejoy_
https://www.linkedin.com/in/dr-christopher-lovejoy/
https://chrislovejoy.me/
https://www.anterior.com/

## Scaling AI Agents Without Breaking Reliability — Preeti Somal, Temporal

- Upload date: 2025-07-28
- Video: https://www.youtube.com/watch?v=1izYWsokr9s
- Transcript: raw/20250728_1izYWsokr9s/1izYWsokr9s.en-orig.vtt
- Metadata: raw/20250728_1izYWsokr9s/1izYWsokr9s.info.json

As AI agents move from prototypes to production, developers are running into new challenges with orchestration, failure handling, and infrastructure. This session will unpack lessons from teams already building real-world systems and share how to design for reliability from the start.

About Preeti Somal
Preeti is Senior Vice President of Engineering at Temporal. Preeti is passionate about building great products, growing world class organizations and solving complex problems. Prior to Temporal, Preeti led the Platform, Security and IT engineering organizations at HashiCorp. Her extensive career includes engineering leadership roles at Yahoo!, VMware and Oracle. While at Yahoo! Preeti was VP of Cloud Services in the Platform organization delivering highly scalable services used by engineers across Yahoo to build and operate applications with improved agility, reliability and security. These services power Yahoo!’s consumer and advertising business.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## The AI Engineer’s Guide to Raising VC — Dani Grant (Jam), Chelcie Taylor (Notable)

- Upload date: 2025-07-27
- Video: https://www.youtube.com/watch?v=YYNXFsUutbM
- Transcript: raw/20250727_YYNXFsUutbM/YYNXFsUutbM.en-orig.vtt
- Metadata: raw/20250727_YYNXFsUutbM/YYNXFsUutbM.info.json

A no fluff, all tactics discussion. More AI engineers should build startups, the world needs more software. But there’s a way to raise VC and it’s hard to do it if you’ve never seen it done. We are going to walk through the exact playbook to raise your first round of funding. We will show you real pitch decks, real cold emails and real term sheets so when you go out to raise your first round of funding, you are setup to do it. Every AI Engineer should be equip to start their own company and this session makes sure raising $$$ is not going to be the blocker.

About Dani Grant
Dani Grant is the CEO of Jam, a dev tools startup helping 65,000+ improve their bug reporting process, backed by executives from Apple, GitHub, and Vercel, and VCs such as Village Global (LPs include Mark Zuckerberg, Bill Gates, Jeff Bezos). Before Jam, Dani was an early product manager at Cloudflare, where she worked on core developer products such as 1.1.1.1 (now used by 10 million+ people). She also worked as a VC at Union Square Ventures.

About Chelcie Taylor
Leading early stage AI apps investments at Notable Capital ($5B AUM VC).

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Ship Agents that Ship: A Hands-On Workshop - Kyle Penfound, Jeremy Adams, Dagger

- Upload date: 2025-07-27
- Video: https://www.youtube.com/watch?v=Fzb1a24hF-o
- Transcript: raw/20250727_Fzb1a24hF-o/Fzb1a24hF-o.en-orig.vtt
- Metadata: raw/20250727_Fzb1a24hF-o/Fzb1a24hF-o.info.json

Coding agents are transforming how software gets built, tested, and deployed, but engineering teams face a critical challenge: how to embrace this automation wave without sacrificing trust, control, or reliability.

In this 80 minute workshop, you’ll go beyond toy demos and build production-minded AI agents using Dagger, the programmable delivery engine designed for real CI/CD and AI-native workflows. Whether you're debugging failures, triaging pull requests, generating tests, or shipping features, you'll learn how to orchestrate autonomous agents that live in and around your codebase: from your laptop to your CI platform.
We’ll guide you through:

Building real-world agents with Dagger and popular LLMs (GPT, Claude, etc.)

Programming agent environments using real languages (Go, Python, TypeScript)

Executing agent workflows locally and in GitHub Actions, so you can bring them to production

Using a composable runtime that ensures isolation, determinism, traceability, and repeatability

Designing agents that automate and enhance debugging, test generation, code review, bug fixing, and feature implementation

By the end of the workshop, you’ll walk away ready to build your own army of autonomous agents, working collaboratively across your codebase, locally and in CI, accelerating development without ceding control. Let’s build agents that don’t just talk, they ship!

About Kyle Penfound
Kyle is part of the ecosystem team at Dagger working on the future of composable software. He has a background in DevOps and just loves giving demos!

About Jeremy Adams
Jeremy is a senior leader with both a technical and a strategic streak. Passionate about people and entrepreneurship, integration and automation. Through technical/business roles at Dagger, GitHub, Twistlock, and Puppet, Jeremy has both zoomed in and zoomed out a lot, acquiring an appreciation for the details and an ever-broader sense of the big architectural picture.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Strategies for LLM Evals (GuideLLM, lm-eval-harness, OpenAI Evals Workshop) — Taylor Jordan Smith

- Upload date: 2025-07-27
- Video: https://www.youtube.com/watch?v=89NuzmKokIk
- Transcript: raw/20250727_89NuzmKokIk/89NuzmKokIk.en-orig.vtt
- Metadata: raw/20250727_89NuzmKokIk/89NuzmKokIk.info.json

Accuracy scores and leaderboard metrics look impressive—but production-grade AI requires evals that reflect real-world performance, reliability, and user happiness. Traditional benchmarks rarely help you understand how your LLM will perform when embedded in complex workflows or agentic systems. How can you realistically and adequately measure reasoning quality, agent consistency, MCP integration, and user-focused outcomes?

In this practical, example-driven talk, we'll go beyond standard benchmarks and dive into tangible evaluation strategies using various open-source frameworks like GuideLLM and lm-eval-harness. You'll see concrete examples of how to create custom eval suites tailored to your use case, integrate human-in-the-loop feedback effectively, and implement agent reliability checks that reflect production conditions. Walk away with actionable insights and best practices for evaluating and improving your LLMs, ensuring they meet real-world expectations—not just leaderboard positions!
---
Benchmarks and leaderboards are helpful—but they rarely reflect the realities of production AI. Evaluating real-world performance demands deeper insight into reasoning quality, agent reliability, user satisfaction, and integration with agentic systems and MCP (Model Context Protocol).

This hands-on workshop teaches you tangible evaluation methods using popular open-source frameworks (GuideLLM, lm-eval-harness, OpenAI Evals). No prior evaluation expertise required!

You’ll learn how to:

- Build custom evaluation workflows beyond traditional accuracy benchmarks.
- Evaluate reasoning skills, consistency, and reliability in agentic AI applications.
- Integrate human-in-the-loop assessments for better user-aligned outcomes.
- Validate MCP and agent interactions with practical reliability tests.

Whether you're deploying chatbots, copilots, or autonomous AI agents, robust evaluation is critical. Join us to learn actionable strategies to confidently deploy your LLMs in real-world applications.

---related links---

https://www.linkedin.com/in/taylorjordansmith/
https://www.redhat.com/en/products/ai

## Why you should care about AI interpretability - Mark Bissell, Goodfire AI

- Upload date: 2025-07-27
- Video: https://www.youtube.com/watch?v=6AVMHZPjpTQ
- Transcript: raw/20250727_6AVMHZPjpTQ/6AVMHZPjpTQ.en-orig.vtt
- Metadata: raw/20250727_6AVMHZPjpTQ/6AVMHZPjpTQ.info.json

The goal of mechanistic interpretability is to reverse engineer neural networks. Having direct, programmable access to the internal neurons of models unlocks new ways for developers and users to interact with AI — from more precise steering to guardrails to novel user interfaces. While interpretability has long been an interesting research topic, it is now finding real-world use cases, making it an important tool for AI engineers.

About Mark Bissell
Mark Bissell is an applied researcher at Goodfire AI working on real-world applications for mechanistic interpretability. He recently joined Goodfire after 3 years at Palantir, where he worked on various U.S. healthcare initiatives including research projects with the NIH, vaccine distribution during the Covid pandemic (Operation Warp Speed), and AI-enabled hospital operations across many of the nation's leading health systems.

Mark is passionate about translating frontier research into practical solutions. He believes that recent AI developments increase the importance broad skillsets, and that roles of the future will blur the lines between traditionally distinct categories such as engineer, researcher, inventor, designer, and entrepreneur.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Information Retrieval from the Ground Up - Philipp Krenn, Elastic

- Upload date: 2025-07-27
- Video: https://www.youtube.com/watch?v=4Xe_iMYxBQc
- Transcript: raw/20250727_4Xe_iMYxBQc/4Xe_iMYxBQc.en-orig.vtt
- Metadata: raw/20250727_4Xe_iMYxBQc/4Xe_iMYxBQc.info.json

Vector search is only a feature. Search engines and information retrieval have retaken their position as the foundation of RAG. This workshop takes you through decades of research, what has been working for a long time, and how it got better with Machine Learning.

About Philipp Krenn
Philipp leads Developer Relations at Elastic — the company behind the Elasticsearch, Kibana, Beats, and Logstash. Based in San Francisco, he lives to demo interesting technology and solve challenging problems — all with a smile and a terminal window.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## A2A & MCP Workshop: Automating Business Processes with LLMs — Damien Murphy, Bench

- Upload date: 2025-07-26
- Video: https://www.youtube.com/watch?v=wXVvfFMTyzY
- Transcript: raw/20250726_wXVvfFMTyzY/wXVvfFMTyzY.en-orig.vtt
- Metadata: raw/20250726_wXVvfFMTyzY/wXVvfFMTyzY.info.json

Ever wished your webhooks could think for themselves? Join us to discover how A2A agents can transform passive webhook endpoints into intelligent workflow processors.

In this session, we'll show you how to build a system that automatically spawns AI Agents to handle incoming webhooks.

Using Google's Agent-to-Agent framework and MCP, you'll learn how to create dynamic AI agents that respond to events, communicate with external services, and make decisions based on content analysis.

See the future of workflow automation where webhooks don't just trigger actions—they trigger intelligence!

About Damien Murphy
Full Stack Dev for 20+ years focusing on AI Agents

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Waymo's EMMA: Teaching Cars to Think - Jyh Jing Hwang, Waymo

- Upload date: 2025-07-26
- Video: https://www.youtube.com/watch?v=iS9YFW28XyM
- Transcript: raw/20250726_iS9YFW28XyM/iS9YFW28XyM.en-orig.vtt
- Metadata: raw/20250726_iS9YFW28XyM/iS9YFW28XyM.info.json

This session explores Waymo's latest research on the End-to-End Multimodal Model for Autonomous Driving (EMMA) and advanced sensor simulation techniques. Jyh-Jing Hwang will demonstrate how multimodal large language models like Gemini could improve autonomous driving through unified end-to-end architectures that process raw sensor data directly into driving decisions.

The presentation will showcase EMMA's state-of-the-art performance in trajectory planning, 3D object detection, and road graph understanding, as well as another Drive&Gen research approach to sensor simulation for evaluating an end-to-end motion planning model. Attendees will gain insights into the benefits of co-training across multiple autonomous driving tasks and the potential of controlled video generation for testing under various environmental conditions.

More on EMMA here: https://waymo.com/blog/2024/10/introducing-emma

About Jyh Jing Hwang
Jyh-Jing is currently a Research Scientist and TLM at Waymo Research. He also taught machine learning and computer vision as a lecturer at UPenn MCIT Online in 2022 and 2023. Before joining Waymo in 2020, Jyh-Jing received his Ph.D. degree in Computer and Information Science from University of Pennsylvania, advised by Prof. Jianbo Shi and Prof. Stella Yu at UC Berkeley / ICSI. Before coming to the U.S., he received the B.S. and M.S. degrees from National Taiwan University and worked with Dr. Tyng-Luh Liu at Academia Sinica. His research interests are broadly in artificial intelligence, computer vision, and machine learning. Particularly, he's interested in end-to-end autonomous driving, large multimodal models, general image/video structures, and sensor fusion for robust perception.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Robotics: why now? - Quan Vuong and Jost Tobias Springberg, Physical Intelligence

- Upload date: 2025-07-26
- Video: https://www.youtube.com/watch?v=cGLa8DsOYdk
- Transcript: raw/20250726_cGLa8DsOYdk/cGLa8DsOYdk.en-orig.vtt
- Metadata: raw/20250726_cGLa8DsOYdk/cGLa8DsOYdk.info.json

Sharing recent progress from Physical Intelligence and why it is an exciting time to push the frontier in general purpose robotics

About Quan Vuong
Quan Vuong is co-founder at Physical Intelligence. His research focuses on generalist robotics and algorithms that enable intelligent behaviors through large scale learning.

About Jost Tobias Springenberg
Tobias is currently a research scientist at Physical Intelligence where he works on bringing AI into the real world and understanding the fundamentals of sequential decision making (e.g. imitation and reinforcement learning). He likes his machine learning models big and his data to be plentiful and focuses most of his research on engineering driven machine learning at scale for robotics.
Before joining Physical Intelligence Tobias was a research scientist Google Deepmind in London within the control team which generally focuses on applications of ML to control for science and robotics. Before that he was a researcher at the University of Freiburg working with the Machine Learning Group and Computer Vision Groups. Tobias holds a BSc. in Cognitive Science from the University of Osnabrueck – from which he still retains an interest in understanding human cognition – and a MSc. in Computer Science from the University of Freiburg.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Piloting agents in GitHub Copilot - Christopher Harrison, Microsoft

- Upload date: 2025-07-26
- Video: https://www.youtube.com/watch?v=DdaAABdAqZY
- Transcript: raw/20250726_DdaAABdAqZY/DdaAABdAqZY.en-orig.vtt
- Metadata: raw/20250726_DdaAABdAqZY/DdaAABdAqZY.info.json

The agent capabilities added to GitHub Copilot have enhanced its ability to act as a peer programmer. Copilot can now discover and generate code based on existing standards, run tests, recover from errors, and call tools using Model Context Protocol (MCP). This workshop will guide you through piloting Copilot's agent capabilities and how to best integrate with the most widely adopted AI coding assistant in the world.

Key takeaways include:

- Understanding how and when to bring agents into your software development workflow
- Providing context through the use of custom instructions and prompt files to ensure consistency across your team
- Discovering how MCP provides access to an additional set of external tools and capabilities that the agent can use
- Configuring Copilot's agentic capabilities to take advantage of your custom MCP server
- Recommended best practices to help your responsibly accelerate your development while maintaining code quality and governance

About Christopher Harrison
Christopher is a long-time geek who's spent the bulk of his career training, supporting and upskilling developers. He's a web developer at heart with passions which span from Python to DevOps to TypeScript to AI. In his current role as an Enterprise Advocate for GitHub he seeks to help organizations improve their DevOps process and culture. When not found writing code he can be found running, playing Civilization, or spending time with his partner and their four-legged child (a rescue mutt).

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Introduction to LLM serving with SGLang - Philip Kiely and Yineng Zhang, Baseten

- Upload date: 2025-07-26
- Video: https://www.youtube.com/watch?v=Ahtaha9fEM0
- Transcript: raw/20250726_Ahtaha9fEM0/Ahtaha9fEM0.en-orig.vtt
- Metadata: raw/20250726_Ahtaha9fEM0/Ahtaha9fEM0.info.json

Do you want to learn how to serve models like DeepSeek and Qwen with SOTA speeds on launch day? SGLang is an open-source fast serving framework for LLMs and VLMs that generates trillions of tokens per day at companies like xAI, AMD, and Meituan. This workshop guides AI engineers who are familiar with serving models using frameworks like vLLM, Ollama, and TensorRT-LLM through deploying and optimizing their first model with SGLang, as well as providing guidance on when SGLang is the appropriate tool for LLM workloads.

About Philip Kiely
Philip Kiely leads Developer Relations at Baseten. Prior to joining Baseten in 2022, he worked across software engineering and technical writing for a variety of startups. Outside of work, you'll find Philip practicing martial arts, reading a new book, or cheering for his adopted bay area sports teams.

About Yineng Zhang
Yineng Zhang is a Software Engineer at Baseten Model Performance team. He is also a core developer of the SGLang project.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

00:00 Introduction to LLM serving with SGLang
02:14 What is SGLang?
03:36 History of SGLang
06:49 Deploying Your First Model
13:01 Optimizing Performance with CUDA Graph Max Batch Size
24:19 Optimizing Performance with Eagle 3 Speculative Decoding
30:02 SGLang Community and Contributions
35:24 Invitations and Job Opportunities
36:52 Q&A

## Beyond the Prototype: Using AI to Write High-Quality Code - Josh Albrecht, Imbue

- Upload date: 2025-07-25
- Video: https://www.youtube.com/watch?v=x_1EumTaXeE
- Transcript: raw/20250725_x_1EumTaXeE/x_1EumTaXeE.en-orig.vtt
- Metadata: raw/20250725_x_1EumTaXeE/x_1EumTaXeE.info.json

In this case study-based keynote, Josh Albrecht, CTO of Imbue, examines the critical engineering challenges in building AI coding systems that create more than just prototypes. Drawing from Imbue's research developing Sculptor, an experimental coding agent environment, Josh shares key insights into the fundamental technical obstacles encountered when evolving AI-assisted coding from toy applications to more robust software systems. 

The session will explore approaches to core challenges like safely executing code, managing context across large codebases, automating test generation, and creating systems that can identify potential pitfalls in AI-generated code. Attendees will gain practical insights into the technical underpinnings of next-generation coding agents that aim to handle complex software engineering challenges architecting larger systems, increasing meaningful test coverage and designing systems that are easy to debug—moving us closer to AI systems that can help create maintainable software.

About Josh Albrecht
Josh Albrecht is CTO and Co-founder of Imbue, an AI lab launched in 2022 that has since raised $230M at a $1B valuation to create coding agents that make it easier for more people to write software. Josh is also a partner at angel fund Outset Capital, where he invests in promising pre-seed companies. Previously, Josh founded multiple companies including an AI recruiting startup that went through Y Combinator and a 3D injection molding software company that was acquired. He was also an early engineer at Addepar, served as a Thiel Fellow mentor, and published machine learning research as an academic researcher.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Software Development Agents: What Works and What Doesn't - Robert Brennan, OpenHands

- Upload date: 2025-07-25
- Video: https://www.youtube.com/watch?v=o_hhkJtlbSs
- Transcript: raw/20250725_o_hhkJtlbSs/o_hhkJtlbSs.en-orig.vtt
- Metadata: raw/20250725_o_hhkJtlbSs/o_hhkJtlbSs.info.json

The adoption of AI into software development has been bumpy. While autocomplete tools like Copilot have gone mainstream, autonomous agents like Devin and OpenHands have generated both enthusiasm and skepticism. Some engineers claim they generate a 10x productivity boost; others that they just create noise and tech debt.

The difference between the enthusiasts and the skeptics is that the enthusiasts have reasonable expectations for what these agents can do, and have both practical and intuitive knowledge for how to use them effectively.

In this session, we'll talk about what tasks are appropriate for today's software agents, what tasks they might start to succeed at in 2025, and what tasks are best left to humans no matter how good they get.

Session Outline:
Learn how to use software development agents like OpenHands (fka OpenDevin) effectively, without creating noise and tech debt.


---related links---

https://x.com/rbren_dev
https://linkedin.com/in/robert-a-brennan
https://www.openhands.dev/blog
https://www.openhands.dev

## Human seeded Evals — Samuel Colvin, Pydantic

- Upload date: 2025-07-25
- Video: https://www.youtube.com/watch?v=o_LRtAomJCs
- Transcript: raw/20250725_o_LRtAomJCs/o_LRtAomJCs.en-orig.vtt
- Metadata: raw/20250725_o_LRtAomJCs/o_LRtAomJCs.info.json

In this talk I'll introduce the concept of Human-seeded Evals, explain the principle and demo them with Pydantic Logfire.

---related links---

https://x.com/samuel_colvin
https://www.linkedin.com/in/samuel-colvin/
https://github.com/samuelcolvin
https://pydantic.dev/

## Ship Production Software in Minutes, Not Months — Eno Reyes, Factory

- Upload date: 2025-07-25
- Video: https://www.youtube.com/watch?v=iheWKg2Tkrk
- Transcript: raw/20250725_iheWKg2Tkrk/iheWKg2Tkrk.en-orig.vtt
- Metadata: raw/20250725_iheWKg2Tkrk/iheWKg2Tkrk.info.json

Planning, coding, testing, monitoring—the endless cycle that spans 10+ tools that fragment our focus and slows delivery to a crawl. Vibe coding doesn't work when you've got 10TB of code. If you just sighed, you're one of many professional software engineers trapped in the traditional software development lifecycle (SDLC) that was designed before AI could parallelize your entire workflow.

But what if you could orchestrate multiple AI agents on tasks beyond just generating code, while you focus on the creative decisions that matter?

In this talk, I'll demonstrate how real enterprise organizations are changing their entire SDLC—going from understanding, planning, coding, and testing all the way to incident response—using AI agents. You'll witness the next evolution of software engineering—where AI doesn't just generate code, but orchestrates the entire development lifecycle.

About Eno Reyes
Eno Reyes is cofounder and CTO of Factory, a platform that accelerates enterprise software development with autonomous AI agents and unified context from across your engineering tools. Enterprises are using Factory to accelerate everything from bug-fixing and coding to PRD creation, release automation, migrations, and more.

Prior to Factory, he was an ML engineer at Hugging Face working on enterprise LLMs.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Your Coding Agent Just Got Cloned And Your Brain Isn't Ready - Rustin Banks, Google Jules

- Upload date: 2025-07-25
- Video: https://www.youtube.com/watch?v=X4BwOu0GWb8
- Transcript: raw/20250725_X4BwOu0GWb8/X4BwOu0GWb8.en-orig.vtt
- Metadata: raw/20250725_X4BwOu0GWb8/X4BwOu0GWb8.info.json

Will the future engineer code alongside a single coding agent, or will they spend their day orchestrating many agents? Traditional development rewards synchronous focus. This session dives into the significant mindshift required to move from sequential coding to orchestrating parallel agents. We are the builders of ""Jules"", Google's massively parallel asynchronous coding agent (to be opened up in May). We'll share real-world insights from building Jules and explore how to rewire your brain for this powerful new ""post-IDE"" development paradigm.

About Rustin Banks
I'm Rustin, an AI Product Manager at Google Labs. I taught myself to program at age 12 using a compiler I purchased on AOL classifieds. As a teenager I hosted a popular bulletin board system (BBS) out of my cousin’s closet using salvaged 286 computers. I’ve always had a passion for making the world better using technology. When I saw AI write code I dedicated the rest of my career to AI coding. At Google labs I am lucky to explore the frontier of coding models and agents.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Devin 2.0 and the Future of SWE - Scott Wu, Cognition

- Upload date: 2025-07-25
- Video: https://www.youtube.com/watch?v=MI83buT_23o
- Transcript: raw/20250725_MI83buT_23o/MI83buT_23o.en-orig.vtt
- Metadata: raw/20250725_MI83buT_23o/MI83buT_23o.info.json

A talk on the future of software engineering with Scott Wu of Cognition AI, the makers of Devin.

About Scott Wu
Scott is the co-founder and CEO of Cognition AI. He previously competed in international programming competitions (3x IOI gold medalist) and co-founded Lunchclub, an AI-powered professional networking platform. Scott grew up in Louisiana and attended Harvard University.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Latent Space Paper Club: AIEWF Special Edition (Test of Time, DeepSeek R1/V3) — VIbhu Sapra

- Upload date: 2025-07-25
- Video: https://www.youtube.com/watch?v=9k3xPh-40mo
- Transcript: raw/20250725_9k3xPh-40mo/9k3xPh-40mo.en-orig.vtt
- Metadata: raw/20250725_9k3xPh-40mo/9k3xPh-40mo.info.json

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

Timestamps:

00:00:00 Paper Club Year in Review & Future Plans

00:08:00 DeepSeek Paper Discussion

00:09:10 DeepSeek R1 (May 28th Update)

00:12:40 DeepSeek Distillation

00:16:51 Original DeepSeek Model Overview (DeepSeek V3 and R1)

00:21:15 Development of reasoning capabilities through a pure RL process

00:24:46 DeepSeek R10

00:39:05 DeepSeek R1 four-stage training pipeline

00:35:01 Emergence of "reflection moments" and "aha moments"

00:44:15 Distillation Strategy

00:52:34 Community and Call to Action

## How to build Enterprise Aware Agents - Chau Tran, Glean

- Upload date: 2025-07-24
- Video: https://www.youtube.com/watch?v=hxFpUcvWPcU
- Transcript: raw/20250724_hxFpUcvWPcU/hxFpUcvWPcU.en-orig.vtt
- Metadata: raw/20250724_hxFpUcvWPcU/hxFpUcvWPcU.info.json

While LLMs demonstrated impressive reasoning capabilities, their out-of-the-box reasoning is akin to hiring a brilliant but brand-new employee who doesn’t have the enterprise context of “how things are done at this company”. In this talk, I'll introduce “Workflow Search” as a paradigm to build enterprise-aware agents that can balance predictability on common tasks, and flexibility on unforeseen tasks.

About Chau Tran
Chau Tran is a Software Engineer at Glean, currently leading the technical work on Glean Assistant and semantic search. They have been with Glean for over 3 years and have a history of impactful contributions in engineering teams. Previously, Chau worked as a Research Engineer at FAIR within Meta and held technical roles at Quora. They graduated from Brown University with a Bachelor's degree in Computer Science.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Building AI Products That Actually Work — Ben Hylak (Raindrop), Sid Bendre (Oleve)

- Upload date: 2025-07-24
- Video: https://www.youtube.com/watch?v=eSvXbb2EBYc
- Transcript: raw/20250724_eSvXbb2EBYc/eSvXbb2EBYc.en-orig.vtt
- Metadata: raw/20250724_eSvXbb2EBYc/eSvXbb2EBYc.info.json

You've made the demo. How do you make the product? A lot of AI products don't actually work. Even worse, a lot of the techniques being advertised for making AI products better don't work either. We'll cover the challenges + techniques we've seen actually work in the real world.

About Ben Hylak
Ben Hylak is co-founder at Raindrop, building Sentry for AI products. He was previously a designer at Apple for 4 years, building the Apple Vision Pro.

About Sid Bendre
Sid Bendre is the co-founder of Oleve, a company building a portfolio of iconic consumer software across multiple verticals. With a lean team, Oleve has already launched two virally successful consumer AI products that have amassed over 250 million views across social media platforms. One of their products reached #4 on the App Store's Education charts in 2024 and #5 in 2025, competing alongside giants like Photomath (Google) and Duolingo. Backed by Neo, Cal Henderson (co-founder of Slack), Russell Kaplan (President of Cognition), and Maria Zhang (ex-CTO of Tinder), Oleve is building the AI infrastructure to run a $1B portfolio of consumer software over the next decade. At Oleve, Sid leads technical and AI efforts, running the “Platform” team responsible for the underlying AI infrastructure that powers their lean scaling approach. Before Oleve, Sid led AI experimentation efforts at a startup hedge fund and worked at Slack, Zendesk, and Microsoft.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## AX is the only Experience that Matters - Ivan Burazin, Daytona

- Upload date: 2025-07-24
- Video: https://www.youtube.com/watch?v=e9sLVMN76qU
- Transcript: raw/20250724_e9sLVMN76qU/e9sLVMN76qU.en-orig.vtt
- Metadata: raw/20250724_e9sLVMN76qU/e9sLVMN76qU.info.json

If you’re building devtools for humans, you’re building for the past. 

Already a quarter of Y Combinator’s latest batch used AI to write 95% or more of their code. AI agents are scaling at an exponential rate and soon, they’ll outnumber human developers by orders of magnitude.


The real bottleneck isn’t intelligence. It’s tooling. Terminals, local machines, and dashboards weren’t built for agents. They make do… until they can’t.

In this talk, I’ll share how we killed the CLI at Daytona, rebuilt our infrastructure from first principles, and what it takes to build devtools that agents can actually use. Because in an agent-native future, if agents can’t use your tool, no one will.

About Ivan Burazin
Ivan Burazin co-founded Codeanywhere, the very first cloud IDE, back in 2009 where he and the team had to create everything from scratch, from the IDE itself, to the entire orchestration. Concurrently, he established Shift, the premier developer conference in Europe, which was later acquired by Infobip - a global communications cloud giant in 2021. Following the acquisition, Ivan served on the executive board of this 4,000-person company and as the Chief Developer Experience Officer, where he oversaw global developer-oriented operations.

In 2023, Ivan co-founded Daytona, a fast-growing open-source platform addressing the limitations of AI coding agents by enabling them to programmatically and securely interact with runtime environments.

Backed by $7M in funding, Daytona empowers developers, from startups to Fortune 500 companies to enable AI agents to achieve their full potential.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Mentoring the Machine — Eric Hou, Augment Code

- Upload date: 2025-07-24
- Video: https://www.youtube.com/watch?v=Zniw5c9_jx8
- Transcript: raw/20250724_Zniw5c9_jx8/Zniw5c9_jx8.en-orig.vtt
- Metadata: raw/20250724_Zniw5c9_jx8/Zniw5c9_jx8.info.json

You’d never let a swarm of fresh interns ship to prod on day one—same deal with AI agents. Mentoring the Machine dives into how acting like a tech lead (not just a user) turns those bots into real leverage. In this talk, Eric will deliver practical advice for working with AI agents in the SDLC. He'll also preview how effective use of AI agents changes the calculus of software engineering at both a micro and macro level.



---related links---

## AI That Pays: Lessons from Revenue Cycle — Nathan Wan, Ensemble Health

- Upload date: 2025-07-24
- Video: https://www.youtube.com/watch?v=TquUsN1QsWs
- Transcript: raw/20250724_TquUsN1QsWs/TquUsN1QsWs.en-orig.vtt
- Metadata: raw/20250724_TquUsN1QsWs/TquUsN1QsWs.info.json

While much of the AI innovation in healthcare has centered on clinical and patient-facing applications, Revenue Cycle Management (RCM) remains an underexplored yet critical domain. Given the growing financial pressures facing providers, rethinking how healthcare gets paid is essential to ensuring access and sustainability. The combination of which makes RCM an opportune area for AI disruption.

This session explores how the combination of vast structured and unstructured data, often rule-based workflows, and direct financial opportunity to drive meaningful outcomes. We’ll also share practical lessons from our journey evolving a traditional machine learning mindset to incorporate the latest advances in Generative AI, and how that shift is reshaping what's possible in healthcare operations.

---related links---

https://www.linkedin.com/in/nwan1/

## Structuring a modern AI team — Denys Linkov, Wisedocs

- Upload date: 2025-07-24
- Video: https://www.youtube.com/watch?v=SbUxRluVRwk
- Transcript: raw/20250724_SbUxRluVRwk/SbUxRluVRwk.en-orig.vtt
- Metadata: raw/20250724_SbUxRluVRwk/SbUxRluVRwk.info.json

You've been given an AI mandate but don't have additional headcount, what next? Re-skilling, up-skilling and team augmentation become essential to delivering on a new mandate. In this talk we'll cover strategies to structure cross functional AI teams with domain experts, software engineers and ML engineers. We'll cover key skills and milestones that each traditional role can contribute to in unique ways.


---related links---

https://www.linkedin.com/in/denyslinkov/

Timestamps
00:00:00 - Introduction to Hiring a Modern AI Team

00:01:10 - The Anatomy of an AI Team and Company Types

00:03:38 - Technology as an Enabler, Not a Limiter

00:03:56 - Do You Need to Hire an AI Researcher?

00:04:33 - Ampere's Wager: Team vs. Researchers

00:05:07 - What an AI Team Needs to Do

00:06:12 - Identifying Your Bottleneck

00:06:48 - The Evolution of a Generalist

00:07:03 - Building the First Machine Learning Team

00:07:53 - Prioritizing Skills: Model Training, Serving, and Business Acumen

00:09:16 - Building the Second AI Team with Advanced Open Source Tools

00:10:45 - Reskilling and Upskilling Existing Teams

00:10:55 - Inner and Outer Loops of Team Activities

00:11:53 - Winning with Generalists in Early AI Strategy

00:12:46 - Upskilling, Reskilling, and Hiring for the AI Wave

00:14:11 - When and Who to Hire

00:15:08 - Verifying Trends and First Principles in Hiring

00:16:00 - Asking Relevant Questions in Interviews

00:16:12 - Reconsidering Ampere's Wager and Final Lessons

## Building Applications with AI Agents — Michael Albada, Microsoft

- Upload date: 2025-07-24
- Video: https://www.youtube.com/watch?v=R30col3UPUg
- Transcript: raw/20250724_R30col3UPUg/R30col3UPUg.en-orig.vtt
- Metadata: raw/20250724_R30col3UPUg/R30col3UPUg.info.json

Generative AI has dramatically shortened the distance between ideas and implementation, enabling faster prototyping and deployment than ever before. But while language models can streamline individual tasks, true transformation comes from combining these capabilities into intelligent, autonomous systems—AI agents.

This talk explores how to build and deploy foundation model-enabled agent systems that go beyond simple prompt chaining or chatbots. Drawing from real-world implementations and the latest research, it offers a clear and practical path to designing both single-agent and multi-agent systems capable of handling complex workflows with minimal oversight.

Attendees will gain a deeper understanding of the core design principles behind agentic systems, the architectural trade-offs involved in orchestrating multiple agents, and the strategies required to develop tailored solutions that enhance efficiency and innovation. Whether just beginning or scaling up, participants will leave with actionable insights to navigate the rapidly evolving world of AI autonomy.


---related links---

https://x.com/michaelalbada
https://www.linkedin.com/in/albada/
https://theneuralnexus.substack.com/
https://michaelalbada.com

Timestamps
00:00 - Introduction by Michael Albada, Principal Applied Scientist at Microsoft.

01:14 - The Promise and Obstacles of Agentic Development.

02:37 - Defining What an AI Agent Is (and Isn't).

04:42 - Core Component 1: Tool Use and Function Calling.

06:37 - Core Component 2: Orchestration Patterns (Chains, Trees, Agentic).

08:47 - Core Component 3: Multi-Agent Systems.

09:43 - Common Pitfall 1: Insufficient Evaluation.

11:25 - Overview of specific Evaluation Tools.

12:57 - Common Pitfall 2: Lack of Observability.

13:50 - Other Common Pitfalls (Tool issues, complexity).

14:45 - The Critical Importance of Security and Safety.

15:15 - Conclusion and Future Outlook.

## Rise of the AI Architect — Clay Bavor, Cofounder, Sierra w/ Alessio Fanelli

- Upload date: 2025-07-24
- Video: https://www.youtube.com/watch?v=C3geUfBR2js
- Transcript: raw/20250724_C3geUfBR2js/C3geUfBR2js.en-orig.vtt
- Metadata: raw/20250724_C3geUfBR2js/C3geUfBR2js.info.json

As the amount of consumer facing AI products grows, the most forward leaning enterprises have created a new role: the AI Architect. These leaders are responsible for helping define, manage, and evolve their company's AI agent experiences over time.

In this session, Clay Bavor (Cofounder of Sierra) will join Alessio Fanelli (co-host of Latent Space) in a fireside chat to share what it means to be an AI Architect, success stories from the market, and the future of the role.


Timestamps
00:00 Introduction to Sierra and its mission
02:11 The concept of an "AI Architect"
05:13 Backgrounds of successful AI Architects
06:08 Traits of successful AI Architects and AI strategy
08:56 Build vs. buy fallacies in AI agent development
11:36 The agent building iteration process and testing
14:09 Staying up to date on AI model capabilities
16:47 The future of AI interfaces and hardware

## The Rise of Open Models in the Enterprise — Amir Haghighat, Baseten

- Upload date: 2025-07-24
- Video: https://www.youtube.com/watch?v=3WV1vT0B0cg
- Transcript: raw/20250724_3WV1vT0B0cg/3WV1vT0B0cg.en-orig.vtt
- Metadata: raw/20250724_3WV1vT0B0cg/3WV1vT0B0cg.info.json

This year kicked off with the DeepSeek-R1 news cycle breaking out of our AI Engineering bubble into the mainstream tech and business world. Leaders at the highest levels of the largest enterprises started asking how open source models could enhance and accelerate their AI strategy.

Open source models promise increased ownership of AI systems: control over performance and price, improved uptime and reliability, better compliance, and flexible hosting options. How are these promises playing out after months of implementation? In this talk, I’ll draw on hundreds of conversations with AI leaders at enterprise companies to discuss what has — and hasn’t — changed about enterprise AI strategy in a world where open-source models compete on the frontier of intelligence.


---related links---

http://twitter.com/amiruci
https://www.linkedin.com/in/amirhaghighat/
https://www.baseten.co/blog/
https://www.baseten.co/

## Machines of Buying and Selling Grace - Adam Behrens, New Generation

- Upload date: 2025-07-23
- Video: https://www.youtube.com/watch?v=zlZz0mDF2eg
- Transcript: raw/20250723_zlZz0mDF2eg/zlZz0mDF2eg.en-orig.vtt
- Metadata: raw/20250723_zlZz0mDF2eg/zlZz0mDF2eg.info.json

How to go beyond browser automation to truly agentic commerce, where AI can buy, sell and negotiate on behalf of users and merchants.

About Adam Behrens
Adam Behrens is the co-founder and CEO of New Gen, a company that partners with global brands and merchants to unlock AI native commerce opportunities. New Gen builds infrastructure for brands to host their own conversational AI experiences and to connect their data into 3rd party chat clients like ChatGPT and Claude. Adam previously worked on trading infrastructure at Bridgewater and Banking-as-a-Service at Stripe. Outside of training AI models he is busy training his 8 month old Vizsla puppy.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## POC to PROD: Hard Lessons from 200+ Enterprise GenAI Deployments - Randall Hunt, Caylent

- Upload date: 2025-07-23
- Video: https://www.youtube.com/watch?v=vW8wLsb3Nnc
- Transcript: raw/20250723_vW8wLsb3Nnc/vW8wLsb3Nnc.en-orig.vtt
- Metadata: raw/20250723_vW8wLsb3Nnc/vW8wLsb3Nnc.info.json

The transition from experimental GenAI demonstrations to robust, production-grade systems involves significant technical and organizational complexities. Humans provide a ceiling on the true ROI of automations. This session synthesizes key patterns and practical strategies gathered from more than 200 GenAI implementations across multiple industries and business sizes.

Beyond the general lessons that apply to most products leveraging GenAI, we'll cover detailed observations within three application areas: multimodal understanding and search, enterprise knowledge retrieval, and AI agent architectures. We will share real-world comparative performance data and metrics on embedding models, vector index implementations, and explore various implementation methodologies that balance performance and cost.

Additionally, the session addresses organizational insights critical to successful AI deployments, such as the importance of clearly defined evaluation processes and understanding real-world user interaction challenges, highlighted by examples from healthcare environments. Attendees will gain an understanding of decision-making criteria, including the appropriate complexity of prompt engineering versus more elaborate orchestration methods, token/cost management strategies in multilingual settings, and the challenges in driving behavioral change with new UX and application interaction capabilities.

Participants will leave equipped with practical, data-supported insights for effectively navigating their own GenAI projects, including benchmarks and criteria for informed technology selection, and techniques to streamline the transition from initial concept to sustainable operational deployment. Please note, we all know this field evolves rapidly and we will mark which lessons we believe are immutable.

About Randall Hunt
Randall Hunt is a technology leader, investor, and hands-on keyboard coder based in Los Angeles, CA. Previously, Randall led software and developer relations teams at Facebook, SpaceX, AWS, MongoDB, and NASA. Randall spends most of his time listening to customers, building demos, writing blog posts, and mentoring junior engineers. Python and C++ are his favorite programming languages, but he begrudgingly admits that Javascript rules the world. Outside of work, Randall loves to read science fiction, advise startups, travel, and ski.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Does AI Actually Boost Developer Productivity? (100k Devs Study) - Yegor Denisov-Blanch, Stanford

- Upload date: 2025-07-23
- Video: https://www.youtube.com/watch?v=tbDDYKRFjhk
- Transcript: raw/20250723_tbDDYKRFjhk/tbDDYKRFjhk.en-orig.vtt
- Metadata: raw/20250723_tbDDYKRFjhk/tbDDYKRFjhk.info.json

Forget vendor hype: Is AI actually boosting developer productivity, or just shifting bottlenecks? Stop guessing.

Our study at Stanford cuts through the noise, analyzing real-world productivity data from nearly 100,000 developers across hundreds of companies. We reveal the hard numbers: while the average productivity boost is significant (~20%), the reality is complex – some teams even see productivity decrease with AI adoption.

The crucial insights lie in why this variance occurs. Discover which company types, industries, and tech stacks achieve dramatic gains versus minimal impact (or worse). Leave with the objective, data-driven evidence needed to build a winning AI strategy tailored to your context, not just follow the trend.

About Yegor Denisov-Blanch
Researcher at Stanford University researching all things developer productivity

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter


----

The main thesis of the video is that while AI does increase developer productivity, it is not a one-size-fits-all solution. The speaker, Yegor Denisov-Blanch from Stanford, presents findings from a large-scale study on software engineering productivity to support this claim, arguing that the effectiveness of AI in software development is highly dependent on a variety of factors including task complexity, codebase maturity, language popularity, and codebase size.

timestamps:

- 00:00 Introduction and the context of AI in software development, including Mark Zuckerberg's bold claims.
- 04:37 Limitations of existing studies on AI's impact on developer productivity.
- 07:19 The methodology used by the Stanford research group to measure productivity.
- 09:50 The overall impact of AI on developer productivity, including the concept of "rework."
- 11:42 How productivity gains vary by task complexity and project maturity (Greenfield vs. Brownfield).
- 14:21 The impact of programming language popularity on AI's effectiveness.
- 15:42 How codebase size affects AI-driven productivity gains.
- 17:22 The final conclusions of the study.

## How to Build Planning Agents without losing control - Yogendra Miraje, Factset

- Upload date: 2025-07-23
- Video: https://www.youtube.com/watch?v=sl3icG-IjHo
- Transcript: raw/20250723_sl3icG-IjHo/sl3icG-IjHo.en-orig.vtt
- Metadata: raw/20250723_sl3icG-IjHo/sl3icG-IjHo.info.json

LLMs are getting smarter—but Agents are still unpredictable, unreliable, and hard to control.

In this talk, I’ll share practical lessons from building real-world plan-and-execute agents —covering how to steer autonomous agents using agentic workflows, blueprints, and evals.

If you’re struggling to make your agents behave (without giving up flexibility), this one’s for you.

About Yogendra Miraje
I'm a backend engineer turned ML engineer turned AI engineer, with 16 years of experience building intelligent systems. I hold a Master’s degree in Computer Science from Northeastern University in Boston, and I currently work as an AI Engineer in FactSet.

I'm also the host of AI Blindspot, a podcast where we explore the frontiers of artificial intelligence—and the blind spots we often overlook in its development and deployment.

With a strong foundation in Machine Learning and software Engineering and a product-minded approach, I focus on aligning autonomous agents with real-world user goals, emphasizing safety, control, and robust evaluation techniques.

I'm passionate about building AI that’s not just powerful, but grounded, aligned, and truly useful in practice.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## 3 ingredients for building reliable enterprise agents - Harrison Chase, LangChain/LangGraph

- Upload date: 2025-07-23
- Video: https://www.youtube.com/watch?v=kTnfJszFxCg
- Transcript: raw/20250723_kTnfJszFxCg/kTnfJszFxCg.en-orig.vtt
- Metadata: raw/20250723_kTnfJszFxCg/kTnfJszFxCg.info.json

It's easy to build a prototype of an agent, but hard to put an agent in production - especially in an enterprise setting. In this section, will talk about three ingredients for building reliable agents in the enterprise.

About Harrison Chase
Harrison Chase is the CEO and co-founder of LangChain, a company formed around the popular open source Python/Typescript packages. The goal of LangChain is to make it as easy as possible to use LLMs to develop context-aware reasoning applications. Prior to starting LangChain, he led the ML team at Robust Intelligence (an MLOps company focused on testing and validation of machine learning models), led the entity linking team at Kensho (a fintech startup), and studied stats and CS at Harvard.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## From Copilot to Colleague: Trustworthy Agents for High-Stakes - Joel Hron, CTO Thomson Reuters

- Upload date: 2025-07-23
- Video: https://www.youtube.com/watch?v=kDEvo2__Ijg
- Transcript: raw/20250723_kDEvo2__Ijg/kDEvo2__Ijg.en-orig.vtt
- Metadata: raw/20250723_kDEvo2__Ijg/kDEvo2__Ijg.info.json

This keynote will explore what it takes to move from basic generative assistants to fully agentic AI—systems that don’t just suggest but plan, act, and adapt—all within the structured, high-trust environments where professionals actually work.

About Joel Hron
Joel Hron is a passionate innovator driving the future of product technology and AI at Thomson Reuters. As Chief Technology Officer, he leads Product Engineering and AI Research & Development, pushing the boundaries of what’s possible in Legal, Tax, Audit, Trade, Compliance, and Risk solutions.

Joel joined Thomson Reuters in 2022 through the acquisition of ThoughtTrace, where he served as CTO. Previously, he led AI and TR Labs, launching seven groundbreaking GenAI products in just 18 months, transforming legal research, tax analysis, and contract drafting.

His approach is centered on rethinking processes through technology, building teams rooted in trust, transparency, and customer-centric innovation. Joel envisions AI not as a replacement for human expertise, but as a force that enhances professional decision-making, making expert information more accessible and impactful.

A New Orleans native, Joel’s global career spans work in London and Africa, and he now calls Zug, Switzerland home. He holds a Master’s in Mechanical Engineering from the University of Texas at Austin and a Bachelor’s in Engineering from Texas Christian University.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Building Agents (the hard parts!) - Rita Kozlov, Cloudflare

- Upload date: 2025-07-23
- Video: https://www.youtube.com/watch?v=j_TKDweOsYE
- Transcript: raw/20250723_j_TKDweOsYE/j_TKDweOsYE.en-orig.vtt
- Metadata: raw/20250723_j_TKDweOsYE/j_TKDweOsYE.info.json

AI workloads are rapidly shifting from AI being used for augmentation (co-pilots), to AI becoming responsible for full, end-to-end automation (agents). But building effective agents, and even more importantly, agent experiences that boost productivity requires many pieces. In this talk, we'll be covering the building blocks of agents, how to put them together, and what we've learned from top companies building agents along the way.

About Rita Kozlov
From the very beginning, Rita has been a key figure in the development of Cloudflare's developer platform. Their initial experience as a solutions engineer, helping early enterprise customers adopt the service, gave them firsthand insight into user needs. It was the power of Cloudflare Workers that truly resonated, inspiring a vision for a serverless future. For the past eight years, they have built out the platform which now spans products including storage, compute and AI, and is used by everyone from indie millions of indie developers to Fortune 500 companies.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## How Intuit uses LLMs to explain taxes to millions of taxpayers - Jaspreet Singh, Intuit

- Upload date: 2025-07-23
- Video: https://www.youtube.com/watch?v=_zl_zimMRak
- Transcript: raw/20250723__zl_zimMRak/_zl_zimMRak.en-orig.vtt
- Metadata: raw/20250723__zl_zimMRak/_zl_zimMRak.info.json

I will talk about how Intuit uses LLMs to explain tax situations to Turbotax users.

Users want explanations of their tax situations - this drives confidence in the product. Over the course of last two tax years, Intuit has built out explanations using Anthropic and openAI’s models to develop genAI powered explanations. This includes design a complex system with prompt engineered solutions and both LLM & human powered evaluations to ensure high quality bar that our users expect when filing taxes with us.

During the course of my talk, I will talk across GenAI development lifecycle at scale - including development , evaluations and scaling. And security evaluations. We also developed a fine-tuned version of Claude Haiku & shall be covering that in the presentation.

We also expanded into tax question and answering powered by RAG, including graphRAG and I would be covering those developments too.

About Jaspreet Singh
I’m Jaspreet Singh, a Senior Staff Software Engineer with 12 years of experience in the tech industry. I am the tech lead for the Smart Turbotax AI team at Intuit - focusing on development of new GenAI powered experiences in Intuit Turbotax. I have worked extensively on Personalization and Recommendations problems in the past and I’m very passionate about bringing the latest in AI to help drive Taxes are done experiences for our users. I recently became a father for the first time, and enjoy spending time with my little one. As a speaker at the AI Engineer World’s Fair, I’m excited to share our journey of transforming our user’s tax filing journeys with the power of Gen AI..

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## The Billable Hour is Dead; Long Live the Billable Hour — Kevin Madura + Mo Bhasin, Alix Partners

- Upload date: 2025-07-23
- Video: https://www.youtube.com/watch?v=Wv1tAxKYLeE
- Transcript: raw/20250723_Wv1tAxKYLeE/Wv1tAxKYLeE.en-orig.vtt
- Metadata: raw/20250723_Wv1tAxKYLeE/Wv1tAxKYLeE.info.json

If software was eating the world before, knowledge work will soon be devoured by AI. In corporate America there are thousands of hours spent on rote tasks every day by employees, consultants, and lawyers alike. But is AI really capable of replacing work in the real world yet? Productivity estimates from GenAI range from 1.5% (NBER) to 96% (☝ us! ️). 

In this talk we'll share war stories of where the answer is yes (and no) and how we reduced human time spent on tasks from days to minutes in high-impact situations. The path from promise to actual product, used in real world settings, from our experience, is still unmapped. Learn what we built, how we built it - with code - and how we got stakeholder buy-in to deploy it.

About Kevin Madura
Kevin leads technical advisory engagements and investigations in situations involving complex software, applied AI, and digital assets. As testifying expert and "translator" of technical material, he regularly interfaces with executive leadership, legal counsel, regulators, and engineers, balancing deep technical expertise with strategic clarity to drive outcomes.

About Mo Bhasin
Mo Bhasin is Director of AI Products at AlixPartners, where he leads development of the firm's internal genAI platform. He helped scale the platform to 50+ deployments, and grew the AI team from 2 to 20 in under a year.

Over the last 15 years, he's built products as a data scientist at Google, Nest, and most recently as a startup founder at Outoftheblue.ai.

He holds an engineering degree from the University of California Berkeley, and an MBA from University of Chicago Booth School of Business.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

Timestamps
00:00 Introduction to Alix Partners and the AI Shift
01:05 How AI is Reshaping Knowledge Work
02:19 The Future of Professional Services Models with AI
03:36 AI's Impact on the Three Phases of Engagements
05:07 Scaling Data Analysis Beyond Human Limitations
06:36 The Paradox of AI Investment and Productivity
07:22 Use Case 1: Categorization with Structured Outputs
10:34 Use Case 2: Retrieval-Augmented Generation (RAG)
12:46 Use Case 3: Structured Data Extraction from Unstructured Data
15:54 Key Requirements for Scaling GenAI Initiatives
16:48 Final Thoughts: The Future of LLMs in the Enterprise

## How agents will unlock the $500B promise of AI - Donald Hruska, Retool

- Upload date: 2025-07-23
- Video: https://www.youtube.com/watch?v=Lqq_LcBaJCc
- Transcript: raw/20250723_Lqq_LcBaJCc/Lqq_LcBaJCc.en-orig.vtt
- Metadata: raw/20250723_Lqq_LcBaJCc/Lqq_LcBaJCc.info.json

AI agents are on the cusp of revolutionizing work as we know it. The number of use cases software can tackle is set to explode as AI handles tasks requiring real judgment. But to cross the gap between an interesting AI prototype and an essential business tool, you need agents built by developers with real guardrails and security.

This means blending AI assistance with traditional coding in a multimodal approach that maximizes efficiency and control. The future isn't about dropping in an LLM — it requires integrating any model, any data, any system to deliver results.

Companies utilizing this approach can finally turn their slice of the $500B+ of total AI investment into real business results.

About Donald Hruska
Donald is the engineering lead for Retool's new Agents product.

In his three years at Retool, Donald has led teams across AI, Mobile, and Retool's core app building product. Prior to his time at Retool, Donald co-founded and spent 5+ years growing Draftbit, a Y Combinator-backed company in the low code app building space.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Build Dynamic Products, and Stop the AI Sideshow — Eliza Cabrera (Workday) + Jeremy Silva (Freeplay)

- Upload date: 2025-07-23
- Video: https://www.youtube.com/watch?v=CB-4NKDYnRs
- Transcript: raw/20250723_CB-4NKDYnRs/CB-4NKDYnRs.en-orig.vtt
- Metadata: raw/20250723_CB-4NKDYnRs/CB-4NKDYnRs.info.json

AI across product, GTM, and strategy was a great approach in 2023, but by now, we all already know that AI is disrupting the global landscape and how business gets done. Now is the time to stop chasing your competitors, and letting the technology lead your product strategy. There’s a better way to build that will allow you to differentiate and keep pace.

Join AI product managers Eliza Cabrera and Jeremy Silva to learn how to crawl, walk, and run your way towards building dynamic products.

About Jeremy Silva
A seasoned ML engineer with extensive experience building and deploying language models in the healthcare sector, Jeremy currently serves as Product Lead at Freeplay. At Freeplay, he oversees an enterprise-ready platform that empowers teams to run experiments, create evaluations, monitor production systems, and label data—all within a unified environment.

Drawing from hands-on collaboration with Freeplay's enterprise customers, Jeremy brings valuable "in-the-trenches" experience building LLM systems at scale. This direct customer engagement has also positioned him as a trusted advisor, helping organizations shape and refine their AI product roadmaps for maximum impact.

Jeremy’s unique perspective spans technical implementation and product development making him well-positioned to share insights on effectively bridging the gap between AI capabilities and real-world product outcomes.

About Eliza Cabrera
Building and scaling 0-1 products in the enterprise.

https://www.linkedin.com/in/itselizacab/

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Monetizing AI — Alvaro Morales, Orb

- Upload date: 2025-07-23
- Video: https://www.youtube.com/watch?v=6WQYLQB0odc
- Transcript: raw/20250723_6WQYLQB0odc/6WQYLQB0odc.en-orig.vtt
- Metadata: raw/20250723_6WQYLQB0odc/6WQYLQB0odc.info.json

As AI continues to transform industries, companies are faced with the critical challenge of effectively monetizing AI-driven products in a way that captures value, ensures customer adoption, and scales revenue sustainably. Unlike traditional SaaS models, AI-powered products have unique complexities - such as fluctuating usage patterns, variable compute costs, and evolving customer demands, making conventional pricing strategies unhelpful to the growth of an AI product-led startup.

In this session, Alvaro Morales, CEO and co-founder of Orb, will explore why the often overlooked monetization aspect of AI is critical for businesses. He’ll share real-world examples and data to demonstrate how adaptive pricing models can drive cost savings, enhance customer experience, and reduce operational bottlenecks.

Alvaro will lead a live demo, showcasing how engineers can simulate AI pricing strategies and subsequently integrate them with a simple plug-and-play solution. He’ll also share how real-world revenue simulations enable companies to test and refine pricing before implementing — reducing risk, boosting adoption, and unlocking new revenue streams. As a quick example, cloud software development platform Replit was looking to adopt a usage-based pricing model for a new product, but their existing billing system couldn't support the new model, and building a new billing system would delay the launch timeline. In order to get things done, they turned to Orb, which enabled them to make pricing changes up to the last minute. After the launch, Orb became the single source of truth for both Replit and its customers - providing usage alerts to notify Replit when users hit cost thresholds and provide insights into user spend and payment methods.

Key takeaways: 
The challenge of AI monetization – Why traditional subscription-based SaaS pricing models don’t work for AI-powered products.
Precision pricing – Exploring how usage-based, tiered, and hybrid pricing models can maximize revenue potential. 
Revenue simulation for AI pricing – Leveraging real-time data to test, adjust and optimize pricing strategies.
Avoiding common pricing pitfalls – Identifying mistakes that can lead to revenue leakage and customer churn.

This session is designed for AI executives, product leaders, and engineering teams looking for actionable strategies to build adaptive, scalable pricing models that drive long-term growth and profitability.




---related links---

https://x.com/alvaromorales
https://www.linkedin.com/in/alvaro-morales/
https://www.withorb.com/

## From Hype to Habit: How We’re Building an AI-First SaaS Company—While Still Shipping the Roadmap

- Upload date: 2025-07-23
- Video: https://www.youtube.com/watch?v=3YGRcgZJ3yc
- Transcript: raw/20250723_3YGRcgZJ3yc/3YGRcgZJ3yc.en-orig.vtt
- Metadata: raw/20250723_3YGRcgZJ3yc/3YGRcgZJ3yc.info.json

What does it really take to move a modern SaaS company from AI experimentation to becoming truly AI-first?

At Sprout Social, we’re in the midst of that transformation—rearchitecting strategy, systems, teams, and incentives to put AI at the heart of how we think, build, and deliver value. This is a story in motion: a behind-the-scenes look at how we’re evolving from isolated AI feature experiments to an AI-native operating model.

I’ll share what we’re learning as we navigate the innovation dilemma—integrating disruptive AI capabilities without breaking what already works or our roadmap. That includes rethinking how we define success, how we hire, reward, grow talent, and how we handle legal and ethical complexity without slowing down. We’ll explore the real-world tensions between rapid innovation, value delivery, making progress on Responsible AI, all while elevating internal AI fluency, and engaging with the broader AI ecosystem to stay at the edge.

This isn’t a playbook from the finish line—it’s a candid reflection from deep inside the journey.

About Rossella Blatt Vital
Rossella Blatt Vital is a passionate AI leader with nearly 20 years of experience turning data into business value—from hands-on research and model-building to strategic executive leadership. She began her journey with a PhD in machine learning, focusing on brain-computer interfaces and cancer detection, and spent years writing code, building models, and shipping AI-powered products before stepping into leadership roles across startups, academia, and Fortune 100 companies.

As VP of AI, Data, and Data Science at Sprout Social, Rossella leads the company’s AI transformation—driving strategy across engineering, applied science, and analytics. Her team is building AI-first capabilities across product experiences, platform infrastructure, and foundational data systems.

She’s passionate about building meaningful technology—and the teams that power it—with the belief that AI, when led with vision and integrity, can help shape a more thoughtful and human-centered future.

About Deepsha Menghani
Deepsha Menghani is a passionate AI leader with over a decade of experience translating data and machine learning into meaningful business impact—from predictive modeling and customer analytics to large language model applications. Her career spans hands-on data science, applied AI, and strategic leadership across global tech organizations. As Director of Engineering – AI at Sprout Social, her team is responsible for embedding AI into core product experiences and delivering insights that accelerate growth, improve customer understanding, and inform business strategy across the company.

She’s especially passionate about building AI that is not only technically robust, but also responsible, human-centered, and aligned with real-world decision-making.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Top Ten Challenges to Reach AGI — Stephen Chin, Andreas Kollegger

- Upload date: 2025-07-22
- Video: https://www.youtube.com/watch?v=ypyvj_56sBU
- Transcript: raw/20250722_ypyvj_56sBU/ypyvj_56sBU.en-orig.vtt
- Metadata: raw/20250722_ypyvj_56sBU/ypyvj_56sBU.info.json

an opener to the GraphRAG track!

## Knowledge Graphs in Litigation Agents — Tom Smoker, WhyHow

- Upload date: 2025-07-22
- Video: https://www.youtube.com/watch?v=yYxr6LdXNWM
- Transcript: raw/20250722_yYxr6LdXNWM/yYxr6LdXNWM.en-orig.vtt
- Metadata: raw/20250722_yYxr6LdXNWM/yYxr6LdXNWM.info.json

Structured Representations are pretty important in the law, where the relationships between clauses, documents, entities, and multiple parties matter. Structured Representation means Structured Context Injection. Better Context, Less Hallucinations. We walk through a couple of case studies of systems that we’ve built in production for legal use-cases - from recursive contractual clause retrieval, to HITL legal reasoning news agents.

You'll gain insights into how structured representations significantly improve the effectiveness and reliability of legal agents.

---related links---

https://www.linkedin.com/in/thomassmoker
https://www.whyhow.ai/

## Continuous Profiling for GPUs — Matthias Loibl, Polar Signals

- Upload date: 2025-07-22
- Video: https://www.youtube.com/watch?v=wt8gzWR6auQ
- Transcript: raw/20250722_wt8gzWR6auQ/wt8gzWR6auQ.en-orig.vtt
- Metadata: raw/20250722_wt8gzWR6auQ/wt8gzWR6auQ.info.json

Continuous Profiling for GPUs extends our industry-leading continuous profiling platform to provide deep, always-on visibility into your GPU workloads.

Now you can see exactly how your GPUs are being utilized millisecond by millisecond. Our solution helps you move from guesswork to data-driven optimization.


---related links---

https://twitter.com/metalmatze
https://www.linkedin.com/in/metalmatze/
https://matthiasloibl.com/
https://polarsignals.com

## How to run Evals at Scale: Thinking beyond Accuracy or Similarity — Muktesh Mishra, Adobe

- Upload date: 2025-07-22
- Video: https://www.youtube.com/watch?v=coKKKKh8Vns
- Transcript: raw/20250722_coKKKKh8Vns/coKKKKh8Vns.en-orig.vtt
- Metadata: raw/20250722_coKKKKh8Vns/coKKKKh8Vns.info.json

https://www.linkedin.com/in/mukteshkrmishra/

## How to Hire AI Engineers when EVERYONE is cheating with AI — Beth Glenfield, DevDay

- Upload date: 2025-07-22
- Video: https://www.youtube.com/watch?v=Zqu0VaJw3vo
- Transcript: raw/20250722_Zqu0VaJw3vo/Zqu0VaJw3vo.en-orig.vtt
- Metadata: raw/20250722_Zqu0VaJw3vo/Zqu0VaJw3vo.info.json

AI broke recruitment - how to think about hiring for AI-enabled engineers in the era of AI cheating agents and AI customised resumes.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## When Vectors Break Down: Graph-Based RAG for Dense Enterprise Knowledge - Sam Julien, Writer

- Upload date: 2025-07-22
- Video: https://www.youtube.com/watch?v=XlAIgmi_Vow
- Transcript: raw/20250722_XlAIgmi_Vow/XlAIgmi_Vow.en-orig.vtt
- Metadata: raw/20250722_XlAIgmi_Vow/XlAIgmi_Vow.info.json

Enterprise knowledge bases are filled with "dense mapping," thousands of documents where similar terms appear repeatedly, causing traditional vector retrieval to return the wrong version or irrelevant information. When our customers kept hitting this wall with their RAG systems, we knew we needed a fundamentally different approach.

In this talk, I'll share Writer's journey developing a graph-based RAG architecture that achieved 86.31% accuracy on the RobustQA benchmark while maintaining sub-second response times, significantly outperforming vector approaches.

I'll survey the key techniques behind this performance leap and why graph-based approaches excel with complex enterprise information structures like product documentation, financial documents, and technical specifications that challenge traditional RAG systems. You'll learn about using specialized LLMs to build semantic relationships, how compression techniques efficiently handle concentrated enterprise data patterns, and how infusing key data points in the memory layer of the LLM lowers hallucination.

The presentation will provide practical insights into identifying when graph-based approaches make sense for your organization's specific data challenges, helping you make informed architectural decisions for your next enterprise RAG system.

About Sam Julien
Sam Julien is the Director of Developer Relations at Writer and is passionate about helping engineers improve their effectiveness and advance their careers. He loves spending time outside with his family in the Pacific Northwest. You can find more of Sam's work at samjulien.com.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Practical GraphRAG: Making LLMs smarter with Knowledge Graphs — Michael, Jesus, and Stephen, Neo4j

- Upload date: 2025-07-22
- Video: https://www.youtube.com/watch?v=XNneh6-eyPg
- Transcript: raw/20250722_XNneh6-eyPg/XNneh6-eyPg.en-orig.vtt
- Metadata: raw/20250722_XNneh6-eyPg/XNneh6-eyPg.info.json

RAG has become one standard architecture component for GenAI applications to address hallucinations and integrate factual knowledge. While vector search over text is common, knowledge graphs represent a proven advancement by leveraging advanced RAG patterns to access and integrate interconnected factual information, complementing the language skills of LLMs. This talk explores GraphRAG challenges, implementation patterns, and real-world agentic examples with Google's ADK, demonstrating how this approach delivers more trustworthy and explainable GenAI solutions with enhanced reasoning capabilities.

About Michael Hunger
Michael Hunger has been passionate about software development for more than 30 years.

For the last 15 years, he has been working on the open source Neo4j graph database filling many roles, most recently heading product innovation and GenAI.

As a developer Michael enjoys many aspects of software development and architecture, learning new things every day, participating in exciting and ambitious open source projects and contributing and writing software related books and articles. Michael spoke at numerous conferences and helped organize others.

Michael helps kids to learn to program by running weekly girls-only coding classes at local schools.

About Jesús Barrasa
Dr. Jesús Barrasa is the AI Field CTO at Neo4j, where he works with organisations combining the power of GenAI with Knowledge Graphs. He co-authored "Building Knowledge Graphs" (O'Reilly 2023) and is cohost of the monthly Going Meta live webcast (https://goingmeta.live/) since 2022.
Jesús holds a Ph.D. in Artificial Intelligence/Knowledge Representation and is an active thought leader in the KG and AI space.

About Stephen Chin
Stephen Chin is VP of Developer Relations at Neo4j, conference chair of the LF AI & Data Foundation, and author of numerous titles including the upcoming GraphRAG: The Definitive Guide for O'Reilly. He has given keynotes and main stage talks at numerous conferences around the world including AI Engineer Summit, AI DevSummit, Devoxx, DevNexus, JNation, JavaOne, Shift, Joker, swampUP, and GIDS. Stephen is an avid motorcyclist who has done evangelism tours in Europe, Japan, and Brazil, interviewing developers in their natural habitat. When he is not traveling, he enjoys teaching kids how to do AI, embedded, and robot programming together with his daughters.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## AI powered entomology: Lessons from millions of AI code reviews — Tomas Reimers, Graphite

- Upload date: 2025-07-22
- Video: https://www.youtube.com/watch?v=TswQeKftnaw
- Transcript: raw/20250722_TswQeKftnaw/TswQeKftnaw.en-orig.vtt
- Metadata: raw/20250722_TswQeKftnaw/TswQeKftnaw.info.json

This talk will explore insights from millions of automated code reviews, revealing trends in bugs, vulnerabilities, and code health that Graphite’s AI code review agent have uncovered. This talk will also provide meta commentary into the types of bugs AI code review agents are great at spotting, and how far the field of AI code review has come in the last year alone.


---related links---

## Stop Using RAG as Memory — Daniel Chalef, Zep

- Upload date: 2025-07-22
- Video: https://www.youtube.com/watch?v=T5IMo5ntyhA
- Transcript: raw/20250722_T5IMo5ntyhA/T5IMo5ntyhA.en-orig.vtt
- Metadata: raw/20250722_T5IMo5ntyhA/T5IMo5ntyhA.info.json

RAG is great for static knowledge retrieval—but terrible at memory. Vectorstore-based systems sold as memory lack relational and temporal awareness, leading agents astray with outdated or ambiguous information.

Discover how temporally-aware knowledge graphs—built by the open-source Graphiti framework—solve these limitations. You’ll learn practical strategies to maintain precise, context-rich memory, enabling agents to reason accurately about historical context and knowledge provenance.

About Daniel Chalef   
I’m Daniel Chalef, an engineer turned startup founder currently building Zep, where we're creating AI's foundational memory layer powered by knowledge graphs. Our vision is a world where AI agents reliably handle personalized tasks, from the mundane to the monumental, always prioritizing privacy and compliance.

Previously, I've led ML and data science teams, marketing, and corporate development at both early-stage startups and late-stage companies, building data-driven products at scale. My first startup was an open source document management application, KnowledgeTree.

When I’m not building Zep (which is seldom 🙂), you’ll likely find me cycling or hiking around the Bay Area with my dog.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Books reimagined: AI to create new experiences for things you know — Lukasz Gandecki, TheBrain.pro

- Upload date: 2025-07-22
- Video: https://www.youtube.com/watch?v=Kcka7rzcxLk
- Transcript: raw/20250722_Kcka7rzcxLk/Kcka7rzcxLk.en-orig.vtt
- Metadata: raw/20250722_Kcka7rzcxLk/Kcka7rzcxLk.info.json

[last round of Attendee-Led 10min lightning talks] I will showcase how I got tired of waiting for an AI assisted/no spoiler book reading experience and built my own. Check 30s video at https://youtu.be/JjwnYqy668M or go to demo book at https//bookgenius.net Open Sourcing!

contact: https://x.com/lgandecki

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Critical AI Inference your CIO can Trust — Sahil Yadav, Hariharan Ganesan, Telemetrak

- Upload date: 2025-07-22
- Video: https://www.youtube.com/watch?v=6Tpm4m1YxHk
- Transcript: raw/20250722_6Tpm4m1YxHk/6Tpm4m1YxHk.en-orig.vtt
- Metadata: raw/20250722_6Tpm4m1YxHk/6Tpm4m1YxHk.info.json

Enterprise AI adoption is accelerating, but with it comes a hard question: Do we trust the model’s decisions? In this 18-minute talk, I’ll explore the invisible risks behind automated decision-making in safety-critical and revenue-sensitive environments. Drawing on case studies across manufacturing, telecom, and industrial IoT, I’ll highlight how explainability, traceability, and robust guardrails drive adoption and protect enterprise value.
Attendees will walk away with:
• A 3-step framework for operationalizing AI trust
• Real-world lessons from building guardrails in on-prem and hybrid systems
• Tools and techniques for debugging and explaining inferences at scale
• A blueprint for building trust between models, engineers, and executive stakeholders


---related links---

https://www.linkedin.com/in/yadavsahil/
https://telemetrak.com

## Stateful environments for vertical agents — Josh Purtell, Synth Labs

- Upload date: 2025-07-22
- Video: https://www.youtube.com/watch?v=5rMc-moNVx0
- Transcript: raw/20250722_5rMc-moNVx0/5rMc-moNVx0.en-orig.vtt
- Metadata: raw/20250722_5rMc-moNVx0/5rMc-moNVx0.info.json

Hey All - gave a talk on building stateful environments for vertical agents at AI tinkerers and ppl really liked it, happy to do again. Here's the repo - general code that endows environments like Pokemon Red, Minecraft, Swe-Bench, and others with the same interface for development and agent training. github.com/synth-laboratories/Environments

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## HybridRAG: A Fusion of Graph and Vector Retrieval  - Mitesh Patel, NVIDIA

- Upload date: 2025-07-22
- Video: https://www.youtube.com/watch?v=-tgQa8Fzf80
- Transcript: raw/20250722_-tgQa8Fzf80/-tgQa8Fzf80.en-orig.vtt
- Metadata: raw/20250722_-tgQa8Fzf80/-tgQa8Fzf80.info.json

Interpreting complex information from unstructured text data poses significant challenges to Large Language Models (LLM), with difficulties often arising from specialized terminology and the multifaceted relationships between entities in document architectures. Conventional Retrieval Augmented Generation (RAG) methods face limitations in capturing these nuanced interactions, leading to suboptimal performance. In our talk, we introduce a novel approach integrating Knowledge Graph-based RAG (GraphRAG) with VectorRAG, designed to refine question-answering (Q&A) systems for more effective information extraction from complex texts. Our approach employs a dual retrieval strategy that harnesses both knowledge graphs and vector databases, enabling the generation of precise and contextually appropriate answers, thereby setting a new standard for LLMs in processing sophisticated data.

About Mitesh Patel
Mitesh Patel is a developer advocate manager at NVIDIA. His team is responsible for creating workflows to showcase how developers can harness GPU acceleration in their workflows using tools and frameworks popular in the developer community. Before NVIDIA, he was a senior research scientist at Fuji Xerox Palo Alto Laboratory Inc. (a research subsidiary of Fuji Xerox), where he worked on developing indoor localization technologies for applications such as asset tracking in hospitals and delivery cart tracking in manufacturing facilities. Mitesh received his Ph.D. in Robotics from the Center of Autonomous Systems (CAS) at the University of Technology Sydney, Australia in 2014.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## UX Design Principles for Semi Autonomous Multi Agent Systems — Victor Dibia, Microsoft

- Upload date: 2025-07-21
- Video: https://www.youtube.com/watch?v=fmZWvE7yDZo
- Transcript: raw/20250721_fmZWvE7yDZo/fmZWvE7yDZo.en-orig.vtt
- Metadata: raw/20250721_fmZWvE7yDZo/fmZWvE7yDZo.info.json

Autonomous or semi-autonomous multi-agent systems (MAS) involve exponentially complex configurations (system config, agent configs, task management and delegation, etc.). These present unique interface design challenges for both developer tooling and end-user experiences.
In this session, I'll explore UX design principles for multi-agent systems, addressing critical questions: What is the true configuration space for autonomous MAS? How can users arrive at the correct mental model of an MAS's capabilities, if at all? How can we improve trust and safety through techniques like cost-aware action delegation? What makes agent actions observable? How do we enable seamless interruptibility? Attendees will gain actionable insights to create more transparent, trustworthy, and user-centered multi-agent applications, illustrated through real-world implementations in AutoGen Studio - a low code developer tool built on AutoGen (44k stars on GitHub, MIT license) and similar tools.


---related links---

https://x.com/vykthur
https://www.linkedin.com/in/dibiavictor/
https://newsletter.victordibia.com/
https://victordibia.com/

## Excalidraw: AI and Human Whiteboarding Partnership - Christopher Chedeau

- Upload date: 2025-07-21
- Video: https://www.youtube.com/watch?v=aopgVJBQC0o
- Transcript: raw/20250721_aopgVJBQC0o/aopgVJBQC0o.en-orig.vtt
- Metadata: raw/20250721_aopgVJBQC0o/aopgVJBQC0o.info.json

Covid sent everybody home and created the space of virtual whiteboards. At first the experience reused the physical constraints but soon it became better than a physical whiteboard thanks to using virtual native concepts like copy-paste and using keyboard input.
The next step in this evolution is to integrate AI into the workflow. We've tried a lot of things with Excalidraw and ended up landing on turning prompt into diagram. Come to the talk to understand how it fits into the workflow and how we implemented it.

About Christopher Chedeau   
Co-creator of React Native and Prettier. Creator of Excalidraw, "CSS-in-JS", Yoga and React Conf.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## CIAM for AI: Authn/Authz for Agents — Michael Grinich, CEO of WorkOS

- Upload date: 2025-07-21
- Video: https://www.youtube.com/watch?v=D4Dswf-__RM
- Transcript: raw/20250721_D4Dswf-__RM/D4Dswf-__RM.en-orig.vtt
- Metadata: raw/20250721_D4Dswf-__RM/D4Dswf-__RM.info.json

AI agents are changing the way modern SaaS products operate. Whether automating workflows, integrating with APIs, or acting on behalf of users, AI-driven assistants and autonomous systems are becoming core product features. But securing these agents presents a fundamental challenge: How do you authenticate AI agents? How do you control what they can access? How do you ensure they act within the right permissions? This talk will explore these concepts and more while highlighting current research and best practices.


---related links---

https://x.com/grinich/
https://www.linkedin.com/in/grinich/
https://workos.com/guides
https://workos.com/

## The Bitter Layout or: How I Learned to Love the Model Picker — Maximillian Piras, Yutori

- Upload date: 2025-07-21
- Video: https://www.youtube.com/watch?v=BZtD0yYAgCQ
- Transcript: raw/20250721_BZtD0yYAgCQ/BZtD0yYAgCQ.en-orig.vtt
- Metadata: raw/20250721_BZtD0yYAgCQ/BZtD0yYAgCQ.info.json

Are conversational interfaces the future or, as many designers have suggested, a lazy solution that is bottlenecking AI-HCI? Despite well-documented usability issues, the design of many AI applications defaults to an input field, turn-by-turn flow, and an endless model picker — I call this “The Bitter Layout”.

In this talk, we’ll explore how Clay Christensen’s theory of commoditization from the early PC industry can explain why scaling laws require AI interfaces to remain modular until models fully commoditize. The killer feature of conversational interfaces may not be that they’re natural, but that they’re conformable. Learn how to evolve interfaces as inference scales, spot shifts in the basis of competition, and stop worrying about the next model update steamrolling your design decisions.

Foothill G 1&2: Design Engineering

About Maximillian Piras
Currently the Founding Designer at Yutori working on AI web agents. Previously, Head of Design at Headliner and Sr. Designer at 8tracks. Led cross-platform UIUX design for multiple early-stage consumer startups shipping to millions of users. Contributing writer to Smashing Magazine covering AI-first design. Before that, developed graphics and animations for clients including Giphy, MIT, and Ryuichi Sakamoto.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Agentic GraphRAG: AI’s Logical Edge — Stephen Chin, Neo4j

- Upload date: 2025-07-21
- Video: https://www.youtube.com/watch?v=AvVoJBxgSQk
- Transcript: raw/20250721_AvVoJBxgSQk/AvVoJBxgSQk.en-orig.vtt
- Metadata: raw/20250721_AvVoJBxgSQk/AvVoJBxgSQk.info.json

AI models are getting tasked to do increasingly complex and industry specific tasks where different retrieval approaches provide distinct advantages in accuracy, explainability, and cost to execute. GraphRAG retrieval models have become a powerful tool to solve domain specific problems where answers require logical reasoning and correlation that can be aided by graph relationships and proximity algorithms. We will demonstrate how an agent architecture combining RAG and GraphRAG retrieval patterns can bridge the gap in data analysis, strategic planning, and retrieval to solve complex domain specific problems. 


---related links---

https://twitter.com/steveonjava
https://www.linkedin.com/in/steveonjava/
http://steveonjava.com/
https://neo4j.com/

## Good design hasn’t changed with AI — John Pham, SF Compute

- Upload date: 2025-07-21
- Video: https://www.youtube.com/watch?v=7e7eVtcygCM
- Transcript: raw/20250721_7e7eVtcygCM/7e7eVtcygCM.en-orig.vtt
- Metadata: raw/20250721_7e7eVtcygCM/7e7eVtcygCM.info.json

Bad designs are still bad. AI doesn’t make it good. The novelty of AI makes the bad things tolerable, for a short time. Building great designs and experiences with AI have the same first principles pre-AI. When people use software, they want it to feel responsive, safe, accessible and delightful. We’ll go over the big and small details that goes into software that people want to use, not forced to use.

About John Pham   
I'm John Pham, an engineer and a self-taught designer. I seek the dopamine hits of building delightful experiences for others. I've worked at Vercel, Microsoft and NASA doing just that.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## tldraw.computer - Steve Ruiz, tldraw

- Upload date: 2025-07-21
- Video: https://www.youtube.com/watch?v=1C2TdPkj6aQ
- Transcript: raw/20250721_1C2TdPkj6aQ/1C2TdPkj6aQ.en-orig.vtt
- Metadata: raw/20250721_1C2TdPkj6aQ/1C2TdPkj6aQ.info.json

Learn about tldraw's latest experiments with AI on an infinite canvas. In 2024, we created tldraw computer, a loose visual programming environment where arrows and LLMs powered every step of a graph on tldraw's canvas.

About Steve Ruiz
Steve Ruiz is founder and CEO of tldraw, a London-based startup building an infinite canvas component for the web.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## What every AI engineer needs to know about GPUs — Charles Frye, Modal

- Upload date: 2025-07-20
- Video: https://www.youtube.com/watch?v=y-UGrYbJsJk
- Transcript: raw/20250720_y-UGrYbJsJk/y-UGrYbJsJk.en-orig.vtt
- Metadata: raw/20250720_y-UGrYbJsJk/y-UGrYbJsJk.info.json

Every programmer needs to know a few things about hardware, like processors, memory, and disks. Due to AI systems' extreme demand for mathematical processing power, AI engineers need to know a few things about GPUs -- the world's most popular high-throughput mathematical co-processor.

In this talk, I will explain the fundamental engineering constraints and design decisions that shape GPUs and trace those up to some counter-intuitive facts about the performance characteristics of AI systems, with actionable insights for their deployers and consumers.


---related links---

## Robots as professional Chefs - Nikhil Abraham, CloudChef

- Upload date: 2025-07-20
- Video: https://www.youtube.com/watch?v=MBWGiWJDlSo
- Transcript: raw/20250720_MBWGiWJDlSo/MBWGiWJDlSo.en-orig.vtt
- Metadata: raw/20250720_MBWGiWJDlSo/MBWGiWJDlSo.info.json

How we converted a bimanual robot into a professional chef that works in novel kitchens and learn new recipes from a single demonstration

About Nikhil Abraham
Nikhil is the CEO of CloudChef - reimagining cooking using embodied AI. CloudChef builds robots that enable commercial kitchens to cook high quality meals while solving for availability of skilled chefs. Our robots are already doing full-time work in several leading commercial kitchens. Nikhil is an alum of IIT Bombay and was the cofounder of Rephrase AI (acquired by Adobe)

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Building Effective Voice Agents — Toki Sherbakov + Anoop Kotha, OpenAI

- Upload date: 2025-07-20
- Video: https://www.youtube.com/watch?v=-OXiljTJxQU
- Transcript: raw/20250720_-OXiljTJxQU/-OXiljTJxQU.en-orig.vtt
- Metadata: raw/20250720_-OXiljTJxQU/-OXiljTJxQU.info.json

How to build production voice applications and learnings from working with customers along the way!

https://x.com/tokisherbakov
https://www.linkedin.com/in/akotha7/

## OpenThoughts: Data Recipes for Reasoning Models — Ryan Marten, Bespoke Labs

- Upload date: 2025-07-19
- Video: https://www.youtube.com/watch?v=liG97YXaTSA
- Transcript: raw/20250719_liG97YXaTSA/liG97YXaTSA.en-orig.vtt
- Metadata: raw/20250719_liG97YXaTSA/liG97YXaTSA.info.json

Peel back the curtain on state of the art model post-training through the story of OpenThinker, a SOTA small reasoning model (outperforming DeepSeek distill), built in the open. Learn about the dataset recipe used to build the strongest reasoning models which you can apply to your own domain-specific specialized reasoning models. Hear about the strategies that scale (and that don't) based on our rigorous experimentation on the journey from thousands of data points (Bespoke-Stratos) to millions of data (OpenThinker3). Build upon our open source engineering solutions for large-scale synthetic data generation, training on multiple supercomputing clusters, and building out fast reliable evaluations.

About Ryan Marten
Ryan Marten is co-lead of OpenThinker collaboration and a founding engineer at Bespoke Labs, working on data curation and model post-training. Previously, Ryan has been an AI researcher at the University of Illinois Urbana-Champaign, University of Toronto, University of Oxford, AI2, and Vector Institute. When he's not at the lab, he's probably out surfing.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

Timestamps:

0:00 - Introduction to the problem of open-source reasoning in AI models.

1:09 - The effectiveness of Supervised Fine-Tuning (SFT) for reasoning.

3:38 - Introduction to OpenThoughts 3 and its performance.

7:52 - Key learnings from the data recipe development.

11:34 - Guidance on adapting the dataset recipe to specific domains.

15:15 - Call for open collaboration and where to find the project's resources

## A Taxonomy for Next-gen Reasoning — Nathan Lambert, Allen Institute (AI2) & Interconnects.ai

- Upload date: 2025-07-19
- Video: https://www.youtube.com/watch?v=jQcsVk0KWiQ
- Transcript: raw/20250719_jQcsVk0KWiQ/jQcsVk0KWiQ.en-orig.vtt
- Metadata: raw/20250719_jQcsVk0KWiQ/jQcsVk0KWiQ.info.json

Current AI models are extremely skilled, which was seen as the step change in evaluation scores across the industry in the first half of 2025, but often fail when presented with even medium time-horizon tasks. This talk presents a taxonomy of 4 traits of reasoning models -- skills, calibration, strategy, and abstraction -- that will be crucial to creating the next generation of AI applications. With this, we focus on the latter two, strategy and abstraction, and discuss how these traits will enable long-horizon and reliable agents. The talk concludes with a scenario where these agentic behaviors are the foundation for RL continuing to scale in the coming years and post-training techniques reaching compute parity with pretraining methors sooner than later.

About Nathan Lambert
Nathan Lambert is a Senior Research Scientist and post-training lead at the Allen Institute for AI focusing on building open language models. At the same time he founded and operates Interconnects.ai to increase transparency and understanding of current AI models and systems.

Previously, he helped build an RLHF research team at HuggingFace. He received his PhD from the University of California, Berkeley working at the intersection of machine learning and robotics. He was advised by Professor Kristofer Pister in the Berkeley Autonomous Microsystems Lab and Roberto Calandra at Meta AI Research. He was lucky to intern at Facebook AI and DeepMind during his Ph.D. Nathan was was awarded the UC Berkeley EECS Demetri Angelakos Memorial Achievement Award for Altruism for his efforts to better community norms.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

Timestamps:

[00:00] The Current State of Reasoning in AI Models

[01:06] Unlocking New Language Model Applications

[03:48] The Need for Advanced Planning in AI

[04:29] A Proposed Taxonomy for Next-Generation Reasoning

[06:16] Reinforcement Learning with Verifiable Rewards

[08:23] Current Challenges and Future Directions

[12:07] The Effort Required to Build New Capabilities

[16:20] A Research Plan for Training Reasoning Models

[17:36] The Shift in Compute Allocation from Pre-training to Post-training

## Design like Karpathy is watching — Zeke Sikelianos, Replicate

- Upload date: 2025-07-19
- Video: https://www.youtube.com/watch?v=huQPkrwVWwc
- Transcript: raw/20250719_huQPkrwVWwc/huQPkrwVWwc.en-orig.vtt
- Metadata: raw/20250719_huQPkrwVWwc/huQPkrwVWwc.info.json

Legendary AI engineer and educator Andrej Karpathy recently blogged about his experiences building, deploying, and monetizing a vibe-coded web app called MenuGen. Let's dig into the challenges he faced and learn what we as AI designers can do to make life better for the Andrejs of the world.

About Zeke Sikelianos
Zeke's been building developer tools at companies like Heroku, npm, GitHub, and Replicate for over ten years. He cares deeply about simple and tasteful developer experiences, and thinks the world of generative AI deserves small, sharp, and composable tools!

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## How to Train Your Agent: Building Reliable Agents with RL — Kyle Corbitt, OpenPipe

- Upload date: 2025-07-19
- Video: https://www.youtube.com/watch?v=gEDl9C8s_-4
- Transcript: raw/20250719_gEDl9C8s_-4/gEDl9C8s_-4.en-orig.vtt
- Metadata: raw/20250719_gEDl9C8s_-4/gEDl9C8s_-4.info.json

Have you ever launched an awesome agentic demo, only to realize no amount of prompting will make it reliable enough to deploy in production? Agent reliability is a famously difficult problem to solve!

In this talk we’ll learn how to use GRPO to help your agent learn from its successes and failures and improve over time. We’ve seen dramatic results with this technique, such as an email assistant agent that whose success rate jumped from 74% to 94% after replacing o4-mini with an open source model optimized using GRPO.

We’ll share case studies as well as practical lessons learned around the types of problems this works well for and the unexpected pitfalls to avoid.

About Kyle Corbitt
Kyle Corbitt is the co-founder and CEO of OpenPipe, the RL post-training company. OpenPipe has trained thousands of customer models for both enterprises and tech-forward startups.

Before founding OpenPipe, Kyle led the Startup School team at Y Combinator, which was responsible for the product and content that YC produces for early-stage companies. Prior to that he worked as an engineer at Google and studied ML at school.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

Timestamps:

[00:00] - Introduction to building reliable agents with RL.

[00:49] - Case Study: ART-E, an AI email assistant.

[02:19] - The importance of starting with prompted models before moving to RL.

[03:17] - Performance improvements of RL over prompted models.

[05:18] - Cost and latency benefits of the RL approach.

[08:02] - The two hardest problems in modern RL: realistic environments and reward functions.

[13:13] - Optimizing agent behavior with "extra rewards."

[15:25] - The problem of "reward hacking" and how to address it.

[18:37] - The solution to reward hacking:

## ComfyUI Full Workshop — first workshop from ComfyAnonymous himself!

- Upload date: 2025-07-19
- Video: https://www.youtube.com/watch?v=_FKeSzM9fPc
- Transcript: raw/20250719__FKeSzM9fPc/_FKeSzM9fPc.en-orig.vtt
- Metadata: raw/20250719__FKeSzM9fPc/_FKeSzM9fPc.info.json

Quick introduction to ComfyUI and what's new followed by a QA session.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Real world MCPs in GitHub Copilot Agent Mode — Jon Peck, Microsoft

- Upload date: 2025-07-19
- Video: https://www.youtube.com/watch?v=RkVILz06y08
- Transcript: raw/20250719_RkVILz06y08/RkVILz06y08.en-orig.vtt
- Metadata: raw/20250719_RkVILz06y08/RkVILz06y08.info.json

As developers, we don't spend most of our time vibe-coding prototypes. More often, we're adding features, squashing bugs, and building tests for existing apps across a wide variety of services and technologies. Come learn how MCPs help GitHub Copilot to untangle real engineering problems. By allowing agent mode to securely work with data sources, testing tools, infrastructure providers, and even core DevOps tooling -- we can go beyond the hype, and solve the actual engineering problems we face every day.


---related links---

http://twitter.com/peckjon
http://linkedin.com/in/peckjon
https://github.com/peckjon

## [Full Workshop] Reinforcement Learning, Kernels, Reasoning, Quantization & Agents — Daniel Han

- Upload date: 2025-07-19
- Video: https://www.youtube.com/watch?v=OkEGJ5G3foU
- Transcript: raw/20250719_OkEGJ5G3foU/OkEGJ5G3foU.en-orig.vtt
- Metadata: raw/20250719_OkEGJ5G3foU/OkEGJ5G3foU.info.json

Why is Reinforcement Learning (RL) suddenly everywhere, and is it truly effective? Have LLMs hit a plateau in terms of intelligence and capabilities, or is RL the breakthrough they need?

In this workshop, we'll dive into the fundamentals of RL, what makes a good reward function, and how RL can help create agents.

We'll also talk about kernels, are they still worth your time and what you should focus on. And finally, we’ll explore how LLMs like DeepSeek-R1 can be quantized down to 1.58-bits and still perform well, along with techniques to maintain accuracy.

About Daniel Han
I'm building Unsloth and we're an open-source startup trying to make AI more accessible and accurate for everyone! We have 40K GitHub stars, 10M monthly downloads on Hugging Face and worked with Google, Meta, Hugging Face teams to fix bugs in open-source models like Llama, Phi & Gemma models. I was previously working at NVIDIA making TSNE 2000x faster.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

Timestamps

00:00 Introduction and Unsloth's Contributions
03:25 The Evolution of Large Language Models (LLMs)
09:47 LLM Training Stages and Yann LeCun's Cake Analogy
16:56 Agents and Reinforcement Learning Principles
23:17 PPO and the Introduction of GRPO
48:12 Reward Model vs. Reward Function
51:22 The Math Behind the Reinforce Algorithm
01:08:50 PPO Formula Breakdown
01:16:29 GRPO Deep Dive
02:00:20 Practical Implementation and Demo with Unsloth
02:33:07 Quantization and the Future of GPUs
02:41:59 Conclusion and Call to Action

## Dream Machine: Scaling to 1m users in 4 days — Keegan McCallum, Luma AI

- Upload date: 2025-07-19
- Video: https://www.youtube.com/watch?v=EY4O9M6AsWI
- Transcript: raw/20250719_EY4O9M6AsWI/EY4O9M6AsWI.en-orig.vtt
- Metadata: raw/20250719_EY4O9M6AsWI/EY4O9M6AsWI.info.json

Talking about Luma AI, our mission, and how our ML infrastructure enables SOTA multimodal model development

About Keegan McCallum 
I'm Keegan McCallum, the Head of ML infrastructure at Luma AI. I began my career in research focusing on portfolio optimization. Since then I've founded two startups, lead engineering at two others and have landed at Luma AI working on an unconventional multimodal path to AGI among a cracked team of researchers and engineers. When I'm not working, I'm usually out in the woods hiking with my family, or exploring the culinary delights in whatever city I happen to be in. I'm excited to share the insights and war stories I've gathered launching one of the most successful AI products to date in a (hopefully) fun and engaging way

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

Timestamps
The initial launch challenges [00:00]: Luma AI was unprepared for the high traffic, quickly exhausting their initial GPU allocation and facing a large queue of requests.

Rapid scaling efforts [00:57]: They rapidly scaled their GPU capacity from 500 to 5,000 H100 GPUs within six hours, and later added another 4,000 H100 GPUs from their training cluster to keep up with demand.

Luma AI's mission [03:10]: Beyond just video models, Luma AI aims to build general multimodal intelligence that can generate, understand, and operate in the physical world.

Their product capabilities [03:22]: They demonstrate a "modify video" feature where users can upload iPhone videos and transform them with text prompts. They also highlight their public API for integrating this functionality into applications [03:52].

Infrastructure re-architecture [06:02]: They moved from a brittle, tightly coupled container setup using Triton inference server to a custom-built serving stack on vanilla PyTorch, which offers better support for multiple GPUs, nodes, and different chipsets.

Challenges and solutions in scaling [07:39]:

Back pressure [07:51]: They implemented a dispatch limitation system to prevent too many CPU workers from queuing jobs in one cluster.

Fair scheduling and work starvation [08:36]: To address issues with different user tiers (API, enterprise, unlimited, light, free) and prevent lower-priority jobs from being starved, they developed an SLO (Service Level Objective) based system that prioritizes jobs based on the percentage of their worst-case waiting time [11:14].

Handling different models and bursts [08:43]: They built a system to automatically scale up compute on their training cluster to handle demand bursts [09:16].

Model management [13:24]: They use a model repository system where each model has immutable versions stored in object storage, including the full Python environment and checkpoints. This allows for reproducible rollbacks and seamless, on-the-fly version switching for workers [14:46].

Hiring [15:13]: Luma AI is actively hiring engineers, researchers, and AI enthusiasts

## Google Photos Magic Editor: GenAI Under the Hood of a Billion-User App - Kelvin Ma, Google Photos

- Upload date: 2025-07-19
- Video: https://www.youtube.com/watch?v=C13jiFWNuo8
- Transcript: raw/20250719_C13jiFWNuo8/C13jiFWNuo8.en-orig.vtt
- Metadata: raw/20250719_C13jiFWNuo8/C13jiFWNuo8.info.json

Go behind the scenes of Google Photos' Magic Editor. Explore the engineering feats required to integrate complex CV and cutting-edge generative AI models into a seamless mobile experience. We'll discuss optimizing massive models for latency/size, the crucial interplay with graphics rendering (OpenGL/Halide), and the practicalities of turning research concepts into polished features people actually use.

About Kelvin Ma
I'm Kelvin Ma. A product engineer with 15 years of experience working across innovative consumer applications that is used by millions of consumers. I'm passionate about using technology to build tools that improves users lives by allowing greater expression, building skills, and fostering communication.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## On Curiosity — Sharif Shameem, Lexica

- Upload date: 2025-07-19
- Video: https://www.youtube.com/watch?v=0F8mnGPUycY
- Transcript: raw/20250719_0F8mnGPUycY/0F8mnGPUycY.en-orig.vtt
- Metadata: raw/20250719_0F8mnGPUycY/0F8mnGPUycY.info.json

Creating and sharing demos is the easiest way to influence the future. It gets people to think about what's possible. A good tech demo doesn't have to be fully fleshed out. It doesn't even have to be fully functional. The purpose of a demo is to inspire. A good demo makes you feel like someone jumped into the future and pulled back an idea to the present.

About Sharif Shameem
I'm the founder of Lexica – we're building creative tools backed by state-of-the-art generative models (P.S. we're hiring). I previously worked on a low-code tool powered by language models called Debuild.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## MCP is all you need — Samuel Colvin, Pydantic

- Upload date: 2025-07-18
- Video: https://www.youtube.com/watch?v=bmWZk9vTze0
- Transcript: raw/20250718_bmWZk9vTze0/bmWZk9vTze0.en-orig.vtt
- Metadata: raw/20250718_bmWZk9vTze0/bmWZk9vTze0.info.json

Everyone is talking about agents, and right after that, they’re talking about agent-to-agent communications. Not surprisingly, various nascent, competing protocols are popping up to handle it.

But maybe all we need is MCP — the OG of GenAI communication protocols (it's from way back in 2024!).

Last year, Jason Liu gave the second most watched AIE talk — “Pydantic is all you need”.

This year, I (the creator of Pydantic) am continuing the tradition by arguing that MCP might be all we need for agent-to-agent communications.

What I’ll cover:

- Misusing Common Patterns: MCP was designed for desktop/IDE applications like Claude Code and Cursor. How can we adapt MCP for autonomous agents?
- Many Common Problems: MCP is great, but what can go wrong? How can you work around it? Can the protocol be extended to solve these issues?
- Monitoring Complex Phenomena: How does observability work (and not work) with MCP?
- Multiple Competing Protocols: A quick run-through of other agent communication protocols like A2A and AGNTCY, and probably a few more by June 😴
- Massive Crustaceans Party: What might success look like if everything goes to plan?


---related links---

https://x.com/samuel_colvin
https://www.linkedin.com/in/samuel-colvin/
https://github.com/samuelcolvin
https://pydantic.dev/


Timestamps
00:00:00 - Introduction: Speaker Samuel Colvin introduces himself as the creator of Pydantic.

00:00:42 - Pydantic Ecosystem: Introduction to Pydantic the company, the Pydantic AI agent framework, and the Logfire observability platform.

00:01:18 - Talk Thesis: Explaining the title "MCP is all you need" and the main argument that MCP simplifies agent communication.

00:02:05 - MCP's Focus: Clarifying that the talk focuses on MCP for autonomous agents and custom code, not its original desktop automation use case.

00:02:48 - Tool Calling Primitive: Highlighting that "tool calling" is the most relevant MCP primitive for this context.

00:03:10 - MCP vs. OpenAPI: Listing the advantages MCP has over a simple OpenAPI specification for tool calls.

00:03:21 - Feature 1: Dynamic Tools: Tools can appear and disappear based on server state.

00:03:26 - Feature 2: Streaming Logs: The ability to return log data to the user while a tool is still executing.

00:03:33 - Feature 3: Sampling: A mechanism for a tool (server) to request an LLM call back through the agent (client).

00:04:01 - MCP Architecture Diagram: Visualizing the basic agent-to-tool communication flow.

00:04:43 - Complex Architecture: Discussing scenarios where tools are themselves agents that need LLM access.

00:05:24 - Explaining Sampling: Detailing how sampling solves the problem of every agent needing its own LLM by allowing tools to "piggyback" on the client's LLM access.

00:06:42 - Pydantic AI's Role in Sampling: How the Pydantic AI library supports sampling on both the client and server side.

00:07:10 - Demo Start: Beginning the demonstration of a research agent that uses an MCP tool to query BigQuery.

00:08:23 - Code Walkthrough: Validation: Showing how Pydantic is used for output validation and automatic retries (model_retry).

00:09:00 - Code Walkthrough: Context Logging: Demonstrating the use of mcp_context.log to send progress updates back to the client.

00:10:51 - MCP Server Setup: Showing the code for setting up an MCP server using fast_mcp.

00:11:54 - Design Pattern: Inference Inside the Tool: Explaining the benefit of having the tool perform its own LLM inference to reduce the context burden on the main agent.

00:12:27 - Main Application Code: Reviewing the client-side code that defines the agent and registers the MCP tool.

00:13:16 - Observability with Logfire: Switching to the Logfire UI to trace the execution of the agent's query.

00:14:09 - Observing Sampling in Action: Pointing out the specific span in the trace that shows the tool making an LLM call back through the client via sampling.

00:14:48 - Inspecting the SQL Query: Showing how the observability tool can be used to see the exact SQL query that was generated by the internal agent.

00:15:15 - Conclusion: Final summary of the talk's points.

## The rise of the agentic economy on the shoulders of MCP — Jan Curn, Apify

- Upload date: 2025-07-18
- Video: https://www.youtube.com/watch?v=blW-lSd5CYQ
- Transcript: raw/20250718_blW-lSd5CYQ/blW-lSd5CYQ.en-orig.vtt
- Metadata: raw/20250718_blW-lSd5CYQ/blW-lSd5CYQ.info.json

Thanks to MCP and all the MCP server directories, agents can now autonomously discover new tools and other agents. This lays down the foundation for the future agentic economy, where businesses will sell to autonomous agents (B2A) and eventually agents will sell to other agents (A2A).

But one key part is still missing: agents do not have a standard way to subscribe to external services and pay for them.

In this talk, we’ll show how to give agents full autonomy to discover and pay for new external MCP-enabled services, even if those services don’t support it, using a little-known MCP server nesting capability. We’ll also cover how to monetize AI agents and the B2A/A2A business models.



---related links---

https://x.com/jancurn
https://www.linkedin.com/in/jancurn/
https://blog.apify.com/author/jancurn/
https://apify.com/

Timestamps
[00:00] Emergence of Intelligence

[02:42] Apify and the Agentic Economy

[07:30] Challenges and Solutions for Agent Autonomy

[11:50] Demo of Apify's MCP Integration

[15:52] Monetization and Future Outlook

## Shipping an Enterprise Voice AI Agent in 100 Days - Peter Bar, Intercom Fin

- Upload date: 2025-07-18
- Video: https://www.youtube.com/watch?v=HOYLZ7IVgJo
- Transcript: raw/20250718_HOYLZ7IVgJo/HOYLZ7IVgJo.en-orig.vtt
- Metadata: raw/20250718_HOYLZ7IVgJo/HOYLZ7IVgJo.info.json

What does it take to go from blank page to live enterprise voice agent in 100 days?

That’s the challenge we took on with Fin Voice at Intercom. Enterprise customer service demands high-quality, reliable voice interactions - but delivering that fast means wrestling with tough problems like latency, hallucinations, voice quality, and answer accuracy.

We rapidly evaluated and integrated a full voice stack - including transcription, language model, text-to-speech, retrieval-augmented generation, and telephony - while designing tools that fit seamlessly into existing human support workflows.

In this session, I’ll share key lessons from our accelerated development of Fin Voice. We'll explore the technical and operational hurdles we faced, the trade-offs we made, and how we built deployment and handover tools that work for customer service teams. You'll leave with insights into building AI-driven voice products that are both powerful and practical.

About Peter Bar
I’m Peter Bar, a Product Lead with over 10 years of experience in the tech industry. At Intercom, I’m responsible for Voice AI initiatives and led the development and launch of Fin Voice, our AI voice agent. My background spans both B2B and consumer tech, blending technical depth with strategic product leadership. Before Intercom, I drove growth and customer experience efforts at Deliveroo (food delivery) and worked on music discovery products at Shazam. I hold a Master’s degree in Computer Science from Imperial College London.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Full Spec MCP: Hidden Capabilities of the MCP spec — Harald Kirschner, Microsoft/VSCode

- Upload date: 2025-07-18
- Video: https://www.youtube.com/watch?v=ExeD-8gFUMM
- Transcript: raw/20250718_ExeD-8gFUMM/ExeD-8gFUMM.en-orig.vtt
- Metadata: raw/20250718_ExeD-8gFUMM/ExeD-8gFUMM.info.json

The true power of Model Context Protocol emerges when clients and servers collaborate across the full spectrum of the specification. This talk presents practical examples of how VS Code's comprehensive implementation of MCP transforms the capabilities of AI assistants, making them more contextual, efficient, and user-friendly. We'll showcase advanced features like dynamic tool discovery and workspace-aware roots, demonstrating how they create experiences impossible with standard tools integrations while confronting the reality gap between MCP's theoretical potential and practical implementation challenges.

Timestamps

[00:00] Introduction to MCP and its Current State

[01:42] The "MCP is just another API wrapper" Syndrome

[02:51] VS Code's Full Spec Support

[03:40] Challenges with Tools and Solutions

[06:35] Resources and Their Importance

[07:41] Sampling

[09:21] Developer Experience Improvements

[10:28] Staying Updated with the Spec

[10:53] Key Upcoming Features and Community Efforts

[12:46] Call to Action

## What We Learned from Using LLMs in Pinterest — Mukuntha Narayanan, Han Wang, Pinterest

- Upload date: 2025-07-16
- Video: https://www.youtube.com/watch?v=XdAWgO11zuk
- Transcript: raw/20250716_XdAWgO11zuk/XdAWgO11zuk.en-orig.vtt
- Metadata: raw/20250716_XdAWgO11zuk/XdAWgO11zuk.info.json

Pinterest Search integrates Large Language Models (LLMs) to enhance relevance scoring by combining search queries with rich multimodal content, including visual captions, link-based text, and user curation signals. A semi-supervised learning framework enables scaling to large and multilingual datasets, going beyond English and limited human labels. These LLM-driven models are distilled into efficient architectures for real-time serving, with experimental validation and large-scale deployment demonstrating substantial improvements in search relevance for Pinterest users worldwide.


Timestamps
[00:00] Introduction to Pinterest and its search functionality.

[01:52] Overview of the Pinterest search backend architecture.

[02:29] The search relevance model.

[02:55] Key learnings from using LLMs for search relevance.

[05:04] The value of VLM-generated captions and user actions as content annotations.

[07:16] Productionizing LLMs with knowledge distillation.

[12:14] The utility of relevance-tuned LLM embeddings as general-purpose semantic representations.

[13:55] Q&A session.

## 360Brew: LLM-based Personalized Ranking and Recommendation - Hamed and Maziar, LinkedIn AI

- Upload date: 2025-07-16
- Video: https://www.youtube.com/watch?v=U0S6CfzAY5c
- Transcript: raw/20250716_U0S6CfzAY5c/U0S6CfzAY5c.en-orig.vtt
- Metadata: raw/20250716_U0S6CfzAY5c/U0S6CfzAY5c.info.json

We will give a talk about our journey of building a foundation model for solving ranking and recommendation tasks

About Hamed Firooz
Principal AI Scientist at LinkedIn Core AI. With 15 years in large-scale AI, Hamed leads the 50-person team behind LinkedIn’s 150-billion-parameter foundation model that personalizes the experience for hundreds of millions of members. Before LinkedIn, he led multimodal Content Understanding model at Meta AI that handle tens of billions of daily requests. His work spans open-source projects like Hateful Memes benchmark dataset and papers at venues such as NeurIPS and ICML.

About Maziar Sanjabi
Maziar is a Principal Scientist at LinkedIn AI, where he leads efforts in training large language models (LLMs) for personalization tasks. Prior to joining LinkedIn AI, he worked at Meta AI, applying AI research to the development of multimodal systems for real-world applications. With over a decade of experience in AI research across both industry and academia, Maziar has a proven track record of building and scaling cutting-edge AI technologies, including LLMs, multimodal systems, and privacy-aware AI. He has published over 60 papers, many of which have been featured in top-tier AI conferences such as NeurIPS, ICML, ICLR, ACL, EMNLP, and CVPR.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## RL for Autonomous Coding — Aakanksha Chowdhery, Reflection.ai

- Upload date: 2025-07-16
- Video: https://www.youtube.com/watch?v=QluDzKVfp6A
- Transcript: raw/20250716_QluDzKVfp6A/QluDzKVfp6A.en-orig.vtt
- Metadata: raw/20250716_QluDzKVfp6A/QluDzKVfp6A.info.json

The models and techniques to build fully autonomous coding agents - not just coding copilots - are already here. In this talk, former Google DeepMind staff research scientist, now CEO of Reflection Misha Laskin will present new research on post-training open weight LLMs for autonomous SWE tasks. He’ll focus on how scaling LLMs with Reinforcement Learning improves the autonomous coding capabilities of LLMs, and provide insight on the technical challenges required to train such systems at scale.

About Aakanksha Chowdhery 
Aakanksha Chowdhery is a Research Leader at Reflection AI pushing the frontier of reasoning for coding agents. She is also an adjunct faculty at Stanford. Before her startup journey, she was the technical Lead of 540B PaLM model and lead researcher at Google in pre-training, scaling, and post-training of Large Language Models. She was a lead researcher in Gemini, PaLM-E, MedPaLM, and Pathways project at Google. Prior to joining Google, she led interdisciplinary research initiatives at Microsoft Research and Princeton University across machine learning and distributed systems.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

Timestamps:
[00:00:00] Introduction to LLMs and Scaling Laws

[00:01:41] Emergent Behavior in LLMs

[00:04:00] Reinforcement Learning from Human Feedback (RLHF)

[00:06:11] Inference-Time Scaling and Verification

[00:10:33] Challenges with Inference-Time Scaling

[00:11:16] The Next Frontier: Reinforcement Learning for Correct Generation

[00:13:20] Challenges in Scaling RL

[00:14:58] Autonomous Coding as a Prime Domain for RL

[00:15:53] Reflection.ai's Mission

## Transforming search and discovery using LLMs — Tejaswi & Vinesh, Instacart

- Upload date: 2025-07-16
- Video: https://www.youtube.com/watch?v=PjaVHm_3Ljg
- Transcript: raw/20250716_PjaVHm_3Ljg/PjaVHm_3Ljg.en-orig.vtt
- Metadata: raw/20250716_PjaVHm_3Ljg/PjaVHm_3Ljg.info.json

Learn how Instacart uses cutting-edge LLMs to redefine search and product discovery. 
- Explore innovative solutions overcoming traditional search engine limitations for grocery shopping.
- Discover how LLMs enhance user intent understanding and generate engaging content.
- See practical applications of LLM technology to improve search relevance and user experience.

About Tejaswi Tenneti
Tejaswi Tenneti is currently a Director of Machine Learning at Instacart, the north american leader in online grocery. Prior to Instacart, Tejaswi was a tech lead in machine learning teams at Apple and Oracle where he worked on various applications related to Search and Recommendations for local maps data and Enterprise. Tejaswi holds a BS from IIIT, Allahabad and an MS from Stanford University specializing in AI

About Vinesh Gudla
Vinesh is a Staff Machine Learning Engineer at Instacart on the search and discovery team. He has previously worked on balancing multiple objectives in search in a marketplace and has authored numerous well-received blogposts and articles about his work. He is currently working on bringing Generative AI to production at ecommerce scale at Instacart.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## The State of Generative Media - Gorkem Yurtseven, FAL

- Upload date: 2025-07-16
- Video: https://www.youtube.com/watch?v=P370D8Kmlkw
- Transcript: raw/20250716_P370D8Kmlkw/P370D8Kmlkw.en-orig.vtt
- Metadata: raw/20250716_P370D8Kmlkw/P370D8Kmlkw.info.json

Generative AI is reshaping the creative landscape, enabling the production of images, audio, and video with unprecedented speed and sophistication. This session offers an in-depth exploration of the current state of generative media, highlighting cutting-edge models, platforms, and tools that are transforming the industry.

About Gorkem Yurtseven
Gorkem Yurtseven is the co-founder and CTO of fal, a generative media platform empowering developers to build with cutting-edge AI models. Previously, he was a Senior Software Engineer at AWS and holds a degree in Computer Engineering from the University of Pennsylvania.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter


Timestamps
[00:00:00] Introduction to Generative Media

[00:03:49] Evolution of Generative Image Models

[00:05:11] Impact on Industries

[00:10:50] The Rise of Generative Video

[00:14:23] Future of Generative Media

[00:16:33] Conclusion and Call to Action

## Teaching Gemini to Speak YouTube: Adapting LLMs for Video Recommendations to 2B+DAU - Devansh Tandon

- Upload date: 2025-07-16
- Video: https://www.youtube.com/watch?v=LxQsQ3vZDqo
- Transcript: raw/20250716_LxQsQ3vZDqo/LxQsQ3vZDqo.en-orig.vtt
- Metadata: raw/20250716_LxQsQ3vZDqo/LxQsQ3vZDqo.info.json

YouTube recommendations drive the majority of video watch time for billions of daily users. Traditionally powered by large embedding models (LEMs), we're undertaking a fundamental shift: rebuilding our recommendation stack using foundation models like Gemini. This talk dives into our engineering journey adapting general-purpose LLMs (Gemini) for the highly specialized, dynamic, and massive-scale task of YouTube recommendations.

We'll discuss:

SemanticID: creating a "language" for YouTube videos, from our paper last year – Better Generalization with Semantic IDs: A Case Study in Ranking for Recommendations
Adapting Gemini checkpoints to understand SemanticID
Generative Video Retrieval with prompts
There’s a lot of attention on the LLM-led transformation of Search (with AI Overviews, Perplexity, ChatGPT-Search etc). However, across large consumer apps, it’s the recommendation systems & feeds that drive most consumer engagement, not just search. This talk is about the LLM-led transformation of recommendations & feeds – building a recommendation engine on top of Gemini.

About Devansh Tandon
Devansh Tandon is a Product Manager at Google, leading YouTube’s discovery system and GenAI efforts. At YouTube, Devansh leads a team of research scientists and ML engineers to develop the recommendation engine, which powers the majority of YouTube watchtime for billions of daily active users.

He led Google DeepMind & YouTube partnerships, and has launched GenAI products including video summaries & AI dubbing for YouTube. At DeepMind, Devansh led the development of a new generative recommendation system – adapting Gemini to power YouTube recommendations – from research to scaled consumer launch.

Previously, Devansh has led AI teams in Google Search, Google News and Google Ads. He graduated Magna Cum Laude from Yale University, with a BS in Computer Science and Economics.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Netflix's Big Bet: One model to rule recommendations: Yesu Feng, Netflix

- Upload date: 2025-07-16
- Video: https://www.youtube.com/watch?v=AbZ4IYGbfpQ
- Transcript: raw/20250716_AbZ4IYGbfpQ/AbZ4IYGbfpQ.en-orig.vtt
- Metadata: raw/20250716_AbZ4IYGbfpQ/AbZ4IYGbfpQ.info.json

Discuss the foundation model strategy for personalization at Netflix based on this post https://netflixtechblog.com/foundation-model-for-personalized-recommendation-1a0bd8e02d39 and recent developments.

About Yesu Feng
Yesu Feng is a staff research scientist/engineer at Netflix, his work focused on generative foundation models for personalized recommendation. Before Netflix, he was at Linkedin and later Uber, worked on homepage feed and marketplace optimization, respectively.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Measuring AGI: Interactive Reasoning Benchmarks for ARC-AGI-3 — Greg Kamradt, ARC Prize Foundation

- Upload date: 2025-07-16
- Video: https://www.youtube.com/watch?v=3XmFPwjG8pg
- Transcript: raw/20250716_3XmFPwjG8pg/3XmFPwjG8pg.en-orig.vtt
- Metadata: raw/20250716_3XmFPwjG8pg/3XmFPwjG8pg.info.json

ARC Prize Foundation is building the North Star for AGI—rigorous, open benchmarks that track reasoning progress in modern AI. We'll show why static AGI evaluations are useful, but fall short when comparing models to human intelligence. Sneak peak preview of ARC-AGI-3: a dynamic, game-like benchmark launching Q1 '26.

About Greg Kamradt   
Greg Kamradt is President of the ARC Prize Foundation, the ARC‑AGI benchmark series that challenges frontier AI models on out‑of‑distribution reasoning tasks.​ He has taught thousands of developers to build production AI applications.​

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Recsys Keynote: Improving Recommendation Systems & Search in the Age of LLMs - Eugene Yan, Amazon

- Upload date: 2025-07-16
- Video: https://www.youtube.com/watch?v=2vlCqD6igVA
- Transcript: raw/20250716_2vlCqD6igVA/2vlCqD6igVA.en-orig.vtt
- Metadata: raw/20250716_2vlCqD6igVA/2vlCqD6igVA.info.json

Recommendation systems and search have long adopted advances in language modeling, from early adoption of Word2vec for embedding-based retrieval to the transformative impact of GRUs, Transformers, and BERT on predicting user interactions. Now, the rise of large language models (LLMs) is inspiring innovations in model architecture, scalable system designs, and richer customer experiences.

In this keynote, we'll dive into cutting-edge industry applications of LLMs in recommendation and search systems, exploring real-world implementations and measurable outcomes. Join us for an look at current trends and an exciting vision of how LLM-driven techniques will shape the future of content discovery and intelligent search.

About Eugene Yan
Eugene Yan is a Principal Applied Scientist at Amazon building recommendation systems and AI-powered products that serve customers at scale. He's led ML/AI teams at Alibaba, Lazada, and a Healthtech Series A. He writes about RecSys, LLMs, and engineering at eugeneyan.com.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

Timestamps:

[00:00] Introduction to Language Modeling in Recommendation Systems

[01:31] Challenge 1: Hash-based Item IDs

[02:14] Solution: Semantic IDs

[05:37] Challenge 2: Data Augmentation and Quality

[06:10] Solution: LLM-Augmented Synthetic Data

[06:21] Indeed Case Study

[10:37] Spotify Case Study

[13:34] Challenge 3: Separate Systems and High Operational Costs

[14:24] Solution: Unified Models

[14:51] Netflix Case Study (Unicorn)

[16:46] Etsy Case Study (Unified Embeddings)

[20:26] Key Takeaways

## Bolt.new: How we scaled $0-20m ARR in 60 days, with 15 people — Eric Simons, Bolt

- Upload date: 2025-07-15
- Video: https://www.youtube.com/watch?v=s8RM8uYxkoY
- Transcript: raw/20250715_s8RM8uYxkoY/s8RM8uYxkoY.en-orig.vtt
- Metadata: raw/20250715_s8RM8uYxkoY/s8RM8uYxkoY.info.json

Tiny Teams are the future of how startups are built, and it all comes down to team culture, decision making, tooling choices, and endless grit.

In this talk, Eric will share the high octane insights & learnings of how the 2nd fastest growing product in history _made it_ with a team of less than 15 people.

About Eric Simons
CEO of Bolt.new

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Rethinking Team Building: how a 30-person Startup serves 50 Million Users — Grant Lee, Gamma

- Upload date: 2025-07-15
- Video: https://www.youtube.com/watch?v=q8zoXAbmJdI
- Transcript: raw/20250715_q8zoXAbmJdI/q8zoXAbmJdI.en-orig.vtt
- Metadata: raw/20250715_q8zoXAbmJdI/q8zoXAbmJdI.info.json

The central thesis of this talk is that in the rapidly evolving age of AI, startups and tech companies should reject the traditional "blitzscaling" model of hyper-growth and specialized roles. Instead, they should focus on building lean, agile teams of generalists and "player coaches" who can adapt quickly to change. Grant Lee argues that investing in brand and culture from day one is a more scalable and sustainable way to build a company than simply hiring more people.

Timestamps

00:00:00 - Introduction to Gamma and its "content-first" philosophy.

00:01:55 - Shifting focus from product innovation to organizational innovation.

00:04:19 - The case for hiring generalists over specialists.

00:06:48 - Introducing the "player coach" leadership model.

00:08:57 - The importance of scaling with brand and culture.

00:12:04 - Q&A session begins.

About Grant Lee
Grant has spent the past 10+ years building tech startups and has a background in finance and operations. He was interim CFO at Optimizely and the COO of Clearbrain, two YC startups. He grew up in the bay area and studied at Stanford, where he received his B.S. and M.S. in mechanical engineering. He is currently building Gamma, an AI-powered platform to create presentations, websites, and more.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Using OSS models to build AI apps with millions of users — Hassan El Mghari

- Upload date: 2025-07-15
- Video: https://www.youtube.com/watch?v=gcseUQJ6Gbg
- Transcript: raw/20250715_gcseUQJ6Gbg/gcseUQJ6Gbg.en-orig.vtt
- Metadata: raw/20250715_gcseUQJ6Gbg/gcseUQJ6Gbg.info.json

In this talk, Hassan will go over how he builds open source AI apps that get millions of users like roomGPT.io 2.9 million users, restorePhotos.io 1.1 million users, Blinkshot.io 1 million visitors, and LlamaCoder.io 1.4 million visitors. He'll go over his journey in AI, demo some of the apps that he's built, and dig into his tech stack and code to explain how he builds these apps from scratch. He’ll also go over how to market them and go over his top tips and tricks for building great full-stack AI applications quickly and efficiently.

This talk will start from first principles and give you a glimpse into Hassan’s workflow of idea - working app - many users. Attendees should come out of this session equipped with the resources to build impressive AI applications and understand some of the behind the scenes of how they’re built and marketed. This will hopefully serve as an educational and inspirational talk that encourages builders to go build cool things.

About Hassan El Mghari
Hassan El Mghari is a software engineer based in New York specializing in building full-stack AI applications. His AI applications have a combined user base of over 3 million. He currently leads the developer relations team at Together.ai, where his work includes building example AI apps, creating content, and educating developers on AI development.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Benchmarks Are Memes: How What We Measure Shapes AI—and Us - Alex Duffy, Every.to

- Upload date: 2025-07-15
- Video: https://www.youtube.com/watch?v=W3khHzajE04
- Transcript: raw/20250715_W3khHzajE04/W3khHzajE04.en-orig.vtt
- Metadata: raw/20250715_W3khHzajE04/W3khHzajE04.info.json

Benchmarks shape more than just AI models—they shape our future. The things we choose to measure become self-fulfilling prophecies, guiding AI toward specific abilities and, ultimately, defining humanity’s evolving role in the AI era. Today’s benchmarks have propelled incredible progress, but now we have an exciting opportunity: thoughtfully designing benchmarks around what genuinely matters to us—cooperation, creativity, education, and meaningful human experiences.

In this talk, we’ll explore how benchmarks function as powerful cultural memes, influencing not only technical outcomes but societal direction. Drawing on practical examples we have seen at Every consulting in industries like finance, journalism, education, and even personally making AI play diplomacy. We’ll uncover what makes a benchmark impactful, approachable, and inspiring. You’ll see our engaging new AI Diplomacy benchmark demo, illustrating vividly how thoughtful evaluation design can excite both engineers and the wider community.

You’ll hopefully walk away inspired and equipped to define benchmarks intentionally, helping steer AI toward outcomes that truly matter.

About Alex Duffy
I’m Alex Duffy. I lead AI strategy at Every Inc., helping teams across industries put AI into practice. Previously, I co-founded AI Camp, teaching thousands of students to build their own AI projects, and launched Salt AI, creating tools to help researchers, designers, and creators bring ideas to life. I’m passionate about building teams and tools to empower people with AI. I really believe in creating technology that works for us, not that is work for us

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Building a 10 person unicorn - Max Brodeur-Urbas, Gumloop

- Upload date: 2025-07-15
- Video: https://www.youtube.com/watch?v=Qw9P1zvCupE
- Transcript: raw/20250715_Qw9P1zvCupE/Qw9P1zvCupE.en-orig.vtt
- Metadata: raw/20250715_Qw9P1zvCupE/Qw9P1zvCupE.info.json

An overview of how Gumloop is scaling automation across companies like Instacart, Webflow and Shopify with less than 10 people.

About Max Brodeur-Urbas
ex-microsoft engineer, started Gumloop in my bedroom and scaled to millions in ARR with a hyper-lean team

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Small AI Teams with Huge Impact — Vik Paruchuri, Datalab

- Upload date: 2025-07-15
- Video: https://www.youtube.com/watch?v=K-iYKDMFKhE
- Transcript: raw/20250715_K-iYKDMFKhE/K-iYKDMFKhE.en-orig.vtt
- Metadata: raw/20250715_K-iYKDMFKhE/K-iYKDMFKhE.info.json

We scaled Datalab 5x this year - to 7-figure ARR, with customers that include tier 1 AI labs. We train custom models for document intelligence (OCR, layout), with popular repos surya and marker.

I'll talk about a new approach to building AI teams, including lessons I learned from Jeremy Howard, and how we manage building popular repos, scaling revenue, and training models with a tiny team.

About Vikas Paruchuri
CEO of Datalab

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Prompt Engineering and AI Red Teaming — Sander Schulhoff, HackAPrompt/LearnPrompting

- Upload date: 2025-07-14
- Video: https://www.youtube.com/watch?v=_BRhRh7mOX0
- Transcript: raw/20250714__BRhRh7mOX0/_BRhRh7mOX0.en-orig.vtt
- Metadata: raw/20250714__BRhRh7mOX0/_BRhRh7mOX0.info.json

Learn from the creator of Learn Prompting, the internet's 1st Prompt Engineering guide (released 2 months before ChatGPT), and HackAPrompt, the World's 1st AI Red Teaming competition.

My talk will cover topics ranging from the history of prompt engineering to the most advanced research-backed prompt engineering techniques.

I will also discuss the origins of prompt injection and AI red teaming, as well as the current state of industry and the need for agentic red teaming.

https://www.hackaprompt.com

About Sander Schulhoff
I'm Sander Schulhoff, the founder and CEO of HackAPrompt and Learn Prompting. I created the first Prompt Engineering guide on the internet, two months before ChatGPT was released, which has taught 3 million people how to prompt ChatGPT. I also ran, in collaboration with OpenAI, the first AI Red Teaming Hackathon (an event that nearly doubled a similar one by the White House). Today, HackAPrompt partners with the Frontier AI labs to produce research that makes their models more secure. My background is primarily in NLP and deep reinforcement learning. I recently led the team behind The Prompt Report, the most comprehensive study of prompt engineering ever done. Our 76-page survey, co-authored with OpenAI, Microsoft, Google, Princeton, Stanford, and other leading institutions, analyzed 1,500+ academic papers and covered 200+ prompting techniques.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Automating Escrow with USDC and AI - Corey Cooper, Circle

- Upload date: 2025-07-14
- Video: https://www.youtube.com/watch?v=AXMdSqdoGHM
- Transcript: raw/20250714_AXMdSqdoGHM/AXMdSqdoGHM.en-orig.vtt
- Metadata: raw/20250714_AXMdSqdoGHM/AXMdSqdoGHM.info.json

This workshop explores how USDC, AI, and smart contracts can streamline escrow by automating fund release based on task or process verification. By using AI to interpret off-chain signals such as document validation, delivery confirmations, or milestone completion, we can trigger secure, programmable USDC payouts without manual intervention. The result is a faster, trust-minimized escrow system ideal for services, trade, and gig economy use cases.

About Corey Cooper
I'm a developer who was once a high school basketball scout, where I built scouting technology to make data more accessible for college coaches. A lifelong Lakers fan from Atlanta, I love basketball and have spent my career building enterprise software. With over 15 years of experience as a solutions engineer, I bring a mix of technical depth, business insight, and hands-on leadership to product launches. Today, I am passionate about the programmability of money, now empowered by smart contracts, and how it is reshaping what is possible in digital finance.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Survive the AI Knife Fight: Building Products That Win — Brian Balfour, Reforge

- Upload date: 2025-07-14
- Video: https://www.youtube.com/watch?v=1MVh05GDydE
- Transcript: raw/20250714_1MVh05GDydE/1MVh05GDydE.en-orig.vtt
- Metadata: raw/20250714_1MVh05GDydE/1MVh05GDydE.info.json

If you’ve ever been blocked by vague specs, shifting goals, or chasing “vibes,” things have only gotten messier in the age of AI. Everyone is obsessing over engineers doing PM work and PMs cranking out prototypes—but that skips the hardest question: What should we build, and why will it win? Today’s competitive landscape is a knife-fight. When it’s trivial to ship “something,” true differentiation becomes brutally difficult.

At Reforge, we built AI agents that analyze user feedback at scale, perform real-time market analysis, model feature impact, and run continuous user research -- pushing us to rethink what "product work” actually looks like.

In this talk, we’ll explore:

- How to find a seam within the red ocean of incumbents, well-funded upstarts, and the horde of startups.
- How to use real-time feedback analysis, competitive monitoring, synthetic users, AI-native research to understand impact before it ships.
- How to architect workflows where human intuition and machine intelligence ship product side by side.

About Brian Balfour
Brian Balfour, Founder/CEO of Reforge, previously VP Growth @ HubSpot. Prior to Reforge, he has started multiple VC backed companies, and grown user bases to millions of daily active users.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## How LLMs work for Web Devs: GPT in 600 lines of Vanilla JS - Ishan Anand

- Upload date: 2025-07-13
- Video: https://www.youtube.com/watch?v=ZuiJjkbX0Og
- Transcript: raw/20250713_ZuiJjkbX0Og/ZuiJjkbX0Og.en-orig.vtt
- Metadata: raw/20250713_ZuiJjkbX0Og/ZuiJjkbX0Og.info.json

Don't be intimidated. Modern AI can feel like magic, but underneath the hood are principles that web developers can understand, even if you don't have a machine learning background. In this workshop, we'll explore a complete GPT-2 inference implementation built entirely in Vanilla JS. This JavaScript translation of the popular "Spreadsheets-are-all-you-need" approach will let you debug and step through a real LLM line by line without the overhead of learning a new language, framework, or even IDE.

All the major LLMs, including ChatGPT, Claude, DeepSeek, and Llama, inherit from GPT-2's architecture, making this exploration a solid foundation to understand modern AI systems and comprehend the latest research.

While we won't have time to cover everything, you'll gain the essential knowledge to understand the key concepts that matter when building with LLMs, including how they:

- Convert raw text into meaningful tokens
- Represent semantic meaning through vector embeddings
- Train neural networks through gradient descent
- Generate text with sampling algorithms like top-k, top-p, and temperature

This intense but beginner-friendly workshop is designed specifically for web developers diving into ML and AI for the first time. It’s your "missing AI degree" in just two hours. You'll walk away with an intuitive mental model of how Transformers work that you can apply immediately to your own LLM-powered projects.

About Ishan Anand
Ishan Anand is an AI consultant and technology executive specializing in Generative AI and LLMs. He created "Spreadsheets-are-all-you-need," an innovative course that demystifies large language models by implementing GPT-2 entirely in Excel. As the former CTO and co-founder of Layer0 (acquired by Edgio), and most recently Vice-President of Product Management for Edgio, he's led teams in developing cutting-edge solutions in web performance, edge computing, and AI/ML for enterprise web applications. Ishan brings deep technical expertise from his dual B.S. degrees in Mathematics and EECS from MIT, combined with a unique ability to make advanced technology accessible to broader audiences.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

Timestamps
00:00 Introduction to the Talk and Conference
01:24 Mission: Breaking Clark's Third Law (Demystifying LLMs)
02:45 Overview of the "Spreadsheets are All You Need" Approach
04:14 Today's Approach: Vanilla JavaScript Implementation
04:47 Background Needed for the Workshop
05:22 Key Resources for the Workshop
05:50 Simplified GPT-2 Diagram as a Roadmap
07:07 Quick Tour of the JavaScript Implementation of GPT-2
12:20 Understanding Large Language Models (LLMs)
17:47 Tokenization: Splitting Text into Subword Units
33:12 Embeddings: Token and Position Embeddings
56:51 Attention Mechanism
01:02:57 Multi-Layer Perceptron (MLP) and Backpropagation
01:16:07 Iteration: Refining Predictions Across Blocks
01:17:49 Language Head: Turning Embeddings Back into Tokens
01:23:18 Chat GPT vs. GPT-2: Key Innovations
01:31:37 Summary and Conclusion
01:35:13 Q&A Session

## [Workshop] AI Pipelines and Agents in Pure TypeScript with Mastra.ai — Nick Nisi, Zack Proser

- Upload date: 2025-07-12
- Video: https://www.youtube.com/watch?v=FWlRHPZWyHE
- Transcript: raw/20250712_FWlRHPZWyHE/FWlRHPZWyHE.en-orig.vtt
- Metadata: raw/20250712_FWlRHPZWyHE/FWlRHPZWyHE.info.json

This hands-on workshop introduces Mastra.ai, a TypeScript framework that streamlines the development of agentic AI systems compared to traditional approaches using LangChain and vector databases. Participants will learn to build structured AI workflows with composable tools and reliable control, enabling them to create internal AI assistants that can handle requests like data cleaning, email drafting, and document summarization with minimal code. The session covers Mastra installation, running a local MCP server, defining tools and agents in TypeScript, using the Mastra playground, and implementing practical examples such as RAG setups and tool-chaining agents—all designed to equip attendees with the skills to develop scalable AI-driven internal tools based on sound software engineering principles rather than just experimental prompts.

About Nick Nisi
Nick Nisi is an elite software engineer who is a veteran of open source web development, a lover of karaoke, an advocate for diversity in tech, a conference organizer extraordinaire, a lover of new experiences, and a beacon of expertise, kindness and hope for his development team.

About Zack Proser
Zachary Proser builds AI systems that actually ship. For over thirteen years at Cloudmark, Cloudflare, Gruntwork, Pinecone, and now WorkOS, he’s worked across the stack—from infrastructure to interface—shipping production code.

At WorkOS, he shares what he learns in the open: creating sample applications and architectures, technical guides, and real-world lessons that make identity, security, and AI accessible. His posts are known for their copy-paste readiness and refusal to hand-wave.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## AI Engineering with the Google Gemini 2.5 Model Family - Philipp Schmid, Google DeepMind

- Upload date: 2025-07-11
- Video: https://www.youtube.com/watch?v=zK9lYrLbjSg
- Transcript: raw/20250711_zK9lYrLbjSg/zK9lYrLbjSg.en-orig.vtt
- Metadata: raw/20250711_zK9lYrLbjSg/zK9lYrLbjSg.info.json

Hands on Workshop on learning to use Gemini 2.5 Pro in combination with Agentic tooling and MCP Servers.

About Philipp Schmid  
Philipp Schmid is a Senior AI Developer Relations Engineer at Google DeepMind working on Gemini, Gemma with the mission to help every developer and builder to create and benefit from AI in a responsible way.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## The New Code — Sean Grove, OpenAI

- Upload date: 2025-07-11
- Video: https://www.youtube.com/watch?v=8rABwKRsec4
- Transcript: raw/20250711_8rABwKRsec4/8rABwKRsec4.en-orig.vtt
- Metadata: raw/20250711_8rABwKRsec4/8rABwKRsec4.info.json

In an era where AI transforms software development, the most valuable skill isn't writing code - it's communicating intent with precision. This talk reveals how specifications, not prompts or code, are becoming the fundamental unit of programming, and why spec-writing is the new superpower.

Drawing from production experience, we demonstrate how rigorous, versioned specifications serve as the source of truth that compiles to documentation, evaluations, model behaviors, and maybe even code.

Just as the US Constitution acts as a versioned spec with judicial review as its grader, AI systems need executable specifications that align both human teams and machine intelligence. We'll look at OpenAI's Model Spec as a real-world example.

Finally, we'll end on some open questions about what the future of developer tooling looks like in a world where communication once again becomes the most important artifact in engineering.

About Sean Grove
Sean Grove works on alignment reasoning at OpenAI, helping translate high‑level intent into enforceable specs and evaluations. Before OpenAI he founded OneGraph, a GraphQL developer‑tools startup later acquired by Netlify. He has delivered dozens of technical talks worldwide on developer tooling, APIs, AI UX and design, and now alignment.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter
