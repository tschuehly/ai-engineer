# Compete on Glue and Distribution When Building on Managed APIs

Summary: When a product is assembled from managed, already-scalable APIs (voice, agents, auth), the prototype-to-production gap collapses — there's no hard technical problem left to solve and no way a single app dents the providers' API volume — so the durable engineering value and competitive differentiation shift to the integration glue and the distribution story, not to solving the hard problem the APIs already solved.

Use when:
- Deciding whether a viral or hackathon prototype can scale, and where the remaining work actually is.
- Scoping an AI product where the core capability is a third-party managed API.
- Reminding a team that "easy to prototype" no longer implies "owns a moat."

Details:
- The statue app stitched together existing APIs "designed to scale": OpenAI deep research, the ElevenLabs Voice Design API, and the ElevenLabs Agents platform, with a ~30-second end-to-end run built in two hours from one Cursor prompt — and it went from 50,000 to 1.5M impressions with no infra change. 02:38-03:45, 03:50-04:20
- Scaling is not the hard part because the heavy-lifting APIs are managed: "there's no way I can make a dent in the API volume even if this goes absolutely gangbusters," and the remaining surface (user management, logins, magic links) can itself be one-shot with Supabase. 05:55-06:20
- The thesis: "the glue pieces and telling a good story about the glue is in part the most important thing of the project rather than solving hard technical problems" — vibe coding is showing that the glue plus the narrative is the project. 06:20-06:50
- Distribution is the differentiator once tools are easy: "it's getting easier and easier to make tools … the main differentiator now is getting your word out there." 29:30-29:50
- The viral mechanic was the *story about the glue*, not the app: the first post got 50k, but the next-day repost framed as "I vibe coded this in two hours — not a brag, just this is interesting" hit 1.5M and drove inbound from museums, auction houses, and travel platforms (a museum CEO who'd had "a team of 10 working on this for a year" tracked down his WhatsApp). 03:50-04:40
- Caveat — managed APIs are a demo shortcut, not the production content layer: take-a-photo-and-get-web-research-back is explicitly *not* the long-term solution; production needs curators to design the narrative grounded in first-party data (museums treat their databases as core IP and expose public APIs, e.g. the V&A), so the glue layer must eventually call authoritative sources rather than ad-hoc deep research. 07:00-07:45
- **The provider's own account of where the room is, including the part that argues against you.** Krieger says he joined Anthropic partly because better models would "unlock a whole next generation of startups. Not because it was going to solve their ideation or their taste, but because it would make experimentation way simpler." His argument for why the lab does not take your market is structural rather than generous: a platform is "bound by the integrations that they already have and it's going to play to their strengths," leaving room "to be laser obsessed with your particular vertical... in a way that none of the labs are ever going to get to that level of understanding." The counterweight he supplies himself is the sharp one: "some of these things can be skillified and maybe don't need their own dedicated product." What survives is what this page already claims — "writing code was never the limiting part... it's really that space and user understanding." ([Krieger](../sources/20260827_qqrk7CtkuIw.md), 17:44-19:40)

Related topics:
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [AI Does Not Replace Shareable Product Marketing](ai-does-not-replace-shareable-product-marketing.md)
- [Build domain-specific workflow wrappers around models](build-domain-specific-workflow-wrappers-around-models.md)
- [Use hosted model playgrounds to prototype before owning infrastructure](use-hosted-model-playgrounds-to-prototype-before-owning-infrastructure.md)
- [Ask Size Lags Model Capability Because Early Products Boxed the Model In](ask-size-lags-model-capability-because-early-products-boxed-the-model-in.md)

Sources:
- [How to talk to statues — Joe Reeve, ElevenLabs](../sources/20260601_u-rJwPPU3QA.md), 02:38-04:40, 05:55-07:45, 29:30-29:50
- [How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 17:30-19:40
