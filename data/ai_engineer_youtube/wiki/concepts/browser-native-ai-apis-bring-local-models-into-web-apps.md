# Browser-native AI APIs bring local models into web apps

Summary: Experimental browser-native AI APIs let web apps call local browser-managed models for focused tasks such as summarization and proofreading, plus broader multimodal prompt calls, without sending every request to an external AI API.

Use when:
- Prototyping AI features directly in a web application.
- Weighing local browser inference against cloud API calls for privacy, cost, latency, or offline behavior.

Details:
- The talk describes Web AI APIs as draft browser APIs that expose local models for summarization, writing, rewriting, proofreading, prompting, and multimodal inputs. (23:31-24:10, 27:23-28:12, 30:21-31:02)
- The summarizer demo checks API availability, creates a summarizer with options such as summary type, length, input language, output language, and context, then summarizes product reviews in the page. (24:53-27:21)
- The browser downloads the model locally, caches it for reuse across websites, and may evict it if storage is low; the demo notes the model is about 4 GB at that point. (26:05-26:30)
- Chrome on-device internals expose model loading, prompt playgrounds, image and audio inputs, top-k, temperature, event logs, model status, and token counts for debugging. (27:44-28:12)
- The prompt API demo accepts text plus image input to generate review content from a product image, with the speakers emphasizing that the local model runs on the client machine in the browser. (30:21-34:35)
- The speakers warn that the APIs are highly experimental, browser support is uneven, flags may be required, and API shapes can change. (27:23-27:44, 34:41-35:21)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Use edge inference when latency, privacy, offline access, or token cost dominate](use-edge-inference-when-latency-privacy-offline-access-or-token-cost-dominate.md)
- [On-device agents can combine local reasoning with tool and API calls](on-device-agents-can-combine-local-reasoning-with-tool-and-api-calls.md)
- [Tune multimodal token budgets by visual or audio task](tune-multimodal-token-budgets-by-visual-or-audio-task.md)

Sources:
- [AI Didn't Kill the Web, It Moved in! - Olivier Leplus (AWS) & Yohan Lasorsa (Microsoft)](../sources/20260410_XZ0boOjtbNo.md), 23:31-35:29
