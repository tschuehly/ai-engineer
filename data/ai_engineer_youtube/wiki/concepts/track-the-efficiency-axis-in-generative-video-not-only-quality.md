# Track the Efficiency Axis in Generative Video, Not Only Quality

Summary: Generative video improves along two axes, and the second one is where the product decisions now live: efficiency and generation horizon have moved far enough that a real-time model lands at roughly the *previous* year's frontier quality for about one-hundredth the cost. Keegan McCallum (uRun) argues the practical consequence is a change of unit — from dollars per clip to dollars per hour of continuous generation.

Use when:
- Deciding whether a generative-video feature is priced as content production or as an interaction surface.
- Choosing between a frontier video model and a distilled real-time one for a given product.
- Sanity-checking a budget for a feature where the user generates continuously rather than requesting single clips.
- Explaining why real-time generative media became buildable in 2026 without a quality breakthrough.

Details:
- The quality axis is the one everyone tracks, and McCallum compresses it to four beats before setting it aside: Will Smith eating spaghetti in 2023 ("nightmare fuel"), Sora in 2024 ("still has a bit of… an AI feel"), Sora 2, and Seedance this year, "absolutely incredible. So photorealistic" (00:25-01:05). The axis he cares about is "efficiency and… the long horizon generations" (01:05-01:16).
- The parity claim that makes the cheap axis usable: real-time generated clips are "about at the same quality as the frontier models were last year" (01:16-01:41). This is a one-year lag, not parity with today's frontier, and it is the honest way to state what the efficiency axis buys.
- The residual quality gap is specific rather than general. In a side-by-side against a generation that took minutes, the slow clip keeps a *motion* edge — "it's got better motion" — while the real-time path costs on the order of a hundred times less (02:03-02:28). If a use case depends on motion fidelity, the trade is not free.
- Price points to plan against: "$10 can get you 3 hours worth of generated video continuously with most of these models, and $50 would give you an entire day interacting with an AI in a visual medium. 15 hours" (03:34-03:52). He calibrates that against the audience's own habits, asking for a show of hands on burning $10-$50 of coding tokens in a single hour and getting "a lot of people" (03:23-03:34).
- The unit being replaced: the batch shape is "setting up a prompt and maybe some keyframes and spending about $10 a minute to try and get the shot that you want" (05:02-05:17). Per-minute-of-attempt versus per-hour-of-session is a ~100x difference in how a budget is written, which is the same order as the cost gap above.
- Supply side: "at least 40 models with real-time capabilities and long horizon generation capabilities released this year," and the enabling techniques are "being applied all over the place, not just the one model" (02:42-03:23). Efficiency here is a field-wide movement, not one vendor's optimization.
- A second vendor supplies an independent price anchor from the avatar side, and it is stated as a comparison rather than a rate. Sidney Primas (LemonSlice) reports that after making "the models small enough and efficient enough… the costs are about the same as a voice model," and flags it as the thing that surprised him: "which is crazy to me. Cuz think about a voice model, how much data is streamed there compared to a video model… it's much more pixel heavy… and the costs are about similar" (z1dqv74SpUs 13:59-14:29). Read carefully, the claim is about *price*, not COGS — in Q&A he restates it as "the same level as an audio model in terms of what we charge for it" (24:57-25:16) — but it is still the more useful planning number for a buyer, because it collapses a whole budgeting question: if the visual layer costs about what the voice layer costs, adding video to a voice product is not a new order of magnitude.
- The consequence Primas draws is a market one, matching McCallum's interface argument from a different direction: "this enables us to do consumer use cases. And a lot of our customers are consumer companies that basically use the video for consumer and entertainment applications" (14:29-14:43). He also names what cheaper compute buys next, which is not margin: "as the cost goes down we can do higher resolution which will help us a lot," attributed to "algorithm improvements and hardware improvements" plus a possible architectural shift "to more of a token approach instead of a diffusion approach" (25:16-26:00).
- Caveats to carry: this is a vendor talk with no benchmark table legible in the transcript; the ~100x figure comes from a single demoed side-by-side; the caption sentence attaching the cost figure is ambiguous and is read here per the index record's description; and quality parity is claimed against last year's frontier, so a product whose value depends on current-frontier fidelity is not covered by the argument.

Related topics:
- [Generative Media](../topics/generative-media.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Real-Time Generation Changes the Medium, Not Just the Latency](real-time-generation-changes-the-medium-not-the-latency.md)
- [Steer in Real Time, Then Render the Chosen Shot at Full Fidelity](steer-in-real-time-then-render-the-chosen-shot-at-full-fidelity.md)
- [Distill diffusion models to reduce sampling steps](distill-diffusion-models-to-reduce-sampling-steps.md)
- [Stack Additive Diffusion Optimizations for Real-Time Generation](stack-additive-diffusion-optimizations-for-real-time-generation.md)
- [Select State of the Art on a Quality-Efficiency Pareto Front](select-state-of-the-art-on-a-quality-efficiency-pareto-front.md)
- [Serve Real-Time Video as Stateful Streaming Sessions, Not Batch Jobs](serve-realtime-video-as-stateful-streaming-sessions.md)
- [Split an Embodied Conversational Agent Into an EQ Layer and an IQ Model](split-an-embodied-agent-into-an-eq-layer-and-an-iq-model.md) - the product shape that voice-parity pricing makes affordable.

Sources:
- [Generative Video at the Speed of Light — Keegan McCallum, uRun](../sources/20260818_Xln-On3syJk.md), 00:25-03:52, 05:02-05:17
- [Voice agents with Realtime Video — Sidney Primas, LemonSlice](../sources/20260818_z1dqv74SpUs.md), 13:59-14:43, 24:57-26:00
