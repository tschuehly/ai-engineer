# AI Engineer YouTube Index

- Channel: https://www.youtube.com/@aiDotEngineer/videos
- Generated at: 2026-05-06T11:05:31+00:00
- Since: 2025-05-06
- Until: 2026-05-06
- Videos: 431

## The Small Model Infrastructure Nobody Built (So We Did) — Filip Makraduli, Superlinked

- Upload date: 2026-05-05
- Video: https://www.youtube.com/watch?v=qdh_x-uRs9g
- Transcript: raw/20260505_qdh_x-uRs9g/qdh_x-uRs9g.en-orig.vtt
- Metadata: raw/20260505_qdh_x-uRs9g/qdh_x-uRs9g.info.json

Most embedding infrastructure assumes you know exactly which model you want ahead of time. This talk starts where that assumption breaks. Filip Makraduli walks through the real profiling mistakes, infrastructure gaps, and production constraints that led to building an embedding inference engine designed for dynamic model loading, hot-swapping, and memory-aware eviction instead of brittle one-model-per-container deployments.

If you're working on small-model inference, embeddings, or GPU infrastructure, this is a practical look at what breaks in the real world and how to design around it.

Speaker info:
- https://www.linkedin.com/in/filipmakraduli/

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

## Mastering AI Pricing: Flexible & Agile Monetization — Mayank Pant, Stripe

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

## "Software Fundamentals Matter More Than Ever" — Matt Pocock

- Upload date: 2026-04-23
- Video: https://www.youtube.com/watch?v=v4F1gFy-hqg
- Transcript: raw/20260423_v4F1gFy-hqg/v4F1gFy-hqg.en-orig.vtt
- Metadata: raw/20260423_v4F1gFy-hqg/v4F1gFy-hqg.info.json

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

## A year of Gemini progress + what comes next — Logan Kilpatrick, Google DeepMind

- Upload date: 2025-07-10
- Video: https://www.youtube.com/watch?v=wE1ZCmCLP5g
- Transcript: raw/20250710_wE1ZCmCLP5g/wE1ZCmCLP5g.en-orig.vtt
- Metadata: raw/20250710_wE1ZCmCLP5g/wE1ZCmCLP5g.info.json

Over the last year, Google and Gemini models have shown rapid progress across all dimensions (model, product, etc). Let's highlight all the work that has happened, how we got the worlds best models, and where we are going next (across both the model landscape and out AI products).

About Logan Kilpatrick
Logan leads product for Google AI Studio and works on the Gemini API. Before Google, Logan led developer relations at OpenAI.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Production software keeps breaking and it will only get worse — Anish Agarwal, Traversal.ai

- Upload date: 2025-07-10
- Video: https://www.youtube.com/watch?v=L6_NiGIEXZQ
- Transcript: raw/20250710_L6_NiGIEXZQ/L6_NiGIEXZQ.en-orig.vtt
- Metadata: raw/20250710_L6_NiGIEXZQ/L6_NiGIEXZQ.info.json

Software is eating the world. AI is eating software. AI-powered SWE means a whole lot more software is going to be written that powers mission critical systems in the coming years, with hardly any of it written by humans. Hence, when these software systems inevitably break, it’s going to be next to impossible to troubleshoot them. Towards addressing this issue, we’ll do a product launch of Traversal’s AI, a significant step towards self-healing software systems. We will showcase how it is already used to autonomously troubleshoot production incidents in some of the most complex enterprise environments.

About Anish Agarwal
Anish Agrawal is the CEO and Co-founder of Traversal, where he and his team are revolutionizing observability and troubleshooting with AI Agents. A Professor of Computer Science and Operations Research at Columbia University, Anish earned his PhD in Computer Science from MIT, specializing in causal machine learning—teaching AI to understand cause and effect from data. Despite achieving his goal of becoming a professor, Anish pivoted from academia, recognizing a once-in-a-lifetime opportunity to apply his AI research to tackle the industry’s toughest challenges, with autonomous troubleshooting at the forefront. His career also includes roles as a management consultant at BCG and research scientist at Amazon and Microsoft Research.

About Matthew Schoenbauer
Matt Schoenbauer is a founding engineer at Traversal, where he and his team are redefining observability and troubleshooting with AI agents. Previously, he was a systematic trader at Citadel Securities, operating at the core of the world’s largest equities market-making platform, where live troubleshooting in the Linux terminal was a critical part of his work. Before that, he worked in quantitative research at Proof Trading. Matt has published research across cryptography, number theory, and algebraic topology, and holds a master’s degree from Columbia University, where he focused on machine learning systems and causal machine learning.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

Timestamps:

00:00 Introduction: The Three Pillars of Software Engineering
02:10 The Worsening Problem of Troubleshooting
04:15 Why Current AI/ML Solutions are Failing
07:08 Traversal.ai's Novel Approach to Autonomous Troubleshooting
11:35 Case Study: How Traversal.ai helped Digital Ocean
16:03 The Broader Vision for Traversal.ai

## Thinking Deeper in Gemini — Jack Rae, Google DeepMind

- Upload date: 2025-07-10
- Video: https://www.youtube.com/watch?v=8EQo4J2BWKw
- Transcript: raw/20250710_8EQo4J2BWKw/8EQo4J2BWKw.en-orig.vtt
- Metadata: raw/20250710_8EQo4J2BWKw/8EQo4J2BWKw.info.json

Progress towards general intelligence has been marked by identifying fundamental intelligence bottlenecks within existing models and developing solutions that improve the architecture or training objective. From this perspective, we discuss our work on Thinking in Gemini as a solution to a bottleneck in test-time compute. We will discuss recent progress in Thinking both from the benefit of capability and steerability, and discuss where our models are headed.

About Jack Rae
Lead of Gemini Thinking, co-lead of Gemini Pre-training

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## 2025 in LLMs so far, illustrated by Pelicans on Bicycles — Simon Willison

- Upload date: 2025-07-09
- Video: https://www.youtube.com/watch?v=YpY83-kA7Bo
- Transcript: raw/20250709_YpY83-kA7Bo/YpY83-kA7Bo.en-orig.vtt
- Metadata: raw/20250709_YpY83-kA7Bo/YpY83-kA7Bo.info.json

What's changed in the world of LLMs since the AIE World's Fair last year? A lot!

I'll be taking full advantage of my role as a fiercely independent researcher to review the past 12 months of advances in the field and catch everyone up on the latest models, free from any influence of vendors or employers.

About Simon Willison
Simon Willison is the creator of Datasette, an open source tool for exploring and publishing data. He currently works full-time building open source tools for data journalism, built around Datasette and SQLite.

Prior to becoming an independent open source developer, Simon was an engineering director at Eventbrite. Simon joined Eventbrite through their acquisition of Lanyrd, a Y Combinator funded company he co-founded in 2010.

He is a co-creator of the Django Web Framework, and has been blogging about web development and programming since 2002 at simonwillison.net

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

Timestamps:

00:00 A review of the last six months in LLMs
01:08 The "Pelican Riding a Bicycle" Benchmark
02:10 AWS Nova and Llama 3.3 70B
03:30 DeepSeek and its impact
05:42 Mistral Small 3 and the rise of local models
06:45 Claude 3.7 Sonnet and GPT 4.5
08:44 Gemini 2.5 Pro, GPT-4o, and Llama 4
11:21 GPT 4.1, O3, and O4 Mini
12:05 Claude 4 and other recent releases
14:11 Amusing and concerning LLM bugs
16:58 The power of tools and reasoning in AI
17:41 Prompt injection and the "Lethal Trifecta"
18:11 The future of the pelican benchmark

## Trends Across the AI Frontier — George Cameron, ArtificialAnalysis.ai

- Upload date: 2025-07-08
- Video: https://www.youtube.com/watch?v=sRpqPgKeXNk
- Transcript: raw/20250708_sRpqPgKeXNk/sRpqPgKeXNk.en-orig.vtt
- Metadata: raw/20250708_sRpqPgKeXNk/sRpqPgKeXNk.info.json

The entire AI stack is developing faster than ever - from chips to infrastructure to models. How do you sort the signal from the noise? Artificial Analysis an independent benchmarking and insights company dedicated to helping developers and companies pick the right models and technologies for building applications. This talk will walk through the state of the frontier across the AI stack.

About George Cameron
CPO of Artificial Analysis

About Micah Hill-Smith
I'm Micah, co-founder and CEO of Artificial Analysis - an independent AI benchmarking company. We help developers understand AI capabliites and make critical decisions about models and technologies. We publish extensive benchmarking results on our public website (including intelligence, performance, cost and more), and develop reports to inform key strategic decisions. I became obsessed with benchmarking AI models initially as an AI engineer building applications, and have previously spent time as a strategy consultant with McKinsey & Company.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

Timestamps
[00:00] Introduction to Artificial Analysis: An overview of the company's work in benchmarking AI models across various modalities and metrics.

[01:54] The State of AI Progress: A look at the rapid advancements in AI since the launch of ChatGPT, with a focus on the current leaders in AI intelligence.

[04:06] The Reasoning Models Frontier: An exploration of the trade-offs between the enhanced intelligence of reasoning models and their increased latency and cost.

[08:25] The Open Weights Frontier: A discussion on the closing intelligence gap between open-weights and proprietary models, with a nod to the significant contributions from China-based AI labs.

[10:26] The Cost Frontier: An analysis of the dramatic decrease in the cost of accessing high-level AI intelligence and the implications for application development.

[14:09] The Speed Frontier: A look at the remarkable increase in the output speed of AI models and the technological advancements driving this trend.

[16:34] The Future of Compute Demand: A concluding perspective on why the demand for compute will likely continue to rise despite efficiency gains, driven by larger models, the quest for greater intelligence, and the rise of AI agents.

## Training Agentic Reasoners — Will Brown, Prime Intellect

- Upload date: 2025-07-07
- Video: https://www.youtube.com/watch?v=PbHm2qKnu10
- Transcript: raw/20250707_PbHm2qKnu10/PbHm2qKnu10.en-orig.vtt
- Metadata: raw/20250707_PbHm2qKnu10/PbHm2qKnu10.info.json

This talk will be a technical deep dive into RL for agentic reasoning via multi-turn tool calling, similar to OpenAI's o3 and Deep Research. In particular, we'll cover:

- When, why, and how
- GRPO vs PPO vs etc
- Designing environments and rewards
- Survey of recent research highlights
- Results on example tasks
- Overview of open-source ecosystem (libraries, compute requirements, tradeoffs, etc.)

About Will Brown
Will Brown is a Research Engineering Lead at Prime Intellect, focusing on RL for reasoning and agents. He previously held research roles at Morgan Stanley and AWS, and completed his PhD in Computer Science at Columbia University.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

Timestamps
[00:00] Introduction to the idea that reasoning and agents are similar.
[01:05] The growing effectiveness of Reinforcement Learning (RL) in AI.
[03:04] The complexities and challenges of implementing RL.
[04:41] The connection between popular AI products (agents) and RL fine-tuning.
[07:18] The core process of Reinforcement Learning.
[10:21] The importance of tools and real-world tasks for agents.
[12:13] The problem of "reward hacking" and how to design better evaluations.
[14:51] Future directions for agentic systems and a practical toolkit for implementation.

## New York Times' Connections: A Case Study on NLP in Word Games — Shafik Quoraishee, NYT Games

- Upload date: 2025-07-05
- Video: https://www.youtube.com/watch?v=P_uhFGH4J9Y
- Transcript: raw/20250705_P_uhFGH4J9Y/P_uhFGH4J9Y.en-orig.vtt
- Metadata: raw/20250705_P_uhFGH4J9Y/P_uhFGH4J9Y.info.json

This session will examine the interplay between human intuition and artificial intelligence in puzzle-solving, using the popular New York Times Connections game as a practical case study.
    
    We'll investigate how gameplay can be systematically evaluated through AI algorithms, exploring machine learning strategies such as clustering, semantic mapping, and natural language processing.
    
    Attendees will gain insights into building AI-driven puzzle solvers, learn methods for quantitatively assessing gameplay complexity, and discuss the potential impacts of AI on puzzle game design and player engagement.

Timestamps [00:00]:

[01:45] Introduction to Connections

[03:50] Why Connections is Interesting for AI

[05:18] Human vs. AI Problem Solving

[06:55] AI Analysis and Methodology

[09:26] Semantic Similarity

[10:45] Relational Alignment

[12:16] Multi-dimensional Analysis

[15:44] Graph Neural Networks (GNNs)

[17:42] Motivation and Next Steps

## Claude Code & the evolution of agentic coding — Boris Cherny, Anthropic

- Upload date: 2025-07-04
- Video: https://www.youtube.com/watch?v=Lue8K2jqfKk
- Transcript: raw/20250704_Lue8K2jqfKk/Lue8K2jqfKk.en-orig.vtt
- Metadata: raw/20250704_Lue8K2jqfKk/Lue8K2jqfKk.info.json

A ten thousand foot view of the coding space, the UX of coding, and the Claude Code team's approach.

About Boris Chemy
Created Claude Code. Member of Technical Staff @Anthropic. Prev: Principal Engineer @Meta, Architect @Coatue. Author, OReilly's Programming TypeScript.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## MCP Is Not Good Yet — David Cramer, Sentry

- Upload date: 2025-07-03
- Video: https://www.youtube.com/watch?v=FCi4jT86gSw
- Transcript: raw/20250703_FCi4jT86gSw/FCi4jT86gSw.en-orig.vtt
- Metadata: raw/20250703_FCi4jT86gSw/FCi4jT86gSw.info.json

You’ve heard a lot about MCP, probably been given an AI mandate or two, and are trying to figure out what’s real and what’s make believe. 

This session will give practical advice for how you should be thinking about MCP, the implementation pit falls, and where the speaker thinks things are going. 

---related links---

https://twitter.com/zeeg
https://cra.mr
https://sentry.io

## 12-Factor Agents: Patterns of reliable LLM applications — Dex Horthy, HumanLayer

- Upload date: 2025-07-03
- Video: https://www.youtube.com/watch?v=8kMaTybvDUw
- Transcript: raw/20250703_8kMaTybvDUw/8kMaTybvDUw.en-orig.vtt
- Metadata: raw/20250703_8kMaTybvDUw/8kMaTybvDUw.info.json

Hi, I'm Dex. I've been hacking on AI agents for a while.
    
    I've tried every agent framework out there, from the plug-and-play crew/langchains to the "minimalist" smolagents of the world to the "production grade" langraph, griptape, etc.
    
    I've talked to a lot of really strong founders who are all building really impressive things with AI. Most of them are rolling the stack themselves. I don't see a lot of frameworks in production customer-facing agents.
    
    I've been surprised to find that most of the products out there billing themselves as "AI Agents" are not all that agentic. A lot of them are mostly deterministic code, with LLM steps sprinkled in at just the right points to make the experience truly magical.
    
    Agents, at least the good ones, don't follow the "here's your prompt, here's a bag of tools, loop until you hit the goal" pattern. Rather, they are comprised of mostly just software.
    
    So, I set out to answer:
    
    What are the principles we can use to build LLM-powered software that is actually good enough to put in the hands of production customers?

# The Short  Version: The 12 Factors

Even if LLMs continue to get exponentially more powerful, there will be core engineering techniques that make LLM-powered software more reliable, more scalable, and easier to maintain.

How We Got Here: A Brief History of Software
Factor 1: Natural Language to Tool Calls
Factor 2: Own your prompts
Factor 3: Own your context window
Factor 4: Tools are just structured outputs
Factor 5: Unify execution state and business state
Factor 6: Launch/Pause/Resume with simple APIs
Factor 7: Contact humans with tool calls
Factor 8: Own your control flow
Factor 9: Compact Errors into Context Window
Factor 10: Small, Focused Agents
Factor 11: Trigger from anywhere, meet users where they are
Factor 12: Make your agent a stateless reducer


---

https://x.com/dexhorthy/
https://github.com/humanlayer/12-factor-agents
https://news.ycombinator.com/item?id=43699271

## Your Personal Open-Source Humanoid Robot for $8,999 — JX Mo, K-Scale Labs

- Upload date: 2025-07-02
- Video: https://www.youtube.com/watch?v=BS92RdBvI90
- Transcript: raw/20250702_BS92RdBvI90/BS92RdBvI90.en-orig.vtt
- Metadata: raw/20250702_BS92RdBvI90/BS92RdBvI90.info.json

Introducing developer ready robots that are open-source, affordable, and easy to use. https://www.kscale.dev/

About Jingxiang Mo 
Jingxiang Mo is a founding engineer at K-Scale Labs, where he leads the fast-moving, open-source development of general-purpose humanoid robots. His work spans the full stack—from training end-to-end reinforcement-learning policies on in-house infrastructure to building the robot operating system and shipping mass-manufactured hardware such as the 5 feet tall K-Bot and 1.5 feet tall Z-Bot humanoid robots.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## The Build-Operate Divide: Bridging Product Vision and AI Operational Reality

- Upload date: 2025-07-02
- Video: https://www.youtube.com/watch?v=1__V4KTv_Gw
- Transcript: raw/20250702_1__V4KTv_Gw/1__V4KTv_Gw.en-orig.vtt
- Metadata: raw/20250702_1__V4KTv_Gw/1__V4KTv_Gw.info.json

Product leaders see AI possibilities. Operations teams see implementation chaos. That disconnect can kill promising AI features before they ever reach users.

In this session, Chris Hernandez (Chime) and Jeremy Silva (Freeplay) share an integrated framework that bridges product strategy and operational reality. You'll learn how they transformed fragmented AI workflows into a unified approach—from prototyping and prompt testing to human review loops and model benchmarking.

We’ll explore how to build evaluation systems that satisfy both technical and business stakeholders, create effective HITL processes from day one, and use QA as a strategic enabler of generative AI quality. Most importantly, we’ll show how product and operations can move beyond friction—working together to deliver AI features that scale responsibly and ship faster, with confidence.

About Jeremy Silva
A seasoned ML engineer with extensive experience building and deploying language models in the healthcare sector, Jeremy currently serves as Product Lead at Freeplay. At Freeplay, he oversees an enterprise-ready platform that empowers teams to run experiments, create evaluations, monitor production systems, and label data—all within a unified environment.

Drawing from hands-on collaboration with Freeplay's enterprise customers, Jeremy brings valuable "in-the-trenches" experience building LLM systems at scale. This direct customer engagement has also positioned him as a trusted advisor, helping organizations shape and refine their AI product roadmaps for maximum impact.

Jeremy’s unique perspective spans technical implementation and product development making him well-positioned to share insights on effectively bridging the gap between AI capabilities and real-world product outcomes.

About Chris Hernandez
I’m a Manager of Speech Analytics at Chime, where I lead a team in developing and implementing AI-powered insights to enhance member experiences and operational efficiency. With over a decade of experience in leadership, AI, and machine learning, I specialize in designing and scaling AI solutions that drive measurable impact.

At Chime, we believe that everyone can feel good about their money. We’re proud to be the most loved banking app™, providing millions of members with transparent, easy-to-use tools that help them unlock financial progress. By leveraging AI, my team helps uncover insights that improve quality, efficiency, and overall member satisfaction.

I joined Chime because of its mission and the opportunity to work alongside an incredible team focused on innovation. I’m excited about the future as we continue to push the boundaries of AI-driven quality solutions—and we’re just getting started! 🚀

**The views and opinions expressed here are my own and do not necessarily reflect the official policy or position of Chime.**

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Conquering Agent Chaos — Rick Blalock, Agentuity

- Upload date: 2025-07-01
- Video: https://www.youtube.com/watch?v=yASxPZ-tZe0
- Transcript: raw/20250701_yASxPZ-tZe0/yASxPZ-tZe0.en-orig.vtt
- Metadata: raw/20250701_yASxPZ-tZe0/yASxPZ-tZe0.info.json

Agent deployments can be dicey, especially at first.  This session goes over all the things that cause headache with deployments from serverless issues to networking issues - and how we fix them.

About Rick Blalock
Seasoned founder with exit. Developer at night and during the day if I can fit it in meetings... Scaled a mobile developer platform from hundreds to 800,000 developers. Successfully started and sold a fisheries platform & app to the world's largest fishing app with 15m+ users, and then led that company as CPO.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## The New Lean Startup — Sid Bendre, Oleve

- Upload date: 2025-07-01
- Video: https://www.youtube.com/watch?v=pQz-PgA1eJw
- Transcript: raw/20250701_pQz-PgA1eJw/pQz-PgA1eJw.en-orig.vtt
- Metadata: raw/20250701_pQz-PgA1eJw/pQz-PgA1eJw.info.json

In this session, I will be presenting a case study of Oleve's journey, revealing how we've scaled a profitable multi-product portfolio with a tiny team. I'll walk you through the emergence of "tiny teams," our two-track engineering methodology that has become our blueprint, as well as an inside look at our technical alpha – specifically how we've engineered deterministic AI agents to deliver magical and reliable consumer experiences to millions. You'll learn how we've built internal tools to grow leanly and created operating playbooks to scale operations without traditional headcount requirements. I'll also share our approach to scrappy infrastructure innovation and how our investment in internal tooling has served as a critical force multiplier. Finally, I'll give an overview of parts of the profitable portfolio playbook that keeps us lean, adaptable, and profitable across multiple product lines.

Structure of talk:
- the tiny teams revolution
- the two-track engineering approach
- technical alpha: deterministic ai agents at scale
- scrappy infrastructure innovation
- internal tooling as a multiplier
- the profitable portfolio playbook

About Sid Bendre
Sid Bendre is the co-founder of Oleve, a company building a portfolio of iconic consumer software across multiple verticals. With a lean team, Oleve has already launched two virally successful consumer AI products that have amassed over 250 million views across social media platforms. One of their products reached #4 on the App Store's Education charts in 2024 and #5 in 2025, competing alongside giants like Photomath (Google) and Duolingo. Backed by Neo, Cal Henderson (co-founder of Slack), Russell Kaplan (President of Cognition), and Maria Zhang (ex-CTO of Tinder), Oleve is building the AI infrastructure to run a $1B portfolio of consumer software over the next decade. At Oleve, Sid leads technical and AI efforts, running the “Platform” team responsible for the underlying AI infrastructure that powers their lean scaling approach. Before Oleve, Sid led AI experimentation efforts at a startup hedge fund and worked at Slack, Zendesk, and Microsoft.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Optimizing inference for voice models in production - Philip Kiely, Baseten

