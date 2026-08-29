# Treat CAPTCHA And Proof Of Work As Economic Friction

Summary: CAPTCHA and proof-of-work defenses should be evaluated as cost-shifting mechanisms, not absolute human-verification guarantees.

Use when:
- Choosing a challenge mechanism for automated clients.
- Balancing crawler deterrence against accessibility and user-experience costs.

Details:
- CAPTCHA-style puzzles are easier for AI systems to solve or route around through audio transcription, making them cheap to breach in some settings. (13:01-13:25)
- Proof of work can deter large-scale crawling by forcing every request or site visit to spend CPU time, but it may not stop attacks with enough downstream profit, such as resale of scarce inventory. (13:32-14:42)
- Risk-adaptive challenge difficulty can use other signals, but harder challenges can create accessibility and usability failures for legitimate users. (14:46-15:08)
- **The attacker's side of the same ledger, from a source that built it.** An agent driving a real Chrome through the DevTools Protocol cleared Cloudflare Turnstile, an image CAPTCHA, a drag puzzle, and reCAPTCHA v2 with no human in the loop. Each defense fell to a different cost, not to a break: Turnstile's closed shadow root and cross-origin iframe fell to a coordinate-computed trusted click; text and tile challenges fell to the agent's own vision; the drag puzzle's pointer-trail sampling fell to an eased, curved path with a deliberate overshoot; and reCAPTCHA's round expiry — the only defense that made the attacker restructure anything — was answered by moving the whole loop into deterministic code and calling the model once per round. That last point is the useful one for a defender: the round timer forced an architecture change, while the perception challenges only cost inference. ([Corey Gallon](../sources/20260814_26RtyAm9y_Q.md), 12:41-19:36)
- Proxy projects such as Anubis, Go Away, and Nepenthes can place proof-of-work challenges in front of suspicious traffic without embedding the logic directly in the application. (15:12-15:30)

- **A third reading of the ledger, from an agent operator who does not fight the challenge at all.** Where Gallon prices each defense in inference and engineering, Šteimantas prices the challenge that is never solved: an agent that cannot tell a challenge page from a product page pays full input-token rates to have its model read the CAPTCHA — "a large language model of course can distinguish between valid shop content and a capture. But we need to spend tokens in order to do that." For a defender this is an ambiguous result. The friction lands, and it lands as real money on the automated caller, which is what a cost-shifting defense is for. But nothing is protected: the crawler is not stopped, the response is served and paid for on both sides, and the operator's obvious fix is to detect the block cheaply and route around it rather than to stop crawling. Challenges that are cheap to *detect* therefore impose less friction than challenges that are cheap to *solve* — a distinction this page's solve-cost framing does not capture. ([Šteimantas](../sources/20260826_XsvUhpnHepE.md), 08:39-10:29)

Related topics:
- [Security](../topics/security.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Layer Bot Detection Signals Instead Of Trusting One Header](layer-bot-detection-signals-instead-of-trusting-one-header.md)
- [Climb a Humanness Ladder Only as High as the Page Forces](climb-a-humanness-ladder-only-as-high-as-the-page-forces.md)
- [Chrome Stamps Every Input Trusted or Untrusted](chrome-stamps-every-input-trusted-or-untrusted.md)
- [Validate Retrieved Content Before Spending Tokens on It](validate-retrieved-content-before-spending-tokens-on-it.md)
- [Gate an Environment to Agents Only](gate-an-environment-to-agents-only.md)

Sources:
- [How to defend your sites from AI bots - David Mytton, Arcjet](../sources/20250730_Gi4V8viBGYQ.md), 13:01-15:30
- [The Dark Arts of Web Automation — Corey Gallon, Rexmore](../sources/20260814_26RtyAm9y_Q.md), 11:20-12:41, 12:41-19:36
- [The Missing Layer in Agentic AI — Giedrius Šteimantas, Oxylabs](../sources/20260826_XsvUhpnHepE.md), 08:39-10:29
