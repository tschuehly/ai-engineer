# Ship AI Audio Features as Plugins Inside the Host DAW

Summary: An AI audio feature does not need its own application. Building it as a DAW plugin — Todd Fisher used JUCE and dropped the result into Logic Pro "just like any other plugin… where you just plop it in there" — inherits the host's audio graph, transport, effect chaining, and the user's existing workflow, so the build reduces to the signal processing that is actually new.

Use when:
- Adding generation, transcription, or transformation to a workflow that already has a dominant host application (a DAW, an editor, an IDE).
- Deciding whether an AI media feature should be a standalone app, a service, or an in-host extension.
- Scoping a first version of an audio feature and looking for what not to build.

Details:
- The framing that makes the choice obvious: "your DAW is effectively your IDE but for musicians and music producers" (06:13-06:19). The users of an audio feature already live in Pro Tools, Logic, or Fruity Loops, and the last two decades of the guitar's own toolchain moved pedals into that host as software emulation, "even to the point where all the effects are in software now" (03:36-03:48).
- JUCE is named as the framework for this — "really awesome for anyone building audio software" — alongside the several plugin formats a DAW can load (05:59-06:13). The source does not compare formats or discuss cross-format packaging.
- What the host supplies for free is the point: the plugin is "just, you know, chaining all the effects together" with everything else in the session (06:56-07:01), so live input, routing, monitoring, the backing track, and mixing are the host's problem. The demo jams a speaking guitar over a recorded chord track without the project owning playback at all (12:31-13:32).
- The plugin still owns its own controls where the model output needs shaping — a "clarity" lever mixes the synthesized note against the generated voice (13:38-13:47), and a manual segment editor lets the user drag word boundaries (09:26-09:37). In-host delivery does not mean an empty UI; it means the UI is only the new decisions.
- Caveat from the same demo: hosting inside someone else's real-time audio thread is not free. The talk hits repeated stage failures ("technical difficulties… Live demos always the best," 12:44-13:19), and the heavier parts of the pipeline had to be moved off the live path entirely.
- The same shape appears elsewhere in this wiki as agent-side plugin surfaces, but the motive differs: there, plugins let a system absorb experiments; here, the plugin is a *distribution* decision that puts an AI feature inside the tool where the work already happens.

Related topics:
- [Tools](../topics/tools.md)
- [Generative Media](../topics/generative-media.md)

Related concepts:
- [Separate What Generated Audio Says From When It Plays](separate-what-generated-audio-says-from-when-it-plays.md)
- [Pre-Bake Transforms Too Heavy for the Real-Time Path](pre-bake-transforms-too-heavy-for-the-realtime-path.md)
- [Plugin architectures let agent systems absorb experiments](plugin-architectures-let-agent-systems-absorb-experiments.md)
- [Orchestrate Generative Media From a Real-Time Voice Agent via Tool Use](orchestrate-generative-media-from-a-realtime-voice-agent.md)

Sources:
- [While my guitar gently speaks — Todd Fisher, Philo Ventures](../sources/20260818_E_Txocq-Lrw.md), 03:36-03:48, 05:59-07:01, 09:26-09:37, 12:31-13:47