- Upload date: 2025-07-01
- Video: https://www.youtube.com/watch?v=gmTHs5T_YAE
- Transcript: raw/20250701_gmTHs5T_YAE/gmTHs5T_YAE.en-orig.vtt
- Metadata: raw/20250701_gmTHs5T_YAE/gmTHs5T_YAE.info.json

How do you get time to first byte (TTFB) below 150 milliseconds for voice models -- and scale it in production? As it turns out, open-source TTS models like Orpheus have an LLM backbone that lets us use familiar tools and optimizations like TensorRT-LLM and FP8 quantization to serve the models with low latency. But client code, network infrastructure, and other outside-the-GPU factors can introduce latency in the production stack. In this talk, we'll cover the basic mechanics of TTS inference, common pitfalls to avoid in integrating them into production systems, and how to extend this high-performance system to serve customized models with voice cloning and fine-tuning.

About Philip Kiely
Philip Kiely leads Developer Relations at Baseten. Prior to joining Baseten in 2022, he worked across software engineering and technical writing for a variety of startups. Outside of work, you'll find Philip practicing martial arts, reading a new book, or cheering for his adopted bay area sports teams.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## [Evals Workshop] Mastering AI Evaluation: From Playground to Production

- Upload date: 2025-07-01
- Video: https://www.youtube.com/watch?v=9iN-cPnp7xg
- Transcript: raw/20250701_9iN-cPnp7xg/9iN-cPnp7xg.en-orig.vtt
- Metadata: raw/20250701_9iN-cPnp7xg/9iN-cPnp7xg.info.json

This hands-on workshop will guide participants through the complete AI evaluation lifecycle using Braintrust, from initial prompt testing to production monitoring. Attendees will learn to build evaluation frameworks that ensure their AI applications perform reliably in real-world scenarios. Topics covered include both offline and online evaluation strategies, logging and feedback systems, and human review processes.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Agents, Access, and the Future of Machine Identity — Nick Nisi (WorkOS) + Lizzie Siegle (Cloudflare)

- Upload date: 2025-06-30
- Video: https://www.youtube.com/watch?v=px2e2OOS2Sk
- Transcript: raw/20250630_px2e2OOS2Sk/px2e2OOS2Sk.en-orig.vtt
- Metadata: raw/20250630_px2e2OOS2Sk/px2e2OOS2Sk.info.json

AI agents are calling APIs, submitting forms, and sending emails—but how do you control what they’re allowed to do? As agents act on behalf of users or organizations, traditional patterns like OAuth, session tokens, and role-based access often fall short.
In this talk, we’ll explore how machine identity is evolving to meet this new landscape. You’ll learn:

- How to think about authentication for agents (not just humans)
- What it means to authorize an action when the actor is an LLM or headless service
- Real-world strategies from WorkOS and Cloudflare for assigning, managing, and revoking agent identity and access

By the end, you’ll walk away with practical tools and mental models to build agent-powered systems that are secure, auditable, and scalable.

About Nick Nisi
Nick Nisi is an elite software engineer who is a veteran of open source web development, a lover of karaoke, an advocate for diversity in tech, a conference organizer extraordinaire, a lover of new experiences, and a beacon of expertise, kindness and hope for his development team.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Turning Fails into Features: Zapier’s Hard-Won Eval Lessons — Rafal Willinski, Vitor Balocco, Zapier

- Upload date: 2025-06-30
- Video: https://www.youtube.com/watch?v=blrovBxxN9o
- Transcript: raw/20250630_blrovBxxN9o/blrovBxxN9o.en-orig.vtt
- Metadata: raw/20250630_blrovBxxN9o/blrovBxxN9o.info.json

Every agent failure can be a roadmap to your next breakthrough. This talk reveals how Zapier's evaluation system transforms frustrating user experiences into targeted improvements, creating a data flywheel that continuously strengthens our agents. You'll learn practical approaches for building the data flywheel, detecting implicit feedback signals, building solid evals, prioritizing metrics that actually matter, and why your most reliable evals might secretly be sabotaging your performance.

About Rafal Wilinski
Rafal Wilinski is the AI Tech Lead for Zapier Agents, where he builds intelligent systems that enable workflow automation for millions of users. I'm passionate about bringing products to life from 0 to 1. Began my career with an interest for AWS cloud, where I've spent my first decade helping startups and enterprises build robust infrastructure. When not working, I'm most likely climbing or drinking whiskey (but not simultaneously).

About Vitor Balocco
Vitor is a Staff Software Engineer on the AI R&D team at Zapier, involved in most of Zapier's AI initiatives:
- Co-creator of Zapier Agents
- Co-creator of Zapier MCP
- Creator of the AI Zap builder (natural language to automation)
- Co-creator of AI custom actions

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Intro to GraphRAG — Zach Blumenfeld

- Upload date: 2025-06-30
- Video: https://www.youtube.com/watch?v=J-9EbJBxcbg
- Transcript: raw/20250630_J-9EbJBxcbg/J-9EbJBxcbg.en-orig.vtt
- Metadata: raw/20250630_J-9EbJBxcbg/J-9EbJBxcbg.info.json

Learn the foundations of GraphRAG, starting with knowledge graph construction and then common retrieval patterns.
---
GraphRAG has gone from nice-to-have to essential as AI solutions have increased in sophistication. 

This workshop will get you started, answering:

- what is GraphRAG, and when do I need it?
- what's the best way to construct a knowledge graph?
- how do I combine unstructured and structured data?
- how do I retrieve the right information?

About Zach Blumenfeld
Zach Blumenfeld is a Data Science Product Specialist at Neo4j who helps empower the market with Neo4j’s industry-leading graph data science capabilities. He has first-hand experience with various modern-day DS/ML challenges, including criminal fraud detection, identity resolution, and recommendation systems. Having served in both data science and software developer capacities, Zach has applied graph computing to law enforcement and government entities in support of missions that counter drug trafficking, human smuggling, money laundering, and child exploitation. He has led the development and deployment of full-stack graph systems designed to facilitate broad data science and operational requirements.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## The emerging skillset of wielding coding agents — Beyang Liu, Sourcegraph / Amp

- Upload date: 2025-06-30
- Video: https://www.youtube.com/watch?v=F_RyElT_gJk
- Transcript: raw/20250630_F_RyElT_gJk/F_RyElT_gJk.en-orig.vtt
- Metadata: raw/20250630_F_RyElT_gJk/F_RyElT_gJk.info.json

It's raining coding agents! But while many are saying they're feeling the AGI, others say they're not that useful for serious programming. How much is hype and how much is a skill issue? We'll share empirical observations that help explain the divergence of developer opinion. And we'll cover emergent strategies uncovered by users of Amp, a new coding agent in research preview, that can help you employ agents to complete more complex tasks in production codebases.

About Beyang Liu
Beyang is the co-founder and CTO of Sourcegraph, the company behind Sourcegraph Code Search and Amp. Beyang started his career working on software for some of the largest banks as an engineer at Palantir, where he brought a background in machine learning and data analysis at Stanford.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

Timestamps

Introduction & The State of AI in Coding
[00:14] Current Discourse: The talk begins by acknowledging the polarized debate on AI's role in coding. While some elite programmers are skeptical, many developers find significant value in AI tools, suggesting a disconnect between top-tier and mainstream experience. Liu frames the discussion by referencing opinions from figures like Jonathan Blow and Eric S. Raymond, highlighting the varied perspectives in the field.

[03:01] Paradigm Shift: The most significant mistake developers make is using new agents with old mental models. Liu emphasizes that we are in a "step function transition" in model capabilities, meaning that strategies from even six months ago are already outdated for leveraging the full power of today's agents.

The Three Eras of AI Coding Tools
[05:06] GPT-3 Era (2022): This era was defined by text completion models. The primary application was "copilot" or "autocomplete," where the AI would suggest the next few lines of code based on the preceding context.

[05:24] ChatGPT Era (2023): The introduction of instruct-tuned models like GPT-3.5 led to the rise of chatbots. In the coding world, this manifested as "ragbots," which combined a chat interface with a retrieval engine to answer questions about a codebase.

[06:11] Agent Era (Present): The current era is defined by models capable of tool use and autonomous operation. This requires a new application architecture where the agent can directly edit files, run commands, and interact with external services to accomplish a goal.

Controversial Design Philosophy for Agents
[07:27] Autonomous Edits
[09:55] Unix Philosophy
[10:24] New Applications

Live Demo: Sourcegraph's Amp Agent
[13:15] The Task
[14:30] Tool Use
[15:53] Sub-Agents
[17:56] Planning & Execution
[19:46] Nuanced Problem Solving

Best Practices from Power Users
[23:21] Detailed Prompts
[24:21] Feedback Loops
[28:03] Code Understanding
[28:36] Code Reviews

Anti-Patterns and Future Outlook
[30:35] Micromanagement
[30:46] Under-prompting
[31:52] Parallel Agents
[33:18] High-Ceiling Skill

## Securing Agents with Open Standards — Bobby Tiernay and Kam Sween, Auth0

- Upload date: 2025-06-30
- Video: https://www.youtube.com/watch?v=FZoMSupg37E
- Transcript: raw/20250630_FZoMSupg37E/FZoMSupg37E.en-orig.vtt
- Metadata: raw/20250630_FZoMSupg37E/FZoMSupg37E.info.json

Shipping AI agents that are safe for production means solving some tough identity and authorization challenges that are not always obvious at the prototype stage. In practice, this comes down to a handful of deeply technical questions:
- How do you make sure agents are only acting for the right user?
- How do you prevent over-broad API access or data leaks?
- How do you handle user approvals when there is no UI, or you need a human in the loop?
- And how do you avoid the usual pain points like manual credential sharing, stale keys, or unpredictable scopes without writing a lot of brittle, custom code?

This talk digs into the real technical trade-offs behind building secure, user-aware AI agents. We will go beyond what to do and explain why, sharing the architectural decisions, open standards, and hard lessons learned from integrating OAuth, OIDC, RAR, and async authorization into agent-driven workflows.

You will see a hands-on demo using an open-source Node.js agent and open protocols, with a focus on practical integration and no magic. The session will show how these solutions have shaped our approach to identity in GenAI and where we see the field heading next.

If you are an engineer building AI apps that need real guardrails, not just a happy-path demo, we hope to leave you with some practical patterns, design rationale, and a clear view of the trade-offs for making your own agents production ready.

About Bobby Tiernay
Bobby has spent eight years at Okta as an architect working on Auth0 and Okta Platform products. He's passionate about generative AI and loves experimenting with new tech in his free time. At work, he helps teams develop AI solutions that improve both internal tools and customer products. With a background in data security and AI governance, Bobby connects research ideas to real-world applications. He's driven by a simple goal: making identity security easier and more secure for the people who use Auth0. When tackling complex challenges, he keeps things straightforward, collaborative, and (hopefully 🤞) fun.

About Kam Sween
Kam is a Staff Engineer at Auth0 (an Okta company), where he transforms regulation-heavy legacy systems into lean, cloud-native platforms—and builds the tools that make tomorrow’s tech possible today. As the tech lead for the AI Frameworks & Services team, Kam architects the SDKs and frameworks that help developers harness AI responsibly (and without accidentally scripting Skynet).

With over a decade of experience building secure, compliant platforms around some of the most sensitive data legally storable in the cloud, Kam brings a rare blend of deep technical fluency and regulatory savvy. His career spans the full stack—from low-level infrastructure to high-level developer experience—making him a natural prototyper of what’s next.

Whether navigating contradictory compliance regimes or designing future-forward architectures, Kam is driven by a simple principle: scalability isn’t a buzzword—it’s a survival tactic. And speed? That’s just what happens when you build things the right way.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Building voice agents with OpenAI — Dominik Kundel, OpenAI

- Upload date: 2025-06-29
- Video: https://www.youtube.com/watch?v=iXhba366fQc
- Transcript: raw/20250629_iXhba366fQc/iXhba366fQc.en-orig.vtt
- Metadata: raw/20250629_iXhba366fQc/iXhba366fQc.info.json

We'll walk through the differences between chained and speech-to-speech powered voice agents, how to approach them, best practices and transform a text-based agent into our first voice-enabled agent

About Dominik Kundel
Dominik is a developer and product leader with a passion for Developer Experience and Generative AI. He's currently working on Developer Experience & SDKs at OpenAI. Previously he lead Product & Design for Twilio's Emerging Tech & Innovation organization where his team worked on customer-aware AI agents. Dominik loves tinkering with anything that can run JavaScript, from front-end servers to CLIs and coffee machines. You can find him tweeting @dkundel and in his spare time he's working on cocktails, food and photography.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter


Timestamps [0:00:00] :

Part 1: High-Level Summary and Timestamps
The video is a presentation by Dominic from OpenAI on building voice agents. The main thesis is that voice agents are the future of accessible and information-dense technology, acting as an API to the real world. The presentation introduces the new OpenAI Agents SDK for TypeScript and dives deep into the architectures, best practices, and hands-on-building of these voice agents.

[00:16] Introduction to voice agents.

[01:28] Overview of the OpenAI Agents SDK for TypeScript.

[03:27] The case for why voice agents are important.

[04:21] A look at different architectures for voice agents.

[01:00:16] Best practices for building voice agents.

[01:17:31] A hands-on guide to building a voice agent.

[38:07] Q&A session with the audience.

Part 2: Detailed Technical Summary
Introduction to Voice Agents: Dominic defines voice agents as systems that can accomplish tasks independently for users, which are composed of a model, instructions, access to tools, and a runtime [01:04]. He emphasizes that these agents are designed to be autonomous and helpful.

OpenAI Agents SDK for TypeScript: A new TypeScript SDK has been launched, mirroring the Python SDK, to provide a structured way to build agents based on OpenAI's best practices [01:35]. The SDK includes features like handoffs, guardrails, streaming I/O, tool support, built-in tracing, human-in-the-loop support with resumability, and native voice agent support [01:58].

Why Voice Agents?: Voice agents make technology more accessible [03:34] and are more information-dense due to the nuances of tone and voice [03:47]. A key advantage is their ability to act as an API to the real world, for instance, by calling a business that lacks a formal API [04:02].

Voice Agent Architectures:

Chained Approach (Text-based): This architecture follows a speech-to-text to text-based agent to text-to-speech pipeline [04:34]. While easier to start with and offering more control, it suffers from challenges like turn detection, increased latency, and a loss of audio context [05:33].

Speech-to-Speech Approach: Here, the model is trained directly on audio for a more seamless conversational experience and tool usage [06:30]. This approach boasts lower latency and a more contextual understanding of tone and voice, leading to a more natural flow [06:47]. However, it is harder to integrate with existing text-based systems and struggles with complex decision-making [07:01].

Delegation Approach: This hybrid approach uses a front-line agent for user interaction which then delegates complex tasks to more powerful reasoning models like GPT-4 mini or GPT-3 via tool calls [07:45]. A demo shows the agent effectively handling interruptions and delegating tasks such as checking the weather or processing refunds [08:00].

Best Practices for Building:

Start Small: Begin with a small and clear goal to make performance measurement and iteration more manageable [01:12:40].

Early Evaluations: Implement evaluations and guardrails early in the development process to ensure reliability and manage complexity as the agent grows [01:13:33].

Generative Tone: Leverage generative models to create a specific tone and personality for your agent by prompting for emotions and roles, for example using openai.fm [01:14:14].

Descriptive Flows: Use JSON structures to guide the model through conversational flows, much like a human agent's script, to improve the processing of steps [01:16:46].

Hands-on Building: The presentation includes a live coding session where Dominic builds a voice agent from scratch [01:17:31]. He demonstrates setting up the agent, adding tools, and connecting it to a real-time browser session using Next.js and WebRTC. The demo showcases real-time interaction, interruption handling, conversation transcripts, debugging with the traces dashboard, human-in-the-loop tool execution approval, and agent handoffs for specialized tasks [01:30:29, 01:50:00].

## Containing Agent Chaos — Solomon Hykes, Dagger

- Upload date: 2025-06-28
- Video: https://www.youtube.com/watch?v=bUBF5V6oDKw
- Transcript: raw/20250628_bUBF5V6oDKw/bUBF5V6oDKw.en-orig.vtt
- Metadata: raw/20250628_bUBF5V6oDKw/bUBF5V6oDKw.info.json

AI agents promise breakthroughs but often deliver operational chaos. Building reliable, deployable systems with unpredictable LLMs feels like wrestling fog – testing outputs alone is insufficient when the underlying workflow is opaque and flaky. How do we move beyond fragile prototypes?

This talk, from the creator of Docker, argues the solution lies outside the model: engineering reproducible execution workflows built on rigorous architectural discipline. Learn how containerization, applied not just to deployment but to each individual step of an agent's workflow, provides the essential isolation and environmental consistency needed.

Discover how combining this granular container approach with patterns like immutable state management allows us to contain agent chaos, unlock effective testing, simplify debugging, and bring essential control and predictability back to building powerful AI agents you can actually ship with confidence.

About Solomon Hykes
Solomon Hykes is best known as the creator of Docker, the open-source platform that revolutionized software development and deployment through containerization. His work fundamentally changed how applications are built, shipped, and run by standardizing their execution environments. Drawing on his deep experience tackling complexity at the infrastructure level, Solomon is now Founder and CEO of Dagger, focusing on the foundational challenges of building and operating reliable, scalable AI agent systems. He is passionate about applying platform engineering principles to the emerging AI landscape, helping engineers navigate this technological shift and build more dependable systems.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Taming Rogue AI Agents with Observability-Driven Evaluation — Jim Bennett, Galileo

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=xJXm4Wcw4m8
- Transcript: raw/20250627_xJXm4Wcw4m8/xJXm4Wcw4m8.en-orig.vtt
- Metadata: raw/20250627_xJXm4Wcw4m8/xJXm4Wcw4m8.info.json

LLM agents often drift into failure when prompts, retrieval, external data, and policies interact in unpredictable ways. This session introduces a repeatable, metric-driven framework for detecting, diagnosing, and correcting these undesirable behaviors in agentic systems at production scale.

About Jim Bennett
Jim is the worlds most energetic dev rel, and a Principal Developer Advocate at Galileo, focusing on enabling AI developers to be more productive by monitoring and evaluating LLMs and AI agents. He’s British, so sounds way smarter than he actually is, and lives in the Pacific North West of the USA. In the past he’s lived in 4 continents working as a developer in the mobile, desktop, and scientific space. He's spoken at conferences and events all around the globe, organised meetup groups and communities, and written books on mobile development and IoT. He is currently a Microsoft MVP for AI and Developer Tools.

He also hates and is allergic to cats, but has a 12-year-old who loves cats, so he has 2 cats.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Building Agentic Applications w/ Heroku Managed Inference and Agents — Julián Duque & Anush Dsouza

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=vRFqbEzzDsI
- Transcript: raw/20250627_vRFqbEzzDsI/vRFqbEzzDsI.en-orig.vtt
- Metadata: raw/20250627_vRFqbEzzDsI/vRFqbEzzDsI.info.json

In this workshop, you’ll learn how to use Heroku Managed Inference and Agents to build agentic applications. We’ll cover how to provision and deploy LLM models to your app, run untrusted code securely in Python, Node.js, Go, and Ruby using built-in tools, and use the Model Context Protocol (MCP) to connect tools and actions that extend your agents' capabilities.
---
Agentic applications are reshaping how developers approach automation and AI integration. In this workshop, you’ll learn how to use Heroku’s new Managed Inference and Agents platform to create applications that can reason, make decisions, and trigger actions, all while staying fully integrated with your app logic and infrastructure.

We’ll walk through how to provision and deploy LLMs, run untrusted code securely in multiple languages, and extend your agents with the Model Context Protocol (MCP). Whether you're building internal tools, developer assistants, or customer-facing AI features, this workshop will give you the technical foundation to get started.

You’ll learn how to:

- Deploy and manage LLMs using Heroku Managed Inference and Agents
- Safely run untrusted code in Python, Node.js, Go, and Ruby using Heroku’s built-in tools
- Use the Model Context Protocol (MCP) to extend your agent capabilities

By the end of this session, you’ll know how to build and deploy agentic applications on Heroku using production-ready infrastructure.

---related links---

https://twitter.com/julian_duque
https://www.linkedin.com/in/juliandavidduque/
https://julianduque.co/
https://www.heroku.com/

## timestamps

Introduction to Heroku AI [00:00]
Core Mission: The product's goal is to make every software engineer an AI engineer. Anush Dsouza, the Product Manager, states Heroku wants to make it “simple to attach agents and AI to your application.” [04:24]

Agentic Control Loop: Heroku provides an "agentic control loop" running on its platform. This loop gives AI models access to tools like code execution and data access, all secured under Heroku's trust layer. [05:01]

AI Primitives: Heroku AI is built on key primitives. These include inference for accessing curated models, the Model Context Protocol (MCP) for extending app functionality, and PG Vector for handling embeddings. [06:25]

Trusted Compute: Heroku's trusted compute layer, Dynos, runs first-party tools. They plan to expand this with tools for web search and memory, and users can bring their own tools via MCP. [07:08]

Provisioning and Usage
Managed Inference: This service allows you to run AI models directly within your Heroku infrastructure. This keeps your data within your application's network for enhanced security. [13:23]

Supported Models: The platform supports text-to-text models from Anthropic (Claude 3.5, 3.7, and 4), embeddings from Cohere Embed, and image generation with Stable Image Ultra. [14:38]

Chat Completions API: The basic chat completions endpoint is designed to be highly compatible with the OpenAI and Anthropic APIs. The presenter notes it's “95% compatible with the OpenAI API,” allowing the use of the OpenAI SDK. [50:51] It supports standard parameters like temperature and max_tokens, as well as streaming responses. [21:29]

Heroku Tools and Agents
Serverless Execution: Tools run on one-off Dynos, which scale to zero after execution. This means you “only pay for the compute that you use.” [17:57]

Dyno Run Command: This powerful tool allows the LLM to execute Unix commands or pre-deployed scripts on a Heroku Dyno. This gives the agent access to real-time information and the ability to interact with the file system. [25:08]

Database Querying: The agent can interact with your PostgreSQL database through two tools:

postgres-get-schema: This retrieves the database schema, which helps prevent the LLM from hallucinating incorrect table or column names. [25:45]

postgres-run-query: This tool generates and executes SQL queries based on the provided schema and the user's natural language request. [25:52]

Code Execution: The agent can generate and run code in Python, Node, Ruby, and Go on a one-off Dyno. It even supports installing dependencies on the fly. [27:02]

