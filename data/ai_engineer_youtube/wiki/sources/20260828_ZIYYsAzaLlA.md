# Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma

Source: [Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma](https://www.youtube.com/watch?v=ZIYYsAzaLlA)
Uploaded: 2026-08-28
Transcript: `raw/20260828_ZIYYsAzaLlA/ZIYYsAzaLlA.en-orig.vtt`

## Summary

Jesse Lumarie, a software engineer at Figma for three years, recounts building Figma's first MCP server from a Figma plug-in prototype he worked on one day a week — "kind of my 20% project that we didn't we didn't really have 20% projects, but I really wanted to work on it, so I did." Anthropic published the MCP spec in November 2024 and, outside Anthropic, nothing supported it: "OpenAI cursor VS Code they didn't support it yet." Access to the feature in Cursor was what turned the demo into something closer to a product. A few weeks into the build "a new version of the spec dropped uh deprecating the support type that we were going to use which was server events," and client support diverged from there — Claude Desktop had early support while Claude Code "wasn't really supported uh with all the complete set of features," OpenAI and VS Code had none until that spec update, and VS Code "didn't get to G until July." A client compatibility matrix from March 2025 was a maintained artifact, because "in many cases only tools were supported" and "it was hard to kind of understand what you were building towards."

The most transferable decisions are about representation. Figma's canvas is "represented as a scene graph in C++… a graph of connected nodes, not unlike the HTML DOM," and there were three candidate serializations: an internal JSX/XML-like representation that was "abstract and sparse, but it didn't have super rigorous fidelity"; D2R, "our like way of saying a react tailwind representation," which already existed because Figma Sites needed scene-graph-to-HTML conversion; and a plain image. They chose React and Tailwind on an explicit bet about pretraining exposure — "we had a hunch that this representation would be the best one because lots of the models were sort of [trained] on this React Tailwind type of code" — and the result is pixel perfect: paste the MCP output into a simple HTTP server and "it should be pixel perfect. Um and if it's not, file a bug." Images are hoisted out of the scene graph to the top level as links; the first attempt, "passing B 64 data into the code," "just blew up the context window and was bad all around. um don't do that." An image alone converted poorly, because "back in early 2025… agents weren't great at converting images directly to HTML or CSS," but "having the code context plus the image actually had better agentic output," so the screenshot is a supplement rather than the medium.

Pixel perfect turned out to be "only half the story." An enterprise "doesn't care if it's pixel perfect if it's not using its like battle tested accessible and internationalized components," and emitting markup has a second cost: "you'd eat up the context window." Figma already had Code Connect, which links design components to components in a codebase, so the server returns "effectively what is a pointer which allows the agent to use the code component," collapsing "this big old thing of uh react [tailwind]" into "the small react component that just says use button component" — higher fidelity and less context at once. Evaluation followed the same arc from manual to automated: a mix of quantitative checks (did it use variables, the expected theming, the right spacing) and qualitative ones (does it look good, "did it make good decisions with incomplete information"), graded once by hand — "we spent like two hours grading an eval into an Excel spreadsheet. And we said, we're never we're never doing that again. It was awful. Don't do eval by hand if you can help it." The eval corpus had to be built rather than collected, because "there's a lot of open source code out there but there's not a lot of uh open-source code that also has fig files attached." Today an eval "runs like hundreds of times a week," engineers kick it off to grade prompt changes with LLM judges, "so we kind of remove the human from the loop where we don't need it."

The rest of the talk is about building against clients that had not implemented the spec. Server instructions "was in the spec, but no clients implemented it… and it wasn't really highlighted in the docs until Anthropic added a nice blog post," so Figma pushed "additional instructions into each tool call. Basically instructing the LLM how to use our server." They now expose resources — how to use the server, plus Figma help articles — where previously that information came back "with like an [error]… and the agent would have to call uh wasting inference and sort of reasoning to sort of figure out what is actually going wrong." Elicitation and sampling were the two features they wanted most, to ask the user for permission to map their codebase and then have the agent scan it for Code Connect matches; "most of the clients didn't implement these features," sampling is now deprecated, and even where VS Code supported it "you could only really query it as a general agent not specific to the codebase" — the primitive existed but did not carry the context that made the workflow worth doing. Both were reimplemented through tool results: return a prompt asking the user's permission (mimicking elicitation), then a prompt telling the agent to scan the code and return matches "in a specified format… in bulk" (mimicking sampling). With no way to learn about the user's environment, they added optional query arguments to tools like `get design context` so the agent reports language and framework — "This is imperfect uh agents lie but it was at least a signal for us to understand like oh this type of user… may not have had a good experience. Perhaps our translation layer wasn't working as well." Shipping local first was the fastest path: the Figma desktop app is Electron running figma.com with an IPC bridge to a Node process that can reach the user's file system, so they exposed a server-events server in Node, relayed auth from the web app to the desktop app, and skipped OAuth entirely — the March 2025 spec added OAuth but before that "there wasn't this [auth] spec to to build from." Local also suited enterprises "because they kind of like the idea of our data not being sent anywhere." The remote server launched in September, both GA'd in October 2025, read and write capabilities followed, and the result was "one of the fastest growing products that they've ever had, which was not something we expected." The closing note is scale-setting: "we're so early… The MCP spec is only two years old."

## Provenance and Limits

- This is a first-party build retrospective by the engineer who started the project, presented at a conference, about a product his employer sells. The framing that the local-first architecture and the React/Tailwind representation were correct choices is not independently evaluated anywhere in the talk.
- There is exactly one outcome number and it is unquantified: "one of the fastest growing products that they've ever had." No adoption figure, retention figure, revenue figure, or growth rate is given, and no comparison product is named.
- No eval result is reported. The talk says an eval exists, that it mixes quantitative and qualitative criteria, that it runs "hundreds of times a week," and that LLM judges grade it — but no score, no pass rate, no before/after on any representation choice. The claim that React/Tailwind beat the internal representation is stated as a hunch that was borne out, with the eval named as the instrument but no numbers shown.
- "Pixel perfect" is asserted as an invariant with a bug-report escalation attached ("if it's not, file a bug"), not measured. No fidelity metric, tolerance, or sample is given.
- The pretraining-exposure argument ("lots of the models were sort of [trained] on this React Tailwind type of code") is a stated hunch about training corpora, not evidence. Figma has no visibility into any lab's training mix, and the talk does not claim otherwise.
- The image findings are dated by the speaker himself to "early 2025." He explicitly scopes the weakness of image-only conversion to agents of that period, so the code-plus-image pairing is reported as a finding of its time, not a durable model property.
- Client-support facts are a snapshot: the compatibility matrix shown is "from March 2025," sampling's deprecation and the SSE deprecation are protocol-version-specific, and the talk's own closing point is that the spec is two years old and moving.
- Two segments are lost to a technical failure during the talk. Slides stopped advancing around 08:40-08:55 ("it's going to let you restart it… pause that"), and the speaker narrates from memory across the gap, so the Code Connect walkthrough is thinner than it was designed to be.
- The Make product mention is flagged by the speaker as "only slightly self-serving," which is accurate: it is a Figma product pitch used to set up the closing point about how early the field is.

## Extracted Concepts

- [Pick the Serialization the Models Have Seen Most, Not the One Native to Your System](../concepts/pick-the-serialization-the-models-have-seen-most.md) - Figma had three text serializations of its own scene graph and chose the one with the most pretraining mass over its own internal format.
- [Return a Pointer to the Reader's Own Component Instead of a Faithful Copy](../concepts/return-a-pointer-to-the-readers-own-component-instead-of-a-copy.md) - Code Connect turns generated markup into `use button component`, raising fidelity and cutting context in the same move.
- [Tools Are the Only Primitive Every Client Implements](../concepts/tools-are-the-only-primitive-every-client-implements.md) - server instructions, elicitation, and sampling were all reimplemented as tool results because clients had not built them.
- [Optional Self-Reported Tool Arguments Are Segmentation Signal, Not Ground Truth](../concepts/optional-self-reported-tool-arguments-are-segmentation-signal.md) - "agents lie, but it was at least a signal" — an argument added to the schema purely to be logged.
- [An Installed Desktop App Is an Auth and Filesystem Beachhead](../concepts/an-installed-desktop-app-is-an-auth-and-filesystem-beachhead.md) - Electron plus an IPC bridge let Figma ship an MCP server before the protocol had an auth story.

## Topic Links

- [Tools](../topics/tools.md)
- [Context Engineering](../topics/context-engineering.md)
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)

## Notes

- 00:20-00:37 What the server is for: "a way for you to send context between production uh code and design and vice versa. AI tools don't need to build a dedicated integration."
- 00:39-00:55 Timeline: Anthropic released the MCP spec November 2024; "outside of anthropic none of the other AI agents or labs were really using it. So OpenAI cursor VS Code they didn't support it yet."
- 00:59-01:08 Access to the feature in Cursor is what let them "ideate and understand what it was capable of" and get "something a little bit closer to an actual product."
- 01:10-01:29 Origin: working on growth initiatives, saw an internal demo, wanted non-designers to use Figma, built a Figma plug-in based MCP server one day a week. "It was kind of my 20% project that we didn't we didn't really have 20% projects, but I really wanted to work on it, so I did."
- 01:30-01:44 Credit disclaimer: "I'm going to say I a lot and we there was a big team behind this so it's not just me."
- 01:46-01:56 "A few weeks later after we started getting our initial architecture sorted a new version of the spec dropped uh deprecating the support type that we were going to use which was server events."
- 01:58-02:11 Uneven client support: "cloud had early support cloud desktop but cloud code you was wasn't really supported uh with all the complete set of features. OpenAI and VS Code didn't have support until that spec update."
- 02:13-02:26 "VS Code didn't get to G until July. It didn't mean that all the features were implemented either… in many cases only tools were supported."
- 02:26-02:37 "VS Code was truly like the golden client… they eventually supported kind of all pieces of the spec, but it was hard to kind of understand what you were building towards because clients supported so many different things."
- 02:50-03:05 Local server launched "about a year ago"; local "was heavily designed for developer use cases. You kind of had to know what you were doing a little bit."
- 03:00-03:12 Why developers first: "they were the first to adopt AI workflows. they would use a single… prompt like help me implement this and a developer could pull everything that they would normally get from Figma's dev mode into their coding agent."
- 03:14-03:31 What came through: "component data, spacing, variables"; then more read tools "for fig jam for make um etc.," sharing the goal "to make Figma context available for… developers wherever they are."
- 03:33-03:44 "Figma is a canvas… represented as a scene graph in C++. It's a graph of connected nodes, not unlike the HTML DOM."
- 03:47-03:59 Option one, the internal representation: "kind of akin to JSX or XML, effectively converting the scene graph into JS[X] tags and XML tags and passing those to the agent. It was abstract and sparse, but it didn't have super rigorous fidelity."
- 04:02-04:16 Option two: "D2R which is our like way of saying a react tailwind representation. Uh and the reason we had this is Figma has a sites product and so we already had a way of basically converting the scene graph into HTML."
- 04:18-04:28 The fidelity claim: "If you actually copy the output of the Figma MCP today and you paste into like a simple MCP or simple HTTP server, it should be pixel perfect. Um and if it's not, file a bug."
- 04:30-04:40 The bet: "we had a hunch that this representation would be the best one because lots of the models were sort of [trained] on this React Tailwind type of code… we had a suspicion that it would work really well."
- 04:41-04:54 Option three, the plain image: "back in early 2025… agents weren't great at converting images directly to HTML or CSS or sort of other languages. And so we kind of use that as an additional piece of context, not as the sole one."
- 05:09-05:17 Images are abstracted out of the scene graph and hoisted "at the top level" as links.
- 05:17-05:24 "Our first attempt was just passing B 64 data into the code and that was just a terrible idea. It it just blew up the context window and was bad all around. um don't do that."
- 05:27-05:39 The pairing result: "While the image by itself did not do a good job of converting to uh code, having the code context plus the image actually had better agentic output."
- 05:44-05:59 Eval criteria, quantitative: "did it use variables? Uh, did it use the theming we expected? Did it use the right sp[acing]?"
- 05:59-06:05 Eval criteria, qualitative: "does it look good? Did it make good decisions with incomplete information?"
- 06:05-06:13 "And we spent like two hours grading an eval into an Excel spreadsheet. And we said, we're never we're never doing that again. It was awful. Don't do eval by hand if you can help it."
- 06:13-06:28 Corpus and harness: "we had a bunch of toy repos that we kind of created or kind of had folks create for us… we eventually ended up coding up a web app to sort of help us with the eval which made things a lot easier at least from like a… process perspective."
- 06:28-06:45 The dataset problem: "there's a lot of open source code out there but there's not a lot of uh open-source code that also has fig files attached and so we had to either create our own or sort of find different ways to make automated systems."
- 06:45-06:58 Where it landed: an eval "that sort of runs like hundreds of times a week. Engineers can kick this off and sort of grade against prompt changes um, with LLM judges. So, we kind of remove the human from the loop where we don't need it."
- 06:58-07:10 "But having an agent translate a pixel uh, perfect version of code isn't enough… That's really only half the story."
- 07:10-07:17 "An enterprise doesn't care if it's pixel perfect if it's not using its like battle tested accessible and internationalized components."
- 07:17-07:28 Code Connect "allows you to link design components to components in your codebase. We needed a way to use this with our MCP server so that an agent used the correct components."
- 07:36-07:50 The two problems with emitting markup: "if you had a primary button in your codebase, you wouldn't be referencing it. And that's not ideal if it has accessibility properties or internationalization properties. And then second… you'd eat up the context window."
- 07:52-08:03 "we use React Tailwind to basically convert things over… but we want to make sure we do it in the sparest way possible."
- 08:12-08:30 "It's going to then be converted into sending over… basically a sparse representation of it via code connect… by connecting the user's code to the design, we're able to pass back effectively what is a pointer which allows the agent to use the code component leading to our higher fidelity implementation."
- 08:30-08:37 The compression: "you go from like this big old thing of uh react [tailwind] to the small react component that just says use button component."
- 08:40-08:55 Slides stop advancing; the speaker narrates from memory across the gap.
- 09:06-09:23 "once we felt good about the serialization syntax, we started to look at what an MC[P] server can be. And the MCP spec had a lot of great pieces in it, but some features weren't quite fleshed out within clients, and other features we really wish existed. Many clients only implemented a subset of the spec, and many features were very experimental."
- 09:24-09:28 "This is the client compatibility matrix from March 2025."
- 09:28-09:47 Resources instead of errors: "we expose a host of resources to an agent so that it can figure out how to use our server as well as different help articles within Figma. Um whereas before we would send that information down with like an [error]… and the agent would have to call uh wasting inference and sort of reasoning to sort of figure out what is actually going wrong."
- 09:48-10:02 Server instructions: "it was in the spec, but no clients implemented it. Um, and it wasn't really highlighted in the docs until Anthropic added a nice blog post uh to sort of talk about it and then some clients started adding it."
- 10:02-10:14 The workaround: "we would add uh additional instructions into each tool call. Basically instructing the LLM how to use our server um even though server descriptions weren't necessarily written out yet."
- 10:16-10:27 "Some other features that we really really wanted were elicitation and sampling… elicitation… is a way for you to ask the user a question, take that input, and pass it back to your server."
- 10:40-10:44 "sampling, which is unfortunately deprecated, but it's fine because you're able to work around it."
- 10:44-10:53 "Sampling is a way of having a server query the client's LLM from our server and in kind of the canonical case was for small queries."
- 10:55-11:16 The intended workflow: "ask a user can we map out your code base for code connections so that our MCP server can link them so that the output would be better and reduce the amount of context we send."
- 11:16-11:22 "Unfortunately though most of the clients didn't implement these features and didn't allow you to properly query the agent in the context of the codebase."
- 11:23-11:33 The deeper defect: "for sampling even when VS code supported it you could only really query it as a general agent not specific to the codebase. But we were able to kind of hack around it using tools."
- 11:33-11:48 Mimicking elicitation: "if we noticed it was a component and that it wasn't code connected, we'd send down a prompt to ask the user if they'd want to map the unlink[ed] component… Kind of mimicking elicitation."
- 11:49-12:03 Mimicking sampling: "If the user said yes, we'd send down another prompt to have the agent scan the code for potential matches, mimicking sampling. We then [surface] them in a specified format or ask the agent to do so and then have them send it back in bulk to make a bunch of code connections."
- 12:04-12:13 Tooling recommendation: "the screenshot on the right is the MCP inspector and if you haven't used it and you're developing an MCP server, you're doing yourself a disservice. It's a really great tool and it's open source."
- 12:15-12:25 "the magic in our case was combining these two features because we could ask the user for permission. we can have the agent give us those suggestions and we can map them and in the end the users got a better experience."
- 12:29-12:45 Why they needed environment signal: "we didn't know if the react tailwind code would be successful for other types of code bases… outside of the elicitation and sampling which didn't really work as we wanted there was no way of getting that information from the user."
- 12:45-12:53 "So we added some optional query arguments to our tool calls for ones like get design context where they would send back what sort of language what sort of framework the user might be using."
- 12:53-13:09 "This is imperfect uh agents lie but it was at least a signal for us to understand like oh this type of user… may not have had a good experience. Perhaps our translation layer wasn't working as well. We have found that that works pretty well but this was kind of our way of verifying that."
- 13:13-13:28 Four beta requirements: "we wanted to launch quickly. Um we wanted to have the highest possible bar for our security. We wanted to respect file permissions. And we wanted to respect our pricing [and] packaging so we didn't have abuse vectors."
- 13:28-13:41 "after the spec changed and introduced O[Auth] in March 2025, we had to decide whether to keep our MCP server local or sort of switch to the new remote server using streamable HTTP and kind of like work on all the [auth] problems."
- 13:41-13:49 "we punted so until [then] there wasn't this [auth] spec to to build from and we could easily relay [auth] from our web app to our desktop app."
- 13:49-14:12 The architecture: "the Figma desktop app is Electron and so the front end of it is a web app and we basically just run figma.com in that and then we have an IPC bridge between the two and that sends it to our node process that allows us to talk to the user's file system. Um we then sort of expose a server events server in node and that way clients could talk directly locally."
- 14:12-14:18 "The local story was also really great with enterprises because they kind of like the idea of our data not being sent anywhere."
- 14:18-14:25 "this architecture was our fastest path to getting something into the hands of users to understand product market fit and what kind of tools and use cases folks had."
- 14:28-14:44 Internal launch: "the reception was extremely honest… but we worked out a lot of the kinks and we started to get some really positive feedback in the community."
- 14:47-15:07 "we immediately started working on the remote server as soon as we launched… In September we launched the remote server. We G[A]'d both servers in October 2025."
- 15:07-15:18 "then we started adding read and write capabilities and kind of all these things combined ended up making for Figma one of the fastest growing products that they've ever had, which was not something we expected when we started working on this."
- 15:19-15:45 Adjacent product: research showed "designers really wanted to shift to writing production code in certain cases," which became "make in your local codebase… Figma's agent solution for working on GitHub and local code bases." Flagged by the speaker as "only slightly self-serving."
- 15:49-16:02 Closing point one: "if there's one thing you want to take away from this talk it's that we're so early… The MCP spec is only two years old and we're still figuring out the best way to do things."
- 16:02-16:20 Closing point two: "Figma's done a great job of letting engineers build and figure out what's next and letting them run with it. I wasn't staffed on MCP. I wasn't staffed on our make product, but I ended up helping them be built um, just because I was kind of given the leeway to do so."

## Caption Artifacts

The auto-generated captions garble several proper nouns and protocol terms. Resolutions used above, with the raw caption text in parentheses:

- "cloud" / "cloud desktop" / "cloud code" -> Claude / Claude Desktop / Claude Code (repeated).
- "MCB server" / "MC MCP" -> MCP server (repeated stutter).
- "didn't get to G until July" / "We ged both servers" -> GA'd (general availability).
- "OOTH" / "all the off problems" / "relay off from our web app" / "this offspec to build from" -> OAuth / auth (repeated).
- "server events" -> server-sent events (SSE), the transport deprecated by the spec revision.
- "JSS tags" -> JSX tags.
- "rldled on this React Tailwind" -> trained (or "world-modeled"); the intended sense is that models saw a lot of React/Tailwind in pretraining.
- "passing B 64 data" -> base64.
- "the image can crew meetup uh link" -> an image link in the sample output; the exact asset name is not recoverable.
- "did it use the right spot?" -> the right spacing (the preceding tool output list is component data, spacing, variables).
- "react tailin" / "react tailwin" -> React Tailwind.
- "the sparest way possible" -> sparsest.
- "we then service them in a specified format" -> surface them.
- "unlink component component" -> unlinked component.
- "we punted so until HMR there wasn't this offspec" -> the "HMR" token is unrecoverable; from context it stands for the March 2025 spec revision that introduced OAuth.
- "this felt user may not have had a good experience" -> unrecoverable; from context, a user in a particular language/framework segment.
- "a single plop prompt" -> a single prompt.
- "highle re recap" -> high-level recap.
