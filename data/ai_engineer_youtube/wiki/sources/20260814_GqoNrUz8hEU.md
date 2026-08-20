# Bringing agents onto the world wide web — Paul Klein IV, Browserbase

Source: [Bringing agents onto the world wide web — Paul Klein IV, Browserbase](https://www.youtube.com/watch?v=GqoNrUz8hEU)
Uploaded: 2026-08-14
Transcript: `raw/20260814_GqoNrUz8hEU/GqoNrUz8hEU.en-orig.vtt`

## Summary

Klein, the founder of Browserbase, opens on the half-empty computer-use track ("very sleepy crowd… have we all given up at this point?") and argues the stall is not a model problem. Models a year ago were bad at long-horizon tasks; that "has clearly been solved in a major way," and the last six months put as much investment into RL environments for computer use as the prior year put into coding. What is missing is the engineering: "agents are missing the right harness and tools," which he calls a capabilities overhang that any team — not just a lab — can close, pointing at Factory beating baseline Claude Code on the same model and at Cursor as the first harness-engineering company. Working browser agents have three properties. They are **multimodal and write code**: the most reliable ones in production intercept network requests and replay them from a generated script instead of driving pixels, and route simple pages to cheaper models. They carry a **real harness** with skills and memory so a site is not rediscovered every run (Browserbase's `browser.sh` publishes per-site skills; WebMCP feeds the same knowledge), and they compress page context rather than dumping it. And they run on **consistent infrastructure**: "if your infrastructure renders a page in a mobile layout one time and then in a desktop layout the second time, it's going to have inconsistent results" — the anti-pattern being the OpenClaw-era Mac mini at home, SSH'd into and clearing CAPTCHAs off a residential IP ("I've yet to see a SOC 2 compliant Mac mini setup at scale"). He then turns to what the web owes agents: accessibility trees and ARIA rather than raw DOM, Chrome's new WebMCP for site-blessed tool calls, `llms.txt` / `skills.md` / `agents.md`, and two unsolved problems — how an agent logs in on your behalf, and who certifies that an agent is trustworthy ("a Verisign moment for web agents… nobody's come out and done that yet"). The closing thesis is a market claim: "solving computer use accelerates the diffusion of AI to the real economy" — the logistics company in Singapore, the bank in South Africa, the lumber factory in Mexico, all running PHP forms with people clicking buttons every day.

## Extracted Concepts

- [Hold the Browser Environment Constant Across Runs](../concepts/hold-the-browser-environment-constant-across-runs.md) - a page that renders mobile on one run and desktop on the next makes agent results irreproducible, and the developer-machine workaround does not survive scale or compliance.
- [Pair Clicking With Generated Code and Replayed Network Requests](../concepts/pair-clicking-with-generated-code-and-replayed-network-requests.md) - the most reliable production browser agents write and run code alongside the browser instead of driving pixels for every step.
- [Publish Per-Site Skills So Agents Do Not Rediscover a Website](../concepts/publish-per-site-skills-so-agents-do-not-rediscover-a-website.md) - skills and memory let an agent know a site's available tasks before it visits, instead of re-exploring every run.
- [Agent Trust Needs a Certificate Issuer, Not a CAPTCHA](../concepts/agent-trust-needs-a-certificate-issuer-not-a-captcha.md) - the web's bot defenses cannot separate good agents from bad bots, and no one has taken the certificate-authority role.
- [Design an Agent-First Signup and Login Flow](../concepts/design-an-agent-first-signup-and-login-flow.md) - authentication, not capability, is the gate on enterprise computer use, and the three current paradigms all have costs.
- [Computer Use Diffuses AI Into the Form-Filling Economy](../concepts/computer-use-diffuses-ai-into-the-form-filling-economy.md) - the market is PHP forms in Singapore, South Africa, and Mexico, not San Francisco-native AI companies.

## Topic Links

- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)
- [Security](../topics/security.md)
- [Product Strategy](../topics/product-strategy.md)

## Notes

### Framing: the stalled computer-use track (00:13-01:00)

- Opens on the room: "very sleepy crowd in the computer use room. Have we all given up at this point?" The audience is people who "tried operator when it came out" and asked "why isn't this happening yet? This seems obvious."
- Target category: "the largest category of AI agents, the agents that actually go out and do work on your behalf in the real world."
- Thesis stated up front: "there's a huge model capabilities overhang in this category specifically, and you all here can hopefully solve it."

### Why the web resists agents (01:05-01:57)

- "The web wasn't built for agents. It was built for people."
- The concrete roadblocks: pages change; "the web was built in a very context inefficient way. It's a lot of text, a lot of tokens"; "you get a broken browser that doesn't spin up… pages that don't work… blockers or other sort of problems."
- Personal history: he started his career doing web automation, "maintaining these scripts every single day. It was very painful." Agents let him write *durable* web automation scripts — "but we still haven't gone to agents yet."

### It is no longer the models (01:59-03:13)

- "Until recently the bottleneck was the models. The models one year ago really weren't good at long context horizon tasks. But that's clearly been solved in a major way."
- Epistemic caveat he applies to himself: "anything I believe 6 months ago I have to revisit every single week because these models are progressing at an insanely fast pace."
- The training-investment argument: "in the last year a lot of investment was made in RL environments for coding. And in the last 6 months just as much investment has been made in RL environments for computer use." Mechanism: "when you train things on human trajectories in RL environments that model our real world, the real web, you can make better models."
- The diffusion argument, attributed to a speaker whose name the captions garble as "Docus" (unrecoverable — see Caption Artifacts): "if the models were good enough diffusion would just happen." Klein's read is that diffusion has not happened, so work remains.

### The harness is the missing piece (03:27-04:13)

- "I'd argue that agents are missing the right harness and tools." Definition given for the room: a harness is "the scaffolding and systems around your model that enable it to actually interact with the world."
- "I really think you can invest a lot in a harness and get a lot more out of the models and extract that overhang out of the models."
- Karpathy's November 2023 sketch of "systems around an LLM" is cited as the harness before the word existed, and its list has held: "a code interpreter for the LLM, audio and video input like screenshots, a browser, and other LLMs as subagents. All of these principles have held true."

### Harnesses that beat the baseline model (04:13-05:46)

- Evidence slide: Factory compared against Claude Code "using the same model but using their kind of custom harness."
- The claim: "when you build a harness optimized for the domain that your agent is operating in, it can actually achieve above model results in that domain. Harness engineering is a real thing."
- Attribution: "Cursor actually started this. Cursor was the first one that was doing… harness engineering on top of the original LLMs," and Browserbase's own work with browser models "has been harness engineering."
- The democratization point, stated twice: "building a good harness is an engineering problem. You don't have to be a lab to build a good harness… Your company can make a great harness for your domain and actually improve model results. You don't just have to wait for the models to catch up."
- Open question he explicitly declines to settle: "it's not clear yet if custom harnesses are going to beat out durable RL'd models… we're not going to debate that today."
- The operational rule that survives either answer: "you should still have some sort of harness on your model and measure the performance versus baseline model."

### The overhang, sized (05:46-07:01)

- Cites a tweet by (captions: "Brokman"; almost certainly Greg Brockman of OpenAI, given the Codex reference): "whenever I don't use Codex for a task, I ask myself why" — and it feels like the task is outside the model's capability. "The overhang is there. The actual work we can do is missing."
- The gap, measured loosely against coding: "when you look at the amount of task completion you can get with coding, it's so much higher than [CUA] because we haven't actually really pushed the models far enough and given it the right tools."
- Market framing: "non-coding is a much bigger opportunity than it is coding… It's a problem worth investing in, and the wrong answer is to sit around and just wait for the models to get better. You can actually solve this today. Solving overhang is an engineering problem."

### Property 1 — multimodal agents that also write code (07:01-07:59)

- "You no longer have to use a single model to actually interact with the task… Sometimes you'll use a smarter model for a more complex page. Sometimes a dumber model for a simpler page. And maybe you're using a combination of coding and computer use to actually power your agent."
- The insight he flags as important: "automating the web isn't always just clicking the button on the screen. It might be intercepting the network requests and writing a coding agent or having coding write a script to actually replay those network requests."
- Production observation: "the most reliable browser agents that we see in production right now are often writing code alongside using the browser to actually automate a task."
- Personal-automation analogue: "you might see Claude Code output a script more often than using Claude in Chrome because that's a very context-efficient way to automate a repeatable task." (Captions render both as "Cloud".)

### Property 2 — harness engineering: skills, memory, compression (07:59-08:54)

- "Doing these things repeatedly, you want to benefit from things like memory and skills."
- Browserbase shipped `browser.sh` (as spoken), "which actually publishes skills for websites. So before your agent even goes to the website, it can observe what types of tasks it can do."
- "WebMCP is very useful for this. It's part of pulling in existing knowledge to optimize a website. Your agent doesn't have to discover something in the first place if it's done it before. It can use its memory and its skills to actually make it better."
- Skills apply to CLI-driven control too: "if your agent is using CLIs to control websites like the Playwright CLI, you could actually give it skills and context to be more effective there."
- Token consequence: "if you're throwing everything on the page to a model, you're going to get sub-par results and it's going to cost you a lot. The right harness should not only present the right tools, but present an optimized amount of tokens that are compressed to get exactly the right repeatable result every single time."

### Property 3 — infrastructure that renders the same page every time (08:54-10:09)

- Requirement: "when you're running browser agents in production, you want an environment that's going to work everywhere, every time… computer use environments are pretty complex to scale up."
- The anti-pattern, named: when OpenClaw came out "everyone started buying Mac minis, which to me feels like an infrastructure problem, right? You're running [OpenClaw] on a Mac mini in your house because that's the best way to run macOS that you can SSH into and then end up solving the CAPTCHAs because of your home IP address."
- Why it does not generalize: "that is not something you can do when you're building thousands of agents for customers in production. I've yet to see a SOC 2 compliant Mac mini setup at scale, but please tell me afterwards if you found one."
- The consistency requirement, stated concretely: "when your agent is running across a website multiple times, you want it to see the same inputs and outputs, the same page layout, the same size. If your infrastructure renders a page in a mobile layout one time and then in a desktop layout the second time, it's going to have inconsistent results."
- Layering: "consistency in the infrastructure is the nice base layer on top of your harness and on top of your models."

### What the web owes agents — accessibility and WebMCP (10:09-11:25)

- Framed as the harder half: "we're not just engineering on our own systems anymore. We have to be evangelists to the web and to the broader world that, hey, you want agents to come to your website."
- Observation surface: "best-in-class browser agents… are not just consuming the raw DOM and HTML of the page anymore. They're looking at subsections of that like the accessibility tree, the ARIA tags. These are labeled components of a page that can help show your agent where it needs to click and why."
- WebMCP: "Chrome just added WebMCP… Websites can now publish MCP servers within their page that your agent can take advantage of without pre-installing the actual MCP. It can now issue tool calls to a website like submit the registration form in a way that's not only context-efficient, but is website approved and blessed."
- The broader file-convention trend: "we've seen things like `llms.txt`, `skills.md`, `agents.md` all being published alongside our websites. We need to see more of that to build the agent-first web."

### Authentication as the production gate (11:25-12:37)

- "I think authentication is actually an even bigger problem here… once your agent can actually go to a website, how can it log in on your behalf?"
- Three paradigms named: "maybe you're just giving your agent your password, but doing that securely can be very challenging"; "maybe you're creating a service account for your agent where it has some limited access and you constantly have to give it new permissions"; and human-in-the-loop approval — "doing that securely where you can have a human loop approve certain actions on a website is going to be a major challenge for unlocking computer[ use] for the enterprise."
- The gating claim: "the biggest gate to building agents that actually can work in prod is going to be the systems it has access to."
- Concrete development: "WorkOS just launched [captions: 'OffMD' — from context, an `auth.md`-style convention], which is a new way for your agent that goes to a website to find how to sign up on that website and get its own accounts."
- The advice to builders: "if you're building software now, you should think about what is my agent-first sign up and login flow look like because agents are going to be using your software whether you like it or not. It's best to let them use it securely."

### Trust: who certifies an agent (12:37-13:39)

- The classification problem: "the web was built to stop bad bots, but now there's good agents and bad bots. How do we delineate between the two?"
- "The CAPTCHA has been the tool in our tool chest for a very long time, but as we all know, CAPTCHAs are not as effective as we think against agents."
- Existing work: "there's been a lot of cool frameworks and work done on things like [captions: 'web bot off'; from context, Web Bot Auth] and in more authenticated ways to say this is my agent, it's coming from me, and you can follow me along on the web, but I still don't think we've solved the issue yet."
- The missing institution: "I think there needs to be almost like a Verisign moment for web agents where who can be the certificate issuer in saying my agent is trusted [and] this agent vendor is trusted? Nobody's come out and done that yet."

### What a platform has to provide (13:39-15:10)

- Summary claim: "building reliable browser agents is not a model problem. It's an engineering problem that all of us can solve, but doing that engineering is a full-time job."
- Four requirements for a browser-agent platform:
  - **Scalable infrastructure** — "you can want to run one agent, but also thousands of agents. And the challenge is that those different levels of scale is very very important."
  - **Model agnostic** — "as a developer, I don't want to be locked into a single model provider. As models continually change and get better, I want to be able to move my agent around."
  - **Agent identity** — "somebody who's going to go out and negotiate with the anti-bot providers of the world and say, we are the platform for trusted agents and we are the ones that can help broker the access for your agents as you use the web."
  - **Observability** — "you need to see where they're going and why and how… You need screen recordings, logs, network activity. And you need to feed that back into your agent so it can self-improve. Every agent you run should get better every single time."
- Browserbase published "Auto Browse" (as spoken) earlier in the year as "a really interesting way to see how is my agent able to improve itself over multiple loops," with observability data as the feed.

### The real economy (15:10-16:11)

- "My core belief with this company is that solving computer use accelerates the diffusion of AI to the real economy."
- "As much as I love our bubble here in San Francisco, the real economy is companies like the logistics company in Singapore, the bank in South Africa, or the lumber factory in Mexico. These people are built on PHP websites with forms and human beings clicking buttons every single day. That's a huge opportunity for you to go solve."

### Product note and close (16:11-18:00)

- Vendor content, recorded for context rather than as durable knowledge: Browserbase launched "BrowserBase agents" the day before the talk — a prompt-in, "battery-included" agent where the platform stands up "the harness, the runtime, the sandbox, the code execution, the fetch, the search tools, and the models." The pitch is composition: "pull it in as a sub-agent of your larger agentic system… You should be focusing your time on actually solving customer problems, not trying to rebuild the best-in-class browser agents."
- Close: "a lot of people have stepped back from computer[ use] because they've had so much challenges over the past year making browser agents work in production, but I can tell you first hand from our customers we see it working… the models are getting better, the techniques are getting better, and the tools are getting better. It's just on us to build better things."

### Caption Artifacts

- **"Open Cloud" → OpenClaw.** The auto-captions render it "Open Cloud" throughout; the video description names OpenClaw explicitly, and the description is treated as authoritative here.
- **"Brokman" → Greg Brockman (OpenAI), high confidence.** The quoted tweet is about Codex, an OpenAI product, and the caption "great Brokman tweet" is a plausible mis-transcription of "Greg Brockman tweet." Recorded with the reasoning rather than asserted silently.
- **"Docus" → unrecoverable.** The name attached to "if the models were good enough diffusion would just happen" is garbled beyond safe reconstruction and does not appear in the description. The claim is recorded; the attribution is not guessed.
- **"OffMD" → an `auth.md`-style convention from WorkOS, inferred from context.** Klein describes it as a way for an agent "to find how to sign up on that website and get its own accounts," which parallels `llms.txt` / `agents.md`. The exact name is not recoverable from the audio or the description, so the wiki records the described capability rather than the spelling.
- **"web bot off" → Web Bot Auth, inferred from context.** He pairs it with "more authenticated ways to say this is my agent," which matches signed-request agent-identity work. Recorded as an inference.
- **"area tags" → ARIA tags.** Unambiguous from the accessibility-tree context.
- **"Cloud code" / "Cloud in Chrome" → Claude Code / Claude in Chrome.**
- **"COA" → CUA (computer-use agents).** Spoken as an initialism in the coding-versus-computer-use comparison.
- **`browser.sh` and "Auto Browse"** are recorded as spoken; neither appears in the description, so no spelling correction is applied.