Extending with Model Context Protocol (MCP)
Bring Your Own Tools: You can extend the agent's capabilities by deploying your own tools as MCPs to Heroku. [37:38]

Deployment: MCPs are deployed by configuring a Procfile with an mcp process type. This makes your custom tool discoverable by the Heroku agent. [46:19]

Example MCP: The workshop demonstrates a "Brave Search MCP" that allows the agent to perform web searches, showcasing how to add external knowledge to the agent. [43:42]

## Realtime Conversational Video with Pipecat and Tavus — Chad Bailey and Brian Johnson, Daily & Tavus

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=ujt0da9Z29Q
- Transcript: raw/20250627_ujt0da9Z29Q/ujt0da9Z29Q.en-orig.vtt
- Metadata: raw/20250627_ujt0da9Z29Q/ujt0da9Z29Q.info.json

Tavus shipped the world's first realtime video avatar platform last year. Developers use Tavus' conversational video APIs to create education, social, and customer support agents. The Tavus team built their innovative product using the Pipecat open source framework and Daily's global WebRTC infrastructure. Join us for a technical deep dive into conversational video.

About Char Bailey
Chad Bailey started his career testing software for the Space Shuttle. After many years of building web apps, he's spent the last several working on real-time communication at Daily. Most recently, he's been building the Pipecat framework, and a series of increasingly ridiculous voice bots to show it off.

About Brian Johnson
Brian Johnson is a Staff Engineer at Tavus, a market-leading generative AI video research company building foundational models and operating systems for human-AI interaction. With a background in electrical engineering and law, he brings decades of experience building and scaling systems across frontend, backend, and ML infrastructure. At Tavus, Brian leads development of real-time AI systems that power lifelike digital humans. His work focuses on combining technical precision with human-centered design to push the boundaries of conversational video AI.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## From Mixture of Experts to Mixture of Agents with Super Fast Inference - Daniel Kim & Daria Soboleva

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=tzRvcTEapzo
- Transcript: raw/20250627_tzRvcTEapzo/tzRvcTEapzo.en-orig.vtt
- Metadata: raw/20250627_tzRvcTEapzo/tzRvcTEapzo.info.json

Our hands-on workshop will walk you through how to build your own Mixture of Agents (MoA) system using the fastest, and most capable open models available: Qwen3-32B and Llama 3.3-70B. MoA is an emerging architecture that combines the strengths of multiple large language models in a layered, agent-based design. This approach delivers superior performance by enabling specialized agents to collaborate across layers—outperforming today’s frontier models in both accuracy and efficiency.

To ground this new paradigm in its roots, we’ll also explore how Mixture of Experts (MoE) architectures continue to push the boundaries of scale and specialization. Learn how Cerebras trains state-of-the-art MoEs from Daria Soboleva, Head Research Scientist.

About Daniel Kim
I'm currently the Head of Growth at Cerebras Systems, the world's fastest provider of AI Inference built on the Cerebras Wafer-Scale Engine. I live in sunny and foggy San Francisco, CA. You can find me relaxing in the park, eating spicy noodles, and recently running!

About Daria Soboleva
Daria Soboleva is a Head Research Scientist at Cerebras working on efficient AI systems. Prior to Cerebras, Daria worked at Google, building expertise in research and engineering. She's the creator of SlimPajama (627B token dataset with 1M+ downloads) and BTLM-3B-8K, a model achieving 7B-level performance with less compute. Daria specializes in optimizing LLM architectures with focus on mixture-of-experts models and hardware-efficient training.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## The Agent Awakens: Collaborative Development with Copilot - Christopher Harrison, GitHub

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=tHJSZ1-ZqcA
- Transcript: raw/20250627_tHJSZ1-ZqcA/tHJSZ1-ZqcA.en-orig.vtt
- Metadata: raw/20250627_tHJSZ1-ZqcA/tHJSZ1-ZqcA.info.json

About Christopher Harrison
Christopher is a long-time geek who's spent the bulk of his career training, supporting and upskilling developers. He's a web developer at heart with passions which span from Python to DevOps to TypeScript to AI. In his current role as an Enterprise Advocate for GitHub he seeks to help organizations improve their DevOps process and culture. When not found writing code he can be found running, playing Civilization, or spending time with his partner and their four-legged child (a rescue mutt).

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Engineering Better Evals: Scalable LLM Evaluation Pipelines That Work — Dat Ngo, Aman Khan, Arize

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=spvXj9tnWAQ
- Transcript: raw/20250627_spvXj9tnWAQ/spvXj9tnWAQ.en-orig.vtt
- Metadata: raw/20250627_spvXj9tnWAQ/spvXj9tnWAQ.info.json

As LLM-powered products become more sophisticated, the need for scalable, reliable evaluation pipelines has never been more critical. This session dives deep into advanced LLM evaluation strategies that move beyond toy benchmarks and toward real-world production impact.

We’ll explore how to architect and implement evaluation pipelines that work across both online and offline environments—reducing dev complexity and accelerating iteration. The session will cover:

- LLM-as-a-judge frameworks
- Human-in-the-loop evaluation
- How hybrid approaches unlock more robust and nuanced performance assessments

We’ll break down technical architectures, share real implementation patterns, and examine trade-offs between evaluation techniques to help engineers make informed choices.
Whether you’re building from scratch or refining existing workflows, this talk offers practical strategies for crafting efficient, scalable, and accurate eval pipelines tailored to custom LLM products.

About Dat Ngo
I'm Dat Ngo, Director of AI Solutions at Arize, where I work with the world's largest companies to build and optimize AI applications for their business. With nearly a decade of experience in the AI space, I specialize in helping organizations tackle their biggest challenges around AI evaluation, observability, and making AI systems work reliably at scale.

At Arize, we partner with industry leaders including Reddit, Booking.com, Siemens, Roblox, and hundreds of other companies to solve the most complex problems in AI deployment and monitoring. This gives me unique insight into what it really takes to build production AI systems that deliver business value.

My passion for AI extends beyond the office—I eat, live, and breathe AI. I'm deeply engaged with the AI community through speaking, learning, and connecting with fellow practitioners who are pushing the boundaries of what's possible with artificial intelligence.

As a speaker, I bring real-world expertise from the trenches of enterprise AI deployment, sharing practical insights on evaluation frameworks, observability strategies, and the operational realities of making AI work at scale.

About Aman Khan
Aman is Director of Product, LLM at Arize AI. Prior to Arize, Aman was the PM on the Jukebox Feature Store in the ML Platform team at Spotify across ~50 data science teams. Aman was also PM for ML Evaluation frameworks across data science and engineering teams for self-driving cars at Cruise, which helped launch the first self-driving car service in an urban environment. Aman studied Mechanical Engineering at UC Berkeley and lived in the SF Bay Area for 9 years before moving to NYC.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## The State of AI Powered Search and Retrieval — Frank Liu, MongoDB (prev Voyage AI)

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=pIPtpBZ6TKk
- Transcript: raw/20250627_pIPtpBZ6TKk/pIPtpBZ6TKk.en-orig.vtt
- Metadata: raw/20250627_pIPtpBZ6TKk/pIPtpBZ6TKk.info.json

In this talk, we examine the state-of-the-art in AI-powered search and retrieval. We detail techniques for enhancing performance beyond base embedding models, including hybrid search, reranking strategies, query decomposition and document enrichment, the use of domain-specific and fine-tuned embeddings, custom data processing pipelines (ETL), and contextualized chunking methods.

About Frank Liu
Frank Liu is Staff Product Manager at MongoDB. He has over a decade of industry experience in machine learning and hardware engineering and presents at major industry events like the Open Source Summit Open Data Science Conference. In his spare time, he enjoys experimenting with and training models. Frank holds MS and BS degrees in Electrical Engineering from Stanford University.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Forget RAG Pipelines—Build Production Ready Agents in 15 Mins: Nina Lopatina, Rajiv Shah, Contextual

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=lArgRvBV3tQ
- Transcript: raw/20250627_lArgRvBV3tQ/lArgRvBV3tQ.en-orig.vtt
- Metadata: raw/20250627_lArgRvBV3tQ/lArgRvBV3tQ.info.json

Want to take advantage of your data, but don't want to reinvent RAG infrastructure? Join our workshop and see how you can deploy Agentic RAG in minutes using Contextual AI's managed RAG solution. We'll explore how Contextual handles intelligent parsing and chunking of your data, retrieves information with state of the art accuracy, and generates responses with a multi layered set of guardrails against hallucinations. Together, we'll build an end-to-end Agentic RAG pipeline and demonstrate its integration with Claude Desktop via MCP, so you can see how this could plug into your existing ecosystem.

By the end of this session, you'll have a functioning Agentic RAG prototype that you can easily customize and deploy to production for your specific use cases, even with complex, unstructured documents.

About Nina Lopatina
Nina Lopatina is Lead Developer Advocate at Contextual AI, the fastest way for developers to build accurate, scalable RAG agents. She focuses on enabling developers to transform unstructured data into applications by connecting product, content, and community. Nina has worked as a developer and leader in the NLP and language for the last 7 years. She began her tech career after applying machine learning techniques to neural data throughout her PhD and postdoctoral research focused on reinforcement learning and decision-making. When she is not working, Nina is likely chasing fresh snow on the slopes or camping and hiking with her family.

About Rajiv Shah
Rajiv Shah is the Chief Evangelist at Contextual AI with a passion and expertise in Practical AI. He focuses on enabling enterprise teams to succeed with AI. Rajiv has worked on GTM teams at leading AI companies, including Hugging Face in open-source AI, Snorkel in data-centric AI, Snowflake in cloud computing, and DataRobot in AutoML. He started his career in data science at State Farm and Caterpillar.

Rajiv is a widely recognized speaker on AI, published over 20 research papers, been cited over 1000 times, and received over 20 patents. He holds a PhD in Communications and a Juris Doctor from the University of Illinois at Urbana Champaign. You find him on social media with his short videos, @rajistics, that have received over ten million views.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Foundry Local: Cutting-Edge AI experiences on device with ONNX Runtime/Olive — Emma Ning, Microsoft

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=l614N5W60ls
- Transcript: raw/20250627_l614N5W60ls/l614N5W60ls.en-orig.vtt
- Metadata: raw/20250627_l614N5W60ls/l614N5W60ls.info.json

About Emma Ning 
Emma Ning is a Principal PM in the Microsoft AI Framework team, focusing on AI model operationalization and acceleration with ONNX Runtime/Olive for open and interoperable AI. She has more than five years of product experience in search engines taking advantage of machine learning techniques and spent more than six years exploring AI adoption among various businesses. She is passionate about bringing AI solutions to solve business problems as well as enhancing product experience.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Serving Voice AI at Scale — Arjun Desai (Cartesia) & Rohit Talluri (AWS)

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=knH3fmGAteQ
- Transcript: raw/20250627_knH3fmGAteQ/knH3fmGAteQ.en-orig.vtt
- Metadata: raw/20250627_knH3fmGAteQ/knH3fmGAteQ.info.json

Real-Time Voice AI applications demand the lowest possible latencies to enhance user experiences with more advanced reasoning and agentic capabilities. AWS is hosting Arjun Desai, co-founder of Cartesia, in a fireside chat for a technical deep dive into learnings and best practices for building a state-of-the-art inference stack that serves global enterprise customers.

About Arjun Desai
Cofounder @ Cartesia | Prev. Stanford ML PhD

About Rohit Talluri
Amazon Web Services (AWS) Generative AI ML Frameworks, focusing on Foundation Model Training & Inference.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Prompt Engineering is Dead — Nir Gazit, Traceloop

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=jvKf6zXrNO4
- Transcript: raw/20250627_jvKf6zXrNO4/jvKf6zXrNO4.en-orig.vtt
- Metadata: raw/20250627_jvKf6zXrNO4/jvKf6zXrNO4.info.json

Manual prompt crafting doesn't scale. In this session, we'll explore how to replace it with a test-driven, automated approach. You'll see how to define output evaluators, write minimal prompts, and let agents iterate toward optimal performance—all without manual tweaking. If you're still hand-tuning prompts, you're doing it wrong.

About Nir Gazit
CEO @ traceloop; ex-chief architect @ Fiverr, ex-tech lead @ Google; OpenTelemetry contributor

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## The Eyes Are The (Context) Window to The Soul: How Windsurf Gets to Know You — Sam Fertig, Windsurf

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=jUv5WSPo9fk
- Transcript: raw/20250627_jUv5WSPo9fk/jUv5WSPo9fk.en-orig.vtt
- Metadata: raw/20250627_jUv5WSPo9fk/jUv5WSPo9fk.info.json

Sometimes it seems like Windsurf knows you a little too well. It's one thing to generate generic code, but to predict your next intent? From matching existing code patterns and styles to tracking how local changes affect the larger codebase, this talk digs into the technical challenges of context awareness and why simply indexing code falls short. Relive our journey tackling the core issue in the AI IDE space : balancing retrieval quality with latency constraints and scaling effectively as codebases grow. For those curious about the infrastructure behind context-aware AI, this talk offers insights into our approach of turning massive codebases into collections of useful context.

About Sam Fertig
Sam Fertig is a Deployed Engineer at Windsurf, where he helps deliver cutting-edge software solutions in complex operational environments. Prior to Windsurf, he worked at C3 AI, gaining experience at the intersection of data, engineering, and enterprise AI. Sam holds a degree in Computer Science and Politics from Oberlin College. Outside of work, he’s passionate about MMA and Jiu Jitsu, and enjoys playing guitar in his free time.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Why should anyone care about Evals? — Manu Goyal, Braintrust

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=jJ45Yz1lJao
- Transcript: raw/20250627_jJ45Yz1lJao/jJ45Yz1lJao.en-orig.vtt
- Metadata: raw/20250627_jJ45Yz1lJao/jJ45Yz1lJao.info.json

An introduction to the evals track

About Manu Goyal
Manu Goyal is the founding engineer at Braintrust. Previously, he developed autonomous systems at Nuro. He has an 8 year old Pomeranian named Hendrix.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Vibe Coding at Scale: Customizing AI Assistants for Enterprise Environments - Harald Kirshner,

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=i1uPAN6uW4s
- Transcript: raw/20250627_i1uPAN6uW4s/i1uPAN6uW4s.en-orig.vtt
- Metadata: raw/20250627_i1uPAN6uW4s/i1uPAN6uW4s.info.json

"Vibe coding" often falters in complex enterprise environments. Drawing from real implementations, this talk demonstrates systematic approaches to customizing AI assistants for challenging codebases. We'll explore specialized techniques for navigating complex architectures, evidence-based strategies for undocumented legacy systems, methodologies for maintaining context across polyglot environments, and frameworks for standardizing AI usage while preserving developer autonomy. Through case studies from finance and healthcare, we'll present a comprehensive evaluation framework that bridges the gap between AI's theoretical capabilities and practical enterprise implementation, enabling true flow-state collaboration even within the most complex development ecosystems.

About Harold Kirshner
I'm Harald Kirschner, a Principal Product Manager at Microsoft working on Visual Studio Code and GitHub Copilot, supporting over 40 million active developers code faster and more efficiently across virtually any programming language. Before Microsoft, I led Developer Experience at Mozilla, where I led Firefox DevTools and helped deliver Firefox Quantum, which doubled browser performance. My background in software engineering, including early work on MooTools, gives me hands-on insight into the challenges developers face daily. When I'm not working, I enjoy hiking California's coastal trails and experimenting with generative art. As a speaker at the AI Engineer Summit, I'm excited to share insights from our work on AI coding tools and Model Context Protocol to help developers achieve flow state even in complex environments.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Memory Masterclass: Make Your AI Agents Remember What They Do! — Mark Bain, AIUS

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=gsedOXz8FX4
- Transcript: raw/20250627_gsedOXz8FX4/gsedOXz8FX4.en-orig.vtt
- Metadata: raw/20250627_gsedOXz8FX4/gsedOXz8FX4.info.json

Are you ready to give your AI agents a memory upgrade?
Join us for a fast-paced workshop exploring how memory can transform your agents.

What You'll Do:
Learn Leading Memory Solutions: Gain practical experience with open-source tools like Neo4j, Cognee, Graphiti, and Mem0.
Explore Memory Types: Understand the theory behind long-term, short-term, episodic, semantic, and other memory types.
Discover Memory Benefits: Learn how memory improves recall, contextual awareness, and reasoning in autonomous agents.
Compare Implementations: Get a snapshot of how different solutions implement memory—what’s built-in, flexible, and experimental. We'll also demonstrate GraphRAG memory solutions and a GraphRAG chat implemented with Google ADK.
Whether you’re working on AI copilots, agentic workflows, or research prototypes, this workshop will help you embed real memory into your AI stack.


About Mark Bain
I'm a deep tech founder building a private research lab: AIUS Technologies. We're on a mission to develop artificial life through R&D of long-term memory.

Previously I led a cybersecurity lab and an edtech startup. Worked with defense and national security clients, banks and Fortune 500 clients.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Milliseconds to Magic: Real‑Time Workflows using the Gemini Live API and Pipecat

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=fWY1FQwpWkY
- Transcript: raw/20250627_fWY1FQwpWkY/fWY1FQwpWkY.en-orig.vtt
- Metadata: raw/20250627_fWY1FQwpWkY/fWY1FQwpWkY.info.json

The Gemini Live API GA  is now powered by Google's best cost-effective thinking model Gemini 2.5 Flash. We will do a deep dive on the capabilities that the Gemini Live API combined with Pipecat unlock for devs with special focus on session management, turn detection, tool use (including async function calls), proactivity, multilinguality and integration with telephony and other infra. We will demo some of the more innovative capabilities. We will also talk through some customer use cases - especially how customers can use Pipecat to extend these realtime multimodal capabilities to client side applications such as customer support agents, gaming agents, tutoring agents etc. In addition, we also have an experimental version of the Live API powered by with Google's native audio offering that can be tried in an experimental capacity . This experimental model  can communicate with seamless, emotive, steerable, multilingual dialogue and enhances use cases where more natural voices can be a big differentiator.

About Kwindla Kramer
Kwin works on large-scale WebRTC infrastructure at Daily. He is the originator of Pipecat, the widely used, open source, vendor neutral voice agent framework supported by NVIDIA, Google, AWS and used by hundreds of startups. Before co-fonding Daily, Kwin built the sci-fi user interfaces in Minority Report and Iron Man.

About Shrestha Basu Mallick
Shrestha Basu Mallick is Group Product Manager and product lead for Gemini API at Google DeepMind. Prior to this, Shrestha led product development for AI assistance across all Google coding surfaces. Shrestha’s first role in Alphabet was at X, the Moonshot Factory, as Head of Product for a materials discovery platform that has since graduated to become its own startup. Before Google, Shrestha has had various roles in product and strategy at Salesforce Einstein, McKinsey, and Docusign. Shrestha holds a PhD in Applied Physics from Stanford.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Building agent fleet architectures your CISO doesn't hate — Lou Bichard, Gitpod

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=d9rsC6_VLoA
- Transcript: raw/20250627_d9rsC6_VLoA/d9rsC6_VLoA.en-orig.vtt
- Metadata: raw/20250627_d9rsC6_VLoA/d9rsC6_VLoA.info.json

Security is the biggest blocker for agent orchestration adoption in regulated industries for SWE agents. Gitpod's agent orchestration went from an originally self-hosted kubernetes architecture to the current 'bring your own cloud' model that enables deployment our SWE agent orchestration platform in secure environments. The architecture allows customers to securely connect their foundational models and agent memory solutions and comes with features like auto-suspend and resume for agent fleets. In this talk we deep dive into the architecture to share our years of learnings in how to secure agent workloads at scale in secure and regulated environments.

About Lou Bichard   
Lou is Product Manager at Gitpod, a platform for secure development environments for both humans and agents powering some of the world's largest financial, insurance, and health care providers. Lou was previously Principal Engineer for developer experience at DAZN building a platform for ~15M global users in 150+ markets.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## GraphRAG methods to create optimized LLM context windows for Retrieval — Jonathan Larson, Microsoft

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=c5qJHr3DnT4
- Transcript: raw/20250627_c5qJHr3DnT4/c5qJHr3DnT4.en-orig.vtt
- Metadata: raw/20250627_c5qJHr3DnT4/c5qJHr3DnT4.info.json

Jonathan Larson is a Senior Principal Data Architect at Microsoft Research working in Special Projects.  He currently leads a research team focused on the intersection of graph machine learning, LLM memory representations, and LLM orchestration. 

His research has led to shipping new features in Bing, Viva, PowerBI. He also shipped new tools to combat tech fraud. Many of the supporting libraries have been open sourced in collaboration on GitHub. Prior to joining Microsoft, Jonathan was Chief Scientist and Technical Fellow at Sotera Defense Solutions on assignment to DARPA, and led a variety of research across several programs. Jonathan has also led large-scale data science efforts at Google, Zillow, and the US Army. Early in his career, he also worked several startups and incubators.

About Jonathan Larson
Jonathan Larson is a Senior Principal Data Architect at Microsoft Research working in Special Projects. He currently leads a research team focused on the intersection of graph machine learning, LLM memory representations, and LLM orchestration. 

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Evals 101 — Doug Guthrie, Braintrust

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=bk0TmxoZlUY
- Transcript: raw/20250627_bk0TmxoZlUY/bk0TmxoZlUY.en-orig.vtt
- Metadata: raw/20250627_bk0TmxoZlUY/bk0TmxoZlUY.info.json

This hands-on workshop guides participants through the full AI evaluation lifecycle with Braintrust, from initial prompt testing to production monitoring. Attendees will build evaluation frameworks, practice offline and online strategies, and implement logging systems.

About Doug Guthrie
Doug Guthrie is a solutions engineer at Braintrust. Previously, he helped customers deploy data infrastructure at dbt Labs. He is also a proud girl dad.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Vector Search Benchmark[eting] - Philipp Krenn, Elastic

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=YrUBFXa1KUY
- Transcript: raw/20250627_YrUBFXa1KUY/YrUBFXa1KUY.en-orig.vtt
- Metadata: raw/20250627_YrUBFXa1KUY/YrUBFXa1KUY.info.json

Every vector database out there is both faster and slower than any other competitor — if you believe all the benchmarketing out there.
Let's turn the marketing into useful benchmarks that actually help you:
1. How not to benchmark (spoiler: don’t trust the glossy charts).
2. What’s uniquely tricky about benchmarking vector search.
3. How to build meaningful benchmarks tailored to your use case.

