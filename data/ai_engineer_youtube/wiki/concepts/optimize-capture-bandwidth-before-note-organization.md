# Optimize Capture Bandwidth Before Note Organization

Summary: In an agent-maintained knowledge base the human's only irreplaceable job is capture, so the human-side optimization is throughput, not tidiness — dictate rather than type, keep the raw note deliberately sloppy, and let a later agent pass impose every bit of structure.

Use when:
- Designing a personal or team knowledge base where agents will do the tagging, linking, and summarizing.
- Deciding whether to ask users to file, format, or template their notes at capture time.
- Diagnosing why a generated wiki, digest, or memory layer is thin — the usual cause is not enough raw material underneath it.

Details:
- The sequencing argument: because agents can now enrich, link, and synthesize, the scarce resource shifts to volume of raw input. "If you want to get to a point where you can actually have LLMs generate wikis, visualizations, etc., you need a lot of raw data. You need a lot of raw materials. So don't worry if you're being a little bit scrappy, a little bit rambly. You're not formatting things with perfect bullet points. That's fine. The goal should just be get down as many thoughts in the moment as possible." ([LLM Knowledge Bases](../sources/20260812_I3bpdgFJCUY.md), 05:01-05:35)
- Speech is the fastest human input channel and the talk treats that as decisive: "It's going to be like 200 words per minute, I believe, is the average. Unless you're an absolute Olympic typist, it will be faster than any other method that you have." The figure is the speaker's own hedge about average speech rate, not a measurement of his capture throughput. (03:08-03:29)
- The cost is social, not technical, and is named rather than dismissed: "it is pretty awkward to talk into your computer with a bunch of co-workers around." A phone-based capture path is what makes the pattern survive that. (03:10-04:25)
- Local on-device dictation removes the subscription barrier that keeps adoption low (a show of hands for Whisper Flow got "not enough hands"): Handy is "an open-source tool for voice dictation that just uses a local model, stays on device"; VoiceInk (captioned "Voice Inc.") is a ~$20 lifetime fee and provides a hotkey plus a mobile app, emitting punctuated sentences and paragraphs rather than a wall of words. (03:33-04:25)
- What counts as raw material is deliberately broad: a rambling dictation after a podcast, a meeting transcript, research notes taken after an important passage. The example note that later becomes a fully enriched wiki entry started as "just one long transcription I wrote down after listening to a podcast." (04:29-05:35)
- The independent convergence is worth noting: a separate solo-developer workflow reached the same conclusion from the opposite direction — voice-first dictation measured at ~184 wpm, adopted not for note-taking but because it is what lets one person drive several agent windows in parallel. Two different bottlenecks, same human-side fix. See [Drive agents remotely and by voice to decouple work from the desk](drive-agents-remotely-and-by-voice-to-decouple-work-from-the-desk.md).
- Caveat: nothing about capture quality is measured here. The claim is that sloppy-and-plentiful beats tidy-and-sparse *given* a working enrichment pass; it is not evidence that dictation errors, tangents, and missing structure are free downstream.

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Personal Knowledge Bases Become Agent Context Substrates](personal-knowledge-bases-become-agent-context-substrates.md)
- [Materialize Backlinks at Ingest With Key-Term Search](materialize-backlinks-at-ingest-with-key-term-search.md)
- [Generate an Entity Wiki Over Your Own Notes](generate-an-entity-wiki-over-your-own-notes.md)
- [Drive agents remotely and by voice to decouple work from the desk](drive-agents-remotely-and-by-voice-to-decouple-work-from-the-desk.md)
- [Use voice-dumped UI and code observations as agent feedback](use-voice-dumped-ui-and-code-observations-as-agent-feedback.md)

Sources:
- [LLM Knowledge Bases: a practical guide — Ben Holmes, Warp](../sources/20260812_I3bpdgFJCUY.md), 02:44-05:35
