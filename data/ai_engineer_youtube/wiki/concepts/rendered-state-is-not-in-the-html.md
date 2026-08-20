# Rendered State Is Not in the HTML

Summary: A large amount of what a web page *shows* is never written down as text anywhere in the document. It arrives in a later asynchronous fetch, or it is computed by a script from a JSON value into a visual affordance like a grayed-out option. An agent that reads the DOM therefore reads a page that does not contain the answer, and the failure is silent — the extraction succeeds and returns the wrong thing.

Use when:
- A DOM- or HTML-based extractor returns empty, stale, or subtly wrong values on pages that look fine in a browser.
- Choosing the observation channel for a browser agent: raw DOM, accessibility tree, compressed page representation, or pixels.
- Deciding whether "have a coding agent parse the HTML" is a viable substitute for a computer-use model.

Details:
- **Failure one: the content has not arrived yet.** Asked for the final score of an NBA game, the page a human sees shows 125-109, but "when you actually load the page and read it… there's an empty placeholder initially, and you wait a few hundred milliseconds to a few seconds depending on your network connection, and your browser makes an asynchronous call later to fetch the information… If you just read the HTML when you load it, the answer is not in the HTML." Batra grants the obvious patch — "I just have to add some waits and sleeps" — and moves to the case where waiting does not help. ([Dhruv Batra](../sources/20260814_Ki980nV0__0.md), 09:01-10:14)
- **Failure two: the content was never text.** On a product page, three variants of a 25mm osmium cube are sold out and one is available, "even though it doesn't actually say in stock — like there's no text there that says in stock, but you understand that grayed out means sold out." The HTML confirms it: "there is an option selector. It actually doesn't say any of the things that I'm seeing on screen. It doesn't say sold out. It doesn't say available." The mechanism is a fetched JSON object holding a `quantity` (10 sometimes, zero sometimes) "and there's a different rendering script that anytime there's zero grays it out and makes it unclickable." (10:14-11:21)
- **The generalization.** "This information that you are seeing on screen is not written somewhere as pure text. It is calculated. It is rendered." (11:21-11:33)
- **Why this is structural rather than a bug to route around.** "The browser is a rendering engine. You are seeing pixels on screen. Think of it as a game engine." Recovering the display state from the source is then "an exact inversion of that process" — possible in principle, "well, yes, eventually," but not what a DOM reader is doing today. Batra flags that this is common knowledge in the browser industry and a blind spot for people arriving from AI: "people who are coming from an AI background like me, we didn't always understand this." (11:33-12:08)
- **The conclusion he draws, stated as a property of the artifact rather than of models.** "Fundamentally the web was built for human eyes. Pixels are the source of the truth because the consumers of the websites are humans… machines will need vision to operate those things." (12:08-12:24)
- **What this qualifies in the wiki's observation-channel material.** [A compact whole-page markdown representation](give-browser-agents-a-compact-whole-page-representation.md) and [accessibility-tree/ARIA reading](agent-readable-web-surfaces-guide-browsing-agents.md) are both cheaper than pixels and both derived from the document, so they inherit this failure exactly where it bites: an affordance conveyed only by styling (grayed, unclickable, struck through) has no token to compress. The accessibility tree is the partial exception worth checking per case, since `aria-disabled` and similar attributes sometimes do carry the state — but "sometimes" is the operative word, and nothing guarantees it on the long tail. Pair the cheap channel with a pixel check on the specific fact you are extracting rather than choosing one channel globally.
- **The same failure seen from a training lab.** Gaurav Mishra reports partial observability from both directions in real trajectories: "the DOM missed the ad text because it was baked into an image; the screenshot missed what needed scrolling" — see [Map RL Assumptions to Deployment Realities for Computer-Use Agents](map-rl-assumptions-to-deployment-realities-for-computer-use-agents.md). Neither channel is complete, which is why [multi-source reconciliation is trained as a perception primitive](train-screen-perception-primitives-beyond-coding-ability.md).
- **Operational corollary.** Because the DOM reader returns *something*, this is a silent-wrong-answer failure rather than an error, which puts it in the same class as [silent web-access failure producing confident hallucination](silent-web-access-failure-produces-confident-hallucination.md) and argues for [verifying through a channel other than the one that acted](verify-an-action-through-a-different-channel-than-the-one-that-acted.md).

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [The Long Tail of the Web Will Not Ship APIs](the-long-tail-of-the-web-will-not-ship-apis.md)
- [Give Browser Agents a Compact Whole-Page Representation](give-browser-agents-a-compact-whole-page-representation.md)
- [Verify an Action Through a Different Channel Than the One That Acted](verify-an-action-through-a-different-channel-than-the-one-that-acted.md)
- [Map RL Assumptions to Deployment Realities for Computer-Use Agents](map-rl-assumptions-to-deployment-realities-for-computer-use-agents.md)
- [Train Screen-Perception Primitives Beyond Coding Ability](train-screen-perception-primitives-beyond-coding-ability.md)
- [Let an Agent Build and Maintain Self-Healing Scrapers](let-agents-build-and-maintain-self-healing-scrapers.md)

Sources:
- [Computer-use models will agentify the web, not APIs — Dhruv Batra, Yutori](../sources/20260814_Ki980nV0__0.md), 08:33-12:24
