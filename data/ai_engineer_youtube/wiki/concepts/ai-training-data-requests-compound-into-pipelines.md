# AI Training-Data Requests Compound Into Pipelines

Summary: A single data request from an AI team is rarely a feature — it is the first visible piece of a pipeline. A "download videos" ask became downloader, transcripts, subtitles, language search, metadata, and an internal glue library inside roughly three months, and the most instructive failure along the way was a wholesale request failure caused by a definition mismatch (the client said transcripts, they needed subtitles), not by a bug.

Use when:
- Scoping a data-collection or ingestion feature for an AI training, fine-tuning, or evaluation workload.
- Every request from a new integration is failing and you are about to debug the code path.
- Deciding whether to build a one-off collector or the surrounding collection/transfer/storage/delivery pipeline.

Details:
- The ask that reframed itself: a two-week deadline at a floor of "at least 5 petabytes per month" for a video API. "The feature stops sounding like a product feature. It sounds like infrastructure, because what the client actually is asking to build is not just to download some videos. They are asking for a pipeline: collection, transfer, storage, delivery" — with reliability compatible with AI training workloads. (02:33-03:18)
- Multimodal demand is the driver: "AI infrastructure is becoming increasingly more multimodal. It's no longer about the text," and companies need pipelines for video, metadata, transcripts, subtitles, and the structural context around the content. (03:18-03:40)
- The definition-mismatch failure mode: they built transcript support, the client tested, "and we see that all of the requests are failing." Investigation found nothing wrong on the provider side — "the client actually didn't need a transcript, they needed the subtitles." When a new integration fails uniformly rather than intermittently, check that both sides mean the same artifact before debugging. (04:03-04:34)
- The compounding: subtitles, then search (the client could not find videos in the languages they needed), then metadata and channel information, then an internal library gluing it together — "once it started as one product feature request, it actually became the whole product suite," a video API suite in roughly three months. (04:34-05:58)
- The commercial caveat, stated plainly: by 2026 the client had gathered 30 petabytes "and we're still waiting for a payment." Petabyte-scale delivery can outrun collection on the revenue side. (05:58-06:10)
- The lesson she draws is about what is actually being bought: "innovation is actually a repeated adaptation under high pressure… the client actually doesn't buy the first product iteration, they buy your ability to adapt." (06:10-06:21)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Works in Dev, Passes Tests, and Survives Reality Are Three Different Systems](works-in-dev-passes-tests-and-survives-reality-are-three-systems.md)
- [Define the Unit of Work Behind a Throughput Target](define-the-unit-of-work-behind-a-throughput-target.md)
- [Elicit Requirements as the Non-Automatable Bottleneck](elicit-requirements-as-the-non-automatable-bottleneck.md)
- [Let an Agent Build and Maintain Self-Healing Scrapers](let-agents-build-and-maintain-self-healing-scrapers.md)

Sources:
- [How Web Data Infrastructure Powers the Next Generation of AI — Patricija Žemaitytė, Oxylabs](../sources/20260814_1UmZHb_E_SM.md), 02:33-06:21
