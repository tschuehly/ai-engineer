# Climb a Humanness Ladder Only as High as the Page Forces

Summary: Web automation should escalate through graded levels of human-likeness — synthetic in-page action, then real browser-level input, then human-like motion and vision — stopping at the cheapest rung that actually works, and then recording the winning path as code or a skill so it is never rediscovered.

Use when:
- Building or debugging an agent that drives real websites and hits pages that ignore, block, or challenge automated input.
- Deciding how much fidelity a browser action needs, and resisting the urge to start at the most expensive technique.
- Turning a one-off manual exploration of a hostile page into a repeatable automation.

Details:
- **The premise underneath the ladder.** An agent driving Chrome through the Chrome DevTools Protocol is, at the input layer, "just like a meat bag with a mouse" — "your agent's clicks and keystrokes travel the exact same path inside Chrome that yours do," as far as Google, Cloudflare "and the rest can tell." Human-likeness is therefore an engineering choice about which path input takes, not a property of the model. ([Corey Gallon](../sources/20260814_26RtyAm9y_Q.md), 01:35-02:22)
- **The loop that runs on each rung.** Sense (read the page through one or more channels), act (do exactly one thing), verify (sense again through a *different* channel), and repeat "until the page gives in." When the loop will not close — you sensed, you acted, the page still will not do the thing — that is the page fighting back, and the signal to climb. See [Verify an Action Through a Different Channel Than the One That Acted](verify-an-action-through-a-different-channel-than-the-one-that-acted.md). ([Corey Gallon](../sources/20260814_26RtyAm9y_Q.md), 05:39-06:47)
- **Rung one — don't act human at all.** Use an API exposed inside the page, or issue a synthetic JavaScript click. "It's easy. It's free. It's instant. And it's the right default." A batch of personalized emails from the Outlook web client needs nothing more: the compose box "has nothing for us to defeat," so a synthetic click opens compose, fields are filled programmatically, a synthetic click sends, and the captured sequence loops "whether it's 20 emails or 200." ([Corey Gallon](../sources/20260814_26RtyAm9y_Q.md), 07:07-07:20, 08:48-09:57)
- **Rung two — real browser input.** When faking it stops working, issue a real click through the CDP input domain: "agent input that the page cannot tell apart from your own." This is the rung that defeats trusted/untrusted event checks — see [Chrome Stamps Every Input Trusted or Untrusted](chrome-stamps-every-input-trusted-or-untrusted.md). ([Corey Gallon](../sources/20260814_26RtyAm9y_Q.md), 07:20-07:34, 10:43-12:00)
- **Rung three — human behavior and human perception.** A real mouse path with dwell and jitter, plus vision to see and interpret what no selector can reach. Three worked examples, all at this rung: Cloudflare Turnstile hides its checkbox behind a closed shadow root inside a cross-origin iframe containing another shadow root, so there is "no element to grab" — the fix is to ask the browser where the iframe sits on screen, compute the checkbox position, and fire a trusted click at that spot on the glass. An image CAPTCHA is screenshotted, read with the agent's own vision, and answered with trusted keystrokes routed into the widget's iframe one character at a time. A drag-puzzle CAPTCHA samples "the mouse movement into a trail of points the whole way," so the drag eases in gently, curves, deliberately overshoots the target, and eases back in. ([Corey Gallon](../sources/20260814_26RtyAm9y_Q.md), 07:34-08:01, 12:41-16:30)
- **The stopping rule is the point.** "You climb only as high as the page forces you… climb to the lowest rung that actually works." Each rung costs more in latency, complexity, and fragility than the one below it, so starting at rung three is a real tax paid on pages that never needed it.
- **Explore by hand, then write it down.** "First, you explore, you run the loop by hand, you climb rungs until the thing actually works, and then you automate. You write the solution down so you never have to figure it out again… as code or as an agent skill or very often as both." This is what converts a hostile page from a per-run reasoning problem into a programmed sequence — the same capture-once-replay-forever move that makes a CLI cheaper than a model in the loop. ([Corey Gallon](../sources/20260814_26RtyAm9y_Q.md), 08:01-08:26)
- **Caveat — this is adversarial ground with terms-of-service and account risk attached.** Preparing this material got the speaker a ban threat from OpenAI "for cyber abuse with a web browser" (later rescinded), and every demonstration was restricted, on legal advice, to "infrastructure that I own and accounts that I operate." Techniques that defeat bot challenges sit against the defensive posture documented in [Treat CAPTCHA and Proof of Work as Economic Friction](treat-captcha-and-proof-of-work-as-economic-friction.md) and [Layer Bot Detection Signals Instead of Trusting One Header](layer-bot-detection-signals-instead-of-trusting-one-header.md); the transferable engineering is the escalation discipline, not the specific challenge bypasses. ([Corey Gallon](../sources/20260814_26RtyAm9y_Q.md), 00:01-01:09, 08:26-08:48, 19:36-20:22)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Security](../topics/security.md)

Related concepts:
- [Chrome Stamps Every Input Trusted or Untrusted](chrome-stamps-every-input-trusted-or-untrusted.md)
- [Verify an Action Through a Different Channel Than the One That Acted](verify-an-action-through-a-different-channel-than-the-one-that-acted.md)
- [Let Deterministic Code Drive the Timed Loop and Call the Model Only for Perception](let-code-drive-the-timed-loop-and-call-the-model-only-for-perception.md)
- [Use Browser UI Control When APIs Are Absent](use-browser-ui-control-when-apis-are-absent.md)
- [Fix the Browser-Agent Runtime Interface Before Reaching for a Better Model](fix-the-browser-agent-runtime-interface-before-reaching-for-a-better-model.md)
- [Skills Turn Procedural Feedback Into Transferable Agent Memory](skills-turn-procedural-feedback-into-transferable-agent-memory.md)

Sources:
- [The Dark Arts of Web Automation — Corey Gallon, Rexmore](../sources/20260814_26RtyAm9y_Q.md), 01:35-08:26, 08:48-16:30, 19:36-20:22
