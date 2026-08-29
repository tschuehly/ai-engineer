# Pre-Bake Transforms Too Heavy for the Real-Time Path

Summary: When a transform cannot meet a real-time budget, the alternative to making it faster is removing it from the live path: enumerate the control input's possible values offline, run the expensive transform once per value, and let the runtime do a lookup. Todd Fisher pitch-shifts VocalSet singing samples with WORLD ahead of time because "this is a very heavy process, and so I can't really do that live," then maps each fret to a finished sample.

Use when:
- A generation or DSP step blows a real-time budget and optimization (quantization, distillation, more GPUs) is not available or not worth it.
- The runtime control input has a small, discrete, enumerable domain — notes, frets, presets, poses, phrases, locales.
- Deciding what a feature's first shippable version should compute live versus bake at build time.

Details:
- The constraint and the response, stated together: pitch-shifting the sample set is "a very heavy process, and so I can't really do that live. I have to effectively pre-bake that. And then once it's already pre-baked, I could then go and jam out with it" (16:03-16:15).
- What makes the substitution legal is that the control surface is finite. The guitar produces a bounded set of notes, so the runtime step becomes "mapping each fret or each note on the guitar to one of those samples that are pre-baked" (17:28-17:35) — an index into precomputed results rather than a computation.
- Baking cost is the budget that replaces latency, and it is paid in coverage. Because the process is slow he "just started with the vowel sounds. So, there's somebody singing all each of the five vowels" (16:23-16:31), which is why the result is "kind of fun, kind of weird" and "not quite your opera singer" (16:41-17:17). The tradeoff is explicit: a real-time-capable system with a coarse output space instead of a rich one that cannot run.
- The upstream sources are ordinary offline assets — open-source singing recordings (VocalSet) transformed by the WORLD library (15:36-16:03) — which is what makes the offline stage cheap to build compared with training or serving a model that could do it live.
- This is the third distinct answer to a real-time budget in this wiki, and the cheapest one. Diffusion serving makes the generation itself shorter (quantization, caching, step distillation); real-time video platforms rebuild the serving topology around streams and nearby GPUs; pre-baking simply refuses to run the step at request time. Reach for it first when the input domain is enumerable, and note that it is unavailable exactly when it would help most — open-ended prompts have no finite key to bake against.
- Caveat: the source states the constraint qualitatively and never measures the transform's latency, the size of the baked set, or where the boundary would move on faster hardware.
- **The same shape in a data system: the expensive join is done on a batch cadence so the live path is a keyed lookup.** Notion computes "a small set of modeled, versioned entities" in Snowflake with "daily transforms and in some cases real time," then publishes "a denormalized, key-addressable profile that agents can quickly query in milliseconds with no joins." The enumerable-inputs trick from the audio case has a database counterpart — the key space is the entity set — and the same tradeoff applies: what is pre-baked is as stale as its refresh interval. ([Liu](../sources/20260826_L4I7WgiEquo.md), 09:11-09:49)

Related topics:
- [Inference](../topics/inference.md)
- [Generative Media](../topics/generative-media.md)

Related concepts:
- [Separate What Generated Audio Says From When It Plays](separate-what-generated-audio-says-from-when-it-plays.md)
- [Stack Additive Diffusion Optimizations for Real-Time Generation](stack-additive-diffusion-optimizations-for-real-time-generation.md)
- [Serve Real-Time Video as Stateful Streaming Sessions, Not Batch Jobs](serve-realtime-video-as-stateful-streaming-sessions.md)
- [Hit realtime latency with fast models, eager inference, and prefix caching](hit-realtime-latency-with-fast-models-eager-inference-and-prefix-caching.md)
- [Compute Truth in the Warehouse and Serve It as a Denormalized Profile](compute-truth-in-the-warehouse-and-serve-it-as-a-denormalized-profile.md)

Sources:
- [While my guitar gently speaks — Todd Fisher, Philo Ventures](../sources/20260818_E_Txocq-Lrw.md), 15:36-17:35
- [AI in GTM at Notion — Flora Liu](../sources/20260826_L4I7WgiEquo.md), 09:11-09:49