PS: Yes, you will have to get your hands dirty. Never believe a benchmark that you haven't tweaked yourself.

About Philipp Krenn
Philipp leads Developer Relations at Elastic — the company behind the Elasticsearch, Kibana, Beats, and Logstash. Based in San Francisco, he lives to demo interesting technology and solve challenging problems — all with a smile and a terminal window.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## RAG in 2025: State of the Art and the Road Forward — Tengyu Ma, MongoDB (acq. Voyage AI)

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=W_CYk2ogcDI
- Transcript: raw/20250627_W_CYk2ogcDI/W_CYk2ogcDI.en-orig.vtt
- Metadata: raw/20250627_W_CYk2ogcDI/W_CYk2ogcDI.info.json

The talk will have three parts
1.Roadmap debate: RAG vs. finetuning vs. long-context
2.RAG today: benefits, challenges, and current solutions
3.RAG tomorrow: AI models do more work

About Tengyu Ma
Tengyu Ma is the Chief AI Scientist @ MongoDB and an Assistant Professor @ Stanford. He was the co-founder and CEO of Voyage AI before the acquisition by MongoDB.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Mastering Engineering Flow with Windsurf - Eashan Sinha, Windsurf

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=W_5tzQY-hVs
- Transcript: raw/20250627_W_5tzQY-hVs/W_5tzQY-hVs.en-orig.vtt
- Metadata: raw/20250627_W_5tzQY-hVs/W_5tzQY-hVs.info.json

As experienced engineers, especially senior and staff engineers, our focus shifts towards complex problem-solving, architectural decisions, and mentoring. While AI tools promise productivity gains, Windsurf offers more than just code completion and chat assistance – it's an agentic IDE built to enhance engineering flow. This talk explores how experienced engineers can leverage Windsurf's deep contextual awareness, structured guidance, and automated workflows to tackle sophisticated and complex tasks. We'll demonstrate practical strategies for accelerating feature development, automating code maintenance and reviews, and ultimately freeing up cognitive load to focus on high-impact engineering challenges. Learn how to move beyond basic AI assistance and truly partner with Windsurf to excel in your role.

About Eashan Sinha  
Graduating from Georgia Tech with his bachelors and masters in computer science, Eashan specializes in AI and ML and has a strong foundation in building GenAI products. Eashan spent time as an engineer at TikTok and founded his own generative AI based company that was accepted into Y Combinator prior to joining Windsurf as a Deployed Engineer. Currently, Eashan is focused on enhancing AI agent efficiency and performance with large codebases and enterprise use cases.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## CI in the Era of AI: From Unit Tests to Stochastic Evals — Nathan Sobo, Zed

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=WXy8Yy9xGss
- Transcript: raw/20250627_WXy8Yy9xGss/WXy8Yy9xGss.en-orig.vtt
- Metadata: raw/20250627_WXy8Yy9xGss/WXy8Yy9xGss.info.json

Software engineers have long understood that high-quality code requires comprehensive automated testing. For decades, our industry has relied on deterministic tests with clear pass/fail outcomes to ensure reliability.

High-quality software depends on automated testing. That's certainly true at Zed, where we're building a next-generation native IDE in Rust. Zed runs at 120 frames per second, but it would also crash once a second if we didn't maintain and run a comprehensive suite of unit tests on every change.

But what happens when AI enters the equation?

In this talk, we'll explore how continuous integration evolves when working with AI components. "Evals" - parlance from the machine learning field - are fundamentally a continuation of the software testing tradition, but with a critical difference: they're inherently stochastic.

Zed's traditional CI goes to extreme lengths to eliminate non-determinism, as nobody likes having their pull requests blocked by flaky builds. We've even fully simulated network interactions with a deterministic random scheduler. AI components, however, forced us to confront a fundamental paradigm shift—uncertainty isn't a bug but an intrinsic feature of these systems, compelling us to embrace what we couldn't avoid.

We'll share our journey of reconceptualizing evals as "stochastic unit tests" - still verifying system behavior, but without binary pass/fail grades.

We'll discuss practical approaches to:
- Thoughtfully building test suites for AI components
- Shifting from red/green outcomes to "shades of gray"
- Replacing build gates with trend analysis and performance monitoring
- Maintaining engineering confidence despite statistical variance

Whether you're incorporating AI into existing systems or building new AI-powered tools, this talk will provide practical insights into maintaining quality when determinism gives way to probability.

About Nathan Sobo
Nathan joined GitHub in late 2011 to build the Atom text editor, and he led the Atom team until 2018.

He also co-led development of Teletype for Atom, pioneering one of the first production uses of conflict-free replicated data types for collaborative text editing.

He's been dreaming about building the world's best text editor since he graduated from college, and is excited to finally have the knowledge, tools, and resources to achieve this vision.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Architecting Agent Memory: Principles, Patterns, and Best Practices — Richmond Alake, MongoDB

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=W2HVdB4Jbjs
- Transcript: raw/20250627_W2HVdB4Jbjs/W2HVdB4Jbjs.en-orig.vtt
- Metadata: raw/20250627_W2HVdB4Jbjs/W2HVdB4Jbjs.info.json

In the rapidly evolving landscape of agentic systems, memory management has emerged as a key pillar for building intelligent, context-aware AI Agents. Inspired by the complexity of human memory systems—such as episodic, working, semantic, and procedural memory—this talk unpacks how AI agents can achieve believability, reliability, and capability by retaining and reasoning over past experiences.

We’ll begin by establishing a conceptual framework based on real-world implementations from memory management libraries and system architectures:
Memory Components representing various structured memory types (e.g., conversation, workflow, episodic, persona)
Memory Modes reflecting operational strategies for short-term, long-term, and dynamic memory handling

Next, the talk transitions to practical implementation patterns critical for effective memory lifecycle management:

Maintaining rich conversation history and contextual awareness
Persistence strategies leveraging vector databases and hybrid search
Memory augmentation using embeddings, relevance scoring, and semantic retrieval
Production-ready practices for scaling memory in multi-agent ecosystems
We’ll also examine advanced memory strategies within agentic systems:
Memory cascading and selective deletion
Integration of tool use and persona memory
Optimizing performance around memory retrieval and LLM context window limits
Whether you're developing autonomous agents, chatbots, or complex workflow orchestration systems, this talk offers knowledge and tactical insights for building AI that can remember, adapt, and improve over time.
This session is ideal for:
AI engineers and agent framework developers
Architects designing Agentic RAG or multi-agent systems
Practitioners building contextual, personalized AI experiences
By the end of the session, you’ll understand how to leverage memory as a strategic asset in agentic design—and walk away ready to build agents that not only act and reason but also remember. 


---related links---

https://www.linkedin.com/in/richmondalake/

## Data is Your Differentiator: Building Secure and Tailored AI Systems — Mani Khanuja, AWS

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=ROfHHJmumcc
- Transcript: raw/20250627_ROfHHJmumcc/ROfHHJmumcc.en-orig.vtt
- Metadata: raw/20250627_ROfHHJmumcc/ROfHHJmumcc.info.json

As  organizations seek to harness their proprietary data while maintaining  security and compliance, Amazon Bedrock provides a comprehensive framework  for building tailored AI applications. Using Amazon Bedrock Knowledge Bases  and Amazon Bedrock Data Automation, organizations can create AI solutions  that truly understand their unique business context, terminology, and  requirements. Combined with Amazon Bedrock Guardrails, these capabilities  enhance the accuracy and relevance of AI-generated responses, while ensuring  that sensitive information remains protected within the organization's  control - enabling businesses to build secure and compliant enterprise-grade  generative AI solutions that accelerate time to value.

About Mani Khanuja
Mani Khanuja is a Principal Generative AI Specialist SA, and an author of the book Applied Machine Learning and High Performance Computing on AWS. She leads machine learning projects in various domains such as computer vision, natural language processing, and generative AI. She speaks at internal and external conferences such AWS re:Invent, Women in Manufacturing West, YouTube webinars, and GHC 23. In her free time, she likes to go for long runs along the beach.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Introducing Strands Agents, an Open Source AI Agents SDK — Suman Debnath, AWS

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=Q3NreEAdKMc
- Transcript: raw/20250627_Q3NreEAdKMc/Q3NreEAdKMc.en-orig.vtt
- Metadata: raw/20250627_Q3NreEAdKMc/Q3NreEAdKMc.info.json

Building AI agents used to require complex orchestration, extensive scaffolding, and months of tuning. With Strands Agents, an open source SDK from AWS. You can now build, test, and deploy intelligent agents in just a few lines of code. This session introduces the model-driven approach behind Strands, where a model, a prompt, and a set of tools are all you need to create powerful, production-ready agents. Learn how Strands leverages modern foundation models to handle reasoning, tool use, and reflection, reducing development time from months to days.

About Suman Debnath
Suman Debnath is a Principal Machine Learning Advocate at Amazon Web Services. Currently, his focus is on Supervised Learning, Natural Language Processing (NLP), Large Language Models (LLMs), and Retrieval Augmented Generation (RAG). Suman is committed to leveraging open-source tools like LangChain, PyTorch, Numpy, and Pandas for advancing machine learning. He has developed performance benchmarking and monitoring tools for distributed storage systems. Suman has spoken at over 100 global events, including AWS re:Invent, AI Engineer Summit, PyCon, PyData, ODSC, and meetups across multiple countries.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Building Code First AI Agents with Azure AI Agent Service — Cedric Vidal, Microsoft

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=N4vCBM5YbN0
- Transcript: raw/20250627_N4vCBM5YbN0/N4vCBM5YbN0.en-orig.vtt
- Metadata: raw/20250627_N4vCBM5YbN0/N4vCBM5YbN0.info.json

This workshop offers a hands-on introduction to developing Large Language Model (LLM)-powered AI agents using Microsoft’s Azure AI Agent Service. Participants will build a conversational agent capable of analyzing sales data, generating visualizations, and delivering actionable insights.

The session takes a code-first approach using the Azure AI Foundry SDK for Python, and demonstrates how to integrate core Azure services including Azure OpenAI, Azure AI Search, and Azure Storage.

Attendees will explore key concepts such as function calling, document grounding, and leveraging code interpreters to generate diagrams. The workshop also covers how to connect agents to external data sources like SQL databases (e.g., SQLite), enabling access to legacy relational systems.

By the end of the session, participants will have a solid foundation for building and deploying intelligent, code-first AI agents with Azure AI Agent Service—ready to power real-world applications.

About Cedric Vidal
Cedric Vidal is a Principal AI Advocate at Microsoft, specializing in Generative AI 🤖, and the startup 🚀 and research 🔬 ecosystems. He is dedicated to promoting AI in startups and facilitating the transition of research and startup products to the market. If you're an AI Startup Founder or Engineer, I'd like to feature your work, come talk to me. Before his current role, Cedric spent 4 years as an Engineering Manager in the AI data labeling space for the self-driving 🚕 industry at Argo AI (now re-spawned as Latitude AI). He also served as the CTO of the Fintech AI SAAS startup Quicksign and worked as a software engineering services consultant for major Fintech enterprises for 10 years.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Events are the Wrong Abstraction for Your AI Agents - Mason Egger, Temporal.io

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=KJ9eZYTWS1Y
- Transcript: raw/20250627_KJ9eZYTWS1Y/KJ9eZYTWS1Y.en-orig.vtt
- Metadata: raw/20250627_KJ9eZYTWS1Y/KJ9eZYTWS1Y.info.json

AI Agents are distributed systems. Agents need to connect and communicate with tools, data repositories, other agents, etc., all over a network. Event-Driven Architecture is a common pattern for facilitating this connectivity, using Events as the communication abstraction. However, this pattern introduces complexities as well, such as fragmented logic, increased latency, decreased observability, and more. But what if there were a way to get the benefits of Event-Driven Architecture without the complexities? Enter Durable Execution. In this talk, we'll discuss the pitfalls of Event-Driven Architecture, how Durable Execution solves these issues, and why Durable Execution, not Events, is the correct abstraction for building AI Agents.

About Mason Egger
Mason is currently a Senior Developer Advocate at Temporal Technologies who specializes in building community, developer-focused educational content, distributed systems, and Python. Prior to his work at Temporal he worked in Developer Relations at DigitalOcean and as a backend engineer at various companies. He’s an avid programmer, speaker, educator, and writer/blogger. He is President of the PyTexas Foundation, Conference Chair of the PyTexas Conference, and a founding organizer of the PyTexas Meetup.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## AI Red Teaming Agent: Azure AI Foundry — Nagkumar Arkalgud & Keiji Kanazawa, Microsoft

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=JhJKgRAmfIU
- Transcript: raw/20250627_JhJKgRAmfIU/JhJKgRAmfIU.en-orig.vtt
- Metadata: raw/20250627_JhJKgRAmfIU/JhJKgRAmfIU.info.json

In the age of autonomous AI agents, ensuring their safety and reliability is paramount. But how can we proactively uncover vulnerabilities before they impact real-world scenarios? Enter Azure AI Evaluation SDK’s Red Teaming Agent—a cutting-edge tool designed to rigorously challenge your AI agents, exposing hidden risks and unexpected behaviors. This session will guide you through the powerful capabilities of Azure’s Red Teaming Agent, demonstrating how it simulates adversarial scenarios, stress-tests agentic decision-making, and ensures your applications remain robust, ethical, and safe. You’ll learn practical techniques for systematically identifying weaknesses, interpreting evaluation results, and integrating safety checks into your development lifecycle. Join us to explore how embracing adversarial testing not only mitigates risks but strengthens trust in your AI solutions—keeping you ahead in the rapidly evolving landscape of responsible AI.

About Nagkumar Arkalgud
Nagkumar Arkalgud is a Senior Software Engineer at Microsoft, working on the Azure AI Evaluation SDK. With 10 years of experience in software engineering, he designed and built the SDK that enables red teaming for GenAI applications. Nagkumar focuses on advancing AI evaluation methodologies to optimize tools for AI applications.

About Keiji Kanazawa
Product lead working on a world class machine learning / artificial intelligence platform at Microsoft. Proven product leader with over 20 years deep technical expertise building web scale services and API platforms.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Agentic Excellence: Mastering AI Agent Evals w/ Azure AI Evaluation SDK — Cedric Vidal, Microsoft

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=J4vPq2i0QzE
- Transcript: raw/20250627_J4vPq2i0QzE/J4vPq2i0QzE.en-orig.vtt
- Metadata: raw/20250627_J4vPq2i0QzE/J4vPq2i0QzE.info.json

As AI agents transition from experimental assistants to critical components of enterprise workflows, reliably evaluating their performance becomes essential. But how do you systematically measure an AI agent’s capabilities, contextual understanding, and accuracy across diverse scenarios?

In this talk, we'll dive deep into the Azure AI Evaluation SDK, an innovative tool designed to rigorously assess agentic applications. Learn how to create powerful evaluations using structured test plans, scenarios, and advanced analytics that pinpoint strengths and expose hidden weaknesses. Through practical examples and real-world case studies, you'll discover how companies are already leveraging this SDK to enhance agent trustworthiness, reliability, and performance.

Whether you're developing conversational agents, data-driven decision-makers, or autonomous workflow orchestrators, this session equips you with the techniques and insights needed to ensure your AI solutions deliver exceptional value and exceed user expectations."

About Cedric Vidal
Cedric Vidal is a Principal AI Advocate at Microsoft, specializing in Generative AI 🤖, and the startup 🚀 and research 🔬 ecosystems. He is dedicated to promoting AI in startups and facilitating the transition of research and startup products to the market. If you're an AI Startup Founder or Engineer, I'd like to feature your work, come talk to me. Before his current role, Cedric spent 4 years as an Engineering Manager in the AI data labeling space for the self-driving 🚕 industry at Argo AI (now re-spawned as Latitude AI). He also served as the CTO of the Fintech AI SAAS startup Quicksign and worked as a software engineering services consultant for major Fintech enterprises for 10 years.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Ship it! Building Production Ready Agents — Mike Chambers, AWS

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=HT4l0DeP69I
- Transcript: raw/20250627_HT4l0DeP69I/HT4l0DeP69I.en-orig.vtt
- Metadata: raw/20250627_HT4l0DeP69I/HT4l0DeP69I.info.json

Explore the practical challenges and solutions for deploying AI agents in real-world production environments. Through detailed technical analysis and practical examples, we'll examine strategies for building and orchestrating agent systems at scale. We'll cover critical infrastructure decisions, scalability frameworks, and best practices for creating robust, production-ready agent architectures.

About Mike Chambers
Mike is a passionate developer advocate and expert in the fields of machine learning, AI, and generative AI. With a strong background in cloud computing, he brings a unique blend of technical knowledge and communication skills to engage and inspire audiences. Join Mike in exploring the possibilities and shaping the future of these transformative technologies.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Don’t get one-shotted: Use AI to test, review, merge, and deploy code — Tomas Reimers, Graphite

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=H6MrR5NbTZA
- Transcript: raw/20250627_H6MrR5NbTZA/H6MrR5NbTZA.en-orig.vtt
- Metadata: raw/20250627_H6MrR5NbTZA/H6MrR5NbTZA.info.json

As AI tools like GitHub Copilot and ChatGPT help engineers generate code at an unprecedented rate, the “outer loop”—reviewing, testing, merging, and deploying—becomes more vital than ever. Studies have shown that up to half of AI-generated solutions contain bugs or vulnerabilities, underscoring the continued importance of thorough, human-in-the-loop reviews. In this talk we'll take a look at how next-gen developer tools can harness AI not just for generating code, but also reviewing it. By thoughtfully integrating AI into that fully understands your entire codebase, teams can accelerate velocity without sacrificing quality.

Attendees will learn real-world strategies and best practices for establishing an “outer loop” that safely and efficiently deploys high volumes of AI-assisted code,  without compromising reliability. We’ll also discuss pitfalls to avoid when integrating AI into existing pipelines.

About Tomas Reimers
Tomas Reimers, Forbes 30u30 class of ‘23, is the CPO and Co-founder of Graphite, the NYC DevTools startup that’s revolutionizing how the fastest-moving engineers build and ship software. Prior to co-founding Graphite, Tomas was a dev-tools engineer at Meta, developing a framework that supported the work of 200+ product teams and more than 1000 developers. He is passionate about all things software and will enthusiastically debate best engineering and architecture practices with you for hours.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Graph Intelligence: Enhance Reasoning and Retrieval Using Graph Analytics - Alison & Andreas, Neo4j

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=GGxAQVbwBL4
- Transcript: raw/20250627_GGxAQVbwBL4/GGxAQVbwBL4.en-orig.vtt
- Metadata: raw/20250627_GGxAQVbwBL4/GGxAQVbwBL4.info.json

Advanced GraphRAG techniques apply graph ML and algorithms, wrapped into tidy notebooks.

About Alison Cossette 
Alison Cossette is a dynamic Data Science Strategist, Educator, and Podcast Host. As a Developer Advocate at Neo4j specializing in Graph Data Science, she brings a wealth of expertise to the field. With her strong technical background and exceptional communication skills, Alison bridges the gap between complex data science concepts and practical applications. Alison’s passion for responsible AI shines through in her work. She actively promotes ethical and transparent AI practices and believes in the transformative potential of responsible AI for industries and society. Through her engagements with industry professionals, policymakers, and the public, she advocates for the responsible development and deployment of AI technologies. She is currently a Volunteer Member of the US Department of Commerce - National Institute of Standards and Technology's Generative AI Public Working Group Alison’s academic journey includes Masters of Science in Data Science studies, specializing in Artificial Intelligence, at Northwestern University and research with Stanford University Human-Computer Interaction Crowd Research Collective. Alison combines academic knowledge with real-world experience. She leverages this expertise to educate and empower individuals and organizations in the field of data science. Overall, Alison Cossette’s multifaceted background, commitment to responsible AI, and expertise in data science make her a respected figure in the field. Through her role as a Developer Advocate at Neo4j and her podcast, she continues to drive innovation, education, and responsible practices in the exciting realm of data science and AI.

About Andreas Kollegger
Andreas is a technological humanist. Starting at NASA, Andreas designed systems from scratch to support science missions. Then in Zambia, he built medical informatics systems to apply technology for social good. Now with Neo4j, he is democratizing graph databases to validate and extend our intuitions about how the world works. Everything is connected.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Collaborating with Agents in your Software Dev Workflow - Jon Peck & Christopher Harrison, Microsoft

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=G1hhmz6mXT0
- Transcript: raw/20250627_G1hhmz6mXT0/G1hhmz6mXT0.en-orig.vtt
- Metadata: raw/20250627_G1hhmz6mXT0/G1hhmz6mXT0.info.json

GitHub Copilot's agentic capabilities enhance its ability to act as a peer programmer. From the IDE to the repository, Copilot can generate code, run tests, and perform tasks like creating pull requests using Model Context Protocol (MCP). This instructor-led lab will guide you through using agent capabilities on both the client and the server: Key takeaways include:
Understanding how to bring agents into your software development workflow
Identifying scenarios where agents can be most impactful, as well as tips and tricks to provide the right context to lead to success
Discovering how Model Context Protocol provides access to an additional set of external tools and capabilities that the agent can use
Recommended practices to accelerate your development while maintaining code quality.

About Jon Peck
An Enterprise Advocate (and occasional manager) at GitHub, Jon Peck meets daily with maintainers, startups, and F500 executives to familiarize them with industry best practices, policy suggestions, and product capabilities across DevOps and AI. With 25+ years of experience as a fullstack developer, architect, and advocate, he aims to to bring engaging, real-world learnings to both boardrooms and global conferences.

- Speaker (conferences): Dev Exec World 2025, STARWEST 2024, InnerSource Summit 2023, GitHub Galaxy 2023, DevWeek Management 2023, Startup Grind 2022, GitHub InFocus 2022, DeveloperWeek 2018-20, SeattleJS, Global AI Conf 2018-19, AI Next 2019-20, MLOps World, Data Innovation Summit, Nordic APIs 2018-19 (keynote), ODSC East+West, API World, O'Reilly AI, OSCON
- Speaker (tech schools): Galvanize, CodeFellows, Metis, Epicodus, Alchemy
- Organizer: Seattle Building Intelligent Applications Meetup
- Educator: Cascadia College, Seattle C&W, consultant
- Lead Developer: Empower Engine, Giftstarter, Mass General Hospital, Cornell University
- Technical Advocate: Algorithmia, GitHub

