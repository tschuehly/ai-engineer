# Treat the Prompt as a Batch Protocol, Not a Conversation

Summary: Separate any AI interface into three parts — the *channel* (physical transport/bandwidth), *expression* (the range of meaning it is permitted to carry), and the *protocol* (the rules and shape of the exchange). LLMs exploded expression while leaving the protocol as batch: prompting is the same "assemble the whole turn, submit, wait, read, fix, resubmit" loop the punch card inherited from the weaving loom. Naming that protocol "prompt engineering" hides that it is just a set of rules for packaging a good batch deck, and shorter batch is still batch.

Use when:
- Diagnosing why a capable model still "feels like work" or unnatural to use, despite strong intelligence.
- Deciding whether the next product improvement is a better model/prompt or a change to the interaction protocol itself.
- Explaining why streaming updates, faster responses, or voice transcription do not make a prompt-based UX genuinely interactive.

Details:
- The three parts: channel = the transport (keyboard, microphone, screen, punch card, prompt box), which carries different signals (text = discrete symbols; voice = timing/pitch/hesitation; a diagram = spatial relations) but is "bandwidth, not the differences in meaning"; expression = how much of what you mean the interface lets through; protocol = the rules you follow and the shape of the interaction. 01:38-04:00, 05:43-06:20
- With AI the channel never changed ("you're still typing into a box, still hitting the submit button") — what changed is expression: from assembly opcodes → shell commands/flags → composable programming primitives → natural language, which "blew that menu open." Earlier steps forced you to "choose from a menu the machine will accept." 03:02-04:41, 05:03-05:50
- The protocol "is the part that hasn't kept up." Punch-card batch = encode the whole request in advance away from the machine, submit the deck, wait (sometimes overnight), read the printout, fix one thing, resubmit; "the machine never engaged with you while you were thinking." Batch itself came from the weaving loom (set the pattern, then run the cloth). 06:14-07:09, 09:36-09:56
- Prompting maps 1:1 onto that loop, and "interactive features" (progress updates, summaries) are "batch with interactive sprinkles"; shrinking the wait to seconds "fooled us into thinking that it become interactive. It hasn't. It's still batch. You still package a complete turn before the machine is allowed to participate." Voice doesn't change it — "your voice just gets transcribed into the box and submitted." 07:09-08:07
- "Prompt engineering" is a flattering label for rules to assemble a good batch deck (think step-by-step, give examples, act/don't act as an expert, paste more/less context, only talk in markdown — "we trade incantations, we've learned the magic words"); the mastery is the punch-card operator's "knowing exactly how to assemble the deck so the job wouldn't fail." That we got *good* at it "should bother us, not reassure us." 08:13-08:52
- Prompts, command lines, and punch cards were "brilliant solutions for constraints of their time" — the point is not that they are bad, but that batch may no longer be the right protocol now that the machine "no longer needs us to" pre-package intent: it can ask a follow-up, clarify mid-thought, and notice something missing. 08:52-09:36
- Failure mode: model capacity (reasoning, speech, vision, memory, planning) curves up while the protocol stays flat, so the human still carries the whole interface burden and, when it fails, blames themselves — "the mismatch isn't the user, it's the interface." Each historical step also "carried the old constraint forward" as a translation tax, precision tax, context tax, and repair tax. 10:10-11:06, 19:07-19:36

Related topics:
- [Product Strategy](../topics/product-strategy.md)
- [Voice Agents](../topics/voice-agents.md)

Related concepts:
- [Treat AI as an Interface Technology That Removes Human Burden](treat-ai-as-an-interface-technology-that-removes-human-burden.md)
- [Full-duplex speech models make turn-taking a learned behavior](full-duplex-speech-models-make-turn-taking-a-learned-behavior.md)
- [Engineer the Interaction, Not the Model, for Discernment](engineer-the-interaction-not-the-model-for-discernment.md)
- [Shrink the System Prompt and Drop Examples as Models Improve](shrink-the-system-prompt-and-drop-examples-as-models-improve.md)

Sources:
- [The Prompt Is Still a Punch Card - Ted Johnson, JoinIn AI](../sources/20260702_hVJOnuhFmTA.md), 01:38-11:06, 19:07-19:36
