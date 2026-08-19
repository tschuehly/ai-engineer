# Real-Time World-Model Evaluation Is Still Human Judgment

Summary: For real-time interactive video, per-frame fidelity is measurable but temporal and spatial consistency is not — as of this talk nobody, including the frontier labs, has a working automated eval for it, so teams watch the output. Treat that as a planning constraint: a product built on this model class cannot yet be regression-tested the way a batch generator can.

Use when:
- Planning an eval strategy for interactive video, generated worlds, or live avatars.
- Deciding how much of a real-time media roadmap can be gated on automated scores.
- Distinguishing which media-quality problems existing perceptual metrics actually cover.

Details:
- Asked how consistency is measured, Ahres answers that "you're asking a question that the entire research community in world models has not answered," and splits the problem: "fidelity is easy. It's just like pixels, right? But… evaluation for these real-time models is an unsolved problem" (16:27-16:49).
- The current method is stated plainly: "today it's literally just look at it and human judgment," and he explicitly includes the frontier labs — "this is including, by the way, DeepMind and everything. Nobody has solved this problem yet" (16:50-17:03). Reactor has a research team working on it (17:04-17:06).
- The concrete defect an eval would have to catch is a memory failure over a session rather than a bad frame: in Genie 3 demos "the character can look back and then will not remember what's going on" (12:45-12:56). That is a trajectory property, which is why the wiki's existing perceptual media metrics — computed per image or per clip — do not reach it.
- Deterministic rule-checking over the simulated world is the other obvious handle, and it is not something the platform does: asked about checking generations against deterministic rule sets, Ahres says "we don't do any of that today," notes developers build such layers on top and open-source them, and frames it as a prioritization consequence of the infrastructure work (15:35-16:24).
- Practical reading: for this model class, treat human review as the eval of record for consistency, keep automated scoring scoped to fidelity, and expect any consistency harness to be something you or the community build rather than adopt. The claim is a vendor's snapshot as of mid-2026, not a survey.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Generative Media](../topics/generative-media.md)

Related concepts:
- [Evaluate generative media with perceptual metrics](evaluate-generative-media-with-perceptual-metrics.md)
- [Personalize aesthetic evals with preference classifiers](personalize-aesthetic-evals-with-preference-classifiers.md)
- [Interactive world models need memory, control, and live prompting](interactive-world-models-need-memory-control-and-live-prompting.md)
- [Pick a Real-Time World-Model Class by What the User Steers](pick-a-realtime-world-model-class-by-what-the-user-steers.md)

Sources:
- [The Next Medium: Why Real-Time Interactive Video Changes Everything — Ahmed Ahres, Reactor](../sources/20260818_5dCAmSDOAjI.md), 12:45-12:56, 15:35-17:06