About Christopher Harrison
Christopher is a long-time geek who's spent the bulk of his career training, supporting and upskilling developers. He's a web developer at heart with passions which span from Python to DevOps to TypeScript to AI. In his current role as an Enterprise Advocate for GitHub he seeks to help organizations improve their DevOps process and culture. When not found writing code he can be found running, playing Civilization, or spending time with his partner and their four-legged child (a rescue mutt).

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## [Full Workshop] Vibe Coding at Scale: Customizing AI Assistants for Enterprise Environments

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=EAfP8pDs7h4
- Transcript: raw/20250627_EAfP8pDs7h4/EAfP8pDs7h4.en-orig.vtt
- Metadata: raw/20250627_EAfP8pDs7h4/EAfP8pDs7h4.info.json

"Vibe coding" often falters in complex enterprise environments. Drawing from real implementations, this talk demonstrates systematic approaches to customizing AI assistants for challenging codebases. We'll explore specialized techniques for navigating complex architectures, evidence-based strategies for undocumented legacy systems, methodologies for maintaining context across polyglot environments, and frameworks for standardizing AI usage while preserving developer autonomy. Through case studies from finance and healthcare, we'll present a comprehensive evaluation framework that bridges the gap between AI's theoretical capabilities and practical enterprise implementation, enabling true flow-state collaboration even within the most complex development ecosystems.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## How fast are LLM inference engines anyway? — Charles Frye, Modal

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=DeFF3J8T5Pk
- Transcript: raw/20250627_DeFF3J8T5Pk/DeFF3J8T5Pk.en-orig.vtt
- Metadata: raw/20250627_DeFF3J8T5Pk/DeFF3J8T5Pk.info.json

Open weights models and open source inference servers have made massive strides in the year since we last got together at AIE World's Fair.

Where once we had only pirated LLaMA 2 weights and Transformers, we now have an embarrassment of riches. In fact, we have too many choices! What's an AI engineer looking to self-host inference to do?

In this session, we'll share our benchmarking results from hundreds of runs across models, frameworks, and hardware. We'll also share tips and tricks from working with teams deploying LLM inference at scale.

About Charles Frye
Charles teaches people to build data, ML, and AI applications. He got his PhD from the University of California, Berkeley, in 2020 for work on the geometry of neural network optimization. He has since worked as an educator and evangelist for neural network applications at Weights & Biases, Full Stack Deep Learning, and now Modal Labs.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Agentic GraphRAG: Simplifying Retrieval Across Structured & Unstructured Data — Zach Blumenfeld

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=CzM3cW6FdBs
- Transcript: raw/20250627_CzM3cW6FdBs/CzM3cW6FdBs.en-orig.vtt
- Metadata: raw/20250627_CzM3cW6FdBs/CzM3cW6FdBs.info.json

Agentic workflows often become complex, brittle, and hard to maintain when they need to retrieve and reason across both structured data (typically requiring precise query execution) and unstructured data (commonly handled via vector search in RAG). In this talk, we’ll explore how mapping key information into a knowledge graph can simplify these workflows and improve retrieval quality. You’ll learn core concepts behind GraphRAG, how to integrate it into agent tools, and get access to end-to-end code examples so you can start building right away.

About Zach Blumenfeld
Zach Blumenfeld is an AI/ML graph specialist at Neo4j who helps engineers, data scientists, and business leaders leverage graph technology for analytics and intelligent applications. His expertise spans several dynamic fields, including GraphRAG and AI systems, criminal fraud detection, entity resolution, and recommendation engines.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Why Your Agent’s Brain Needs a Playbook: Practical Wins from Using Ontologies - Jesús Barrasa, Neo4j

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=CbiR9xS2skQ
- Transcript: raw/20250627_CbiR9xS2skQ/CbiR9xS2skQ.en-orig.vtt
- Metadata: raw/20250627_CbiR9xS2skQ/CbiR9xS2skQ.info.json

You're trying to guide how your agents think and act. Code-orchestrated workflows are too rigid, but LLMs charting their own course feel too chaotic. When you need a middle ground, it’s time to reach for the secret weapon: ontologies. These graph-shaped fragments of actionable knowledge can fill in critical gaps.

In this talk, we’ll explore together how ontologies bring structure, semantics, and sanity to GenAI-powered applications. You’ll learn when they’re useful, how to apply them, and what kinds of problems they help solve. Through practical examples, we’ll show how ontologies (1) guide knowledge graph construction, (2) add a semantic layer for more efficient and accurate retrieval (GraphRAG), and (3) encode domain logic you don’t want to leave up to the LLM.

