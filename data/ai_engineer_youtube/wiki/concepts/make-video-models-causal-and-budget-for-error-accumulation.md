# Make a Video Model Interactive With a Causal Attention Mask, Then Budget for Error Accumulation

Summary: A batch video model attends bidirectionally over all its latents, which is impossible for an interactive one because the future inputs — the next second of user audio — do not exist yet. Sidney Primas (LemonSlice) makes the model causal by training with an attention mask that forbids attending forward, so the inference condition is the training condition. The price is structural rather than incidental: every block conditions on blocks that already contain error, so error compounds for as long as the session runs, and for a live avatar the session is hours.

Use when:
- Converting a batch video, world-model, or avatar generator into a streaming interactive one.
- Diagnosing quality that degrades over the length of a generated session rather than being bad from the first frame.
- Sizing the engineering risk of a real-time media feature whose sessions are long-lived.
- Deciding what a real-time generative session actually needs to be evaluated on.

Details:
- The property being removed, stated precisely: "usually video models are bidirectional, so they can look into the past, but they actually also can look into the future… and they basically generate videos all at the same time by looking at all of the latents that are being generated. For us, you can't do that. You only can look into the past" (10:17-10:41).
- The fix is applied at training time, not by masking at inference: "we basically train a model with an attention mask so that the model can only look into the past. So, when you do inference, it never can see the future because the future doesn't exist because you haven't given it those inputs yet. So, for example, it doesn't see audio in the future, it only sees what has been said in the past" (10:43-11:07). The reason this belongs in training is that a model trained bidirectionally and then masked at inference would be run outside its training distribution on every step; enforcing the constraint during training makes the two match.
- Real-time is a separate conversion stacked on top: "usually you spend like a bunch of steps denoising these video models. So, like let's say 30 steps… what we need to do is go from like 30 steps, bring it out to one step" (11:11-11:44). Causal masking buys interactivity; step reduction buys the frame budget. Both are needed and they are independent.
- The cost of causality, and why it is not a bug to be fixed: "since you only can look backwards, you're looking actually backwards at videos that you've previously generated, but each video block you generate has some error in it. So now you're looking in the past, you're looking at the error, you're adding more error to it, and then the error compounds over time" (12:08-12:40). Primas calls this error accumulation and describes it as familiar to "anybody in real-time video generation and world models" (11:46-12:04). The generating mechanism is the same one that makes the model interactive, which is why it cannot simply be trained away.
- The horizon that turns it from a nuisance into the hard problem: "ideally these video models are endless. Like the Teddy avatar is generating continuously non-stop frame by frame for 8 hours straight with like no reset throughout the entire process. We have another one that's going to be generating for 16 hours straight" (12:40-13:02). Note the design consequence: a batch model's 5-30 second horizon means drift never has time to show, so a technique validated on clip-length generation says nothing about a session-length one. Plan the mitigation against the longest session you intend to sell, not against the demo.
- Mitigation is claimed but undisclosed. LemonSlice says it "came up with a new way to solve this problem that is different to the best of our knowledge than what everybody else does today," declines to describe it, and claims long videos with "no noticeable error accumulation" (13:05-13:27). Treat the existence of a solution as a vendor claim and the problem statement as the transferable part.
- This is exactly the defect class that has no automated eval. Ahmed Ahres (Reactor) reports that per-frame "fidelity is easy. It's just like pixels," while consistency across a steered session is unsolved "including, by the way, DeepMind and everything" (5dCAmSDOAjI 16:27-17:03). Error accumulation is a trajectory property, so the perceptual metrics this wiki catalogues — computed per image or per clip — will score a drifting 8-hour session as fine. If you ship a causal streaming model, you are shipping a failure mode your metrics cannot see and your demo is too short to reveal.
- Forward-looking caveat on the architecture: Primas expects "very cool architectural updates to move to more of a token approach instead of a diffusion approach that will make this type of video generation way cheaper" (25:29-26:00). He offers no claim about what that would do to error accumulation, so the causal-drift analysis here is tied to the diffusion formulation he describes.

Related topics:
- [Generative Media](../topics/generative-media.md)
- [Models](../topics/models.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Distill diffusion models to reduce sampling steps](distill-diffusion-models-to-reduce-sampling-steps.md) - the other half of the real-time conversion, and the source of the single-step constraint this page's model runs under.
- [Serve Real-Time Video as Stateful Streaming Sessions, Not Batch Jobs](serve-realtime-video-as-stateful-streaming-sessions.md) - the serving shape a long causal session forces.
- [Real-Time World-Model Evaluation Is Still Human Judgment](realtime-world-model-evaluation-is-still-human-judgment.md) - why this failure mode escapes automated scoring.
- [Interactive world models need memory, control, and live prompting](interactive-world-models-need-memory-control-and-live-prompting.md) - the adjacent long-session failure, where the model forgets rather than drifts.
- [Pick a Real-Time World-Model Class by What the User Steers](pick-a-realtime-world-model-class-by-what-the-user-steers.md) - which class of interactive video you are building, which decides how long a session runs.
- [The Real-Time Model Harness Is Where the Product Work Sits](the-realtime-model-harness-is-where-the-product-work-sits.md) - the orchestration layer that keeps the causal stream running without stutter.

Sources:
- [Voice agents with Realtime Video — Sidney Primas, LemonSlice](../sources/20260818_z1dqv74SpUs.md), 10:17-13:27, 25:29-26:00
- [The Next Medium: Why Real-Time Interactive Video Changes Everything — Ahmed Ahres, Reactor](../sources/20260818_5dCAmSDOAjI.md), 16:27-17:03
