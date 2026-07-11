# Browser Agents Don't Need Better Models. They Need Better Eyes.

Source: [Browser Agents Don't Need Better Models. They Need Better Eyes. - Kushan Raj, ARK](https://www.youtube.com/watch?v=JnubYCYunk8)
Uploaded: 2026-06-28
Transcript: `raw/20260628_JnubYCYunk8/JnubYCYunk8.en-orig.vtt`

## Summary

Kushan Raj (ARK, previously founding ML engineer at Sarvam AI) argues that browser agents fail not because the model is too weak but because the runtime interface around it is poor. He rebuilt the interface along three levers — what the model *sees* (a compact whole-page representation instead of a raw DOM dump or a single screenshot), what it can *do* (fast actions with stable handles instead of one click per call), and what it *learns from* (step-by-step delta feedback instead of pass/fail at the end) — and found that changing the interface alone took the *same, cheaper* model from confusion to correct multi-step execution on hostile pages. Concrete demos: a baseline browser agent spent 10-20s just to click a Start button on a 30-step challenge and stalled; Claude took two minutes and got stuck scrolling trying to download an Aadhaar document, and could not pick a date on an unfamiliar Canadian booking site, while his runtime completed both quickly. He plans to open-source it and expose it as a "URL + intent → executed result" API.

## Extracted Concepts

- [Fix the Browser-Agent Runtime Interface Before Reaching for a Better Model](../concepts/fix-the-browser-agent-runtime-interface-before-reaching-for-a-better-model.md) - the talk's thesis: observation, action, and feedback are bigger levers than model swaps for browser agents.
- [Give Browser Agents a Compact Whole-Page Representation](../concepts/give-browser-agents-a-compact-whole-page-representation.md) - the observation lever, with the DOM/screenshot/markdown token comparison.

## Topic Links

- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Context Engineering](../topics/context-engineering.md)

## Notes

- Thesis stated directly: "models are pretty smart, but it's the infra around them that sucks." (00:56-01:01)
- The goal is to "give a nice environment for the agent to use" so it can plan long sequences, figure out where it failed, and plan the click correctly; the enabling piece is "a cool representation which compresses the website and lets the agent see the entire page in very few tokens." (01:09-01:26)
- Baseline browser agent on the "browser challenge" benchmark (30 sequenced steps) took 10-20 seconds just to click the Start button and struggled to debug why a click did nothing. (00:30-01:09)
- Observation-cost comparison for one page: full DOM ≈ 20,000 tokens; a screenshot ≈ 1,100 tokens but shows only one viewport snippet; his markdown ≈ 1,800 tokens and represents the *entire* page. Give markdown alongside a screenshot — cheap token-wise — and the model reasons well and constructs a long action sequence. (03:33-04:23)
- Feedback lever: track the full end-to-end browser page and tell the agent the deltas — "these are the new things that have popped up," "this is now gone," "the thing blocking what you wanted to click has been removed," and "you tried to click this, but that didn't happen" — instead of only a final pass/fail. (03:50-04:08)
- Evidence of the model-vs-interface split: Claude with default computer-use took ~2 minutes and got stuck screenshot-scroll-screenshot on an Aadhaar download, and stalled unable to pick a date on an unfamiliar Canadian booking site; the same tasks completed quickly on his runtime using a cheaper model. (01:28-02:41)
- Productization plan: open-source the (not-very-defensible) code and ship an API — "give me a URL, give me your intent and I will execute it" — or a website/plugin; the mission is to make browser agents faster, cheaper, and more reliable. (02:45-03:17)