About Jesús Barrasa
Dr. Jesús Barrasa is the AI Field CTO at Neo4j, where he works with organisations combining the power of GenAI with Knowledge Graphs. He co-authored "Building Knowledge Graphs" (O'Reilly 2023) and is cohost of the monthly Going Meta live webcast (https://goingmeta.live/) since 2022.
Jesús holds a Ph.D. in Artificial Intelligence/Knowledge Representation and is an active thought leader in the KG and AI space

## Unlocking AI Powered DevOps Within Your Organization — Jon Peck, GitHub

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=C1NivhYS1sI
- Transcript: raw/20250627_C1NivhYS1sI/C1NivhYS1sI.en-orig.vtt
- Metadata: raw/20250627_C1NivhYS1sI/C1NivhYS1sI.info.json

Software development is a team sport, with many different roles, where eveyone can win. But success isn't guaranteed; it depends on specific practices, policies, and tools which enable minimally-siloed, AI-accelerated collaboration across all parts of the DevOps process, from PM to development to CI/CD and security.

Discover the patterns and tools which lead to success, methods for changing the status quo, and perhaps a few horror stories. We'll touch on innersourcing, cloud development, AI, automation, governance, security, scaling and more -- with actionable learnings for everyone from small maintainer communities to F500 Enterprises.

About Jon Peck
An Enterprise Advocate (and occasional manager) at GitHub, Jon Peck meets daily with maintainers, startups, and F500 executives to familiarize them with industry best practices, policy suggestions, and product capabilities across DevOps and AI. With 25+ years of experience as a fullstack developer, architect, and advocate, he aims to to bring engaging, real-world learnings to both boardrooms and global conferences.

- Speaker (conferences): Dev Exec World 2025, STARWEST 2024, InnerSource Summit 2023, GitHub Galaxy 2023, DevWeek Management 2023, Startup Grind 2022, GitHub InFocus 2022, DeveloperWeek 2018-20, SeattleJS, Global AI Conf 2018-19, AI Next 2019-20, MLOps World, Data Innovation Summit, Nordic APIs 2018-19 (keynote), ODSC East+West, API World, O'Reilly AI, OSCON
- Speaker (tech schools): Galvanize, CodeFellows, Metis, Epicodus, Alchemy
- Organizer: Seattle Building Intelligent Applications Meetup
- Educator: Cascadia College, Seattle C&W, consultant
- Lead Developer: Empower Engine, Giftstarter, Mass General Hospital, Cornell University
- Technical Advocate: Algorithmia, GitHub

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Effective agent design patterns in production — Laurie Voss, LlamaIndex

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=72XxWkd8Jrk
- Transcript: raw/20250627_72XxWkd8Jrk/72XxWkd8Jrk.en-orig.vtt
- Metadata: raw/20250627_72XxWkd8Jrk/72XxWkd8Jrk.info.json

At LlamaIndex we see a lot of agents built every day, and we've got a sense of what works and what doesn't. We've distilled those learnings down into a series of patterns and best practices for building real-world, production agents, and we're here to share them. You'll learn patterns for applying structure and guidance to famously nondeterministic LLMs and get concrete instruction on how to implement them.

About Laurie Voss
Laurie has been a web developer for 27 years, and along the way he co-founded npm, Inc.. He cares passionately about making technology accessible to everyone by demystifying complex technology topics.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## How to build world-class AI products — Sarah Sachs (AI lead @ Notion) &  Carlos Esteban (Braintrust)

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=6YdPI9YbjbI
- Transcript: raw/20250627_6YdPI9YbjbI/6YdPI9YbjbI.en-orig.vtt
- Metadata: raw/20250627_6YdPI9YbjbI/6YdPI9YbjbI.info.json

Join us for a hands-on workshop where you'll learn practical strategies to evaluate AI applications throughout their lifecycle—from initial testing of prompts to ongoing monitoring in production. We’re excited to host Sarah Sachs, AI Lead at Notion, who will share insights into how Notion built their acclaimed Notion AI.

About Carlos Esteban
Carlos Esteban is a Solutions Engineer at Braintrust. Previously, he helped enterprises secure and scale infrastructure at HashiCorp. He’s also a former tennis player turned yoga enthusiast, still auditioning his next full-time sport.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## To the moon! Navigating deep context in legacy code with Augment Agent — Forrest Brazeal, Matt Ball

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=6NIr_cYPglk
- Transcript: raw/20250627_6NIr_cYPglk/6NIr_cYPglk.en-orig.vtt
- Metadata: raw/20250627_6NIr_cYPglk/6NIr_cYPglk.info.json

Shortened presentation-only version of our Apollo 11 workshop!

About Forrest Brazeal
Forrest Brazeal is an author, tech educator, cartoonist, and Pwnie Award-winning songwriter. He left Google in 2024 to found the technical media company Freeman & Forrest. His community initiative, the Cloud Resume Challenge, has helped thousands of nontraditional learners take their first steps toward a career in tech.

About Matt Ball
Matt is passionate about empowering developers. At Postman, Matt was the first Solutions Architect where he helped build the go-to-market strategy. Matt previously led Professional Services Engineering at Qubit.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Building Multimodal AI Agents From Scratch — Apoorva Joshi, MongoDB

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=640KMYtxCeI
- Transcript: raw/20250627_640KMYtxCeI/640KMYtxCeI.en-orig.vtt
- Metadata: raw/20250627_640KMYtxCeI/640KMYtxCeI.info.json

In this hands-on workshop, you will build a multimodal AI agent capable of processing mixed-media content—from analyzing charts and diagrams to extracting insights from documents with embedded visuals. Using MongoDB as a vector database and memory store, and Google's Gemini for multimodal reasoning, you will gain hands-on experience with multimodal data processing pipelines and agent orchestration patterns by implementing core components directly, using good ol' Python.

---
In this hands-on workshop, you will build a multimodal AI agent capable of processing mixed-media content—from analyzing charts and diagrams to extracting insights from documents with embedded visuals. Using MongoDB as a vector database and memory store, and Google's Gemini for multimodal reasoning, you will gain hands-on experience with multimodal data processing pipelines and agent orchestration patterns by implementing core components directly, using good ol' Python.

You will be provided with a GitHub repository consisting of learning materials and resources required to successfully execute the hands-on portions of the workshop.

---related links---

https://www.linkedin.com/in/apoorvajoshi95/

## "Data readiness" is a Myth: Reliable AI with an Agentic Semantic Layer — Anushrut Gupta, PromptQL

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=1nOTQsfe1RU
- Transcript: raw/20250627_1nOTQsfe1RU/1nOTQsfe1RU.en-orig.vtt
- Metadata: raw/20250627_1nOTQsfe1RU/1nOTQsfe1RU.info.json

The rapid progress in LLM capability has not translated to increased reliability for business critical AI use cases. The root-cause? Data is ""not ready"".
Conversational analytics doesn't go beyond the analyst team because it's hard to verify if the generated queries are actually doing what they are supposed to.
RAG based systems often fail to handle the breadth and depth of real world use-cases because it requires a prohibitive amount of preparation & maintenance of an underlying knowledge graph.

Agentic AI systems need to hard-code specific workflows to work reliably and end up looking more like software engineering with LLM calls instead of delivering on the promise of truly agentic workflows.

In all of these failure modes, the common culprit is that the planning or reasoning done by the LLM fails to accurately capture the user's intent or the domain's context aka the lack of a well prepared semantic data layer.

Enterprise data is silo-ed and vastly varying levels of quality and the perfect ""semantic layer"" and ""metadata"" is a moving target. New data is continuously being created and business definitions are rapidly changing and often entirely on-demand.
In this talk we'll share how you can build and maintain a semantic data layer that is maintained entirely by AI, and show (with live examples) how that dramatically improves reliability of the AI system that needs dynamic access to data.
We'll demonstrate how this sufficiently augments existing RAG, text-to-SQL and tool calling techniques and starts opening the door to reliable AI deployments.



---related links---

https://www.linkedin.com/in/anushrut-gupta/
https://promptql.hasura.io/

## Revenue Engineering: How to Price (and Reprice) Your AI Product — Kshitij Grover, Orb

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=1C3sZbaxOmw
- Transcript: raw/20250627_1C3sZbaxOmw/1C3sZbaxOmw.en-orig.vtt
- Metadata: raw/20250627_1C3sZbaxOmw/1C3sZbaxOmw.info.json

You’ve trained the model—now it’s time to train the business. This talk dives into the engineering behind pricing systems that can evolve as fast as your AI stack.

Orb CTO Kshitij Grover will walk through how leading AI companies design infrastructure to support experimentation, scale, and real-world monetization constraints.

Topics include:
- How to meter usage and map it to pricing with accuracy and auditability
- Factoring in margins and underlying costs when designing pricing strategy
- Handling complexity across motions: self-serve vs. enterprise, pay-as-you-go vs. committed contracts
- How to test pricing changes safely (and roll them back when needed)

Whether you’re bootstrapping a pricing system from scratch or replacing a brittle V1, you’ll leave with architectural patterns and mental models to make pricing a first-class engineering concern.

About Kshitij Grover
I’m Kshitij Grover, Co-Founder and CTO of Orb, where we’re building billing infrastructure that gives AI and SaaS teams the tools to treat pricing as a product. My focus is on designing systems that are correct, real-time, and intuitive for developers—because billing should be as thoughtfully engineered as the applications it supports. At Orb, we work closely with engineering teams to help them ship pricing changes with speed and confidence. I’m passionate about the intersection of infrastructure, data, and developer experience. As a speaker at the AI Engineering Summit, I’m excited to share what we’ve learned about building billing systems that scale with modern AI workloads.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## (possible dupe but better sound) What does Enterprise Ready MCP mean? — Tobin South, WorkOS

- Upload date: 2025-06-27
- Video: https://www.youtube.com/watch?v=0MqYA52iWQU
- Transcript: raw/20250627_0MqYA52iWQU/0MqYA52iWQU.en-orig.vtt
- Metadata: raw/20250627_0MqYA52iWQU/0MqYA52iWQU.info.json

Everyone is building MCP servers: from Slack integrations to personal data tools. They're good demos, but not ready to turn into production. So, what does it take to make MCP *enterprise-ready?*

We're going to cover the end-to-end process of getting a hacky MCP server authenticated, permissioned, and secure. We'll talk about registries, SSO, audit logs, agent identifiers, autonomy for agents, and oversight. Oh and we'll use MCP to buy some stuff.

Come learn the stack needed to scale your MCP to the enterprise and some fun hacks along the way.

---

Tobin is a PhD from MIT, a fellow at Stanford as the research lead of the Safe and Useful AI Agents initiative, and the head of AI agents for WorkOS.  He's an experienced speaker having presented at events from AI conferences through the world economic forum.

## Fun stories from building OpenRouter and where all this is going - Alex Atallah, OpenRouter

- Upload date: 2025-06-25
- Video: https://www.youtube.com/watch?v=84Vtz2IL1Ug
- Transcript: raw/20250625_84Vtz2IL1Ug/84Vtz2IL1Ug.en-orig.vtt
- Metadata: raw/20250625_84Vtz2IL1Ug/84Vtz2IL1Ug.info.json

How the first LLM aggregator got started, some of the weird moments in its early growth, architecture challenges, and where we'll be taking it down the road.

OpenRouter has just raised $40m from a16z and others: https://x.com/xanderatallah/status/1937957937692938292

---
The Genesis of OpenRouter [00:00]
Initial Question [01:16]: The story begins in early 2023 with the founder, Alex Atallah, pondering if the AI inference market would be dominated by a single player. He noticed the emergence of new models beyond OpenAI and a growing desire from developers to understand the nuances of different models, including their moderation policies [01:48].

The Rise of Open Source [02:35]: The video highlights the beginning of the open-source AI race, with early models like Bloom 176B and OPT from Facebook [02:46]. A pivotal moment was the release of Meta's Llama 1 in February, which surprisingly outperformed GPT-3 on many benchmarks [03:28], signaling a shift in the landscape.

The Alpaca Moment [04:38]: A major breakthrough occurred in March 2023 with the distillation of Alpaca. Stanford researchers demonstrated that by fine-tuning Llama 1 with outputs from GPT-3, they could transfer the style and knowledge of a larger model to a smaller one for less than $600. This proved that creating powerful, specialized models no longer required massive budgets [04:58].

From a Chrome Extension to a Marketplace
Window AI [06:43]: Before OpenRouter, Atallah launched Window AI, an open-source Chrome extension that empowered users to select their preferred LLM for any web application. This project laid the groundwork for what was to come.

The Launch of OpenRouter [07:18]: OpenRouter was co-founded with Lewis, the creator of the framework that Window AI was built on. Initially, it was a simple aggregator to collect models in one place.

Growth and Evolution [07:57]: OpenRouter quickly evolved into a marketplace, driven by the proliferation of model providers with varying prices, performance, and features. The platform has seen impressive growth, with a 10-100% month-over-month increase for two years. It now offers a single API for over 400 models from more than 60 providers [08:07].

Marketplace Dynamics [08:57]: The transition to a marketplace was a response to the complexity of the growing AI ecosystem. By aggregating providers, OpenRouter helps developers achieve better uptime for both open-source and closed-source models and provides valuable data on latency and throughput [10:27].

The Future of OpenRouter
Expanding Modalities [17:02]: The future vision for OpenRouter includes incorporating models that can generate images and "transfusion models" that allow for conversations with images.

Smarter Routing [17:51]: The platform plans to implement more sophisticated routing mechanisms, including geographical routing and enterprise-level optimizations for GPU allocation.

Enhanced Discovery [18:07]: To help developers find the best models for their needs, OpenRouter aims to improve prompt observability, introduce more granular model categorization, and continue to offer competitive pricing.

About Alex Atallah
Cofounder & CEO of OpenRouter, the first LLM aggregator and distributor. Cofounder of OpenSea, the first NFT marketplace.

Helped grow OpenSea to over $4B in monthly volume from 2017 to 2022.

Founded OpenRouter in early 2023, which processes over 2 trillion tokens weekly across over 400 unique language models, as of May 2025.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Building AI Agents that actually automate Knowledge Work - Jerry Liu, LlamaIndex

- Upload date: 2025-06-24
- Video: https://www.youtube.com/watch?v=jVGCulhBRZI
- Transcript: raw/20250624_jVGCulhBRZI/jVGCulhBRZI.en-orig.vtt
- Metadata: raw/20250624_jVGCulhBRZI/jVGCulhBRZI.info.json

Agents are all the rage in 2025, and every single b2b SaaS startup/incumbent promises AI agents that can "automate work" in some way.

But how do you actually build this? The answer is two fold:
1. really really good tools
2. carefully tailored agent reasoning over these tools that range from assistant-to-automation based UXs.

The main goal of this talk is to a practical overview of agent architectures that can automate real-world work, with a focus on document-centric tasks. Learn the core building blocks of best-in-class "tools" around processing, manipulating, and indexing/retrieving PDFs to Excel spreadsheets. Also learn the range of agent architectures suited for different tasks, from chat assistant-based UXs with high human-in-the-loop, to automation UXs that rely on encoding a business process into an end-to-end task solver. These architectures have to be generalizable but also highly accurate as agents get increasingly better at reasoning and code-writing.

About Jerry Liu
Jerry is the co-founder/CEO of LlamaIndex, the most accurate and flexible way to automate your document workflows with AI agents. Before this, he led the ML monitoring team at Robust Intelligence, did self-driving AI research at Uber ATG and worked on recommendation systems at Quora.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## RFT, DPO, SFT: Fine-tuning with OpenAI — Ilan Bigio, OpenAI

- Upload date: 2025-06-23
- Video: https://www.youtube.com/watch?v=JfaLQqfXqPA
- Transcript: raw/20250623_JfaLQqfXqPA/JfaLQqfXqPA.en-orig.vtt
- Metadata: raw/20250623_JfaLQqfXqPA/JfaLQqfXqPA.info.json

Full workshop covering all forms of fine-tuning and prompt engineering, like SFT, DPO, RFT, prompt engineering / optimization, and agent scaffolding.

About Ilan Bigio
Ilan Bigio is a founding member of OpenAI’s Developer Experience team where he explores model capabilities, builds demos and developer tools, and shares his learnings through talks and docs.

His work includes creating the AI phone ordering demo showcased at DevDay 2024, leading technical development for Swarm, the precursor to the Agents SDK, and contributing to Codex CLI. Prior to that, he was a Solutions Architect at OpenAI, partnering with companies like Cursor, Khan Academy, and Klarna to shape their AI products. Before OpenAI, he was a full-stack Software Engineer at Google, building for YouTube at scale.

Ilan’s journey started as a hobby hacker, diving into operating systems and reverse engineering, before shifting to language models in 2020. He created projects like ShellAI—an open-source, AI-powered terminal assistant—and is passionate about sharing knowledge. With a multidisciplinary background spanning web development, AI/ML, and operating systems, he’s designed and taught courses at Brown and continues to share his expertise through in-depth technical OpenAI guides on topics like Function Calling, Latency Optimization, and Agent Orchestration.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Windsurf everywhere, doing everything, all at once - Kevin Hou, Windsurf

- Upload date: 2025-06-23
- Video: https://www.youtube.com/watch?v=JVuNPL5QO8Q
- Transcript: raw/20250623_JVuNPL5QO8Q/JVuNPL5QO8Q.en-orig.vtt
- Metadata: raw/20250623_JVuNPL5QO8Q/JVuNPL5QO8Q.info.json

In this video, we explore the evolution of Windsurf, its core philosophy, and its ambitious vision for the future of AI in software development.

Here's what you'll learn:

00:00 - Introduction to Windsurf: Discover the rapid growth and key features of this AI Engineer World's Fair product, including web search, MCP support, auto-generated memories, and parallel agents.
02:18 - The Core Philosophy: Learn about the "secret sauce" behind Windsurf's intuitive, mind-reading AI, which creates a shared timeline between humans and AI.
03:46 - Windsurf Everywhere: See the vision for Windsurf to ingest context from all developer tools, including Google Docs, Figma, GitHub, Notion, and Linear.
06:21 - Windsurf Doing Everything: Explore how the AI will expand beyond coding to interact with third-party services, write design documents, and more.
08:40 - Windsurf On All the Time: Understand the goal of creating a nearly autonomous AI that works in the background to assist developers.
11:17 - Introducing SWE-1: Get a first look at the new software engineering model trained for entire workflows.
11:36 - Benchmarking Success: Learn about the End-to-End Task Benchmark and Conversational SWE Task Benchmark, showcasing Windsurf's impressive results.
13:32 - The Data Flywheel: Understand the feedback loop that drives Windsurf's continuous improvement.
14:49 - The Future of AI Products: Hear Kevin's thoughts on the harmony of model, data, and application needed to build successful AI products in 2025.


About Kevin Hou
Kevin is the head of product engineering at Windsurf, where he builds AI-powered developer tools. He has spent much of his career in AI, previously working as a tech lead manager at Nuro, an autonomous vehicle startup, as well as other companies like Airbnb & Salesforce. Kevin enjoys photography, playing basketball, and woodworking. He studied computer science & ML at Princeton University.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Case Study + Deep Dive: Telemedicine Support Agents with LangGraph/MCP - Dan Mason

- Upload date: 2025-06-22
- Video: https://www.youtube.com/watch?v=sn79oS4MZFI
- Transcript: raw/20250622_sn79oS4MZFI/sn79oS4MZFI.en-orig.vtt
- Metadata: raw/20250622_sn79oS4MZFI/sn79oS4MZFI.info.json

We've all seen website chat bots which can look up an order or answer a basic question -- but what does it take to build autonomous agents which manage long, delicate processes like multi-day medical treatments?

In this workshop, we'll explore a workflow Stride built in partnership with Avila (https://avilascience.com/) that helps patients self-administer medication regimens at home. The stack includes LangGraph/LangSmith, Claude, MCP, Node.js, React, MongoDB, and Twilio, and rests on a foundation of treatment "blueprints" which LLM-powered agents use to guide patients to good outcomes.

You'll learn how to: -Build a hybrid system of code and prompts that leverages LLM decisioning to drive a web application, message queue and database -Design and maintain flexible agentic workflow blueprints, with no special tools (just Google Docs!) -Create an agent evaluation system, which uses LLM-as-a-judge to evaluate the complexity of each interaction and escalate to human support when needed

We'll also talk about the prompt engineered guidelines and guardrails which helps agents adhere to protocol as much as possible, while gracefully handling curveballs from the patient. Please bring questions -- we look forward to sharing our learnings on how to make agentic systems like this work in the real world!

About Dan Mason
Dan is a product and technology leader with unusually broad experience -- in 20+ years at companies like ESPN, Shutterstock, Viacom, NBCUniversal and a variety of startups and scaleups, he’s accumulated a wealth of knowledge about how digital product development works (and doesn’t), and is excited to apply those insights to reimagining teams and products in the age of LLMs.   He is an engineer turned product manager with strong technical skills, and the teams he leads are highly cross-functional -- often including product, technology, design, PMO and data science.

Dan leads Stride’s AI/LLM practice and is focused on thought leadership, code generation, workflow automation, and shaping and leading generative AI client engagements. He is also an active product coach and consultant, and a member of Docker’s Technical Advisory Group. Dan lives in New Jersey with his wife and three busy teenagers, and holds a BA in Computer Science and English Literature from Williams College.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Building Agents with Amazon Nova Act and MCP - Du'An Lightfoot, Amazon (Full Workshop)

- Upload date: 2025-06-21
- Video: https://www.youtube.com/watch?v=wFTVEDYVJT0
- Transcript: raw/20250621_wFTVEDYVJT0/wFTVEDYVJT0.en-orig.vtt
- Metadata: raw/20250621_wFTVEDYVJT0/wFTVEDYVJT0.info.json

In this 2-hour workshop, participants will gain practical hands-on experience building sophisticated AI agents using Amazon's agent technologies. You'll learn to build agents that can navigate the web like humans, perform complex multi-step tasks, and leverage specialized tools through natural language commands. You’ll explore Amazon Nova Act for reliable web navigation, Model Context Protocol (MCP) for connecting agents to external data sources and APIs, and Amazon Bedrock Agents for orchestrating complex workflows. Through guided exercises, you'll create agents capable of retrieving information and taking action across web applications, all through natural language interactions. By the end of this workshop, you'll have the practical skills to build AI agents that can browse websites, interact with web interfaces, and solve multi-step problems by combining these powerful Amazon technologies.

About Du'An Lightfoot
Du’An is an Air Force veteran and Sr. Developer Advocate at AWS. He has 10+ years of designing, implementing, and supporting enterprise infrastructures. At AWS he uses his experience and knowledge to help customers learn and build on AWS.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Veo 3 for Developers — Paige Bailey, Google DeepMind

- Upload date: 2025-06-21
- Video: https://www.youtube.com/watch?v=hlcAZ2lX_ZI
- Transcript: raw/20250621_hlcAZ2lX_ZI/hlcAZ2lX_ZI.en-orig.vtt
- Metadata: raw/20250621_hlcAZ2lX_ZI/hlcAZ2lX_ZI.info.json

This talk will briefly trace the history of video generation models before diving into Veo 3, Google DeepMind's latest state-of-the-art model that marks a significant leap by generating video with synchronized audio—including dialogue, sound effects, and music—all from text and image prompts. We'll show how it can understanding intricate details, maintain coherence over longer sequences, and simulate realistic physics and camera movements.

For developers, Veo 3, accessible via Vertex AI (preview), unlocks many new capabilities. We'll discuss how its advanced capabilities, such as semantic context rendering and cinematic control, can empower innovation in filmmaking, game development, education, and more. This session will cover how developers can integrate Veo 3 into their workflows, or test it out today in the Gemini App, Flow, and via the Gemini APIs on Google Cloud.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## The Web Browser Is All You Need - Paul Klein IV, Browserbase

- Upload date: 2025-06-20
- Video: https://www.youtube.com/watch?v=YRGjll7uu5w
- Transcript: raw/20250620_YRGjll7uu5w/YRGjll7uu5w.en-orig.vtt
- Metadata: raw/20250620_YRGjll7uu5w/YRGjll7uu5w.info.json

With the rise of MCP servers, A2A, and our trusty friend, OpenAPI, it turns out the web browser may be the default MCP server for the rest of the internet.

In this talk, we'll walk through how a web browsing tool is probably the only tool you'll need to enable production AI Agents.

About Paul Klein IV
Paul Klein IV is a San‑Francisco‑based serial entrepreneur and engineer. After honing his chops at Twilio during it's IPO and founding Stream Club—a live‑streaming platform acquired by Mux in 2021 he launched Browserbase in 2024 to give developers and AI agents fast, reliable, multi‑region headless‑browser infrastructure. In its first 12 months, Klein raised $27.5 million (a $6.5 M seed and a $21 M Series A led by CRV and Kleiner Perkins with Okta Ventures) . He views Browserbase as the “last‑mile” interface between large language models and the web, enabling end‑to‑end workflow automation far beyond traditional scraping 

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Building Protected MCP Servers — Den Delimarsky and Julia Kasper, MCP Steering Committee & Microsoft

- Upload date: 2025-06-20
- Video: https://www.youtube.com/watch?v=PHBGhUKAM-w
- Transcript: raw/20250620_PHBGhUKAM-w/PHBGhUKAM-w.en-orig.vtt
- Metadata: raw/20250620_PHBGhUKAM-w/PHBGhUKAM-w.info.json

Join us to see how VS Code and GitHub Copilot's expanding suite of AI features can match or even surpasses the benefits of other popular AI developer tools. We'll focus on practical scenarios to ensure immediate applicability and work through live demos of Copilot features such as: Code generation using Edits, Planning/problem solving using Chat, Inline terminal command generation, Boilerplate code generation using Agent mode, Improving boilerplate with custom instructions and then refactoring using Agent mode and Edits, Improving test generation and code reviews with custom instructions, as well as an Introduction to MCP.

About Den Delimarsky 
I am a Principal Product Engineer, currently working at Microsoft, where I help build developer tools and AI-powered experiences that make engineers more productive. You can learn more @ den.dev/about.

About Julia Kasper
Julia Kasper is a member of the Microsoft Developer Division focusing on the developer experience for the Microsoft Power Platform. She is passionate about scenarios where you extend the Power Platform with Azure services and have the best possible end-to-end experience.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## The State of MCP observability: Observable.tools — Alex Volkov and Benjamin Eckel, W&B and Dylibso

- Upload date: 2025-06-20
- Video: https://www.youtube.com/watch?v=Lcqat4iP_lE
- Transcript: raw/20250620_Lcqat4iP_lE/Lcqat4iP_lE.en-orig.vtt
- Metadata: raw/20250620_Lcqat4iP_lE/Lcqat4iP_lE.info.json

AI Engineers deserve observable tools!

MCP getting adoption means that less and less of your agents code is running under your control, and this has DX and observability challenges, let's fix that!

Join Alex Volkov from Weights & Biases and Steve Manual from mcp.run on this recap of the current state of MCP observability, including the observable.tools initiative, a recap of where the field stands and what to look forward to + a practical example of MCP tool usage evaluation framework from mcp.run!

About Alex Volkov
Alex Volkov is an AI Evangelist at Weights & Biases as well as the founder and host of ThursdAI, a weekly newsletter and podcast that explores the latest innovations in AI, their practical applications, and the open-source AI community. Alex is an AI startup founder with 20 years of full-stack software engineering experience, offering a deep well of insights into AI innovation. He’s celebrated for his ability to clarify and summarize the complexities of the rapid AI advances and advocating for its beneficial uses.

About Benjamin Eckel
Benjamin has over a decade of experience as a software engineer and is the co-founder and CTO of Dylibso. He previously led DX at Recurly and worked on integrations and edge observability at Datadog.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## The Geopolitics of AI Infrastructure - Dylan Patel, SemiAnalysis

- Upload date: 2025-06-19
- Video: https://www.youtube.com/watch?v=Zz4QjZsYWK0
- Transcript: raw/20250619_Zz4QjZsYWK0/Zz4QjZsYWK0.en-orig.vtt
- Metadata: raw/20250619_Zz4QjZsYWK0/Zz4QjZsYWK0.info.json

As AI reshapes the global balance of power, the infrastructure behind it—chips, data centers, power, and supply chains—has become a new arena for geopolitical competition. This talk explores how nations are racing to secure critical AI hardware, control compute capacity, and assert influence over the technologies and talent that define the future.

About Dylan Patel
Dylan is the founder, CEO, and Chief Analyst for SemiAnalysis, the preeminent authority on all things AI and semiconductors. Through Dylan’s unwavering commitment to excellence, he has built the firm from the ground up as the thought leader from the semiconductor supply chain to the cloud ecosystem, machine learning models, and all things in between. Since 2020, SemiAnalysis has transformed its business from a solo venture into a cohesive and focused team to provide breaking news and in-depth analysis for the most strategic, complex, and escalating challenges in the semiconductor industry.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## Remote MCPs: What we learned from shipping — John Welsh, Anthropic

- Upload date: 2025-06-19
- Video: https://www.youtube.com/watch?v=0NHCyq8bBcM
- Transcript: raw/20250619_0NHCyq8bBcM/0NHCyq8bBcM.en-orig.vtt
- Metadata: raw/20250619_0NHCyq8bBcM/0NHCyq8bBcM.info.json

We recently released remote MCP support for both claude.ai and the Anthropic API. This talk will cover architectural decisions we made in our implementation, remote MCP authentication, supporting engineers who are building out agentic AI tools, implementing custom internal transports, and whatever else we can fit into 18 minutes of your time.

About John Welsh
I'm John Welsh, a software engineer who's been building large scale systems for the past 20 years. I'm currently at Anthropic, where I've been building our public API and defining how internal systems communicate with MCP servers and other integrations.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## MCP: Origins and Requests For Startups — Theodora Chu, Model Context Protocol PM, Anthropic

- Upload date: 2025-06-18
- Video: https://www.youtube.com/watch?v=x-8pBqWiTzk
- Transcript: raw/20250618_x-8pBqWiTzk/x-8pBqWiTzk.en-orig.vtt
- Metadata: raw/20250618_x-8pBqWiTzk/x-8pBqWiTzk.info.json

Learn more about the latest updates on MCP and get ideas for what startups to build.

About Theodora Chu
Theo is a product manager at Anthropic, focused on bringing knowledge to models. She works on the Anthropic API as well as MCP. Prior to Anthropic, she spent much of her career building zero-to-one products at her own startup as well as at Stripe. She's come full circle since dropping out of her master's in NLP at Stanford.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## How to Build Trustworthy AI — Allie Howe

- Upload date: 2025-06-16
- Video: https://www.youtube.com/watch?v=n6wHJDqlS1I
- Transcript: raw/20250616_n6wHJDqlS1I/n6wHJDqlS1I.en-orig.vtt
- Metadata: raw/20250616_n6wHJDqlS1I/n6wHJDqlS1I.info.json

Trust is a multifaceted outcome that results when product and engineering teams work together to build AI that is aligned, explainable, and secure. Learn strategies for how to build trustworthy AI and why trust is paramount for AI systems.

Trustworthy AI = AI Security + AI Safety

Learn about the differences between AI Security and AI Safety and how the three focus areas of MLSecOps + AI Red Teaming + AI Runtime Security can help you achieve both and ultimately build Trustworthy AI. 

Trustworthy AI Issues in the news:
https://x.com/syddiitwt/status/1923427722241487297
https://fingfx.thomsonreuters.com/gfx/legaldocs/egvblxokkvq/Walters%20v%20OpenAI%20-%20order.pdf?ref=claritasgrc.ai

MLSecOps Resources
Modelscan https://github.com/protectai/modelscan
Community: mlsecops.com

AI Red Teaming Resources:
https://azure.github.io/PyRIT/
https://ashy-coast-00aeb501e.6.azurestaticapps.net/MS_AIRT_Lessons_eBook.pdf

AI Runtime Security Resources:
https://www.pillar.security/solutions#ai-detection
https://noma.security/

Showcasing Trustworthy AI to Customers/Prospects
https://www.vanta.com/collection/trust/what-is-a-trust-center

## Exposing Agents as MCP servers with mcp-agent: Sarmad Qadri

- Upload date: 2025-06-11
- Video: https://www.youtube.com/watch?v=uFPAtKIN-FQ
- Transcript: raw/20250611_uFPAtKIN-FQ/uFPAtKIN-FQ.en-orig.vtt
- Metadata: raw/20250611_uFPAtKIN-FQ/uFPAtKIN-FQ.info.json

In this talk, we will show that agents can be represented as MCP servers, allowing them to be run from any MCP client (such as Claude, Cursor and other applications).

This is made possible with [mcp-agent](https://github.com/lastmile-ai/mcp-agent), a simple, composable framework to build agents using [Model Context Protocol](https://modelcontextprotocol.io/introduction).

## Overview

Currently "agentic" behavior exists only on the MCP client side – clients like Claude or Cursor use MCP servers, which are often simple tool APIs, to solve tasks.

However, if Agents are MCP servers themselves, then any MCP client can invoke, coordinate and orchestrate agents the same way it does with any other MCP server.

This paradigm shift enables: 
1. **Agent Composition**: Build complex multi-agent systems over the same base protocol (MCP).
 2. **Platform Independence**: Use your agents from any MCP-compatible client 
3. **Scalability**: Run agent workflows on dedicated infrastructure, not just within client environments 
4. **Customization**: Develop your own agent workflows and reuse them across any MCP client.

## Background

mcp-agent was inspired by 2 foundational updates that Anthropic introduced for AI application developers:

1. [Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) - a standardized interface to let any software be accessible to AI assistants via MCP servers.

2. [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) - a seminal writeup on simple, composable patterns for building production-ready AI agents.

`mcp-agent` puts these two foundational pieces into an AI application framework:

1. It handles the pesky business of managing the lifecycle of MCP server connections.

2. It implements every pattern described in Building Effective Agents, and does so in a _composable_ way, allowing you to chain these patterns together.

Now as MCP continues to grow adoption, we are exploring advanced agent architectures that allow for sophisticated workflows in simple ways.

## Supercharging developer workflow with Amazon Q Developer - Vikash Agrawal

- Upload date: 2025-06-10
- Video: https://www.youtube.com/watch?v=utxVvGJ4bcg
- Transcript: raw/20250610_utxVvGJ4bcg/utxVvGJ4bcg.en-orig.vtt
- Metadata: raw/20250610_utxVvGJ4bcg/utxVvGJ4bcg.info.json

Supercharging Developer Workflow with Amazon Q Developer

Tired of repetitive coding tasks? What if AI could handle coding, testing, documentation, and deployment for you? In this session, we’ll build the classic 2048 game from scratch using Amazon Q Developer, demonstrating how AI can streamline the development workflow.

Key highlights:
✅ /dev – AI-powered code generation
✅ /test – Automated unit test creation
✅ /doc – Instant documentation generation
✅ /review – AI-assisted code review
✅ Amazon Q Developer in CLI
✅ /dev – Deployment script generation
✅ Deploy & Debug – Seamless AWS deployment & debugging in CloudWatch

By the end of this session, you’ll see firsthand how Amazon Q Developer can boost productivity, reduce boilerplate, and help you ship faster. Let’s build smarter, not harder! 🚀

## Just do it. (let your tools think for themselves) - Robert Chandler

- Upload date: 2025-06-10
- Video: https://www.youtube.com/watch?v=lp0pswT_FEI
- Transcript: raw/20250610_lp0pswT_FEI/lp0pswT_FEI.en-orig.vtt
- Metadata: raw/20250610_lp0pswT_FEI/lp0pswT_FEI.info.json

There's a new type of wrapper in town. The MCP API wrapper. 

Make them thin and you'll be wondering why your chatbot is struggling to even send a Slack message (true story). But make them _agentic_ and the world is unlocked. 

In this talk I'll demonstrate the drawbacks using low level APIs as MCPs and show the magic that happens when your 'tools' are actually other agents. It's prompts all the way down baby!

## Break It 'Til You Make It: Building the Self-Improving Stack for AI Agents - Aparna Dhinakaran

- Upload date: 2025-06-10
- Video: https://www.youtube.com/watch?v=Qvp9vw4jJQ8
- Transcript: raw/20250610_Qvp9vw4jJQ8/Qvp9vw4jJQ8.en-orig.vtt
- Metadata: raw/20250610_Qvp9vw4jJQ8/Qvp9vw4jJQ8.info.json

Building and shipping an AI agent is just the beginning. In real-world systems, the real work starts after deployment — when agents drift, fail silently, or underperform in edge cases no one anticipated.

This talk is about building the full monitoring and improvement stack that keeps agents reliable, efficient, and improving over time. We’ll walk through how to connect evals, tracing, observability, experimentation, and optimization into a virtuous cycle — one where agents not only perform, but learn and adapt in production.

Drawing on real-world deployments, I’ll cover:

- Composing evaluation layers that surface meaningful failure modes
-Tracing and instrumentation for deep visibility into agent behavior
-Running experiments that actually improve outcomes
-Closing the loop with feedback-driven optimization
- People know to improve the agents application, but do they also know they need to improve their evals in tandem?

If you’re scaling agents beyond the prototype phase, this is the talk that helps you move from working once to working continuously.

## MCPs are Boring (or: Why we are losing the Sparkle of LLMs) - Manuel Odendahl

- Upload date: 2025-06-10
- Video: https://www.youtube.com/watch?v=J3oJqan2Gv8
- Transcript: raw/20250610_J3oJqan2Gv8/J3oJqan2Gv8.en-orig.vtt
- Metadata: raw/20250610_J3oJqan2Gv8/J3oJqan2Gv8.info.json

With the mainstream spread especially in coding and with agents, we are starting to imprison ourselves in little cargo culted boxes of what llms and agents are.

I’ll hopefully show you a couple of ideas so you can delve deeper and learn to unleash and harness the shoggoth.

You’re absolutely right – this is the talk you don’t want to miss!

https://x.com/ProgramWithAi/status/1929226124019564993

## The Many Ends of Programming - Ray Myers

- Upload date: 2025-06-10
- Video: https://www.youtube.com/watch?v=5s6Q-y42ZZA
- Transcript: raw/20250610_5s6Q-y42ZZA/5s6Q-y42ZZA.en-orig.vtt
- Metadata: raw/20250610_5s6Q-y42ZZA/5s6Q-y42ZZA.info.json

AI will reshape Software Engineering – but how remains an open question. Will the developers’ role evolve, or vanish entirely? Are we heading toward an Innovator’s Paradise or an Infinite Pile of Garbage?

Visions of the future are so wildly divergent that we struggle to even agree on terms, let alone direction. In this talk, we’ll cut through the noise by exploring six distinct “endgames” for programming in the age of AI. Each offers a different lens on what we build, how we build, and who (or what) is doing the building.

By naming and examining these futures, we gain a clearer view of what’s ahead and a chance to choose our destination.

## Why Bolt.new Won and Most DevTools AI Pivots Failed - Victoria Melnikova

- Upload date: 2025-06-10
- Video: https://www.youtube.com/watch?v=3YRrBFeQ1aw
- Transcript: raw/20250610_3YRrBFeQ1aw/3YRrBFeQ1aw.en-orig.vtt
- Metadata: raw/20250610_3YRrBFeQ1aw/3YRrBFeQ1aw.info.json

Everyone's pivoting to AI—but most are doing it wrong. After conducting in-depth interviews with leaders at 17 developer tools startups that attempted to "add AI" to their roadmap, I've uncovered the patterns that led to either spectacular success or painful failure. This isn't abstract theory—it's battle-tested wisdom from companies that bet their future on AI and lived to tell the tale.

You'll learn:
- The three most common AI pivot traps that led otherwise promising startups to burn through runway with nothing to show for it
- Why adding an AI feature doesn't constitute a real AI transformation (and what actually does)
- The counterintuitive "backward pivot" strategy that worked for 5 of the most successful transitions
- A practical framework for evaluating if your existing developer tooling can meaningfully evolve in the AI era or needs to be reimagined from scratch

## Beyond Conversation: Why Documents Transform Natural Language into Code - Filip Kozera

- Upload date: 2025-06-10
- Video: https://www.youtube.com/watch?v=2Jom-4Brg6Q
- Transcript: raw/20250610_2Jom-4Brg6Q/2Jom-4Brg6Q.en-orig.vtt
- Metadata: raw/20250610_2Jom-4Brg6Q/2Jom-4Brg6Q.info.json

Natural language is quickly becoming our most powerful programming abstraction, perfectly suited to capture the inherent fuzziness and complexity of real-world problems. But despite the power of AI chatbots, endlessly brainstorming in conversational interfaces rarely leads to clarity or reliable results.

This session explores how structured, document-based natural language is uniquely positioned as the ultimate interface for humans to precisely describe complex systems. We'll discuss why conversational interfaces often fail at forcing clarity, and how shifting to a document-driven model ensures that humans articulate their intent clearly and rigorously.

Attendees will learn:

Why natural language (not code) is the most intuitive way to describe complex systems

How documents inherently force clarity, rigor, and structured thinking compared to chatbots

Real-world examples of document-based programming for building reliable, deployable AI systems

Practical insights into transitioning from conversational brainstorming to structured document-driven workflows

## The 4 Patterns of AI Native Development — Patrick Debois

- Upload date: 2025-06-04
- Video: https://www.youtube.com/watch?v=9u6xvcNJaxc
- Transcript: raw/20250604_9u6xvcNJaxc/9u6xvcNJaxc.en-orig.vtt
- Metadata: raw/20250604_9u6xvcNJaxc/9u6xvcNJaxc.info.json

AI is fundamentally reshaping software development roles and activities. While the change is obvious, understanding the actual shifts taking place on the individual developer remains challenging. 

In this talk, we introduce the four AI Native Dev patterns that are currently emerging:
- From producer to manager: we say what AI needs to do
- From implementation to intent: we care less on the how but focus on the why
- From delivery to discovery: we experiment and learn
- From content creation to knowledge: capture knowhow to get better

We backup these patterns by showcasing features in tools that support these shift.

The aim of the patterns is to help grasp how to position you and your team members 's career effectively in this changing landscape.

## The Voice-First AI Overlay: Designing Conversational Co-Pilots - Gregory Bruss

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=y9YQc9a3gNw
- Transcript: raw/20250603_y9YQc9a3gNw/y9YQc9a3gNw.en-orig.vtt
- Metadata: raw/20250603_y9YQc9a3gNw/y9YQc9a3gNw.info.json

This talk introduces the concept of the 'Voice-First AI Overlay': an AI agent assisting conversations directly within the communication interface, operating either single-sidedly or mediating between participants.

I dive into the engineering and design of such a system. We'll cover how overlays fit into the broader agent orchestration landscape, UI principles, and address the voice-first UX problem: how to design AI overlays that genuinely assist without disrupting the primary human interaction

See a live demo transforming messy, real-time captions into helpful conversational hints in the context of a language lesson.

## ChatGPT is poorly designed. So I fixed it

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=y6L5RkEqQ8g
- Transcript: raw/20250603_y6L5RkEqQ8g/y6L5RkEqQ8g.en-orig.vtt
- Metadata: raw/20250603_y6L5RkEqQ8g/y6L5RkEqQ8g.info.json

Let's fix ChatGPT's greatest design sins. We'll design and build a working app that makes ChatGPT multi-modal and multi-model. And no, you don't need to know what those words mean to use it.

Download the source code: https://github.com/bholmesdev/fixgpt

References from this video:
- Try https://warp.dev to vibe code your own solution
- Watch Scott and Mark's podcast episode, "how to not ship the org chart:" https://www.youtube.com/watch?v=Z1yYcUFzH2A
- Read "Why is AI marketing so, so bad?" by Evan Armstrong at The Leverage: https://www.gettheleverage.com/p/why-is-ai-marketing-so-so-bad

## Arrakis: How To Build An AI Sandbox From Scratch - Abhishek Bhardwaj, OpenAI

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=wsFd22SL1s8
- Transcript: raw/20250603_wsFd22SL1s8/wsFd22SL1s8.en-orig.vtt
- Metadata: raw/20250603_wsFd22SL1s8/wsFd22SL1s8.info.json

Arrakis (https://github.com/abshkbh/arrakis) provides MicroVM-based secure sandboxes for code execution and full computer use. It features first-class support for backtracking, a Python SDK, and a Model Context Protocol (MCP) server.

In this talk, we go under the hood to explore how to architect an AI sandbox from the ground up. We’ll also dive into why sandboxes are becoming essential infrastructure for AI models and agents — enabling the next big unlock in intelligence.

Links -
Slides for the talk available here - https://tinyurl.com/arrakis-aie
Vibe coding with Claude and Arrakis -https://x.com/abshkbh/status/1907480355529203809

## 7 Habits of Highly Effective Generative AI Evaluations - Justin Muller

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=wHhlvcQgi9M
- Transcript: raw/20250603_wHhlvcQgi9M/wHhlvcQgi9M.en-orig.vtt
- Metadata: raw/20250603_wHhlvcQgi9M/wHhlvcQgi9M.info.json

Evaluations are the single most reliable indicator of the health and long term viability of any gen AI project.  As a Principal Applied AI Architect for AWS, I've had the opportunity to look at over 100 different attempts at evaluation frameworks over the last few years. 
In this talk I share some stories about the best and worst, and then distill the 7 most common elements I've seen in successful evaluations.  

Slides at https://d2ot4ns4zf41bm.cloudfront.net/slides/7+Habits+AI+World's+Fair.pptx

## Agents reported thousands of bugs, how many were real? - Ian Butler and Nick Gregory

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=wAQK7O3WGEE
- Transcript: raw/20250603_wAQK7O3WGEE/wAQK7O3WGEE.en-orig.vtt
- Metadata: raw/20250603_wAQK7O3WGEE/wAQK7O3WGEE.info.json

Ever had an AI-generated tweak unexpectedly break your entire project? Agentic software development has impressive promise, but the reality still falls short. In this talk we introduce SM-100, a groundbreaking benchmark designed specifically to evaluate autonomous agents on software maintenance tasks.

We're also excited to announce Bismuth, a generalist software agent with strong performance on such maintenance tasks.

https://bismuth.sh & https://sm100bench.com

## The Coherence Trap: Why LLMs Feel Smart (But Aren’t Thinking) - Travis Frisinger

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=u825uxb7LnA
- Transcript: raw/20250603_u825uxb7LnA/u825uxb7LnA.en-orig.vtt
- Metadata: raw/20250603_u825uxb7LnA/u825uxb7LnA.info.json

Why AI engineers must rethink what intelligence means in the age of large language models.

LLMs aren’t thinking.
No awareness. No reasoning. No plan.
And yet—they feel smart. Shockingly so.

This talk introduces coherence reconstruction, a mental model that explains why LLMs are so useful despite their lack of true understanding. You’ll learn how they generate meaning through latent coherence—a kind of internal gravity that pulls language into alignment with context.

We’ll break down:

+ Why hallucinations happen—and why you can’t fully eliminate them.
+ How prompts act like force vectors, shaping behavior in structured ways.
+ What this all means for reasoning tasks, evaluation practices, and agent design.

If you’re building tools, agents, or workflows with LLMs, this talk will reframe how you think about reliability, cognition, and what "understanding" even means.

🔗 Additional resources:
Blog: https://aibuddy.software/
AI Decision Loop Paper: https://aibuddy.software/papers/2500_chatgpt_conversations_case_study.pdf
AI Decision Loop Git Repo: https://github.com/T-rav/gpt-chat-analysis
AI Coherence Paper: https://aibuddy.software/papers/AI_Coherence_A_Theory_of_Utility_in_Large_Language_Models.pdf
Cat Metal Album: https://www.youtube.com/watch?v=gdV5l0JvdNo&list=PL0X82GOpevvYfPLM-JibRJEizHqCJ6U4H&index=7

## The Knowledge Graph Mullet: Trimming GraphRAG Complexity - William Lyon

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=tYCu_57jzL8
- Transcript: raw/20250603_tYCu_57jzL8/tYCu_57jzL8.en-orig.vtt
- Metadata: raw/20250603_tYCu_57jzL8/tYCu_57jzL8.info.json

There are typically two approaches to working with graphs: property graphs and RDF. These systems are often thought of as different knowledge graph paradigms optimized for different workflows. This talk examines how combining property graph interfaces with RDF triple storage creates an optimal foundation for GraphRAG systems. We'll show how to build and use knowledge graphs using the Dgraph graph database and how knowledge graphs are the foundation of building AI Agents.

Resources:

* Dgraph docs: https://docs.hypermode.com/dgraph/overview
* Hypermode: https://hypermode.com
* hyper-news GitHub repo: https://github.com/johnymontana/hyper-news
* Hypermode Agents early access: https://hyp.foo/agents

## Are MCPs Overhyped? A Rant about MCPs — Henry Mao, Smithery

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=tOou_GJ9Ddk
- Transcript: raw/20250603_tOou_GJ9Ddk/tOou_GJ9Ddk.en-orig.vtt
- Metadata: raw/20250603_tOou_GJ9Ddk/tOou_GJ9Ddk.info.json

AI agents are becoming smarter but lack the broad capability to take action in practice. At Smithery, we believe the missing link is an AI orchestration layer—a unified interface that gives agents context, action, and a way to learn from real interactions. This talk explores the problem space in the Model Context Protocol (MCP) ecosystem and how we're tackling it at Smithery.

## Building Reliable Support Agents Using the Effect Typescript Library - Michael Fester

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=sXXl3YMU7ZI
- Transcript: raw/20250603_sXXl3YMU7ZI/sXXl3YMU7ZI.en-orig.vtt
- Metadata: raw/20250603_sXXl3YMU7ZI/sXXl3YMU7ZI.info.json

In this video, we walk through how our team built production-ready support agents using the Effect TypeScript library. The video includes a demo of the agent in action, along with a breakdown of the architecture and design decisions behind it.

We cover what worked well, what was challenging, and why we are continuing to invest in Effect for future development. If you’re building internal tools, working with LLMs, or automating customer support, this talk shares practical lessons on creating robust systems with strong guarantees.

Topics include:
Architectural patterns for agent-based systems
Tradeoffs in developer experience
Techniques for reliability and fault tolerance

Feel free to reach out or share your thoughts:
Twitter: x.com/michaelfester
LinkedIn: linkedin.com/in/michaelfester

## The Robots are coming for your job, and that's okay - Elmer Thomas and Maria Bermudez

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=pSqpC7fFLZA
- Transcript: raw/20250603_pSqpC7fFLZA/pSqpC7fFLZA.en-orig.vtt
- Metadata: raw/20250603_pSqpC7fFLZA/pSqpC7fFLZA.info.json

In a world where AI is revolutionizing API documentation, many wonder: “Why can’t we just use AI to write the docs?” At Twilio, we’ve explored this question deeply. Our Developer Education team found that while generative AI is powerful, it still carries too much risk to be used as an autonomous customer-facing agent. Instead, we use AI to amplify our small team’s impact by automating repetitive tasks, freeing us to focus on high-value, accuracy-critical work.

This talk shares our journey building and deploying AI agents to streamline documentation workflows, support over 100 product managers, and empower less-technical colleagues to contribute. Attendees will learn practical strategies for integrating agentic AI into documentation processes, how to balance automation with human oversight, and ideas for taking their own docs to the next level. This session is ideal for anyone interested in the intersection of AI, APIs, and documentation, especially those on short-staffed teams seeking scalable solutions.

## Blender MCP and The Future Of Creative Tools - Siddharth Ahuja

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=nnktgWtfJHE
- Transcript: raw/20250603_nnktgWtfJHE/nnktgWtfJHE.en-orig.vtt
- Metadata: raw/20250603_nnktgWtfJHE/nnktgWtfJHE.info.json

A dive into the Blender MCP to see how it was made, what use cases for creators it unlocks, and how the future might look for creators.

## Why the Best AI Agents Are Built Without Frameworks (Primitives over Frameworks) — Ahmad Awais, CHAI

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=fcPUqxfrE6Y
- Transcript: raw/20250603_fcPUqxfrE6Y/fcPUqxfrE6Y.en-orig.vtt
- Metadata: raw/20250603_fcPUqxfrE6Y/fcPUqxfrE6Y.info.json

Cursor, v0, chai.new, lovable, bolt — what do they all have in common? They weren’t built on AI frameworks—they're built using primitives optimized for speed, scale, and flexibility.

LLMs are evolving fast—like, literally every week. New standards pop up (looking at you, MCP), and APIs change faster than you can keep track. Frameworks just can't move at this speed.

In this talk, I'll challenge conventional engineering wisdom, sharing my real-world experience scaling thousands of AI agents to handle over 100 million monthly runs.

You'll discover how using AI primitives can dramatically speed up iteration, provide bigger scale, and simplify maintenance. 

I'll share eight practical agent architectures—covering memory management, auto tool integration, and simple serverless deployment—to help you quickly build reliable and scalable AI agents.

By the end of this session, you'll clearly see why we must rethink and rebuild our infrastructure and focus on AI-native primitives instead of heavy, bloated, and quickly outdated frameworks. 

I wonder if we need another S3-moment but for the AI agent infrastructure.

## Unlocking Africa's Potential with AI — Thabang Ledwaba

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=eD_6jP1fkKs
- Transcript: raw/20250603_eD_6jP1fkKs/eD_6jP1fkKs.en-orig.vtt
- Metadata: raw/20250603_eD_6jP1fkKs/eD_6jP1fkKs.info.json

As Africa stands at the crossroads of rapid population growth, urbanization, and digital transformation, Artificial Intelligence (AI) presents unprecedented opportunities to tackle some of the continent’s most pressing challenges. This presentation explores how AI can be harnessed as a tool for sustainable development—addressing issues in healthcare, agriculture, education, infrastructure, and governance.

We’ll delve into real-world applications of AI across African nations, highlight innovative local solutions, and discuss how ethical and inclusive AI development can empower communities, bridge data gaps, and foster economic growth. The session will also examine the importance of homegrown talent, policy frameworks, and cross-sector collaboration in shaping an AI-powered future tailored to Africa’s unique context.

It is time we reimagine the continent’s future through the lens of AI—one that is driven by innovation, equity, and resilience.

## Analyzing 10,000 Sales Calls With AI In 2 Weeks — Charlie Guo

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=dvft0Gp9sEE
- Transcript: raw/20250603_dvft0Gp9sEE/dvft0Gp9sEE.en-orig.vtt
- Metadata: raw/20250603_dvft0Gp9sEE/dvft0Gp9sEE.info.json

AKA: The Data Goldmine You’re Probably Ignoring

Most companies are sitting on mountains of customer data: sales calls, customer support tickets, product reviews, user feedback, and social media interactions. But the truth is that most of this valuable data remains untouched - or worse, unusable.

In this case study, I'll share how our team leveraged Claude to analyze 10,000 sales call transcripts in a handful of days, extracting deep customer insights at scale. We'll cover the AI engineering challenges we faced, including model selection tradeoffs, reducing hallucinations with retrieval-augmented generation (RAG), and optimizing prompt caching to dramatically cut costs and latency (by up to 90% in some cases).

This isn't theoretical - it's a practical blueprint with concrete ROI metrics.
Perfect for AI engineers, data scientists, and anyone sitting on mountains of unstructured customer data they can't analyze at scale.

Read more at https://www.ignorance.ai/

## Agentic Enterprise - What your CEO must know about AI -  Hubert Misztela

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=d7ds6m7fbqg
- Transcript: raw/20250603_d7ds6m7fbqg/d7ds6m7fbqg.en-orig.vtt
- Metadata: raw/20250603_d7ds6m7fbqg/d7ds6m7fbqg.info.json

How large organizations will be transformed by AI?
What people and organizations are scared of because of AI?
What people do not know about AI Agents?
What enterprises need?
Why we might be wrong about Agents and LLMs impact all together? 

Workflows optimization. 
AI beyond LLMs and Agents: Representation Learning + GenAI + New Interfaces.
Context is the new oil, not the data.

Your CEO has to pivot. Now.

## Rust is the language of the AGI - Michael Yuan

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=bbq0b_FpYEY
- Transcript: raw/20250603_bbq0b_FpYEY/bbq0b_FpYEY.en-orig.vtt
- Metadata: raw/20250603_bbq0b_FpYEY/bbq0b_FpYEY.info.json

In the Latent Space podcast, Bret Taylor argued that strongly and statically-typed programming languages, such as Rust, could be especially well suited for AI coding, since the generated code can be validated by compilers for real-time feedback and reinforcement learning. However, unlike weakly or dynamically typed JavaScript or Python, there are few examples of Rust code in LLMs’ training corpora, and hence limiting the LLM's capability in generating Rust code. 

In this talk, we will discuss the open-source Rust Coder project, which provides an integrated agentic framework based on the MCP protocol for generating complete and valid Rust projects. The Rust Coder framework enables the following functionalities for coding LLMs (e.g., Qwen Coder or Codestral).

* Provides Rust example code, explanations, and tutorials relevant to the user’s request within the LLM query context.
* Generates and parses generated code artifacts into Rust Cargo projects.
* Compiles and executes generated Rust Cargo projects.
* Executes the compiled project against test cases.
* Provides coding LLM feedback based on compiler and testing outputs.
* Runs continuously until all issues are fixed.

We will demonstrate how the Rust Coder project works, how to integrate it into your agents, and ways to contribute to the open-source effort. We will also discuss pilot results from a large Rust coding camp (1000+ college students) using the Rust Coder tool.

The Rust Coder is supported by two Linux Foundation Mentorship grants, as well as content provided by the Rust Foundation.

## The Future of Qwen: A Generalist Agent Model — Junyang Lin, Alibaba Qwen

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=b0xlsQ_6wUQ
- Transcript: raw/20250603_b0xlsQ_6wUQ/b0xlsQ_6wUQ.en-orig.vtt
- Metadata: raw/20250603_b0xlsQ_6wUQ/b0xlsQ_6wUQ.info.json

Since Alibaba launched the Qwen series of large models in 2023, the Qwen series of large language models and multimodal large models have been continuously updated and improved. This presentation will introduce the latest developments in the Qwen series of models, including the large language model Qwen3, vision-language large model Qwen2.5-VL, omni model Qwen2.5-Omni, etc. Additionally, this presentation will also cover the future development directions of the Qwen series.

## The End of Awkward AI Transcriptions - Travis Bartley and Myungjong Kim

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=aDj9sY2RoG8
- Transcript: raw/20250603_aDj9sY2RoG8/aDj9sY2RoG8.en-orig.vtt
- Metadata: raw/20250603_aDj9sY2RoG8/aDj9sY2RoG8.info.json

NVIDIA is setting the new global standard for speech AI—with 6 top-ten models on the Hugging Face ASR leaderboard and blazing a trail with models like Parakeet2. In this talk, we’ll pull back the curtain on what it takes to build the world’s fastest, most accurate conversational AI, from open-source research to enterprise-ready NIM microservices that scale across any infrastructure.

We hear you, developers: Whether you’re building call center agents, video dubbing tools, or digital humans, NVIDIA’s ecosystem is designed for you. With Python-first frameworks, intuitive configurators, and a thriving open-source community, we’re making rapid iteration and seamless integration a reality—so you can launch faster, cut costs, and innovate boldly.

Real-world impact is already here. Enterprises are deploying multilingual, noise-robust, and highly customizable voice agents at scale, while our digital human blueprint lets you create interactive avatars. But the real story is the underlying conversational AI stack that’s transforming customer experience, accessibility, and global communication.

Join us to see why developers and industry leaders alike are calling NVIDIA’s speech AI “a game-changer”—and how you can be part of the next wave of conversational intelligence.

## How agents broke app-level infrastructure - Evan Boyle

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=_-oIuRH4oGA
- Transcript: raw/20250603__-oIuRH4oGA/_-oIuRH4oGA.en-orig.vtt
- Metadata: raw/20250603__-oIuRH4oGA/_-oIuRH4oGA.info.json

LLMs have completely broken our assumptions about app-level workloads. Compared to querying a database, LLMs are extremely flakey and slow. In web 2.0, p99 latency was just a few hundred milliseconds - anything higher and the on call is getting paged. 

But today any API that uses LLMs has a p1 latency of a couple of seconds. Yet, the infrastructure we build on top of hasn't caught up with these new assumptions. There isn't a single serverless provider that supports running code for more than a few minutes!

In this session we'll take about infrastructure patterns that used to be niche, but today require attention from anyone building on top of LLMs:

- Durable execution
- Long running workflows and APIs
- Durable execution
- Agent-scoped storage

## Breaking the Chain: Agent Continuations for Resumable AI Workflows - Greg Benson

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=ZB7l4uxW3Yo
- Transcript: raw/20250603_ZB7l4uxW3Yo/ZB7l4uxW3Yo.en-orig.vtt
- Metadata: raw/20250603_ZB7l4uxW3Yo/ZB7l4uxW3Yo.info.json

AI agents are powerful—but brittle. Once an agent chain starts, you either let it run or you tear it down and lose state. Agent Continuations change that contract. Borrowing from programming‑language continuations, we capture an agent’s entire call stack—tools, goals, partial responses—in a compact JSON blob combined with the familiar messages array. The result is a protocol‑level "Agent State" that lets you:

- Pause anytime for human-in-the-loop approval gates, rate‑limit resets, or progressive UI updates.

- Migrate agents across nodes, clouds, even different agent execution platforms

- Checkpoint long‑running multi‑agent plans using off‑the‑shelf storage and enable restarting in the presence of agent failure

- Resume seamlessly through standard LLM function‑calling APIs, so every framework that speaks OpenAI JSON can speak continuations.

Our approach works with single-level agent loops and multi-level agents in which agents can call subagents.

Attendees will leave with open‑source Python snippets and a mental model that turns “monolithic” agents into restart‑able, human‑aware services—shrinking failure windows and unlocking new UX patterns for AI products.

**Key Takeaways**

- Why Continuations are a good construct for Agent State
- Protocol spec and reference JSON examples and a - Python implementation
Live demo: suspend a three‑layer agent with suspending for human approval

** Links **

https://github.com/SnapLogic/agent-continuations
https://agentcreator.com

## RAG Evaluation Is Broken! Here's Why (And How to Fix It) - Yuval Belfer and Niv Granot

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=Ywl4LsvHKzU
- Transcript: raw/20250603_Ywl4LsvHKzU/Ywl4LsvHKzU.en-orig.vtt
- Metadata: raw/20250603_Ywl4LsvHKzU/Ywl4LsvHKzU.info.json

Optimizing local benchmarks, chunking strategies, perfect retrieval scores. If you just nodded along, you're one of many developers building RAG systems optimized for metrics that don't matter in the real world.

But what if our entire approach to evaluating retrieval-augmented generation is fundamentally flawed? The uncomfortable truth is that current RAG benchmarks reward systems that fail spectacularly on realistic information retrieval tasks.

In this talk, I'll expose the critical gaps in how we evaluate RAG systems today, from the chunking catch-22 to the myth of perfectly contained information. Using examples like the "Seinfeld Test," we'll explore why high benchmark scores often lead to disappointed users.

You'll learn practical strategies for meaningful RAG evaluation that reflects how information actually works in the wild, helping you build systems that impress not just benchmark leaderboards, but actual humans.

To learn more, check out the full episode on RAG evaluation on YAAP: https://youtu.be/RsSkwpTmn8o?si=9gIR6EeIzPgbqY4O

## The Demo I Wish I'd Had: OpenAI's Agents SDK... serverless! - Brook Riggio

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=UcW_s4BmuD0
- Transcript: raw/20250603_UcW_s4BmuD0/UcW_s4BmuD0.en-orig.vtt
- Metadata: raw/20250603_UcW_s4BmuD0/UcW_s4BmuD0.info.json

Deploying and orchestrating significant AI workflows on serverless platforms like Vercel presents unique infrastructure challenges, like managing time limits and persistent state, handling task failures, and achieving reliable execution. As an engineer exploring OpenAI's powerful new Agents SDK on Vercel, I initially struggled with fitting sizeable jobs within the limits of our serverless platform.

In this highly practical, hands-on session, you'll experience the demo I wish I'd had—showing exactly how to use Inngest's native integration with Vercel to run OpenAI's Agents SDK for robust orchestration and execution of complex, long-running AI workflows. We'll cover practical solutions for retries, state preservation, and seamless orchestration within the constraints of Vercel's serverless platform.

You'll leave this talk equipped with clear, actionable strategies for implementing production-ready AI infrastructure on Vercel, including essential best practices for monitoring, observability, and robust error handling. Whether you're building your first AI system or enhancing existing workflows, this demo-driven talk provides the tools and insights needed for resilient, scalable AI deployments on Vercel.

Complete demo repo: https://github.com/brookr/serverless-agents 

Please fork this, build your own examples, and send a PR to link to your work!

## Real AI Agents Need Planning, Not Just Prompting - Yuval Belfer

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=Th5e4h-oVmc
- Transcript: raw/20250603_Th5e4h-oVmc/Th5e4h-oVmc.en-orig.vtt
- Metadata: raw/20250603_Th5e4h-oVmc/Th5e4h-oVmc.info.json

AI agents that actually deserve the name - do they even exist? Despite the hype, most "agents" today are just LLMs with fancy prompt engineering tricks, lacking true agency capabilities.

Here's a deeper issue: it's 2025, and LLMs still struggle with basic instruction following. Weird when one of the first big models was literally called "InstructGPT," right? Benchmarks are saturated but meaningless, and without genuine planning abilities, these systems will keep hitting the same walls.

In this session we will go through:
- Why conventional agent frameworks like ReAct miss the mark on true agency
- How dynamic planning creates agents that actually follow complex instructions
- Tips to improve instruction following in any AI system you build

## Will Agent evaluation via MCP Stabilize Agent Networks? - Ari Heljakka

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=RVN9HWKmkNU
- Transcript: raw/20250603_RVN9HWKmkNU/RVN9HWKmkNU.en-orig.vtt
- Metadata: raw/20250603_RVN9HWKmkNU/RVN9HWKmkNU.info.json

Exposing complex AI Evaluation frameworks to AI agents via MCP allows for a new paradigm of agents to self-improve in a controllable manner. Unlike the often unstable straight-forward self-criticism loops, the MCP-accessible evaluation frameworks can provide the persistence layer that stabilizes and standardizes the measure of progress towards plan fulfillment with agents. 

In this talk, we show how MCP-enabled evaluation engine already allows agents to self-improve in a way that is independent of agent architectures and frameworks, and holds promise to become a cornerstone of rigorous agent development.

## MCP Agent Fine tuning Workshop - Ronan McGovern

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=Nqb7JTx0Pqo
- Transcript: raw/20250603_Nqb7JTx0Pqo/Nqb7JTx0Pqo.en-orig.vtt
- Metadata: raw/20250603_Nqb7JTx0Pqo/Nqb7JTx0Pqo.info.json

This is a hands on workshop where students will run an agent with access to MCP servers (a playwright browser, although others can be added), generate high quality reasoning traces, and then train a Qwen3 model on those traces.

Students will learn:
- How to generate high quality MCP agent reasoning traces, via an OpenAI style endpoint
- How to save tools and multi-turn traces
- Fine-tune a Qwen3 model on those traces with unsloth
- Run the fine-tuned model

## From PM at Stripe to Building an AI startup, a recent founder's journey - Mounir Mouawad

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=HIGpxVjGFBw
- Transcript: raw/20250603_HIGpxVjGFBw/HIGpxVjGFBw.en-orig.vtt
- Metadata: raw/20250603_HIGpxVjGFBw/HIGpxVjGFBw.info.json

I spent a bunch of time building products in Big Tech, most recently at Stripe but before that at Google and Amazon. In this short talk I am sharing the highs and lows of building a business in AI and how that differs from building products in Big Tech. May this be an inspiration to would-be founders or useful commiseration material for fellow founders :)

## My AI Thinks I'm Eating My Feelings (and Other Nutritional Insights) - Rami Alhamad

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=Ghc-qalQFLw
- Transcript: raw/20250603_Ghc-qalQFLw/Ghc-qalQFLw.en-orig.vtt
- Metadata: raw/20250603_Ghc-qalQFLw/Ghc-qalQFLw.info.json

Eating well shouldn't require an advanced degree or hours decoding nutrition labels. Alma leverages cutting-edge AI to turn complex nutritional science into straightforward, personalized advice. 

In this talk, we'll dive into how we're using large language models and real-world user data to reshape how people track, understand, and improve their diets. We'll share insights on building user-friendly AI experiences, practical lessons from Alma's journey, and how we're making nutrition advice smarter, simpler, and genuinely helpful—one meal at a time.

## Letting AI Interface with your App with MCP — Kent C Dodds

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=EyZiAp0pelw
- Transcript: raw/20250603_EyZiAp0pelw/EyZiAp0pelw.en-orig.vtt
- Metadata: raw/20250603_EyZiAp0pelw/EyZiAp0pelw.info.json

We are entering a new era of user interaction. It's being built right before our very eyes and changing rapidly. As crazy as it sounds, soon each one of us will get our own Jarvis capable of performing actually useful tasks for us with a completely different user interaction mechanism than we're used to.

But someone's gotta give Jarvis the tools to perform these tasks, and that's where we come in.

In this talk, Kent will live code an MCP server and use it with an AI assistant to help us catch the vision of what this future could look like and our role in it.

## The Benchmarks Game: Why It's Rigged and How You Can (Really) Win - Darius Emrani

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=EnT4Wej5M5k
- Transcript: raw/20250603_EnT4Wej5M5k/EnT4Wej5M5k.en-orig.vtt
- Metadata: raw/20250603_EnT4Wej5M5k/EnT4Wej5M5k.info.json

AI benchmarks control billions in investment and shape entire markets - but the game is rigged. In this talk, I'll expose the three "cheat codes" companies use to game benchmarks:

* Cherry-picking comparisons (xAI's selective Grok-3 graphs)
* Buying privileged access (OpenAI's FrontierMath funding)
* Optimizing for style over substance (Meta's 27 Llama-4 variants on LM Arena)

When Andrej Karpathy says "I don't really know what metrics to look at right now," we have a crisis. I'll show you why Goodhart's Law guarantees benchmarks fail when billions are at stake, and more importantly, what to do about it.

You'll learn:
How to spot benchmark manipulation (with real examples)
Why 39% of score variance is just writing style
A 5-step framework to build evaluations that actually matter for YOUR use case
How pre-deployment evaluation loops separate reliable AI from constant firefighting

Drawing from my experience building evaluation systems at Waymo, Uber ATG, and SpaceX (where bad evals literally crash), I'll show you how to stop playing the rigged benchmarks game and start measuring what actually matters.

## The Current State of Browser Agents - Jerry Wu and Wyatt Marshall

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=Djv8Sp11UjI
- Transcript: raw/20250603_Djv8Sp11UjI/Djv8Sp11UjI.en-orig.vtt
- Metadata: raw/20250603_Djv8Sp11UjI/Djv8Sp11UjI.info.json

Browser agents are here. But beyond simple sample use cases (I'm looking at you flight booking demo), are they as good as advertised? 

In this talk, we introduce Web Bench, a new benchmark we've developed that rigorously tests browser agents across 450+ websites on real-world action based objectives such as info extraction, login/auth, form filling, and others. We'll dive into the results, unpack some unexpected discoveries, and discuss broader implications for the future of general purpose agents. 

You'll walk away with practical insights into:

1. data-driven understanding of the capabilities and limitations of state-of-the-art browser agents
2. how to meaningfully evaluate browser agents 
3. hard-won lessons on designing and launching a benchmark

Come through and see what browser agents can really do.

Resources

Leaderboard - https://webbench.ai/
Technical Report: https://halluminate.ai/blog/benchmark
Github - https://github.com/Halluminate/WebBench
Huggingface - https://huggingface.co/datasets/Halluminate/WebBench

## Stop Ordering AI Takeout  A Cookbook for Winning When You Build In House - Jan Siml

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=DjUIecgpYAo
- Transcript: raw/20250603_DjUIecgpYAo/DjUIecgpYAo.en-orig.vtt
- Metadata: raw/20250603_DjUIecgpYAo/DjUIecgpYAo.info.json

Forget the multi-agent buffet—this is the home-cooked GenAI playbook that actually drives revenue.

In this 10-minute lightning talk, Jan Siml shares how a small, in-house team skipped the hype playbook—no multi-agent pipelines with GraphRAG, no monster eval suites—and still turned an internal GenAI assistant into real business impact.

🔑 What you’ll learn

- Go Deep on One Job-to-Be-Done – depth crushes breadth when you own the data and the user.

- Trace Every Click to Dollars – offline evals don’t sign contracts; revenue funnels do.

- Push, Don’t Wait – zero-click Slack/email nudges outperform shiny chat UIs.

- Convert Time-Saved into Time-Well-Spent – guide the next action, not just the answer.

- Data & UX vs Bigger Models – integrations and better flow move the needle; fancy LLMs mostly move the bill.

If you’re ready to trade Michelin-priced SaaS features for pragmatic, in-house wins—and you like your lessons straight from the kitchen rather than the brochure—hit play. Your AI roadmap (and budget) will thank you.

## Text-to-Speech Data Preparation and Fine-tuning Workshop - Ronan McGovern

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=CXsbjcrf_5g
- Transcript: raw/20250603_CXsbjcrf_5g/CXsbjcrf_5g.en-orig.vtt
- Metadata: raw/20250603_CXsbjcrf_5g/CXsbjcrf_5g.info.json

By the end of this workshop, you'll have train Sesame's CSM-1B text-to-speech model on a voice from a Youtube video. The workshop will cover data preparation, fine-tuning and evaluation.

## Buy Now, Maybe Pay Later: Dealing with Prompt-Tax While Staying at the Frontier - Andrew Thomspson

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=Bf71xMwd-Y0
- Transcript: raw/20250603_Bf71xMwd-Y0/Bf71xMwd-Y0.en-orig.vtt
- Metadata: raw/20250603_Bf71xMwd-Y0/Bf71xMwd-Y0.info.json

Frontier LLMs now drop at warp speed. Each upgrade hits you with a Prompt‑Tax: busted prompts, cranky domain experts, and evals that show up fashionably late.

In this talk I’ll share 18 months of bruises (and wins) from shipping an agentic product for real‑estate lawyers:

• The challenge of an evolving prompt library that breaks every time the model jumps

• The bare‑bones tactics that actually work for faster migrations

•  Our “betting on the model” mantra: ship the newest frontier model even when it’s rough around the edges, then race to close the gaps before anyone else does

Walk away with a playbook to stay frontier‑fresh without blowing up your roadmap or your team’s sanity.

## GPU-less, Trust-less, Limit-less: Reimagining the Confidential AI Cloud - Mike Bursell

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=A0PxE39xaMc
- Transcript: raw/20250603_A0PxE39xaMc/A0PxE39xaMc.en-orig.vtt
- Metadata: raw/20250603_A0PxE39xaMc/A0PxE39xaMc.info.json

What happens when private AI models or sensitive data need to run in the public cloud?

Can we still maintain control – without relying on blind trust?
Can we eliminate that blind trust and make infrastructure verifiable by design?

In this talk, you’ll discover what a “GPU-less” future really means: not the absence of acceleration, but the freedom to collaborate and deploy private AII workloads in a confidential, self-sovereign AI cloud – with open, on-chain guarantees that centralized clouds simply can’t offer. 

No GPU-provider lock-in. No black-box execution. Just algorithmic, sovereign infrastructure – where the confidential cloud is a protocol, not a service.

You’ll learn the foundations of Confidential AI and see real-world results powered by it. 
Then, through four demos on Super Protocol, you’ll learn how to:

1. AI Marketplace & Confidentiality Check – Deploy models in a few clicks and verify on-chain they’re running inside hardware-backed confidential environments.
2. n8n Healthcare AI Workflow – Build and run agentic automations for sensitive data – entirely within confidential environments.
3. Distributed vLLM Inference – Parallelize LLM inference across multiple GPU servers– with zero data exposure and no dependency on any single provider.
4. Provable Medical-Data Training & On-Chain Reporting – Train on multiple sensitive datasets inside confidential environments – no data or IP exposed to participants, infrastructure providers, or Super Protocol – and generate verifiable on-chain proofs of exactly what ran, where, and how.

Join us to discover how you can leverage Confidential AI today – and unlock new possibilities.

Extra resources:
- NVIDIA on Super Protocol: https://developer.nvidia.com/blog/exploring-the-case-of-super-protocol-with-self-sovereign-ai-and-nvidia-confidential-computing
- Website  https://superprotocol.com/
- Super AI Marketplace: https://marketplace.superprotocol.com/
- Documentation: https://docs.superprotocol.com/

## Grounded Reasoning Systems for Cloud Architecture - Iman Makaremi

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=9mzfioh1Zag
- Transcript: raw/20250603_9mzfioh1Zag/9mzfioh1Zag.en-orig.vtt
- Metadata: raw/20250603_9mzfioh1Zag/9mzfioh1Zag.info.json

As LLMs move into enterprise workflows, developers face a new kind of architecture challenge: how do you build reliable, interpretable systems powered by agents and reasoning?

This talk unpacks how we designed and implemented an AI orchestration framework for enterprise architecture — combining LangGraph for multi-agent workflows, Flyte for distributed execution, and AWS Bedrock for LLM inference using Claude 3. The product: an AI copilot for enterprise architects, deeply rooted in your tech stack context.

At the core of this system is a domain-specific **knowledge graph** that acts as long-term memory for the agents. It enables persistent, structured representations of architectural state, system dependencies, and business context — giving the agents the grounding they need to generate accurate recommendations, translate natural language into SQL or code, and maintain continuity across workflows.

We’ll also cover how we’ve integrated observability practices — including planned OpenTelemetry instrumentation — to trace and debug autonomous AI systems in production.

If you’re a developer or AI engineer thinking beyond the chatbot and looking to embed reasoning into complex system design and data tasks, this talk offers an end-to-end blueprint — from orchestration and grounding to production monitoring.

## Invisible Users, Invisible Interfaces: Accelerating Design Iteration with AI Simulation - Alex Liss

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=8D_VdU6DBhI
- Transcript: raw/20250603_8D_VdU6DBhI/8D_VdU6DBhI.en-orig.vtt
- Metadata: raw/20250603_8D_VdU6DBhI/8D_VdU6DBhI.info.json

The genAI explosion has flipped classic software design on its head. Instead of building invisible interfaces, experiences so intuitive they feel second nature, we’ve seen a flood of awkward chatbot overlays and bolt-on features that confuse more than they help. But what if AI could be part of the solution? The path back to seamless design lies in using AI not as a feature, but as a tool for design itself. Through invisible users, like Intelligent Twins for AI-driven audience simulations, and computer use agents for visual evaluation, designers can accelerate needfinding and test interface concepts at scale. This session will explain that by simulating how diverse users experience new interactions, teams can anticipate user needs, reduce friction, and build great interfaces faster. Don’t bolt-on genAI features to existing products and tell people its magic – use AI to design software that actually feels like magic.

## Effective AI Agents Need Data Flywheels, Not The Next Biggest LLM –  Sylendran Arunagiri, NVIDIA

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=6lTxD_oUjXQ
- Transcript: raw/20250603_6lTxD_oUjXQ/6lTxD_oUjXQ.en-orig.vtt
- Metadata: raw/20250603_6lTxD_oUjXQ/6lTxD_oUjXQ.info.json

Building effective AI agents isn’t about using the next biggest LLMs in the market  - it’s about creating self-improving systems with data flywheels. By continuously learning from real-world data and agent interactions, these flywheels help evaluate, retrain, and optimize smaller, faster models that match the performance of large LLMs - at a fraction of the cost and compute.

In this video, learn how NVIDIA uses data flywheels and NeMo microservices to run efficient AI agents with lower TCO and faster inference. Explore a thoughtful framework on building a data flywheel for your own AI agent systems.

#aiagents #dataflywheel #generativeai #modeldistillation #nvidia

## Cognitive Shield Real Time Real Smart - Rachna Srivastava

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=5_QWh4LGoxg
- Transcript: raw/20250603_5_QWh4LGoxg/5_QWh4LGoxg.en-orig.vtt
- Metadata: raw/20250603_5_QWh4LGoxg/5_QWh4LGoxg.info.json

This high-energy demonstration unveils Cognitive Shield, a revolutionary three-level defense system that harnesses AI to combat sophisticated financial fraud. Watch as we showcase real-time deepfake detection, graph intelligence for fraud ring visualization, and cross-channel correlation of threats – all integrated within a comprehensive platform that amplifies human expertise rather than replacing it. 

Learn how the same AI powering today's most dangerous financial attacks can be turned into our strongest defense.

## The RAG Stack We Landed On After 37 Fails - Jonathan Fernandes

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=2CXn-CByNoo
- Transcript: raw/20250603_2CXn-CByNoo/2CXn-CByNoo.en-orig.vtt
- Metadata: raw/20250603_2CXn-CByNoo/2CXn-CByNoo.info.json

Retrieval returning irrelevant results? Can't deploy solutions in the cloud? If these questions keep you up at night, you're likely experiencing the common frustrations of building an effective RAG system. But what if we could systematically optimise each component of the pipeline? 

In this talk, I'll share the insights gained from 37 failed attempts, demonstrating live with documents from a knowledge base and how each optimisation impacts the end result. You'll walk away understanding how to diagnose the weaknesses in your RAG pipeline and apply targeted improvements that dramatically boost performance in real-world applications.

## open-rag-eval: RAG Evaluation without "golden" answers — Ofer Mendelevitch, Vectara

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=1cQlnfwmIdU
- Transcript: raw/20250603_1cQlnfwmIdU/1cQlnfwmIdU.en-orig.vtt
- Metadata: raw/20250603_1cQlnfwmIdU/1cQlnfwmIdU.info.json

Open-RAG-Eval is an open-source framework that revolutionizes RAG evaluation by harnessing the power of LLM judges for scalable, automated evaluation without the need for golden answers or golden chunks. Building on pioneering research from the University of Waterloo, this framework integrates innovative tools like UMBRELA for reference-free relevance scoring and AutoNuggetizer for automated fact-checking. Designed with a flexible connectors architecture, it seamlessly plugs into any RAG pipeline while delivering fast, transparent, and interpretable metrics on retrieval, generation, and hallucination in RAG.

## Luminal - Search-Based Deep Learning Compilers - Joe Fioti

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=0uj9lMI-sIo
- Transcript: raw/20250603_0uj9lMI-sIo/0uj9lMI-sIo.en-orig.vtt
- Metadata: raw/20250603_0uj9lMI-sIo/0uj9lMI-sIo.info.json

Luminal is a deep learning compiler for CPUs, GPUs, and ASICs that takes a search-first approach to discovering efficient kernels, such as flash attention, automatically.

## Designing AI To Scale Human Thought — Jun Yu Tan, Tusk

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=0tVu-V3_fFw
- Transcript: raw/20250603_0tVu-V3_fFw/0tVu-V3_fFw.en-orig.vtt
- Metadata: raw/20250603_0tVu-V3_fFw/0tVu-V3_fFw.info.json

Forget the hype of AI automation replacing jobs. The future lies in human augmentation — revealing blind spots, sparking creativity, and amplifying thoughtful decision-making. In this talk, we’ll explore the principles that distinguish augmentation from automation in AI UX design, covering interaction patterns, design principles, and trust-building feedback loops. Drawing from real-world experiences building AI-powered tools and beyond, we’ll dive into concepts for crafting interfaces that empower users to think smarter, not just work faster. Expect practical insights and a fresh perspective on AI’s role as a collaborative partner.

AI Augmentation: https://jytan.net/blog/2025/ai-augmentation/
Tusk: https://www.usetusk.ai/

## The Agent Native Company — Rick Blalock, Agentuity

- Upload date: 2025-06-03
- Video: https://www.youtube.com/watch?v=0ZPAvzhpGjw
- Transcript: raw/20250603_0ZPAvzhpGjw/0ZPAvzhpGjw.en-orig.vtt
- Metadata: raw/20250603_0ZPAvzhpGjw/0ZPAvzhpGjw.info.json

Are you just using AI—or are you building a company around it?

In this talk, I break down what it means to be an agent-native company—a business designed from the ground up with AI agents at the core of operations, culture, and product. Drawing from my own founder experience (building 14 months of product in 8 weeks with just 6 people and a stack of agents), I’ll walk you through the real-world shift happening right now across tech.

🔍 What you'll learn:

The difference between AI-enhanced vs. AI-native orgs

Why the future of hiring is about AI fluency, not just professional networks or credentials

The rise of new job titles like “Agent Manager” (yes, that’s a real job)

How lean teams can use AI agents to achieve 10x—or even 100x—impact

What “culture is the new stack” really means when humans and AI work together

🧠 Featuring real-world examples, practical hiring insights, and a peek into how workflows and job roles are changing fast.

📈 Whether you’re a founder, tech leader, or just curious about the future of work, this is your guide to scaling smart—with AI at the wheel.
