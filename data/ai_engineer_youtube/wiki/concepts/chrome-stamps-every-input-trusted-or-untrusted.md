# Chrome Stamps Every Input Trusted or Untrusted

Summary: Chrome marks every input event with whether it originated from real user input, and pages that check the flag drop synthetic JavaScript events silently — no error, no exception, nothing happens. Driving input through the browser's own input path (CDP's input domain) produces trusted events the page cannot distinguish from a physical mouse or keyboard.

Use when:
- A browser automation click or keystroke "works" in code but the page does not respond, and there is no error to debug.
- The same synthetic-click technique succeeds on one site and does nothing on another.
- Choosing between page-level scripted actions and browser-level input for an agent's action space.

Details:
- **The failure mode is silence, which is why it burns time.** The same JavaScript click that opens and sends mail in the Outlook web client, pointed at a mega-retailer's add-to-cart button, gives "literally nothing. There's no failure, there's no error, just nothing happens, and the page is ignoring it." ([Corey Gallon](../sources/20260814_26RtyAm9y_Q.md), 10:43-11:32)
- **The mechanism.** The page is checking whether the click came from a human source, and "Chrome stamps every single event with just that answer, whether it's trusted or untrusted." A JavaScript-dispatched click is stamped untrusted, and the page quietly discards it. ([Corey Gallon](../sources/20260814_26RtyAm9y_Q.md), 11:20-11:45)
- **The fix.** Click through Chrome's CDP input domain, which "uses the exact same input path that your actual mouse uses." The event is stamped trusted and "the page can't tell the difference between your mouse and our agent." Viewed from inside the page's own logs, "every one of the untrusted clicks fails, but the trusted ones go through." ([Corey Gallon](../sources/20260814_26RtyAm9y_Q.md), 11:45-12:41)
- **This is a graded property, not a binary.** Trusted input clears provenance checks but not behavioral ones: challenges that sample the pointer trail still reject a straight-line, constant-speed drag, which is why the escalation continues into human-like motion. See [Climb a Humanness Ladder Only as High as the Page Forces](climb-a-humanness-ladder-only-as-high-as-the-page-forces.md). ([Corey Gallon](../sources/20260814_26RtyAm9y_Q.md), 15:00-16:30)
- **Trusted input also reaches places selectors cannot.** Because a trusted click is delivered at a screen position rather than to an element, it lands inside closed shadow roots and cross-origin iframes that expose no grabbable element — compute the coordinates from the iframe's position and let Chrome route the click. Real keystrokes route into a cross-origin widget the same way. ([Corey Gallon](../sources/20260814_26RtyAm9y_Q.md), 12:41-15:00)
- **Design consequence for agent runtimes.** "Send a JS click" and "send a CDP input event" look interchangeable in an action-space design and are not; a runtime that only offers the former will fail invisibly on a subset of sites. This is a concrete instance of the interface-not-the-model argument in [Fix the Browser-Agent Runtime Interface Before Reaching for a Better Model](fix-the-browser-agent-runtime-interface-before-reaching-for-a-better-model.md), and a reason to verify actions out-of-band ([Verify an Action Through a Different Channel Than the One That Acted](verify-an-action-through-a-different-channel-than-the-one-that-acted.md)) — a silently dropped click returns success to the caller.
- **Defender's mirror image.** Event-provenance checking is cheap and stops naive scripting, but it stops only naive scripting: any agent driving a real browser at the protocol level passes it, so it cannot carry a bot-detection strategy on its own. Compare [Layer Bot Detection Signals Instead of Trusting One Header](layer-bot-detection-signals-instead-of-trusting-one-header.md).

Related topics:
- [Agents](../topics/agents.md)
- [Security](../topics/security.md)

Related concepts:
- [Climb a Humanness Ladder Only as High as the Page Forces](climb-a-humanness-ladder-only-as-high-as-the-page-forces.md)
- [Verify an Action Through a Different Channel Than the One That Acted](verify-an-action-through-a-different-channel-than-the-one-that-acted.md)
- [Fix the Browser-Agent Runtime Interface Before Reaching for a Better Model](fix-the-browser-agent-runtime-interface-before-reaching-for-a-better-model.md)
- [Choose agent observation and action spaces explicitly](choose-agent-observation-and-action-spaces-explicitly.md)
- [Layer Bot Detection Signals Instead Of Trusting One Header](layer-bot-detection-signals-instead-of-trusting-one-header.md)

Sources:
- [The Dark Arts of Web Automation — Corey Gallon, Rexmore](../sources/20260814_26RtyAm9y_Q.md), 10:43-12:41, 12:41-16:30
