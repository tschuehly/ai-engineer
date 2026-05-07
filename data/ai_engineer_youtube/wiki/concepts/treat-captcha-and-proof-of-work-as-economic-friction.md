# Treat CAPTCHA And Proof Of Work As Economic Friction

Summary: CAPTCHA and proof-of-work defenses should be evaluated as cost-shifting mechanisms, not absolute human-verification guarantees.

Use when:
- Choosing a challenge mechanism for automated clients.
- Balancing crawler deterrence against accessibility and user-experience costs.

Details:
- CAPTCHA-style puzzles are easier for AI systems to solve or route around through audio transcription, making them cheap to breach in some settings. (13:01-13:25)
- Proof of work can deter large-scale crawling by forcing every request or site visit to spend CPU time, but it may not stop attacks with enough downstream profit, such as resale of scarce inventory. (13:32-14:42)
- Risk-adaptive challenge difficulty can use other signals, but harder challenges can create accessibility and usability failures for legitimate users. (14:46-15:08)
- Proxy projects such as Anubis, Go Away, and Nepenthes can place proof-of-work challenges in front of suspicious traffic without embedding the logic directly in the application. (15:12-15:30)

Related topics:
- [Security](../topics/security.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Layer Bot Detection Signals Instead Of Trusting One Header](layer-bot-detection-signals-instead-of-trusting-one-header.md)

Sources:
- [How to defend your sites from AI bots - David Mytton, Arcjet](../sources/20250730_Gi4V8viBGYQ.md), 13:01-15:30
