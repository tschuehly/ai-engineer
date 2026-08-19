# Pick a Real-Time World-Model Class by What the User Steers

Summary: "World model" is used for several different products; Ahmed Ahres (Reactor) separates the real-time interactive video family into three classes by what the user actually controls — the scene through prompts, a character inside a generated world, or a speaking avatar — and reports very different maturity for each. The class decides the application shape, so pick it before picking a vendor model.

Use when:
- Scoping an interactive-video, simulation, or avatar feature and choosing which model family to build on.
- Reading "world model" claims from vendors and needing a discriminator that is not marketing.
- Judging what is buildable today versus what is still a research preview.

Details:
- Ahres explicitly narrows the term: world models are treated by some "from a Gaussian splatting standpoint," others from video, but his working definition is "real time interactive video" — infinite (not stopping at 5, 10, or 30 seconds), interactive (you can change what is on screen), and fast enough that "you don't need to wait to see what's going on" (00:39-00:52, 04:47-05:08).
- Class one — steerable infinite video: Veo/Sora-shaped generation made real-time and promptable mid-stream. The demo starts from an image of a dog and prompts a cat into the running scene; the extension he describes is an unfolding story ("the dog starts running, starts jumping, a dragon shows up"), i.e. the user steers the *scene* (04:47-05:41). Reactor's example is Helios, from ByteDance (11:06-11:15).
- Class two — controllable-character worlds: "the Genie 3 like from Google," conditioned on an image plus text, where the user controls a character inside the world (07:06-07:26). Its applications reach past games: mixed game/film experiences of the Netflix *Bandersnatch* kind (07:26-07:58), robotics training data because "you can control whatever you want to control in any environment… this creates a new opportunity to generate infinite amount of data for robotics," which he says a large number of robotics labs are already training on (08:00-08:25), and education, where a student can be placed inside a history lesson rather than reading a textbook or an LLM's answer (08:26-08:53). Reactor's example is captioned "Link bot," a Genie-3-like world model trained by Alibaba (11:15-11:20).
- Class three — live interactive avatars: the most familiar and the least ready. "It hasn't actually been cracked. They're still all kind of weird. If you speak to an avatar in any customer support or anything, it's still kind of off." He places these in research preview and expects the payoff when combined with classes one and two, targeting customer support, training, sales, gaming, and streaming (08:56-09:38).
- Two adjacent model shapes fill gaps the three classes leave: a multi-shot film model (captioned "Long live 2," from NVIDIA) where prompts are supplied in advance to hold a consistent story over time, and a video-to-video editing model (captioned "sound streaming," also attributed to NVIDIA) used to add visual effects, remove people, or replace backgrounds on footage generated elsewhere — Ahres names previsualization for film as the interesting case (11:20-11:50).
- What users actually ship on these, as reported: interactive livestreams where viewers type and vote on what happens next, medical simulation ("what if I put this medicine? What if I remove this medicine?") as a training playground, cooking simulation, and real-time video editing by prompt, click, or voice (10:06-11:00).
- Maturity caveats to carry: the video-editing products are "not very good yet just because of the quality of the models" (10:44-10:50), avatars are unsolved by his own account, and the demoed frame rate is 16 FPS (14:28-14:36). Several model names above are ASR-damaged in the captions and should be verified against vendor documentation before use.

- An independent enumeration from a second inference provider lands on the same families and adds a discriminator for class one. Keegan McCallum (uRun) lists "world models which can keep consistency over long horizons and you can control in a fine-grained way, the camera and the viewport"; "avatar models like we just talked about with LemonSlice"; and "video-to-video models that can transform what you're seeing in real time, almost like a magic mirror" (Xln-On3syJk 02:42-03:11). The camera-and-viewport phrasing is a sharper handle than "steer the scene": what the user moves is the observer, not the content. The video-to-video class is also the one with a live *input* stream — a webcam — rather than a prompt, which is a different serving shape (03:52-04:31).
- Provenance discrepancy worth carrying about Helios, since both sources name it: Ahres presents it as a model "from ByteDance," while McCallum, who serves it, says "Helios is a distill of [Wan] 2.1 14B" and that it "came out in March" (Xln-On3syJk 01:41-02:48). These are not necessarily in conflict — a distill can be produced by one party from another lab's open weights — but the two talks attribute the model differently, so check vendor documentation before repeating either lineage.

Related topics:
- [Generative Media](../topics/generative-media.md)
- [Models](../topics/models.md)

Related concepts:
- [Real-Time Generation Changes the Medium, Not Just the Latency](real-time-generation-changes-the-medium-not-the-latency.md)
- [Interactive world models need memory, control, and live prompting](interactive-world-models-need-memory-control-and-live-prompting.md)
- [Serve Real-Time Video as Stateful Streaming Sessions, Not Batch Jobs](serve-realtime-video-as-stateful-streaming-sessions.md)
- [Real-Time World-Model Evaluation Is Still Human Judgment](realtime-world-model-evaluation-is-still-human-judgment.md)
- [Robotics data pyramids combine scarce real trajectories with synthetic data](robotics-data-pyramids-combine-scarce-real-trajectories-with-synthetic-data.md)
- [Steer in Real Time, Then Render the Chosen Shot at Full Fidelity](steer-in-real-time-then-render-the-chosen-shot-at-full-fidelity.md)

Sources:
- [The Next Medium: Why Real-Time Interactive Video Changes Everything — Ahmed Ahres, Reactor](../sources/20260818_5dCAmSDOAjI.md), 00:39-00:52, 04:47-11:50, 14:28-14:36
- [Generative Video at the Speed of Light — Keegan McCallum, uRun](../sources/20260818_Xln-On3syJk.md), 01:41-04:31
