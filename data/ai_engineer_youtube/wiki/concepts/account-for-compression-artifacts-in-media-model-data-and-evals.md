# Account For Compression Artifacts In Media Model Data And Evals

Summary: Media models and evals inherit the perceptual assumptions and artifacts embedded in compressed internet data. Training and scoring pipelines should consider JPEG, audio, and video compression effects instead of treating downloaded media as neutral ground truth.

Use when:
- Curating internet-scale image, audio, or video training data.
- Debugging eval disagreement between metric scores and human perceptual judgment.

Details:
- JPEG exploits human sensitivity differences by separating brightness from color and downsampling color channels, producing images that can look the same to humans while carrying much less information (04:02-05:24).
- The same perceptual-compression principle appears in audio and video codecs such as MP3 and MP4, where imperceptible information is removed by design (05:36-05:55).
- Because much internet media is already compressed, model training and evaluation may propagate human perceptual limits and codec artifacts into generated-media systems (06:33-07:00).
- The speaker recommends taking artifacts and the nature of compressed training data into account when training and evaluating media models (13:10-13:31).

Related topics:
- [Generative Media](../topics/generative-media.md)
- [Models](../topics/models.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Curate generative-media data before tuning model internals](curate-generative-media-data-before-tuning-model-internals.md)
- [Train image and video diffusion models in learned latent spaces](train-image-and-video-diffusion-models-in-learned-latent-spaces.md)

Sources:
- [Perceptual Evaluations: Evals for Aesthetics - Diego Rodriguez, Krea.ai](../sources/20250823_h5ItAJuB3Fc.md), 04:02-07:00, 13:10-13:31
