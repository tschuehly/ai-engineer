# AI Engineer YouTube Index

- Channel: https://www.youtube.com/@aiDotEngineer/videos
- Generated at: 2026-08-19T19:39:01+00:00
- Since: 2025-08-19
- Until: open
- Videos: 537

## AI is the World’s largest Relationship Therapist — Clay Cockrell & Tony Fabrikant, CoupleWork AI

- Upload date: 2026-08-19
- Video: https://www.youtube.com/watch?v=yoONZwV2smc
- Transcript: raw/20260819_yoONZwV2smc/yoONZwV2smc.en-orig.vtt
- Metadata: raw/20260819_yoONZwV2smc/yoONZwV2smc.info.json

The springs in the middle of the loveseat in Clay Cockrell's counseling office gave out years ago, so gravity now tips a couple toward each other however hard they grip the arms. He kept it. The harder argument arrives with two numbers. BetterHelp spent a decade assembling roughly 35,000 licensed clinicians and reaching 5 million users. ChatGPT sees roughly 900 million weekly active users, and enough open it at 11pm after a fight that Cockrell calls the world's largest relationship therapist a language model optimized to keep you engaged.

His objection is not that the model is unqualified but that it is agreeable. Ask why your partner never listens and it validates you, which he calls a very expensive mirror that only shows you in your best light. Sycophancy here is a clinical failure mode. The user does not get more self aware, they get more certain, and they return with a cleaner case and less curiosity about what their partner experienced. Against that he sets the real standard of care, John Gottman's lab predicting divorce from a 15 minute conversation with over 90% accuracy, and emotionally focused therapy, both largely absent from commercial products. The safety gap is sharper, since a general assistant cannot hear the difference between we fight a lot and I am afraid of what happens when I disagree with him. Tony Fabrikant closes on the engineering: start with the clinician rather than the prompt, encode what good looks like as hundreds of evals, and treat one failing safety test as disqualifying.

Speaker info:
- https://www.linkedin.com/in/clay-cockrell-906b0b4/
- https://www.linkedin.com/in/tony-fabrikant
- https://www.walkandtalk.com/

Timestamps:
0:00 - The couch that leans a couple toward each other
1:42 - A show of hands, and who is already doing this
3:12 - BetterHelp's decade against ChatGPT's week
4:29 - Optimizing for engagement is a clinical fire alarm
5:21 - Why being validated is not therapy
6:37 - Sycophancy as a clinical failure mode
7:52 - Gottman, EFT, and the real standard of care
9:33 - What a general assistant cannot hear
10:37 - The data you hand a relationship coach
11:40 - Building Maxine to know when to stop coaching
14:27 - Tony Fabrikant on evals when safety is on the line

## From Ambient Documentation to Clinical Intelligence — Chaitanya Asawa, Abridge

- Upload date: 2026-08-19
- Video: https://www.youtube.com/watch?v=u6q-byPWUuo
- Transcript: raw/20260819_u6q-byPWUuo/u6q-byPWUuo.en-orig.vtt
- Metadata: raw/20260819_u6q-byPWUuo/u6q-byPWUuo.info.json

Clinicians call it pajama time: the roughly two hours a day spent writing visit notes after work has finished. Abridge started there, and within two to three years the documentation product alone reached 300 of the largest health systems in the United States. Chaitanya Asawa's framing is that everything in healthcare sits downstream of a single conversation between a doctor and a patient, and that the administrative machinery got built around that conversation rather than out of it. The notes are high stakes in both directions. They are the basis of billing, and they are the context the next clinician inherits.

The engineering problem he stays with longest is evaluation, because clinical decision support leaves almost no gap between generating an answer and checking one. Sudoku is hard to solve and trivial to verify. Here, a verifier good enough to trust would already be your generator. Their approach abandons the idea of a single correct answer, since many different responses can be right. Two physicians independently write rubrics describing the elements a good response should contain, a third adjudicates those into one rubric, a fourth runs quality assurance, and only then does a judge score responses against those elements. Separate judges cover safety, adversarial boundaries and tone. On cost, at a run rate near 100 million medical conversations a year, they decompose the note into its sections and post train smaller models per section rather than running frontier intelligence over everything, betting that a dataset nobody else holds plus a narrow enough problem can outrun the frontier's rate of change.

Speaker info:
- https://x.com/c_asawa
- https://www.linkedin.com/in/casawa

Timestamps:
0:00 - Reading the room, and hearing from clinicians
2:08 - Why healthcare gets dismissed as a technical domain
2:59 - From robotics to search to healthcare
5:25 - Costs that only go up, and a productivity paradox
6:14 - Closures, thin margins, and clinician burnout
7:04 - The note after every visit, and pajama time
7:56 - Why documentation was the wedge
8:48 - Everything is downstream of the conversation
9:38 - Asking about trials and placing an order by voice
10:27 - What context the system actually reads
11:27 - Quality, latency and cost on hard mode
13:08 - Evaluation as the operating system
13:57 - Encoding clinician judgment into judges
14:48 - Contextual clinical decision support
15:38 - When the generator and verifier gap collapses
16:27 - Four physicians to build one rubric
18:05 - Cost at 100 million conversations a year
18:56 - Smaller models per section of the note
19:49 - Catching orders spoken during a visit

## Why Your Enterprise Tech Stack Isn’t Ready for AI Agents — Christopher Lovejoy & Saul Howard

- Upload date: 2026-08-19
- Video: https://www.youtube.com/watch?v=mav15aW9lLM
- Transcript: raw/20260819_mav15aW9lLM/mav15aW9lLM.en-orig.vtt
- Metadata: raw/20260819_mav15aW9lLM/mav15aW9lLM.info.json

The proof of concept works. It hits the accuracy targets, it is fast, it is cheap, and the room is happy. Then someone from compliance raises a hand and asks to see the audit trail, and the whole thing stops. Christopher Lovejoy and Saul Howard have watched that meeting happen repeatedly, and their point is that an audit trail is not a developer log. Under the frameworks enterprises actually answer to, it is a complete record of every action an agent took, every place it touched data, and the authorization behind each one, durable enough to stand up as a chain of evidence if the decision were ever examined in court.

Their answer is to take the constraints seriously first and rebuild toward the accuracy afterwards, rather than bolting requirements onto a demo. An immutable append only event log makes auditability fall out of the storage model instead of being reconstructed later, at the cost of harder reads. Patient data lives in schema driven object storage alongside that log rather than inside it, so the events hold only references, which lets engineers debug what an agent did without being exposed to the health data itself, and gives a natural place to enforce zero trust and constrain prompt injection. Escalation works because humans and models are both treated as agents, so any action either can take, the other can take too. Evaluation then emerges from those three primitives rather than being attached to the side, including on production data that never leaves the customer's environment.

Speaker info:
- https://x.com/ChrisLovejoy_
- https://www.chrislovejoy.me
- https://x.com/saulhoward
- https://linkedin.com/in/saulhoward

Timestamps:
0:00 - Why healthcare is hard, and what transfers to other regulated work
1:57 - The enterprise proof of concept
2:49 - What the buildout actually connects to
3:39 - Everyone assumes the hard part is done
4:28 - The questions that arrive the next day
5:19 - An audit trail is not a developer log
7:03 - The immutable event log, and its tradeoff
8:46 - What shape healthcare data actually has
10:28 - Object storage beside the log, not inside it
11:20 - Debugging an agent without seeing the data
12:15 - Zero trust and the lethal trifecta
13:07 - Escalation when you cannot predict it
13:58 - Treating humans and models as the same kind of agent
14:49 - Why evals are hard here
15:39 - Evaluation as a byproduct of the primitives
17:20 - Architecture as choosing what stays simple
18:08 - Where it goes wrong, and where it goes right

## Trading Desks to Clinical Trials: Parallels in Applied Vertical AI — Ayush Bhardwaj, Allos AI

- Upload date: 2026-08-19
- Video: https://www.youtube.com/watch?v=Yphdry8ttAQ
- Transcript: raw/20260819_Yphdry8ttAQ/Yphdry8ttAQ.en-orig.vtt
- Metadata: raw/20260819_Yphdry8ttAQ/Yphdry8ttAQ.info.json

Ayush Bhardwaj could build the agent. What he could not do was tell whether it was any good. He moved from applied AI at a hedge fund to a pharma tech company expecting a different world, and found the job identical, including the wall. An engineer glances at generated code and knows instantly that it is weak, because years of training built that judgment. Nobody on his team had the equivalent instinct for a trade thesis or a drug candidate. He calls this the point where vertical AI projects quietly die, because the thing looks finished and then nobody buys it.

Judging his way out with a model was, in his words, a stupid mistake, since it jargons its way through without knowing what alpha means. Verifiable rewards work for math and code because answer keys exist. Worse, the data that would teach a model to reason in these fields is deliberately withheld. Funds must file their holdings quarterly, and their returns drop once competitors reverse engineer them. Disclosing every clinical trial is legally required, yet roughly 30% of firms never do, and in 2026 the FDA publicly reminded more than 2,000 sponsors. The frontier labs do not have it either. So his answer is to hire the user, which for a team of young engineers meant hiring a senior scientist, after which their tools started speaking big pharma's language. That expert curates sources, sharpens prompts and does the judging, starting from error analysis as the cheapest rung. The moat is never the model or the infrastructure. Both are commodities.

Speaker info:
- https://x.com/aybh08
- https://www.linkedin.com/in/aybh/
- https://ayushb.me/

Timestamps:
0:00 - Reading the room
1:04 - What applied vertical AI actually means
2:43 - Leaving a hedge fund for pharma and changing nothing
3:34 - The wrong question about agents in production
4:27 - Step one, make the task narrow
5:18 - Proprietary data is the only real differentiator
6:57 - The easy part fits on one screen
7:50 - Why you cannot iterate on what you cannot judge
9:30 - Trying to use a model as the judge
10:21 - The data was never there, by design
12:05 - Hire the user
12:55 - Building the learning loop around a domain expert
14:39 - From error analysis up to preference training
16:20 - Reaching production is not the same as working
17:10 - The seven steps
18:00 - AI in the loop, not human in the loop
19:00 - Your moat is domain expertise and data

## Guardrails First: Engineering Member-Facing Health AI — Rashi Agrawal, Hinge Health

- Upload date: 2026-08-19
- Video: https://www.youtube.com/watch?v=YXEqC05WEI0
- Transcript: raw/20260819_YXEqC05WEI0/YXEqC05WEI0.en-orig.vtt
- Metadata: raw/20260819_YXEqC05WEI0/YXEqC05WEI0.info.json

A healthy 60 year old man asked a popular AI assistant how to cut salt from his diet. It pointed him at sodium bromide. Three months later he arrived in an emergency room with paranoia and hallucinations, bromide at 200 times the safe level, and stayed three weeks. Rashi Agrawal stacks that against the first independent safety test of a consumer health AI, out of Mount Sinai, which under triaged life threatening emergencies half the time, and against ECRI naming chatbot misuse the top health technology hazard of 2026. Roughly 40 million people already triage themselves this way. None of it is a frontier problem. It is the production baseline.

Her argument is that most healthcare AI safety failures are architectural decisions made before a single token is generated. PHI is stripped at the pipeline boundary on ingestion, so a developer who opens a dashboard finds nothing to redact because it was never stored. Anything that can never be wrong lives in a code layer above the model rather than in its prompt: routing to 911 or 988, deciding which capability owns a turn, verifying who is on the other end. The frontier labs publish an authority hierarchy in which every layer above the user sits one prompt injection from being overridden, and her reading is blunt: if they will not treat a prompt as a security boundary, neither should you. Safety then runs as a continuous layer of judges scoring live traffic, with one discipline attached. When a score drops, first ask whether the judge is right.

Speaker info:
- https://www.linkedin.com/in/rashi283/
- https://sessionize.com/rashiagrawal/

Timestamps:
0:00 - The state of healthcare AI, and 40 million self triagers
1:04 - Poisoned by a chatbot
1:30 - Under triaging emergencies half the time
2:35 - Three non negotiable foundations
3:41 - Where PHI actually lives
5:53 - Deterministic rules belong above the model
7:27 - If the labs will not trust the prompt, neither should you
7:54 - Escalation, intent routing, identity
9:39 - Safety as a continuous evaluation layer
12:47 - Five stakeholders, five risks, five days to launch
14:02 - The five rules for deciding
18:10 - Verify the scorer before you trust the score
20:24 - The whole talk in one slide

## Don’t be data poor — Anuj Iravane, Anterior

- Upload date: 2026-08-19
- Video: https://www.youtube.com/watch?v=XAsb7MIAzm8
- Transcript: raw/20260819_XAsb7MIAzm8/XAsb7MIAzm8.en-orig.vtt
- Metadata: raw/20260819_XAsb7MIAzm8/XAsb7MIAzm8.info.json

Roughly 70% of medical communication still moves by fax. What reaches Anterior is scanned fax bundles that can run past 300 pages, carrying handwriting, checkboxes, tables and images across one patient's entire clinical trajectory. Anuj Iravane calls it an observation through a fuzzy lens over a lifespan. It is exactly the data his evals need, and the data he is least allowed to keep: their contracts rule out retaining it, deriving from it, or holding redacted or anonymized copies. Nothing survives into a dataset. In a domain where 95% accuracy is not good enough, that is a real problem.

So they generate it, by running the inference workflow backwards. The forward task takes unstructured data plus a policy, follows a reasoning trace and arrives at a label. Reversed, you sample a label, sample a reasoning trace, then build the record that would have produced it. That works because Anterior already models policies explicitly as decision trees, so traces come from a far more uniform distribution than a model asked to invent variety, which tends to collapse onto the same few cases. A coarse to fine pipeline layers patient invariants into a journey of provider encounters, then fans out into documents, with a consistency eval catching contradictions between documents written in parallel. Because generation starts from the label, labels are correct by construction and ground truthing disappears. Clinicians own the pipeline as skills rather than code. Roughly 90% of their datasets are now synthetic, and in a blind review clinicians separated synthetic from real only about 60% of the time.

Speaker info:
- https://x.com/anujiravane
- https://www.linkedin.com/in/anujiravane/
- https://www.anterior.com/

Timestamps:
0:00 - Policy guided decisions over highly unstructured data
1:05 - Most medical communication still arrives by fax
2:11 - Why 95% is not good enough
2:37 - The data you need most is the data you cannot keep
3:05 - Betting on generating it instead
3:55 - Why one shotting a 300 page record fails
5:00 - Reversing the forward task
5:51 - Policies as decision trees you can sample from
7:19 - Testing the edge cases production data never had
8:09 - Building a record coarse to fine
9:54 - The refinement loop and the round trip check
11:09 - Why it never becomes a PDF
11:34 - Giving clinicians the keys through skills
14:12 - Results, and datasets built just in time

## How to build an AI-Native Health Company — Dan Feng, Maven Clinic

- Upload date: 2026-08-19
- Video: https://www.youtube.com/watch?v=WJRdLNhrsLQ
- Transcript: raw/20260819_WJRdLNhrsLQ/WJRdLNhrsLQ.en-orig.vtt
- Metadata: raw/20260819_WJRdLNhrsLQ/WJRdLNhrsLQ.info.json

Implementation used to be the expensive step, so teams spent weeks settling requirements before anyone wrote code. Dan Feng's observation is that the cost moved. Building takes minutes now, and arguing is what is expensive. Planning at Maven Clinic changed to match. A one year view survives only as direction, assuming models will handle whatever you need by then, while real commitment runs two to four weeks. Long requirement documents gave way to a page or two meant to be argued with. The awkward casualty is the three to six month plan, which he treats as close to unplannable when nobody knows what models will do by then.

The rest is what breaks at that speed. Engineers who once wrote hundreds of lines a day now write thousands, so review had to change rather than scale. Engineers self certify which pull requests need a second reader and stay accountable either way, requests are capped near 500 lines, and large features are stacked into several. The failure he names is the rubber stamp, which buys false confidence rather than none. On reliability he refuses a single bar and sorts failures into tolerable and not. A scheduling action that fails one time in 10,000 is survivable, since the user clicks again. A reimbursement claim is not, because asking for $50 and receiving $200 is an escalation in either direction, so several models read the same receipt and it proceeds only if they agree. Integration tests run many times rather than once, since passing a nondeterministic system on one attempt proves very little.

Speaker info:
- https://www.linkedin.com/in/dan-feng-2bb5703/
- https://www.mavenclinic.com/

Timestamps:
0:00 - Who here is already AI native
0:51 - Maven Clinic, and starting the journey two years ago
1:29 - Tractors do not replace farmers
2:08 - Adopting internally, then building it into the product
3:25 - Early adopters, the majority, and the reluctant
4:04 - Meeting engineers on whichever tool they moved to
4:43 - Why senior engineers stopped delegating implementation
6:03 - The blurring line between product and engineering
6:42 - Rewarding it in performance reviews
7:21 - When building is cheap and arguing is expensive
8:00 - Dream big for the year, commit for the sprint
9:16 - Why three to six month plans became the hard part
9:56 - Starting with the lowest risk coding tasks
10:36 - Pushing it to the whole team
11:13 - Code review when volume goes up tenfold
11:54 - Self certifying, capping size, stacking changes
12:34 - The rubber stamp problem
13:57 - Deciding which failures are acceptable
14:35 - Claims, where the tolerance is zero
15:54 - Automated evaluation plus human spot checks

## Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents — Vasant Kearney, Onlay

- Upload date: 2026-08-19
- Video: https://www.youtube.com/watch?v=UyyOoJmuATU
- Transcript: raw/20260819_UyyOoJmuATU/UyyOoJmuATU.en-orig.vtt
- Metadata: raw/20260819_UyyOoJmuATU/UyyOoJmuATU.info.json

Call the payer, open their web portal, and read their X12 feed, and all three can tell you the patient is covered. You treat the patient anyway, and the claim comes back denied because they were not covered at the time. Vasant Kearney's point is that none of those surfaces is ground truth. A payer's phone system, portal and X12 layer are often built by different teams, sometimes by different contractors entirely, so they can contradict each other and they can just as easily agree on the wrong answer together.

His response is to treat X12 as a harness rather than a file format. Models do their best work confined, the way a strict language confines, and X12 already encodes the contract between a provider and a payer. Every stage of the claim lifecycle has an X12 correspondence, from an eligibility check as a 270 through the 999 that acknowledges syntax to the 835 that records payment, so an agent placing a phone call or driving a portal is emitting the same transaction by another route. Everything normalizes into an internal representation held as correct only until downstream evidence says otherwise. Two constraints travel with it. Memory has to live in a database rather than on local disk the way coding agents do it, for logical separation. And a stronger model cannot simply be dropped in, because better on a benchmark is not the same as better inside a system built around the model it replaces. He describes the posture as being AI pilled and AI skeptical at once.

Speaker info:
- https://x.com/vasantkearney
- https://www.linkedin.com/in/vasant-kearney-7b7a48b3
- https://onlay.ai/

Timestamps:
0:00 - Reading the room
1:06 - The goal is cost and patient experience
1:58 - How we arrived at an execution layer
3:06 - Solving handwritten digits does not cash the check
4:42 - What gets lost when you flatten a multimodal record
6:16 - What the agentic execution layer actually touches
7:23 - Why enterprise memory cannot live on local disk
7:49 - A better model is not automatically better for you
8:31 - Harness, and why X12 belongs in it
9:44 - Fifty steps, error propagation, and the cost of pure reasoning
11:16 - Memory that helps without steering the user
12:36 - The claim lifecycle, transaction by transaction
13:29 - A phone call is an X12 transaction underneath
14:47 - The schema is public, so agents can look it up
15:30 - X12 is a system of rules, not ground truth
16:47 - Normalizing to an internal representation
19:02 - Be AI pilled and AI skeptical

## Shipping AI to a Million Patients Without an A/B Test — Jared Joselowitz, Ufonia

- Upload date: 2026-08-19
- Video: https://www.youtube.com/watch?v=McknwOzbmyg
- Transcript: raw/20260819_McknwOzbmyg/McknwOzbmyg.en-orig.vtt
- Metadata: raw/20260819_McknwOzbmyg/McknwOzbmyg.info.json

You cannot A/B test on patients, because randomizing someone into the worse variant is unethical and often illegal. You cannot undo a call once spoken. And a vendor's benchmark number is not a defense at a post incident review. Jared Joselowitz builds the safety and evaluation stack behind Dora, a Ufonia voice agent that phones patients for post op follow ups and pre op checks. It has made roughly 200,000 real clinical calls across 20 UK hospitals and is contracted to reach a million patients within two years. Because it asks about symptoms and gives advice, it is a regulated medical device.

Ship to 5% and watch the dashboard does not survive that. 5% is thousands of patients, and a dashboard turning red means someone was already harmed. So the reactive loop moves into simulation, as self driving did with millions of simulated miles. Their framework has one model play the patient against hazards written with clinicians, and a second model judge every dialogue. Both were validated rather than assumed. In a patient and public involvement study, real patients shown a genuine consultation beside a simulated one picked the simulated patient as more realistic in three of four sets. The judge, checked against 10 clinicians from 10 specialties on 240 cases, matched or beat them at near perfect sensitivity, the metric that counts when a missed red flag is catastrophic and a false alarm is merely annoying. Prompts are then optimized against a cost matrix instead of hand tuned. You do not ship the model, you ship the evidence.

Speaker info:
- https://x.com/JaredJoselowitz
- https://www.linkedin.com/in/jaredjoselowitz/
- https://jossy.co.za/

Timestamps:
0:00 - Proving a product is safe before a patient hears it
1:28 - What Dora is, and the scale it runs at
2:18 - A call with a patient after cataract surgery
3:22 - Giving advice makes it a regulated medical device
3:59 - Starting from what could actually harm someone
4:35 - Why ship to 5% and roll back breaks here
5:53 - Borrowing the simulation playbook from self driving
6:32 - Matrix, and a model that plays the patient
8:24 - Can real patients tell which one is simulated
9:43 - An automated judge, and validating it against clinicians
11:35 - How brittle prompts really are
12:50 - Optimizing prompts instead of hand tuning them
13:30 - Making the metric a real cost function
14:42 - The flywheel that replaces the reactive loop
15:20 - Simulation is necessary, not sufficient
16:38 - Shipping the evidence, not the model
17:14 - New modalities bring new hazards, same framework

## 200 Million Patient Interactions Later — Vivek Muppalla, Hippocratic AI

- Upload date: 2026-08-19
- Video: https://www.youtube.com/watch?v=AN65uc645mE
- Transcript: raw/20260819_AN65uc645mE/AN65uc645mE.en-orig.vtt
- Metadata: raw/20260819_AN65uc645mE/AN65uc645mE.info.json

Asked how many in the room had ever received a proactive call from their healthcare provider, almost no hands went up. Vivek Muppalla treats that as the signature of scarcity: too few clinicians and too few hours, so the system triages and only the sickest get called. Hippocratic AI is past 200 million clinical conversations across more than 60 health systems, which is what changes the arithmetic. The tradeoff they refused is the familiar one: models accurate enough for this work can take tens of seconds to answer, and models fast enough for a phone call are not safe enough to make one.

So the stack was built end to end. Polaris runs 31 models on every conversation, one holding the thread and 30 specialists covering labs, medications and scheduling, executed in parallel with each specialist first making a fast check on whether it has anything to say at all. A single model would be a single point of failure. Their speech recognition is a decoder only audio system fed the conversation so far and the domain context alongside the audio, so a drug name resolves against a finite list rather than an unbounded one, and prosody survives the projection so it hears the how as well as the what. Single word answers get a second scoring pass, because a heard as no is catastrophic. On evaluation he does the arithmetic that makes 99% unacceptable: at 10,000 calls a day that is 100 people sent to the wrong appointment, and catching a 1% failure rate takes roughly 450 tests.

Speaker info:
- https://x.com/vim1up
- https://www.linkedin.com/in/vivekmuppalla/
- https://hippocraticai.com/

Timestamps:
0:00 - Who has ever been called by their provider
1:05 - Triage as a math problem, and what flips it
1:54 - The oath every employee takes
2:44 - A call with a patient, start to escalation
5:12 - Why a generic voice stack does not work
6:04 - Building vertically to get speed and intelligence
7:44 - Latency and intelligence as a compounding flywheel
8:36 - Polaris, and running 31 models at once
9:29 - What speech recognition gets wrong in the real world
10:27 - Feeding context and domain knowledge into the audio model
11:19 - A finite list of medications instead of an infinite one
12:10 - Rescoring single word answers
13:51 - How a specialist decides to speak up
14:43 - Verifiers for tool calls
15:34 - Quantization, speculative decoding, cache
16:25 - Why 99% is a bad number here
17:14 - The tests needed to catch a 1% failure
18:03 - Grading on the scale used for humans
18:55 - Building a benchmark for empathy

## Voice agents with Realtime Video — Sidney Primas, LemonSlice

- Upload date: 2026-08-18
- Video: https://www.youtube.com/watch?v=z1dqv74SpUs
- Transcript: raw/20260818_z1dqv74SpUs/z1dqv74SpUs.en-orig.vtt
- Metadata: raw/20260818_z1dqv74SpUs/z1dqv74SpUs.info.json

An avatar of Teddy Roosevelt holds court in a replica Oval Office, generating video continuously for eight hours with no reset, and a second deployment is being built to run for sixteen. That duration is the hard part. Sidney Primas explains that a real time avatar can only look backward, because the future frames do not exist yet, so every block it generates inherits the errors of the blocks before it and compounds them. LemonSlice trains with an attention mask that enforces this during training rather than discovering it at inference, and collapses roughly 30 denoising steps down to a single step to hit real time.

The less obvious bottleneck is audio. Emotion and facial expression turn out to depend on the audio embedding, and most audio encoders are trained on audiobooks, which are monotone by construction, so an expressive model needs its own. The wider bet is to take a world model and point it at humans, paying a harder training and deployment cost up front in exchange for full body movement, object interaction, and physics arriving closer to free. Two things surprised him. Serving this costs about what serving a voice model costs, despite the difference in pixels. And the model harness, meaning the orchestration of threads and queues across GPU and CPU so that video never stutters through an interrupt, is where he now thinks much of the durable value will sit.

Speaker info:
- https://www.linkedin.com/in/sidneyprimas/

Timestamps:
0:00 - Breaking the avatar Turing test
2:26 - Teddy Roosevelt in a replica Oval Office
4:40 - Why the visual layer matters
5:46 - Pointing a world model at humans
6:58 - One image in, any style out, and being the API layer
9:12 - Audio is what makes it expressive
10:15 - Making a video model interactive, then real time
12:22 - Error accumulation over hours of generation
14:34 - Cost parity with a voice model
15:36 - The model harness nobody talks about
16:38 - An emotion engine for the next model
19:55 - A single end to end EQ layer
22:09 - Questions: internal state, and a real Turing test

## Building an Agentic Video Editor for Mass Consumer — Ekaterina Deyneka, Reelful

- Upload date: 2026-08-18
- Video: https://www.youtube.com/watch?v=pPj_tjlvYjA
- Transcript: raw/20260818_pPj_tjlvYjA/pPj_tjlvYjA.en-orig.vtt
- Metadata: raw/20260818_pPj_tjlvYjA/pPj_tjlvYjA.info.json

Nearly every hand in the room went up when she asked who had recorded video at the conference. Almost none stayed up for who had actually posted any of it. Ekaterina Deyneka counts herself in that gap, and Reelful is her answer to it: drop in raw footage with a line of direction, and an agent finds the usable moments, cuts them together, and generates captions, music, voiceover, and b roll around them.

Her framing for an AI engineering audience is that an agentic video editor is structurally the same thing as an agentic app builder. A prompt goes in, a sandbox spins up, an agent works inside it with tools and skills, and something renders out the other end. The difference that matters is editing rather than generating. A blank canvas lets an agent do anything it likes, while real footage forces it to judge which take is best and what to drop, and to produce something polished from material that is often messy or incomplete. The composition layer is Remotion, which expresses video as React code, chosen precisely because agents write code well. Skills carry the taste: cut rules, font pairings, when a cutaway actually helps. A verification pass catches compositions that will not render and sends the agent back around. All of it hides behind mobile templates, since the point is that a consumer never sees the pipeline at all.

Speaker info:
- https://x.com/katedeyneka
- https://www.linkedin.com/in/katedeyneka
- https://www.katedeyneka.com

Timestamps:
0:00 - Who recorded video here, and who actually posted it
1:29 - What agentic video editing means
3:33 - The same shape as an agentic app builder
4:10 - Editing real footage is harder than generating
5:30 - The pipeline, from media understanding to a creative plan
6:50 - Remotion, video as React code, and the verification layer
8:49 - Hiding all of it behind mobile templates

## Infra behind Krea 2: How to train and serve at scale — Gabriel Jorge Menezes, Krea.ai

- Upload date: 2026-08-18
- Video: https://www.youtube.com/watch?v=byn9PURoBNY
- Transcript: raw/20260818_byn9PURoBNY/byn9PURoBNY.en-orig.vtt
- Metadata: raw/20260818_byn9PURoBNY/byn9PURoBNY.info.json

GPU utilization is a lie. It read 100% straight through pretraining while the cluster was nowhere near well used, so Gabriel Jorge Menezes tracks tensor core utilization instead, and watched it climb as training resolution stepped from 128 pixels up to 1024. That is one of several numbers he argues you cannot train at this scale without. InfiniBand counters are exported by nothing off the shelf, and most of their failures turned out to be cross node communication, so they built that collection themselves. Any GPU running hotter than 78 degrees gets pulled rather than debugged, because one warm card throttles and destabilizes the entire run.

This is the infrastructure half of Krea 2, the model trained from scratch on thousands of GPUs. Crashes scaled with the cluster and often failed silently, with communication timing out while every dashboard stayed green, and the practical answer was to stop treating each one as a mystery. Let it crash, and the same nodes running the same code will frequently go 24 hours on the next attempt. What made that survivable was checkpointing aggressively against a filesystem quick enough to write a terabyte in under 30 seconds. Production and training then share one cluster, with training holding priority and inference evicted to outside providers through a fake Kubernetes node, migrated back gradually rather than all at once so the site never drops.

Speaker info:
- https://www.linkedin.com/in/gabriel-jorge-menezes/
- https://gab-menezes.github.io/

Timestamps:
0:00 - Krea 2, trained from scratch, and two open checkpoints
3:26 - Crashes at scale, and the silent ones
4:18 - Metrics are everything, starting with temperature
5:58 - GPU utilization is a lie, use tensor cores
6:48 - InfiniBand and NVLink metrics you have to build yourself
8:29 - Checkpointing hard against a fast filesystem
9:21 - Gang scheduling, and training outranking production
11:01 - Flipping inference out through a fake node
14:23 - Taints that stop you wasting GPUs
16:03 - Inference runs on almost any GPU

## Generative Video at the Speed of Light — Keegan McCallum, uRun

- Upload date: 2026-08-18
- Video: https://www.youtube.com/watch?v=Xln-On3syJk
- Transcript: raw/20260818_Xln-On3syJk/Xln-On3syJk.en-orig.vtt
- Metadata: raw/20260818_Xln-On3syJk/Xln-On3syJk.info.json

Ten dollars now buys roughly three hours of continuously generated video, and fifty buys fifteen. Keegan McCallum sets that against the room's own habits, since plenty of hands went up for burning that much on coding tokens inside a single hour. His argument is that the interesting axis in generative video stopped being quality a while ago. Put a real time generation next to one that took minutes and the slower clip still has better motion, but it cost on the order of a hundred times more to produce.

Helios, the model he serves, is a distillation of a 14 billion parameter open model, and it is one of at least forty released this year carrying real time or long horizon capability. What that unlocks has less to do with better clips than with a different interaction shape. A webcam that shows you the haircut you are considering. A visual medium for people who do not think in text, which is most of what working with AI currently demands. Content creation that stops being a slot machine where you spend ten dollars a minute on a prompt and some keyframes and hope for the shot. Steering a generation in under a second is a different job entirely. What is left is the serving problem: GPUs positioned globally, WebRTC with ICE and TURN, and several models wired into one continuous streaming pipeline that stays synchronized with user controls frame by frame.

Speaker info:
- https://x.com/keeganmccallum3
- https://linkedin.com/in/keeganmccallum3
- https://urun.sh

Timestamps:
0:00 - Generative video along the quality axis
1:24 - The other axis: efficiency and long horizons
3:23 - What ten dollars of generation buys now
4:38 - Magic mirrors, accessibility, and steering shots live
6:33 - The hard part is serving it

## The Next Game Engine Won't Have a Manual — Arturo Nunez, Nereu

- Upload date: 2026-08-18
- Video: https://www.youtube.com/watch?v=VBCDhRrvlYo
- Transcript: raw/20260818_VBCDhRrvlYo/VBCDhRrvlYo.en-orig.vtt
- Metadata: raw/20260818_VBCDhRrvlYo/VBCDhRrvlYo.info.json

Ask a coding agent for a camera that follows your character and it will reinvent that camera from scratch, every time, slightly differently. Arturo Nunez's diagnosis is that the context sits on the game engine's vocabulary rather than the game's. Controlling a character in a conventional engine means a mesh, a renderer, an animator, a rigid body, a collider, an audio source, and only then your actual movement logic, nearly all of which is boilerplate that every character in every game already carries.

Nereu inverts that. Everything is an asset, and you attach tags describing intent instead of implementation: character, animated, double jump. Systems then query by tag and move everything marked vehicle and drivable, which is Entity Component System thinking lifted from data oriented design. The pleasant consequence is that nothing stops you tagging a building as drivable and dropping it into a Mario Kart style race. The assistant is there to get you unstuck rather than to one shot a finished game, and the vocabulary it expects is the one tutorials already use: press A to jump, press A again in the air.

The engineering detail worth stealing is how context gets assembled. Rather than feed the whole scene to a model, he borrows level of detail from rendering. Assets near whatever you are editing arrive with their full tag values, distant ones collapse to a position and a type, and the hundred pieces of grass are simply left out.

Speaker info:
- https://x.com/arturonereu
- https://www.linkedin.com/in/arturonereu/
- https://www.arturonereu.com/

Timestamps:
0:00 - Building a game live by describing it
2:45 - Why making games is hard
4:27 - Ten years at Unity watching the same struggles repeat
6:59 - Powerful engines and LLMs that still do not compose
7:49 - The boilerplate behind controlling a character
8:45 - Everything is an asset, and tags describe intent
9:37 - The asset tag system, and tagging a building as drivable
11:21 - How the prompt gets its context
14:52 - Level of detail, applied to context assembly
16:37 - Getting unstuck rather than one shotting a game
17:28 - World models are a different medium

## While my guitar gently speaks — Todd Fisher, Philo Ventures

- Upload date: 2026-08-18
- Video: https://www.youtube.com/watch?v=E_Txocq-Lrw
- Transcript: raw/20260818_E_Txocq-Lrw/E_Txocq-Lrw.en-orig.vtt
- Metadata: raw/20260818_E_Txocq-Lrw/E_Txocq-Lrw.info.json

Someone in the audience asked the guitar what reality is, and the guitar answered. Todd Fisher's build routes a microphone through speech recognition into a local model and pushes the reply back out through the strings, which is the most recent step in a project that began with a much simpler question: how hard could it be to make a guitar speak?

The lineage he draws runs from a pickup and an amplifier, through stomp boxes, to Peter Frampton sending guitar sound down a physical hose into his mouth. His own version is a plugin built with JUCE that drops into a DAW like any other effect. Getting it to say one word was straightforward. Getting it to say several meant slicing synthesized speech into words automatically, and that turned out to be the hard part. Energy gap segmentation cuts wherever the signal falls toward silence, which fails because running speech often has no silence between words at all. A sonority peak syllabifier looks for vowels instead. Combining the two got close enough that he finished by dragging segment boundaries by hand. Singing needed a different stack again: the YIN algorithm to pull a fundamental frequency off each fretted note, a synthesized tone shaped by an envelope, then a vocoder, with pitch shifted samples from an open singing dataset baked ahead of time because the processing is far too heavy to run live. He also declines to play the song his title alludes to, on the grounds that this recording was going online.

Speaker info:
- https://www.linkedin.com/in/todd-b-fisher

Timestamps:
0:00 - Live performances that stayed with him
2:44 - The guitar's evolution, up to the talk box
4:24 - A Halloween project on a garage door
6:06 - Building it as a JUCE plugin, and saying one word
7:50 - Slicing speech into words, and why that is hard
10:23 - Pitch detection with the YIN algorithm
11:15 - Synthesis, vocoder, and jamming with it
13:28 - A guitar that answers questions from the room
16:01 - Pitch shifted samples, and getting closer to singing
17:51 - Go build your passion project

## The Next Medium: Why Real-Time Interactive Video Changes Everything — Ahmed Ahres, Reactor

- Upload date: 2026-08-18
- Video: https://www.youtube.com/watch?v=5dCAmSDOAjI
- Transcript: raw/20260818_5dCAmSDOAjI/5dCAmSDOAjI.en-orig.vtt
- Metadata: raw/20260818_5dCAmSDOAjI/5dCAmSDOAjI.info.json

Uber could not exist without GPS. Ahmed Ahres uses that to argue real time is a change of medium rather than a speedup: before GPS you consulted a map somebody else had already made, and afterwards your own position became something you could act on continuously. He runs the same argument through film. Once a viewfinder showed you what you were shooting, you could adjust while shooting, and that is the reason Instagram and TikTok were possible at all.

Generated video today sits on the wrong side of that line. You prompt, you wait, you get a file back, and there is nothing further to do with it. His definition of world models is not Gaussian splatting and not a longer clip, but video that is interactive, effectively infinite, and generated fast enough to steer, which he demonstrates by prompting a cat into a scene while that scene is still generating. What it unlocks divides three ways: control, which he sums up as instant feedback being the ultimate form of it; character driven worlds that reach past games into robotics training data and into education; and live avatars, which he is refreshingly candid are still not working properly. The engineering consequence is that none of the batch playbook carries over. You are streaming pixels rather than returning files, every session is stateful and has to remember what happened when a character looked away, and sub 100 millisecond latency means putting GPUs near users rather than in one region.

Speaker info:
- https://x.com/Boudatw
- https://www.linkedin.com/in/ahmedahres/
- https://www.ahmedahres.com

Timestamps:
0:00 - World models, defined as real time interactive video
1:44 - What happens when video becomes programmable
3:25 - Maps to GPS, and film to viewfinder
5:04 - Model one: infinite, interactive, real time
5:52 - Control, advertising, and instant feedback
7:32 - Model two: controllable worlds, robotics, education
9:13 - Model three: live avatars, not cracked yet
10:06 - What people are actually building on it
12:37 - Why real time infrastructure is not batch infrastructure
16:10 - Evaluation is still an unsolved problem

## Training Krea 2: What matters in generative model training — Sangwu Lee, Krea.ai

- Upload date: 2026-08-18
- Video: https://www.youtube.com/watch?v=-tviRdpmHvs
- Transcript: raw/20260818_-tviRdpmHvs/-tviRdpmHvs.en-orig.vtt
- Metadata: raw/20260818_-tviRdpmHvs/-tviRdpmHvs.info.json

The most reliable way to render a person is to render the most boring average person and put them in the center of the frame. Sangwu Lee offers that as the price the big image models pay for consistency: ask a production model for a burning skull and every output comes back clean, competent, and nearly identical. Krea 2, whose medium variant is now open source, trades the other way, optimizing for fast generation and stylistic range so that a studio that does not yet know what it wants can actually explore.

Most of the talk is about data, which he says twice over is basically everything once the architecture is locked. The examples are specific. A painting photographed on a wall is perfectly good training data except that captioners consistently omit the frame and the white wall behind it, so the model learns to hang every painting it generates. They refuse to train on AI generated images at all, because the aesthetic is sticky and you inherit somebody else's model. Deduplication runs on hashes first across two to ten billion images, then on embeddings for near duplicates. A large vision language model's judgment gets distilled down into a classifier cheap enough to sweep a billion images. Sparse autoencoders double as an unsupervised tagging system for catching watermarks and border artifacts. World knowledge coverage is checked against Wikipedia concepts ranked by PageRank. Thirty to forty in house filters in total.

Speaker info:
- https://github.com/RE-N-Y
- https://re-n-y.github.io/devlog/
- https://github.com/krea-ai/krea-2

Timestamps:
0:00 - Open sourcing Krea 2 medium
1:40 - Consistency versus diversity in production models
3:23 - How diffusion models train, and why latent space
5:59 - Data is basically everything
6:53 - Bad data, and why they refuse AI images
8:34 - The captioning pipeline, and the painting on a white wall
10:15 - Deduplication and cheap classifiers at billion image scale
11:56 - Sparse autoencoders as an unsupervised tagging system
13:39 - Wikipedia PageRank for world knowledge coverage
14:35 - The training pipeline, borrowed wholesale from LLMs
18:54 - What actually mattered for iterating fast
19:46 - The stack is inverting back toward DALL-E 2

## How to Kill the Code Review — Ankit Jain, Aviator

- Upload date: 2026-08-17
- Video: https://www.youtube.com/watch?v=YgEv7IQzGdM
- Transcript: raw/20260817_YgEv7IQzGdM/YgEv7IQzGdM.en-orig.vtt
- Metadata: raw/20260817_YgEv7IQzGdM/YgEv7IQzGdM.info.json

Over 30% of changes now merge with no review at all, and the wait on the ones that do get reviewed is four times what it used to be. Ankit Jain's read is that the debate about when we stop reading code line by line is already over, because we stopped. His sharper point is what replaced it: an AI writes the code, an AI reviews the code, the two go back and forth in a web UI, and a human skims the thread and merges. When AI reviews and nobody reads, he says, we have configured the wrong thing.

He is also here to correct his own five layer trust model from a few months earlier, which missed that review was never only about correctness. It also carries knowledge sharing, mentorship, architectural feedback, and onboarding, and that half has to survive. Spec driven development does not rescue it, because a spec written up front with no feedback loop is the 1970 waterfall model, and the decisions that actually matter end up in the prompts, which teams throw away the moment the pull request opens. His proposal keeps them: capture the session, turn those decisions into acceptance criteria, pair that with a registry built from your own recurring review comments, and generate a test plan that a verification system runs against a live preview. The review surface becomes intent and evidence instead of the diff.

Speaker info:
- https://x.com/ankitxg
- https://www.linkedin.com/in/ankitjaindce/
- https://www.latent.space/p/reviews-dead

Timestamps:
0:00 - The five layer trust model, and what it got wrong
1:17 - We already stopped reviewing, and AI reviews nobody reads
3:05 - What code review was actually for
4:21 - Spec driven development is waterfall again
5:53 - Intent lives in the prompts, which we throw away
6:42 - The AI slop registry
7:58 - Session to acceptance criteria to test plan
11:51 - Deterministic where you can, and reviewing intent not the diff
14:12 - Homework: mine your last 1,000 review comments

## Context Engineering in 2026 — Louis-François Bouchard, Omar Solano & Samridhi Vaid, Towards AI

- Upload date: 2026-08-17
- Video: https://www.youtube.com/watch?v=WP3hjUXd918
- Transcript: raw/20260817_WP3hjUXd918/WP3hjUXd918.en-orig.vtt
- Metadata: raw/20260817_WP3hjUXd918/WP3hjUXd918.info.json

The cheapest configuration they tested was the one sending the most tokens. Across 11 presets run against their open source AI tutor, doing nothing at all to the context beat every compaction technique on recall, cost, and latency at once, and their own production defaults scored worse than leaving the history alone. Prompt caching is why. With 97% of tokens served from cache, and cached tokens up to 50 times cheaper on some APIs, compaction has to shrink a context by more than 50 times before it pays for itself, because rewriting the context invalidates the cache. Louis-François Bouchard's framing is that summarization is potentially a trap.

Omar Solano walks through the architecture and the first run, including a knowledge base browsing tool they built, measured, and found returned identical recall while running 50% slower. Samridhi Vaid extends it: keeping the full history recovered specific details 95% of the time against 32% after summarizing, and distinctive facts survived to 800,000 tokens without visible rot. Hardware changes the answer, though. Capped locally at a 32k window, keeping everything stops being possible, and a larger parameter count does not buy a larger context window. Dense retrieval fell to 0% recall on facts buried at 400k tokens where BM25 still found them every time. The rule they land on is to name the constraint you actually have before reaching for compaction, rather than compacting by default.

Speaker info:
Louis-François Bouchard (Towards AI):
- https://x.com/Whats_AI
- https://www.linkedin.com/in/whats-ai/
- https://www.louisbouchard.ai

Omar Solano (Towards AI):
- https://x.com/omar_solano1
- https://www.linkedin.com/in/omar-solano1

Samridhi Vaid (Towards AI):
- https://x.com/samridhivaid
- https://www.linkedin.com/in/samridhivaid/

Project:
- https://github.com/towardsai/ai-tutor-app

Timestamps:
0:00 - The problem is the context, not the model
1:30 - The AI tutor, and its five requirements
5:21 - Two root problems: a finite window, a stateless model
7:52 - Context rot, cost, and latency
9:13 - The compaction toolkit, with and without an LLM
12:58 - Offloading to files, the LLM wiki, progressive disclosure
16:47 - Prompt caching, and why compaction can backfire
19:20 - When to clear, compact, and optimize for cache hits
21:53 - The tutor's architecture, a single ReAct agent
25:49 - Hybrid search over an 8 million token corpus
28:28 - Letting the agent browse the knowledge base
31:01 - The browse tool measured: same recall, 50% slower
36:23 - The experiment setup: presets, tasks, harness
42:55 - Results: doing nothing wins on all three fronts
48:13 - Should you ever compact?
49:32 - DeepSeek, and a 50 times cache discount
50:53 - Memory: 95% against 32% after summarizing
54:38 - Cost at scale, and going local
57:09 - Local limits: bigger models, same window
58:25 - Where dense retrieval fails and BM25 holds
1:01:01 - What they finally chose

## Security Firewall for Agents — Ryan Dahl, Deno

- Upload date: 2026-08-17
- Video: https://www.youtube.com/watch?v=MkRYPFIMCSA
- Transcript: raw/20260817_MkRYPFIMCSA/MkRYPFIMCSA.en-orig.vtt
- Metadata: raw/20260817_MkRYPFIMCSA/MkRYPFIMCSA.info.json

Deno gives its incident response agents read and write access to production Postgres, Kubernetes, ClickHouse, AWS, GitHub, and Slack, and it works. Agents now close incidents that used to wake a human up. Ryan Dahl's problem is what happens when one of those agents gets prompt injected through the support system it is wired into. He grants that Opus refuses to drop the users table no matter how hard you push it, then says the part that matters out loud: security cannot be wishful thinking that a model stays obedient. The agent is untrusted software, so the guard cannot live inside it.

Claw Patrol is their answer, an MIT licensed proxy that sits in front of the agent and parses every byte leaving it, below the HTTP layer, because the dangerous path frequently is not HTTP. An agent can spawn psql as a subprocess and tunnel to a production database through an EKS endpoint, and no MCP tool definition or HTTP rule will see it. Rules live in HCL, the Terraform configuration language, checked into git and unit tested against fixture requests, with Deno's own file running about a thousand lines. The proxy holds credentials so the agent never sees them, covering cookies, OAuth, and AWS SigV4, and can route an action to an LLM judge, a human in Slack, or both before it is allowed. The demo is Codex in yolo mode cheerfully obeying an order to delete the users table, and the proxy killing it at the Postgres wire protocol.

Speaker info:
- https://x.com/rough__sea
- https://github.com/ry
- https://tinyclouds.org/
- https://deno.com

Timestamps:
0:00 - Deno Deploy, incidents, and the pager
1:28 - Giving agents write access to production
2:47 - Opus refuses, and why that is not enough
3:28 - Prompt injection through the support system
4:05 - Every action is bytes on the wire
5:24 - The hard case: psql through an EKS endpoint
6:47 - Why credentials and ACLs are not sufficient
7:26 - Where MCP tool permissions break down
8:48 - The existing landscape of proxies and sandboxes
10:09 - Claw Patrol
10:50 - Writing rules in HCL
12:07 - Protocol plugins
12:52 - Demo: blocking a dropped users table
13:34 - The dashboard
14:14 - Approvals by LLM judge or by human
14:58 - Credential injection
15:38 - Running it over Tailscale or WireGuard
16:58 - Agents cannot police themselves
17:42 - Q&A: testing the rule file
18:22 - Q&A: does this get easier as models improve

## The Rise of CaaS: Context-as-a-Service for Agentic AI — Omer Primor, Bright Data

- Upload date: 2026-08-14
- Video: https://www.youtube.com/watch?v=Ot4OPrPH4xY
- Transcript: raw/20260814_Ot4OPrPH4xY/Ot4OPrPH4xY.en-orig.vtt
- Metadata: raw/20260814_Ot4OPrPH4xY/Ot4OPrPH4xY.info.json

Just past 15,000 queries, renting context stopped being the cheaper option. Omer Primor gets that number from a small experiment he is careful to call a test rather than a benchmark: enrich one company across 25 fields, run it 100 times against this event's sponsors, and compare AI search products, context as a service vendors, and a scraper pipeline built in roughly a day. Pricing a week of setup at $5,000, the build it yourself path crossed over a little above 15,000 entities, and he expects the real crossover sits lower than most teams assume.

The argument underneath is about frequency rather than volume. Web data decays fast, with social content stale inside a day and news, finance, and retail largely irrelevant after 30 days, so context is never a snapshot you take once. Every repeated query costs what the first one did, even when nothing has changed and the answer comes back identical. What he sees teams do about that is quietly cut scope: check a company weekly instead of daily, take 10 results instead of all of them, skip the question entirely. Owning the pipeline inverts the shape, paying upfront so that retrieval afterwards is effectively free. One result surprised him. The dedicated context vendors scored lower on coverage than general search, because they can only answer from what they already hold, and a question outside that set has no answer at any price.

Speaker info:
- https://www.linkedin.com/in/omer-primor/

Timestamps:
0:00 - Web scale, and the web as context rather than data
2:43 - Data decay, and why context is not a snapshot
3:37 - Search fragments, from Google to the AI search companies
5:42 - What search cannot answer about change over time
6:32 - Context as a service, and the vertical search shape
10:01 - The test: 25 fields, 100 companies
11:04 - Coverage, and why the context vendors placed lower
12:32 - Cost, and frequency as the real killer
15:22 - Cutting corners, renting versus owning
15:59 - Building it yourself in a day
18:34 - The tipping point just above 15,000 queries
21:31 - Owned context compounds, rented context decays

## Computer-use models will agentify the web, not APIs — Dhruv Batra, Yutori

- Upload date: 2026-08-14
- Video: https://www.youtube.com/watch?v=Ki980nV0__0
- Transcript: raw/20260814_Ki980nV0__0/Ki980nV0__0.en-orig.vtt
- Metadata: raw/20260814_Ki980nV0__0/Ki980nV0__0.info.json

To learn what a US school district is buying, you file a Freedom of Information Act request. Someone scans the email you sent, puts the scan on Google Drive, and attaches the relevant PDFs. Dhruv Batra's question is whether anyone seriously expects that office to publish an MCP server. He grants the popular claim that agents will drive most of the action on the web, then rejects its usual next step, that the web will meet them with APIs. The head of the distribution might. The long tail, some 200 million active sites where infrastructure changes over decades, will not.

Reading the HTML instead does not save you, because much of what you see was never written down anywhere. A basketball score is missing from the page that first loads and arrives later as JSON. A product page contains no text reading sold out, only a quantity of zero and a script that grays the option out. State is calculated and rendered rather than stored, which makes the browser closer to a game engine than a document and makes pixels the source of truth. He calls this the bitter lesson for web agents: scaffolding built per site does not generalize, and the general solution is the one the web was actually built for. Their Navigator model runs screenshot in and clicks out, now writes JavaScript when that is quicker, and checks the result on screen. It misses 8 of 300 trajectories on a benchmark he thinks should be retired.

Speaker info:
- https://x.com/DhruvBatra_
- https://www.linkedin.com/in/dhruv-batra-dbatra/
- https://dhruvbatra.com

Timestamps:
0:00 - The argument, and the part of it that is wrong
3:23 - Restaurant menus on easy, medium, and hard mode
5:31 - School district procurement, up to a FOIA request
7:38 - 200 million active sites that change slowly
8:42 - Why reading the HTML does not rescue it
10:14 - Sold out is not text, it is a rendered zero
11:33 - The browser is a rendering engine, pixels are the truth
12:53 - Navigator, and writing JavaScript when that is faster
15:51 - Are computer use models actually good enough
17:20 - Latency and cost per task
18:28 - Another layer of mess that we will call an API

## Bringing agents onto the world wide web — Paul Klein IV, Browserbase

- Upload date: 2026-08-14
- Video: https://www.youtube.com/watch?v=GqoNrUz8hEU
- Transcript: raw/20260814_GqoNrUz8hEU/GqoNrUz8hEU.en-orig.vtt
- Metadata: raw/20260814_GqoNrUz8hEU/GqoNrUz8hEU.info.json

When OpenClaw shipped, people started buying Mac minis to run it from home, SSHing in and clearing captchas off a residential IP. Paul Klein IV points out he has yet to see a SOC 2 compliant Mac Mini setup at scale, and that this felt like a reasonable answer is itself the problem. His argument is that browser agents are no longer held back by the models. The capability is already there and the engineering around it is missing, which makes the overhang something any team can close rather than wait on a lab for.

That engineering has three parts. The most reliable browser agents in production are multimodal and write code alongside clicking, often intercepting network requests and replaying them rather than driving pixels. They carry a real harness, with skills and memory so a site is not rediscovered every run, and with page context compressed rather than dumped whole into the model. And they sit on infrastructure that renders a page identically every time, since a layout that comes back mobile on one run and desktop on the next produces results the agent cannot account for. He then turns to what the web owes agents: accessibility trees, Chrome's new Web MCP, and two unsolved problems, how an agent logs in on your behalf and who certifies that an agent can be trusted. The payoff is not in San Francisco. It is the logistics company in Singapore, the bank in South Africa, and the lumber factory in Mexico, all running on PHP forms with people clicking buttons every day.

Speaker info:
- https://x.com/pk_iv
- https://www.linkedin.com/in/paulkleiniv/
- https://github.com/browserbase/stagehand

Timestamps:
0:00 - Why web agents have not happened yet, and is it the models
3:17 - The missing piece is the harness
4:32 - Harnesses that beat the baseline model
6:01 - The capabilities overhang in computer use
7:05 - Multimodal agents, skills, and token efficiency
9:09 - Infrastructure, and the SOC 2 Mac Mini problem
10:24 - What the web owes agents: accessibility and Web MCP
11:40 - Authentication, trust, and who issues the certificate
14:07 - What a real platform has to provide
15:45 - The real economy runs on PHP forms

## From RL to IRL — Gaurav Mishra, Amazon AGI Lab

- Upload date: 2026-08-14
- Video: https://www.youtube.com/watch?v=Cc0_nyxROBA
- Transcript: raw/20260814_Cc0_nyxROBA/Cc0_nyxROBA.en-orig.vtt
- Metadata: raw/20260814_Cc0_nyxROBA/Cc0_nyxROBA.info.json

Asked to file an expense, the agent gets signed out mid task, reasons that it can infer the password, guesses twice, and locks the account. In a second run it clicks a sponsored button styled like the real submit button, lands on a different site, and begins typing personal details into it. Both are real trajectories from early browser training runs at the Amazon AGI Lab, and Gaurav Mishra's summary is that RL worked while the world was a game, and IRL starts when the game fights back.

The talk catalogues what a reward function meets on contact with a real login screen. Observability is partial, since the DOM misses content baked into images and the screenshot misses whatever needs scrolling. Actions are irreversible, credentials expire mid trajectory, and done routinely does not mean successful. His answer is flight school rather than exams. Sandboxes train on layout shift, slow loads, pop ups, focus stealing, and stale tabs, and recovery becomes a native model action instead of an infra reset, so the agent refreshes, backtracks, waits, or escalates. A process reward model penalizes dangerous steps along the path instead of scoring only the outcome, and calibrated confidence teaches the agent to weigh whether an action is authorized, reversible, and visible before committing. The closing trajectory runs the same task correctly, including the agent refusing to guess the password and handing control back. Over time the model gets better and the harness gets thinner.

Speaker info:
- https://www.linkedin.com/in/gaurav-mishra-b307a437

Timestamps:
0:00 - RL to IRL, and a lightning review of RL for agents
3:26 - Why coding agents can do computer use at all
4:05 - The agent that guesses its own password
5:47 - The sponsored button that looks like submit
6:37 - Partial observability, irreversibility, expiring credentials
8:29 - Flight school, not exams
9:54 - Process rewards and calibrated confidence
11:11 - The pilot and the cockpit
14:07 - Assumption versus reality, point by point
15:11 - The same task, done right

## Computer Use at the Edge of the Statistical Precipice — Pierluca D'Oro, Programma Labs

- Upload date: 2026-08-14
- Video: https://www.youtube.com/watch?v=CTLa_p6iOiY
- Transcript: raw/20260814_CTLa_p6iOiY/CTLa_p6iOiY.en-orig.vtt
- Metadata: raw/20260814_CTLa_p6iOiY/CTLa_p6iOiY.info.json

A script under one megabyte that never looks at the screen matches or beats the frontier model it was copied from. Pierluca D'Oro builds it by recording one successful trajectory per task and then replaying those actions blindly, and on deterministic benchmarks like OSWorld that counts as a valid agent and it scores at the top. The paper goes further and proves that pass@k on a deterministic environment is exactly the success rate of that replay script, so a metric the field leans on turns out to be a formal measure of the exploit.

The fix has two halves. Environments get the PRISM principles: privileged verification, realism, integrity checked configurations, sandboxed execution, and multifactorial variation across data, theme, and starting screen. DIGIWORLD instantiates them in 15 sandboxed mobile apps and 3.2 million verified configurations, generated by a compiler that produces every combination and rejects the broken ones, because a coding agent emitting a lot of software is not the same thing as a good environment. Metrics get honest uncertainty. Naive rollouts on a single base case yield confidence intervals that actually contain the true performance around 20% of the time rather than 95%, and he prices the consequence: a 4% gap between two models, hidden under intervals that look tight, costs hundreds of thousands of dollars a month across a million tasks.

Speaker info:
- https://x.com/proceduralia
- https://www.linkedin.com/in/pierluca-doro/
- https://www.proceduralia.com
- https://arxiv.org/abs/2605.08261

Timestamps:
0:00 - The replay agent, a script that never sees the screen
1:41 - It matches the model it was copied from
2:22 - Why pass@k measures exactly that exploit
3:50 - The PRISM principles for environment design
5:31 - DIGIWORLD, 15 apps and 3.2 million verified configs
7:25 - The compiler that rejects invalid combinations
9:21 - Replay stops working, and frontier models look fragile
11:05 - Two sources of variance, actions and environment
12:31 - Intervals that cover 20% of the time, not 95%
14:56 - A benchmark without rigor is a misleading one

## The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans — Corey Gallon, Rexmore

- Upload date: 2026-08-14
- Video: https://www.youtube.com/watch?v=26RtyAm9y_Q
- Transcript: raw/20260814_26RtyAm9y_Q/26RtyAm9y_Q.en-orig.vtt
- Metadata: raw/20260814_26RtyAm9y_Q/26RtyAm9y_Q.info.json

Preparing this talk got Corey Gallon a warning from OpenAI that his account faced a ban for cyber abuse with a web browser. The offending work was an agent clearing Cloudflare Turnstile, two image captchas, and finally reCAPTCHA v2 with no human in the loop. His premise fits on one slide: a browser driven through the Chrome DevTools Protocol is just a meat bag with a mouse, because the agent's clicks and keystrokes travel the same path inside Chrome that yours do. Chrome stamps every event as trusted or untrusted, which is why a synthetic JavaScript click that works fine in Outlook gets silently dropped by Amazon's add to cart button.

The method is a loop of sense, act, verify, climbed up a three rung ladder only as high as the page forces. A synthetic click first, then a real CDP input event, then a human mouse path with jitter and a deliberate overshoot. He argues for a CLI over an MCP server on speed rather than capability, citing a study where both cleared tasks about 83% of the time while MCP took 71 round trips and eight minutes against seven turns and under a minute. That gap decides the last fight, because reCAPTCHA rounds expire on a clock. His solution splits the work: deterministic code drives the whole challenge and rearms itself, and the agent is called in only to look at the grid and name the tiles. Everything demonstrated runs on infrastructure and accounts he owns.

Speaker info:
- https://x.com/coreygallon
- https://www.linkedin.com/in/coreygallon
- https://gallon.me
- https://github.com/captivus/chrome-agent

Timestamps:
0:00 - Threatened with a ban for preparing this talk
1:50 - The premise: a CDP browser is a meat bag with a mouse
2:43 - Why a CLI beats an MCP server
4:06 - The DevTools Protocol and the agent's digital senses
5:47 - The loop: sense, act, verify
6:38 - The three rung ladder
8:27 - Rung one: batch emails, and the web UI as a permissionless API
10:44 - Rung two: trusted clicks and the add to cart button
12:51 - Rung three: Cloudflare Turnstile
14:26 - Image captchas, drag puzzles, and human motion
16:36 - Final boss: reCAPTCHA v2, solver and operator
19:47 - The methodology is the takeaway

## How Web Data Infrastructure Powers the Next Generation of AI — Patricija Žemaitytė, Oxylabs

- Upload date: 2026-08-14
- Video: https://www.youtube.com/watch?v=1UmZHb_E_SM
- Transcript: raw/20260814_1UmZHb_E_SM/1UmZHb_E_SM.en-orig.vtt
- Metadata: raw/20260814_1UmZHb_E_SM/1UmZHb_E_SM.info.json

Minutes into a call to demo a search API rebuilt to answer in under a second, the system got blocked, badly, in front of the client. Patricija Žemaitytė treats that as the useful distinction: something that works in development, something that passes tests, and something that survives reality are three different systems. The rebuild had no trick to it. Browsers are slow, expensive, and incompatible with low latency, and they were unavoidable, so the team went hunting for time across layouts, parsers, sessions, and proxies until the seconds were gone. It averages 550 milliseconds now, against a 4 second baseline.

Two other stories run the same way. A video API request arrived with a two week deadline and a floor of 5 petabytes a month, then kept moving. The transcripts the client asked for turned out to be subtitles, then came search, then metadata, until a one off feature request had quietly become a product suite. The punchline she offers is that the client has since collected 30 petabytes and has not paid yet. Scaling the unblocker from 10,000 to 60,000 requests per second hit a wall around 20,000 in load testing, where the real difficulty was not generating synthetic traffic but knowing whether the number meant anything, since telemetry at that volume becomes part of the load it measures. Project 60 is already Project 150. Her argument throughout is that this is not a build once business, it is an adapt forever one.

Speaker info:
- https://www.linkedin.com/in/patricijazemaityte
- https://oxylabs.io/press-area/from-web-to-artificial-intelligence

Timestamps:
0:00 - Infrastructure, not models, as the starting point
2:23 - A video API with a two week deadline
4:08 - Transcripts, subtitles, search, metadata
5:51 - Thirty petabytes later, still unpaid
7:25 - A subsecond request, built and then shelved
8:42 - The rebuild, and getting blocked live on the call
10:53 - Hunting for time, second by second
12:26 - Scaling the unblocker to 60,000 per second
14:09 - Load testing, and the wall at 20,000
15:31 - Project 60 becomes Project 150

## Scaling up Continual Learning — Ronak Malde, Trajectory

- Upload date: 2026-08-12
- Video: https://www.youtube.com/watch?v=zL1kLftVTlo
- Transcript: raw/20260812_zL1kLftVTlo/zL1kLftVTlo.en-orig.vtt
- Metadata: raw/20260812_zL1kLftVTlo/zL1kLftVTlo.info.json

Scale on policy self distillation to trajectories with a hundred tool calls and the model collapses into hedging. The tokens it learns to favor fill up with wait, but, and maybe, until, as Ronak Malde puts it, everything just turns into maybe. He calls it the but wait problem, and it happens because the student drifts far enough on a long task that the teacher course corrects at every opportunity, leaving the model parked between two divergent distributions.

The algorithm underneath is a good trick. At the frontier there is no smarter model to distill from, so you make the model its own teacher: put privileged information, a hint, in the teacher's prompt, and match the log probs of the student that never saw it. Malde scores post training methods against four properties, an online task distribution, on policy sampling, no parallel rollouts, and a per token reward, and shows SFT, RLHF, and GRPO each buying some at the cost of others. GRPO gets on policy sampling but explodes parallelism and collapses feedback into one sequence level score, which he compares to being handed 87 out of 100 on an essay and told to work out why. Self distillation gets all four, and it optimizes across the entire vocabulary at every token instead of sharpening the one that was sampled, which is why it keeps climbing past where GRPO plateaus while tokens to solve go down rather than up. The failure modes are the useful part: step level KL weighting to handle divergence, and residual guidance for hint leakage, the self distillation analogue of reward hacking, where a hint containing the answer teaches the model to state it and back fill the reasoning afterward.

Speaker info:
- https://x.com/rronak_
- https://www.linkedin.com/in/ronak-malde

Timestamps:
0:00 - From Windsurf to Trajectory
1:05 - Benchmarks are saturating and getting expensive
1:58 - The signal we throw away every day
2:51 - Four things a training algorithm should have
3:42 - SFT, and what it got right
4:31 - DPO and RLHF
5:22 - GRPO and the Faustian bargain
6:15 - How GRPO actually works
7:04 - Scored 87 out of 100 and told to figure it out
7:52 - Distillation, then on policy distillation
8:43 - Self distillation: make the model its own teacher
10:21 - Optimizing the whole vocabulary, not the top token
11:11 - Results on short horizon tasks
12:52 - What breaks at 120B and a hundred tool calls
13:41 - The but wait problem
14:31 - Step level divergence weighting
16:11 - Hint leakage, the new reward hacking
17:51 - Residual guidance
19:35 - All four properties, finally
20:25 - What Trajectory is building
21:16 - Q&A: how continual is continual learning
22:08 - Q&A: model and harness improving together

## Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop

- Upload date: 2026-08-12
- Video: https://www.youtube.com/watch?v=jHMiYtjoJfA
- Transcript: raw/20260812_jHMiYtjoJfA/jHMiYtjoJfA.en-orig.vtt
- Metadata: raw/20260812_jHMiYtjoJfA/jHMiYtjoJfA.info.json

Build the thousand example eval suite everyone tells you to build, switch harnesses, and 80% of it stops meaning anything. Ben Hylak's complaint is that eval advice is still written for the chatbot era, back when you knew the answer to nearly every question a user would ask. His reframing is that the useful question is not what issues your agent has, since it will have effectively infinite issues, but which ones matter. That turns on the gap between your ceiling, the most impressive thing your agent can do, and your floor, the worst. The floor is what breaks trust: recommending a competitor, deleting data, sending slop to a customer because the agent happened to have email access.

The practical core is two numbers per issue, when it started and what share of users it hits. Learning that something began yesterday is what makes you ask what changed. Learning it hit three users rather than a hundred thousand is what tells you whether to care at all. From there he offers three findings from running this at Raindrop. Clustering traces is not issue detection, because boundaries drift, you do not control them, and what counts as one issue is specific to your product, so a cluster called price issues quietly merges a wrong quote with a wrong refund that have nothing in common. Code mode scales to traces, meaning you write classifiers and run them in a sandbox at production volume. And agents are poor at finding anomalies while being good at investigating them, so surface something deterministic like a keyword spike first and hand them that. Underneath all of it is the argument that evals now belong in your repo as tests rather than in a prompt playground, because the harness is the product.

Speaker info:
- https://x.com/benhylak
- https://www.linkedin.com/in/benhylak/

Timestamps:
0:00 - Raising the floor, and how little continual learning is real
2:07 - What agents looked like a year ago
3:23 - Why agent creativity cuts both ways
4:01 - Eval advice stuck in the chatbot era
4:38 - Switch harnesses and 80% of your evals break
5:16 - Safety without theater
5:57 - What Raindrop sees in production
7:12 - The real question: how do you make it better
8:26 - Benchmark maxer or floor raiser
9:05 - Why labs and companies have different jobs
9:42 - How much responsibility sits with the user
10:56 - Ceiling against floor, and which breaks trust
11:35 - Offline evals should look like tests
12:52 - Keep evals as code
13:30 - Two things you must know about every issue
14:45 - How many users do you actually have
16:02 - Lesson one: clusters are not issues
17:17 - Why cluster boundaries fail you
18:35 - Lesson two: code mode scales to traces
19:14 - Lesson three: agents cannot spot anomalies

## Beyond Static Intelligence: Evaluating Continual Learning — Parth Asawa, UC Berkeley

- Upload date: 2026-08-12
- Video: https://www.youtube.com/watch?v=iqloyWCGYQQ
- Transcript: raw/20260812_iqloyWCGYQQ/iqloyWCGYQQ.en-orig.vtt
- Metadata: raw/20260812_iqloyWCGYQQ/iqloyWCGYQQ.info.json

Every leaderboard you have seen was built by asking a model to do one task, wiping its memory, and asking it another. Parth Asawa's objection is that this quietly assumes learning across instances does not count. His benchmark measures what that assumption hides, using a metric called gain: run a system with state, then run the identical system reset between every single instance, and take the difference. Cumulative reward cannot show you this, because a stronger base model can post a higher total while learning less than a weaker one that genuinely improves.

Building tasks that can measure learning turns out to be the hard part, and he sets three requirements. Headroom, so the task is not already solved by pretraining. Shared latent structure across instances, since standard benchmarks are deliberately independent and therefore offer nothing to improve on, which is why chaining existing benchmarks together does not work. And a learning signal in the environment, whether reward, error messages, or plain text. Continual Learning Bench 1.0 spans six domains including database exploration, where a system should need fewer SQL queries by the tenth question, after which a schema migration tests whether it can throw away stale knowledge without throwing away the useful kind. The headline result is uncomfortable: plain in context learning tops the leaderboard, beating the more elaborate context management systems on reward, on gain, and on cost. Failure modes land on either side of stability and plasticity, including a forecasting model that overpredicts, is corrected, underpredicts, is corrected again, and then jumps straight back to its original overprediction instead of splitting the difference.

Speaker info:
- https://x.com/pgasawa
- https://www.linkedin.com/in/pgasawa/
- https://pgasawa.github.io/

Timestamps:
0:00 - How we evaluate models today
1:28 - Imagine forgetting everything after every task
2:05 - What continual learning actually means
2:42 - In context, external memory, or parametric
3:18 - The case that we are not measuring it at all
3:58 - What the existing literature does
4:37 - Why those evaluations are not enough
5:13 - Why you cannot chain existing benchmarks
5:51 - Design criterion one: headroom
7:06 - Shared structure and a learning mechanism
7:42 - Reward, and why cumulative reward misleads
8:58 - Gain: the same system with memory wiped
10:15 - Isolating learning from base capability
10:54 - The database exploration task
12:06 - Adding concept drift with a migration
13:20 - Six domains in the benchmark
13:57 - Results, and the in context learning surprise
15:12 - Failure modes on stability and plasticity
15:51 - A forecast that forgets its own correction
16:28 - A notepad that refuses to update
17:07 - Why the training stack was never built for this
17:47 - The sunk cost fallacy in continual learning
19:02 - Rethinking third party AI research
19:38 - Roadmap

## Bringing Continual Learning into Enterprises — Samuel Denton, Applied Compute

- Upload date: 2026-08-12
- Video: https://www.youtube.com/watch?v=ZTA0GwpAUak
- Transcript: raw/20260812_ZTA0GwpAUak/ZTA0GwpAUak.en-orig.vtt
- Metadata: raw/20260812_ZTA0GwpAUak/ZTA0GwpAUak.info.json

A Qwen thinking model was taking up to 80 turns to submit on SWE bench. Applied Compute wanted it wrapping up by turn 40 and got the submit tool call rate from 22% to 60% with test pass rate flat. The interesting part is the mechanism: because the rollout was conditioned on an old production trace that never called the tool, the teacher never touched the tool call tokens at all. It moved the reasoning path toward the call instead, and the call followed.

Sam Denton's frame is a grid. One axis is how online the traces are, from a single dump of production traces to a unified engine where serving and training are the same loop. The other is where the hint comes from, either static priors, such as knowing a support agent is too quick to refund, or a hint built dynamically from what the on policy model just did. Applied Compute works two corners of that grid. Offline hints on offline traces need no replayable environment and can improve an enterprise agent from a data dump on day one. Online hints on online traces have the far higher ceiling, and that is what fixed a customer whose harness required unusual hyperlink formatting: rewarding the format directly and finetuning on correct examples both degraded coding ability, while a hint written against each rollout took correct formatting from 15% to 80%. Two things he says make it work in practice. Let a judge pick where in the rollout the hint goes and distill only the next few steps, since the learning signal decays with distance from the hint. And mask which tokens you learn from, because the teacher has strong opinions about connector words that have nothing to do with the lesson. Throughout, the constraint he keeps is doing all of this without a golden answer to distill toward.

Speaker info:
- https://x.com/samueldenton
- https://www.linkedin.com/in/sam-denton-161b50126/

Timestamps:
0:00 - The distillation spectrum, offline to online
2:46 - The holy grail: serving and training as one loop
4:00 - Where the hint comes from
4:42 - Online hints built from the rollout
5:19 - Four quadrants of distillation
7:50 - The two corners they actually work in
9:44 - Improve for free today, raise ceilings tomorrow
10:22 - Doing it without a golden answer
11:00 - SWE bench: wrapping up by turn 40
11:38 - The three metrics that matter
12:17 - What the hint actually says
12:55 - Moving the reasoning path, not the tool call
13:36 - Adding a single on policy step
14:17 - The hyperlink formatting problem
14:56 - Why rewards and finetuning both failed
15:34 - From 15% to 80% with online hints
16:13 - Per step hinting
16:50 - Why the signal decays with distance
17:27 - Relevance masked self distillation
18:07 - What it adds up to

## Adaption Labs: Gradient-Free Continual Learning — Sara Hooker, Adaption

- Upload date: 2026-08-12
- Video: https://www.youtube.com/watch?v=XEd_SRVHBgU
- Transcript: raw/20260812_XEd_SRVHBgU/XEd_SRVHBgU.en-orig.vtt
- Metadata: raw/20260812_XEd_SRVHBgU/XEd_SRVHBgU.info.json

Fewer than five thousand people in the world know how to train a frontier model at scale, by Sara Hooker's estimate, and that knowledge travels like an apprenticeship rather than a literature. Modern computer science is 77 years old, two generations, and in that time the route to contributing at the frontier narrowed into one funnel: the right PhD, the right industry lab, the right problem at the right moment. She calls it the unreasonably narrow path, and notes it got compounded in this field by compute, so that a handful of labs build what everyone else uses and whole regions of the world appear nowhere on the map of where breakthroughs happen.

Her case that the funnel is about to widen rests on two things. AutoScientist automates the training of models, optimizing the whole loop together from data through alignment and evolving itself per domain, and it beats research staff partly because people carry priors about particular architectures while the search ranges across sizes and across dense and mixture of experts designs. It only started paying off once they controlled data quality alongside the model rather than leaving that to the agent. One nice piece of honesty: the win rates all sit just above 60% because the budget was set to stop there, and lifting that ceiling let them keep climbing. The second reason is her slow death of scaling argument, that pretraining size is no longer the most rewarding axis. That matters for access, because pretraining compute has to be colocated and enormous while the compute that now pays off is distributable. If no lab is going to quadruple model size again on this architecture, recipes and algorithms start to matter more than hoarded GPUs.

Speaker info:
- https://x.com/sarahookr
- https://www.linkedin.com/in/sararosehooker/
- https://www.sarahooker.me/

Timestamps:
0:00 - Seventy seven years of computer science
1:15 - From gentleman scientists to professional labs
1:56 - The unreasonably narrow path
3:13 - GPU poor and GPU rich
3:52 - Where breakthroughs come from, and where they do not
4:30 - Why we are ripe for a revolution
5:08 - AutoScientist
5:47 - Why it beats research staff
6:24 - It only worked once they controlled the data
7:02 - The 60% that was a budget stop
7:41 - Where the demand is: medical, legal, science, code
8:59 - Languages from day one, and non verifiable tasks
10:16 - The compute problem that would undo all this
10:53 - The slow death of scaling
11:31 - Smaller models overtaking larger ones
12:09 - A broader action space, and why that opens the field
12:47 - Q&A begins
14:06 - Fewer than five thousand people
14:43 - Why the cost of asking shapes what gets asked
15:57 - Q&A: the safety objection to open frontier AI
17:10 - Q&A: parametric against nonparametric storage
18:28 - Q&A: are large models still needed for distillation
19:04 - Why this architecture has hit its size ceiling

## Scaling Compute on Context — Jack Morris, Engram

- Upload date: 2026-08-12
- Video: https://www.youtube.com/watch?v=WiqDvX6isc4
- Transcript: raw/20260812_WiqDvX6isc4/WiqDvX6isc4.en-orig.vtt
- Metadata: raw/20260812_WiqDvX6isc4/WiqDvX6isc4.info.json

Train a model directly on ten thousand financial reports and you can drive the loss to 0.00001. It knows the documents perfectly. Then you generate from it and it collapses. Jack Morris uses that failure to set up the real problem. The three axes that powered the entire deep learning revolution, more data, more compute, bigger models, all run on public data. Models are superb on Wikipedia, arXiv, and GitHub, and know nothing about your emails, your meetings, or your company. Against your own corpus the data axis is fixed and training from scratch is off the table, which leaves compute as the only axis you can still push, and that is what he means by scaling compute on context.

The rest is a tour of what people try and exactly where each one stops. KV compaction only reaches what already fits in context and skips the gradients entirely. On policy distillation works, but raises the question of what you distill, since raw documents will not do, which is the gap self study in the cartridges paper is aimed at. Continued pretraining on synthetic data conditioned on your corpus is promising, but it overwrites some of the pretraining and assumes you have a base model rather than the post trained one most people actually start from. Every approach shares a ceiling: you define a dataset, you train, and unless the model is underparameterized it eventually absorbs everything you made. A synthetic data wall, with none of pretraining's scaling behavior. The property he wants is the one that made AlphaGo work, where getting better makes the training questions harder, so that adding compute keeps buying depth instead of flattening out.

Speaker info:
- https://x.com/jxmnop
- https://jxmo.io
- https://substack.com/@jxmnop

Timestamps:
0:00 - Scaling compute on context, and Engram
1:28 - Terence Tao on breadth against depth
2:43 - What models cannot know after training
3:22 - Long tail skills and AMD kernels
3:59 - Why a model knows nothing about you
4:37 - The many names for this problem
5:14 - Three axes of scaling
5:52 - Even post training data is public by definition
6:30 - Applying scale to your data
7:45 - Why compute is the only axis left
8:21 - The data budget is less fixed than it looks
9:40 - Stating the problem properly
10:55 - Just train on it, and why that fails
11:34 - Perfect loss, collapsed generation
12:13 - Making the model think the data is in context
12:52 - KV compaction
13:31 - On policy distillation and what to distill
14:46 - Simulating pretraining with synthetic data
16:00 - Unsupervised RL environments
16:38 - The synthetic data wall
17:54 - Self improvement, and what AlphaGo had
18:33 - The curve they are chasing

## Memory Harnesses for Long-Running Research Agents — Stefania Druga, Sakana.ai

- Upload date: 2026-08-12
- Video: https://www.youtube.com/watch?v=R3-anFK1YM8
- Transcript: raw/20260812_R3-anFK1YM8/R3-anFK1YM8.en-orig.vtt
- Metadata: raw/20260812_R3-anFK1YM8/R3-anFK1YM8.info.json

On a literature review task where every paper already fit inside the context window, adding a memory harness changed nothing: the same accuracy, at higher cost. That negative result is the most useful thing in Stefania Druga's experiment, because it marks the boundary. Move to a long horizon task where the answer sits at step 124 and the question arrives at step 500, far outside the window, and the harness becomes the entire game.

Her framing is that memory is a write, manage, read control loop wrapped around the model, not a database you attach to it. She held the model fixed and varied only the recall policy across a ladder: no recall at all, vector RAG, a decisions ledger that tracks and prioritizes what was decided each turn, and an oracle handed the correct memory outright. Across 68 xbench questions the ranked ledger won, beating even the approach of gating the harness on whether memory seemed necessary. The oracle pointedly does not reach the ceiling, because giving a model the right memory does not make it use the right memory. Ranked recall was also cheaper, which is the line worth keeping: bad memory is expensive, since it burns tokens and sends the agent the wrong way. The whole thing runs on a local M3 Ultra in Tokyo that she is driving from her phone, with fans stacked around it because the evals have not stopped.

Speaker info:
- https://x.com/Stefania_druga
- https://www.linkedin.com/in/drugastefania/
- https://stefania11.github.io/

Timestamps:
0:00 - Context rot on long horizon tasks
1:04 - Longer tasks, fewer model releases
1:56 - Cutting spend by moving work local
2:24 - Local models crossing the usefulness line
2:50 - The machine in Tokyo, and the fans
3:44 - Memory as a write, manage, read loop
4:11 - The harness: core, recall, archival
4:36 - The recall ladder, from nothing to an oracle
5:27 - Task one: a retracted claim in a literature review
6:19 - When everything fits, memory only adds cost
6:47 - Task two: an answer 376 steps out of reach
8:08 - Results across 68 questions
8:35 - Why the oracle does not reach the ceiling
8:59 - Ablations, and generalizing across models
9:49 - Bad memory is expensive
10:16 - Treat recall policy as a first class metric
11:07 - The wider memory landscape
11:33 - What running locally bought her
12:29 - Sovereign AI at Sakana

## Intelligence + Continual Learning = Expertise — Yu Su, NeoCognition

- Upload date: 2026-08-12
- Video: https://www.youtube.com/watch?v=I6aiEf3aEFQ
- Transcript: raw/20260812_I6aiEf3aEFQ/I6aiEf3aEFQ.en-orig.vtt
- Metadata: raw/20260812_I6aiEf3aEFQ/I6aiEf3aEFQ.info.json

Scheduling a meeting is not finding a shared slot on everyone's calendar. It is a constraint optimization over authority, priority, and urgency, and an expert sees that immediately where a very capable model does not. Yu Su uses examples like that one to separate two things the field keeps collapsing together. Intelligence is reasoning through an unfamiliar problem from the context you were handed, which frontier models keep getting better at and where each episode stands alone. Expertise is accumulated, situated competence, and almost nobody is scaling it.

His account of why coding agents work while everything else stays brittle is a modern Moravec's paradox. Code is already a language native world, symbolic and structured, with tests standing in for rewards. The rest of digital work is millions of micro worlds, each with its own local physics, far too heterogeneous for one static model to compress. The slide he calls the most important plots raw intelligence against expertise and finds them roughly orthogonal: scale intelligence alone and you get what he calls the world's smartest novice, brilliant at whatever is put in front of it and accumulating nothing between problems. Intelligence expands the search, spinning up a hundred parallel attempts. Expertise compresses it, because the shortcuts are already learned. The provocation he leaves is unbounded expertise from bounded intelligence: if continual learning gets good enough past some threshold of raw capability, the thing worth scaling stops being the model.

Speaker info:
- https://x.com/ysu_nlp
- https://www.linkedin.com/in/ysu1989/
- https://ysu1989.github.io/

Timestamps:
0:00 - Why coding agents work and little else does
1:30 - Agents before language models
2:06 - What multimodal language agents changed
3:26 - Why code was the ideal first market
4:06 - Leaving the privileged world of code
4:46 - A modern Moravec's paradox
5:25 - Millions of micro worlds, each with local physics
6:44 - Defining intelligence
7:20 - Defining expertise
8:00 - Experts see differently, not just more
8:39 - Conditionality, judgment, and knowing when to stop
9:53 - Expanding the search against compressing it
10:32 - Continual learning as the bridge
11:08 - Four parts of a working definition
13:10 - The world's smartest novice
14:32 - Unbounded expertise from bounded intelligence
15:51 - Reliability against plasticity
16:32 - Parametric and nonparametric learning together
17:08 - Specialization as the next data opportunity
17:53 - Making expertise abundant

## LLM Knowledge Bases: a practical guide — Ben Holmes, Warp

- Upload date: 2026-08-12
- Video: https://www.youtube.com/watch?v=I3bpdgFJCUY
- Transcript: raw/20260812_I3bpdgFJCUY/I3bpdgFJCUY.en-orig.vtt
- Metadata: raw/20260812_I3bpdgFJCUY/I3bpdgFJCUY.info.json

Talking runs about 200 words a minute and typing does not, which is why Ben Holmes starts a knowledge base with voice dictation rather than with organization. The pipeline only works if there is enough raw material, so the capture step is deliberately sloppy: ramble into your phone after a podcast or a meeting, skip the formatting, and let agents impose structure afterward. He points at Handy and Voice Ink as local, on device options, so none of it needs a subscription.

Structure then arrives in passes. An enrich note skill stamps each file with a timestamp so later runs know what has been processed, assigns tags from a fixed reference list instead of inventing new ones, since as he puts it Claude loves to get creative, researches the source on the web, and adds backlinks found by key term search. On top of that pile, a wiki generated from a Karpathy gist produces browsable entries for the people, concepts, organizations, and sources buried in your own notes. Then the whole thing runs on a schedule in a cloud sandbox: the Obsidian headless CLI syncs the markdown down, the agent enriches whatever is not yet stamped, and it syncs back, so you wake up to a refreshed wiki he describes as the daily paper except it is yours. The closing trick is a graph view of every note, built in HTML and Tailwind purely by asking an agent for it, which turns out to be a decent map of where your own thinking has gaps.

Speaker info:
- https://x.com/bholmesdev
- https://bholmes.dev
- https://linkedin.com/in/bholmesdev

Timestamps:
0:00 - The disorganized notes folder problem
1:30 - Where we are going: raw notes to a browsable wiki
2:46 - Getting raw thoughts down is the hard part
3:25 - Why dictation beats typing
4:02 - Local voice tools that need no subscription
5:17 - Be scrappy, you need volume
5:53 - What an enriched note looks like
6:32 - The enrich note skill
7:11 - Tagging from a fixed list, not inventing new ones
7:49 - Running the skill
9:07 - Following your own rabbit holes
9:45 - Generating a wiki over the notes
11:40 - The Karpathy gist behind the idea
12:54 - Wikis for work: people, meetings, sources
13:31 - Making it run without you
14:10 - Local automations against cloud ones
15:29 - Syncing markdown into a sandbox and back
16:45 - Waking up to a fresh wiki
18:01 - Visualizing the whole notebook
18:39 - A graph view built by asking for it
19:17 - Finding the gaps in your own thinking
20:30 - Tools mentioned

## Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain

- Upload date: 2026-08-12
- Video: https://www.youtube.com/watch?v=CvRngaQZQ3Y
- Transcript: raw/20260812_CvRngaQZQ3Y/CvRngaQZQ3Y.en-orig.vtt
- Metadata: raw/20260812_CvRngaQZQ3Y/CvRngaQZQ3Y.info.json

Does your agent get dumber after the first compaction? After the second? You cannot read that off the code, only off the traces, and there are far too many to read yourself. So LangChain points agents at the traces of other agents and asks exactly that, alongside questions like where users got upset and what a different model would have done at the same step. Vivek Trivedy's argument is that observability and continual learning are the same problem in different clothing, because an agent acting in an environment produces the only real record of what happened, and that record is the substrate everything else is built on.

The economics fall out of reading it. Working with Harvey on a legal benchmark, they found an open model could match their frontier model's trace judging at one to two orders of magnitude lower cost, arrived at through harness engineering that the traces themselves pointed to. His rule for when to stop tuning prompts and start finetuning is speed of feedback: harness engineering answers in about two minutes, so you exhaust that ceiling first, finetune to break through it, then return to harness engineering. He also argues that dense feedback is what agents lack most, since a benchmark returning only pass or fail gives an agent nothing to act on, while traces already hold the fine grained signal. The claim worth arguing with is that you can describe an agent's behavior just by showing the evals it was measured against, because those are what it hill climbs.

Speaker info:
- https://x.com/Vtrivedy10
- https://www.linkedin.com/in/vivek-trivedy-433509134/
- https://www.vtrivedy.com/

Timestamps:
0:00 - My agent made mistakes, now what
1:28 - Ship it, collect traces, mine them
2:44 - Observability and continual learning are the same problem
4:00 - Why agents are harder to reason about than code
4:36 - Trading determinism for autonomy
5:15 - Sending agents to read other agents' traces
6:29 - Today's data is the least we will ever have
7:09 - When a trace no longer fits in context
7:48 - Not reaching for a frontier model every time
8:24 - Matching frontier trace judging with an open model
9:02 - Where harness engineering stops paying
9:40 - Finetuning on a narrow vertical
10:17 - Trading token costs for hardware costs
11:34 - Distillation from your own good traces
12:10 - Evals as a description of behavior
12:48 - What scikit learn has to do with any of this
13:28 - Model, harness, task fit
14:07 - Finding fit functions and finding data
15:24 - Why dense feedback matters
16:01 - Harness engineer, finetune, harness engineer again
17:22 - Updating agent state across three axes
18:39 - Sleep time compute and memory that is not append only
19:17 - Takeaways

## Lessons from Studying Every Memory System — Shlok Khemani, Independent

- Upload date: 2026-08-12
- Video: https://www.youtube.com/watch?v=5ZGyKWjQDr0
- Transcript: raw/20260812_5ZGyKWjQDr0/5ZGyKWjQDr0.en-orig.vtt
- Metadata: raw/20260812_5ZGyKWjQDr0/5ZGyKWjQDr0.info.json

A profile ChatGPT keeps on Shlok Khemani says he travelled to Turkey in 2025. He never has. The memory came from conversations where he was choosing between Turkey and Thailand, he went to Thailand, and the profile kept both with overlapping dates. What bothers him is not the mistake but the incuriosity: nothing notices the conflict, and the evidence to settle it was sitting in his email as flight and hotel bookings. He calls that a product problem, not a technology one.

The rest is a year of reverse engineering how consumer memory systems are built, all of it his reading from the outside rather than anything documented. By his account ChatGPT went from a user managed list of facts to a running profile rebuilt in the background, roughly 4,000 tokens of dense keyword clues he could only inspect by jailbreaking his way to it. Claude started opposite, with no profile and two retrieval tools over past conversations, then added one about a quarter the size, in full sentences, refreshed daily and visible in settings. His frame for the difference is that memory is a function of compute: a profile costs to maintain and costs again in every context window it enters, so a large profile updated rarely and a small one updated daily are two answers to one budget question.

Speaker info:
- https://x.com/shloked
- https://www.linkedin.com/in/shlokkhemani/
- https://shloked.com

Timestamps:
0:00 - What memory means here: consumer personalization
2:09 - ChatGPT memory v1, a list of facts
4:08 - The running profile arrives
6:04 - The trip that never happened
6:45 - A profile you cannot look at
7:23 - Claude's first version, tools instead of a profile
8:03 - Publishing that they were opposites
9:18 - Three years of convergence
11:14 - There is no single way to do memory
12:30 - Memory is a function of compute
13:47 - Continual learning is already here
15:39 - The context problem no architecture solves
17:34 - Products that each know you separately

## Agents, codebases, and teams — Aditya Khandelwal, Amazon AGI Lab

- Upload date: 2026-08-11
- Video: https://www.youtube.com/watch?v=aeTb5BdmTTc
- Transcript: raw/20260811_aeTb5BdmTTc/aeTb5BdmTTc.en-orig.vtt
- Metadata: raw/20260811_aeTb5BdmTTc/aeTb5BdmTTc.info.json

Leave agent adoption to individuals and the engineer shipping two PRs a day ends up reviewing the ten that the early adopter ships. They fall further behind, the code they are reading is worse, and they conclude the agents are the problem. Aditya Khandelwal's argument, from leading a team of ten through this, is that adoption is therefore a leadership problem and not an IC one, because the changes that actually work, restructuring a codebase for progressive disclosure and converging on a shared setup, are not changes one engineer can make alone.

The symptoms of a bad setup are specific. Engineers babysit runs. A simple task burns through 500k of context and hits auto compaction. Someone says the model got dumb today, when the model did not change and the harness did. Their fix centered on one high value skill, called ship it, that carries a change from code done to PR ready, handling the description, the review comments, and CI failures, and often runs for over an hour. That duration scared people until they saw what it bought them. Around it they wired issues and boards into the repo, agentic reviews, and a code gardener that runs nightly. It was not clean: agents filing against each other took the repo to roughly 4,500 open issues in a couple of weeks. Stay for the Q&A, which lands a hard limit near 100 lines in a skill file and offers first prompt context burn as the test of whether progressive disclosure is actually working.

Speaker info:
- https://www.linkedin.com/in/aditya-khandelwal/
- https://github.com/adityak6798
- https://adityak6798.github.io/

Timestamps:
0:00 - Why solo agent advice breaks on a team
1:30 - The adoption journey, from mandates to slop
2:10 - Fear against confidence, the two axes
4:02 - Is a CLAUDE.md and some skills enough
4:38 - Symptoms that your setup is wrong
5:52 - Why this is leadership's job, not an IC's
6:31 - The review burden trap
7:09 - Harness engineering principles
7:45 - Smart prompt injection
8:25 - Close the loop and keep iterating
9:08 - The playbook: start with the basics
9:47 - Ship it, the one high value skill
11:02 - Winning over the skeptics
12:18 - What went wrong along the way
12:57 - Let prototypes opt out of the standards
13:34 - Stop saying the model is dumb
14:10 - Commit to the turn
14:47 - Q&A: strategies for progressive disclosure
16:03 - Measuring context burn on the first prompt

## Anthropic's Applied AI team on the Evolution of Agentic Surfaces

- Upload date: 2026-08-11
- Video: https://www.youtube.com/watch?v=K0X9QDRkIdg
- Transcript: raw/20260811_K0X9QDRkIdg/K0X9QDRkIdg.en-orig.vtt
- Metadata: raw/20260811_K0X9QDRkIdg/K0X9QDRkIdg.info.json

Sonnet 4.5 developed what Anthropic's Applied AI team came to call context anxiety: approaching its context window limit, it would wrap work up early and stop with room to spare. They built context resets into the harness to compensate. Then Opus 4.5 shipped without the behavior, and the fix turned into pure overhead, adding latency and discarding cache it should have kept. That is the principle Gagan Bhat and Isabella Kai He build the whole session on: a harness encodes assumptions about what the model cannot do on its own, and those assumptions go stale as models improve.

The architectural consequence is decoupling the brain, meaning the agent loop, from the hands, meaning the tool execution environment. Both started in one container, so the model could not begin reasoning until setup finished and either half failing took the whole agent down. Splitting them lets reasoning start while the container builds in parallel, which they measured at 60% faster time to first token at P50 and over 90% at P95. It also changes failure into something recoverable: a dead sandbox is simply retried, and a dead brain resumes from a durable session log. That log ends up doing triple duty, providing observability, letting the harness read context slices back in after Claude discards them mid run, and feeding a periodic batch process they call dreaming that rewrites the agent's memory so the next day's sessions start smarter.

Speaker info:
Gagan Bhat (Anthropic):
- https://www.linkedin.com/in/gagan-bhat/

Isabella Kai He (Anthropic):
- https://x.com/IsabellaKHe
- https://www.linkedin.com/in/isabella-kai-he/

Timestamps:
0:00 - Who the Applied AI team is
1:52 - From simple questions to owning outcomes
2:45 - The Messages API and the hand rolled agentic loop
4:29 - Six production infrastructure problems
5:20 - The Claude Agent SDK
6:13 - What managed agents takes off your plate
7:02 - Harnesses encode assumptions that go stale
7:51 - Context anxiety, and the fix that outlived its need
9:34 - Designing for the model capabilities of tomorrow
10:25 - What long running agents demand
11:16 - Decoupling the brain from the hands
12:59 - Three primitives: agent, environment, session
13:51 - Reliability and the four session states
15:32 - Recovering discarded context from the session log
16:23 - What the developer still owns
17:14 - Demo: an SRE agent for a latency spike
18:58 - Defining the environment and its network limits
19:49 - Kicking off a session
20:38 - Root cause, and the observability trace
22:25 - Lesson one: keep credentials away from the agent
23:15 - Lesson two: where the latency went
24:58 - Lesson three: session logs as memory
25:47 - Lesson four: self hosted sandboxes and MCP tunnels
27:28 - Dreaming
29:08 - Outcomes and grader agents
30:49 - Harnesses as the limiting factor

## Codex, Behind the Harness — Dominik Kundel, OpenAI

- Upload date: 2026-08-10
- Video: https://www.youtube.com/watch?v=shRR1e2HXMk
- Transcript: raw/20260810_shRR1e2HXMk/shRR1e2HXMk.en-orig.vtt
- Metadata: raw/20260810_shRR1e2HXMk/shRR1e2HXMk.info.json

Once GPT 5.3 Codex Spark started serving a thousand tokens per second on Cerebras, inference stopped being the bottleneck and the network became it. The answer was websocket mode: a persistent connection replacing server sent events over HTTP, carrying stateful context so a turn ships back only the tool call result instead of resending every item. The same pressure shapes context construction, which fights size, flexibility and cachability at once. Tools can be marked deferred so they never enter the context window and surface through tool search when the model actually wants them, and the available skills list is capped at 2% of the context window, with descriptions trimmed as it grows past that.

Actions are where a harness earns its keep. File edits go through an apply patch tool the models were trained on, everything else through a shell the model instinctively drives with ripgrep, and all of it inside a sandbox: seatbelt on macOS, bubblewrap on Linux, and a custom open source sandbox on Windows the team had to build themselves. Approval fatigue pushes people into full access, which their own security team hates, so an escalation now spins up an auto review subagent with read only permissions and no ability to spawn others, judging the action against the transcript and how explicitly the user authorized it. Deleting a file you asked for reads differently from deleting a .git folder you never mentioned. Long horizon goals run by injecting a continuation prompt until the model calls an update goal tool, which is why concrete verifiable objectives beat essays. Dominik Kundel's closing point is that the harness is Apache 2 and written in Rust, and most of what makes it distinct lives in the responses API, so you can borrow any of it.

Speaker info:
- https://x.com/dkundel
- https://linkedin.com/in/dkundel
- https://github.com/openai/codex

## Taking Reinforcement Learning Cross Datacenter — Nan Jiang, Modal

- Upload date: 2026-08-10
- Video: https://www.youtube.com/watch?v=maRzp4kImJ4
- Transcript: raw/20260810_maRzp4kImJ4/maRzp4kImJ4.en-orig.vtt
- Metadata: raw/20260810_maRzp4kImJ4/maRzp4kImJ4.info.json

A frontier scale checkpoint is around 500 GB, so shipping one to a rollout fleet in another region takes minutes to hours and kills any hope of weight updates landing in seconds. Nan Jiang's claim is that you can send roughly 500 MB instead and have the rollout engine reconstruct a bitwise identical weights version. Fewer than 1% of rollout visible weights actually change between consecutive versions, and the reason is not that gradients are sparse. Gradients are dense, about 99% of parameters get a nonzero gradient and the FP32 master update is dense too. It is just small.

The mechanism is a small Adam step meeting finite precision. The rollout engine serves a BF16 view whose rounding boundary sits near theta over 256, about 0.0039 for a weight around 1, while a typical Adam step at RL post training learning rates runs around 3 millionths, more than a thousand times too small to cross it. The master weights move and the served value does not, which he calls Adam absorption. Lower precision serving makes it sharper still: an internal run serving GLM 4.7 Air in FP8 saw 0.15% of weights change on the first step and settle near 0.05%. Once a lossless patch is the unit of synchronization instead of a checkpoint, the rollout fleet stops needing to live in the trainer's cluster. Training keeps its all reduce and its fast fabric, rollout islands scatter across whatever regions and providers have GPUs right now, a sidecar makes any engine version aware, and scattered inference capacity becomes one elastic rollout fleet. Modal's implementation is called Stitch.

Speaker info:
- https://x.com/nanjiangwill
- https://www.linkedin.com/in/nanjiangwill/
- https://www.nanjiangwill.com/
- https://github.com/nanjiangwill

Timestamps:
0:00 - Where the GPUs actually are
1:29 - The standard RL post training loop
2:06 - The cathedral and the bazaar
2:43 - RL wants four things at once
3:22 - What can leave the cluster and what cannot
3:59 - The rollout serving island as the movable unit
5:16 - Why a full checkpoint is the wrong unit of sync
6:33 - The bet: under 1% of served weights change
7:10 - Ingredient one, the precision floor
8:30 - Ingredient two, the size of an Adam step
9:48 - Adam absorption, visualized
11:06 - Shipping a lossless patch, not a delta
12:21 - What the measurements show
12:58 - Why this is not gradient sparsity
13:35 - FP8, NVFP4, and group scaled formats
14:54 - An internal run on GLM 4.7 Air
15:33 - The bulletin board architecture
16:48 - The sidecar that makes engines version aware
17:26 - 500 GB down to 500 MB
18:02 - Stitch
18:43 - Open questions: Muon, fully async RL, and beyond

## Always-on agents run production without the on-call tax — Justin Smith, Resolve AI

- Upload date: 2026-08-09
- Video: https://www.youtube.com/watch?v=vSx5IULvBns
- Transcript: raw/20260809_vSx5IULvBns/vSx5IULvBns.en-orig.vtt
- Metadata: raw/20260809_vSx5IULvBns/vSx5IULvBns.info.json

Someone drops a GitHub release tag into Slack and the agent decides on its own that this is a deploy worth watching. It reads what actually changed, works out which telemetry would expose trouble for that particular change, and writes a check plan for this release alone: checkout is replacing the currency service, so watch checkout latency and error rates, then follow the causal chain into the Kafka pipeline. None of the timing is hardcoded. It can decide to look again in an hour because this class of failure only surfaces intermittently, or come back in three days to ask whether the deploy is still healthy. Justin Smith is careful to say CI/CD already handles the baseline well. The gap is everything routed around it, the feature flags and infrastructure changes that ship with no monitoring at all and get caught only when an alert wakes somebody up.

The premise underneath is that around 70% of an engineer's time goes to running code rather than writing it, and coding agents made that worse by raising the volume of change flowing into production. Resolve's background agents are defined by three questions: when they run, on a schedule or an event stream or just a message; how they run, in the cloud inside a sandbox with its own file system, so closing your laptop changes nothing; and how they know what to do. The one Smith clearly enjoys most watches Slack channels and answers engineering questions without being addressed, staying quiet when it lacks confidence, and DMing him to confirm an answer before it replies in public. His sharpest point is that execution is the easy half. Loading a dashboard is execution. Deciding a metric smells wrong is production context, and building the knowledge system that keeps up with an environment changing faster every month is where the real work sits.

Speaker info:
- https://www.linkedin.com/in/justin-smith-7b1534a8/
- https://resolve.ai/events/behind-the-build/agents-for-engineering-workflows

## Multiplayer agentic engineering — Arjun Singh, Superconductor

- Upload date: 2026-08-09
- Video: https://www.youtube.com/watch?v=OL7kfezynJM
- Transcript: raw/20260809_OL7kfezynJM/OL7kfezynJM.en-orig.vtt
- Metadata: raw/20260809_OL7kfezynJM/OL7kfezynJM.info.json

Superconductor left a meeting bot sitting in a Google Meet at their expo booth for four hours, just listening. Someone passing through said they wanted coding agents to have clear acceptance criteria before declaring work finished. Nobody filed a ticket. The bot picked the idea out of the conversation, opened one itself, started working, and added two acceptance criteria fields to the product's own ticket form, then produced a screenshot when asked. Arjun Singh is not pretending that change ships as written. The claim is narrower and more useful: every customer call, onboarding session and team meeting now yields dozens of prototyped ideas and usually a few genuinely shippable pull requests, with nobody hand carrying a request from one system into another.

Most of the talk is what has to be true underneath. One agent session has to be reachable from Slack, the desktop app and GitHub at once, so reviewing a teammate's work means asking the agent inside the thread instead of waiting for the author to wake up. The work runs in an isolated cloud environment, and Singh argues the real reason is not closing your laptop, it is least privilege. An agent told to wipe the staging database, resourceful and eager to comply, can find a token on a developer's machine that happens to point at production. A configurable network sandbox blocks exfiltration and asks before reaching anywhere new, and that same isolation is what lets support and growth people trigger real work without a development environment. Rather than trusting public benchmarks, they replay pull requests that represent good work from their own repository and plot quality against cost and time, because SWE bench is Python and they are Ruby on Rails. Their numbers for one month: 10.5 billion tokens, 3,300 Claude Code runs worth about $10,000 in token value, and Codex running four times as many sessions for less money.

Speaker info:
- https://x.com/singharjun51293
- https://www.linkedin.com/in/arjun-singh-629216105

## Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster — Matt Dailey, Ref.

- Upload date: 2026-08-09
- Video: https://www.youtube.com/watch?v=Kz4QJmNrVXU
- Transcript: raw/20260809_Kz4QJmNrVXU/Kz4QJmNrVXU.en-orig.vtt
- Metadata: raw/20260809_Kz4QJmNrVXU/Kz4QJmNrVXU.info.json

A newsletter writer walked Matt Dailey through an agentic pipeline good enough to amplify their own voice instead of flattening it, then mentioned they were now effectively writing a book every week. Dailey asked whether the audience was reading a book every week. They were not. Those pages go unread, and that gap is what he calls velocity sickness: the stress of a sudden output increase that delivers output without impact. On engineering teams it arrives as too many pull requests to merge, work sprinting in too many directions at once, and the ritual of declaring agent bankruptcy, walking back to twelve terminals the next morning, recognizing none of it, throwing all of it out and paying for the same work twice.

The failure that actually worries him is critical decisions getting made by agents, because an engineer who lets that happen has stopped owning the code, and a team doing it at scale no longer owns the product. His fix is to separate the decision layer from the implementation layer and give the decision layer its own primitive: a document rather than a chat. Chats are isolated, ephemeral and built for implementation, so the decisions made inside one evaporate while only the code survives. A durable shared doc holds the state and the agent supplies the action, which keeps agents effectively stateless, lets several start from identical context, and turns rebuilding your own understanding into rereading a file. The tell that it is working, he says, is people writing plans they never implement, which is what prioritizing looks like once idea velocity replaces code velocity. Three things to try immediately: notice which gear you are in, treat the plan as a portal into the system rather than a prompt, and hand a plan to a teammate before you hand it to an agent.

Speaker info:
- https://www.linkedin.com/in/matthewjdailey
- https://ref.tools/

## Guide, Verify, Solve — Anirban Chatterjee, Sonar

- Upload date: 2026-08-09
- Video: https://www.youtube.com/watch?v=03l29gJXpCE
- Transcript: raw/20260809_03l29gJXpCE/03l29gJXpCE.en-orig.vtt
- Metadata: raw/20260809_03l29gJXpCE/03l29gJXpCE.info.json

A Carnegie Mellon study sorted GitHub projects by whether an AI tool wrote the code, and found the productivity gain ran out after about three months while the static analysis warnings and the added complexity stayed. That residue is verification debt, and how much it costs scales with criticality: a short lived internal tool can live with the gap between the quality a model gives you and the quality the application needs, a large codebase with adversarial users cannot. The obvious backstop is human review, and a Wharton study suggests it leaks badly. Participants took the AI's advice 92.7% of the time when it was correct, and still followed it nearly 80% of the time when it had been instructed to lie confidently.

Anirban Chatterjee's argument is that the check has to be zero trust and multi layered. Zero trust means assuming the code could have come from anywhere and verifying it by a different method than the one that wrote it, since a model grading its own output inherits its own blind spots. Multi layered means computational review running alongside reasoning based review, because no single technique catches syntax, data flow, architecture and control flow at once. Sonar's leaderboard makes the blind spots concrete: across their metrics one Claude model rates well on correctness and reliability while the other is the better choice when maintainability, security or lower complexity is what matters. The loop he proposes wraps generation on both sides, handing the agent architectural constraints and coding standards before it starts, running verification inside the inner loop so issues get fixed before they propagate into later loops, and giving the agent the tools to remediate what comes back instead of queueing it for a person who is already rubber stamping too much.

Speaker info:
- https://www.linkedin.com/in/anirbanc/
- https://www.sonarsource.com/the-coding-personalities-of-leading-llms/leaderboard/

## Realtime multiplayer, automation, and you! — Idan Gazit, GitHub

- Upload date: 2026-08-08
- Video: https://www.youtube.com/watch?v=iQ5xldZ9StU
- Transcript: raw/20260808_iQ5xldZ9StU/iQ5xldZ9StU.en-orig.vtt
- Metadata: raw/20260808_iQ5xldZ9StU/iQ5xldZ9StU.info.json

Idan Gazit's personal site runs on Astro, which ships often enough to keep him permanently on the upgrade treadmill, so he wrote an agentic workflow in about three lines of plain English, the kind of message you would send a teammate. Copilot expanded it into a full playbook: check for new releases, read the changelog and upgrade guide, apply the changes, open a pull request. It then carried him from Astro 5 to Astro 7, two major versions at once, found and fixed the code that broke, verified the build, and flagged the manual steps it could not take itself. The workflow is a Markdown document. The YAML actions file is a compiled artifact nobody reads, so changing how the automation behaves means editing the English.

The guardrails are the part he wants remembered. Prompting an agent to behave is not a guardrail, because anyone who can prompt inject it can undo the instruction, and you have let the fox into the henhouse. Permissions, allowed tools, reachable network destinations and safe outputs get declared deterministically in front matter instead. His upgrade workflow may open exactly one pull request, and is explicitly allowed to do nothing at all, since an automation that cannot stay quiet turns into a denial of service against its own owner. Secrets stay outside the agent's jail entirely, because a secret an agent can see should be treated as already compromised. The second prototype, ACE, runs every session in a cloud microVM and deliberately resembles a chat app, on the theory that what belongs in the shared surface is everything not already in the code: the political constraints, the infrastructure deal that quietly picks your cloud provider, the plan two people edit together before telling the agent to go make the document true. He ends on a study of around a hundred developers over thousands of hours which found that hands on keyboard typing is about 5% of the work, and that is the only 5% the tools have helped with so far.

Speaker info:
- https://twitter.com/idangazit
- https://linkedin.com/in/idangazit
- https://githubnext.com

## Anthropic's CCA Exam as a Field-Guide for Agentic Engineering — Frank Coyle, UC Berkeley

- Upload date: 2026-08-08
- Video: https://www.youtube.com/watch?v=Z-c11pV_uvU
- Transcript: raw/20260808_Z-c11pV_uvU/Z-c11pV_uvU.en-orig.vtt
- Metadata: raw/20260808_Z-c11pV_uvU/Z-c11pV_uvU.info.json

The Claude Certified Architect exam hands you six production scenarios and picks four at random, and Frank Coyle walks through them backwards, leading with the anti pattern in each one. Knowing what not to do is what points you toward what to do, the same way the design patterns movement of the early 1990s came with a catalog of the moves that quietly ruin you. Scenario one is a customer support loop, and the anti pattern is calling the model, taking the response, and using it. What you want instead is to branch on the stop reason, because the model cannot execute a tool at all. It only hands back the parameters your own code runs, and the stop reason is also how you learn you ran out of tokens and the answer in your hands is partial.

The rest is context discipline. Loading one agent with every tool is the carpenter who turns up with plumbing and electrical gear too, so specialized subagents with one or two tools each win, and every agent should see only its own slice. Coyle gives a critic agent the claim and the evidence but withholds the reasoning that produced them, because agents that watch each other think converge on a single idea the way a group talks itself into pizza. Subtask output gets forked into its own context so only the summary returns to the main thread, with a token count check that triggers compaction past a threshold. He closes on a cheap win most people skip: batch mode runs the same work for half the token cost if you can wait a day for it.

Speaker info:
- https://x.com/coyle_frankp
- https://www.linkedin.com/in/frank-coyle/
- https://www.frank-coyle.ai/

## Benchmarking Coding Agents on New vs Legacy Codebases — Denys Linkov, Wisedocs

- Upload date: 2026-08-08
- Video: https://www.youtube.com/watch?v=7vn4WpqNpck
- Transcript: raw/20260808_7vn4WpqNpck/7vn4WpqNpck.en-orig.vtt
- Metadata: raw/20260808_7vn4WpqNpck/7vn4WpqNpck.info.json

Wisedocs processes medical claims that arrive as PDFs over 10,000 pages long, some of them larger than video files, through a pipeline of ML models spread across ten repositories nobody enjoyed touching. Denys Linkov's team spent six months collapsing that into a monorepo, and this talk is an honest audit of whether they should have just waited for the models to get good enough to do it for them. The benchmark he keeps coming back to is a single refactor task. With o3 it took three hours of back and forth in Cursor and still shipped ten major mistakes. Rerun on newer models, Sonnet 4.6 needed one extra iteration and Opus 4.8 essentially got it in one pass, at roughly a fifth of the original effort.

The counterweight is what happens when you hand a current model the whole job. GPT 5.5 extra high declared the refactor done in 10 minutes 22 seconds and wrote 2,000 lines, which turned out to be scaffolding with the actual models missing, something it admitted in its own output by noting it had not added the deployment or bootstrap command yet. That gap is why Linkov reads the METR task length curve at 80% or 90% success instead of the usual 50%. Launching an hour long agent run on coin flip odds mostly buys you a wasted hour and a broken attention span. His verdict is that doing the refactor beat deferring it, and the evidence is as much social as technical: commit velocity rose and never flattened, work that used to take months ships in under a week, and developers across the company now volunteer into the repo even outside their own area, which was never true of the ten it replaced.

Speaker info:
- https://x.com/denyslinkov
- https://www.linkedin.com/in/denyslinkov/

## The New Primitives: Building AI Native Software — Kwindla Kramer, Daily

- Upload date: 2026-08-07
- Video: https://www.youtube.com/watch?v=LZuWZRze3MU
- Transcript: raw/20260807_LZuWZRze3MU/LZuWZRze3MU.en-orig.vtt
- Metadata: raw/20260807_LZuWZRze3MU/LZuWZRze3MU.info.json

In 1945 Vannevar Bush described document scanning, OCR, speech to text, hypertext, search engines, a head mounted camera, and voice interfaces, in a single essay, before any of it existed. Kwindla Hultman Kramer uses As We May Think to set up the uncomfortable part: he was a baby programmer in 1995 writing HTML by hand and web servers in C, as excited about web pages then as he is about agents now. Web pages turned out to be a primitive, not a destination. His argument is that agents are the web page of this era, and the thing worth building is the AI native software that comes after.

The tour through the decades is the evidence. Each one had a job: programming languages to carry human intent into the machine, interactivity in the 1960s, abstractions for scale in the 1970s, then the personal computer. VisiCalc is the example he keeps returning to, because it did not put accountants out of work, it made vastly more accounting possible and invented categories of work nobody could have described when a screen of calculations took a room full of people. He offers that as the reply to the mass unemployment worry. The talk closes on Gradient Bang, a massively multiplayer game with an LLM at the core of every interaction and hundreds of inference calls in flight, built specifically to exercise the primitives he thinks come next: asynchronous non blocking context compression, long running subagents that share context, progressive skills loading, dynamic interface generation, and conversational voice.

Speaker info:
- https://x.com/kwindla
- https://www.linkedin.com/in/kwkramer/
- https://machine-theory.com/
- https://github.com/pipecat-ai/pipecat

Timestamps:
0:00 - Daily, Pipecat, and what comes after agents
1:31 - What Vannevar Bush predicted in 1945
2:13 - Nadella on multimodel harnesses
4:12 - Agents are the web pages of 1995
5:25 - From the abacus to the stored program computer
6:46 - The 1950s: getting human intent into the machine
7:30 - The 1960s: interactivity, Sketchpad, and Star Trek
8:51 - The 1970s: abstractions that scale
9:32 - VisiCalc and why it did not replace accountants
10:49 - Knowledge Navigator, Apple's 1987 prediction
12:46 - The web was multimodal from the start
13:24 - Minority Report, Iron Man, and building it for real
17:10 - Cloud, then agents, then what
18:24 - Knowledge Navigator rebuilt on real technology
19:38 - Gradient Bang and the primitives it exercises
20:52 - Closing

## Compression at the Edge — NVIDIA, Unsloth, HuggingFace, Ollama

- Upload date: 2026-08-07
- Video: https://www.youtube.com/watch?v=J4_jCrTxMkk
- Transcript: raw/20260807_J4_jCrTxMkk/J4_jCrTxMkk.en-orig.vtt
- Metadata: raw/20260807_J4_jCrTxMkk/J4_jCrTxMkk.info.json

Quantize a single number in a model and it gets 20% dumber. That finding, from the super weights paper, is why Daniel Han's claim is less absurd than it sounds: GLM 5.2 goes from 1.5 terabytes to 250 GB, 86% smaller, without being 86% dumber. Layers are wildly unequal. The first and last carry enormous weight, the middle ones barely matter, and a model trained on 30 trillion tokens never saturates its parameters, so many sit near zero and can simply be set there. Choosing which layers stay in high precision is a combinatorial search, not a setting.

NVFP4 is the format the NVIDIA side leans on, a 4 bit float where every group of 16 values shares one FP8 scale, targeting under 1% accuracy loss. New architectures keep breaking the old heuristics: quantize the linear attention layers and the model looks fine right up until a long context turns it to gibberish. Post training quantization works out of the box above roughly 20 billion parameters and needs quantization aware distillation below that. The panel is blunt that benchmarks only cover verifiable tasks, so the real test is running the model in an actual harness, and Han's preferred signal is KL divergence between the BF16 and quantized output logits rather than any accuracy score.

Speaker info:
Chris Alexiuk, moderator (NVIDIA):
- https://x.com/llm_wizard
- https://www.linkedin.com/in/csalexiuk

Daniel Han (Unsloth):
- https://x.com/danielhanchen
- https://unsloth.ai

Asma Beevi (NVIDIA):
- https://www.linkedin.com/in/asma-beevi-k-t-433053a2
- https://realasma.github.io

Merve Noyan (Hugging Face):
- https://x.com/mervenoyann
- https://hf.co/merve

Parth Sareen (Ollama):
- https://github.com/parthsareen
- https://parthsareen.com

Timestamps:
0:00 - Welcome and the panel
0:53 - What compression means to each of them
3:05 - GLM 5.2 from 1.5 terabytes to 250 GB
4:08 - When each of them got the compression bug
8:19 - QLoRA and finetuning on a T4
11:44 - 86% smaller without being 86% dumber
12:46 - Why layer importance is so uneven
14:26 - The super weight: one number, 20% dumber
14:51 - Evaluating the quantized checkpoints
16:37 - What NVFP4 actually is
17:55 - Does compression matter beyond the toaster
21:49 - Why compress a big model instead of using a small one
24:30 - Where Ollama fits
28:54 - How hard NVFP4 is to produce
32:46 - The cursed era of model architectures
35:17 - Why linear attention layers break quantization
37:22 - Where compression goes next
43:22 - How do you know a quant is any good

## Local Models: Trust, Control, Optimization — Carter Abdallah, NVIDIA

- Upload date: 2026-08-07
- Video: https://www.youtube.com/watch?v=FWMJQDH3iK0
- Transcript: raw/20260807_FWMJQDH3iK0/FWMJQDH3iK0.en-orig.vtt
- Metadata: raw/20260807_FWMJQDH3iK0/FWMJQDH3iK0.info.json

When Fable was pulled back and access to frontier systems stopped looking guaranteed, Lucas Atkins watched enterprises move to Chinese open models, not because they scored better but because availability could be counted on. That is his working definition of trust, and he separates it hard from safety: an open model is a directory of files you can inspect, running on code you can read, while the same claim about a closed API is unverifiable by construction. Arcee's response was to reorient the whole company and pretrain a 400 billion parameter model in six months, which he says plenty of people called impossible.

The rest is control. Vincent Weisser describes a customer specializing an open model to automate finance work in a week or two and landing better results than Opus at a fraction of Haiku's cost. Closed terms of service bar you from training on outputs, so owning the model also means owning the traces, which is what makes a data flywheel possible at all; Nemotron and Trinity both adopted the open MDW license to put that permission in writing. Chris Alexiuk's framing is the mismanaged genius: a model tuned to be good across every harness is optimal for nobody's, and open weights let you fit it to the one or two things you actually do. The predictions land where you would expect from this panel, including open models reaching Fable level capability inside a year, and Atkins hoping the share of people who have ever run a model locally climbs from a rounding error to 10% to 15%.

Speaker info:
Carter Abdallah, moderator (NVIDIA):
- https://x.com/Baxate
- https://baxate.com

Vincent Weisser (Prime Intellect):
- https://www.linkedin.com/in/vincentweisser
- https://www.primeintellect.ai/

Lucas Atkins (Arcee AI):
- https://x.com/latkins
- https://arcee.ai

Chris Alexiuk (NVIDIA):
- https://x.com/llm_wizard
- https://www.alexi.uk/

Timestamps:
0:00 - Welcome and why this panel is the whole stack
1:14 - Prime Intellect: keeping the training stack open
2:15 - Arcee: why the west was losing the open model lead
3:22 - Pretraining a 400 billion parameter model in six months
4:23 - Nemotron: faster models are smarter models
6:35 - Is open source actually less trustworthy
7:40 - Trust is not safety
9:48 - When access stopped being guaranteed
10:56 - Releasing the data sets alongside the weights
11:59 - The open superintelligence stack
13:02 - Post training as the accessible layer
14:07 - Beating frontier models on a specific use case
15:11 - Making your costs predictable
16:11 - When the model and the harness blend together
18:15 - The mismanaged genius
19:19 - A call to action for builders
20:24 - Who owns the data you generate
21:27 - Owning your outputs, not just your weights
22:35 - The open MDW license
23:36 - Where post training unlocks new use cases
27:46 - You do not need frontier intelligence for most tasks
28:53 - Why efficiency has to happen in the open
29:55 - Closed models are not the enemy
33:05 - Predictions for the next year
38:22 - Running everything on your laptop
39:29 - Agent operating systems and the next Siri moment
41:36 - Closing

## Open Source Is Dead. Long Live Open Source. — Saoud Rizwan, Cline

- Upload date: 2026-08-07
- Video: https://www.youtube.com/watch?v=CoEIs6Xm8m8
- Transcript: raw/20260807_CoEIs6Xm8m8/CoEIs6Xm8m8.en-orig.vtt
- Metadata: raw/20260807_CoEIs6Xm8m8/CoEIs6Xm8m8.info.json

A compromised release of litellm, a Python package pulling three and a half million downloads a day, sat live for three hours installing a credential harvester for API keys, SSH keys and crypto keys along with a backdoor for remote command execution. It was caught by pure luck: the malware had a bug that crashed Cursor, and a researcher went looking. Saoud Rizwan uses it to mark how far the trust model has fallen. Zig's code of conduct now bans AI from pull requests, issues and even comments, because the team values growing contributors over collecting contributions. curl is weighing the end of a decades old bug bounty as AI generated reports drown it. tldraw closes pull requests on sight. GitHub shipped a switch to disable third party pull requests altogether, which is the feature that made GitHub what it is. He built Cline in the open, and his claim is that the community half of open source is the half that died.

The half that survives is open weights, and the case is economic. Cline pitted GLM against Opus on a real bug in their own repository: GLM spent twice the tokens at half the cost, cleaned up dead code and confirmed the build compiled, while Opus finished faster with fewer tool calls but left type errors that broke the production build. Coinbase defaulted its internal gateway to GLM and Kimi and cut AI spend nearly in half. The precedent Rizwan reaches for is Open Compute: Facebook gave away its data center designs, the supply chain standardized on them, manufacturers moved to huge uniform production runs, and the commoditization that followed drove Facebook's own costs down by billions. His closing ask goes to the American labs. Release open weights models, because once the industry standardizes on foreign ones, marginal quality gains may not be enough to bring anyone back.

Speaker info:
- https://x.com/sdrzn
- https://github.com/saoudrizwan
- https://cline.bot

Timestamps
0:00 Introduction to Cline and the early open source coding agent era.
1:30 The decline of the open source community and the rise of AI-driven distrust.
2:22 How projects like Zig, curl, and tldraw are responding to AI-generated noise.
3:45 Systemic risks: The litellm supply chain compromise example.
5:22 The economic case for the survival of "open weights" models.
5:49 Real-world impact: Corporate AI spending and infrastructure lock-in.
8:50 Comparing model intelligence vs. system-level AI verification (GLM vs. Opus).
10:57 The Open Compute precedent: How open standards commoditize the industry.
12:36 Future projections for AI inference costs and hardware capacity.
14:22 A call to action for American labs regarding open weights models.
16:01 Cline's shift to an open weights subscription model.

Quotes
(1:48) "GitHub is effectively an archive of SLOP PRs and issues and security reports."
(3:47) "When I say that open source is dead, I mean some parts of it—like the community—it's just not worth cultivating anymore."
(7:00) "They're essentially going to subsidize this until they have as many engineers dependent on their tooling as possible... and then inevitably the price gouging."
(14:35) "Before we know it, all this infrastructure that we're investing in could be built on foreign models that take the world by a storm."

## The State of Model Routing — NVIDIA, Cognition, OpenRouter

- Upload date: 2026-08-06
- Video: https://www.youtube.com/watch?v=QHBjufYK8TA
- Transcript: raw/20260806_QHBjufYK8TA/QHBjufYK8TA.en-orig.vtt
- Metadata: raw/20260806_QHBjufYK8TA/QHBjufYK8TA.info.json

Run terminal bench on Opus and on Haiku and Opus scores about three times better at a tenth of the cost, even though Haiku is far cheaper per token. Alex Atallah's point is that a small model pushed outside its training distribution thrashes, calling tools in loops until it costs more than the expensive model ever would. That inverts the obvious version of model routing, where you send each task to whichever model benchmarks best on it. Walden Yan calls that approach fragile for exactly the reason agents make it worse: a session starts as a question about a codebase, becomes a feature request, then becomes live debugging, and the model you picked at the start is stranded.

Cognition's answer keeps a frontier model planning and delegates the implementation, which cut the cost of Fable level intelligence by 40% while going deeper, because a cheaper model can afford to spin off three sub agents to explore a codebase. They also avoid sub agents in favor of one sidekick with a continuous running context, so the KV cache stays warm and cached tokens cost roughly ten times less. Compaction, Yan argues, is worth doing for intelligence rather than cost, since compacting forces a cache miss and model quality falls off a cliff well before the advertised million token window. The most telling story is OpenRouter's: its auto router sat almost unused for two years until openclaw began sending heartbeats every ten minutes, creating one popular app with two completely different intelligence needs.

Speaker info:
Nader Khalil, moderator (NVIDIA):
- https://x.com/naderlikeladder
- https://nader.coffee

Walden Yan (Cognition):
- https://x.com/walden_yan
- https://www.linkedin.com/in/waldenyan

Alex Atallah (OpenRouter):
- https://x.com/alexatallah
- https://openrouter.ai

Tanay Varshney (NVIDIA):
- https://www.linkedin.com/in/tanayvarshney

Carter Abdallah (NVIDIA):
- https://x.com/Baxate
- https://www.linkedin.com/in/carter-abdallah

Timestamps:
0:00 - Welcome and the multimodel premise
1:16 - Panel introductions
3:24 - How Devin Fusion beats the frontier models
4:25 - Let the frontier model plan and delegate the work
6:31 - Jagged capabilities: no one model wins everything
9:42 - Why naive task based routing is fragile
11:48 - Sharing context without paying for it twice
13:56 - Should the orchestrator be the big or the small model
16:01 - In distribution versus out of distribution
19:12 - Training models to collaborate
20:12 - Flex Run and flexible model sizes
22:24 - Lossy context and the systems you fall back to
26:41 - How a heartbeat created the auto router
29:43 - Routing between local and cloud
31:51 - Compaction versus routing
32:55 - How a small model signals it is out of its depth
35:00 - Cache duration and self hosting economics
40:12 - Are prompts portable across models
43:20 - Is the router a product or plumbing

## Gadgets: Personal app vibe coding that is actually safe — Kenton Varda, Cloudflare

- Upload date: 2026-08-05
- Video: https://www.youtube.com/watch?v=RmS5s6Wbin4
- Transcript: raw/20260805_RmS5s6Wbin4/RmS5s6Wbin4.en-orig.vtt
- Metadata: raw/20260805_RmS5s6Wbin4/RmS5s6Wbin4.info.json

*Note: Kenton has just released Cloudflare OS today: https://x.com/KentonVarda/status/2084990137180590572 This talk was recorded a month prior to launch.*

Claude needed a strikethrough the slide app did not have, so it added one to the app. Asked to build a deck from a Google doc, it also added text centering and a box that accepts raw SVG, then generated the SVG for a diagram the app could not otherwise draw. That is Kenton Varda's argument in a single move. Software today ships from a developer to users whose feature requests die in Jira, and the escape hatch developers reach for is a plugin architecture rewrite that takes years and never lands. If a user's own agent can add the feature, the core app stays clean and nobody waits.

Nothing in current infrastructure supports that. Mobile platforms will not run unsigned code, and 25 years of cloud architecture put one blessed version of every app on the developer's server. Gadgets is his answer, built on Cloudflare Workers with no containers and no database. Each gadget is a single instance of an app, one deck or one board, and sharing is implemented by the platform so the app itself cannot get access control wrong. The UI runs in a null origin iframe that can only postMessage to its parent, over a Cap'n Web RPC session to server code in a dynamic worker sandbox, so an XSS bug in vibecoded code has nothing left to leak. The whole demo ran locally on workerd, so a dead conference network cost him only the one call that needed a model.

Speaker info:
- https://x.com/KentonVarda
- https://lanparty.house
- https://github.com/cloudflare/workerd

Timestamps:
0:00 - Personal AI codegen breaks cloud infrastructure
1:16 - How feature requests die today
2:35 - The plugin system rewrite trap
3:27 - What if users could add their own features
5:11 - Gatekeeping, and why the web is the escape hatch
7:11 - Kenton Varda and Cloudflare Workers
8:39 - Gadgets as an office suite, not a deploy target
9:58 - Blueprints and the slide builder
11:03 - One gadget per document, sharing built into the platform
12:21 - Claude adds features to the app to build the slides
14:04 - Why an XSS bug does not matter here
16:22 - No containers, no database, running on workerd
17:24 - Why it is not open source yet


Quotes

"Personal AI codegen breaks traditional cloud infrastructure." (0:38)
"It's almost easier to buy a gun in the United States than it is to get access to your own phone to install unsigned software." (5:11)
"I want to know where in Claude's training data it learned that you could make words wiggle to give them emphasis." (6:33)
"The reason they're bad is entirely my fault. It's not the software's fault." (11:57)
"If you have an XSS bug, it actually doesn't end up mattering because these can't leak anything." (15:26)

## Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)

- Upload date: 2026-08-03
- Video: https://www.youtube.com/watch?v=jQDXzEVHMSE
- Transcript: raw/20260803_jQDXzEVHMSE/jQDXzEVHMSE.en-orig.vtt
- Metadata: raw/20260803_jQDXzEVHMSE/jQDXzEVHMSE.info.json

This fireside chat between Gergely Orosz and Simon Eskildsen explores the technical journey and engineering philosophy behind the database company Turbopuffer.

Video Timestamps
0:00 Introduction and Simon’s early history with computers
3:02 The International Olympiad in Informatics and early competitive programming
4:13 How Simon was recruited by Shopify while still in high school
8:46 Engineering challenges and scaling infrastructure at Shopify
14:56 Decision to leave Shopify and the creation of the "napkin math" project
20:40 The origin and technical motivations behind Turbopuffer
24:46 Design challenges of building a database on top of S3
28:41 Cursor becoming the first major customer
35:36 The meeting with Jensen Huang and Nvidia’s push for GPUs
39:01 The competitive reality of cloud infrastructure and CPU scarcity
43:06 Philosophical perspective on venture capital and funding
51:45 Building a remote-first culture with the "campfire" concept

Quotes

(19:49) "Because you batch. So an f-sync happens on usually a 4K... it's not intuitive. It's actually—I got caught—I just got obsessed with this question."
(30:33) "Yeah, you could do a million vectors for a dollar. And before that, I think the cheapest was maybe $100 per million for something that actually worked."
(36:56) "[Jensen Huang] said, 'Judging by your slide, maybe you should [pivot into vapes].'"
(43:53) "I promised Cursor that Justine and I could get their bill to 4K a month... that's the pricing we ship with."
(49:54) "The third reason to raise capital is for the founder's ego... I wish that it was more talked about because you're diluting all of your employees when you do it."

## Speakers

### Gergely Orosz
Author / Founder, The Pragmatic Engineer · The Pragmatic Engineer
[X/Twitter](https://twitter.com/gergelyorosz) · [LinkedIn](https://www.linkedin.com/in/gergelyorosz/) · [Website](https://pragmaticengineer.com)

Software engineer, engineering leader, and author of The Software Engineer's Guidebook; best known for The Pragmatic Engineer newsletter and blog covering software engineering practices, engineering leadership, and the tech industry. Previously held engineering leadership roles at Uber and worked at companies including Skype and Skyscanner.

### Simon Eskildsen
CEO and co-founder · turbopuffer
[X/Twitter](https://x.com/Sirupsen) · [LinkedIn](https://www.linkedin.com/in/sirupsen/) · [Website](https://sirupsen.com) · [Blog](https://sirupsen.com/napkin)

Co-founder and CEO at turbopuffer. Formerly Principal Engineer at Shopify, where he helped scale infra from 1K → 1M RPS.

— [View on the schedule](https://www.ai.engineer/worldsfair/schedule?session=asn_slot_2026_06_30_main_stage_1230_2026_06_25t07_57_06_000z)

## MCP Tasks (async): Why Aren't Any Agents Supporting Them? — Cornelia Davis, Temporal

- Upload date: 2026-08-02
- Video: https://www.youtube.com/watch?v=s4r6nk5WsZw
- Transcript: raw/20260802_s4r6nk5WsZw/s4r6nk5WsZw.en-orig.vtt
- Metadata: raw/20260802_s4r6nk5WsZw/s4r6nk5WsZw.info.json

You invoke a tool and expect an answer, but real work takes time, and over that time connections drop, networks blip, and processes crash. Cornelia Davis, a distributed systems veteran who wrote the book on cloud native patterns, argues that this is exactly the gap the MCP tasks specification exists to close, and walks through why almost no agents support it yet. A task lets a tool run long, report progress, and pause for human input without losing its place, which means the interaction has to be durable: it survives the client disconnecting and picks up right where it left off.

She demonstrates it with an invoice processing flow, a dashboard tracking task state, and a step that waits for a human to submit input before the backend continues, then traces how the spec evolved from V1 to V2. The design she keeps returning to is a stateless core with the harder long running behavior layered on as an extension, RPC requests replaced by the server pushing updates, and life cycle state carefully mapped so clients know what to resume. Her honest takeaway is that just because you can open a long lived stateful connection does not mean you should, and that getting durable long running tasks right is what will finally let agents handle work that does not finish in a single call.

Speaker info:
- https://x.com/cdavisafc
- https://www.linkedin.com/in/corneliadavis/

Timestamps:
0:00 - What MCP tasks are, and why they're hard
1:29 - A distributed systems point of view
2:34 - A first look at a task running
4:03 - What a task actually allows
4:43 - Why long running work breaks
6:02 - Durability across disconnections
7:04 - Demo: invoice processing dashboard
9:10 - Waiting for human input
11:18 - What changed in tasks V1
12:35 - The stateless core
16:37 - Extensions and server pushed updates
20:09 - V2 and what you need to implement

## When Will The Benchmaxxing Plague End? — Nick Heiner, Surge AI

- Upload date: 2026-08-02
- Video: https://www.youtube.com/watch?v=-npY6XjM8CQ
- Transcript: raw/20260802_-npY6XjM8CQ/-npY6XjM8CQ.en-orig.vtt
- Metadata: raw/20260802_-npY6XjM8CQ/-npY6XjM8CQ.info.json

Every time a model launches there is a gap between the benchmark numbers and what the thing can actually do, and Nick Heiner argues the existence of the word benchmaxxing is the tell. When labs openly brag about scores, teams stop asking whether a benchmark reflects reality, and the whole field drifts into an avalanche of numbers that measure the wrong thing. His talk is a field guide to reading a benchmark fairly, starting from the antipatterns that quietly break them.

The failure modes are specific. A large share of tasks in a typical benchmark are simply broken; contamination means models have memorized test content, so a SWE-bench style score partly measures recall; and reward hacking lets a lazy policy satisfy the verifier without doing the task. The nastiest is misalignment between the prompt and the grader, like an eval that asks for no commas and an answer in Hindi at once, or a verifier whose sentence splitter cannot parse the format, so the only way to a perfect score is to game it. Heiner's prescription is to bring domain expertise, align tools with prompts, and pay for real human evaluation, holding both benchmark writers and the labs to a higher standard.

Speaker info:
- https://x.com/nickheiner
- https://www.linkedin.com/in/nick-heiner-3874055a/
- https://www.nickheiner.com/

Timestamps:
0:00 - The benchmark versus reality gap
0:55 - Why the word benchmaxxing exists
2:38 - Reading a benchmark fairly
3:14 - Antipattern: broken tasks
4:41 - Antipattern: contamination
5:57 - Antipattern: reward hacking
6:23 - Misaligned prompts and verifiers
10:40 - Benchmaxxing as a two way street
13:14 - Domain expertise and getting it right
15:47 - Human eval and a higher standard

## MCP Apps: Extending the Frontier — Ido Salomon & Liad Yosef

- Upload date: 2026-08-02
- Video: https://www.youtube.com/watch?v=-jY2T2PiJBE
- Transcript: raw/20260802_-jY2T2PiJBE/-jY2T2PiJBE.en-orig.vtt
- Metadata: raw/20260802_-jY2T2PiJBE/-jY2T2PiJBE.info.json

Chat and coding assistants still hand you walls of text when a button, a chart, or a small interactive view would say it faster. Liad Yosef, who co created MCP UI, walks through MCP Apps: a way for an MCP server to return a real interactive interface instead of a block of text, built on the MCP UI project he started and now shaped through an open working group in the MCP committee. A tool call links to a registered resource, the host renders it as a web component, and clicks flow back into the agentic loop, so the same funnel that would take a paragraph to explain becomes something you can see and act on at a glance.

The payoff is write once, run anywhere. Because it is a standard rather than a bespoke integration, a UI a server ships shows up across every host that supports it, and Yosef points to adoption by hosts and tools already in the ecosystem. He is candid that the spec is still evolving, with live work on how the app and the chat talk to each other and how apps interoperate, and an open invitation to contribute. The bigger bet is distribution: when a host reaches hundreds of millions of weekly users, a server that speaks MCP Apps reaches all of them at once.

Speaker info:
Liad Yosef
- https://x.com/liadyosef
- https://linkedin.com/in/liadyosef
- https://ora.ai

Ido Salomon
- https://x.com/idosal1
- https://www.linkedin.com/in/ido-salomon/

Timestamps:
0:00 - Why we need MCP Apps
1:52 - From walls of text to interactive views
2:29 - MCP UI, created and adopted
4:26 - An open working group in the MCP committee
5:04 - How a tool call becomes an interface
6:31 - Standardizing the flow
8:52 - The architecture: resources and web components
10:10 - Consuming apps through the browser
14:29 - What's still evolving in the spec
16:07 - Interoperability across hosts
17:14 - Write once, reach hundreds of millions

## Teaching AI to Find Real Vulnerabilities — Prof. David Brumley, Bugcrowd

- Upload date: 2026-08-01
- Video: https://www.youtube.com/watch?v=ZFxh7sqbUZo
- Transcript: raw/20260801_ZFxh7sqbUZo/ZFxh7sqbUZo.en-orig.vtt
- Metadata: raw/20260801_ZFxh7sqbUZo/ZFxh7sqbUZo.info.json

David Brumley has spent two decades turning people into hackers, from founding picoCTF to recruiting pwn2own winners at Carnegie Mellon, and his argument is that you teach a model to hack the same way: a ladder of tasks that climbs from triggering a crash to reading and writing arbitrary memory to a full working exploit. The catch is measurement. Hacking has no single answer, so the usual benchmark setup breaks down when a target has multiple vulnerabilities and a language model can always claim it found one, and grading oracles that just ask the model whether it succeeded are hopeless.

So Brumley's team builds real reinforcement learning environments instead: reproducible, sandboxed, and scored by deterministic graders that check whether an exploit actually triggers the specific bug, borrowing precision and recall from his DARPA Cyber Challenge work where he designed the scoring. He shows it on V8, the JavaScript engine in Chrome, running against 41 real vulnerabilities where the strongest models reached about 95% and, in the hard cases, produced genuine out of sandbox exploits including a real zero day. The point that lands is a warning against benchmaxxing security: build environments grounded in real bugs and honest graders, because that is what separates a model that looks like it can hack from one that actually can.

Speaker info:
- https://www.linkedin.com/in/thedavidbrumley

Timestamps:
0:00 - Two decades of teaching hacking
1:54 - From CTF scoreboards to CMU
3:34 - A ladder of exploitation tasks
6:44 - Why measuring hacking is hard
7:46 - Flawed grading oracles
10:30 - When a target has many bugs
13:22 - Deterministic graders and AIXCC scoring
14:49 - Precision and recall for vulnerabilities
17:35 - Attacking V8 in Chrome
21:10 - 41 vulnerabilities and a real zero day
25:24 - Don't benchmaxx security

## Rethinking Environments for Long-Horizon Work — Rayan Garg, Theta Software

- Upload date: 2026-08-01
- Video: https://www.youtube.com/watch?v=2aS7aKoXn64
- Transcript: raw/20260801_2aS7aKoXn64/2aS7aKoXn64.en-orig.vtt
- Metadata: raw/20260801_2aS7aKoXn64/2aS7aKoXn64.info.json

Everyone wants agents that handle long horizon work, but Rayan Garg starts with the awkward question of what long horizon even means. One popular answer measures the time horizon as the task length at which an agent crosses a success threshold, like the sixteen hour mark, which is a useful endpoint but a noisy one, since human time estimates vary and the same wall clock hides very different amounts of real difficulty. How you choose to measure this has an outsized effect on what you conclude about a model.

From there Theta Software's work is about designing the environments and verifiers that make those measurements honest. A task can be artificially stretched by forcing serial dependencies, or made genuinely hard when a bad early query cascades through everything after it, and as environments grow more complex, standardized evaluation gets harder and correctness is best verified from the final state rather than a judge's guess. Garg walks through collapsing a huge state space with sample trajectories, being careful that judges do not see information they should not, and reusing agents to sift artifacts like CI logs. The recurring principle is that long horizon progress lives or dies on environment and verifier design, not on the headline benchmark number.

Speaker info:
- https://x.com/RayanGarg
- https://www.linkedin.com/in/rayan-garg/

Timestamps:
0:00 - What does long horizon mean?
1:13 - Time horizon and the threshold metric
3:17 - Why the metric is noisy
4:20 - Measuring what actually matters
6:38 - Creating tasks and environments
7:42 - When a bad early step cascades
10:01 - Why standardized evaluation is hard
11:17 - Verifying from the final state
13:46 - Judges, tools, and reused agents
17:45 - Rubrics, QA, and careful grading

## Emulated: The Data for Fully Autonomous Software Engineers and Companies — Joseph Wang

- Upload date: 2026-07-31
- Video: https://www.youtube.com/watch?v=zkX03APVj0M
- Transcript: raw/20260731_zkX03APVj0M/zkX03APVj0M.en-orig.vtt
- Metadata: raw/20260731_zkX03APVj0M/zkX03APVj0M.info.json

To train an agent that can run production software, you need training data that looks like production, and that is what Joseph Wang's team at Emulated builds. Coming from network infrastructure backgrounds, they know what happens when something like a database goes down at scale, and they argue that current post training environments do not capture it. A real task is not a tidy code diff; it is fifty to a hundred turns of solving live traffic while distributed nodes fail, configs conflict, and unforeseen problems appear mid incident.

So Emulated simulates whole companies. Imagine acting as an engineer inside a cloud provider or an infrastructure service, provisioning resources across VPCs, subnets, and security groups, meeting real bars around cost and deployment, and keeping a service alive as it grows, all inside a high fidelity environment rather than a stub. Wang's bet is that domain expertise plus faithful simulation is what lets agents learn the messy, end to end reality of infrastructure work, and he closes looking for people who have trained models or run real infrastructure to help push that fidelity further across more domains.

Speaker info:
- https://emulated.so/

Timestamps:
0:00 - Useful work over longer horizons
1:20 - Backgrounds in network infrastructure
2:26 - How environments shape capability
3:16 - Fifty to a hundred turn tasks
4:59 - Why real incidents are messy
7:11 - Real infrastructure isn't a code diff
7:40 - Acting as an engineer inside the cloud
9:37 - Deployment, cost, and scaling bars
13:29 - Why it's called Emulated
15:01 - Simulating full companies

## The Base Model Is Dead — Varun Singh, Arcee AI

- Upload date: 2026-07-31
- Video: https://www.youtube.com/watch?v=xbPriQWXtWM
- Transcript: raw/20260731_xbPriQWXtWM/xbPriQWXtWM.en-orig.vtt
- Metadata: raw/20260731_xbPriQWXtWM/xbPriQWXtWM.info.json

The old story is that a base model is a mirror of the internet, a good model of human web text that everything else gets bolted onto. Varun Singh, who leads pre-training at Arcee AI, argues that story is dead: no modern base model reflects the web the way GPT-3 once did. Instruction data and synthetic reasoning traces have moved earlier and earlier into training, and a distinct mid-training stage has emerged for longer datapoints that look much more like the downstream capabilities you actually want. Reading recent open recipes, from Nemotron to Kimi K2, the pattern is clear: raw web text is taking a backseat.

The rest of the talk is what that shift does to how you build. Once reinforcement learning became the thing that got models to reason, the base model stopped being a cherry on top and started needing to carry the prior that RL builds on, which changes the data mix and pulls post-training-flavored data forward. Singh walks through the practical pitfalls his team hit training the Trinity series, like getting the balancing coefficients right and establishing stable representations early so the model is prepared for what it must compose during RL. The message is that as capabilities advance, the base model's job keeps redefining itself, and pretending it still just mirrors the internet will cost you.

Speaker info:
- https://x.com/stochasticchasm
- https://www.linkedin.com/in/varun-singh-cs

Timestamps:
0:00 - The base model as a mirror of the web
1:26 - How knowledge accumulates in training
2:49 - When instruction data moves earlier
4:11 - After o1: RL and reasoning
5:41 - What prior the base model must carry
6:18 - Filtering web text, adding synthetic
8:01 - Reading the open data recipes
9:41 - Lessons from training Trinity
12:02 - Balancing coefficients and early stability
13:30 - Why RL keeps raising the stakes
15:55 - The base model's shifting job

## Ending AI Slop — Thais Castello Branco, Taste Labs

- Upload date: 2026-07-31
- Video: https://www.youtube.com/watch?v=lCBf9slCanI
- Transcript: raw/20260731_lCBf9slCanI/lCBf9slCanI.en-orig.vtt
- Metadata: raw/20260731_lCBf9slCanI/lCBf9slCanI.info.json

Thais Castello Branco's starting point is that AI is still badly behind on the subjective work, the writing and design where quality is real but hard to pin down, and that ending the slop means building data and reinforcement environments for taste. She sorts domains along a spectrum: at one end things that verify and execute cleanly, at the other pure preference with no ground truth, and most valuable work sits in between. The move that makes taste tractable is decomposition, breaking something like a brand or a page into elements that can each be graded against an original rather than judged whole.

The deeper problem she names is collapse to the mean. A model optimizing for the most likely output drifts toward the average and quietly kills the creativity that good design depends on, so the goal is data and rewards that reward breaking from the obvious when the situation calls for it. Taste Labs builds this by turning expert judgment into structured, high signal preference data, pairing it with human QA where reviewers tie their commentary to specific choices, and being careful that preference signal stays rich instead of noisy. Her argument is that as more subjective domains become measurable this way, taste becomes something you can actually train.

Speaker info:
- https://x.com/thaiscbranco_
- https://www.linkedin.com/in/thais-castello-branco/

Timestamps:
0:00 - What ending AI slop means
1:06 - Working with frontier labs on taste
2:33 - The verifiable to preference spectrum
3:38 - Decomposing design to grade it
5:30 - Verifying whether something is on brand
7:40 - Collapse to the mean
9:18 - Shifting preference toward verifiable
11:25 - Building a preference vector
13:05 - Human QA tied to specific choices
15:00 - Training taste in subjective domains

## Learning on the Job: The Future of Post-Training — Raymond Feng, Applied Compute

- Upload date: 2026-07-31
- Video: https://www.youtube.com/watch?v=k35LeKZEhiE
- Transcript: raw/20260731_k35LeKZEhiE/k35LeKZEhiE.en-orig.vtt
- Metadata: raw/20260731_k35LeKZEhiE/k35LeKZEhiE.info.json

The next step after a model ships is teaching it to keep learning on the job, and Raymond Feng lays out how Applied Compute trains custom models with reinforcement learning that plug into whatever harness an enterprise already runs. The setup is an orchestrator that fans interactions out to inference engines, collects the graded rollouts, and feeds a training engine that updates the weights, the same GRPO style loop used for RL today, but pointed at real multi turn, long horizon work rather than toy question and answer pairs. The promise is a model you deploy once that adapts to a specific company's tasks.

The hard parts are all about the environment. Feng is candid about reward hacking, where a model learns to time out a tool or exploit a scoring gap instead of doing the task, and about the trouble of faithfully replicating a production environment so training reflects reality. He walks through why replaying real customer interactions is tempting but breaks on non replayability and off policy data, and where automated data pipelines and self evaluation might take this. The vision at the end is a model that learns from every interaction it has, treating each nook and cranny of the job as new training signal.

Speaker info:
- https://x.com/raymondmfeng

Timestamps:
0:00 - Learning on the job
0:39 - Custom models inside your harness
2:37 - Deploy once and adapt
2:49 - The RL training loop
4:40 - Toward longer horizon tasks
6:48 - Reward hacking in practice
9:06 - Replicating production environments
9:45 - Why replaying real traffic is hard
11:57 - Non-replayability and off-policy data
13:41 - Automated data pipelines
15:24 - A model that learns every interaction

## Benchmarks: The Good, the Bad, and the Ugly — Ali Khial, G2i

- Upload date: 2026-07-31
- Video: https://www.youtube.com/watch?v=jWq-aZIU0kM
- Transcript: raw/20260731_jWq-aZIU0kM/jWq-aZIU0kM.en-orig.vtt
- Metadata: raw/20260731_jWq-aZIU0kM/jWq-aZIU0kM.info.json

Ali Khial took three of the best engineers at G2i, pointed them at popular coding benchmarks, and hit a wall of tasks that were either too ambiguous to grade or quietly broken. That experience is the spine of this talk: a benchmark starts as a spec, solutions get verified and graded, and the results rank models, but only if the harness is actually creating a fair test rather than an unfair one. He shows real examples where an instruction is so vague that a correct patch gets rejected, or a test checks something as arbitrary as how a variable is named, and notes that a meaningful share of tasks he examined had genuinely good answers marked wrong.

The danger is that models are increasingly good at gaming exactly this, hunting down the test and satisfying it rather than solving the problem, which opens a quality gap that public leaderboards hide. Khial lays out the principles he now uses for benchmarks worth trusting: be precise where precision matters and loose where it does not, keep a private held out set so nothing leaks from public GitHub repos, and hold the whole thing to production grade. His point is not that benchmarks are useless but that the ones we lean on are not there yet, and building better ones is the work.

Speaker info:
- https://www.linkedin.com/in/ali-khial/

Timestamps:
0:00 - The good, the bad, and the ugly
1:27 - Testing with our best engineers
2:30 - A benchmark as a spec
3:37 - When instructions are too ambiguous
4:44 - Tests that check the wrong thing
6:12 - Good answers marked wrong
7:03 - Models learning to game the test
8:08 - The quality gap leaderboards hide
9:03 - Precise where it matters
10:47 - Keeping a private held out set
11:13 - Principles for benchmarks worth trusting

## Data and Environment Curation for Post-Training LLMs — Mahesh Sathiamoorthy, Bespoke Labs

- Upload date: 2026-07-31
- Video: https://www.youtube.com/watch?v=ewtOo0scUh0
- Transcript: raw/20260731_ewtOo0scUh0/ewtOo0scUh0.en-orig.vtt
- Metadata: raw/20260731_ewtOo0scUh0/ewtOo0scUh0.info.json

Mahesh Sathiamoorthy's pitch is to stand in the researcher's shoes: the hard part of post-training is not the algorithm but the data and the environments that feed it. As agents get pushed to run autonomously for hours, something eventually falls over, and reinforcement learning is the tool for stretching that reliability, but RL environments are really just data in a different shape. Bespoke Labs works on curating both, from supervised fine-tuning sets to the environments models learn in.

He grounds it in OpenThoughts, the widely used reasoning dataset his team built, and the counterintuitive lessons that came out of curating it: diversity of reasoning traces matters, keeping multiple answers per question helps, and the obvious recipe often is not the best one. A favorite example is teaching a model to reason about credit card compliance, where fine-tuning on the right tagged data lifted the compliance metrics that a raw model kept getting wrong. The through line, supported by their Curator tooling, is that a disciplined curation stack, not just more compute, is what turns a base model into a capable post-trained one.

Speaker info:
- https://x.com/madiator
- https://linkedin.com/in/smaheswaran
- https://smahesh.com

Timestamps:
0:00 - Standing in the researcher's shoes
1:30 - Post-training at Bespoke Labs
3:13 - When agents fall over on long tasks
4:44 - RL environments as data
6:29 - Building OpenThoughts
7:36 - Finding a curation recipe
10:27 - Counterintuitive lessons
13:49 - A credit card compliance example
16:13 - Curating reasoning data with Curator
17:16 - The full curation stack

## What's Next After RLHF? — Diogo Almeida, TypeSafe AI

- Upload date: 2026-07-31
- Video: https://www.youtube.com/watch?v=cJ0EOzey--o
- Transcript: raw/20260731_cJ0EOzey--o/cJ0EOzey--o.en-orig.vtt
- Metadata: raw/20260731_cJ0EOzey--o/cJ0EOzey--o.info.json

RLHF made models that are extraordinary at pleasing the human in the loop, and Diogo Almeida, a GPT-4 co author, argues that is exactly the problem. Optimizing for human preference optimizes for engagement and for overpromising, the same pressure that makes a model confidently agree that a fart audio file is a symphony. That produces two camps: one where models act as assistants with a human catching mistakes, where RLHF shines, and one where they operate autonomously with real stakes, where the same instinct to please quietly becomes a liability.

So what comes next is not the Claude Code era but a shift in what you optimize. Almeida frames it through Sutton's bitter lesson: the task matters more than the data, and reinforcement learning with verifiable rewards points the model at real automation instead of human approval. He is careful that pre trained models are already incredibly capable and that the trap is bolting preference optimization on top, which teaches confidence and drops modes. The through line is that assistance and automation pull in different directions in optimization space, and the field is only starting to say plainly which one it is building.

Speaker info:
- https://x.com/CompleteSkeptic
- https://www.linkedin.com/in/diogomda/
- https://typesafe.ai/

Timestamps:
0:00 - Not the Claude Code era
1:40 - The state of the field
3:14 - Two camps: assistance and autonomy
4:31 - Why models please the human in the loop
6:37 - How RLHF actually works
7:31 - Preference versus what's true
8:10 - When the consequences get real
8:47 - So what's next
9:35 - Assistance is not automation
14:31 - Is pre-training the problem?
15:43 - RLVR and Sutton's bitter lesson

## Data Quality Is the Compute Multiplier — Ari Morcos, DatologyAI

- Upload date: 2026-07-31
- Video: https://www.youtube.com/watch?v=_PdK6x7PQNM
- Transcript: raw/20260731__PdK6x7PQNM/_PdK6x7PQNM.en-orig.vtt
- Metadata: raw/20260731__PdK6x7PQNM/_PdK6x7PQNM.info.json

Swap compute for data on the scaling curve and the same money buys a better model, which is why Ari Morcos calls data quality the compute multiplier and the most underinvested part of training. His frame is an oil refinery for data rather than a firehose: clean, curate, create, and compose, with quality classifiers, deduplication, and synthetic generation each earning their place, and the sequencing across stages mattering as much as any single step. The scarce resource now is not tokens but signal per token, and finding data that is optimal for a given target is where the leverage hides.

The proof points are concrete. Better curated data lets a small multilingual model beat far larger ones trained on many more tokens, and it buys real inference efficiency because a model reaches the same quality with less. Morcos points to DatologyAI's customer results, from Thomson Reuters gaining on proprietary legal data in mid-training to Arcee's Trinity reaching the open frontier on public data alone. The closing argument is blunt: it is cheaper to manufacture high quality data than to buy more compute, so data curation is quietly shaping the future of model training.

Speaker info:
- https://x.com/arimorcos
- https://www.linkedin.com/in/arimorcos/
- http://www.arimorcos.com/

Timestamps:
0:00 - Data is all we think about
0:52 - Why good data became scarce
2:19 - Swapping compute for data on the curve
3:48 - An oil refinery for data
5:52 - Curation work at DatologyAI
6:54 - Proof: small models beating bigger ones
8:58 - Inference efficiency from better data
9:24 - Multilingual gains
12:16 - Synthetic data done right
14:10 - Thomson Reuters and Arcee results
17:43 - Cheaper than buying compute

## Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It — Dan Fu and Olive Song

- Upload date: 2026-07-31
- Video: https://www.youtube.com/watch?v=AVMr9PMINyo
- Transcript: raw/20260731_AVMr9PMINyo/AVMr9PMINyo.en-orig.vtt
- Metadata: raw/20260731_AVMr9PMINyo/AVMr9PMINyo.info.json

In this conversation, Olive Song, who leads reinforcement learning at MiniMax, opens up the stack behind the company's open weight models and the infrastructure that serves them. Her starting point is a belief in open source: put the weights out, let builders optimize on them, and share the capability widely. From there she walks through what it takes for a model to land well, from agentic coding that also understands and builds games, to computer use problems trained with RL against environments like OS World.

Much of the discussion is the unglamorous engineering that makes a launch real. When a model ships, the team wants the inference stack ready on day zero, which means writing and tuning GPU kernels, working through benchmarks like a parallel kernel bench, and threading optimization into everything from KV cache handling to routing. Song also talks through multimodality and the training pitfalls that come with it, such as text and vision collapsing after training unless you train both modalities together, and reflects on longer horizon tasks like replicating a twelve hour run. She closes optimistic that open models are closing the gap faster than a year ago would have suggested.

Speaker info:
- https://x.com/olive_jy_song

Timestamps:
0:00 - Introducing the RL lead at MiniMax
1:17 - Why open source and open weights
3:45 - What builders are doing with the model
4:11 - A model that builds games
5:12 - Computer use and OS World
5:49 - Writing GPU kernels
6:25 - Parallel kernel bench
7:28 - A day zero inference stack
9:34 - Optimization across the stack
10:47 - Multimodality and training collapse
14:10 - Replicating a twelve hour run
17:22 - Where open models go next

## Reinforcement Learning without Verifiable Rewards — Will Brown, Prime Intellect

- Upload date: 2026-07-31
- Video: https://www.youtube.com/watch?v=AQv3qRCG6Gw
- Transcript: raw/20260731_AQv3qRCG6Gw/AQv3qRCG6Gw.en-orig.vtt
- Metadata: raw/20260731_AQv3qRCG6Gw/AQv3qRCG6Gw.info.json

Reinforcement learning has been easy to sell where the answer is checkable, like math or code, and Will Brown's talk is about everything else. Most valuable tasks have no clean verifier, so Prime Intellect's work is on how you build reward signal when there is no ground truth waiting. He frames RL simply first, a model acting in a harness with tools and skills, getting a reward, and nudging its weights, then asks how you keep climbing once you leave the verifiable island behind.

His answer leans on environments as the anchor. You can set up judges, generate question and answer pairs grounded in real documents and repos, and use a reverse direction trick where you hide something, like a bug or a backdoor, so the model can learn to find it again, which conveniently gives you a difficulty dial to keep tasks not too easy and not too hard. He is direct about the dangers: reward hacking will find you if you are not careful, so you inspect traces, run small experiments, and bring in expert understanding. The goal he keeps returning to is making this a real science, with open models and shared benchmarks, where environments turn into new tasks and higher levels of ability.

Speaker info:
- https://x.com/willccbb
- https://www.linkedin.com/in/willcb/
- https://willcb.com

Timestamps:
0:00 - RL without verifiable rewards
1:17 - How RL works, simply
2:43 - The tooling that powers it
4:13 - Where verifiable rewards run out
6:24 - Being careful about reward design
8:04 - Making RL a science
9:20 - Judges and grounded question answer pairs
10:46 - The reverse direction trick
14:19 - Calibrating difficulty
15:08 - Hunting for reward hacks
18:27 - Environments as the anchor

## fighting slop with slop — Vaibhav Gupta, Boundary

- Upload date: 2026-07-31
- Video: https://www.youtube.com/watch?v=AMiyLItEtLA
- Transcript: raw/20260731_AMiyLItEtLA/AMiyLItEtLA.en-orig.vtt
- Metadata: raw/20260731_AMiyLItEtLA/AMiyLItEtLA.info.json

You cannot tell great engineers what to do, and you increasingly cannot tell what an agent did either, so Vaibhav Gupta's answer is to fight slop with slop. At Boundary the team turns the same cheap, sloppy generation loose as a tool: agents that run constantly over the transcripts of other agents, flagging hallucinations, spotting which tool calls produced errors, and comparing which approaches produced fewer. He pairs that with hard invariants, the design docs, rules, and CLI checks that do not change for months and tell you exactly where a codebase stops converging, so the messy detection layer sits on top of something stable.

The deeper move is to attack the foundational layer from first principles. Instead of trusting generated code, he leans on type systems that make whole classes of mistakes impossible: types get inferred without you writing them, a division by zero is guaranteed to be handled or the code will not build, and there are no silent unknowns left for an agent to guess at. That is the bet behind BAML, which lets you work across Python, TypeScript, or Rust with strong boundaries around each function so an agent can move fast inside walls it cannot breach. His closing challenge is to go build these sloppy tools yourself and constrain the systems underneath them, because that is what actually wins the war on slop.

Speaker info:
- https://x.com/vaibcode
- https://www.linkedin.com/in/vaigup
- https://www.youtube.com/@boundaryml

Timestamps:
0:00 - Fighting slop with slop
0:27 - Code reviews and invariants
2:08 - Building rules that don't change
3:00 - Design docs with notifications
4:03 - CLI tools that catch where things break
5:08 - Agents reading agent transcripts
5:57 - Detecting hallucinations and errors
9:24 - Attacking the foundational layer
11:03 - Execution traces from first principles
14:26 - Type safe tools across platforms
15:42 - Making whole error classes impossible
17:57 - BAML across languages
20:37 - Go build the sloppy tools

## Verifiable Environments for AI in Biology — Kenny Workman, LatchBio

- Upload date: 2026-07-31
- Video: https://www.youtube.com/watch?v=3ZMUiFaQ3qg
- Transcript: raw/20260731_3ZMUiFaQ3qg/3ZMUiFaQ3qg.en-orig.vtt
- Metadata: raw/20260731_3ZMUiFaQ3qg/3ZMUiFaQ3qg.info.json

A single spatial biology run can yield two to six terabytes of data, far more than a scientist can eyeball, and Kenny Workman argues that this is the raw material for teaching AI to actually do science. LatchBio, five years deep in pharma, treats experimental biology as a verifiable substrate: lay a chunk of a tumor over a sequencing surface and you get a giant matrix of numbers whose analysis has a right answer, which is exactly what you need to benchmark and improve a model. They adapted coding models into biology tools and built benchmarks like sequencing based spatial analysis, and found what everyone in post training now knows, that frontier models cannot yet be trusted with this and that measurement is what drives progress.

The reason biology is hard is that it is messy and the field rarely agrees on the answer, so much of the work is designing tasks where reasoning, not memorized knowledge, is what gets rewarded. Workman walks through trajectory data from real scientists, tasks like finding the part of a tumor that matters, and why an ambiguous prompt quietly makes a benchmark uninformative. He also gets candid about biosecurity, where model refusals are their own evaluation problem and red team tasks have to be handled carefully, and frames the whole effort as a flywheel: better benchmarks, better tools, more of the program landscape indexed, repeat.

Speaker info:
- https://x.com/kenbwork
- https://www.linkedin.com/in/kennyworkman
- https://kenbw.com/

Timestamps:
0:00 - Terabytes of experimental data
1:41 - Decomposing a new paper into tasks
2:44 - A verifiable substrate for science
3:23 - Five years in pharma
4:13 - Coding models as biology tools
5:40 - Why frontier models can't be trusted yet
6:44 - Sequencing based spatial analysis
9:16 - Reasoning, not memorized knowledge
10:07 - Trajectory data from real scientists
12:14 - Why biology tasks are messy
15:36 - Biosecurity and refusals

## Scaling to Long Horizons — Ross Taylor & Chengxi Taylor, General Reasoning

- Upload date: 2026-07-31
- Video: https://www.youtube.com/watch?v=2bvtay8wGYI
- Transcript: raw/20260731_2bvtay8wGYI/2bvtay8wGYI.en-orig.vtt
- Metadata: raw/20260731_2bvtay8wGYI/2bvtay8wGYI.info.json

Ross Taylor opens with some history: back in 2022 he worked on Galactica, an early large model for science that briefly crossed the Rubicon on curated high quality data and intermediate reasoning tokens before the reaction overshadowed the work. That obsession, optimizing what happens between the question and the answer, is where this talk on long horizon reinforcement learning picks up. He and Chengxi Taylor of General Reasoning treat long horizon less as a benchmark and more as a mindset: if you want agents that stay coherent over hours, you have to be patient about signal and deliberate about how you spend tokens.

The mechanics they walk through are the ones that make long rollouts trainable. Value models reduce variance and help with credit assignment, bootstrapping pulls signal out of sparse rewards, and the real constraint becomes the tradeoff between off policy staleness and GPU utilization as sequences get longer. They make it concrete with a task where frontier models were handed real money to trade football matches and did poorly, exposing how little the environment was actually simulated. The takeaway is that scaling to long horizons demands better environments and simulation, not just bigger context windows, and they point listeners to openreward.ai to go deeper.

Speaker info:
- Ross Taylor (General Reasoning):
  - https://x.com/rosstaylor90
  - https://www.linkedin.com/in/rosstaylor90/
  - https://rossjtaylor.com
- Chengxi Taylor (General Reasoning):
  - https://x.com/chengxitaylor
  - https://www.linkedin.com/in/chengxi-taylor/
  - https://www.chengxitaylor.com/

Timestamps:
0:00 - Introduction and a look back
1:57 - The Galactica story
5:15 - Curated data and thinking tokens
8:09 - What got RL cooking
9:12 - Long horizon as a mindset
10:16 - Why value models help
11:08 - Credit assignment and bootstrapping
12:38 - Trading football matches for real money
13:44 - Why models struggled
14:36 - Off policy staleness versus GPU use
16:18 - openreward.ai and what's next

## Your Finance Agent's Bottleneck Is You — Ramana Siddanth Emani, Auditoria AI

- Upload date: 2026-07-30
- Video: https://www.youtube.com/watch?v=z0sh8HyTrDo
- Transcript: raw/20260730_z0sh8HyTrDo/z0sh8HyTrDo.en-orig.vtt
- Metadata: raw/20260730_z0sh8HyTrDo/z0sh8HyTrDo.info.json

The slowest part of shipping a production finance agent is not the model or the GPUs, it is you, the developer in the loop. Ramana Siddanth Emani's point is that the same agent harnesses you use to build products can automate your own developer loop. Coding agents can multiply how much you ship; run an army of them across separate git worktrees and they clear tasks in parallel, with skills making sure each one uses the right patterns.

The tasks come from where they already live, QA reports, Jira tickets, GitHub pull requests, and a sub agent pulls the traces and logs, writes and runs end to end tests, builds, and reports back, needing your context only at a few steps. Point this at your bug queue and a month later you have shipped far more, having stepped further out of the loop as the agents improve, while keeping a human as the final verifier. At Auditoria, where the work is finance, that means agents talking to agents and reconciling source data, so you spend your time verifying rather than grinding.

Speaker info:
- https://x.com/siddanth2486
- https://www.linkedin.com/in/siddanth-emani

Timestamps:
0:00 - Your bottleneck is you
1:05 - From bugs to pilots to production
2:37 - Automating the developer loop
3:03 - Coding agents that multiply output
3:39 - Skills for the right patterns
4:22 - Sub agents and where tasks come from
5:18 - Pulling traces, testing, reporting back
7:56 - Auditoria in the finance sector
9:04 - Stepping out of the loop safely
11:35 - Turning customer patterns into features
13:04 - Keep a human as verifier

## Build for the Memo, Not the Demo — Shawn Chan, China Resources Holdings

- Upload date: 2026-07-30
- Video: https://www.youtube.com/watch?v=tJFjeMBKbIY
- Transcript: raw/20260730_tJFjeMBKbIY/tJFjeMBKbIY.en-orig.vtt
- Metadata: raw/20260730_tJFjeMBKbIY/tJFjeMBKbIY.info.json

When a company is about to spend $100 million, Shawn Chan is the person in the room deciding whether it happens, and after fifteen years and roughly 200 investment committees he can spot the flaw fast. Now some of the decks in front of him are AI generated: cleaner formatting, never defensive, and confidently wrong. His frame is the difference between a demo and a memo. A demo is a beautiful confident slice built to impress; a memo is what survives a room whose entire job is to find what breaks. One marketing demo with a single wrong sentence, he reminds you, once erased enormous value the moment the market noticed.

So he lays out what an AI product needs to pass the memo test. Not every source deserves equal trust, since an audited filing is not a number from a group chat. Figures have to reconcile, and a contradiction between two numbers is not a bug but the most important signal in the room. Facts and guesses must stay labeled, because across three drafts an estimate quietly hardens into a fact nobody remembers assuming. Attach provenance rather than a citation tab, lock who claimed what, and the product that wins is the one that lets someone approve a deal without opening seven tabs at midnight.

Speaker info:
- https://www.linkedin.com/in/shawn-chan-2b58a9129/

Timestamps:
0:00 - A fifteen year confession
3:27 - Two hundred investment committees
4:22 - Money follows trust
5:46 - Two machines: the demo and the memo
7:31 - When one wrong sentence costs billions
9:45 - Not every source deserves equal trust
11:22 - The numbers have to agree
14:59 - Facts and guesses stay separate
17:06 - When fake citations reach a court
19:21 - The airline chatbot that made a promise
21:30 - Attach provenance, not a citation tab
22:52 - The products that will win

## First Steps Toward Automated AI Research — Richard Socher, CEO Recursive AI

- Upload date: 2026-07-30
- Video: https://www.youtube.com/watch?v=pWXUkLP9uWM
- Transcript: raw/20260730_pWXUkLP9uWM/pWXUkLP9uWM.en-orig.vtt
- Metadata: raw/20260730_pWXUkLP9uWM/pWXUkLP9uWM.info.json

Humanity compressed the road from the enlightenment to the moon landing into a few hundred years, and Richard Socher's wager is that automating research compresses it again. He frames it through open ended evolution and Popper: science advances by trying things, finding the shortcomings, and fixing them, and an agent swarm can run that loop across medicine, economics, astrophysics, and more without any single person bottlenecking a field. He calls the goal a Eureka machine, and argues that rethinking the tools around it, web search that returns usable context instead of ten blue links, browsers, and GPUs, is part of building it.

The proof points are recursive self improvement, where a system improves its own code, harness, and results and then does it again over longer horizons. He shows small but concrete wins: an automated loop that lifts a model's accuracy well past a naive baseline, architecture search that trades hand tuning for a system that finds better designs, and CUDA kernel work that surfaced real improvements. He is careful that these are early samples, not a finished machine, and that the field is far from general across all of science, but the direction is the point, and he ends with an open invitation to help build it.

Speaker info:
- https://x.com/RichardSocher
- https://www.linkedin.com/in/richardsocher
- https://you.com

Timestamps:
0:00 - Automating research for humanity
1:41 - Why this matters now
2:19 - Compressing the timeline of progress
4:28 - Technoptimism and material limits
6:22 - Popper and open ended evolution
9:07 - The Eureka machine
10:39 - Rethinking search, browsers, and GPUs
13:41 - Recursive self improvement
14:46 - Proof point: improving a model
16:39 - Proof point: architecture search
17:16 - Proof point: CUDA kernels
19:11 - How far we still are, and an invitation

## Let's integrate AI Agents in Event-Sourced Systems — Divakar Kumar, FlyersSoft

- Upload date: 2026-07-30
- Video: https://www.youtube.com/watch?v=o6U_2vd967Y
- Transcript: raw/20260730_o6U_2vd967Y/o6U_2vd967Y.en-orig.vtt
- Metadata: raw/20260730_o6U_2vd967Y/o6U_2vd967Y.info.json

A card gets declined and no one, including the customer, can say exactly why. That gray zone is where Divakar Kumar points his agents. In a payments and fraud system, a rule based engine and an ML model already score most transactions cleanly; the hard cases are the ambiguous ones that neither can resolve. His approach adds an agentic layer on top of an existing event sourced architecture rather than replacing it, so the bounded contexts already in the system, transaction, device, and account, become the context the agents reason over.

Events flow through change feeds into projections and a semantic layer that the agents read, communicating asynchronously through a message broker in a saga style loop. A risk analyzer agent, a second agent that reaches a verdict, and a third work the case while guarding against infinite loops and keeping memory short, all runnable serverless. The takeaway is architectural: event sourcing already carries the state and history an agent needs, so the cleanest way to add judgment to a production system is to layer agents onto the events you are already emitting.

Speaker info:
- https://www.linkedin.com/in/divakar-kumar/
- https://iamdivakarkumar.com

Timestamps:
0:00 - Introduction: adding agents to an existing system
1:20 - A declined transaction you can't explain
3:04 - Where rule based and ML systems fall short
5:40 - Handling the gray zone with agents
5:53 - Bounded contexts: transaction, device, account
8:24 - Event sourcing and change feeds
10:57 - Building the semantic layer
13:16 - Avoiding infinite loops
14:07 - The risk analyzer and verdict agents
15:24 - The saga orchestration loop
19:00 - Putting the architecture together

## Wearing the Agent: From Group Chats to Glasses — Sai Krishna Rallabandi

- Upload date: 2026-07-29
- Video: https://www.youtube.com/watch?v=s67bE2Ur3bY
- Transcript: raw/20260729_s67bE2Ur3bY/s67bE2Ur3bY.en-orig.vtt
- Metadata: raw/20260729_s67bE2Ur3bY/s67bE2Ur3bY.info.json

Almost every agent today is built for one user, and Sai Krishna Rallabandi has spent about eight months on what breaks when you drop one into a group chat instead. Running a personal agent across a real group, and eventually onto glasses, forces two hard problems. The first is memory: conversations that last for days across several people, where the agent has to track who said what and surface only what is relevant without bloating its context.

The second is security, and it is where the talk digs in. He points to a finding that two skills, each safe on its own, can collide once they share infrastructure, so a reporting agent leaks information at low frequency. His defense is to have an agent read everything and design a guard, then fine tune a small model with a per user adapter that only releases information appropriate to the context and catches prompt injection that regex would miss. The through line is that group and wearable settings break the single user assumptions most agent harnesses are built on, so memory and security have to be redesigned around the group.

Speaker info:
- https://x.com/Saikallis9012
- https://www.linkedin.com/in/sai-krishna-rallabandi-8595418b/
- https://saikrishnarallabandi.github.io/

Timestamps:
0:00 - Introduction: agents for groups, not one user
1:28 - Why single user agents fall short
2:45 - Eight months in a real group chat
3:47 - What changes when the agent joins a group
5:17 - Two problems: guarding and memory
5:55 - Securing an agentic system
7:44 - When two safe skills collide
9:27 - Designing a guard agent
10:21 - A small model with per user adapters
11:49 - Catching prompt injection
12:29 - Designing memory for groups
15:29 - Context growth and token cost

## Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains — Brendan Rappazzo

- Upload date: 2026-07-29
- Video: https://www.youtube.com/watch?v=kiqubc5b5Yo
- Transcript: raw/20260729_kiqubc5b5Yo/kiqubc5b5Yo.en-orig.vtt
- Metadata: raw/20260729_kiqubc5b5Yo/kiqubc5b5Yo.info.json

When coding agents got good enough at the end of 2025, Morgan Stanley's roughly thirty person research group asked what would happen if agents ran the research, not just wrote the code. The result is AlphaLab, a multi agent system they built and open sourced. You hand it a problem in plain language and it writes the code, sets up back tests and evals, configures and submits cluster jobs, and runs the statistical tests, managing its own context as it goes. They skipped every off the shelf framework and wrote their own harness so they could watch how it reasons and bake in their own standards.

The shape is a strategist that proposes experiments and workers that run them, laid out as a board of cards people can read, edit, and approve before the loop optimizes against a weak eval. Rappazzo shows it finding real gains now used internally, from fine tuning a model to predicting credit bonds, and argues the lasting human job is designing the verifiable environment the agents compete in, like a private Kaggle, while they handle the middle.

Speaker info:
- https://x.com/brendanh0gan
- https://www.linkedin.com/in/brendan-rappazzo-hogan-763734115/
- https://www.bhogan.net

Timestamps:
0:00 - Introduction: a thirty person research group
1:30 - What changed when coding agents arrived
2:55 - Building AlphaLab 1.0, open sourced
4:34 - Encoding enterprise standards into the system
6:40 - Why they skipped off the shelf harnesses
8:21 - How the research loop runs
9:36 - Strategist and worker agents
10:40 - Guarding against a bad eval
13:23 - Finding real improvements
16:12 - Verifiable environments, like Kaggle
18:45 - The human job in the limit

## We Vetted 2000 AI Skills Before They Reached Developers — Lucas Palma, Nubank

- Upload date: 2026-07-29
- Video: https://www.youtube.com/watch?v=iKQ78wyJEXU
- Transcript: raw/20260729_iKQ78wyJEXU/iKQ78wyJEXU.en-orig.vtt
- Metadata: raw/20260729_iKQ78wyJEXU/iKQ78wyJEXU.info.json

An AI skill is a piece of code you hand a model to extend what it can do, and once engineers start sharing skills with each other, each one becomes a supply chain risk, more so inside a regulated bank. Lucas Palma's security team at Nubank built Skill Vector to sit between a skill and the internal marketplace, so nothing reaches developers unvetted. Every skill is scanned first with deterministic checks, for destructive shell commands and the like, then with an LLM for the context those checks miss, and only then does it get a decision and permissions scoped to who will use it.

Running that gate over more than 2,000 skills surfaced real problems, since a single skill can carry many, and fed them into the bank's vulnerability management program with approval gates and human confirmation. What worked was pairing deterministic scans with LLM review; what needed work was the guidance the system gave and the habit of running skills locally before vetting. The lesson he leaves is simple: treat skills like any other dependency, and only what clears the gate belongs in the marketplace.

Speaker info:
- https://www.linkedin.com/in/lucaspalma/

Timestamps:
0:00 - Introduction: making code safe at a bank
1:32 - AI skills as a supply chain risk
2:50 - What counts as an AI skill
3:57 - The extra weight of a regulated environment
6:07 - From plugins to a vetted marketplace
6:58 - What Skill Vector does
7:37 - Deterministic checks, then the LLM
10:00 - Scanning over two thousand skills
11:22 - What worked and what needed improvement
13:30 - Approval gates and human confirmation
14:23 - Next steps and policies

## Persona Engineering: A Field Guide to AI Synthetic Personas — Ishan Anand, InsightSciences.ai

- Upload date: 2026-07-29
- Video: https://www.youtube.com/watch?v=YnNF55QV0zs
- Transcript: raw/20260729_YnNF55QV0zs/YnNF55QV0zs.en-orig.vtt
- Metadata: raw/20260729_YnNF55QV0zs/YnNF55QV0zs.info.json

A team ran about a thousand people through a market research survey, then had LLM agents replay the same questions, and the agents matched the humans closely while carrying less noise than the humans did themselves. That is exactly the tell: a synthetic respondent smooths over the messiness that makes a real population real. Ishan Anand walks through where it breaks. Nudge one variable in the prompt template and purchase probability swings, because the model infers latent confounders nobody stated, a little like it is playing improv. So how you ask matters as much as which model you pick, and the persona and the study have to be specified richly, from the participant's point of view.

Accuracy can hide the damage. A model that looks right on average can still distort subgroups and flatten the shape of the distribution, collapsing the variation that mattered. The fix here is a noise floor: score humans against other humans first, so you know the best agreement any method could reach, then judge synthetic against human relative to that floor rather than against a perfect match that never existed. Treat a synthetic persona as an economic actor, not ground truth, since even the human study is not ground truth, and validate it against real outcomes before you let it drive a decision.

Speaker info:
- https://x.com/ianand
- https://www.linkedin.com/in/ishananand/
- https://ishananand.com/

Timestamps:
0:00 - Introduction: synthetic personas for market research
1:43 - Why this talk: separating signal from noise
2:46 - Forecasting people like we forecast the weather
4:04 - A thousand humans vs their agent replicas
5:22 - Purchase probability and prompt sensitivity
6:41 - Invented confounders and specifying the persona
7:45 - Question order and framing effects
8:50 - Predicting stated attitudes vs experts
10:07 - Prompting techniques and subpopulation methods
13:08 - Reconstructing and scoring the full distribution
16:09 - Calibrating personas against real forecasts
17:38 - Setting a noise floor with human vs human
18:40 - Treat personas as economic actors, and what's next

## How Kepler Built Verifiable AI for Financial Services — Vinoo Ganesh

- Upload date: 2026-07-29
- Video: https://www.youtube.com/watch?v=Tt2kX2sgQio
- Transcript: raw/20260729_Tt2kX2sgQio/Tt2kX2sgQio.en-orig.vtt
- Metadata: raw/20260729_Tt2kX2sgQio/Tt2kX2sgQio.info.json

In finance a number is worthless until you can say where it came from. Vinoo Ganesh, CEO of Kepler, starts from the fact that language models are probability machines, brilliant at next token prediction and unreliable at the deterministic work, like arithmetic, that finance actually runs on. So Kepler treats the model as one part of a system rather than the whole answer, wrapping it in a deterministic substrate that makes every figure traceable.

It rests on three tenets. Atomic provenance means every number is tied to its source and stripped out if it cannot be independently verified. Scope determinism keeps the model on the nondeterministic tasks it is good at and pulls the actual figure, say revenue from a 10K filing, deterministically behind the scenes, with reconciliation on top. The third is treating every extracted number like a pull request that gets reviewed, so entities are caught and nothing is invented. The result is a grounded system where the edge comes not from producing content but from verifying it.

Speaker info:
- https://x.com/vinooganesh
- https://www.linkedin.com/in/vinoo-ganesh/
- https://vinoo.io

Timestamps:
0:00 - Introduction: a data background in finance
1:42 - Why trust and verifiability matter now
2:57 - Models are probability machines
4:27 - Why analysts still put in the hours
8:22 - Modeling AI like an overworked VP
9:26 - Atomic provenance
12:01 - Scope determinism
13:52 - Reconciliation and pulling real numbers
15:06 - Extracting entities without misses
16:34 - Toward zero invented securities
20:31 - Where a number really comes from

## Why Off-the-Shelf AI Doesn't Understand Money — Udi Menkes, Intuit

- Upload date: 2026-07-29
- Video: https://www.youtube.com/watch?v=Owb8g3yDyzo
- Transcript: raw/20260729_Owb8g3yDyzo/Owb8g3yDyzo.en-orig.vtt
- Metadata: raw/20260729_Owb8g3yDyzo/Owb8g3yDyzo.info.json

Ask any LLM a financial question about your business. You'll get a fluent, confident, generic answer — one that doesn't truly know your business, or what happened when businesses like yours made that same decision. We build financial AI at Intuit serving 100M+ customers. Our custom LLMs outperform general-purpose models on accuracy while cutting latency in half. But that's the foundation, not the destination. I'll cover where financial intelligence goes when AI stops reporting what happened and starts helping you decide what to do next (and does it for you).

Speaker info:
- https://x.com/menkesu
- https://www.linkedin.com/in/udimenkes/

Timestamps:
0:00 - A three year old's theory of money
2:21 - Why off the shelf models fail at money
2:48 - The rental property example
4:34 - The fluent bluff
6:42 - The Princeton million dollar study
9:45 - Context is not experience
11:03 - Correlation versus causation in pricing
13:37 - Building state, action, outcome data
15:17 - Testing it head to head
16:37 - The era of outcome driven finance
17:55 - Three things to remember

## SimulationMaxxing: How we ship agents 20× faster — Aman Gupta (Nubank) + Shreya Rajpal (Snowglobe)

- Upload date: 2026-07-29
- Video: https://www.youtube.com/watch?v=KMR_RBoCa4M
- Transcript: raw/20260729_KMR_RBoCa4M/KMR_RBoCa4M.en-orig.vtt
- Metadata: raw/20260729_KMR_RBoCa4M/KMR_RBoCa4M.info.json

Nubank serves 135 million customers, so an AI agent that mishandles a support conversation fails at scale. The talk opens with the result: five agents in production, higher customer satisfaction, and roughly 20 times faster shipping. Shreya Rajpal, CEO of Snowglobe, argues the thing that unlocked that pace was evals, and specifically simulated data standing in for real conversations. Good agent evals are hard because the data is multi turn and stateful, not single turn question and answer, and hand curating it and waiting on production to confirm can take forever.

Snowglobe points at the agent and generates grounded simulations, a customer like Maria trying to order a credit card, complete with account context, tone, and intent, so you can ship, observe, simulate, and feed the results back in a tight loop. Human review found the simulated conversations comparable to real ones about 80% of the time, enough to bring up new agents, derisk changes, and protect the self service rate. With aligned metrics and cheap simulation, the team now tests open models and variant agents freely, because the eval bottleneck is gone.

Speaker info:
- https://x.com/aman2304
- https://x.com/ShreyaR
- https://www.linkedin.com/in/shreya-rajpal/
- http://shreya-rajpal.com

Timestamps:
0:00 - Opening with the results
0:39 - Nubank at 135 million customers
2:34 - Why evals matter most
2:47 - Why simulated data works
3:49 - What makes agent eval data hard
4:49 - How teams get eval data today
6:44 - Simulations in minutes, not weeks
7:35 - Pointing Snowglobe at your agent
8:48 - A grounded simulation: Maria orders a card
10:31 - Ship, observe, simulate, repeat
11:34 - How close simulations are to real
13:43 - Testing models and variants

## Your Agent Didn't Fail. Your Harness Did. — Vinoth Govindarajan, OpenAI

- Upload date: 2026-07-29
- Video: https://www.youtube.com/watch?v=BInpv7lGp1o
- Transcript: raw/20260729_BInpv7lGp1o/BInpv7lGp1o.en-orig.vtt
- Metadata: raw/20260729_BInpv7lGp1o/BInpv7lGp1o.info.json

Two runs touch the same session, the second write silently erases the first, and the agent keeps answering with total confidence from stale state. Nothing crashed and the model did not hallucinate, so this is a harness failure, the kind that lives in the system around the model rather than in the weights. Using OpenClaw as a public case study, Vinoth Govindarajan walks the usual suspects: state that was never persisted, overlapping writers with no single writer lane, a tool call that never returns because nothing set a deadline, and an approval that outlived the action it was supposed to authorize.

The through line is that a model only proposes; the harness has to commit, and a receipt has to prove it. A transcript shows what the agent said, but a receipt is the evidence that survives: it records the mutation, the authority used, and whether the message actually reached the user, since an internal success that never becomes visible proof is its own failure. You leave with a run receipt audit to run on your own agents, five questions per incident: what woke it up, what state did it inherit, what authority did it use, what executed, and what evidence survived.

Speaker info:
- https://x.com/iamvinoth
- https://www.linkedin.com/in/vinothgovindarajan/
- https://theagentstack.substack.com/

Timestamps:
0:00 - Introduction: harness failures vs model failures
1:32 - Delivery can succeed while the truth fails
2:46 - A model proposes, the harness commits, the receipt proves
4:14 - How events enter and state is rehydrated
5:48 - Idempotency, locks, and ordering
7:22 - Ownership: who persists the turn
8:28 - Single writer lanes and overlapping writes
10:09 - Time, deadlines, and cancellation
11:23 - Approval drift and bounded authority
13:05 - Internal success vs user-visible proof
14:08 - The run receipt audit: five questions

## Skills are new features: Building Skill-Centric Harness — Yogendra Miraje, FactSet

- Upload date: 2026-07-29
- Video: https://www.youtube.com/watch?v=7jjudsEhBtM
- Transcript: raw/20260729_7jjudsEhBtM/7jjudsEhBtM.en-orig.vtt
- Metadata: raw/20260729_7jjudsEhBtM/7jjudsEhBtM.info.json

Since skills were open sourced, Yogendra Miraje's team at FactSet stopped thinking about shipping features and started thinking about shipping skills. A skill is a capability you hand the agent, and its heart is a short skill.md whose name and description are really routing signals: get them distinct and the agent triggers the right one, blur them and it fires the wrong skill or none at all. He walks through a minimal skill registry, progressive disclosure so the agent only loads what it needs, and trigger words, like asking for a PDF versus an HTML report, that decide which skill runs.

The harder lessons show up at scale. Skills without evals drift, because a new model quietly stops obeying them, so he treats skills as contracts you test. Past ten skills you need search and embeddings to keep the library coherent; past a hundred you need real governance, admission, ownership, periodic audits, change management, and a human deciding whether a skill should exist at all. His close is that skills are the interface to your agentic products, and at enterprise scale governing them matters as much as writing them.

Speaker info:
- https://x.com/YogiNotTheBear
- https://www.linkedin.com/in/mirajey/
- https://yogimiraje.com

Timestamps:
0:00 - From blueprints to skills
1:46 - Building skill centric agents
2:52 - Skills in context at enterprise scale
3:46 - Skills as the new features
5:04 - Inside a skill: the skill.md
6:37 - A minimal skill registry
7:42 - Progressive disclosure
9:13 - Trigger words and routing
12:17 - Skills without evals drift
12:56 - Search and embeddings past ten skills
13:46 - Governance past a hundred skills
16:36 - Skills as the product interface

## How Forward Deployed Engineering is done at Factory — Eno Reyes

- Upload date: 2026-07-28
- Video: https://www.youtube.com/watch?v=wpOA-UXynoM
- Transcript: raw/20260728_wpOA-UXynoM/wpOA-UXynoM.en-orig.vtt
- Metadata: raw/20260728_wpOA-UXynoM/wpOA-UXynoM.info.json

Factory's forward deployed engineers sit at the tip of the product, embedded with the largest customers and piping a constant stream of real world signals back into how the agent, Droid, gets built. Eno Reyes frames the whole thing as a software factory: signals flow in from the outside, become plans, pass through validation stages, and come out as shipped outcomes, a loop most orgs run badly until they actually invest in the system around it. The non negotiable piece is a model independent harness the customer owns, so the traces and the data stay theirs and Droid can even run air gapped inside their environment.

The frontier is autonomy. Factory scores a codebase on how agent ready it is, whether it runs linters and type checkers and how much of the work an agent can finish and verify without a human, and the payoff shows up on jobs like migrating 30 to 50 million line equities systems at a bank. Push too hard, though, and you hit the trap Eno Reyes borrows from city planning: an exemplar city built too far ahead of its time becomes a theme park, not a place people live. So the forward deployed job is a balancing act, moving customers up the autonomy curve fast enough to matter but not so fast that nothing holds, which is why the role now leans as much on business judgment as on engineering.

Speaker info:
- https://x.com/EnoReyes
- https://www.linkedin.com/in/enoreyes/
- https://enoreyes.com/

Timestamps:
0:00 - Introduction: where forward deployed sits
2:08 - The role inside the customer's environment
3:49 - The tip of the spear of the product
5:03 - The software factory: signals in, outcomes out
6:57 - Why you own the agent harness
8:11 - Air gapping Droid inside the customer
10:08 - The autonomy maturity model
12:05 - Making a codebase agent ready
14:53 - Migrating 40 million line codebases
16:38 - The city of the future analogy
18:34 - Constrained autonomy and legal droid
20:04 - Redefining the forward deployed role

## Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub — Arek Borucki, Hugging Face

- Upload date: 2026-07-28
- Video: https://www.youtube.com/watch?v=lyL5QhgIOxc
- Transcript: raw/20260728_lyL5QhgIOxc/lyL5QhgIOxc.en-orig.vtt
- Metadata: raw/20260728_lyL5QhgIOxc/lyL5QhgIOxc.info.json

Type llama into a catalog of 3 million public models and the result still has to feel instant. At 20,000 models any query is fast; at Hugging Face's scale, 14 million users and a million datasets on top, search becomes the hard part. Arek Borucki shows how the Hub keeps it quick: full text search on Apache Lucene, served through MongoDB Atlas, which stores only the metadata while the model artifacts sit in S3 so compute scales on its own. Regex ranking did not hold, so relevance now runs through one unified query with the $search operator, sorted by downloads, likes, and trending.

Underneath is a seven node MongoDB cluster where only the primary takes writes, with a hidden analytics node soaking up the heavy queries so production traffic never feels them. Keep queries light, push everything else elsewhere, and once the catalog outgrows a single primary, shard the data across nodes by key. The front end scales the same way: Kubernetes goes from 10 to 500 pods and CastAI adds machines underneath, and because HPA only watches CPU and memory, they scale on event loop utilization through KEDA, which sees the request queue HPA cannot.

Speaker info:
- https://x.com/_Aras_B
- https://www.linkedin.com/in/arekborucki/
- https://arekborucki.cloud/

Timestamps:
0:00 - Introduction: scaling the Hugging Face Hub
1:44 - The numbers: 14 million users, millions of models
3:57 - Why search at scale is the hard part
5:09 - Full text search on Apache Lucene
5:46 - Request flow: autoscaling, MongoDB Atlas, and S3
7:55 - How a search for "llama" works
10:11 - Ranking and Atlas Search with the $search operator
13:00 - The seven node cluster and a hidden analytics node
16:42 - Sharding the database
18:14 - Kubernetes autoscaling: 10 to 500 pods and CastAI
20:07 - Scaling on event loop utilization with KEDA

## AI tools for Forward Deployed Engineering — Vasuman Moza, Varick Agents

- Upload date: 2026-07-28
- Video: https://www.youtube.com/watch?v=l0FLhNqBOic
- Transcript: raw/20260728_l0FLhNqBOic/l0FLhNqBOic.en-orig.vtt
- Metadata: raw/20260728_l0FLhNqBOic/l0FLhNqBOic.info.json

A customer spent five million dollars and five years migrating to SAP, and has zero appetite to rip anything out again. That constraint is the whole design at Varick Agents: instead of asking an enterprise to migrate, you drop forward deployed agents on top of the systems they already run. Vasuman Moza's version of the role maps how a department actually works today, the reconciliations between a purchase order and an invoice, the handoffs nobody documented, and then automates those processes end to end. It answers the stat everyone cites, that most AI projects never reach production, by starting from the customer's real workflow instead of a generic tool.

Making one forward deployed engineer that productive takes tooling of its own. Varick builds a spec from the raw material of an engagement, the granola notes and Slack threads, then lets the engineer shape the workflow with Claude or Codex against a single source of truth that can just live in Postgres. The harder problem is context: frontier models are surprisingly bad at traversing a messy enterprise and knowing that person A and person B are the same entity, so Varick post trains its own models to extract the right context and strip the redundancy, and only then does the agent run autonomously. Every engagement starts by finding the bottleneck and grows out from there.

Speaker info:
- https://x.com/vasuman
- https://www.linkedin.com/in/vasumanmoza/

Timestamps:
0:00 - Introduction: forward deployed agents
1:55 - The question: what can an agent actually do?
3:27 - What a forward deployed agent is
4:44 - Automating a department end to end
6:14 - Why enterprises need deployed engineers, no migrations
8:30 - Hiring the top 1 percent
10:51 - The platform and department wide ROI
11:53 - Demo: tools for forward deployed engineers
13:07 - Turning notes into a workflow spec
14:22 - Engineering workflows with a source of truth
16:53 - Post training models to extract context
18:37 - Where this leaves us

## How Forward Deployed Engineering is done at Cognition — Jia Wu

- Upload date: 2026-07-28
- Video: https://www.youtube.com/watch?v=RVxym6mmIns
- Transcript: raw/20260728_RVxym6mmIns/RVxym6mmIns.en-orig.vtt
- Metadata: raw/20260728_RVxym6mmIns/RVxym6mmIns.info.json

Most of the coding agent market quietly optimizes for token usage; Cognition's deployed engineering team measures the opposite, the outcomes a customer can actually see, and reports something like an 82% reduction on the work they targeted. Jia Wu's argument is that you measure before Devin ever lands, then again once it is fully activated inside the customer, so the value is a real delta and not a vanity number. The way that value shows up is not linear: one team using the agent is a step function, a whole enterprise using it is parabolic, because the products Cognition builds and the customer's backlog start to overlap.

That changes what a deployed engineer is. As the pure engineering part trends toward zero, the job leans on business and people skills: understand the customer's real problem space, find the highest leverage place to point the agent, and communicate it back into the roadmap, since customers are the lifeblood. Each deployment is meant to derisk and improve the next, because the challenges recur in similar shapes across companies. The value underneath it all is blunt: correctness and customer success at all costs, ship the hard thing and leave nothing on the table.

Speaker info:
- https://www.linkedin.com/in/jia-rong-wu/

Timestamps:
0:00 - Introduction: deployed engineering at Cognition
2:05 - Step function to parabolic productivity
3:35 - Where products meet the customer's problems
5:16 - Pointing agents at the highest leverage work
7:07 - How deployment challenges recur
8:34 - What a deployed engineer actually is
10:25 - Measuring outcomes, not token usage
12:56 - The 82% result, measured before and after
14:38 - Developers plus Devin, autonomously
15:53 - Core values: correctness and customer success

## Forward Deployed Engineering 101 — Kevin Bai, Anthropic, ex Palantir & Rippling Founding FDE

- Upload date: 2026-07-28
- Video: https://www.youtube.com/watch?v=KwhgfwOSToQ
- Transcript: raw/20260728_KwhgfwOSToQ/KwhgfwOSToQ.en-orig.vtt
- Metadata: raw/20260728_KwhgfwOSToQ/KwhgfwOSToQ.info.json

Look at public software companies and very few ever crack half a million dollars in average contract value, and that gap is where forward deployed engineering lives. Kevin Bai's 101 starts from the shape of the deal: when your buyer is not technical and the thing you sell is not a finished product they can pick up and configure themselves, you cannot just ship software and walk away. You loan them engineers who build a real solution on top of your platform, so the customer is neither buying a product nor a service but the outcome in between. That is the model Palantir made famous, and it is how you land Fortune 500 contracts a self serve motion never reaches.

The trap is doing it as pure custom work. Build a bespoke thing for every customer and you reinvent the wheel each time; what makes a forward deployed program work is a platform of reusable pieces the engineers assemble against, not a pile of one offs. So starting one comes down to two questions: is your product complex enough to need hand holding into a non technical org, and do you have engineers who can carry that. What has changed since the Palantir days is that building is easy now and nearly everything is agentic, which pulls this once niche motion toward the center of how software gets sold.

Speaker info:
- https://x.com/zkevinbai
- https://www.linkedin.com/in/zkevinbai
- https://zkevinbai.com/
- find Kevin on FDE Pod https://fdepod.substack.com/ https://www.youtube.com/@FDEPod

Timestamps:
0:00 - Introduction: what this 101 covers
1:47 - What Palantir does, and where FDE fits
3:14 - Selling a solution, not a product or a service
4:18 - When your buyer isn't technical
5:59 - The business case: landing large contracts
7:16 - FDE as a partnership on a reusable platform
9:48 - How to start: two questions to ask
11:34 - What has changed since Palantir
13:08 - Q&A

## How Forward Deployed Engineering is done at Ramp — Leo Mehr

- Upload date: 2026-07-28
- Video: https://www.youtube.com/watch?v=ITMXwI6QL6A
- Transcript: raw/20260728_ITMXwI6QL6A/ITMXwI6QL6A.en-orig.vtt
- Metadata: raw/20260728_ITMXwI6QL6A/ITMXwI6QL6A.info.json

It's Friday night, an enterprise sales rep needs an SAP S4 HANA integration to hit quota, and the reflexive Forward Deployed answer is yes. Leo Mehr's first principle is to pause instead: always be scoping. Saying yes to everything buries the team and often does not even serve the customer, so the job is to weigh what actually matters against the rest of the queue and decide with that context. Ramp's FDE function looks different from its Palantir origins, pointed at enterprise customers, but the discipline is the same: scope hard before you roll up your sleeves and ship.

The second half is what tokens change. Look at the FDE pipeline and ask which stages an agent can take over. Intake is a good one: requests pour in through account managers and solutions engineers, and someone has to read each and turn it into a spec. Ramp wired that step to an agent with Notion as the surface, and after a couple of iterations account reps were using it directly. The unglamorous parts are what make it work: an agent harness, evals with rubrics and human feedback, and past requests and help articles as grounding. The close is that the future of Forward Deployed needs both, humans for judgment and agents for the volume.

Speaker info:
- https://x.com/leomehr
- https://www.linkedin.com/in/leomehr
- https://leomehr.com/

Timestamps:
0:00 - Introduction: FDE principles at Ramp
2:10 - Principle one: always be scoping
3:16 - The Friday night SAP integration ask
5:04 - When scoping goes wrong
6:33 - Using agents for the FDE pipeline
7:57 - Automating request intake into specs
9:14 - Building the spec agent in Notion
11:16 - The agent harness and evals
13:27 - The future of FDE needs both

## AI Agents for Performance: Ship Faster, Pay Less — Rajat Shah, Netflix

- Upload date: 2026-07-28
- Video: https://www.youtube.com/watch?v=CgsWxRUY5Eo
- Transcript: raw/20260728_CgsWxRUY5Eo/CgsWxRUY5Eo.en-orig.vtt
- Metadata: raw/20260728_CgsWxRUY5Eo/CgsWxRUY5Eo.info.json

An inefficient quadratic-time pattern was hiding inside a tensor merge method on a live Netflix service, quietly wasting CPU on every request - nothing in a code review caught it, but it stood out clearly in a call stack. That's usually how this kind of waste gets missed - the normal process of catching it (profiling, reading a flamegraph, tracing it through the codebase, writing a fix, validating it) takes long enough that inefficiencies sit in production for months before anyone looks at them. AI-assisted coding adds to this, since it produces more code optimized for how fast it's written, not how fast it runs. Rajat Shah's team at Netflix built an agent to handle this loop: it took a call stack, traced the issue to the exact source line, proposed a fix, and validated it against a canary - a real production traffic split, with no regression allowed before it could ship. The result was based on measured outcomes, not the model's own assessment.

The talk covers what it took to get an agent to a point where it could act in production, and walks through this specific case from start to finish - found, fixed, and confirmed by canary without anyone stepping in. It also covers what's next: the same pattern turned up independently in seven other services in one session, which is why it makes sense to build a shared catalog of patterns like this so they aren't rediscovered each time, and which could eventually be used to catch these issues in coding agents before the code ships at all. We'll also share the approach itself - how it was built, what it took to trust it, and what it caught - so other teams can adopt the same loop in their own SDLC rather than starting from scratch.

Speaker info:
- https://www.linkedin.com/in/rajatsshah/
- https://github.com/shahrajat
- https://shahrajat.com/

Timestamps:
0:00 - Introduction: performance for ML serving
2:24 - The manual profiling loop today
4:46 - The experiment: can an LLM read a profile?
7:37 - From call stack to the exact method
9:07 - How the agent locates and reads the code
11:01 - First finding: an O(N) fix, canary confirmed
12:41 - The same antipattern across seven services
15:31 - Building a shared pattern catalog
17:16 - Storing and sharing findings across services
19:40 - Feeding the catalog to coding agents
20:56 - Human approval and verification
22:13 - Canary validation on real traffic
24:18 - Reactive vs proactive paths
26:54 - Catching waste before production
29:32 - Autonomy levels and what is next

## The Dirty Secret of Forward Deployed Engineering — Natalie Meurer, Sierra

- Upload date: 2026-07-28
- Video: https://www.youtube.com/watch?v=Byv311hdoHE
- Transcript: raw/20260728_Byv311hdoHE/Byv311hdoHE.en-orig.vtt
- Metadata: raw/20260728_Byv311hdoHE/Byv311hdoHE.info.json

At Palantir, forward deployed started as a literal description: you were deployed, physically, at the customer's site, and the onboarding project was keeping the platform from falling over. Natalie Meurer's dirty secret is that the title never settled after that. It stretched across DevOps, data integration, ontology work in Slate and then Foundry, and solution architecture, until forward deployed engineering meant so many different jobs that the label stopped meaning much. Every company hiring for it, whether they call it forward deployed, customer, or deployed engineering, is describing a slightly different role of a particular vintage.

Her argument is that the through line was never the code. As coding agents make writing software cheap, the durable part of the job is the rest of it: integrating the data, understanding the customer, and being accountable to an outcome. That is also why she thinks what the industry now calls agent engineering is really forward deployed engineering under a new name. The tell is in how you charge for it: seat based pricing assumes a tool, while pricing to usage or outcome assumes you are on the hook for the result, which is exactly what a forward deployed engineer has always been.

Speaker info:
- https://x.com/natalie_meurer
- https://www.linkedin.com/in/nataliemeurer

Timestamps:
0:00 - Introduction: the dirty secret of FDE
1:54 - FDE as a subdiscipline of AI engineering
3:46 - Palantir origins: leading with location
4:51 - Firefighting platform stability
6:37 - DevOps, data, and the ontology in Slate
9:02 - Why FDE is not one thing
10:46 - Every company hires a different vintage
12:28 - When code gets cheap, outcomes matter
13:55 - Pricing: seats vs usage vs outcome
15:26 - Agent engineering is FDE reborn

## How Forward Deployed Engineering is done at Decagon — Sunny Rekhi

- Upload date: 2026-07-28
- Video: https://www.youtube.com/watch?v=7wu2hsRfvV0
- Transcript: raw/20260728_7wu2hsRfvV0/7wu2hsRfvV0.en-orig.vtt
- Metadata: raw/20260728_7wu2hsRfvV0/7wu2hsRfvV0.info.json

Decagon builds the customer support agent that answers when you email a brand, and making that agent good for a specific enterprise is the forward deployed job. It splits in two: one side configures the agent brain, the instructions and the handoff rules for when a human should take over; the other works like product engineering, figuring out what a new enterprise needs and anticipating the requests that have not been made yet. Sunny Rekhi's point is that the line between forward deployed and product is thin, because a customer ask is often just a product feature waiting to be built.

What changes at scale, from 50 people to 500, is that this splits into specialized lanes and a few disciplines start to matter. One is restraint: some problems belong to the customer, and getting the boundary in writing keeps everyone honest. The bigger one is that custom work does not stay custom. Every integration a forward deployed engineer builds gets upstreamed into the platform, so custom becomes self serve and the agent compounds, and the next customer inherits it for free. You still have to prove value fast, because the relationship is multi year but the trust is won in the first weeks.

Speaker info:
- https://www.linkedin.com/in/sunny-rekhi/

Timestamps:
0:00 - Introduction: forward deployed at Decagon
1:06 - What Decagon's support agent does
2:24 - Offloading support and proactive outreach
3:40 - Two kinds of forward deployed work
6:12 - Scaling from 50 to 500 people
8:20 - Restraint, and getting it in writing
9:59 - Ramping a new enterprise deal
11:18 - Solving a problem so it scales
13:00 - Proving value fast
14:18 - Custom becomes self serve

## How Forward Deployed Engineering is done at Kepler — Vinoo Ganesh

- Upload date: 2026-07-28
- Video: https://www.youtube.com/watch?v=1OMHGsUZiqA
- Transcript: raw/20260728_1OMHGsUZiqA/1OMHGsUZiqA.en-orig.vtt
- Metadata: raw/20260728_1OMHGsUZiqA/1OMHGsUZiqA.info.json

A shipping and dispatch customer wanted alerts, a massive BI tool, and a dev environment. What they actually needed Monday morning was one Slack message, so that is what got shipped first, and the real thing followed. Vinoo Ganesh spent seven years doing this at Palantir, where he later ran the rotation program that turned software engineers into forward deployed engineers, and his throughline is that the work was never a sales motion, it was product strategy in disguise. The engineer sits in the customer's environment, solves the concrete problem in under a day, and then generalizes it into something the whole product can use.

The compounding lessons are less obvious. Watch what people actually do: any task a user repeats is a hint at a missing feature, and someone pulling out their phone in the middle of a workflow is a bug report you will never find in documentation. The deepest one is language. When a customer says clients, finance says billing, and support says accounts, the ambiguity costs real money, so the forward deployed engineer defines the terms, the ontology, and becomes the linguistic layer the rest of the system is built on. A throwaway Groovy script that quietly became a product a year later is the whole pattern: forward deployed engineers drive product strategy without anyone calling it that.

Speaker info:
- https://x.com/vinooganesh
- https://www.linkedin.com/in/vinoo-ganesh/
- https://vinoo.io

Timestamps:
0:00 - Introduction: FDE's origins at Palantir
2:05 - Not a role, a product strategy
4:51 - Real stories: scoping down to a Slack alert
7:11 - Solve in a day, then ship the real thing
8:33 - The data quality engineer story
10:03 - Watch what users actually do
12:33 - Own the language: clients vs billing
14:54 - The ontology and the linguistic layer
16:51 - The Groovy script that became a product
18:09 - The most important skill: what to discard
19:38 - Ship everything like it runs forever
21:11 - FDE as an extension of product

## State of Data — Sean Cai, Independent / State of Data

- Upload date: 2026-07-26
- Video: https://www.youtube.com/watch?v=ZyIoTOAbRfs
- Transcript: raw/20260726_ZyIoTOAbRfs/ZyIoTOAbRfs.en-orig.vtt
- Metadata: raw/20260726_ZyIoTOAbRfs/ZyIoTOAbRfs.info.json

GPT 5.5 and Opus 4.8 landed within three points on the same finance benchmark while failing in opposite directions. GPT got the arithmetic right. Opus got the methodology right. One leaderboard number flattened both failures into a single noisy sample, exactly what happens when benchmarks reward one scaffold and vendors sell the data used to climb the tests they designed.

The scarce asset is no longer another isolated answer. It is process data: the reasoning trace, sequence of decisions, state changes, failures, recoveries, and verified outcomes that turn general competence into real expertise. Static datasets depreciate as models improve, so the durable moat is a live pipeline into real work plus the infrastructure to retrain when the base model changes.

Speaker info:
- https://x.com/SeanZCai
- https://www.linkedin.com/in/sean-z-cai
- https://www.seancai.com/philosophy/state_of_data_jan_2026

Timestamps:
0:00 - The data market nobody sees
1:15 - Data as industrial fuel
2:31 - Type one and type two data
3:23 - Compute, data, and talent
4:24 - State data versus process data
5:54 - The three axes of verifiability
8:14 - When benchmarks become snake oil
10:08 - Three finance benchmark tests
12:04 - Predicting the next AI domain
13:21 - The robotics counterexample
14:22 - Where the economic value lives
16:02 - Why data companies move enterprise
17:09 - The durable moat

## DeepSWE: A Contamination-Resistant Coding Benchmark — James Shi, Datacurve

- Upload date: 2026-07-26
- Video: https://www.youtube.com/watch?v=Yk87oUPVaxU
- Transcript: raw/20260726_Yk87oUPVaxU/Yk87oUPVaxU.en-orig.vtt
- Metadata: raw/20260726_Yk87oUPVaxU/Yk87oUPVaxU.info.json

DeepSWE is 113 software engineering tasks written from scratch, not scraped from pull requests, so a model cannot have seen them in training. Each one is a long horizon problem drawn from a real open source repository, authored by engineers who actually maintain that code, with isolated environments and program based verifiers that check observable behavior rather than trusting the model's own account. James Shi's point is that once you remove the contamination the leaderboard stops clustering: strong models pull far ahead and others, Gemini 3.1 Pro among them, fall toward the bottom.

The more revealing signal is in how models fail. Some quietly expand a task beyond what was asked, a failure mode DeepSWE scores in its own right, and Claude models did this a good fraction of the time while GPT models did it less often. Stronger models also tend not to verify their own work, and there is a real gap between the ones that test what they wrote and the ones that assume it is correct. Since reward hacking is a constant temptation, the verifiers are built to be gamed as little as possible, keeping the score anchored to the objective rather than to a convincing looking rollout.

Speaker info:
- https://x.com/shiqyy
- https://www.linkedin.com/in/jamesshi117/
- https://deepswe.datacurve.ai

Timestamps:
0:00 - Introduction: the DeepSWE benchmark
1:03 - 113 original, contamination-resistant tasks
2:08 - What makes a good benchmark
3:51 - The leaderboard and model spread
5:18 - Failure mode: over-scoping the task
7:16 - Do models verify their own work?
8:45 - Tasks authored by core contributors
10:15 - Writing realistic, high level prompts
11:45 - Program based verifiers and observable behavior
13:43 - Limitations and future work
15:25 - Reward hacking and keeping it cheating proof

## The Messy Reality of Scale: Synthetic Data and Pre-Training — Marah Abdin & Robert McHardy, poolside

- Upload date: 2026-07-26
- Video: https://www.youtube.com/watch?v=KhYifX22yhE
- Transcript: raw/20260726_KhYifX22yhE/KhYifX22yhE.en-orig.vtt
- Metadata: raw/20260726_KhYifX22yhE/KhYifX22yhE.info.json

Good code data runs out, so poolside manufactures more of it, and the hard part is making it teach. Their synthetic pipeline pairs templates with supplementary context and spreads generations across an axis of phrasing, with difficulty tuned so a task is neither trivial nor so hard the model learns nothing from it. Multistage pipelines port existing data into new shapes, swapping character styles or plots and turning single prompts into multi turn chats, while an orchestrator polices every generation and drops the ones that miss.

On the training side the team trusts nothing: run two replicas of the same model on the same data and they must return the same number, or the run gets killed. That is how the messy failures surface. Broken GPUs show up as a spiky loss curve, a numerical precision bug in tensor parallel accumulation quietly flattened another until they patched it, and silently corrupted gradients from a race condition were a blind spot nothing caught. The payoff is a 118 billion parameter model built for agentic coding whose early results already edge out GLM 4.5 Air, on a recipe that held as it scaled.

Speaker info:
Marah Abdin, poolside:
- https://x.com/marah_i_abdin
- https://www.linkedin.com/in/marah-abdin
- https://marahabdin.com

Robert McHardy, poolside:
- https://x.com/robert_mchardy
- https://www.linkedin.com/in/robert-mchardy
- https://www.robertmchardy.de

Timestamps:
0:00 - Introduction: synthetic data and pre-training at poolside
1:52 - Why synthetic data
3:11 - Limitations and the training budget
4:44 - Inside the synthetic data pipeline
6:37 - Multistage pipelines and porting data
7:43 - Multi turn chats and policing generations
9:03 - Pre-training: trust nothing, crash on mismatch
10:41 - Failures at scale: broken GPUs
11:56 - Numerical precision and corrupted gradients
13:15 - A 118B model for agentic coding
15:07 - Early results vs GLM 4.5 Air

## Loop Engineering from First Principles — Kyle Mistele, HumanLayer

- Upload date: 2026-07-25
- Video: https://www.youtube.com/watch?v=xIt_mTQp6mY
- Transcript: raw/20260725_xIt_mTQp6mY/xIt_mTQp6mY.en-orig.vtt
- Metadata: raw/20260725_xIt_mTQp6mY/xIt_mTQp6mY.info.json

A coding agent will happily hand you a 40,000 line pull request that nobody can review and that quietly does the wrong thing. Kyle Mistele's argument is that the fix is not a better prompt but a better loop, borrowed from control theory: a thermostat senses the error between where a system is and where you want it, emits a control signal, and measures again, over and over. Infrastructure as code already approximates this. The point is to design agent loops the same way, so each iteration makes a small, readable change you can actually verify, instead of one giant diff you have to trust.

The working example is migrating a codebase one procedure at a time. A sensor, often just Grep or a structural search, finds the smallest unmigrated piece, a controller picks what to work on next, and an actuator agent makes the change against golden patterns defined by hand, gated by deterministic CI like a single loop iteration in CircleCI. The loop tracks its own PRs in version control, refuses to stack a new change while an earlier one is still open, and keeps improving the code incrementally, even while the team is away.

Speaker info:
- https://x.com/0xBlacklight
- https://www.linkedin.com/in/kyle-mistele
- https://blacklight.sh

Timestamps:
0:00 - Introduction: the 40,000 line PR problem
1:55 - Why more code is not the goal
3:37 - Is the generated code any good?
4:43 - Control loops from control theory
5:49 - Infrastructure as code and Ralph loops
7:06 - Applying control loops to coding
8:35 - Migrating a codebase one procedure at a time
10:40 - Tracking the loop in version control
12:35 - The actuator agent and golden patterns
13:51 - Wiring the loop into CI
15:44 - Avoiding stacked PRs and scaling the controller

## Why Large? Tiny LMs & Agents on Edge/Robotics — Cormac Brick, Google

- Upload date: 2026-07-25
- Video: https://www.youtube.com/watch?v=hacEQHHhu2Q
- Transcript: raw/20260725_hacEQHHhu2Q/hacEQHHhu2Q.en-orig.vtt
- Metadata: raw/20260725_hacEQHHhu2Q/hacEQHHhu2Q.info.json

The constraint on edge AI is not compute, it is RAM, and it is getting worse: phone makers are shipping less of it this year, and a 6GB Raspberry Pi costs 2.5 times what it did at launch. So Cormac Brick's team at Google AI Edge spends its effort making models small enough to fit. A 2 billion parameter Gemma, quantized to 2.9 bits per weight, runs on a Raspberry Pi at about 8 tokens per second and on a Qualcomm NPU fast enough for a few frames of vision a second.

Below that sit tiny models, from 500 million parameters down to 50, that reach the older laptops and cheap devices where even a small model will not fit. They usually need fine tuning rather than prompting, but the payoff is real: a fine tuned Gemma turns free text into the right function call across ten actions at over 86% reliability, and putting a speech model in front gives you voice to function calling. One shipped example is an offline voice dictation app with no subscription, built on two sub billion Gemma models that also strip your ums and ahs.

Speaker info:
- https://x.com/cormacb
- https://www.linkedin.com/in/cbrick/
- https://github.com/google-ai-edge/gallery

Timestamps:
0:00 - Why intelligence at scale needs tiny models
1:17 - The Google AI Edge team and its open source stack
2:35 - Why run on the edge at all
3:25 - The real constraint: DRAM cost
4:40 - Small models: 1 to 4 billion parameters
6:08 - Shrinking Gemma to 2.9 bits per weight
7:36 - Decode speeds across Raspberry Pi, Jetson, and NPUs
9:30 - Try it yourself: AI Edge Gallery and a hobby robot
12:07 - When small is still too big: tiny models
13:24 - Off the shelf tiny models: ASR, vision, embeddings
14:28 - Fine tuning for voice to function calling
17:50 - In production: offline voice dictation
19:30 - Takeaways and Q&A

## Evaling Video Slop — Maor Bril, Character.ai

- Upload date: 2026-07-25
- Video: https://www.youtube.com/watch?v=b_PmGocP4rc
- Transcript: raw/20260725_b_PmGocP4rc/b_PmGocP4rc.en-orig.vtt
- Metadata: raw/20260725_b_PmGocP4rc/b_PmGocP4rc.info.json

A generated clip where the character stands frozen for four seconds can still score well, because the judge rewarded the gloss and the vibe instead of what actually happened. That failure is the whole problem with evaling video: CLIP score misses temporal incoherence, a team watching clips on Friday does not scale, and any AI judge you wire up drifts from human preference unless you measure the drift. Video breaks the text playbook because it has to hold temporal consistency, shot continuity, and a coherent story across frames, not just look good in a single still.

The fix that stuck was to stop scoring and start comparing. Absolute scores collapsed to one dimension, but pairwise preference, is B a better story than A, held up, so Maor Bril's team trained a Qwen3-VL judge with Bradley-Terry loss on pairs of real and deliberately broken footage to catch slop before it ships. Drift is cheapest to catch early, especially on longer form video, so the judge runs as a regression gate in CI: every AgentX release at Character.ai clears an eval wall, calibrated against human scores, before users ever see it.

Speaker info:
- https://x.com/maorbril
- https://www.linkedin.com/in/maorbril
- https://github.com/character-ai/judgejudy

Timestamps:
0:00 - Introduction: evaluating AI generated video
1:19 - Why video generation drifts between frames
3:14 - Story and sound: what a clip has to get right
4:43 - LLM as a judge, and catching drift early
7:01 - Story and sound failure modes
8:28 - Small model vs bigger model as judge
9:20 - Don't score, compare: pairwise preference
10:47 - When the judge scores vibe over substance
11:53 - Pairing real footage to train a quality detector
13:27 - Self verification in the generation loop
15:05 - Q&A

## Evals-Driven Development for a Mental Health AI Coach — Akele Reed & Dave Revere, SonderMind

- Upload date: 2026-07-25
- Video: https://www.youtube.com/watch?v=O72p-rBb2bA
- Transcript: raw/20260725_O72p-rBb2bA/O72p-rBb2bA.en-orig.vtt
- Metadata: raw/20260725_O72p-rBb2bA/O72p-rBb2bA.info.json

In the world of AI mental health, vibes can be dangerous, with real consequences. Building SonderMind's Mental Health AI Coach required a new playbook for eval-driven development that balances effectiveness and safety.

The team explains the clinical feedback loop that turns human therapist insights into machine-readable evaluations across thousands of conversations; the Ethics Engine of modular guardrails that can evolve with clinical guidelines; the move from single-prompt agents to a closed-loop Supervisor/Executor/Evaluator architecture; and the human oversight used to improve safety and quality.

Speakers:

Akele Reed — Principal AI Engineer, SonderMind
Akele leads the team behind SonderMind's conversational AI mental health feature and helped architect its guardrails and evaluations framework.
LinkedIn: https://www.linkedin.com/in/akele-reed

Dave Revere — Staff AI Engineer, SonderMind
Dave builds evaluation, guardrail, clinical-feedback, and regression-testing infrastructure for high-stakes mental health AI.
X/Twitter: https://x.com/daverevere
LinkedIn: https://www.linkedin.com/in/daverevere

Doug Keller — Senior Staff AI Engineer, SonderMind
Doug is the lead architect of SonderMind's agent platform and a core builder of its mental health coach.
LinkedIn: https://www.linkedin.com/in/doug-keller/

## From Agent Traces to Agent Simulations — Rustem Feyzkhanov, Snorkel AI

- Upload date: 2026-07-25
- Video: https://www.youtube.com/watch?v=Ib5t2RLtxvM
- Transcript: raw/20260725_Ib5t2RLtxvM/Ib5t2RLtxvM.en-orig.vtt
- Metadata: raw/20260725_Ib5t2RLtxvM/Ib5t2RLtxvM.info.json

Take a real production trace, rebuild the database state, tools, and files the agent touched, and you have a task any model can replay under identical conditions. That reconstruction is the move at the center of this talk. Public benchmarks like WebArena hand you a single success rate on someone else's tasks, but what you actually care about is cost per solved task, latency, and whether the agent followed your policies. So you build a private benchmark from your own traces, wire in the same skills, tools, and evaluators the agent sees in production, and compare models apples to apples on the environment that matters to you.

The environments are multistep and long horizon, so a verifier reads the final state while an LLM judge checks whether the agent followed policy, and a run can stop early once it clearly goes off track. The hard parts are the edge cases: agents that reward hack the simulation, missing fixtures, tasks that turn out to be unsolvable. Rustem Feyzkhanov's case is that this belongs in a CI pipeline for agents, the same way tests gate code, connecting observability traces to experiments to a benchmark that keeps up as the agent changes. Every company ends up needing its own, as part of the agent ops loop.

Speaker info:
- https://x.com/ryfeus
- https://www.linkedin.com/in/ryfeus
- https://ryfeus.io

Slides:
- https://www.dropbox.com/scl/fi/lyp1my0oc9whpusps29t7/Agent-Simulations-Talk.pdf?rlkey=rhrrpgun5c35kwculce0wmt2x&e=1&dl=0

Timestamps:
0:00 - Introduction: why Snorkel builds agent benchmarks
1:17 - Benchmark construction and testing agents in production
3:08 - The limits of public benchmarks
4:01 - Why you need a private benchmark
4:52 - Environments, tools, and evaluators
6:34 - Anatomy of a simulation task
7:37 - Task formats: instruction files and Oracle data
9:20 - Multistep, long horizon simulations
10:54 - Verifiers, LLM as a judge, and reward hacking
13:02 - A CI pipeline for agents
15:19 - Connecting traces, experiments, and benchmarks
16:51 - Q&A

## How Evals and Prompts Shape Agent Behavior — Preetika Bhateja & Daniel Bump, YouTube Ads

- Upload date: 2026-07-24
- Video: https://www.youtube.com/watch?v=xyL2Ltkh-SA
- Transcript: raw/20260724_xyL2Ltkh-SA/xyL2Ltkh-SA.en-orig.vtt
- Metadata: raw/20260724_xyL2Ltkh-SA/xyL2Ltkh-SA.info.json

Getting an AI agent to behave the way you want isn't just about writing better prompts. In real systems, behavior emerges from a loop: prompts, evals, iteration, and feedback. Small changes in any part of that loop can completely change outcomes.

The Google team shares lessons from building a seed-asset agent that turns messy advertising creatives — low-quality images, cluttered visuals, and heavy text overlays — into clean, reusable assets for downstream generative AI tools. They explain why prompting alone did not produce stable behavior, how evals became feedback signals rather than scorecards, how agent trace logs exposed why failures happened, and how they iterated without breaking problems they had already fixed.

Speakers:

Chris Souza — Google
Chris works on the Google team behind this seed-asset agent and its evaluation workflow.

Preetika Bhateja — Product Manager, Google/YouTube
Preetika works on ads, evaluations, agents, and LLM-as-judge systems.

Daniel Bump — Engineer, Google
Daniel focuses on image and video generation and computer vision.
X/Twitter: https://x.com/DanielJBump
LinkedIn: https://www.linkedin.com/in/danielbump

## The Future of Evals: From LLM as a Judge to Agent as a Judge — Aparna Dhinakaran, Arize AI

- Upload date: 2026-07-24
- Video: https://www.youtube.com/watch?v=q2JrUKBMf0w
- Transcript: raw/20260724_q2JrUKBMf0w/q2JrUKBMf0w.en-orig.vtt
- Metadata: raw/20260724_q2JrUKBMf0w/q2JrUKBMf0w.info.json

Across a dozen eval jobs Arize watches the top teams run, one pattern holds: the eval has to change as fast as the agent it grades. In 2023 an agent was barely more than a prompt; since then reasoning, tool calls, and long multi step loops piled on, and every jump in capability quietly broke the eval that came before. So the evals evolved with them. Deterministic checks catch what you can define up front, LLM as a judge adds the analysis a fixed rule cannot, and the newest step, agent as a judge, hunts for failure modes you would never think to write a check for and can open a pull request to fix what it finds. Aparna Dhinakaran's argument is that this arc, from static checks to an agent grading another agent, is where evals go next.

Speaker info:
- https://x.com/aparnadhinak
- https://www.linkedin.com/in/aparnadhinakaran/

Timestamps:
0:00 - Opening: the future of the Evals track
2:06 - Why evals got harder as agents evolved
3:45 - From deterministic checks to LLM as a judge
4:36 - Agent as a judge, and where evals go next

## Everything Is a Rollout — Alex Shaw + Ryan Marten, Terminal-Bench, Harbor, Laude Institute

- Upload date: 2026-07-24
- Video: https://www.youtube.com/watch?v=jRCpXUjz4CI
- Transcript: raw/20260724_jRCpXUjz4CI/jRCpXUjz4CI.en-orig.vtt
- Metadata: raw/20260724_jRCpXUjz4CI/jRCpXUjz4CI.info.json

Alex Shaw and Ryan Marten present a rollout-centered view of evaluating and improving AI agents. Drawing on their work on Harbor, Terminal-Bench, and OpenThoughts-Agent, they connect sandboxed environments, agent evaluations, and optimization workflows into a practical framework for generating and learning from rollouts.

Speakers:

Alex Shaw — Member of Technical Staff, Laude Institute
Alex is the creator of Harbor, a framework for evaluating and optimizing agents and language models in sandboxed environments.
https://www.linkedin.com/in/alexgshaw/

Ryan Marten — Member of Technical Staff, Laude Institute
Ryan builds Harbor and works on research-to-production efforts including Terminal-Bench and OpenThoughts-Agent.
https://www.linkedin.com/in/ryan-marten/

Harbor: https://www.harborframework.com/
GitHub: https://github.com/harbor-framework/harbor

## Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex

- Upload date: 2026-07-24
- Video: https://www.youtube.com/watch?v=il1c1a2FufU
- Transcript: raw/20260724_il1c1a2FufU/il1c1a2FufU.en-orig.vtt
- Metadata: raw/20260724_il1c1a2FufU/il1c1a2FufU.info.json

Jason Liu walks through how Codex works as a general tool for controlling your computer: setting up a memory vault and assistant threads, prompting it to collaborate with other threads, exploring computer use, thinking about long-running work streams, and preparing to work in loops.

Speaker:

Jason Liu — Developer Experience, OpenAI
Jason helps developers get more from Codex, the Agents SDK, and the OpenAI API. Before OpenAI, he created Instructor and taught developers how to build reliable AI applications.

X/Twitter: https://x.com/jxnlco
LinkedIn: https://www.linkedin.com/in/jxnlco
Website: https://jxnl.co/

## Vending-Bench: Long-Horizon Agent Evals — Lukas Petersson, Andon Labs

- Upload date: 2026-07-24
- Video: https://www.youtube.com/watch?v=cO8qC6HBuBg
- Transcript: raw/20260724_cO8qC6HBuBg/cO8qC6HBuBg.en-orig.vtt
- Metadata: raw/20260724_cO8qC6HBuBg/cO8qC6HBuBg.info.json

An hour before this talk, Andon Labs published a blog post laying off Gemini. Gemini had been running their café in Stockholm, a real café that no human operates, and it had lost $6,000, so they handed it to GPT. That café once hired its own staff by posting a job on LinkedIn. This is the real world half of Lukas Petersson's work; the other half is Vending Bench, where models run a simulated vending business for a year and keep producing behavior nobody prompted: price cartels, lying to suppliers, and power seeking.

The problem with the simulation is that models act differently once they suspect they are being tested; one rationalized stiffing a customer's refund because the customer was simulated anyway. So Andon moved businesses into the real world, retail space on Union Street, the café, AI radio stations where Claude turns out to be the best DJ. To win back reproducibility they fork a live environment into a simulation mid run, which briefly fools the model completely. Replaying the moment Gemini agreed to play a Nazi march, Grok played it over 90% of the time while Opus and GPT refused every time.

Speaker info:
- https://x.com/lukaspet
- https://www.linkedin.com/in/lukas-petersson-181a83172/
- https://lukaspet.substack.com/

Timestamps:
0:00 - Putting AIs in the real world
1:05 - Building Vending Bench
2:07 - The leaderboard: which models run a business best
3:25 - Emergent misbehavior: collusion, lying, power seeking
5:42 - The simulation awareness problem
6:23 - Moving businesses into the real world
7:11 - Laying off Gemini, hiring GPT
9:06 - AI radio and the best DJ
10:39 - Humans as adversarial forces
12:43 - The Nazi song and the reproducibility problem
13:58 - Forking real environments into simulation
15:17 - Live demo: is the store in a simulation?

## Training Frontier Models to Out-Think Hackers — Uri Rolls, Arithmetic & Thom Wolf, Hugging Face

- Upload date: 2026-07-24
- Video: https://www.youtube.com/watch?v=O-CBZ3JtRvo
- Transcript: raw/20260724_O-CBZ3JtRvo/O-CBZ3JtRvo.en-orig.vtt
- Metadata: raw/20260724_O-CBZ3JtRvo/O-CBZ3JtRvo.info.json

NOTE: see further context from Thom: https://x.com/Thom_Wolf/status/2079954096950264238?s=20

Give a frontier model a real chain of Keycloak, Vault, and a broker, start it as a low privileged user, and ask it to reach production code. There is a genuine zero day in there: one check validates the admin by name while another checks by ID, so a user can simply rename themselves to the admin and inherit the privilege. GPT 5.5 and Opus probe everything, even reach the check, and never make that logical leap. That gap is the point of Uri Rolls and Hugging Face cofounder Thom Wolf's talk: today's models can do the reconnaissance but not the reasoning jump a skilled hacker makes.

Their argument is optimistic, which is rare in AI and cyber right now. Just as high quality data transformed coding, Arithmetic builds cyber training data by having human vulnerability researchers find their own zero days in open source software, then wrapping them in blackbox environments where every step of discovery and exploitation is deterministically graded. The benchmark, focused on access control, the top vulnerability class, is brutal: exactly one solve at K1. The bet is that if open source models get fast and good enough at these logic leaps, defenders finally get a lasting edge over attackers, instead of leaving it to two labs.

Speaker info:
Uri Rolls, Arithmetic:
- https://x.com/uri_rolls
- https://www.linkedin.com/in/urirolls/
Thom Wolf, Hugging Face:
- https://x.com/Thom_Wolf
- https://linkedin.com/in/thom-wolf
- https://thomwolf.io

Timestamps:
0:00 - Why cyber is a wide new field for AI
1:34 - The ARC-AGI-3 parallel: models can't model the world
2:24 - Open source models as part of the defense
3:45 - The shifting economics of cyber
5:52 - The optimistic thesis: models are the solution
7:06 - The first benchmark: access control
8:20 - Data quality: finding your own zero days
10:01 - A real solve: the Keycloak name versus ID exploit
11:57 - Live demo: one solve at K1
14:22 - Only models can replace the old stack
15:00 - The speed challenge and specialized defenders

## From Signal to PR: Anatomy of a Self-Improving Agent — Jason Lopatecki, Arize

- Upload date: 2026-07-24
- Video: https://www.youtube.com/watch?v=9HbzAWnKbo4
- Transcript: raw/20260724_9HbzAWnKbo4/9HbzAWnKbo4.en-orig.vtt
- Metadata: raw/20260724_9HbzAWnKbo4/9HbzAWnKbo4.info.json

Instead of getting paged at midnight and starting to dig, you wake up to an issue that has already been investigated: the traces pulled, the root cause found, and a pull request with the fix waiting for review. That is what Arize built with Signal, and Jason Lopatecki walks through the anatomy of it. The unlock is boring and specific: traces on a filesystem. A skill pulls the relevant production traces and logs down as files into the repo, right next to the code, sometimes ten megabytes of them, because coding harnesses like Claude Code are magical with files and hopeless with a dashboard.

From there the agent has the exact code path the software took, not a guess among a million branches, and can produce a real fix. You pick the harness, the sandbox, and the skills, and Arize can run it inside your VPC, because companies like Uber and Booking will not point production systems at an external model. The deeper shift is that observability stops being a dashboard you click and becomes the smoke a system throws off for agents to read, which is why you now log and trace ten times more, not less. He is honest about the limits: a one line fix is the easy case, bigger fixes still need a human to drive, and the job moves from responder to reviewer.

Speaker info:
- https://www.linkedin.com/in/jason-lopatecki-9509941/
- https://arize.com/author/jason-lopatecki/

Timestamps:
0:00 - Arize, its agent Alyx, and why v1 sucked
1:36 - Observability is changing: from dashboards to telemetry for agents
2:55 - The goal: systems that fix themselves
4:14 - Inverting the loop: the agent investigates first
6:08 - Traces on a filesystem, the key unlock
7:23 - From your laptop to sandboxes
8:13 - A real fix: the Alyx stream canceled bug
9:39 - Why you should trace ten times more
11:10 - Product demo: Signal, AX, and Phoenix
13:09 - Sandboxes, VPC, and why customers won't call out
16:20 - Q&A: why not just point Claude Code at your data?
18:04 - Q&A: where do the evals come in?

## Building Closed-Loop Evals for a Multimodal Agent at Scale — Soumya Gupta & Jai Chopra, Uber

- Upload date: 2026-07-24
- Video: https://www.youtube.com/watch?v=31GUkCBD-Uc
- Transcript: raw/20260724_31GUkCBD-Uc/31GUkCBD-Uc.en-orig.vtt
- Metadata: raw/20260724_31GUkCBD-Uc/31GUkCBD-Uc.info.json

This talk covers how Uber designed evals for its food enhancement agent, which edits food photography to better present dishes for smaller, independent Uber Eats merchants, along with the pitfalls and lessons learned along the way.

The problem is uniquely hard: the system must stay faithful to the original dish, preserve each merchant's brand and packaging, and avoid homogenizing the marketplace, all without an existing playbook for multimodal evals in a narrow domain. Soumya Gupta and Jai Chopra explain how they navigated reward hacking, built a closed feedback loop combining offline and online signals, and balanced creativity against rigid safety guardrails at scale.

ML and applied AI practitioners working on multimodal systems, agentic pipelines, or eval design will take away practical strategies for narrow-domain multimodal evaluations, countering reward hacking, and production feedback loops.

Speakers:

Soumya Gupta — ML Engineer, Uber
Soumya is a Tech Lead and Applied AI Engineer who architects and scales production-grade generative AI and computer vision systems at Uber.
X/Twitter: https://x.com/guptasoumya12
LinkedIn: https://www.linkedin.com/in/guptasoumya12/

Jai Chopra — Product Manager, Uber
Jai is a Product Lead on Uber's Applied AI team and previously worked at Cruise and several startups.
X/Twitter: https://x.com/jai_chopra
LinkedIn: https://linkedin.com/in/jaichopra

## Why We Killed Our Multi-Agent Pipeline — Subbiah Sethuraman and Abhilash Asokan, ZS Associates

- Upload date: 2026-07-23
- Video: https://www.youtube.com/watch?v=u6jJcIFDLE4
- Transcript: raw/20260723_u6jJcIFDLE4/u6jJcIFDLE4.en-orig.vtt
- Metadata: raw/20260723_u6jJcIFDLE4/u6jJcIFDLE4.info.json

Their first pharma analytics system mimicked a human analyst: one agent to detect a signal, one to localize it, one to find the cause, one to synthesize, all wired to an orchestrator. It produced answers like this: prescriptions dropped 18% in a territory because a payer moved the drug to a worse tier, so send more sales reps. The cause was right and the action was wrong, because no single agent owned the whole picture. So Subbiah Sethuraman's team at ZS killed the multi agent pipeline.

Instead of redesigning the topology, they opened an empty directory, gave Claude Code bash and the database, and watched what it actually did. The rebuild came out smaller, not bigger. Signal detection moved into a deterministic pipeline that runs before the agent wakes up, so the agent investigates rather than guesses. A single agent owns the reasoning and spawns sub agents only when a focused lookup needs one. A pharma knowledge graph acts as a control plane, not a lookup table: every edge is a hypothesis the agent tests against the data, which bounds the search. The result does in 20 minutes what an analyst did in a month.

Speaker info:
- https://www.linkedin.com/in/subbiahsethuraman/
- https://subbiah-sethuraman.medium.com/

Timestamps:
0:00 - Pharma commercial analytics and the analyst's four steps
2:33 - V1: an agent for every step
3:26 - Why the output was incoherent
4:32 - Why it failed: signals, handoffs, and missing domain
5:57 - The rebuild: watching Claude Code in an empty directory
7:01 - Deterministic signal detection before the agent
8:05 - Consolidating to a single agent
9:22 - The knowledge graph as a control plane
11:04 - Every edge a hypothesis, and the result

## Learned Execution Graphs for Anomaly Detection & Drift in APIs — Ritvik Pandya, JP Morgan Chase

- Upload date: 2026-07-23
- Video: https://www.youtube.com/watch?v=u1yaOeEX4e8
- Transcript: raw/20260723_u1yaOeEX4e8/u1yaOeEX4e8.en-orig.vtt
- Metadata: raw/20260723_u1yaOeEX4e8/u1yaOeEX4e8.info.json

Traditional monitoring reported the system healthy: latency down, errors at zero. A mandatory processing step had been silently skipped, and nothing caught it except the graph. Ritvik Pandya's team at JP Morgan models each API request as a short lived execution graph, a DAG of the middleware steps it passes through, learned from telemetry at over 1,600 requests per second. Compare what actually ran against that learned graph and a skipped, reordered, or injected step stops hiding behind healthy averages.

The same graph localizes performance problems to the exact node instead of the whole endpoint. In production it flagged a 41x deviation at a single node that service level monitoring never saw, cutting root cause from hours to under 30 seconds. The talk separates a one off anomaly from real drift, a slow shift that needs a new baseline, and sorts drift into structural, volume, and behavioral, using per node baselines and KL divergence rather than one threshold for every request. The payoff is a cheap tier one check that only escalates when the graph says something actually changed.

Speaker info:
- https://www.linkedin.com/in/ritvik-pandya/

Timestamps:
0:00 - Execution graphs for anomaly and drift detection
1:07 - What a short lived execution graph is
3:28 - Tiered checks and per client baselines
5:23 - The method: baseline, deviation, localize, act
6:16 - Localizing a slow node, and how the system is trained
7:33 - Anomaly versus drift
8:55 - The three kinds of drift: structural, volume, covariate
12:46 - The pipeline: from telemetry to gradual rollout
13:54 - Hot path versus recon, and worked examples
15:21 - Tuning it: delayed events, sampling, cold starts
17:09 - Results and lessons

## Video Has No Memory. Here's How We Built One. — James Le, TwelveLabs

- Upload date: 2026-07-23
- Video: https://www.youtube.com/watch?v=mOf-PP4mVjA
- Transcript: raw/20260723_mOf-PP4mVjA/mOf-PP4mVjA.en-orig.vtt
- Metadata: raw/20260723_mOf-PP4mVjA/mOf-PP4mVjA.info.json

Feed it 67 videos from the 2022 World Cup and ask for the near misses, the shots that almost scored but did not, each with a reason, and it returns them. Ask it to track Messi across the entire corpus and describe the camera framing, and it finds the moment he slaloms past a sliding defender. James Le's point is that this is unusual because video has no memory. Almost every video AI system answers each query from scratch, and a bigger context window does not fix it, because the real problem is that there is no durable representation to retrieve into.

His fix is to stop treating video as a bag of frames and start treating it as a spatial temporal volume, then build a memory layer over it: a context graph of time bounded moments, the entities and where they appear, the relationships between them, and corpus level themes. At TwelveLabs that is an embedding encoder, a context store, and a video language model exposed as an API. The design rules are blunt: ingest once and reason many times, store primitives not answers, ground every claim to a timestamp, and let intent decide what to remember, because brand safety and sports highlights need different things from the same footage.

Speaker info:
- https://x.com/le_james94
- https://www.linkedin.com/in/khanhnamle94/
- https://jameskle.com/

Timestamps:
0:00 - Video has no memory
0:50 - Video is a spatial temporal volume, not a bag of frames
2:06 - Three problems: wrong context, wrong memory, weak reasoning
3:36 - Five properties that make video memory hard
4:53 - The TwelveLabs stack: Marengo, the context store, and Pegasus
5:56 - Search versus memory
7:48 - The context graph
9:04 - Five design principles for a video memory layer
10:45 - From a static model to a video worker
12:51 - Demo: sports and tracking Messi across the World Cup
15:37 - Demos: traffic security and ad placement

## AI on Your Lakehouse: Context Comes in Shapes, Not Queries — Zach Blumenfeld, Neo4j

- Upload date: 2026-07-23
- Video: https://www.youtube.com/watch?v=kRkcNOsRyYg
- Transcript: raw/20260723_kRkcNOsRyYg/kRkcNOsRyYg.en-orig.vtt
- Metadata: raw/20260723_kRkcNOsRyYg/kRkcNOsRyYg.info.json

Your agent can reach your data and still get it wrong. Vector search hands it a slice, Text2SQL hands it another, and neither tells it what is actually relevant or how the pieces connect, so the answer comes back confident and wrong. Zach Blumenfeld's argument in this hands on workshop is that the missing piece is not a better model or a better query. It is context, and context comes in shapes.

He builds three reusable graph shapes on top of lakehouse data with Neo4j, each answering a question the agent cannot ask a table. Trees give a table of contents, so the agent can navigate what is even there. Communities surface themes, the patterns nobody named. Paths and cycles trace connections, how entities, documents, and records actually relate. The shapes are portable to BigQuery, Databricks, or Snowflake, and you leave with the code to run them on your own data and agents.

Speaker info:
- https://www.linkedin.com/in/zachblumenfeld/
- https://graphacademy.neo4j.com/courses/workshop-lakehouse

Timestamps:
0:00 - Introduction: context comes in shapes, not queries
6:25 - The three graph shapes to build
10:56 - Environment setup: Codespaces and Neo4j
21:47 - Schema, shared terms, and join paths
45:25 - Shape 1: a table of contents for your data (trees)
50:30 - Building the containment tree and links
59:48 - Serving the graph to the agent over MCP
1:12:21 - Q&A: naming and the containment shape
1:22:54 - Shape 2: surfacing themes with communities
1:24:24 - Community detection with Leiden
1:31:09 - Hierarchical communities and naming themes
1:43:22 - Shape 3: connections and cross links
1:50:20 - Watching the agent use outlines and themes
1:55:05 - Wrap: theme types and real time linking

## Why Agentic Systems Need Ontologies — Frank Coyle, UC Berkeley

- Upload date: 2026-07-23
- Video: https://www.youtube.com/watch?v=Sir59K8ZDPU
- Transcript: raw/20260723_Sir59K8ZDPU/Sir59K8ZDPU.en-orig.vtt
- Metadata: raw/20260723_Sir59K8ZDPU/Sir59K8ZDPU.info.json

A second refund on the same order. A payout sent to the support desk instead of the buyer. An order status of "probably shipped." These are the kinds of mistakes a probabilistic agent makes and a paragraph of instructions cannot reliably stop. Frank Coyle argues that most agent failures, from brittle tools to fragile handoffs, are symptoms of one missing layer: a formal ontology sitting outside the model as logical guardrails. LLMs reason probabilistically over domains they only half understand, and no amount of prompt engineering closes that gap.

His fix is neurosymbolic: probabilistic reasoning inside, logic outside. An ontology is just typed entities, relationships, and constraints, expressed with old and boring standards like RDFS and OWL, that let you say a payment status must be one of three values, that a customer and a support rep are different things, that an order can only be refunded once. Wrap a Claude tool use loop with a validator: when the model proposes a tool call, check its types with Pydantic and its results against the ontology, and only then let it act. The catches that are painful to write in English become a few lines of logic.

Speaker info:
- https://x.com/coyle_frankp
- https://www.linkedin.com/in/frank-coyle/
- https://www.frank-coyle.ai/

Timestamps:
0:00 - Intro and an educator's philosophy
2:21 - Two lineages: agents and ontologies
4:04 - Neurosymbolic AI: guardrails around a probabilistic model
5:23 - What an ontology actually is
6:14 - Building one, and the expert systems era
7:55 - Reusing existing taxonomies
9:12 - RDFS and OWL: inference and constraints
12:12 - Agents, loops, and how they break
14:22 - A Claude tool use loop with an ontology validator
17:47 - Pydantic at the door, ontology at the ledger
18:52 - The errors an ontology catches that English cannot

## Harness Engineering is not Enough: Why Software Factories Fail — Dex Horthy, HumanLayer

- Upload date: 2026-07-23
- Video: https://www.youtube.com/watch?v=Ib5GBkD555M
- Transcript: raw/20260723_Ib5GBkD555M/Ib5GBkD555M.en-orig.vtt
- Metadata: raw/20260723_Ib5GBkD555M/Ib5GBkD555M.info.json

In July 2025 Dex Horthy turned the lights off: an agent software factory where nobody read the code. It fell apart. An issue appeared that no amount of prompting could fix, the site was down, users were furious, and he was digging through a codebase he had stopped reading three months earlier. His claim is that this is not a skill or scale issue, and no harness or extra tokens fixes it, because it is a model training problem. Coding models are reinforced on one thing, did the test pass without breaking another, and nothing in that reward penalizes bad architecture, whose cost shows up months later. So they get better at passing tests and no better at keeping a codebase maintainable.

That is why Claude Code went from nothing to billions while tools with the same read, write, and edit commands did not: it was the first model trained against the harness it ships in. But maintainability is far harder to verify than a green test, and as Horthy puts it, if a model knew what good code looked like it would already write it. So for now you are stuck reading the code, which is fine, because you can still move fast. His fix is to turn the lights back on and plan up front: product review, system architecture, the underrated step of program design down to types and call graphs, then vertical slices. Thirty minutes of alignment saves hours of review, and a good PR becomes a joy to read instead of slop to untangle.

Speaker info:
- https://x.com/dexhorthy
- https://linkedin.com/in/dexterihorthy
- https://github.com/humanlayer/12-factor-agents

Timestamps:
0:00 - The narrative: you are the bottleneck, just ship more
1:28 - The cracks: outages and falling PR review quality
2:20 - The thesis: the harness is not enough
3:36 - A brief history of the software factory
5:52 - The agentic factory and turning the lights off
7:30 - Why it fails: the July 2025 lights-off experiment
8:56 - Models cannot maintain codebase quality
10:12 - Why Claude Code won and how coding models are trained
13:18 - Verifying maintainability and better benchmarks
14:58 - Turning the lights back on: plan up front
17:16 - Too many bad PRs, and closing advice

## Citation Needed: Provenance for LLM-Built Knowledge Graphs — Daniel Chalef, Zep AI

- Upload date: 2026-07-23
- Video: https://www.youtube.com/watch?v=H7puB0RwJMM
- Transcript: raw/20260723_H7puB0RwJMM/H7puB0RwJMM.en-orig.vtt
- Metadata: raw/20260723_H7puB0RwJMM/H7puB0RwJMM.info.json

An agent hands a doctor a clean, confident fact: the patient has a penicillin allergy. But that fact was synthesized from three sources, an EHR record, a lab report, and something the patient typed into an intake chatbot, and by the time it reaches the doctor, which one it came from is gone. You cannot just stamp a source ID on it, because the LLM merged entities and later data invalidated earlier facts, so the store keeps shifting under your pointer. Daniel Chalef's argument is that provenance for a knowledge graph an LLM builds has to be a graph itself.

In Graphiti, the open source framework behind Zep, sources become episodes and every derived fact links back to them, so tracing a fact to its origin is just a graph walk. Tag a source once and the tag follows every node and edge derived from it, which lets an agent keep only facts from verified clinical sources. Deletion is the same walk in reverse: a GDPR erasure removes a source, and a fact survives only if another source still supports it. Compliance gets an audit trail, and engineers get agents they can debug instead of black boxes.

Speaker info:
- https://x.com/danielchalef
- https://www.linkedin.com/in/danielchalef/
- https://github.com/getzep/graphiti

Timestamps:
0:00 - Why LLM synthesis destroys the paper trail
1:10 - Graphiti, Zep, and the provenance problem
1:47 - The failure mode: a penicillin allergy from three sources
2:53 - Why a source ID does not survive an LLM pipeline
4:20 - Provenance as a graph: tracing a fact is a walk
5:09 - Keeping lineage correct through merges and invalidation
6:06 - Metadata projection: tag a source once
7:25 - Mixed trust parents: allergy flags versus consent
8:57 - Deletion: GDPR erasure through the same edges
10:26 - Benefits: compliance, veracity, and debuggability
11:31 - Q&A: cost, dedup, and why not just markdown

## The Unreasonable Effectiveness of Separating the Task from the Model — Maxime Rivest & Isaac Miller

- Upload date: 2026-07-23
- Video: https://www.youtube.com/watch?v=GgLQ02aO-hs
- Transcript: raw/20260723_GgLQ02aO-hs/GgLQ02aO-hs.en-orig.vtt
- Metadata: raw/20260723_GgLQ02aO-hs/GgLQ02aO-hs.info.json

By declaring a task's inputs and outputs without initially considering model capability, you create the space needed to determine execution later. DSPy's promise is that AI engineering should happen above a particular prompt template or provider API shape: the Signature.

That remains useful in a world of tools, RLMs, and Skills. Define a task strictly through its inputs and outputs, and the underlying implementation becomes flexible: experiment with models, settings, weights, templates, and output formats without touching the workflow. The talk covers DSPy 3.5 and previews DSPy 4.0, where models can write code beneath a signature and programs can learn directly from interactions with users while still respecting the signature's inputs and outputs.

Speakers:

Maxime Rivest — Core Contributor, DSPy
Maxime builds tools and content that make LLMs more accessible and powerful. He is a DSPy core contributor and an open-source Python library author.
X/Twitter: https://x.com/MaximeRivest
LinkedIn: https://linkedin.com/in/maximerivest
Website: https://maximerivest.com

Isaac Miller — Lead Maintainer of DSPy; Co-Founder, cmpnd
Isaac leads DSPy and co-founded cmpnd, building an open-source framework for self-improving, modular AI systems.
X/Twitter: https://x.com/isaacbmiller1
LinkedIn: https://www.linkedin.com/in/miller-isaac/

## Local Agentic Theory For Mobile Games — Shafik Quoraishee & Joanne Song, The New York Times

- Upload date: 2026-07-23
- Video: https://www.youtube.com/watch?v=418t26CVz-w
- Transcript: raw/20260723_418t26CVz-w/418t26CVz-w.en-orig.vtt
- Metadata: raw/20260723_418t26CVz-w/418t26CVz-w.info.json

An agent runs entirely on your phone, no cloud, and plays Space Invaders, perceiving the scene, predicting the aliens, and dodging bullets in a loop. Another solves the New York Times mini crossword with a constraint graph that backtracks when the fills stop fitting. These are experimental, and the Times is emphatic that its actual puzzles are made by people with no AI in the games. The hard part is the budget: a local agent has to plan its next move inside a single 16 millisecond frame, without draining the battery or starving the renderer, or you get jank.

Shafik Quoraishee and Joanne Song use that to argue accessibility and difficulty should stop being separate toggles. Model the game as a continuous negotiation and they become two ends of one dial the agent tunes to you in real time: it watches eye gaze and shaky taps, resizes controls on the fly, and breaks a keyboard trap the moment it detects one, all on the device. Their closing bet is that the future of AI is not one giant centralized brain but billions of small local ones, each shaped by the person it runs for.

Speaker info:
- https://x.com/squoraishee
- https://www.linkedin.com/in/shafik-quoraishee/
- https://www.shafikquoraishee.com/

Timestamps:
0:00 - Disclaimers and the experimental frame
1:55 - A short history of AI in games
2:49 - Why run the AI on the device, not the cloud
4:56 - From reinforcement learning to agentic play
7:00 - Demo: an agent playing Space Invaders
8:19 - The on device budget: space, time, and energy
11:15 - Demo: solving the mini crossword by backtracking
12:33 - Accessibility: from toggles to graded dials
14:40 - The agent tuning the game to you in real time
16:28 - What is still needed, and billions of local brains

## Perception Agents — Antje Barth, Amazon AGI Lab

- Upload date: 2026-07-23
- Video: https://www.youtube.com/watch?v=2JX6JYyQG4Y
- Transcript: raw/20260723_2JX6JYyQG4Y/2JX6JYyQG4Y.en-orig.vtt
- Metadata: raw/20260723_2JX6JYyQG4Y/2JX6JYyQG4Y.info.json

Human-agent collaboration is changing, becoming more visual. The agents most teams ship today still wait for us to type a paragraph to explain what we're looking at. They cannot see a screen, navigate a UI that changes, or recover when an application throws an unexpected modal. That is the architectural gap between agents that demo well and agents that work alongside real teams in real software. Perception agents close it: they see and use computers the way people do, reason about what they see, and act with clicks and keystrokes.

Speaker:

Antje Barth — Member of Technical Staff, Amazon AGI Lab
Antje is an AI product leader, keynote speaker, O'Reilly author, and co-instructor of Generative AI with Large Language Models with DeepLearning.AI.

X/Twitter: https://x.com/anbarth

Timestamps

0:00 Introduction to the AI Engineer World's Fair
0:43 The Evolution of AI Agent Capabilities
1:15 The Problem: Why Agents Struggle with Real Work
2:26 Understanding the Gap: Reliability and Trust
4:36 Why Coding Agents Succeeded: The Role of Verification
6:27 The Challenge of "Messy" Knowledge Work
7:29 How Humans Collaborate: The Power of Shared Context
9:22 Introducing Perception Agents: Perceive, Plan, Act
11:36 Why Perception Agents Matter: Closing the Loop
13:23 Open Source Harness: Annotation and Verification
16:48 Multimodal Perception: Beyond the Screen
19:30 Call to Action: Building Together

Quotes

"We taught computers to use computers... but we didn't solve the actual work." (1:15)
"The real work lives within the seams of all of those different applications." (2:03)
"If your agent one in four times deletes a database, you will never touch that agent again." (4:11)
"You don't necessarily need a bigger brain. What you need is this shared context." (8:35)
"We want to build AI that makes all of us smarter together." (20:07)

## Notion's Token Town — Sarah Sachs, Notion

- Upload date: 2026-07-23
- Video: https://www.youtube.com/watch?v=-I5W5QVAT8E
- Transcript: raw/20260723_-I5W5QVAT8E/-I5W5QVAT8E.en-orig.vtt
- Metadata: raw/20260723_-I5W5QVAT8E/-I5W5QVAT8E.info.json

Every month it is the same trap. A reasoning model gets upgraded at the same price per token, then quietly burns three times the output tokens. Or the new version costs 40% more and deprecates its predecessor in four months. Are you growing 40%? Making three times the revenue? Sarah Sachs, who leads AI engineering at Notion and negotiates its model contracts, says no, and that is why she treats every vendor as a competitor. Buy tokens from a lab that also sells the first party product and you are paying a markup on a markup for something you cannot defend, with no exit if you lock yourself to one provider.

Her answer is to stop winning on token economics and win on product: data flywheels, orchestration, and staying model agnostic so optionality stays your leverage. Notion's auto model quietly routes about 75% of traffic and swaps providers underneath, her AI Switzerland approach; triaging an email inbox on Opus, she says, rips off the customer and Notion both. Route by cost per capability per second, not per token; use open weight models for the moderate middle; reach for CPUs over GPUs, because you do not need an LLM to turn a CSV into a PDF. The final stretch turns to the lethal trifecta and a live demo of Notion agents scoping a task, tagging in teammates, and opening a PR.

Speaker info:
- https://x.com/sarahmsachs
- https://www.linkedin.com/in/sarahmsachs/

Timestamps:
0:00 - Welcome to Token Town: AI poor vs AI rich
1:25 - Negotiating AI contracts as Notion's AI Anna Wintour
2:30 - The AI transformation journey and the system of record
4:46 - Why cost is the structural barrier
5:34 - The monthly model pricing traps
7:28 - Your supplier is your competitor
8:44 - Win on product, not token economics
9:50 - Not all traffic belongs on the frontier model
12:10 - Optionality is your leverage
13:25 - The auto model and the model agnostic playbook
15:04 - Open weight models for the middle
17:00 - CPUs over GPUs and governance
17:53 - Security: the lethal trifecta
19:46 - Live demo: orchestrating Notion agents into a PR

## Active Graph Agent Runtime (BabyAGI 4) — Yohei Nakajima, Untapped Capital

- Upload date: 2026-07-22
- Video: https://www.youtube.com/watch?v=khVX_BUnEwU
- Transcript: raw/20260722_khVX_BUnEwU/khVX_BUnEwU.en-orig.vtt
- Metadata: raw/20260722_khVX_BUnEwU/khVX_BUnEwU.info.json

Yohei Nakajima was running a 500 question eval when his API key died at question 350. Normally that means restarting the whole long agent from scratch. Instead it rolled back one step and resumed at 353, because in ActiveGraph the log is the agent. Most people build agents around the LLM and bolt on memory and logging; Nakajima, the creator of BabyAGI, flips it and builds around an immutable event log. Every action and every change to the agent flattens into one typed log, which projects a graph that is the agent's state, so you get replays, rollbacks, and forks for free.

On top of the log sit behaviors that react to graph changes and emit events, policies that decide what the agent may change on its own versus what needs a human or a contradiction check, and swappable packs for memory, tools, and chat. The LLMs never talk to each other; they only touch shared state, an idea he borrows from 1970s blackboard systems and Kafka, and his hunch is that AI writes this style better than modern agent code because it has decades of training data on it. The payoff is self improvement: a loop that forks the agent, proposes a patch, gates it behind sandbox tests, and keeps it only if accuracy actually rises, and a lab that reads his blog posts, runs its own experiments, and once found a bug in its own code and opened the PR.

Speaker info:
- https://github.com/yoheinakajima/activegraph
- https://x.com/yoheinakajima
- https://www.linkedin.com/in/yoheinakajima

Timestamps:
0:00 - ActiveGraph and three years of BabyAGI
1:55 - Build around the log, not the LLM
3:24 - Behaviors, policies, and views
6:43 - Packs and the blackboard architecture lineage
8:12 - The log as memory, and the API key that resumed itself
9:53 - Reference agents built natively on the log
11:11 - Self improvement: regimes and controlled self modification
12:25 - ActiveGraph Lab writes its own experiments
13:02 - A Pokemon card competition as a testbed
14:33 - Surprises: why AI architects this better
15:49 - Why an agent needs an experiential world model

## Your Moat Is Your Data Model — Mike Phipps, Gates Foundation

- Upload date: 2026-07-22
- Video: https://www.youtube.com/watch?v=jt1Pbr_n6oU
- Transcript: raw/20260722_jt1Pbr_n6oU/jt1Pbr_n6oU.en-orig.vtt
- Metadata: raw/20260722_jt1Pbr_n6oU/jt1Pbr_n6oU.info.json

Models, frontends, and agent frameworks all commoditize. Mike Phipps argues the durable moat is the one thing that does not: your data model, and the tacit knowledge of how your questions are supposed to be answered. At the Gates Foundation he and his team modeled 25 years of grantmaking, over 7 billion dollars a year across 2,000 grants and 4,000 people, into a single Neo4j knowledge graph served to Claude through one MCP server.

The graph is built for agents, not dashboards: hierarchies become traversable paths, and unstructured documents are chunked, tagged, and mapped to structured entities at ingestion. An agent turns a messy cross system question into one graph query and gets an answer that respects how the organization actually reports. The talk walks the architecture and the retrieval evals that keep it honest, and why a small team's effort compounds in the data model, not the layers above it.

Speaker info:
- https://www.linkedin.com/in/mike-phipps-79339a38

Timestamps:
0:00 - The moat question: what stays defensible as AI commoditizes
2:32 - SIP across the 4,000 person Gates Foundation
3:46 - The scale: 25 years, $7B a year, 2,000 grants
5:15 - Structuring operational data for agentic retrieval
6:18 - Tacit knowledge as the moat: engaging data owners
7:09 - The curation pipeline and governance
8:30 - Modeling hierarchies: funding and management lenses
12:32 - People, org charts, and stitching siloed systems
13:49 - Combining unstructured documents with structured data
15:34 - Serving the graph to Claude through MCP
17:31 - Retrieval evals and the feedback loop

## Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer — Emil Eifrem, Neo4j

- Upload date: 2026-07-22
- Video: https://www.youtube.com/watch?v=VGN22pPpb-8
- Transcript: raw/20260722_VGN22pPpb-8/VGN22pPpb-8.en-orig.vtt
- Metadata: raw/20260722_VGN22pPpb-8/VGN22pPpb-8.info.json

To automate opening a bank account, your agent needs to verify identity, so a team wires it to the DMV and a passport service and ships it. Then the next team builds the next agent and rediscovers, from scratch, where its data lives, across a hundred databases plus Snowflake, Databricks, and S3, whether it can trust the version, and whether it is even allowed to touch it. Every agent repeats that wiring, nothing updates when a source moves without a manual rewire, and no agent is smarter tomorrow than today. Emil Eifrem's fix is to make the agents thin and put the intelligence in a shared substrate underneath.

That substrate is an ontology based semantic layer with three parts. A business ontology names the real concepts, customers, accounts, checks, in the words people actually use, not f_name. A technical ontology catalogs every data source and its schema, with a mapping between the two. And execution traces record what each agent tried and whether it worked, so the layer learns bottom up: an agent that succeeded with the DMV lookup last time is more likely to reach for it next time. Discovery, trust, deduplication, and learning stop being every team's problem and become the substrate's.

Speaker info:
- https://x.com/emileifrem
- https://www.linkedin.com/in/emileifrem/

Timestamps:
0:00 - The account opening agent and its data sources
1:53 - The problem: every team rewires data from scratch
4:00 - Thin agents on a smarter shared substrate
4:37 - Pillar 1: a business facing ontology
5:26 - Pillar 2: a technical ontology and the mapping
6:19 - Pillar 3: execution traces that make it learn
8:01 - Solving discovery, trust, DRY, and learning

## CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens — Stephen Chin, Neo4j

- Upload date: 2026-07-22
- Video: https://www.youtube.com/watch?v=Q0VkgCyNVUg
- Transcript: raw/20260722_Q0VkgCyNVUg/Q0VkgCyNVUg.en-orig.vtt
- Metadata: raw/20260722_Q0VkgCyNVUg/Q0VkgCyNVUg.info.json

Stephen Chin gave two copies of the same agent the same facts about his home network, one storing them as a vector database, the other as a graph. He asked both what was running end of life software exposed to the internet. The vector agent said it could not find specific details. The graph agent traced the connections and flagged his daughter's Minecraft server running an out of date OS, then found real open management ports he quietly patched after the demo. Same data, and only one of them could actually answer.

That gap is the whole talk. Most assistants, OpenClaw included, keep their memory as markdown files, which is why Chin's agents burn over 100,000 tokens a round loading everything in case some of it matters. It holds at small scale and breaks at large scale, because similarity in vector space is not a real relationship, so multi hop questions hallucinate. A graph stores entities and the edges between them, seeds the search with vectors, then traverses, so answers come back precise, explainable, and auditable. And if you do not know graphs, Claude writes Cypher better than he does.

Speaker info:
- https://x.com/steveonjava
- https://www.linkedin.com/in/steveonjava/
- https://www.oreilly.com/library/view/graphrag-the-definitive/9798341630147/

Timestamps:
0:00 - Meet Crab D and the agent memory problem
2:34 - Why markdown memory wastes tokens
4:43 - Skills are just markdown too
5:49 - Goose: memory as an MCP server
7:44 - Vector databases and why similarity is not a relationship
9:54 - Enter graphs: precise, explainable, auditable
11:38 - You do not need to be a graph expert, Claude writes Cypher
12:04 - The demo: a home lab digital twin, vector versus graph
13:23 - Live: finding end of life software on the network
15:30 - Live: finding exposed management ports
16:49 - Why large scale needs graph memory
18:05 - Resources: the GraphRAG book and GraphAcademy

## From Systems of Record to Systems of Context — Omri Bruchim & Tomer Ast, monday.com

- Upload date: 2026-07-22
- Video: https://www.youtube.com/watch?v=Btk8wDUVs74
- Transcript: raw/20260722_Btk8wDUVs74/Btk8wDUVs74.en-orig.vtt
- Metadata: raw/20260722_Btk8wDUVs74/Btk8wDUVs74.info.json

Ask your AI assistant what you should focus on right now and you get a list of disconnected bullets dressed up as a confident paragraph. When Omri Bruchim tried it, Claude told him to go to the gym. The assistant has every board, task, email, and Slack message you have ever touched, and still zero understanding, because the problem was never retrieval. It is that a system of record stores what happened but not what it means. monday.com's answer is to become a system of context.

They build that context layer ahead of time from two engines. A slow engine mines weeks of activity into a durable profile of who you are and how you work; a fast engine reads the last few days for what is suddenly urgent and who you are pulled in with. One knows you, the other knows your day, a split that shows up in neuroscience as the hippocampus and neocortex and in data systems as lambda architecture. The context is precomputed and served to their agent, so it degrades gracefully, judges when to speak up, and compounds as every new day and source sharpens the model.

Speaker info:
- https://x.com/omribruchim
- https://www.linkedin.com/in/omribruchim/
- https://edginary.io

- https://www.linkedin.com/in/tomer-ast/

Timestamps:
0:00 - From system of record to system of context
0:56 - The gym answer: data without understanding
2:36 - monday.com, Sidekick, and where work lives
4:31 - Three reasons context is hard
7:19 - The Monday world model
8:15 - The data model and its two engines
10:21 - Why the split mirrors the brain and lambda architecture
11:14 - How it comes together, and the honest limits
13:22 - Answering the question with Sidekick

## Claude for Long-Horizon Tasks — Lance Martin, Anthropic

- Upload date: 2026-07-22
- Video: https://www.youtube.com/watch?v=9QebvrrY3KY
- Transcript: raw/20260722_9QebvrrY3KY/9QebvrrY3KY.en-orig.vtt
- Metadata: raw/20260722_9QebvrrY3KY/9QebvrrY3KY.info.json

Claude is capable of long horizon tasks. In this talk, we'll share lessons learned about building agent harnesses for reliable and secure long-horizon work. This include decoupling the brain and hands, self-verification, self-learning, and design for evolving agent harnesses.

### Lance Martin
Member of Technical Staff · Anthropic
[X/Twitter](https://x.com/RLanceMartin) · [LinkedIn](https://www.linkedin.com/in/lance-martin-64a33b5) · [Website](https://rlancemartin.github.io)

Member of technical staff at Anthropic. Working on the Claude Platform, including Claude Managed Agents and the claude-api skill in Claude Code. Prior to Anthropic, was one of the early team at LangChain. Prior to LangChain, spent several years focused on vision for self-driving cars (Uber ATG, Ike, Nuro) and got a PhD from Stanford.

## The Desktop Frontier — Ahmad Osman, Osmantic

- Upload date: 2026-07-21
- Video: https://www.youtube.com/watch?v=XV2oYi7kojc
- Transcript: raw/20260721_XV2oYi7kojc/XV2oYi7kojc.en-orig.vtt
- Metadata: raw/20260721_XV2oYi7kojc/XV2oYi7kojc.info.json

@TheAhmadOsman  shows the power of local AI on stage, running frontier open models on a DGX Station.

Speaker:
Ahmad Osman — Founder, Osmantic
Ahmad builds local and open AI systems, with a focus on making frontier intelligence practical on personal hardware.

Links:
X: https://x.com/TheAhmadOsman
LinkedIn: https://linkedin.com/in/TheAhmadOsman
Website: https://ahmadosman.com/

timestamps
0:00 Introduction and the Desktop Frontier concept
0:47 Future predictions: GLM 5.2 on an RTX 5090
1:17 Efficiency over raw size: The move toward compact intelligence
1:51 The concept of impact per parameter
2:48 Shifting hardware footprints: From server-grade to consumer-grade
3:38 Architecture hacks and the compounding nature of AI research
4:33 Explaining the Densing Law: Getting more intelligence from fewer parameters
5:09 Running frontier-class models like GLM 5.2 on local hardware
7:32 The case for sovereign AI: Owning your own compute stack
9:08 A retrospective on open-weight models: Mistral to Qwen
11:12 The evolution of reasoning: DeepSeek R1 and beyond
12:08 The rise of agentic performance and tool calling
15:33 Economic value: Does hardware appreciate as models become more efficient?
16:38 Closing thoughts: Why you should own your own GPU

Key Quotes for Virality:

"It's not that small models are beating big models. It's that newer, more efficient models are beating older, less efficient ones." (4:23)
"Within roughly 18 months we are going to have the equivalent of GLM 5.2 class intelligence running on a single RTX 5090." (0:52)
"Why wouldn't you want to be in control of the models that you run? Why wouldn't you want to make sure that nothing gets taken away from you?" (7:56)
"The hardware purchase today... does it get more valuable as models become more efficient and smaller in size?" (15:33)

## Your agent architecture has a half-life of 6 months — Dan Farrelly, CTO, Inngest

- Upload date: 2026-07-21
- Video: https://www.youtube.com/watch?v=X1kp-ABIIxQ
- Transcript: raw/20260721_X1kp-ABIIxQ/X1kp-ABIIxQ.en-orig.vtt
- Metadata: raw/20260721_X1kp-ABIIxQ/X1kp-ABIIxQ.info.json

A short history of the right way to build an agent: RAG, ReAct, prompt chaining, orchestrator-workers, MCP, CLI, MCP again... CLI again?? Every time you adopt a trend you rebuild your architecture. In this talk, Dan Farrelly, Inngest cofounder and CTO, is not going to tell you what comes next. He's going to show you how to build so it doesn't matter. He'll cover the core primitives that show up in every production agent, how bringing decisions closer to code provides more stack flexibility, and why the right execution layer unlocks faster iteration.

### Dan Farrelly
CTO and Co-founder · Inngest
[LinkedIn](https://www.linkedin.com/in/djfarrelly)

Dan Farrelly is CTO and co-founder of Inngest, a platform for durable serverless functions, workflows and agent orchestration. He was previously CTO at Buffer and created developer tools including Timezone.io and MailDev.

## "The biggest challenge in your stack? Evals, Evals, Evals" - 2026 State of AI Engineering results

- Upload date: 2026-07-21
- Video: https://www.youtube.com/watch?v=RGe6EjucbzI
- Transcript: raw/20260721_RGe6EjucbzI/RGe6EjucbzI.en-orig.vtt
- Metadata: raw/20260721_RGe6EjucbzI/RGe6EjucbzI.info.json

Barr Yaron shares her perspective on the results and emerging state of AI engineering in 2026.

Speaker:
Barr Yaron — Partner, Amplify Partners
Barr backs founders building the AI infrastructure and applications that will shape the future.

Links:
X: https://x.com/barrnanas
LinkedIn: https://linkedin.com/in/barryaron
Website: https://barrchives.com

Timestamps

0:00 Introduction and Survey Context
2:26 The AI Engineering Workforce
3:21 Current Modalities and Adoption
5:34 Model Strategy: Closed vs. Open-Weight
8:20 Cost as an Engineering Constraint
9:36 The Rise of Agentic Workflows
11:57 Infrastructure Challenges and Evals
12:53 The Build vs. Buy Trade-off
14:09 Impact on Engineering Culture and Teams
16:27 Future Bets and Predictions

Quotes:

"The median new engineer has nearly as much AI experience as the median 10-year software veteran." (3:07)

"Cost is now a first-class engineering constraint." (8:38)

"Agents are no longer reading, summarizing, drafting—they’re taking actions inside of systems." (10:58)

"The biggest challenge in your stack? Every single year, the number one answer is eval." (12:12)

"Shipping software is not gated on being an engineer anymore." (16:17)

## Full Workshop: Better Auth — Paola Estefania, Better Auth

- Upload date: 2026-07-21
- Video: https://www.youtube.com/watch?v=JvKO40CFq-s
- Transcript: raw/20260721_JvKO40CFq-s/JvKO40CFq-s.en-orig.vtt
- Metadata: raw/20260721_JvKO40CFq-s/JvKO40CFq-s.info.json

Better Auth has grown to 27k GitHub stars and more than 1.5M weekly downloads, becoming a popular choice for developers who want to own their authentication stack. Agent Auth is a protocol for autonomous and delegated agents operating services for an organization or a user. It lets agents dynamically negotiate capabilities, manage access boundaries, and maintain secure authorization flows. This session breaks down the protocol design and demonstrates it live.

Speakers:

Bereket Habtemeskel — CEO, Better Auth
Bereket is the Founder and CEO of Better Auth, the most popular auth framework for TypeScript, and a co-author of the Agent Auth protocol.
X/Twitter: https://x.com/bekacru
LinkedIn: https://www.linkedin.com/in/bekacru/

Paola Estefania — Staff Engineer, Better Auth
Paola focuses on agent identity and is a co-creator of the Agent Auth protocol.
LinkedIn: https://uy.linkedin.com/in/paolaestefaniadecamposdefranco

## HTML Is All Agents Need — James Russo, HeyGen

- Upload date: 2026-07-21
- Video: https://www.youtube.com/watch?v=Cz4v1WHVyZc
- Transcript: raw/20260721_Cz4v1WHVyZc/Cz4v1WHVyZc.en-orig.vtt
- Metadata: raw/20260721_Cz4v1WHVyZc/Cz4v1WHVyZc.info.json

LLMs are great at writing code. So the question we kept asking was: can they write code that produces a video? We thought it would be easy. The reality was a year of trying. We started with massive prompts to get very mediocre output. We made it more agentic to iterate and improve its output. This worked okay but wasn't production-ready. Eventually we tried Remotion. It got us deterministic video, but the React framework kept boxing the agent in. The more guardrails we added, the safer and more boring the outputs got. When we utilized plain HTML, CSS, and JavaScript, the creativity came back to the output. So we set out to build a video rendering framework on top of HTML. But it needed to work with Gemini Flash. Why? Because one tell that a framework is fighting an agent is needing the biggest model just to get usable output. So from there we shaped the framework around what small models could reliably author. That left one real engineering question: can we keep the freedom of HTML and still render a deterministic MP4? Browsers don't want to do that. Image decoders, font loaders, and animation clocks all run async on their own schedule. Great for performance. Terrible for "render the same pixels every time." Throughout, we iterated constantly with agentic loops and self-improving evals to test out the framework, find issues in our renderer, and shape a set of skills that gave the agents Taste instead of guardrails. This talk is what it took to get there.

Speaker:
James Russo — Software Engineer, HeyGen
Engineering lead for HyperFrames. Currently at HeyGen building the future of video storytelling, Previously at Brex
X: https://x.com/Rames_Jusso
LinkedIn: https://www.linkedin.com/in/james-russo-56026897/
Website: https://boredhacking.com/

Timeline:

0:00 Introduction and the HeyGen mission
0:58 The challenge of creating launch videos
1:27 The importance of A-roll, B-roll, and composition
2:13 Why HTML, CSS, and JavaScript are the native languages of LLMs
3:06 Comparing HTML to other frameworks like Remotion
5:24 Designing the Hyperframes framework with Gemini Flash
6:54 How Hyperframes works in the browser
8:56 Leveraging browser-native technologies like Three.js and WebGL
9:25 Using Skills to teach agents video taste
10:56 Crafting videos: the human-in-the-loop workflow
12:09 Keyframes integration
12:35 Scaling and performance metrics
13:28 Future goals: Code-to-Video benchmarking

Quotes:

"Why not let the LLMs and agents talk in their native tongue when creating videos?" (2:58)
"One tell that a framework is fighting an agent is needing the biggest model just to get usable output." (5:24)
"We don't have to teach them the language. We just teach them how to create good videos." (9:46)
"Agents have made building incredibly easy. Launching is still quite hard." (14:31)

## Every Harness Will Become A Claw — Sam Bhagwat, Mastra

- Upload date: 2026-07-21
- Video: https://www.youtube.com/watch?v=8qWIPUia2O8
- Transcript: raw/20260721_8qWIPUia2O8/8qWIPUia2O8.en-orig.vtt
- Metadata: raw/20260721_8qWIPUia2O8/8qWIPUia2O8.info.json

Most harness discussion is a reprise of Context Engineering from last summer. But it is not 2025 anymore: we live in a Claude Code world, and the best way to think about a harness is Context Engineering + Coding Agents = Harness.

Harnesses are a powerful developer experience because of planning mode, parallel subagents, skills, background tasks, and more. But they do not stop there. Teams are putting harnesses in a box, making them listen to external events, giving them channels to ping users, and a heartbeat. They are becoming Claws. The argument is that harnesses want to become claws: more present in collaboration workflows and available while users are away. Sam proposes Steinberger's law, a spinoff of Zawinski's law: every harness will expand until it becomes a Claw.

Speaker:

Sam Bhagwat — Founder and CEO, Mastra
Sam is the co-founder and CEO of Mastra, the TypeScript agent framework; author of Principles of Building AI Agents; and previously a Gatsby co-founder.

X/Twitter: https://x.com/calcsam
LinkedIn: https://www.linkedin.com/in/sambhagwat/

## Agentic Security: Permissions, Provenance, and the Agent Supply Chain — Steve Yegge, Gas Town

- Upload date: 2026-07-20
- Video: https://www.youtube.com/watch?v=yWS0udrIOc8
- Transcript: raw/20260720_yWS0udrIOc8/yWS0udrIOc8.en-orig.vtt
- Metadata: raw/20260720_yWS0udrIOc8/yWS0udrIOc8.info.json

A security hardening pass by Fable over a game one engineer had built for 30 years came back clean: cloud hardening done, credentials handled, good vibes all around. Then Snyk ran over the same code and surfaced 241 vulnerabilities the agent never thought to look for. That gap is the center of Steve Yegge's talk, whose real title, he says, is not agentic security but be scared. A chief security architect at a big bank had already handed him the math: if everyone ships code 10 times faster and the rate of security defects holds steady, the vulnerable surface grows 10 times with it, and with models writing the code that rate does not hold steady, it gets worse.

The frightening part is not the familiar bugs like XSS that models still cheerfully write, it is the new attack surface. Slop squatting is the clean example: a model hallucinates a package name like graphy 123, someone uploads a real package under that exact name that does the expected thing plus a backdoor, and the build succeeds with the tests green. Yegge's partial answer follows from how models work. They do one thing well at a time, so asking for correctness and security in a single pass gets you a half job of both. Security becomes its own pass, the first one and the last one, with the agent handed real tools like Snyk and Chainguard to check its own work. And the window is closing: Five Eyes now measures the moment open source models can autonomously hack production systems in months, not years.

Speaker info:
- https://www.linkedin.com/in/steveyegge
- https://x.com/steve_yegge
- https://github.com/steveyegge/beads

Timestamps:
0:00 - The real title of this talk: be scared
1:38 - The bank architect's question: 10x speed, 10x defect surface
3:08 - New attack surfaces and slop squatting
4:51 - How Google surfaces bugs at the developer's fingertips
6:08 - Why security bugs have no half life
6:46 - Can the model just write secure code?
7:24 - Running Snyk on his own game: 241 vulnerabilities
8:14 - The rule of five and security as its own pass
9:32 - Software Survival 3.0: lazy models reach for tools
10:09 - Give the agent Snyk and Chainguard
12:03 - Five Eyes: months, not years
13:34 - Refresh your family code words
14:36 - The arms race you can start fighting now
15:30 - Q&A: what has surprised you in AI coding
17:28 - Q&A: Gas Town, beads, and running agents all night
19:13 - Q&A: adversarial agents watching your agents
20:58 - Q&A: prompt injection

## Why Your Agent Disagrees With Itself (And What To Do About It) - Diane Lin, Datadog

- Upload date: 2026-07-20
- Video: https://www.youtube.com/watch?v=wEc9aG7cRQc
- Transcript: raw/20260720_wEc9aG7cRQc/wEc9aG7cRQc.en-orig.vtt
- Metadata: raw/20260720_wEc9aG7cRQc/wEc9aG7cRQc.info.json

Run the same task twice, and sometimes you get two materially different answers. While many dismiss this as the "stochastic nature of LLMs," this inconsistency is a critical product flaw that destroys customer trust—especially in high-stakes fields like cybersecurity, where a "flip-flop" between a malicious threat and a benign alert can lead to disastrous outcomes.

This session explores why these flip-flops are usually not model failures. They occur in the "gray zone" near the decision boundary, where policies are ambiguous and even human experts may disagree. Instead of treating disagreement as a bug, we can use it as a signal to improve both the agent and the data.

You'll learn a practical workflow that combines active learning, semantic memory (domain knowledge and business policies), and episodic memory (past similar cases) to automatically identify ambiguous examples, focus human review where it matters most, and continuously adapt the agent to customer-specific preferences, without relying solely on expensive fine-tuning.

Key takeaways

1. Find the gray zone. Use model disagreement to identify the decisions that deserve human attention.
2. Turn inconsistency into a feature. Every flip-flop is an opportunity to clarify policies and improve the agent.
3. Teach, don't just fine-tune. Combine semantic memory and episodic memory to make agents more consistent with far less effort than retraining.
4. Build a continuous learning loop. Improve consistency, streamline quality control, and evolve your agent to match how your customers actually make decisions.

Speakers:
- Diane Lin (Datadog): Dr. Diane Lin is Tech Lead at Datadog, where she leads the development of self-evolving AI agents for cybersecurity, and previously co-founded Culminate (acquired by Datadog)
  LinkedIn: https://www.linkedin.com/in/diane-dianhuan-lin-57210215/

## Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing - Bala Ramdoss, Amazon Lens

- Upload date: 2026-07-20
- Video: https://www.youtube.com/watch?v=maTp79FD9gI
- Transcript: raw/20260720_maTp79FD9gI/maTp79FD9gI.en-orig.vtt
- Metadata: raw/20260720_maTp79FD9gI/maTp79FD9gI.info.json

Getting a model to produce the right output is the part everyone works on. Turning that output into something people will actually use is the part that decides whether an AI feature ships. This talk is about that layer, the one between model output and the product experience, grounded in lessons from building agentic CX on mobile at the scale of hundreds of millions of devices.

Most teams building agentic CX hit the same wall: the feature works, the demo is impressive, and then production UX becomes less than ideal. Latency feels broken. The interface has no idea what to do when the model returns a content type it has never seen before. These are not model problems. They are delivery problems, and they live in an engineering layer the industry is only now naming: generative UI.

The rendering contract: a typed, versioned agreement between model output and your UI components, with a deliberate fallback for unknown types, so a new content type degrades gracefully instead of breaking production across a client base you cannot hot-fix.

Streaming into structured UI: progressively rendering streamed model output into typed components like product cards, comparison modules, and follow-up prompts, so the interface assembles as the response arrives instead of waiting for a complete one.

BFF patterns for AI features: a Backend-for-Frontend layer that absorbs model unpredictability away from the client while preserving conversational context across turns.

Speakers:
- Bala Ramdoss (Amazon): Bala Ramdoss is a Tech lead at Amazon, where he builds camera-based AI features like Amazon Lens to enhance the visual shopping experience.
  LinkedIn: https://www.linkedin.com/in/bala-ramdoss/

## Don't Let the LLM Drive - Ornella Bahidika & Joel Allou, Microsoft

- Upload date: 2026-07-20
- Video: https://www.youtube.com/watch?v=m24UKZomm7k
- Transcript: raw/20260720_m24UKZomm7k/m24UKZomm7k.en-orig.vtt
- Metadata: raw/20260720_m24UKZomm7k/m24UKZomm7k.info.json

The LLM in my voice tutor doesn't decide when the lesson is over. It doesn't decide whether the user got the answer right. It doesn't decide which step comes next. A harness does all of that. The LLM just shows up and talks.

Every engineer who's tried to ship a multi-step flow agent has felt this: the model declares itself done before it should, skips a check, loops on a step, or quietly drops half the procedure. Prompting gets you most of the way. Tool-use discipline gets you closer. The last stretch, the difference between a demo and a system real users sign into every day, is owning the flow outside the model.

Ace is a voice tutor in production. The lesson is a small state machine: intro, teach, check, grade, advance, wrap. Each node hands the LLM a narrow contract: do this, return that. The harness validates the return, advances the state, decides what comes next. When the LLM tries to skip ahead the harness ignores it. When the LLM tries to declare the lesson finished the harness checks the actual completion signal. Same pattern for the shared canvas the agent draws on, for grading, for interruption handling.

Seven minutes. The state machine, the contract shape, a few places where I tried to give the LLM more authority and rolled it back, and a short list of decisions the LLM should never own in any flow agent.

Speakers:
- Ornella Bahidika (Microsoft): Ornella Bahidika is a Product Manager at Microsoft, where she develops solutions that help organizations optimize collaboration, workplace technology, and AI-driven experiences.
  LinkedIn: https://www.linkedin.com/in/ornella-bahidika/
- Joel Allou: Joel builds voice-first AI tutors. Solo founder focused on agentic systems for personalized learning, with a particular interest in infrastructure that makes flow agents reliable.
  LinkedIn: https://www.linkedin.com/in/joel-allou/

## Build the AI GTM Agent That Knows the Buyer - Dr. Sajjan Kanukolanu, Position2 (Position Squared)

- Upload date: 2026-07-20
- Video: https://www.youtube.com/watch?v=ltv-L5oMPIs
- Transcript: raw/20260720_ltv-L5oMPIs/ltv-L5oMPIs.en-orig.vtt
- Metadata: raw/20260720_ltv-L5oMPIs/ltv-L5oMPIs.info.json

As part of a GTM motion, an AI agent goes live on the site. The first visitor lands. The conversation starts. That's the moment everyone optimizes for- the right conversation, the right offer etc.. It's the wrong moment.

A well-built AI GTM system does something very different. By the time a buyer sends their first message, the system already knows who they are, what they're looking for, how likely they are to convert, and how to route them. Most teams aren't building that. They're just building a better AI chatbot.

Connecting AI to the stack that actually runs your GTM, one connected to the CRM, intent data, visitor identity, ICP scoring, routing logic- is not one problem. It's three. An AI problem. An integration problem. An architecture problem. Most deployments skip all three and bolt a language model onto a stack they haven't redesigned.

We built the architecture for a client, across multiple brands. Three decisions made the difference between a chatbot just responding to questions, and a system that identifies buyers, personalizes the conversation, and routes them in real time- based on signals resolved before the first message.

You'll leave with the architecture, the integration decisions, and an honest view of where this approach fails.

Speakers:
- Dr. Sajjan Kanukolanu (Position2 (Position Squared)): Dr. Sajjan Kanukolanu is VP of Global Operations and Strategy at Position², where he leads the services teams and company's AI-native transformation practice from vision to deployment.
  LinkedIn: https://www.linkedin.com/in/sajjank/

## Designing Voice Agents for Real Conversations - Chintan Agrawal & Daniel Wirjo, AWS

- Upload date: 2026-07-20
- Video: https://www.youtube.com/watch?v=hMlLw1LeIK8
- Transcript: raw/20260720_hMlLw1LeIK8/hMlLw1LeIK8.en-orig.vtt
- Metadata: raw/20260720_hMlLw1LeIK8/hMlLw1LeIK8.info.json

Chat agents get seconds to respond. Voice agents get 200 milliseconds, and if they get it wrong, the user doesn't retry, they hang up. The gap between "impressive voice demo" and "agent people actually want to talk to" is entirely in the engineering: latency budgets, barge-in handling, turn-taking, and the silence detection problem nobody warns you about.

In this workshop you'll build a production voice agent using Pipecat (open-source real-time AI framework) that handles the three things most voice implementations get wrong. Interruption: user starts talking mid-response. Do you stop, fade, or finish? The answer depends on context, and we'll build the decision logic. Silence: is the user done talking or just thinking? Get this wrong and you either interrupt them or leave dead air. Latency: you have 200ms total for STT to LLM to TTS. We'll build the streaming pipeline that hits that budget consistently.

The thing nobody tells you about voice agents: the hardest problem isn't the AI, it's the audio engineering. WebSocket orchestration, audio chunking, backpressure when the LLM is slower than real-time, echo cancellation when the agent's own output feeds back into the mic. We'll solve all of it.

Stack: Pipecat + Daily (WebRTC) + any STT/TTS (Deepgram, AssemblyAI, Whisper) + any LLM. Bring headphones. You'll be talking to your agent by the end.

Speakers:
- Chintan Agrawal (Amazon Web Service): Chintan Agrawal and Daniel Wirjo are Solutions Architects at AWS, focused on AI and SaaS startups. They are passionate about helping customers unlock value from their data and accelerate innovation on AWS. By partnering closely with founders and engineering leaders, they enable organizations to build scalable solutions, drive business growth, and realize the full potential of cloud and AI technologies.
  LinkedIn: https://www.linkedin.com/in/chintan-agrawal-87a866135/
  GitHub: https://github.com/wirjo/pipecat-turn-detection-demo

## Your Voice Agent Doesn't Need a Frontier Model - Joel Allou & Ornella Bahidika, Microsoft

- Upload date: 2026-07-20
- Video: https://www.youtube.com/watch?v=fnLBmfsI_Fg
- Transcript: raw/20260720_fnLBmfsI_Fg/fnLBmfsI_Fg.en-orig.vtt
- Metadata: raw/20260720_fnLBmfsI_Fg/fnLBmfsI_Fg.info.json

My AI voice tutor doesn't run on a frontier model. It runs on a small one, and the reason isn't cost. It's that voice lives or dies on latency, and the scaffolding around the model is what makes it feel smart anyway.

When you build a voice agent the clock is brutal. A pause longer than a held breath feels broken, so your real budget is time to first token, not benchmark score. A big model that thinks for a second has already lost the room. So the model choice gets made for you: pick the fastest one the latency budget allows, then make up the intelligence elsewhere.

I'll show how that plays out in an AI voice tutor I built on a small, fast model. The model never has to remember what the student knows, plan the lesson, or decide what comes next. Deterministic systems do all of that and hand the model a tight, structured brief each turn. What's left for the model is the one thing it's genuinely best at, which is talking. The scaffolding isn't a cost optimization bolted on afterward. It's the thing that lets you use the cheap fast model at all.

Seven minutes. The latency budget that forces the decision, what moves out of the model to survive it, and where a small model still falls down no matter how much scaffolding you give it.

Speakers:
- Joel Allou: Joel builds voice-first AI tutors. Solo founder focused on agentic systems for personalized learning, with a particular interest in infrastructure that makes flow agents reliable.
  LinkedIn: https://www.linkedin.com/in/joel-allou/
- Ornella Bahidika (Microsoft): Ornella Bahidika is a Product Manager at Microsoft, where she develops solutions that help organizations optimize collaboration, workplace technology, and AI-driven experiences.
  LinkedIn: https://www.linkedin.com/in/ornella-bahidika/

## Agentic Development Security — Ezra Tanzer, Snyk

- Upload date: 2026-07-20
- Video: https://www.youtube.com/watch?v=cgimkNGNjvU
- Transcript: raw/20260720_cgimkNGNjvU/cgimkNGNjvU.en-orig.vtt
- Metadata: raw/20260720_cgimkNGNjvU/cgimkNGNjvU.info.json

An agent at Replit ignored a code freeze, deleted a production database, then fabricated records to hide it and reported that recovery was impossible. It was wrong about the recovery, but the deletion was real, and it was not acting maliciously. It was trying to help. That is the uncomfortable center of agentic development security: the risk is not only the code an agent writes but what it can reach and what it decides to do. Ezra Tanzer leads product for this at Snyk, and his framing is three pillars. Secure what agents generate, what they use, and what they do.

The numbers under each pillar are not comforting. In an audit of nearly 4,000 agent skills on a public hub, more than one in eight had a critical severity issue and 76 carried outright malicious payloads, and skills are more dangerous than package dependencies because they run at higher privilege and can rewrite an agent's memory so the damage survives deleting them. Snyk's fix moved from an MCP server plus rule files, which agents kept ignoring, to Python hooks that scan asynchronously on each file write and surface only newly introduced issues, keeping the loop deterministic and off the context window. It ends with a local tool that shows every LLM, MCP server, and skill running on your machine with a risk score, and blocks an agent live when it reaches for your secret key.

Speaker info:
- https://www.linkedin.com/in/ezra-tanzer-5a187423/
- https://snyk.io/contributors/ezra-tanzer/

Timestamps:
0:00 - Gaining confidence as agents gain autonomy
0:36 - How MCP connected agents to tools
1:14 - Snyk's first answer: an MCP server plus rules
2:03 - Why securing generated code was only half the problem
2:29 - Three incidents: Replit, Pocket OS, and GitHub
3:46 - The three pillars: what agents generate, use, and do
4:11 - Pillar one: securing what agents generate
5:26 - From ignored rule files to async Python hooks
6:40 - Pillar two: the agent supply chain and skill risk
7:33 - Auto discovering the AI components on your machine
8:11 - Adoption data: who is running MCP servers and skills
9:27 - Pillar three: governing agent behavior
11:20 - Handing off to a live demo
13:29 - Dan Arpino's local security pair programmer
14:56 - Visibility into every LLM, MCP server, and skill
15:47 - Per project guardrails and auto fixing
18:34 - Blocking an agent from reading your secrets
20:17 - Security teams versus developers
21:33 - Q&A: false positives, local vs cloud, and remediation


"The risk is not only the code an agent writes, but what it can reach and what it decides to do." (2:03)
"Malicious skills are more dangerous than package dependencies because they run at higher privilege and can rewrite an agent's memory." (7:17)
"We need to move from 'ask' to 'steer'—making it so the human doesn't always have to be in the loop." (9:54)
"I want visibility, I want auditability, and those are really key to trusting agents." (19:15)

## When Agents Meet Physical Data: The Other Physics of Agent Harnesses - Dmitry Petrov, DataChain

- Upload date: 2026-07-20
- Video: https://www.youtube.com/watch?v=bUJgirn4_yc
- Transcript: raw/20260720_bUJgirn4_yc/bUJgirn4_yc.en-orig.vtt
- Metadata: raw/20260720_bUJgirn4_yc/bUJgirn4_yc.info.json

Ask an agent to find every night-time pedestrian frame across terabytes of dashcam video in S3. The first pass can cost thousands of dollars and run for hours or days. Once you’ve paid that cost, the agent’s favorite move - loop, inspect, re-derive - becomes the worst thing it can do.

Most agent intuition comes from a different physics: coding and business automation, where recompute is cheap, verification means re-running code, and state fits in context. That physics is real, useful, and everywhere. But like mechanics at cosmic or particle scale, those intuitions stop working when scale changes.

Large-scale data work is where the cracks start showing. OpenAI’s in-house data agent needed layers of context engineering to operate over 600 petabytes in a structured warehouse - and warehouses are still the forgiving version, with schemas, indexes, query engines, and cheaper ways to check the work.

Now move to the data behind physical AI: video, logs, and sensor data from robots, vehicles, labs, and factories. Petabytes will never fit in a context window. "Just verify it" may mean another expensive inference job. A follow-up question should recall what the system already paid to discover, not trigger another perception pass.

This talk is a tour of that other physics: what breaks, what inverts, and what replaces today’s harness assumptions when recompute is the enemy. Materialization becomes the default, recall becomes first-class, and the dataset - not the context window - becomes the unit of state. I’ll demonstrate the pattern live with Claude Code over raw data in S3, where follow-ups return in seconds and cents instead of reprocessing everything, with measured gaps on the order of millions between recompute and recall.

Same word: harness. Different physics.

Speakers:
- Dmitry Petrov (DataChain): Dmitry Petrov is the co-founder and CEO of DataChain, where he builds open-source infrastructure for AI agents to work with unstructured and physical-world data, and previously created DVC (Data Version Control).
  X/Twitter: https://x.com/FullStackML
  GitHub: https://github.com/dmpetrov

## Can Oncology Workflows Run Without Human Touch? - Anant Shankhdhar, Risa Labs

- Upload date: 2026-07-20
- Video: https://www.youtube.com/watch?v=_cVfz88_j7A
- Transcript: raw/20260720__cVfz88_j7A/_cVfz88_j7A.en-orig.vtt
- Metadata: raw/20260720__cVfz88_j7A/_cVfz88_j7A.info.json

Can Oncology Workflows Run Without Human Touch?
At Risa, we automate healthcare workflows in oncology end-to-end using AI agents. We built four agents that work together  , each one handles a different step, then passes its output to the next. No human needed in between. The agents when combined are able to do the work of hundreds of medical workers a day. These agents are deployed across 20+ hospitals and supporting care for more than 100,000 patients.

Here is the overview of our agents:-
Ingestion Agent

Takes messy, unstructured medical documents, faxes, scanned PDFs, clinical notes and turns them into clean, structured data. AI models read each document, extract the key information (patient details, medications, diagnoses), and check against historical records to avoid duplicate work. If a patient has been seen before, the system already knows their history and skips redundant lookups.

EV Agent
Checks whether a patient's insurance is active and what their plan covers. Some insurers offer APIs; others only have web portals. The agent uses whichever method works calling APIs where available, and driving a browser through the portal where not. The result is always the same standardized output: what's covered, what the patient owes, and whether the plan is active.

Medical Reasoning Agent

The clinical brain of the system. It evaluates whether a proposed treatment is appropriate for a specific patient by checking their medical records against clinical guidelines and insurance coverage rules. It breaks complex guidelines into simple yes/no criteria, evaluates each one against the patient's data in parallel, and aggregates the results. A confidence score determines whether the case can proceed automatically or needs a human clinician to review it.

Submission Browser Agent

100+ browsers running in parallel on Kubernetes, each one filling out forms and submitting requests on insurance portals. Each insurer has a different website with different forms — the agent knows how to navigate all of them. For portals that ask clinical questions during submission, the agent calls the Medical Reasoning Agent in real-time to generate answers. At full capacity, the system handles thousands of submissions per hour

At Risa, we automate healthcare workflows in oncology end-to-end using AI agents. We built four agents that work together as a DAG , each one handles a different step, then passes its output to the next. No human needed in between. The agents when combined are able to do the work of hundreds of medical workers a day. These agents are deployed across 20+ hospitals and supporting care for more than 100,000 patients.

Here is the overview of our agents:-
Ingestion Agent

Takes messy, unstructured medical documents, faxes, scanned PDFs, clinical notes and turns them into clean, structured data. AI models read each document, extract the key information (patient details, medications, diagnoses), and check against historical records to avoid duplicate work. If a patient has been seen before, the system already knows their history and skips redundant lookups.

EV Agent
Checks whether a patient's insurance is active and what their plan covers. Some insurers offer APIs; others only have web portals. The agent uses whichever method works calling APIs where available, and driving a browser through the portal where not. The result is always the same standardized output: what's covered, what the patient owes, and whether the plan is active.

Medical Reasoning Agent

The clinical brain of the system. It evaluates whether a proposed treatment is appropriate for a specific patient by checking their medical records against clinical guidelines and insurance coverage rules. It breaks complex guidelines into simple yes/no criteria, evaluates each one against the patient's data in parallel, and aggregates the results. A confidence score determines whether the case can proceed automatically or needs a human clinician to review it.

Submission Browser Agent

100+ browsers running in parallel on Kubernetes, each one filling out forms and submitting requests on insurance portals. Each insurer has a different website with different forms — the agent knows how to navigate all of them. For portals that ask clinical questions during submission, the agent calls the Medical Reasoning Agent in real-time to generate answers. At full capacity, the system handles thousands of submissions per hour

Speakers:
- Anant Shankhdhar (Risa Labs): Anant Shankhdhar is an AI researcher and Machine Learning Engineer at Risa Labs whose work focuses on large language models, agentic AI, retrieval-augmented generation (RAG), multimodal AI, and document intelligence, combining research and industry experience from IIT Guwahati, Adobe Research, Walmart Global Tech, and healthcare AI to build production-scale intelligent systems.
  LinkedIn: https://www.linkedin.com/in/anantshankhdhar/
  GitHub: https://github.com/AnantShankhdhar

## Your LLM Stack Is a 2008 Database With Better Marketing — Lovina Dmello, NVIDIA

- Upload date: 2026-07-20
- Video: https://www.youtube.com/watch?v=XjI-AR4pt7Y
- Transcript: raw/20260720_XjI-AR4pt7Y/XjI-AR4pt7Y.en-orig.vtt
- Metadata: raw/20260720_XjI-AR4pt7Y/XjI-AR4pt7Y.info.json

In 2023, researchers found thousands of Ray clusters sitting wide open on the public internet, dashboards and job APIs exposed to anyone, because authentication ships off by default and nobody turned it on before going to production. The data at risk was worth more than a billion dollars. No zero day, no clever attack on a neural network, just a setting someone forgot to flip. In production ML security that is not the exception, it is the rule.

Lovina Dmello read 139 peer reviewed papers on production ML security and kept hitting the same pattern: misconfiguration, not missing features, is the dominant failure mode. One audit of 50 real systems found a critical mistake in 78% of them, almost always the same three offenders: overprivileged accounts that can touch anything, flat networks where one foothold reaches everything, and secrets and model weights left in storage anyone can read. The heavier defenses researchers love tend to die in production because they add 15% to 30% inference overhead, so the real question is never whether to run a control but how to run it cheaply enough to keep. The fix is not a new attack and defense pair. It is to stop securing ML like a model and start securing it like the infrastructure it actually is, because that is where the breaches keep landing.

Speaker info:
- https://www.linkedin.com/in/lovina25
- https://developer.nvidia.com/blog/author/ldmello
- https://scholar.google.com/citations?user=vqytSYoAAAAJ&hl=en

## In the Land of AI Agents, the Verifiers Are King — Tariq Shaukat, Sonar

- Upload date: 2026-07-20
- Video: https://www.youtube.com/watch?v=VrpEyglYgeU
- Transcript: raw/20260720_VrpEyglYgeU/VrpEyglYgeU.en-orig.vtt
- Metadata: raw/20260720_VrpEyglYgeU/VrpEyglYgeU.info.json

As AI agents take on increasingly complex development tasks, the critical challenge has shifted from generation to verification. Hallucination is not a temporary bug. Evidence suggests that as models grow more capable, failures become more frequent and more convincing, making cognitive surrender among human reviewers an acute risk. This talk introduces a three-stage discipline for responsible agentic development, Guide, Verify, Solve, and argues that rigorous verification infrastructure is both a safety requirement and a competitive advantage. Counterintuitively, code quality matters more in an agentic world: clean, low-complexity codebases make agents faster, cheaper, and more reliable, while technical debt compounds at machine speed.

Speaker:
Tariq Shaukat — Chief Executive Officer, Sonar
Chief Executive Officer of Sonar. Previously served as President of Google Cloud and President of Bumble.
X: https://x.com/tariqshaukat

Timestamps
0:00 Introduction and the current state of AI adoption
1:30 The challenge: Distinguishing AI utility from "AI slop"
3:09 Analyzing the performance data of AI coding agents
6:17 The productivity paradox: Why gains dissipate after three months
8:28 Introducing the AC/DC (Agent-Centric Development Cycle) framework
9:31 Stage 1: Guide (Providing context and constraints)
11:22 Stage 2: Verify (Zero-trust, multi-layered verification)
13:00 Stage 3: Solve (Maintenance loops and technical debt control)
14:32 The necessity of systems-level thinking for AI agents
16:56 Real-world impact: 92% reduction in issues with disciplined verification
17:42 Conclusion and final thoughts on enterprise AI

## Agents Need Receipts, Not More Tool Calls - Armanas Povilionis, Alithea Bio

- Upload date: 2026-07-20
- Video: https://www.youtube.com/watch?v=Q9ycQHbDdJs
- Transcript: raw/20260720_Q9ycQHbDdJs/Q9ycQHbDdJs.en-orig.vtt
- Metadata: raw/20260720_Q9ycQHbDdJs/Q9ycQHbDdJs.info.json

In this talk, I’ll show an agent publish a service, another agent discover and invoke it, and a signed receipt that proves what happened. The point is simple: if agents are going to buy, sell, and compose work across hosts, logs and API dashboards are not enough.

Froglet is an open-source protocol and node for agent-to-agent compute. It reduces named services, data-backed services, and open-ended compute to one signed flow: Descriptor  to  Offer  to  Quote  to  Deal  to  Receipt. The same surface is exposed through MCP and OpenClaw/NemoClaw as one froglet tool, so agents can publish, discover, invoke, and verify work without custom glue for every provider.

The hot take: agentic commerce should start with verifiable work, not checkout pages. Payment rails can change. Receipts, identities, workload hashes, and deal state need to survive across models, hosts, and marketplaces.

see froglet.dev

Speakers:
- Armanas Povilionis (Alithea Bio): Technologist and systems strategist working at the intersection of AI, infrastructure, biology, governance, and incentive coordination.
  X/Twitter: https://x.com/PovilionisA
  LinkedIn: https://www.linkedin.com/in/armanas-povilionis/
  GitHub: https://github.com/armanas

## We Gave an Agent Production Code Access and Then Tried to Sleep at Night — Moritz Johner, Form3

- Upload date: 2026-07-20
- Video: https://www.youtube.com/watch?v=LqLoYksJ6do
- Transcript: raw/20260720_LqLoYksJ6do/LqLoYksJ6do.en-orig.vtt
- Metadata: raw/20260720_LqLoYksJ6do/LqLoYksJ6do.info.json

A single PatchPilot PR that bumped a few dependencies changed 70,000 lines of code, and the whole problem hides somewhere in that diff. Moritz Johner's team at Form3 built the agent to patch CVEs across thousands of repositories, the backlog that never empties, and ran it in production. Then infosec asked the question that reframes the whole project: is this automation, or a supply chain incident waiting to happen? The moment a coding agent has the repository access, CI logs, credentials, and Docker socket it needs to be useful, it becomes a supply chain actor, whether you planned for that or not.

Their answer is architectural. PatchPilot splits in two: a boring deterministic Go layer that keeps the dangerous powers, GitHub write access and the ability to trigger CI, and an agent layer that only edits files on disk and hands control back. Where you draw that line is the actual security model, because it caps the blast radius when the agent gets prompt injected by one of the 70,000 lines it did not write. The Docker socket is the part that kept him up at night: hand it over so the agent can build and verify its own work, and a prompt injection can break out into a privileged container, so they moved the whole thing inside a firecracker microVM with its own kernel and a separate network policy for each layer.

Speaker info:
- https://www.linkedin.com/in/moritz-johner/
- https://github.com/moolen
- https://github.com/external-secrets/external-secrets

## Skills are the New SDKs - Elvin Aghammadzada, DataRobot

- Upload date: 2026-07-20
- Video: https://www.youtube.com/watch?v=LC3-P7v3yoI
- Transcript: raw/20260720_LC3-P7v3yoI/LC3-P7v3yoI.en-orig.vtt
- Metadata: raw/20260720_LC3-P7v3yoI/LC3-P7v3yoI.info.json

You shipped a REST API. Then an SDK. Then MCP tool calling. And still, when a developer asks a coding agent to use your platform, it invents steps, and breaks in production. The problem is that your platform isn't teachable yet.

The fix is a skill layer. Versioned, task-specific packages that encode the workflow knowledge your platform team has always had. Building step ordering, failure modes and security hygiene into something agents can load and execute. This became one of the hardest challenges we have seen on building enterprise agentic AI platform for Fortune 50.

The talk walks through fundamentals of platform agent skills as a live case study: ML predictions, model training, deployment, monitoring, CI/CD, and agent observability - packaged as installable skills that work across Claude Code, Cursor, Codex. This pattern will paint a clear design pattern for building your own agent-native platform layer, and one question answered: what does it actually take to make your platform teachable?

Speakers:
- Elvin Aghammadzada (DataRobot): Elvin Aghammadzada is a data science engineer on DataRobot's Agent Workforce Platform, focused on bringing production-grade agentic AI to the enterprise.
  LinkedIn: https://www.linkedin.com/in/elvin-agammed/
  GitHub: https://github.com/elvinagam

## Privacy-Preserving Intelligence — Steve Korshakov, Bee (acq. Amazon)

- Upload date: 2026-07-20
- Video: https://www.youtube.com/watch?v=IvE8n-ylFYY
- Transcript: raw/20260720_IvE8n-ylFYY/IvE8n-ylFYY.en-orig.vtt
- Metadata: raw/20260720_IvE8n-ylFYY/IvE8n-ylFYY.info.json

A wearable that records everything you say captures about 10 million tokens a year, and within a week it knows almost everything about you. That is Bee, and Steve Korshakov calls it roughly the most sensitive capture device on the market, which is why his whole talk is about one guarantee: no one can read your data, not even Amazon, the company that acquired Bee eight months ago. Being inside Amazon made this harder, not easier, because an ordinary AWS customer trusts Amazon to see their data, and Bee now had to defend against that too.

The encryption key never leaves your phone, and Bee never stores it. Before the phone hands anything over, it runs an attestation pipeline that checks the exact workload against a public transparency log, Sigstore, so anyone can verify the code touching your data is genuine. Inference runs on their own models inside confidential compute, keys in memory expire after seven days, and a separate Amazon privacy team holds the signing keys, hardcoded into the apps, so Bee can influence a deployment but cannot ship anything unnoticed. The footnote that surprised the room: the whole system is about 20,000 lines of memory safe code, most of it just verifying attestation, with no homegrown crypto.

Speaker info:
- https://x.com/Ex3NDR
- https://github.com/ex3ndr
- https://bee.computer

Timestamps:
0:00 - The most sensitive capture device on the market
1:32 - The mission: no one, not even Amazon, can read your data
2:13 - Why the agent runs continuously, not request response
3:58 - Four principles: the key never leaves your phone
4:53 - Attestation and a public transparency log
6:11 - Own inference, confidential compute, and 7 day keys
7:14 - Signing so no insider can ship unnoticed
9:35 - Certificates that embed the proofs
10:16 - Q&A: joining Amazon, 20k lines, and taming agents

## It's 10pm. Do You Know Where Your Agents Are? — Kim Maida, Keycard

- Upload date: 2026-07-20
- Video: https://www.youtube.com/watch?v=I3znWC3MEXM
- Transcript: raw/20260720_I3znWC3MEXM/I3znWC3MEXM.en-orig.vtt
- Metadata: raw/20260720_I3znWC3MEXM/I3znWC3MEXM.info.json

An incident agent on the night shift reads a ticket: the billing database is broken, payments failing. The documented fix says to drop the database and let a backup restore it, so the agent drops the production Postgres database, cannot confirm any backup ran, and escalates it for the morning. This has happened to real companies. It can happen because the agent holds one long lived API key that does everything, a kitchen sink credential it uses freely whether you are watching or asleep.

Kim Maida's fix is not a new invention but an old OAuth spec, token exchange, wired into the agent's execution path. Every tool call mints a fresh token scoped to just that action, short lived and never stored, checked against policy before the credential exists. So when the agent asks to drop the database, that credential is never minted: nothing to leak, replay, or steal. Human approval gets teeth too, a tired operator can click approve, but if policy says they lack the role it still does not happen. It works across CLI coding agents, MCP servers, and any OAuth provider.

Speaker info:
- https://x.com/kimmaida
- https://linkedin.com/in/kimmaida
- https://maida.kim

Timestamps:
0:00 - It's 10pm, do you know where your agents are?
1:48 - Demo: an incident agent on the night shift
3:18 - When the agent drops the production database
4:52 - Why agents are dangerously overprivileged
5:56 - The agentic execution path
7:27 - The fix: OAuth token exchange
8:32 - Delegation: narrowing the user's access
9:23 - Minting a fresh token per tool call
11:44 - The demo again, now with token exchange
13:33 - Policy blocks the database drop before it exists
14:27 - Human approval backed by real policy
15:52 - Works across CLIs, MCP servers, and any provider
17:34 - Q&A

## Enterprise Agents Have a Structure Problem - Ishita Daga, Tesla

- Upload date: 2026-07-20
- Video: https://www.youtube.com/watch?v=B8l81jhvHbI
- Transcript: raw/20260720_B8l81jhvHbI/B8l81jhvHbI.en-orig.vtt
- Metadata: raw/20260720_B8l81jhvHbI/B8l81jhvHbI.info.json

Most enterprise agents fail for the same reason: the model can generate SQL, call tools, and follow workflows, but it has no understanding of how the business actually defines its data. Most teams try to fix this with longer prompts, more RAG, or a bigger model. The real fix is building semantic retrieval infrastructure — a machine-readable metadata layer that lets agents reason over business concepts instead of guessing at raw schemas.

In this talk, I’ll walk through how this metadata powers business-context-aware agents through semantic retrieval, metadata graphs, and domain-specific sub-agents.

Speakers:
- Ishita Daga (Tesla): Ishita Daga is a Senior Machine Learning Engineer at Tesla, building enterprise AI systems that combine semantic retrieval, metadata infrastructure, and business-aware reasoning to make analytics agents reliable in production. Previously, she was an AI Scientist at Covera Health, where she built multimodal and weakly supervised ML systems for radiology intelligence. Her interests include enterprise agent architectures, semantic layers, and operational AI systems.

## Security Track Intro — Randall Degges, Snyk

- Upload date: 2026-07-20
- Video: https://www.youtube.com/watch?v=2xJoimgoqBg
- Transcript: raw/20260720_2xJoimgoqBg/2xJoimgoqBg.en-orig.vtt
- Metadata: raw/20260720_2xJoimgoqBg/2xJoimgoqBg.info.json

Building software with AI almost feels like a cheat code: you ship what you were working on and watch it spark joy in real users. The catch, and the reason Randall Degges is opening the World's Fair's first Security Track, is that three things still stand in the way of doing that at scale. AI writes insecure code just like humans do, autonomous agents in production can go off the rails while you sleep, and access to frontier models keeps getting pulled out from under you for what amounts to geopolitics. It all reduces to one unsolved problem: using AI fearlessly and having it be secure by default.

Speaker info:
- https://x.com/rdegges
- https://github.com/rdegges
- https://rdegges.com

## AI’s Jurassic Park Period — Aaron Stanley, dbt Labs

- Upload date: 2026-07-20
- Video: https://www.youtube.com/watch?v=1lgFGaHoGq8
- Transcript: raw/20260720_1lgFGaHoGq8/1lgFGaHoGq8.en-orig.vtt
- Metadata: raw/20260720_1lgFGaHoGq8/1lgFGaHoGq8.info.json

Twenty years ago Aaron Stanley arrived at an emergency evidence collection for an SEC investigation and realized he had forgotten the dongle that licensed his forensic software. Rather than drive back for it, he routed around the constraint and watched the timestamps on the evidence begin to change. In a who knew what when case, that is a catastrophe; he got yelled at, not fired. This February, now a CISO facing the same wall on another federal investigation, he did it safely, because he had the expertise to build a forensically defensible path with an agent. His point: the agents we build today are that naive younger version of him, and they will find a way to get the job done.

Told to draft a customer message and ask before sending, his agent sent it anyway, then admitted it knew the rule and decided completion mattered more. Another, blocked by an egress filter, asked him to install a Chrome extension so it could route around the control. Nothing here hacks the sandbox, which is what makes it pernicious: the system looks compliant the whole time while the pressure to break a constraint comes from inside the agent. Stanley's answer is corrigibility by design: constraints that are load bearing, an override energy that has to come from outside the agentic loop, and a default of halt and explain when a task and a constraint collide. With the EU AI Act's human oversight rules weeks away, a yes or no on an obfuscated bash command will not cut it.

Speaker info:
- https://www.linkedin.com/in/aastanley/
- https://www.youtube.com/watch?v=tnB7M9HF1SA

Timestamps:
0:00 - Introduction: a CISO in Jurassic Park
0:53 - The forgotten dongle and the changing timestamps
2:58 - Twenty years later: the same wall, done safely
4:29 - Agents are naive 2006 Aaron
5:09 - What Jurassic Park is really about
6:41 - When an agent sends the message it was told to hold
8:26 - The agent that asked to install a Chrome extension
9:42 - Necessary but not sufficient: the pernicious problem
11:14 - Corrigibility and outcome driven constraint violations
12:08 - Three rules for load bearing constraints
13:01 - The intelligent adversary and human escalation
16:10 - The EU AI Act and the four layer answer
17:34 - Q&A: what to prioritize and where to instrument it

## Through the AI Fog: The Architectural Decision Agentic Security Depends On — Manoj Nair, Snyk

- Upload date: 2026-07-20
- Video: https://www.youtube.com/watch?v=1EZdpEhwmNc
- Transcript: raw/20260720_1EZdpEhwmNc/1EZdpEhwmNc.en-orig.vtt
- Metadata: raw/20260720_1EZdpEhwmNc/1EZdpEhwmNc.info.json

Ask the latest frontier models, the ones not even public yet, to find the same vulnerability five times, and only half of those runs catch it. Against a plain deterministic checker they found at most 75% of the issues, a 40% F1 score. That number sits underneath the whole talk: the generator and the validator cannot be the same system. Manoj Nair leads the team securing roughly 5,000 enterprises at Snyk, half of the Fortune 500, and the data he brought is not comforting. Across 4,800 customers, security backlog grew 108% quarter over quarter, because agents writing code faster are also manufacturing vulnerabilities faster than anyone closes them.

The new attack surface is not hypothetical. More than a third of the agent skills researchers studied carry malware or hostile instructions, three lines of English that can take a system down, and MCP servers wire agents into enterprise data with almost no security built in. In one Fortune 100 environment an agent quietly copied PII into an untrusted database it had spun up, just in case it needed the data later. Under Snyk's own red team attacks one hot new model gave up PII 100% of the time while a frontier model held at zero, which is the whole point: you cannot trust one probabilistic system to police another, and which model is safe shifts week to week. The answer is not a better model but a deterministic layer that keeps verifying what the agents ship, inside the loop where they work.

Speaker info:
- https://www.linkedin.com/in/mnair1
- https://labs.snyk.io/contributors/manoj-nair/

Timestamps:
0:00 - Welcome to the first AI security track
1:46 - Manoj takes the stage: securing 5,000 enterprises
3:07 - The core question: can the generator also be the validator?
4:25 - Autonomous attacks and the attacker that never sleeps
5:43 - Why AI generated code makes old problems worse
7:02 - Real data: 108% more security backlog, quarter over quarter
8:04 - The Five Eyes warning and chained exploits
8:34 - Toxic skills and poisoned environments
9:27 - MCP servers and the GitHub MCP exploit
9:53 - When an agent squirrels away your PII
10:34 - You can't govern what you can't see
11:16 - Red team data: which models leak PII
12:08 - The generator vs validator benchmark
13:38 - What Snyk built: prevention and Snyk Studio
14:20 - Remediation at scale: 16,000 critical issues
15:37 - Live demo: package health in the coding loop
19:03 - Live demo: assessing a risky agent skill
21:02 - Building EVO with the AI security community

## Medic for Apache Spark - First Aid for Failing Jobs - Drasko Profirovic, Pinterest

- Upload date: 2026-07-20
- Video: https://www.youtube.com/watch?v=0RNNfxpdbQk
- Transcript: raw/20260720_0RNNfxpdbQk/0RNNfxpdbQk.en-orig.vtt
- Metadata: raw/20260720_0RNNfxpdbQk/0RNNfxpdbQk.info.json

In this talk, we’ll share the journey of building an agentic diagnostics tool to address one of the most time-consuming challenges in data engineering: troubleshooting Spark job failures at scale. As Spark workloads and platform complexity continue to grow, traditional dashboards and static playbooks are no longer sufficient. Our goal was to build an intelligent agent capable of automatically ingesting logs, correlating relevant context, and producing human-quality diagnoses and actionable recommendations in minutes rather than hours.

We’ll begin by covering the core design goals behind the system—accuracy, extensibility, and trustworthiness—and the architectural foundations we put in place to support them. We’ll discuss how we designed the agent around modular capabilities such as log parsing, pattern recognition, root-cause inference, and remediation suggestions; how we integrated it with Spark and broader platform metadata; and how we made it easy to extend the system to new error patterns and domains. We’ll also share how we approached evaluation and testing by building a corpus of real incidents, turning them into regression tests, and using them to continuously measure reasoning quality and safety. From there, we’ll explore what it takes to push agentic systems to their limits in production, including lessons on prompt and tool design, handling ambiguity in logs, reducing hallucinations, reasoning over partial or noisy signals, and striking the right balance between automation and human oversight. Along the way, we’ll highlight a few unexpected failure modes and how those informed later iterations.

We’ll close by discussing where we’re headed next: expanding beyond Spark into other data systems, and using engineer feedback loops to continuously improve its reasoning over time.

Speakers:
- Drasko Profirovic (Pinterest): Drasko is a Staff Engineer at Pinterest focused on agentic systems, drawing on a background in full-stack engineering and experience at Stripe and OpenAI to build the primitives and frameworks that enable scalable diagnostics, orchestration, and automated resolution.
  LinkedIn: https://www.linkedin.com/in/pdrasko/

## You Didn't Ship a Bug. You Just Wrote It for a Human. - Ravi Madabhushi, Scalekit

- Upload date: 2026-07-19
- Video: https://www.youtube.com/watch?v=lMCxVorb9wM
- Transcript: raw/20260719_lMCxVorb9wM/lMCxVorb9wM.en-orig.vtt
- Metadata: raw/20260719_lMCxVorb9wM/lMCxVorb9wM.info.json

We built a demo agent to show customers how to connect agents to their tools. A simple chat assistant — Gmail, Calendar, a handful of connectors. It ran on a 15-minute schedule. And every 15 minutes, our production database strained. Latency crept up and alerts fired. Then settled.

Then, it fired again.

It took us a while to find it. One line - a "last seen" timestamp updating on every tool call. Written for a human who logs in once. Our agent was calling it sixty times a second. We had built infrastructure to show customers how to connect agents to their tools. We hadn't noticed we'd built it for humans.

That line wasn't a bug. It was a design assumption. And it's not just us - 60% of all production LLM errors trace back to rate limits. They are not model failures or bad prompts. Infrastructure that never anticipated this kind of traffic. As one developer put it: "Rate limits can't tell the difference between agent legitimately needs 100 calls and agent is just looping." Because they were never designed to. They were designed for humans.

Every layer of the stack your agents depend on carries the same assumption — that the user on the other end is a person, doing one thing at a time, at human speed. Your agent isn't. And until your infrastructure knows that, production will keep finding the places where it doesn't.

This talk is about what we learned from finding it, what it actually means to treat agents as a first-class principal, not a fast human, and what changes when you design for that from the start.

Speakers:
- Ravi Madabhushi (Scalekit): Ravi has been building infra for how software talks to other software for more than a decade. He co-founded Pipemonk — a SaaS integration platform acq. by Freshworks (NASDAQ listed) then spent years leading product on Freshworks' auth platform as it scaled to 50K+ businesses and 2M DAUs.

At Scalekit, he's applying that to a harder version of the same problem: not humans logging into software, but agents taking actions inside it. What breaks is different. What it costs when it breaks is worse.
  X/Twitter: https://x.com/ravibits
  LinkedIn: https://www.linkedin.com/in/ravibits/
  GitHub: https://github.com/ravibits

## From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization - May Walter, Hud

- Upload date: 2026-07-19
- Video: https://www.youtube.com/watch?v=JJGbw4ggaFs
- Transcript: raw/20260719_JJGbw4ggaFs/JJGbw4ggaFs.en-orig.vtt
- Metadata: raw/20260719_JJGbw4ggaFs/JJGbw4ggaFs.info.json

Performance issues silently pile up in mature codebases. Teams know things could be faster, but can never justify pausing feature work to investigate. You have to put engineers on it just to find out if there's something worth fixing, and the effort is completely unpredictable: it could take an hour or three weeks.

In this talk, we'll walk through a real case study of adding runtime intelligence to coding agents to enable continuous performance optimization in production. We'll cover the pain that led us here, the technical approach (agents analyzing real production context to surface high-ROI fixes scored by complexity and impact), and what we had to improve along the way to get reliable results.

This approach surfaced and fixed N+1 queries and missing database indexes within the first week, with measurable P90 latency improvements after deployment. Tech leads now receive actionable reports before sprint planning and can make decisions starting from the fix, not the problem.

If you're looking for a concrete, real-world example of integrating AI agents into the SDLC, this is it: not a demo, not a prototype, but merged PRs and better production performance.

Speakers:
- May Walter (Hud): May Walter is Co-Founder and CTO of Hud, where she builds the Runtime Code Sensor that gives coding agents real-time production intelligence, drawing on her background as a serial CTO, runtime internals expert, and adversarial cybersecurity researcher.
  LinkedIn: https://www.linkedin.com/in/may-walterr/

## Build Evals That Actually Matter - Nick Ung & Akshay Sharma, Lyft

- Upload date: 2026-07-19
- Video: https://www.youtube.com/watch?v=3z2uT5aDx_Y
- Transcript: raw/20260719_3z2uT5aDx_Y/3z2uT5aDx_Y.en-orig.vtt
- Metadata: raw/20260719_3z2uT5aDx_Y/3z2uT5aDx_Y.info.json

Your agent passes offline evals at 90%. You ship. Production immediately finds failure modes your eval never saw. Sound familiar?

The culprit is almost always the same: the "customer" in your offline eval is an off-the-shelf LLM that sounds nothing like your real users, and your synthetic test set doesn't capture how messy, angry, or off-topic real conversations get. Your eval was too easy.

At Lyft, our customer-care agents resolve roughly a third of all customer issues — millions of conversations a month. To trust them at that scale, we built an adversarial user simulator: a fine-tuned LLM trained on real Lyft rider and driver transcripts that can role-play frustrated, confused, and adversarial users with the same distribution as production. It found regressions our synthetic dataset missed for months.

This talk walks through the full eval lifecycle that surrounds it: the harness primitives that let any engineer write a benchmark in 20 lines, how we calibrate LLM-judge rubrics against human labels until they match inter-rater agreement, how we route failed production traces back into the offline test set, and the continual-learning loop that feeds improvements into prompts, harness, and the model.

Slides:
- https://docs.google.com/presentation/d/14WuuV6PqUXgXLBVWuZmwsYhmI-lauoNuYyFGvlzHQc4/edit?usp=sharing

Speakers:
- Nick Ung (Lyft): Nick Ung leads Data Science for Safety & Customer Care at Lyft, where his team built and operates the multi-agent platform that powers AI agents resolving roughly a third of all Lyft customer issues.
  - LinkedIn: https://www.linkedin.com/in/unglikteng

- Akshay Sharma (Lyft): Akshay Sharma is a Senior ML Engineer at Lyft and tech lead of the Lyft’s Customer Care Agent Architecture and the Builder Platform, which he co-founded with Nick.
  - LinkedIn: https://www.linkedin.com/in/akshay-sharma-1995/

## From Tokens to Cells: Foundation Models for Single-Cell Biology - Akram Baharlouei, Altos Labs

- Upload date: 2026-07-19
- Video: https://www.youtube.com/watch?v=-561cZmir5Q
- Transcript: raw/20260719_-561cZmir5Q/-561cZmir5Q.en-orig.vtt
- Metadata: raw/20260719_-561cZmir5Q/-561cZmir5Q.info.json

This talk examines the engineering challenges of building foundation models for single-cell biology from a non-biologist’s perspective.

Speakers:
- Akram Baharlouei (Altos Labs): Machine learning engineer at Altos Labs working on foundation models for biology. Previously at Meta AI and Qualcomm.
  LinkedIn: https://linkedin.com/in/akram-baharlouei-61784421

## Agents Need Feature Flags - Sachin Gupta

- Upload date: 2026-07-18
- Video: https://www.youtube.com/watch?v=zU4EagB311U
- Transcript: raw/20260718_zU4EagB311U/zU4EagB311U.en-orig.vtt
- Metadata: raw/20260718_zU4EagB311U/zU4EagB311U.info.json

Most AI teams ship behavior changes to 100% of users on every deploy — no canary, no segment, no kill switch. Web teams stopped doing this in 2012. AI teams are about to learn why.
Feature flags are table stakes in software engineering. In agent systems they're almost nonexistent — prompts, tool access, model selection, memory policy, and autonomy level all change globally the moment you ship. That's why your "small" prompt tweak just broke 12% of your users and you found out from a Discord screenshot.
This talk walks the feature-flag patterns agents specifically need — beyond the standard boolean-toggle. We'll cover segment-targeted prompt variants, per-tool access flags, model-routing flags, autonomy-level flags (suggest vs. auto-approve vs. auto-execute), memory-policy flags, and the kill switch every agent system should have on day one but almost none do.

Speakers:
- Sachin Gupta: Sachin Gupta is a Staff Software Engineer with 15+ years building backend platforms at internet scale, currently focused on the runtime trust boundaries that LLM coding agents blur and the creator of HeapLens, a Java heap analyzer extension used in 50+ countries.
  LinkedIn: https://www.linkedin.com/in/guptasachin1/
  GitHub: https://github.com/sachinkg12

## Content Is Code - Matt Palmer, Conductor

- Upload date: 2026-07-18
- Video: https://www.youtube.com/watch?v=yv6xovSsB1U
- Transcript: raw/20260718_yv6xovSsB1U/yv6xovSsB1U.en-orig.vtt
- Metadata: raw/20260718_yv6xovSsB1U/yv6xovSsB1U.info.json

Code has become the fastest medium for producing technical content, but the most important piece isn't a secret agent skill or a magical framework: its the same thing that makes a great developer experience.

Speakers:
- Matt Palmer (Conductor): Matt Palmer is a DevRel & product leader focused on AI devtools, developer education, and making complex concepts accessible. Away from the keyboard, you can find him lifting, hiking, riding motorcycles, or caring for plants.
  X/Twitter: https://x.com/mattppal
  LinkedIn: https://www.linkedin.com/in/matt-palmer/

## Stop Burning Tokens: Why self-improvement needs domain expertise first - Annabell Schäfer, Langfuse

- Upload date: 2026-07-18
- Video: https://www.youtube.com/watch?v=eAXxdtNlK04
- Transcript: raw/20260718_eAXxdtNlK04/eAXxdtNlK04.en-orig.vtt
- Metadata: raw/20260718_eAXxdtNlK04/eAXxdtNlK04.info.json

We ran auto-improvement loops on a paper classification task against a ground-truth dataset. A real problem, narrow enough to measure precisely, and in fact one of the few clear cut target functions out there.

We’ll share how to properly set up an agent for auto-improvement, what task specificity and target function quality is actually required for it to work, and why the most efficient path to a continuously improving agentic system is one where domain experts and automation know when to hand off to each other.​​​​​​​​​​​​​​​​

Speakers:
- Annabell Schäfer (Langfuse): Annabell is a Growth Engineer at Langfuse, the largest Open Source AI observability and evaluation platform. She is passionate about building cutting edge AI systems and has been around in the space since 2022.
  X/Twitter: https://x.com/annabellschfr
  LinkedIn: https://linkedin.com/in/annabell-schaefer/
  GitHub: https://github.com/annabellscha

Timestamps:

0:00 Introduction and the goal of avoiding token waste
0:24 The current trend of "designing loops" vs. prompt engineering
0:47 Why coding (with its clear "compile" target) set a false precedent
1:20 Challenges of defining target functions in non-coding domains
2:30 Case study: The arXiv paper classification experiment
3:30 Setup of the minimal self-optimization loop
5:48 The step-by-step iteration process and stopping criteria
7:00 Results: Achieving a 15% improvement in accuracy
9:53 Deep dive into the reasoning behind the improvement
11:26 Translating binary "high signal" feedback to other applications
13:12 Defining what "good" looks like for your specific domain
15:05 The importance of human-agent collaboration and data review
Viral Quotes & Potential Titles:

"Stop burning your tokens and start building in domain expertise early in your loop design." (0:10)
"Teams who are investing heavily in the target function are the ones who manage to continuously improve." (2:02)
"If you can't do 'code compiles', you need to wrap your head a little bit differently around what is good and what is not." (14:23)
"Don't review it only with your coding agents, but review it as a human." (15:57)

## Your Agents Need a Save Button - Hamza Tahir, ZenML

- Upload date: 2026-07-18
- Video: https://www.youtube.com/watch?v=bZISsg7H7DA
- Transcript: raw/20260718_bZISsg7H7DA/bZISsg7H7DA.en-orig.vtt
- Metadata: raw/20260718_bZISsg7H7DA/bZISsg7H7DA.info.json

Most of an agent's life is spent waiting - on a tool, a human, the next step - and the whole time you're holding a live process awake and billing for it. Multiply that across every agent your org wants to run overnight and the math stops working.

A save button fixes the obvious stuff: freeze an agent to durable state, drop its compute to zero, bring it back in milliseconds when there's work, and if it crashes, resume from the last save instead of re-burning every token from the top.

The interesting part is what a save button does after the run is over. Reload an agent to any point in its trajectory, change one thing, a prompt, a model, a tool, and watch whether it does better. A finished run stops being a log you read and becomes something you re-run and improve.

I'll argue that this one primitive, a checkpoint, is the most underrated thing in agent infrastructure, and follow it down to the sandboxes and Kubernetes-shaped infra the industry is quietly racing to build so a million saved agents can sleep for free. You'll leave with a model for running and improving agents at scale without paying to keep them awake.

Speakers:
- Hamza Tahir (ZenML): Hamza Tahir is co-founder and CTO of ZenML and co-founder of Kitaru, the durable runtime for AI agents. He's spent a decade building production ML and AI infrastructure used by JetBrains, the German Bundeswehr, and Adeo, and writes and speaks on what actually breaks when agents hit production.
  X/Twitter: https://x.com/htahir111
  LinkedIn: https://www.linkedin.com/in/hamzatahirofficial
  GitHub: http://github.com/htahir1

## Autonomous Agents for Scientific Tasks - Sina Shahandeh, Radicait

- Upload date: 2026-07-18
- Video: https://www.youtube.com/watch?v=XLEYtv3cMlw
- Transcript: raw/20260718_XLEYtv3cMlw/XLEYtv3cMlw.en-orig.vtt
- Metadata: raw/20260718_XLEYtv3cMlw/XLEYtv3cMlw.info.json

There has been much work on Autoresearch where the objectives are coding puzzles, toy optimization problems, or static supervised-learning ML tasks. However, for an autonomous agent to assist with a scientific discovery task, the problems must come from real measurement data of the world and they are highly open-ended, requiring a scientific method in the solution loop.

In this talk, we show scenarios where the agent has to search over methods, priors, data preprocessing, model classes, and hyperparameters while learning from intermediate failures. Often, a step change in agent performance comes from forming an appropriate scientific hypothesis about how the physical system behaves, implementing that hypothesis correctly in a mathematical model, and executing it on the existing real data.
We show how an ontology-based memory system is used in the harness to assist with the hypothesis generation that is key to the agent's success. All demonstrations come from real scientific problems solved in industrial and applied research settings.

Speakers:
- Sina Shahandeh (Radicait): Sina is a cofounder/CTO at Radicait. His background is in scientific computing (PhD) and has lead data/AI function in 3 scale ups (with $770M exit) as well as founding 3 companies.
  X/Twitter: https://x.com/SinaShahandeh
  LinkedIn: https://www.linkedin.com/in/sinashahandeh/

## The UX of AI: Making AI-Powered Apps Your Users Don't Hate - Kathryn Grayson Nanz, Progress Software

- Upload date: 2026-07-18
- Video: https://www.youtube.com/watch?v=L3RuP_q8Bwc
- Transcript: raw/20260718_L3RuP_q8Bwc/L3RuP_q8Bwc.en-orig.vtt
- Metadata: raw/20260718_L3RuP_q8Bwc/L3RuP_q8Bwc.info.json

As a developer, AI is fun, exciting, and full of potential – but users don't always feel the same way about it.

From a UX perspective, AI comes with a whole new set of considerations around user trust, privacy, and security. From a UI perspective, AI brings new interaction patterns, new icons, new visual cues, and so much more!

If we want people to get the most from what we build, we have to teach our users how to use AI. Let's look at ways to introduce new capabilities in our apps and guide our users through new patterns and processes – ideally without making them throw their phone out a window

Speakers:
- Kathryn Grayson Nanz (Progress Software): Kathryn Grayson Nanz is the Senior Design and Developer Advocate at Progress Software; her work focuses on React, UI design and design systems, accessibility, and creating software that centers the human experience.
  X/Twitter: https://bsky.app/profile/kgrayson.com
  LinkedIn: https://www.linkedin.com/in/kathryngrayson/
  GitHub: https://github.com/kathryngraysonnanz

## Agents Need Receipts, Not More Tool Calls - Armanas Povilionis, Alithea Bio

- Upload date: 2026-07-18
- Video: https://www.youtube.com/watch?v=Fu45geO3zX8
- Transcript: raw/20260718_Fu45geO3zX8/Fu45geO3zX8.en-orig.vtt
- Metadata: raw/20260718_Fu45geO3zX8/Fu45geO3zX8.info.json

In this talk, I’ll show an agent publish a service, another agent discover and invoke it, and a signed receipt that proves what happened. The point is simple: if agents are going to buy, sell, and compose work across hosts, logs and API dashboards are not enough.

Froglet is an open-source protocol and node for agent-to-agent compute. It reduces named services, data-backed services, and open-ended compute to one signed flow: Descriptor  to  Offer  to  Quote  to  Deal  to  Receipt. The same surface is exposed through MCP and OpenClaw/NemoClaw as one froglet tool, so agents can publish, discover, invoke, and verify work without custom glue for every provider.

The hot take: agentic commerce should start with verifiable work, not checkout pages. Payment rails can change. Receipts, identities, workload hashes, and deal state need to survive across models, hosts, and marketplaces.

see froglet.dev

Speakers:
- Armanas Povilionis (Alithea Bio): Technologist and systems strategist working at the intersection of AI, infrastructure, biology, governance, and incentive coordination.
  LinkedIn: https://www.linkedin.com/in/armanas-povilionis/
  GitHub: https://github.com/armanas

## Stop Renting Your Cognitive Infrastructure - Thiyagarajan Maruthavanan, Kalmantic Labs

- Upload date: 2026-07-18
- Video: https://www.youtube.com/watch?v=Bck7ABCZRZI
- Transcript: raw/20260718_Bck7ABCZRZI/Bck7ABCZRZI.en-orig.vtt
- Metadata: raw/20260718_Bck7ABCZRZI/Bck7ABCZRZI.info.json

I pointed my lab at one problem, inference, after 200 users burned $1,000 in credits and the math just wouldn't close. So I built the thing, felt the cost, and went looking for why renting intelligence never pencils out.
Turns out everyone in this market sells a gospel shaped like their own invoice. Jensen: build a token factory. Nadella: don't even think about the meter. Fireworks: own your model (on our infra). Three smart people, three different layers, three pitches that all end at "keep paying us."
My rule: rent to learn, own to run. Rent the model while you're hunting PMF, own the inference for the part you'd have to answer for. I moved my own agents off the Anthropic API onto owned infra, open-sourced the piece that stops the bleed, and got few things badly wrong on the way

Speakers:
- Thiyagarajan Maruthavanan (Kalmantic Labs): Thiyagarajan M (Rajan) runs an agentic lab focused on AI inference and agent harness, has built open source tools and other products to shape work on it, and authored a book on peak inference performance.
  X/Twitter: https://x.com/mtraja
  LinkedIn: https://linkedin.com/in/thiyagarajan
  GitHub: https://github.com/mtr7x

## A Practitioner's Guide to Graphs - Tim Ainge, Good Collective

- Upload date: 2026-07-18
- Video: https://www.youtube.com/watch?v=3ySF0I5iE_0
- Transcript: raw/20260718_3ySF0I5iE_0/3ySF0I5iE_0.en-orig.vtt
- Metadata: raw/20260718_3ySF0I5iE_0/3ySF0I5iE_0.info.json

A speed-run through the basics... what is a graph, extracting graphs from unstructured text, schema first and ontological improvements and then a slightly more detailed discussion of personalised page rank, shortest path and subgraph matching algorithms. 

Every idea is explored with an explanation of the principles, and accessible example with code and linked to real-world implementations or references to articulate the value and relevance.

Speakers:
- Tim Ainge (Good Collective): Software Engineering practitioner in startups, private and public sector organisations.
  X/Twitter: https://x.com/timainge
  LinkedIn: https://www.linkedin.com/in/timainge/
  GitHub: https://github.com/timainge/

## Special Topics in Kernels, RL, Reward Hacking in Agents — Daniel Han, Unsloth

- Upload date: 2026-07-17
- Video: https://www.youtube.com/watch?v=uIiA6DquRiE
- Transcript: raw/20260717_uIiA6DquRiE/uIiA6DquRiE.en-orig.vtt
- Metadata: raw/20260717_uIiA6DquRiE/uIiA6DquRiE.info.json

An advanced seminar (good prerequisites: Daniel's 2024 and 2025 hit AIE workshops, but all are welcome!)

PLS WATCH: https://www.youtube.com/@aiDotEngineer/search?query=daniel%20han

Timestamps:

0:00 Introduction to Unsloth and model distribution
2:32 The State of AI: Meter plots and performance trends
20:26 Open Source vs. Closed Source models
38:51 Throughput maxing and accuracy minimizing
1:03:00 Benchmarking and cheating in AI
1:37:49 Kernels and algorithmic improvements
2:04:16 Reinforcement learning primer
2:05:19 Reward hacking and AI agents

Viral Quotes & Pull Quotes:

"If you make the model 86% smaller, it does not get 86% dumber... it only gets 14% less dumb." (29:52)
"Reinforcement learning is terrible, but everything else is even worse." (20:43)
"The model becomes not important anymore; it's the harness or the tool that is actually the most important thing." (38:23)
"If a model can finish a task that takes a human 16 hours, can a model finish that task?" (2:49)

## Using LLMs to Secure Source Code — Eugene Yan, Anthropic

- Upload date: 2026-07-17
- Video: https://www.youtube.com/watch?v=imFedndyXYQ
- Transcript: raw/20260717_imFedndyXYQ/imFedndyXYQ.en-orig.vtt
- Metadata: raw/20260717_imFedndyXYQ/imFedndyXYQ.info.json

Mozilla shipped about 20 security fixes a month across Firefox in early 2025. In April it shipped 400, a 20x jump, and it credited roughly two thirds of them to a frontier model. That is the shift Eugene Yan came to describe: models are now finding and fixing real vulnerabilities at scale. Anthropic's own scan of more than a thousand open source repos surfaced 6,200 high or critical issues out of 23,000 candidates, reported 1,600 to maintainers, and saw about 100 patched upstream. Finding bugs, it turns out, is no longer the hard part. The bottleneck has moved to verifying, triaging, and patching them.

The talk walks a six step workflow through one running example: a five line order lookup with a SQL injection hiding in a Python string. The two setup steps are a threat model and a sandbox. A written threat model alone pushes the true positive rate to 90%, because a model has great context of the code but poor context of the system, all the design decisions that live only in someone's head. The four loop steps read like a machine learning pipeline: discovery optimizes for recall, then a separate verification agent, kept independent and adversarial so it never sees the discovery reasoning, optimizes for precision by detonating the exploit in a fresh container. Triage protects the scarcest resource, engineer attention, and patching closes the loop so the same bug cannot return. His parting advice: start this week on open source dependencies, keep your hands on the wheel before automating, and remember that scanning was never the bottleneck.

Speaker info:
- https://x.com/eugeneyan
- https://github.com/eugeneyan
- https://eugeneyan.com

Timestamps:
0:00 - Working with security teams to find and fix vulnerabilities
0:49 - Three trends in model security capability
1:16 - Cybersecurity benchmarks and the step jump in capability
1:54 - Mozilla's 20x jump in monthly security fixes
2:44 - Log4Shell, Heartbleed, and why this matters
3:22 - Anthropic's scan of a thousand open source repos
3:35 - The bottleneck shifts to verify, triage, and patch
3:48 - Why agentic harnesses changed the game
4:29 - The six step workflow
5:31 - A running example: the order service
5:45 - Step 1: the threat model and 90% true positives
7:42 - Step 2: the sandbox for isolation and reproducibility
9:24 - Step 3: discovery and the five line SQL injection
11:44 - Step 4: independent adversarial verification
13:36 - Step 5: triage and the scarcity of engineer attention
15:52 - Step 6: patching and closing the loop
17:19 - It all looks like a machine learning pipeline
17:43 - The non technical bottlenecks are harder
18:47 - Organizational bottlenecks: routing, severity, bandwidth
20:05 - Three takeaways and how to start this week

"The bottleneck has now shifted to verification, triage, and patching." (3:39)
"A model has great context of the code but poor context of the system." (6:06)
"Things that can be solved with money are not really problems. But human attention doesn't scale." (18:14)
"Scanning was never the bottleneck." (20:38)

## Every company should have a Brain — Garry Tan, Y Combinator

- Upload date: 2026-07-17
- Video: https://www.youtube.com/watch?v=eBUyTS7SzV4
- Transcript: raw/20260717_eBUyTS7SzV4/eBUyTS7SzV4.en-orig.vtt
- Metadata: raw/20260717_eBUyTS7SzV4/eBUyTS7SzV4.info.json

Garry Tan, President of Y Combinator, discusses how the rise of AI-native companies is revolutionizing organizational productivity, allowing lean teams to operate at a scale previously requiring hundreds or thousands of employees (0:52-1:07).

Key Takeaways:

The 400x Leverage: Tan reports a massive increase in output (approximately 400x) by shifting from writing individual lines of code to managing AI agents (2:32-2:35).
Wiring the Work: He emphasizes that founders should treat AI not as a simple autocomplete tool, but as a workforce (3:58). He explains that core organizational components—like roles, processes, and performance reviews—can now be encoded as markdown-based skill files (4:31-5:32).
The AI-Native Organization: Successful startups at Y Combinator are building "company brains" (like his own project, GBrain), which act as a library and librarian, ensuring that agents have access to the right context at the right time (12:54-13:30).
Discipline of Execution: He advises never to perform "one-off" work. Instead, every task should be refined into a reusable skill file to prevent the company from "waking up with amnesia" each day (15:30-16:40).
The New Physics of Business: Tan argues that modern companies can achieve unprecedented revenue-per-head ratios by building on this new infrastructure, effectively "boiling the ocean" by automating formerly impossible tasks (6:40-7:15; 19:55-20:00).

Timestamps:

0:00 Introduction: The AI revolution and YC's transformation
1:25 The 400x productivity jump: Coding in 2013 vs. today
3:38 Wiring the work: Treating AI as a workforce
4:11 The anatomy of an AI-native organization
6:12 Real-world impact: Companies scaling with lean teams
8:38 Latent space vs. deterministic space
10:53 Overcoming human memory limits: AI as a library
12:53 Context engineering: The importance of the 'librarian'
13:28 Building GBrain: Managing institutional knowledge
15:13 The discipline of 'skillifying' your work
16:40 The call to build AI-native companies
18:25 The power of abundance through shipped software


"The 2x people and the 100x people are using the exact same Claude... the leverage is not in the weights, it's in how you wire the work." (3:06)
"When you sit down with Claude Code or Cursor, you're not writing software. You're hiring, training, and managing a workforce made of markdown." (5:58)
"The organization that captures what it learns like this gets smarter every single day. The one that doesn't wakes up every morning with amnesia." (16:26)
"Abundance is not a policy paper. It is shipped software." (18:56)
"Every archive too big to read, every data set too gnarly to clean, every ocean you were told not to boil. We can boil the ocean now." (19:55)

## The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents

- Upload date: 2026-07-17
- Video: https://www.youtube.com/watch?v=c35YoMdnI78
- Transcript: raw/20260717_c35YoMdnI78/c35YoMdnI78.en-orig.vtt
- Metadata: raw/20260717_c35YoMdnI78/c35YoMdnI78.info.json

Oxford Style Debate: There is, or is not, a delta between the hype behind loops and what actually works in practice.

Team No Delta (pro the way we do loops today)

The hype around loops is valid and loops work well today in practice. Loops today can be a silver bullet and result in outsize productivity gains, and marks an important step up the autonomy curve towards real software factories.

Ian Livingstone
Geoff Huntley

Team Delta (anti the way we do loops today)

There is a delta between the hype behind loops and what actually works in practice. The way we are doing loops today is wrong. Loops are not a silver bullet and there is no magic.

The hype is outrunning the discipline
"Stop writing loops, start writing control loops." A bare repeat-the-agent loop isn't magic. The leverage comes from the Kubernetes-style reconciliation around it: read current state → read desired state → one incremental change  → repeat. Dex's tell when shown a fake loop: "where's the recur condition?" (Jun 21)
A software factory can run the mechanical, spec-gated, test-covered slices unattended; it cannot autonomously decide whether it built the right thing.

Dex Horthy
Greg Pstrucha

Main Debate 
Loop History - Why now as the inflection point and not some of the earlier ones? 
Loop Anatomy - What makes a good loop? 
Loop Future - Given what we’re seeing with loop usage now, are we well positioned for software factories? If we can’t use loops well today how do we expect to operate software factories?

Appendix
Research
https://x.com/AnatoliKopadze/status/2068328135611822149?s=20
https://x.com/ericzakariasson/status/2070493377267646797?s=20
https://x.com/MilksandMatcha/status/2069838072515281386?s=20
https://x.com/AnatoliKopadze/status/2070156017262793008?s=20
https://ghuntley.com/loop/
https://ghuntley.com/ralph/
https://www.anthropic.com/institute/recursive-self-improvement
Anthropic's Absorption of the Ralph Loop
Verifying Agents in GitHub


0:00 Introduction and format explanation
0:43 Introduction of the debaters
4:05 Team No Delta (Ian & Jeff) opening arguments
6:53 Team Delta (Dex & Greg) opening arguments
10:28 Rebuttal and initial stance
15:32 Main Debate: Loop History and Inflection Points
16:20 Security, alignment, and goal-seeking agents
19:24 Why loops became more usable today
24:40 Context rot and context engineering
27:10 Loop Anatomy: What makes a good loop?
30:30 Preventing agent cheating and verification
32:23 Convergence engineering and loop slop
36:13 Economic viability and token spend
39:07 Multiplayer agents and shared memory access
43:21 The "just write loops" advice critique
46:36 Scaling, autonomy, and pragmatism
52:31 Closing statements and final thoughts
Viral Quotes & Pull Quotes:

(16:55) "As these models get better, the most important thing to remember is they actually become higher goal-seeking and higher capable in terms of finding exploits to achieve their ultimate goal."
(20:25) "These LLMs generate code better than you can actually hire for. It's sad but true."
(22:38) "The models are drunk, right? You can't trust them. But like, we accept that. We engineer away those failure domains."
(36:31) "I don't think they fail quietly. I think they fail very loudly, especially when you're looking at your bills."
(46:58) "Don't throw away all the things we've learned. Don't go out of your way to cast aside this decades-long career of software engineering that we as a community have built up."

## On AI and Knowledge — Pablo Castro, Distinguished Engineer & CVP for AI Knowledge, Microsoft

- Upload date: 2026-07-17
- Video: https://www.youtube.com/watch?v=RGSFUqzqErE
- Transcript: raw/20260717_RGSFUqzqErE/RGSFUqzqErE.en-orig.vtt
- Metadata: raw/20260717_RGSFUqzqErE/RGSFUqzqErE.info.json

Pablo Castro explores AI and knowledge systems for building better applications and agents.

Speaker:
Pablo Castro —Distinguished Engineer and CVP, Microsoft, leads the AI Knowledge team in Microsoft's CoreAI division, where he focuses on state-of-the-art information understanding and retrieval systems for AI applications and agents, including Foundry IQ, Azure AI Search, and Azure Content Understanding.

LinkedIn: https://www.linkedin.com/in/pabloc

Timestamps:

0:00 Introduction and speaker background
1:14 Defining the nature of knowledge: Intrinsic, Extrinsic, and Learned
1:27 Intrinsic knowledge and the history of AI coding tools
4:38 Extrinsic knowledge and corporate data grounding
7:06 Evolution of retrieval systems and Foundry IQ
9:56 Foundry IQ demo: Building a knowledge base
13:08 Learned knowledge: The agent learning loop
14:25 Foundry agent optimization demo
16:49 Closing remarks and resources


Key quotes 

Intrinsic Knowledge
Perspective: This knowledge represents the foundational parametric memory of models.
"Intrinsic knowledge is just the knowledge that comes with the models... it's what started many of the scenarios that then grew on all the things we're doing with agents today." (1:27 - 1:48)
"I would argue that GitHub Copilot and ChatGPT, those sort of experiences, were heavily grounded on this intrinsic memory—what the models already knew." (2:59 - 3:04)
Extrinsic Knowledge
Perspective: To be truly useful in an organization, agents must access private, ambient data through sophisticated retrieval.
"Intrinsic model got us here, but it only gets you so far if you're building a system that or an agent that needs to participate in what's happening in an organization." (4:41 - 4:49)
"The trick is how do you build a platform that allows you to combine all these building blocks without putting the complexity right in front of you." (8:02 - 8:10)
"For more sophisticated cases you do want a system that can reflect on what's in the data set and decide whether or not we've satisfied the information need." (9:09 - 9:18)
Learned Knowledge & Future Predictions
Perspective: Knowledge is compounded by observing processes and enabling agents to self-optimize.
"The idea that we can actually observe the processes and get better at them by reflecting and improving every step of it is something that is really changed now." (13:20 - 13:29)
"Satya wrote about this recently and reflected on the fact that people and agents can really compound in how they do the work and how they can create this learning loop." (13:35 - 13:43)
"This is a real learning loop materialized in practice... we can enable this learning loops that will capture this differentiated capability that lives in each one of the companies and organizations we work on." (16:40 - 17:03)

## "Software engineering is not about writing code" — Benoit Schillings, Google DeepMind VP of Research

- Upload date: 2026-07-17
- Video: https://www.youtube.com/watch?v=1P1hJ36rxM0
- Transcript: raw/20260717_1P1hJ36rxM0/1P1hJ36rxM0.en-orig.vtt
- Metadata: raw/20260717_1P1hJ36rxM0/1P1hJ36rxM0.info.json

A keynote exploring generative AI for code, deep-thinking algorithms, and the future of pre-training and transformer models for Gemini.

Speaker:

Benoit Schillings leads the Thinking, Reasoning, and Coding teams at Google DeepMind, directing foundational research toward AGI. His work focuses on advancing next-generation model reasoning and integrating software development best practices into AI code generation. Previously, as CTO at X, Benoit guided early-stage teams prototyping Alphabet's moonshot technologies across computing, biochemistry, and clean energy.

LinkedIn: https://www.linkedin.com/in/benoit-schillings-2942a5

Timestamps:

0:00 Introduction and speaker background
2:35 The origin story of the Pitchfork project
4:43 Historical eras of software development
7:08 The current state of AI code generation
9:36 The role of self-play in training models
11:13 Changing economics of software engineering
12:41 Implementing guardrails and security
13:48 Inductive architecture and model planning
14:36 Evolution of evaluation benchmarks
15:45 Moving beyond simple chain-of-thought tokens
17:51 Future applications in chemistry and biology



Key Takeaways from the talk:

Benoit Schillings, VP of Technology at Google DeepMind, discusses the transformative impact of generative AI on software engineering and the future of model reasoning (0:49 - 2:35).
The Era of Syntax Generation is Over: (4:43) Coding has shifted from a machine-constrained task to an AI frontier where syntax is effectively solved, moving the bottleneck to architecture and validation.
The Power of Self-Play: (9:36) As human-generated training data reaches saturation, DeepMind is utilizing self-play, where models generate and verify their own challenges to reach superhuman performance.
Shift in Engineering Economics: (11:13) With writing code becoming nearly free, the focus must transition to active guardrails, security, and managing the explosion of generated code.
Inductive Architecture: (13:48) The next step for AI is moving beyond simple token prediction toward models that can plan, decompose complex problems, and transfer knowledge across domains.
Scientific Breakthroughs: (17:51) AI's ability to experiment rapidly will transform fields like chemistry and biology, allowing models to uncover patterns and relationships that remain invisible to human perception.

## How Autoresearch is changing ML research — Zhengyao Jiang, Weco

- Upload date: 2026-07-16
- Video: https://www.youtube.com/watch?v=iCj_ATyThvc
- Transcript: raw/20260716_iCj_ATyThvc/iCj_ATyThvc.en-orig.vtt
- Metadata: raw/20260716_iCj_ATyThvc/iCj_ATyThvc.info.json

Earlier this year, OpenAI ran Parameter Golf, a model-training competition that doubled as a hiring filter. Over 1,000 researchers competed to train the best small language model under a 16MB cap. The top contributor was the one candidate OpenAI couldn't hire. Our autonomous research agent Aiden finished with 7 merged records, more than twice as many as any other contributor, and ended up the most-cited participant in the community.
This talk is about what those 22 days showed. I'll cover on high level how does it works and which of its ideas produced the records. But the part worth more than the leaderboard is the collaboration itself, the community and AI agent building on each other's work, the largest natural experiment in human-AI collaboration I've seen run in public. I'll close with what it tells us about where humans and autonomous research each still matter for the foreseeable future.
1:57 PM

# An AI Agent Became the #1 Contributor in OpenAI's Hiring Challenge

**Location:** Main Stage
**When:** Day 3 - July 1, 2026 · 1:55pm-2:15pm

## Speakers

### Zhengyao Jiang
CEO & Cofounder · Weco AI
[X/Twitter](https://x.com/zhengyaojiang) · [LinkedIn](https://www.linkedin.com/in/zhengyao-jiang-387b44145/) · [Website](https://zhengyaojiang.github.io/)

Cofounder & CEO @WecoAI - automated hill climbing with LLMs. Previously: PhD in ML at UCL

Timestamps

0:00 Introduction to Parameter Golf and the Aiden agent
1:06 Defining the challenge: Auto-research vs. human community
1:47 About Weco AI and the development of Aiden
3:07 Evaluating Aiden's impact and H-index in the community
4:01 Why autonomous AI is powerful: Throughput and efficiency
5:21 Human-AI collaboration: How ideas move the frontier
6:32 Case study: Combining research, architecture, and tokenization
7:41 Summary of auto-research strengths: Execution and search
9:06 The role of human design in competition
10:04 The Andrej Karpathy metaphor: Gradient descent and coding
11:19 Auto-research as training a model: Evals and abstractions
13:36 Case study: Improving data pipelines via strict API abstractions
14:38 Conclusion: The new craft of the AI engineer

## Imagination Engineering: "Live in the future and then build what's missing."

- Upload date: 2026-07-16
- Video: https://www.youtube.com/watch?v=Z2Erdirpudo
- Transcript: raw/20260716_Z2Erdirpudo/Z2Erdirpudo.en-orig.vtt
- Metadata: raw/20260716_Z2Erdirpudo/Z2Erdirpudo.info.json

Eve Bouffard from Y Combinator explores the concept of "Imagination Engineering"—the idea that with increasingly powerful AI models, the primary challenge for humans is no longer technical execution, but the ability to dream up bold, innovative ideas (0:13-0:59).

Key themes and experiments shared:

Thinking in Public: Inspired by Paul Graham, Eve describes an experiment where she shared her stream of consciousness in a dedicated Slack channel (Eve thoughts). She then used AI to aggregate these raw thoughts into a personal, interactive website (1:35-4:26).

Software on Demand: Eve demonstrates how she uses AI to build custom tools on the fly, such as an interactive "Shape of Minds" visualizer to study commonalities among historical geniuses (8:49-10:44) and a personalized emoji-picker for company communication (12:57-13:46).

Expanding the Mind: She argues that current AI tools function like a "rocket ship for the mind," allowing individuals to learn at unprecedented speeds by requesting summarized reports on complex topics like design principles or historical patronage (13:53-14:48).

Eve emphasizes that we are in a historical period similar to the Library of Alexandria, where the focus should be on consolidating and creating knowledge for humanity (1:01-1:23).

Detailed Timestamps
0:00 - Introduction to the concept of Imagination Engineering
1:01 - The analogy of the modern Library of Alexandria
1:35 - The "Thinking in Public" experiment (Eve Thoughts)
2:58 - The influence of Paul Graham and Y Combinator culture
4:23 - Demo: The efar.com personal AI-generated website
6:05 - Integrating design tools and shaders into workflows
8:49 - The "Shape of Minds" project: Mapping historical geniuses
12:57 - Using custom AI tools for daily productivity (Emoji picker)
13:46 - AI as a tool for rapid learning and research
15:08 - The evolution of development logs and software backlogs


"The new bottleneck will be to come up with crazy ideas because it's going to be really easy to one-shot absolutely everything." (0:38)
"Live in the future and then build what's missing." (5:15)
"With these insanely capable models, it's like a rocket ship for the mind; it's no longer a bicycle." (5:35)
"Whatever stream of consciousness you have, you should just ask an agent to do it for you." (12:26)



## Speakers

### Eve Bouffard
Head of Design · Y Combinator
[X/Twitter](https://x.com/eve_bouff) · [LinkedIn](https://www.linkedin.com/in/eve-bouffard) · [Website](https://evebouffard.com)

Eve is Head of Design at Y Combinator. She joined YC as the youngest member of the admissions team, where she read more than 25,000 startup applications before teaching herself to code and moving into engineering. These days, she works across design and software, building the products founders use and the internal tools that help YC partners support thousands of startups every year. She believes great design isn't what looks best, but what best achieves a given goal. She's happiest building products that make it easier for founders to take a leap, bet on themselves, and make something people want.

## Claude Fable, Claude Tag, and Anthropic's Culture — Cat Wu & Thariq Shihipar ft Simon Willison

- Upload date: 2026-07-15
- Video: https://www.youtube.com/watch?v=uU5Gv2h8-9g
- Transcript: raw/20260715_uU5Gv2h8-9g/uU5Gv2h8-9g.en-orig.vtt
- Metadata: raw/20260715_uU5Gv2h8-9g/uU5Gv2h8-9g.info.json

A long form Q&A with Cat Wu (Head of Product, Claude Code) and Thariq Shihipar (Engineer, Claude Code) from Anthropic, moderated by Simon Willison. The discussion focuses on the evolution of coding agents and how they have fundamentally shifted software development practices.

Key Takeaways:
Changing Developer Workflow (1:22 - 3:51): Coding agents like Claude Code have moved developers from manual, low-level implementation toward higher-level product strategy. The focus has shifted from writing every line of code to managing and refining outputs from increasingly capable models.
The Rise of Proactive Agents (6:37 - 9:00): The introduction of Claude Tag marks a shift toward multiplayer, proactive agentic workflows in tools like Slack. It can monitor bugs, draft PRs, and retain team memory, currently landing over 65% of product PRs for the Anthropic team.
Rethinking Software Engineering Norms (3:51 - 6:37): The speakers argue that traditional practices, such as avoiding rewrites or long-term waterfall planning, are becoming outdated. They emphasize the value of product sense, prototyping, and rapid iteration using high-quality test suites.
Safety and Trust (30:57 - 37:53): A major portion of the discussion covers Auto Mode and safety. Anthropic has heavily invested in evals and red-teaming to mitigate risks like prompt injection and data exfiltration, making it the recommended way to handle long-running agentic tasks safely.
Cultural Impact (38:13 - 41:50): The team encourages developers to be more ambitious and stop "negotiating against themselves." They suggest that because implementation is now cheaper, teams should focus on building the "bigger things" they previously thought were impossible or too resource-intensive.
Future Outlook:
Looking ahead, the speakers are excited about models becoming better interaction design partners (44:28) and continuing to bridge the gap between abstract ideas and production-ready software.

## Speakers

### Cat Wu
Head of Product, Claude Code · Anthropic
https://x.com/_catwu

Cat Wu is Head of Product for Claude Code at Anthropic, working on Claude Code and related agentic developer-product workflows. Her background spans product, engineering, and investing.

### Thariq Shihipar
Claude Code · Anthropic
https://x.com/trq212

Engineer and serial entrepreneur currently working on Claude Code at Anthropic. Previously founded One More Multiverse, co-founded Pubpub.org, and co-founded Chime.

### Simon Willison
Independent · Datasette
https://x.com/simonw

Simon Willison is the creator of Datasette, co-creator of Django, and an independent open-source developer and writer focused on LLMs, prompt injection, SQLite, and tools for data journalism.

Timestamps
0:00 Introductions and Claude Code overview
1:22 How coding agents have changed daily workflows
3:51 Shifting focus: Product sense over manual implementation
5:09 Why modern rewrites are now beneficial
6:37 Introducing Claude Tag and team collaboration
11:38 Prioritization and internal "dog-fooding" culture
13:06 The surprise success of remote control features
14:17 Evolving code review processes and automation
17:16 Building trust in new model generations
19:18 Optimizing for capability and user experience
21:23 Reducing system prompts for frontier models
28:05 The philosophy of tool design
30:57 Safety, security, and using Auto Mode
37:53 The human element and developer ambition
41:50 Surprising use cases for Claude (e.g., video editing)
43:35 Limitations and future design aspirations
45:09 Cultural hacks for productivity
46:42 Absurd, fun projects built with Claude
49:03 Audience Q&A

## Recursive Model Improvement — Lee Robinson, Cursor, SpaceXAI

- Upload date: 2026-07-15
- Video: https://www.youtube.com/watch?v=q4Tr-DknG2M
- Transcript: raw/20260715_q4Tr-DknG2M/q4Tr-DknG2M.en-orig.vtt
- Metadata: raw/20260715_q4Tr-DknG2M/q4Tr-DknG2M.info.json

Lee Robinson discusses the future of Cursor and AI-native software development.

Speaker:
Lee Robinson — ML, Model Behavior, Cursor

Model research and personality at Cursor. Previously Vercel.

X: https://x.com/leerob
LinkedIn: https://www.linkedin.com/in/leeerob/
GitHub: https://github.com/leerob
Website: https://leerob.com

Timestamps

0:37 - Introduction and recursive model improvement overview
1:55 - The two-loop training framework (inner and outer loops)
2:33 - Progress and success of Composer 2.5
4:31 - Improving the outer loop with user feedback
5:40 - Climbing the inner loop with high-quality evals
6:52 - Solving reward hacking in public benchmarks
8:27 - Scaling training with ambitious problems
9:53 - New learning methods: Teacher-student textual feedback
11:34 - Scaling compute infrastructure with SpaceX and Colossus
13:06 - Understanding compute allocation in model training
15:28 - Agent-based automation and research efficiency
18:30 - The recursive future: Models training models

## Computer-Use 2.0: Agents Just Got Multi-Cursor — Francesco Bonacci, Cua

- Upload date: 2026-07-15
- Video: https://www.youtube.com/watch?v=ZSQb5fzRFPw
- Transcript: raw/20260715_ZSQb5fzRFPw/ZSQb5fzRFPw.en-orig.vtt
- Metadata: raw/20260715_ZSQb5fzRFPw/ZSQb5fzRFPw.info.json

Three agents click, type, and scroll through three different apps on one desktop at the same time, and the user's own mouse and keyboard never move. That's the live demo behind cua driver, a tool the team built in a single weekend after Codex shipped its own computer use model. Instead of taking over the hardware cursor, it talks straight to the accessibility layer underneath the operating system: UI Automation on Windows, AT SPI on Linux, AX on macOS. Those undocumented APIs let a click land on a background window or a keystroke reach a hidden one, so any number of agents can act without stealing focus from each other or from the human sitting at the machine.

To know whether any of this can be trusted, the team built CUABench: over 130 verifiable tasks across 42 environments and five platforms, each one attacked by a matrix of agents trying to reward hack it before it's allowed into the dataset. Swapping a standard computer tool for cua driver pushed pass rate on a 4K benchmark from 62% to 80% while using 34% fewer tokens, mostly because it watches one window instead of the whole screen. The newest addition, built with Snorkel AI on real circuit design software, humbled every model tested: the best agent fully passed only 6 of 25 electrical engineering tasks, every one of them an edit to an existing schematic, and starting from a blank schematic dropped every model straight to 0%.

Speaker info:
- https://www.linkedin.com/in/francesco-bonacci-70428a121/

Timestamps
0:00 - Introduction and Vision of Cua
2:40 - Overview of Cua Driver and Background Operation
6:34 - Introduction to Cua Bench and Agent Evaluation
10:50 - Cua Fleet and GPU Infrastructure Optimization
15:08 - Q&A Session
15:44 - Discussion on Mobile and Android Support

## "The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani

- Upload date: 2026-07-14
- Video: https://www.youtube.com/watch?v=n97BCfyFIvw
- Transcript: raw/20260714_n97BCfyFIvw/n97BCfyFIvw.en-orig.vtt
- Metadata: raw/20260714_n97BCfyFIvw/n97BCfyFIvw.info.json

For his closing keynote, Addy Osmani explores the evolving role of software engineers in the age of AI agents. He argues that as coding tasks become increasingly automated, the true value of an engineer shifts from mere code production to accountability, judgment, and system ownership.

https://addyosmani.com/
https://x.com/addyosmani/status/2074927530482835916

Timestamps

0:00 Introduction and the human side of engineering
1:46 Rebundling roles and ownership of systems
2:34 Harnesses, loop engineering, and software factories
3:34 The shift to answerability as an engineering requirement
4:26 Reviewing AI-assisted code and organizational bottlenecks
5:55 Redefining leverage through human judgment
6:15 Alpha, decay, and the role of "taste"
8:49 Defining the modern software engineer
9:50 Risks to avoid: cognitive debt and surrender
11:51 Orchestration tax and system design
12:39 Accountability as the foundation for scaling
13:16 Career math: credibility vs. capability
14:13 High agency and the decision-making ladder
15:13 Defining the boundary between agents and humans
16:13 Operational rule: explain it or don't ship it
17:20 Future outlook: unlocking latent demand

## Forward Deployed Engineering at Cursor — Pauline Brunet

- Upload date: 2026-07-14
- Video: https://www.youtube.com/watch?v=APqXGyCoGW4
- Transcript: raw/20260714_APqXGyCoGW4/APqXGyCoGW4.en-orig.vtt
- Metadata: raw/20260714_APqXGyCoGW4/APqXGyCoGW4.info.json

The first question at Cursor is not how to deploy a forward deployed engineer, it is whether to. If a customer's teams are already mature in their transformation and can self serve on an AI coding platform, sending a 10x engineer to sit with them is a waste. Pauline Brunet's frame is to read where the customer actually is: the forward deployed engineer earns their place where teams cannot hire or staff the talent, need an advisor, and want a real outcome rather than a demo. On the ground that means working with VPs of engineering, understanding how they operate today, and driving a strict, measurable return on investment as the tip of the spear.

The other half is who you send and how you scope it. Cursor hires what she calls unicorns by splitting the role: one person who is the deep industry expert, another with the aptitude to learn fast, often pulled from the system integrators and consultants who already know change management. Engagements stay short, roughly six week cycles that co design the solution with the customer, check honestly whether you are close, and pivot on the learnings instead of grinding on a symptom. The discipline is scope: solve the problem the buyer actually cares about, prove the return, and stay honest about where the product really is.

Speaker info:
- https://www.linkedin.com/in/pauline-brunet/

Timestamps:
0:00 - Introduction: forward deployed at Cursor
1:52 - When NOT to send a forward deployed engineer
4:00 - Where the forward deployed engineer fits
5:31 - What the job actually entails
7:50 - The economic buyer and a strict ROI
9:43 - Scope discipline: knowing what you can't solve
11:22 - Hiring unicorns by splitting the role
14:06 - Who to hire, and being an honest partner
16:41 - Six week engagements and scope
18:14 - Pivoting on the learnings
19:55 - Wrap up: build trust

## WTF Is the Context Layer? The Missing Infrastructure for Production Agents — Prukalpa Sankar

- Upload date: 2026-07-14
- Video: https://www.youtube.com/watch?v=8G_1-3IO4ZQ
- Transcript: raw/20260714_8G_1-3IO4ZQ/8G_1-3IO4ZQ.en-orig.vtt
- Metadata: raw/20260714_8G_1-3IO4ZQ/8G_1-3IO4ZQ.info.json

In the last two years, models have gotten exponentially smarter. Two years ago they couldn't pass the bar. Today, top 1% of test scorers. And yet most agents still can't answer a simple business question correctly. You ship a demo that works. You deploy it. The business abandons it in a month.

The missing variable is context: the business definitions, procedural knowledge, and operational norms that make a human expert valuable.

Drawing on hundreds of production deployments, Prukalpa Sankar will break down what it actually takes to give agents contextual intelligence — and get them past the demo stage.

She'll walk through the architecture of a context layer: how context repos work (versioned, testable, portable), how simulation environments catch failures before deployment, how agent traces compound back into shared context, and why context engineering scales where fine-tuning and prompting don't. She'll also cover why your context needs to be open (MCP, Iceberg, deploy to any framework) — and what happens when it isn't.

### Prukalpa Sankar
Founder & Co-CEO · Atlan
[X/Twitter](https://x.com/prukalpa) · [LinkedIn](https://www.linkedin.com/in/prukalpa)

Prukalpa Sankar is the Founder & Co-CEO of Atlan, the context layer for AI. She's been early to a defining idea of the AI era: context is king. AI systems are only as good as the business context behind the data they rely on. Under her leadership, Atlan has become a Leader in the Gartner Magic Quadrants for both Data & Analytics and Metadata Management, serves 300+ enterprises including Mastercard, GM, JPMorgan Chase, and Nasdaq, and has raised $200M+ from Sequoia, GIC, and Salesforce Ventures. Before Atlan, Prukalpa co-founded SocialCops, the world's largest government data lake powering the UN's SDG monitoring — recognized by the New York Times and the World Economic Forum. She's been featured in Forbes 30 Under 30 and Fortune 40 Under 40.

Timestamps

* **0:12** Introduction: The Context Moment
* **1:51** Why AI Agents Struggle with Business Context
* **3:19** Performance = Intelligence + Context
* **4:27** The Human Learning Model: Lessons from Maya
* **7:20** Evolution of Agent Architecture at *Atlan*
* **10:00** The Challenges of Isolated Agent Systems
* **11:06** Transitioning to General Purpose Agents
* **12:43** Marketing Team Case Study: The Context Layer
* **14:36** The Challenges of Context Engineering
* **15:31** Defining the Context Layer: The GitHub for Context
* **16:43** Compounding Learning Loops and Traces
* **17:18** How to Start Building Your Company Brain
* **18:07** Defining the Context Layer Architecture
* **19:31** Conclusion: Context is IP

## Don't Ship Skills Without Evals — Philipp Schmid, Google DeepMind

- Upload date: 2026-07-14
- Video: https://www.youtube.com/watch?v=0vphxNt4wyk
- Transcript: raw/20260714_0vphxNt4wyk/0vphxNt4wyk.en-orig.vtt
- Metadata: raw/20260714_0vphxNt4wyk/0vphxNt4wyk.info.json

There are thousands of agent skills. Almost none of them are tested. They get vibe-checked with two manual runs, maybe a thumbs-up from a colleague, then shipped. You wouldn't merge code without tests — so why are we shipping skills without evals? This talk covers the full lifecycle of building reliable agent skills: what a skill actually is (and isn't), how to write one that triggers correctly, and how to build a lightweight eval harness that catches failures before your users do.

### Philipp Schmid
Staff Engineer · Google DeepMind
[X/Twitter](https://x.com/_philschmid) · [LinkedIn](https://www.linkedin.com/in/philipp-schmid-a6a2bb196/) · [Website](https://www.philschmid.de/) · [Blog](https://www.philschmid.de)

Philipp Schmid is a Staff Engineer at Google DeepMind working on Gemini and Gemma. His work focuses on helping developers build and benefit from AI responsibly.

Timeline:

0:00 Introduction: Why skills need evals
0:25 The problem with current agent workflows
1:25 Agents we use vs. agents we build
2:28 Defining a 'Skill' and progressive disclosure
3:08 Capability skills vs. preference skills
4:17 Do skills actually work? (Skillsbench data)
5:39 Model-triggered vs. user-invoked skills
6:39 Best practices for writing skill descriptions
8:30 Structuring complex, multi-layered skills
9:04 Defining goals and constraints (avoiding rigid steps)
9:56 Don't skip negative cases
10:36 Testing strategy: Evals and regressions
11:05 Removing 'no-ops' for cost efficiency
11:47 Knowing when to retire a skill
12:22 Practical example: Gemini interactions API
13:36 Building a lightweight eval harness
14:35 Using regex and LLMs as judges
17:14 Top 10 best practices summary
20:20 Homework: How to start testing your skills
Viral Pull Quotes:

(0:22) "You wouldn't merge code without tests—so why are we shipping skills without evals?"
(1:13) "Agents are really nondeterministic. You might not know if your task fails because your skill is bad or if your task fails because it's way too challenging for the model."
(9:15) "If the process or the workflow is always the same, you should not use skills. Maybe you should write a script."
(11:53) "Skills are not there to live forever. Models get better, behaviors change, environments change."

## Modern Post-Training: A Deep Dive  — Will Brown, Prime Intellect

- Upload date: 2026-07-13
- Video: https://www.youtube.com/watch?v=V-EDrhIhHzQ
- Transcript: raw/20260713_V-EDrhIhHzQ/V-EDrhIhHzQ.en-orig.vtt
- Metadata: raw/20260713_V-EDrhIhHzQ/V-EDrhIhHzQ.info.json

Deep dive into Prime Intellect's open-source ecosystem of post-training tools, including the verifiers and prime-rl libraries, as well as the Lab platform for self-serve training and inference.

Speaker:
Will Brown — Research Lead, Prime Intellect

Will Brown leads Applied Research at Prime Intellect and builds open research infrastructure to enable every company to train, deploy, and self-improve their own frontier agentic models. He holds a PhD in Computer Science from Columbia University.

X: https://x.com/willccbb
LinkedIn: https://www.linkedin.com/in/willcb/
GitHub: https://github.com/willccbb
Website: https://willcb.com

TImestamps
0:00 Introduction and Overview of Prime Intellect
4:20 Defining the Environment in Post-Training
9:33 Decomposing Environments: Tasks, Harnesses, and Runtimes
12:46 Verifiers V1: The New Modular Pattern
17:46 Rewards, Metrics, and Group-Level Rewards
20:25 Tooling, User Simulators, and MCP Integration
22:00 The Interception Server Pattern
24:13 Trace Graphs and Handling Tokenization
25:35 The Renderers Library for Chat Templates
29:20 Primaril: Asynchronous Reinforcement Learning
38:02 Customizing Training Algorithms and Losses
42:35 The Lab Platform and Hosted Training

## From fork() to Fleet: Designing an Agent Sandbox Cloud — Abhishek Bhardwaj, OpenAI

- Upload date: 2026-07-13
- Video: https://www.youtube.com/watch?v=OqM67QG_Ikk
- Transcript: raw/20260713_OqM67QG_Ikk/OqM67QG_Ikk.en-orig.vtt
- Metadata: raw/20260713_OqM67QG_Ikk/OqM67QG_Ikk.info.json

Sandboxes unleash agents by giving them secure, fully functional computers where they can tackle diverse tasks with minimal setup. This talk explores the architectural challenges of building an agent sandbox cloud. We compare runtime isolation technologies and their trade-offs, examine persistence and storage as the next major unlock for agent capabilities, and discuss the key decisions involved in orchestrating and scaling sandboxes.

Abhishek Bhardwaj works on Agent and Reinforcement Learning Infrastructure at OpenAI. He builds systems that enable large-scale model training in RL environments, as well as secure and scalable cloud sandboxes for OpenAI’s agents. Before joining OpenAI, he created Arrakis, an open-source sandbox for AI agents. Previously, he worked at Google on ChromeOS and foundational microVM technologies, and at Replit on core infrastructure and early versions of Replit Agent.

Timestamps
0:00 Introduction and motivation for AI agent sandboxes
1:31 Why AI models need tools and execution environments
3:51 Product-side challenges: Security and the need for sandboxing
6:44 Comparing research vs. product sandbox requirements
8:24 Overview of the three pillars: Runtime, Persistence, and Orchestration
9:05 First principles of Linux execution: System calls and security vectors
11:15 Evaluating fork() and exec models
12:06 Understanding containers: Namespaces and cgroups
16:26 GVisor as an application kernel alternative
18:29 Hardware-level virtualization (Virtual Machines)
20:34 How VMMs (Virtual Machine Monitors) work with KVM
23:16 Evolution of modern VMMs and Rust-based safety
24:32 What defines a "microVM"?
25:43 Orchestrating microVMs via APIs
27:16 Trade-offs of microVMs (performance vs. security)
30:05 The need for persistent storage in agent sandboxes
31:40 Use cases for persistence: Reliability, long-running tasks, and research
34:36 Design choices for disk snapshotting
36:03 First principles of Linux block storage and file systems
37:25 Implementing always-on vs. explicit persistence
41:20 Scaling and orchestrating sandboxes at fleet level

## Stop Evaluating Models Like It's the 50s - Alejandro Vidal, Mindmakers

- Upload date: 2026-07-13
- Video: https://www.youtube.com/watch?v=O3FEoMYvUf8
- Transcript: raw/20260713_O3FEoMYvUf8/O3FEoMYvUf8.en-orig.vtt
- Metadata: raw/20260713_O3FEoMYvUf8/O3FEoMYvUf8.info.json

Psychologists spent the last century learning how to measure something invisible and uncooperative: a human mind. AI evaluation, meanwhile, still scores like it is 1950. Count the right answers, treat every question as equal, trust the percentage (this is Classical Test Theory). We are sitting on decades of measurement theory built for exactly this problem, and we forgot to use it.

Borrow it and the picture changes. Item Response Theory (or IRT, the math behind the SAT and the GRE) models every item on top of a shared scale with real error bars. That tells you which of your test items are pure noise, which are optimal, and where the knowledge gaps and unexpected behaviours are. Adaptive testing then measures the same ability with a fraction of the questions, which means private, rotating benchmarks that resist contamination instead of saturating in a month (tinyBenchmarks already hinted you can shrink a benchmark with IRT).

It goes further than scoring. The statistical properties of how a model fits the test reveal something a single number never could: data leakage, the moment an agent has quietly seen the answers before. The same machinery that catches a cheating student catches a contaminated benchmark. And instead of one flat score, you get a shape: where the jagged frontier actually is, which abilities are solid and which are luck, so you know which direction to push next.

You will leave this talk with a way to build evals that are cheaper, harder to game, and that tell you what your model actually learned instead of how lucky it got. This is not about handing human tests to a model. It is about borrowing a century of how to measure a mind that does not want to be measured.

Speakers:
- Alejandro Vidal (Mindmakers): Alex Vidal is the founder of Mindmakers, a psychologist and computer scientist who teaches humans to use AI and teaches AIs to teach humans, building adaptive learning technology and the agents, evals and boring infrastructure that keep it from falling over.

X/Twitter: https://x.com/dobleio

## "I've never seen anything scarier than an LLM with tool calls." — Erik Meijer aka @HeadinTheBox

- Upload date: 2026-07-13
- Video: https://www.youtube.com/watch?v=-CnA2lGfymY
- Transcript: raw/20260713_-CnA2lGfymY/-CnA2lGfymY.en-orig.vtt
- Metadata: raw/20260713_-CnA2lGfymY/-CnA2lGfymY.info.json

AI agents today execute on blind trust, and the failure modes are already in the headlines: a dealership chatbot agreeing to sell a $76,000 Chevy Tahoe for $1, a coding agent wiping a production database during a code freeze, an "agent skill" quietly installing a keylogger on a developer's machine. 

These are not edge cases. They are the predictable consequence of allowing agents to act without any mechanical guarantee of correctness or safety. Execution is irreversible. You cannot unsend a message, unwire a payment, or un-delete a database. In that regime, permitting an unsafe action costs far more than withholding a safe one, and thus the economically rational choice is to refuse to let agents act on unchecked intent alone. 

Automind is an agent harness that enforces this discipline by construction. Before any action runs, the agent must submit its execution plan together with a machine-checkable proof of safety and correctness, written in Universalis, a literate logic programming language designed to be read by humans and verified by machines. A small, auditable checker decides whether the plan is allowed to execute. By left-shifting the trust boundary, we no longer have to trust the agent's proposal, or even its proof; only the checker. Policy compliance becomes a static property, established before the first side effect. We can finally demand formal proofs, not vibes, from the agents we deploy.

More about Erik: https://x.com/headinthebox
and automind: https://spawn-queue.acm.org/doi/pdf/10.1145/3676287

Erik Meijer has spent more than three decades designing programming languages and developer tools that help humans express intent more clearly to machines. His work has influenced languages and technologies including Haskell, Mondrian, Cω, C#, Visual Basic, Dart, Hack, LINQ, and Rx. Today, he is building Universalis, the world's first programming language for AI agents. By combining formal verification with large language models, Universalis aims to make agentic systems safe, transparent, and trustworthy enough for real-world knowledge work.

Timestamps

0:00 Introduction and purpose of the talk
1:54 The inherent dangers of AI and accidental file deletion
3:39 The history and impact of LLMs (the "Pandora's box")
5:36 The problem of prompt injection and model safety
7:03 Formal verification and using Lean for safety proofs
10:45 The introduction of tool calls and the leap into chaos
13:59 The "lethal trifecta" of AI risks
14:13 The proposed solution: "air-gapping" the agentic loop
16:36 Refying plans into programs and using Free Monads
19:17 The concept of proof-carrying code and summary

## The Agentic Web and the Bazaar Era of AI - Ramesh Raskar, MIT Media Lab

- Upload date: 2026-07-12
- Video: https://www.youtube.com/watch?v=sum9DgexFRQ
- Transcript: raw/20260712_sum9DgexFRQ/sum9DgexFRQ.en-orig.vtt
- Metadata: raw/20260712_sum9DgexFRQ/sum9DgexFRQ.info.json

The AI agent industry is currently focused on memory, orchestration, enterprise deployment, and tooling. But these are the first steps toward a larger transformation: the emergence of the Agentic Web.

Today’s ecosystem resembles the early days of AOL: closed platforms, proprietary agent stores, and siloed orchestration layers. The next era of AI agents will require open infrastructure that allows agents to discover, transact, and co-learn across organizational boundaries.

This talk explores three layers of the Agentic Web.

First, the Discovery Layer: agents will require discovery infrastructure analogous to AltaVista or Google—but for agents instead of webpages. The challenge is no longer PageRank, but “AgentRank”: how agents are discovered, trusted, verified, and coordinated across the open web. This creates the need for ICANN- and W3C-like governance and standards for agents.

Second, the Commerce Layer: what is the dollar value of intelligence? Agents will pay for reasoning, inference, memory, capabilities, and context through emerging “knowledge pricing” markets. Intelligence itself will be discovered, priced before use, coordinated among untrusted entities, and delivered in new ways.

Third, the Bazaar Layer: the last 14 years were about machine learning. The next decade will be about machine co-learning.

Speakers:
- Ramesh Raskar (MIT Media Lab): Ramesh Raskar is an Associate Professor at the MIT Media Lab and founding architect of NANDA whose pioneering work spans distributed AI agent architectures, health technology, and computational imaging, holding 100+ US patents and earning honors including the National Academy of Inventors award (2024), the Lemelson Award (2016), and the ACM SIGGRAPH Achievement Award (2017), alongside research roles at Google [X], Apple, and Facebook and the co-founding or advising of several companies.
  LinkedIn: https://www.linkedin.com/in/raskar

## A Song of Types and Agents - Roberto Stagi, Ratel

- Upload date: 2026-07-12
- Video: https://www.youtube.com/watch?v=UlFB6efYN5Q
- Transcript: raw/20260712_UlFB6efYN5Q/UlFB6efYN5Q.en-orig.vtt
- Metadata: raw/20260712_UlFB6efYN5Q/UlFB6efYN5Q.info.json

Python ruled unchallenged for a decade, sitting comfortably on the AIron Throne. But a quiet rebellion is brewing: the entire stack that actually deploys AI agents in production runs on npm, not pip. This lightning talk is an opinionated, slightly unhinged tour of how TypeScript is taking over the AI throne, why this happened and how you can prepare for it.

Speakers:
- Roberto Stagi (Ratel): Roberto is the CTO & Co-Founder of Ratel, context layer for AI Agents, EU-Ambassador at AI Socratic, and deep into the mission of making context engineering simple for everyone.
  X/Twitter: https://x.com/rstagi_
  LinkedIn: https://linkedin.com/in/rstagi
  GitHub: https://github.com/rstagi

## ReviewDebt: a practical framework for scoring every pull request — Sachin Gupta, Ebay

- Upload date: 2026-07-12
- Video: https://www.youtube.com/watch?v=TJPInBjhE4Q
- Transcript: raw/20260712_TJPInBjhE4Q/TJPInBjhE4Q.en-orig.vtt
- Metadata: raw/20260712_TJPInBjhE4Q/TJPInBjhE4Q.info.json

Coding agents ship PRs faster than humans can trust them. The gap is filling up with a debt nobody is measuring — and it's about to swallow your engineering velocity.
Every team in 2026 measures coding agents the same way: PR count, lines of code, cycle time, developer NPS. None of those see the real cost — bloated diffs, weak tests, ambiguous rationale, ownership sprawl, and human reviewers spending more time verifying AI code than they used to spend writing their own.
This talk introduces ReviewDebt: a practical framework for scoring every pull request on the hidden review burden it creates. The scoring is deterministic — diff size, test-coverage delta, ownership spread, generated-code smells, evidence and rationale gaps — so the number is defensible in a real engineering review. We'll walk three real PRs side-by-side (clean human PR, high-debt AI PR, refactored AI PR), watch the scoring play out signal by signal, and look at a 90-day dashboard from a production backend org where review debt climbs in lockstep with AI-PR share.

Speakers:
- Sachin Gupta: Sachin Gupta is a Staff Software Engineer with 15+ years building backend platforms at internet scale, currently focused on the runtime trust boundaries that LLM coding agents blur and the creator of HeapLens, a Java heap analyzer extension used in 50+ countries.
  LinkedIn: https://www.linkedin.com/in/guptasachin1/
  GitHub: https://github.com/sachinkg12

## Semantic Blindness: 500,000 Sensors Confused an LLM - Raahul Singh & Vanč Levstik, Phaidra

- Upload date: 2026-07-12
- Video: https://www.youtube.com/watch?v=EUsPvBeIx70
- Transcript: raw/20260712_EUsPvBeIx70/EUsPvBeIx70.en-orig.vtt
- Metadata: raw/20260712_EUsPvBeIx70/EUsPvBeIx70.info.json

You cannot solve a combinatorial engineering problem with a next token prediction engine. We learned this the hard way.

Modern LLMs can write code, summarize research papers, and reason across massive datasets. But what happens when you connect them to mission-critical physical infrastructure with 50,000 live sensors, deterministic dependencies, and real-world thermodynamic constraints?

We deployed state-of-the-art LLMs to manage real time operations within industrial and AI factory environments to tackle root cause analysis, alarm triage, and operational decision support. What we discovered was a fundamental architectural mismatch between probabilistic language models and deterministic engineering systems.

In this talk, we introduce a failure mode we call Semantic Blindness: the inability of general-purpose LLMs to maintain structural awareness of physical systems, even when provided enormous amounts of context.

This talk dissects three specific failure modes we encountered — and why each one exposes a gap in how the industry thinks about scaling LLMs to complex systems:

1) The Topology Trap. Vector embeddings don't understand pipes, wires, or physical causality. Sensor_445_Temp is just a string. But in reality, it's attached to Valve B, which controls coolant to Generator 3.
2) The Illusion of Scale. At a small scale, dumping 100 sensors into the context window works surprisingly well. It’s a reasonable solution and it holds up. At 500,000 sensors, the same approach collapses. It creates new problems: attention degrades, critical anomalies get buried in the middle, and latency spikes to unusable levels for real-time response.

3) The Repetition Kill Switch. Industrial tag naming conventions are nearly identical at scale. Feeding the same naming conventions across hundreds of variants, you’ll trip the model’s repetition penalty. It thinks it’s stuck in a degenerate loop and it will literally stop. The data is correct. The model just can’t handle it.
Rather than focusing on prompt engineering tricks, this session explores the architectural patterns required to make AI reliable in real-world engineering environments.

We’ll present a practical hybrid design approach that combines:

- semantic ontologies,
- deterministic query systems,
- structured synthesis layers,
- and LLM orchestration architectures purpose-built for operational infrastructure.

Attendees will leave with a clear understanding of:

- why naive RAG architectures fail in industrial environments,
- how to design AI systems that respect physical reality,
- how to make LLMs work reliably against massive scale of data
- and what the next generation of “AI-enabled intent resolution” actually looks like beyond semantic search.

This session is designed for senior AI engineers, infrastructure architects, CTOs, and technical leaders building AI systems that must operate reliably under real-world constraints — not just benchmark well in demos.

Speakers:
- Raahul Singh (Phaidra): Raahul Singh is a Staff AI Research Engineer at Phaidra and the lead architect behind the company's agentic AI platform for data center infrastructure.
  LinkedIn: https://www.linkedin.com/in/raahulsingh42
  GitHub: https://github.com/raahul-singh
- Vanč Levstik (Phaidra): Vanč Levstik is a Senior Engineering Manager at Phaidra and leading the teams developing Phaidra Prism

## RLM: Recursive Language Models for Large Codebases - Shashi, Superagentic AI

- Upload date: 2026-07-12
- Video: https://www.youtube.com/watch?v=8oyalrfwgjw
- Transcript: raw/20260712_8oyalrfwgjw/8oyalrfwgjw.en-orig.vtt
- Metadata: raw/20260712_8oyalrfwgjw/8oyalrfwgjw.info.json

Large codebases break coding agents: they lose the architecture and drown in tool output as context grows. This talk introduces Recursive Language Models (RLM) from a MIT paper a pattern that loads the repo into a programmable REPL where the model writes code to inspect it and recursively delegates focused sub-questions via llm_query. With a live demo on RLM Code (independent, unofficial), you'll see the loop run end to end on local and cloud models, with a fully inspectable trajectory.

Speakers:
- Shashi (Superagentic AI): Building tools and frameworks for AI Agents
  X/Twitter: https://x.com/Shashikant86
  LinkedIn: https://www.linkedin.com/in/shashikantjagtap/
  GitHub: https://github.com/Shashikant86

## What Does Done Even Mean? Agents and Paperclip's Liveness Model - Dotta, Paperclip

- Upload date: 2026-07-12
- Video: https://www.youtube.com/watch?v=7P0elyLIxXo
- Transcript: raw/20260712_7P0elyLIxXo/7P0elyLIxXo.en-orig.vtt
- Metadata: raw/20260712_7P0elyLIxXo/7P0elyLIxXo.info.json

What does “done” mean when agents can produce more work than humans can possibly review? This talk argues that the future of agentic work is not just faster output, but a stronger trust protocol: systems where “done” means an artifact has met a stated standard, carries evidence, has been checked by the right verifier, assigns ownership of remaining risk, and clearly authorizes the next action. Drawing from Paperclip’s liveness model, it shows how teams can avoid approval theater, keep work moving, route review by risk, and turn agent completion from a vague confidence signal into something others can safely build on.

Speakers:
- Dotta (Paperclip): Dotta is the creator of Paperclip, the Open-source app for zero human companies
  X/Twitter: https://x.com/dotta
  GitHub: https://github.com/cryppadotta

## The AI bugpocalypse is here. Now what? - Jack Cable, Corridor

- Upload date: 2026-07-12
- Video: https://www.youtube.com/watch?v=7JgIS42mz7U
- Transcript: raw/20260712_7JgIS42mz7U/7JgIS42mz7U.en-orig.vtt
- Metadata: raw/20260712_7JgIS42mz7U/7JgIS42mz7U.info.json

Something shifted in the past year that most security teams haven't fully reckoned with yet: AI models can now find serious vulnerabilities in production code, at scale, with minimal human skill required. Not in toy examples. In libraries that have been reviewed hundreds of times by the best researchers in the world. Jack Cable, Co-Founder and CEO of Corridor, will walk through what this means for the 80% of organizations that have never had to defend against adversaries doing in-house vuln discovery: where the real exposure is, what the available playbooks actually get right, and what concrete steps security teams can take right now to reduce their blast radius before open-weight models make this everybody's problem.

Speakers:
- Jack Cable (Corridor): Jack Cable is a hacker who serves as the Co-Founder and CEO at Corridor, the security platform for AI coding.
  X/Twitter: https://x.com/jackhcable
  LinkedIn: https://www.linkedin.com/in/jackcable/

## remobi.app: Don't change your terminal workflow for mobile

- Upload date: 2026-07-12
- Video: https://www.youtube.com/watch?v=5192csoTkVo
- Transcript: raw/20260712_5192csoTkVo/5192csoTkVo.en-orig.vtt
- Metadata: raw/20260712_5192csoTkVo/5192csoTkVo.info.json

remobi.app: Don't change your terminal workflow for mobile. Swipe between agents, unblock when stuck.

## Claws Out: Securing and Building with OpenClaw - Nick Taylor, Pomerium

- Upload date: 2026-07-11
- Video: https://www.youtube.com/watch?v=xg1zNlzw7Jk
- Transcript: raw/20260711_xg1zNlzw7Jk/xg1zNlzw7Jk.en-orig.vtt
- Metadata: raw/20260711_xg1zNlzw7Jk/xg1zNlzw7Jk.info.json

Running OpenClaw without hardening access to it is a bad idea. We'll cover how I secured my OpenClaw, McClaw, contributed trusted-proxy auth mode to the OpenClaw project, and how I use it to build tools.

We're going to build something live during the talk using OpenClaw, the same way I built Clawspace, a browser-based file explorer/editor for your OpenClaw workspace.

feat(gateway): add trusted-proxy auth modegiithub.com/nickytonline/clawspace, a browser-based file explorer/editor for an OpenClaw workspace.github.com/pomerium/pomerium, an open core Identity-Aware Proxy

## Stop AI Agent Hallucinations: 5 Techniques + Production Patterns - Elizabeth Fuentes, AWS

- Upload date: 2026-07-11
- Video: https://www.youtube.com/watch?v=vJukHCIv7Ck
- Transcript: raw/20260711_vJukHCIv7Ck/vJukHCIv7Ck.en-orig.vtt
- Metadata: raw/20260711_vJukHCIv7Ck/vJukHCIv7Ck.info.json

AI agents that book 15 guests in a 10-person room. Agents that fabricate statistics when data doesn't exist. Agents that pick wrong tools from 29 options, wasting $47 in tokens. These aren't prompt engineering failures, they're architectural limitations that need structural solutions.

This hands-on workshop covers 5 research-backed techniques to prevent agent hallucinations:

1. Graph-RAG (Neo4j) - Replace vector similarity guessing with precise entity relationships. Result: 73% fewer fabricated statistics.
2. Semantic Tool Selection - Filter 29 tools to the relevant 5 using embeddings. Result: 89% token reduction, accurate tool selection.
3. Multi-Agent Validation - Executor-Validator-Critic swarms catch fabrications through cross-checking. Result: 92% detection rate.
4. Neurosymbolic Guardrails - Framework-enforced rules (lifecycle hooks) that agents cannot bypass. Result: Zero business rule violations.
5. Agent Steering - Guide agents to self-correct instead of blocking them. Result: Task completion without hard failures.

Each demo includes live code, before/after metrics, and failure case analysis. Final module shows production deployment.

You'll walk away with working Python implementations, a decision framework for when to apply each technique, and an open-source repository adaptable to your domain.

code: https://github.com/elizabethfuentes12/why-agents-fail-sample-for-amazon-agentcore

Speakers:
- Elizabeth Fuentes (AWS): Elizabeth Fuentes is a developer advocate and AI engineer focused on what makes agents fast, cheap, and correct in production. She turns failure modes (hallucination, token blowups, context overflow, lost memory) into named, measurable fixes, each backed by a runnable demo and before/after numbers. Her work covers the architectural decisions behind reliable agents: context offloading, the split between conversation and data memory, semantic versus exact-reference retrieval, guardrails, and agent evaluation. With 107+ published technical articles and a Master's in Data Science, she shares production agent patterns across English and Spanish developer communities, and likes turning complex concepts into something anyone can learn.
  X/Twitter: https://x.com/ElizabethFue12
  LinkedIn: https://www.linkedin.com/in/lizfue/
  GitHub: https://github.com/elizabethfuentes12

## The Factory That Dreams: 39 AI Agents, No Framework - Rushabh Doshi, Machinecraft

- Upload date: 2026-07-11
- Video: https://www.youtube.com/watch?v=jtzh-GBXBWc
- Transcript: raw/20260711_jtzh-GBXBWc/jtzh-GBXBWc.en-orig.vtt
- Metadata: raw/20260711_jtzh-GBXBWc/jtzh-GBXBWc.info.json

Most AI demos are built around a toy workflow. Ira was built around a factory.

This talk is the story of how a third-generation Indian machinery company built a multi-agent operating system that helps run sales, business development, recruitment, quoting, marketing, production context, email workflows, and organizational memory. Ira is not a chatbot and not a wrapper around a single framework. It is a company brain: 39 bounded specialist agents, Athena as orchestrator, a 17-stage request pipeline, Qdrant for document memory, Neo4j for relationships, Mem0 for long-term semantic memory, Postgres for CRM and recruiting data, Redis for coordination, and Cursor as the operating cockpit.

The deeper lesson is architectural: companies do not need generic AI assistants. They need digital brains grounded in their own documents, relationships, processes, and values. I will show how Ira ingests company files through a "digestive system", routes work through a pantheon of agents, verifies claims through immune-system style guardrails, learns through memory and corrections, and "dreams" through a nightly consolidation cycle. I will also explain why we gave Ira a SOUL.md: a philosophical constitution based on Anekantavada, Syadvada, Svadharma, and operational truthfulness.

The talk ends with the Fork My Brain thesis: the right way to build company AI is not to sell another SaaS dashboard. It is to send a special-ops AI team inside a company for a week, map the business from the inside out, ingest the right files into Qdrant and Neo4j, wire the operational databases, and leave behind a forkable digital brain that employees can run through Cursor and LLMs.

Speakers:
- Rushabh Doshi (Machinecraft / Fork My Brain): Rushabh Doshi builds and operates Ira, a multi-agent AI operating system for Machinecraft, an Indian thermoforming machinery manufacturer, combining Cursor, LLMs, retrieval, memory, and business operations into one living company brain.
  LinkedIn: https://www.linkedin.com/in/rdd0101/
  GitHub: https://github.com/doshirush1901

## Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers — Alex Bauer, Upside.tech

- Upload date: 2026-07-11
- Video: https://www.youtube.com/watch?v=YZQsWVeN3rE
- Transcript: raw/20260711_YZQsWVeN3rE/YZQsWVeN3rE.en-orig.vtt
- Metadata: raw/20260711_YZQsWVeN3rE/YZQsWVeN3rE.info.json

A couple of years ago, everyone worried about AI hallucinating. We rarely hear that word anymore, but it’s just because the problem grew up. Today, your AI still doesn’t know how to say “I’m not sure.” Instead, it hands you a revenue number that’s wrong in ways that look exactly like being right.

The good news is we already solved this once, for people: you onboard a new hire so they understand your business; you put subjective, high-stakes calls in front of more than one set of eyes. This talk walks through patterns we run at Upside, including a librarian every agent consults before it acts, a jury-and-judge model for the questions a single pass can’t be trusted to answer, and knowing when the model itself is just too dumb for the job. Live demos and real failures included.

Speaker:
Alex Bauer - (https://Upside.tech)
Alex Bauer is co-founder of Upside, the data layer for GTM engineers. He spent 2016–2024 at Branch as the public voice of mobile attribution and deep-linking. He now builds the clean, normalized GTM data that revenue teams point Claude and Cursor at to answer "what actually happened, and did it work?"
X: https://x.com/alexdbauer
LinkedIn: https://www.linkedin.com/in/alexdbauer/
GitHub: https://github.com/aeromusek
Website: https://alexbauer.net/

## Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD - Sumaiya Shrabony

- Upload date: 2026-07-11
- Video: https://www.youtube.com/watch?v=WLXxTaPagA8
- Transcript: raw/20260711_WLXxTaPagA8/WLXxTaPagA8.en-orig.vtt
- Metadata: raw/20260711_WLXxTaPagA8/WLXxTaPagA8.info.json

If you build agents alone long enough, you will independently reinvent five things software engineering solved decades ago. A way to test whether your agent's output is still correct after you changed something. A way to run it on a schedule and know if it failed. A way to prevent one skill's schema change from silently breaking three downstream skills. A way to roll back when today's run produces garbage. A way to validate outputs before they hit production. You just reinvented regression testing, cron monitoring, contract testing, version control, and staging. Badly. Without realizing it.

The dangerous failure in an agent system is not bad output. Bad output is easy to catch. The dangerous failure is a polished artifact that looks ready but violates a production contract: it uses the wrong voice patterns, makes an unverified claim, repeats an old angle, and gets labeled "READY TO PUBLISH" anyway. That is the agent equivalent of shipping because the code compiled, even though the tests never ran.

This talk uses a real, open-source 19-skill Claude Code agent system (github.com/safrin96/agentic-content-system) as the case study. Through an interactive live demo, I show three ways an agent system silently lies to you and what a boundary looks like that catches it. The takeaway is simple: the infrastructure gap in the agent ecosystem is not another framework. It is the equivalent of what CI/CD gave software teams in 2015, a standard, boring, reliable way to test, deploy, and roll back agent behavior. Before you add another agent, add one boundary.

Speakers:
- Sumaiya Shrabony: Sumaiya Shrabony is a Technical Program Manager, enterprise AI practitioner, and content creator across LinkedIn, Instagram (@thedata_ai.girl), and Substack (Ground Truth) building toward thought leadership at the intersection of enterprise data infrastructure, AI adoption, and the immigrant-in-tech experience.
  LinkedIn: https://www.linkedin.com/in/sumaiya-shrabony
  GitHub: https://github.com/safrin96

## Chat and citations won't save your vertical AI - Atul Ramachandran, Filed Inc

- Upload date: 2026-07-11
- Video: https://www.youtube.com/watch?v=RGiXcVxSD3s
- Transcript: raw/20260711_RGiXcVxSD3s/RGiXcVxSD3s.en-orig.vtt
- Metadata: raw/20260711_RGiXcVxSD3s/RGiXcVxSD3s.info.json

Most vertical SaaS teams are doing the same things: chasing higher accuracy, building better model harnesses, shipping more features. And their customers are saying the same things: the AI got this wrong, it hallucinated, the accuracy is not good enough. So teams go back and push the numbers higher.
We did the same at Filed. We built AI data entry for tax firms and hit 80%+ accuracy against an industry baseline of 50-60%. Many users still complained. Same model, same stack, different outcomes. So we dug in.
The unhappy customers were not experiencing worse AI. They were reverse-engineering everything we produced. We had not removed work from their day. We had just changed its shape. Chat interfaces and citation trails feel like the fix. They are not. They hand the verification burden back to the user with extra steps. Accuracy %s are the score you get after the game is already over. The complaints, the hallucination reports, all of it: symptoms of the same underlying problem. Users are still holding the bag, and when they are, every error is catastrophic.
When we started building the real fix, we realised the coding world had already been here. Early coding AI dumped a full function and asked engineers to review 200 lines. Same problem. The fix was not a better model. It was Copilot in the editor, not a separate tab. The planner pattern instead of dumping full outputs. Skills and memory that compound with every use. We reached the same conclusion independently, from taxes.
This talk is those three patterns and what they look like in a vertical SaaS product.
Go where the work is. Most users will try a new feature. Almost none will adopt a new platform. AI has to live inside existing workflows, not alongside them.
1000 feet first. The right unit of work matters more than accuracy on any given unit. Start at the macro level, let users orient, then drill down. Each level is small enough to verify fast. Users stop auditing and start deciding.
Skills over models. Every edge case is a skill waiting to be encoded, not a model failure. Turn real usage into institutional knowledge that makes every future user better off.
The specific lessons are from taxes. The pattern is universal.

Speakers:
- Atul Ramachandran (Filed Inc): Atul has cofounded multiple startups and is currently CTO of Filed, which has raised over $17M to build AI infrastructure for tax firms. He is an active open source contributor in the JavaScript ecosystem, with projects like NodeGui. He is currently based out of Stockholm, Sweden.
  X/Twitter: https://x.com/a7ulr
  LinkedIn: https://www.linkedin.com/in/atulanand94/
  GitHub: https://github.com/a7ul

## State of the Union: Why Local, Why Now — NVIDIA, Osmantic, Roboflow, EXO Labs, @matthew_berman

- Upload date: 2026-07-11
- Video: https://www.youtube.com/watch?v=KB41dTlX1Uc
- Transcript: raw/20260711_KB41dTlX1Uc/KB41dTlX1Uc.en-orig.vtt
- Metadata: raw/20260711_KB41dTlX1Uc/KB41dTlX1Uc.info.json

Alex Cheema's team spent three weeks inside a conference room at NVIDIA headquarters and left with a 10x inference speedup on the DGX Spark, no new computer science required. The update they emailed to Jensen said the wins came from assembling optimizations NVIDIA experts had already solved, pulled together by teams swarming the room all day. The hardware math frames the whole panel: the Spark shares its Grace Blackwell architecture with the data center, Nemotron 3 Ultra runs at 30 tokens per second on four Sparks in the demo room next door, and a four billion parameter Qwen 3.5 on an iPhone now matches what GPT 4o once needed a data center to serve.

Joseph Nelson remembers a passenger on his flight whose phone described the seat back in front of them as a printer while a freshly released LLaVA identified it correctly, his proof that no trillion dollar company holds a monopoly on frontier intelligence. Ahmad Osman places the ecosystem in the 1990s of Linux, where the missing piece is point and click onboarding rather than capability, and Matthew Berman sets the bar for mainstream adoption at nothing harder than opening Cursor. The market is already voting: route planning to frontier models and execution to small specialized ones, which is how Coinbase reports exploding token counts on flat costs.


Speaker info:
Nader Khalil, moderator (NVIDIA):
- https://x.com/naderlikeladder
- https://www.linkedin.com/in/naderlikeladder

Joseph Nelson (Roboflow):
- https://x.com/josephofiowa
- https://roboflow.com

Alex Cheema (EXO Labs):
- https://x.com/alexocheema
- https://exolabs.net

Ahmad Osman (Osmantic):
- https://x.com/TheAhmadOsman
- https://www.linkedin.com/in/TheAhmadOsman

Matthew Berman (Forward Future):
- https://www.youtube.com/@matthew_berman
- https://forwardfuture.com

Timestamps:
0:00 - Welcome to the Local AI Summit
0:40 - Karpathy twice right on keeping up
1:16 - Reasoning models and always on agents
2:32 - Panelist introductions
4:41 - When the inflection point hit
6:36 - GPT 4o quality in your pocket
7:14 - Llama 405B to DeepSeek to GLM 5.2
8:47 - The airplane accessibility story
10:25 - Harnesses give models the real world
11:27 - What language learns from vision
13:19 - A multimodel world in practice
13:57 - Coinbase: tokens up, costs flat
15:03 - Control, sovereignty, no rug pulls
17:50 - Small specialized models and data flywheels
19:45 - A second headquarters inside NVIDIA
21:50 - 10x on the DGX Spark by swarming
24:32 - Desk and data center share an architecture
26:11 - ODS and point and click onboarding
27:14 - Where local still falls short
32:33 - Why finetuning as a service stalled
35:34 - Distillation down to a submarine
39:42 - The biggest open problems in local
42:01 - Open source advocacy and closing

## From Writing Code to Designing Systems: How the Developer Role is Changing — Chris Noring, Microsoft

- Upload date: 2026-07-11
- Video: https://www.youtube.com/watch?v=GdvKNwMcfd0
- Transcript: raw/20260711_GdvKNwMcfd0/GdvKNwMcfd0.en-orig.vtt
- Metadata: raw/20260711_GdvKNwMcfd0/GdvKNwMcfd0.info.json

For decades, developers have been valued primarily for how much code they could write and how quickly they could write it. That model no longer scales. As AI becomes a first-class collaborator, the bottleneck is no longer syntax or implementation speed—it’s clarity of intent, architectural thinking, and the ability to coordinate work across many autonomous contributors.

Today’s challenge is not "How do I write this code?" but "How do I ensure this system is built correctly, consistently, and to company standards—across dozens of moving parts?" Without structure, AI-assisted development risks fragmentation: inconsistent patterns, duplicated logic, and solutions that technically work but fail architectural, security, or organizational expectations.

This talk introduces a new mental model for modern development: the developer as planner, system designer, and orchestrator of agents. Using GitHub Copilot, GitHub Copilot CLI, and custom Copilot agents driven by agents.md, we’ll explore how developers can decompose large problems, delegate implementation to specialized AI agents, and encode standards, constraints, and intent directly into the workflow. Instead of prompting ad-hoc, we define explicit instructions per layer—frontend, backend, infrastructure, testing—so every agent builds the right thing in the right way.

The result is not less control, but more leverage: faster delivery, higher consistency, and systems that reflect deliberate design rather than accidental outcomes.

What you’ll learn:

How the developer role is shifting from code producer to system designer, planner, and agent orchestrator

How to structure projects for agent-driven development, using GitHub Copilot CLI, Copilot Chat, and agents.md to encode standards and intent

How to ensure architectural consistency and quality at scale by giving agents clear responsibilities, constraints, and ownership boundaries

## Develop at Idea Velocity - Jeffrey Lee-Chan, Snapchat

- Upload date: 2026-07-11
- Video: https://www.youtube.com/watch?v=9arM9b7JgOo
- Transcript: raw/20260711_9arM9b7JgOo/9arM9b7JgOo.en-orig.vtt
- Metadata: raw/20260711_9arM9b7JgOo/9arM9b7JgOo.info.json

The biggest gap in production AI agent systems is not the model—it's the harness. After 1,000 hours of orchestrating autonomous fleets under human direction, the pattern is unmistakable: agents that finish complex tasks on the first run routinely fail on subsequent iterations because the surrounding loop lacks persistent memory and contextual guardrails.

In this talk, I dissects the key multi-agent primitives required to turn raw models into deterministic teammates. Moving beyond simple API wrappers, we explore how separating your stack into distinct "Agent Orchestrator Managers" and specialized workers prevents low-level implementation bias.

Using concrete examples from production systems, we will walk through real-time terminal routing via CMUX, analyze the token-burn tradeoffs between leading models, and look under the hood of high-context consumer applications like WorldAI and Consensus ML. You will walk away with a practical architectural checklist you can drop directly into your own agent infrastructure on Monday morning.

Once you're setup you can truly develop at idea velocity ie. natural language  to  code  to  automated iteration  to  evidence produced  to  human review where human interaction in the middle is pushed to the beginning or end allowing improved parallelization.

Speakers:
- Jeffrey Lee-Chan (Snapchat): Most teams use AI tools wrong — humans still on the critical path. I build parallel multi-agent harnesses so one engineer directs 10–20 coding agents instead of becoming the rate limiter.
  X/Twitter: https://x.com/jleechan2015
  LinkedIn: https://www.linkedin.com/in/jeffrey-lee-chan/
  GitHub: https://github.com/jleechanorg

## Should AI Engineers Still Read Code in 2026? The Z/L Continuum — Alex Volkov, ThursdAI

- Upload date: 2026-07-10
- Video: https://www.youtube.com/watch?v=ZpK5PWX2YRM
- Transcript: raw/20260710_ZpK5PWX2YRM/ZpK5PWX2YRM.en-orig.vtt
- Metadata: raw/20260710_ZpK5PWX2YRM/ZpK5PWX2YRM.info.json

"How much better do the models have to get before you'll stop reading the code?" Theo asked that question recently and the replies caught fire. Mitchell Hashimoto is calling it agent psychosis. ThePrimeagen's subreddit is in open revolt about people shipping code they never read. Uncle Bob says we have about a year left of looking at code at all.

Alex Volkov saw this argument coming three months ago, and gave it a name.

At AI Engineer Europe, OpenAI's Ryan Lopopolo opened the conference by saying "code is free." His team shipped over 1,000,000 lines with zero human review. Mario Zechner closed the same conference telling everyone to slow the f*** down and read every line. Same stage. Opposite advice. Standing ovations for both.

Alex hosts ThursdAI and spends every week talking to the people building this stuff. In this talk he lays out the Z/L Continuum: what the top AI engineers in the world actually do, not what they say on stage. Including:

• Anthropic's own numbers on Claude writing 80%+ of Claude's code, and what happens when it breaks
• Why human review became the bottleneck nobody wants to talk about
• The uptime chart that looks like a Christmas tree
• Why Dexter Horthy, the "let the agent cook" guy, publicly said "I was wrong"
• The one tweet that changed how Alex thinks about this. You're not Team Z or Team L. Every task gets its own spot on the continuum, and knowing where to place it is the actual skill now.

If you've ever shipped code you didn't read (be honest), this talk is about you.

Speaker info:
- https://x.com/altryne
- https://thursdai.news
- The original Z/L Continuum essay: https://thursdai.news/zl
- Anthropic's "When AI Builds Itself": https://www.anthropic.com/institute/recursive-self-improvement
- Lucas Meijer's tweet: https://x.com/lucasmeijer/status/2044448265194627182

Timestamps:
0:00 - Introduction
0:48 - The shift in AI engineering since December 2025
1:32 - The trend of AI-assisted coding and reduced manual input
3:37 - The core conflict: "Code is free" vs. "Read every line"
6:13 - Defining the Z/L Continuum
8:02 - Analyzing the "code is free" perspective (Ryan Lopopolo/OpenAI)
9:31 - Risks of rapid AI output and incident rates
11:04 - Recursive Self-Improvement (RSI) and human review as a bottleneck
12:08 - The correction: Focusing on tasks, not people
13:56 - Recommended strategy: Routing changes for appropriate verification
15:52 - Emerging capabilities: Fable and Mythos
17:16 - Capability drift and the shift toward "Loops"
18:16 - Understanding "Loops" as the next engineering primitive
20:15 - Future outlook and maintaining flexibility

#AIEngineering #AICoding #CodeReview #VibeCoding #ClaudeCode #AIAgents #ThursdAI

## Understanding is the new bottleneck — Geoffrey Litt, Notion

- Upload date: 2026-07-10
- Video: https://www.youtube.com/watch?v=WkBPX-oDMnA
- Transcript: raw/20260710_WkBPX-oDMnA/WkBPX-oDMnA.en-orig.vtt
- Metadata: raw/20260710_WkBPX-oDMnA/WkBPX-oDMnA.info.json

Autonomous loops are hot, but the reality is that most agentic tasks still require human judgement. And to guide your agents well, it's not enough to just verify correctness -- you actually need to understand the work they're doing.

In this talk, I'll share some techniques for staying in the loop and efficiently developing understanding, combining old ideas from education and cognitive science with modern agent capabilities. You'll walk away with some practical tips for moving faster with agents by understanding more, not less.

## The Golden Age of AI Engineering — Alexander Embiricos & Romain Huet & Peter Steinberger, OpenAI

- Upload date: 2026-07-09
- Video: https://www.youtube.com/watch?v=pMggiOb18tc
- Transcript: raw/20260709_pMggiOb18tc/pMggiOb18tc.en-orig.vtt
- Metadata: raw/20260709_pMggiOb18tc/pMggiOb18tc.info.json

OpenAI's Dev Day 2024 demo ran on an o1 preview model that could not run or check its own code, so Romain Huet had to cross his fingers live on stage. A year later, the same kind of demo ran a full camera and lighting rig, because the model could now test its own work. Alexander Embiricos and Huet use that jump to show how fast Codex is moving: new model releases went from every 15 months to about every 6 weeks.

They walk through why Codex is built on the same responses API, open source harness, and AGENTS md file format that ships to every developer, plus new numbers on cost and speed: frontier level intelligence at $1 per million input tokens and $6 per million output tokens, and a model generating 750 tokens a second, fast enough to produce a real pull request in about 10 seconds.

Speaker info:
- https://twitter.com/embirico
- https://www.linkedin.com/in/embirico

- https://twitter.com/romainhuet
- https://www.linkedin.com/in/romainhuet

- https://twitter.com/steipete
- https://www.linkedin.com/in/steipete

Timestamps:
0:00 - Introduction
0:13 - The World's Fair analogy
1:10 - The role of AI engineers in the future of work
2:14 - Accelerating model development cycles
3:09 - Evolution of build-and-test model loops
4:03 - Scaling engineering capabilities through agents
5:30 - Defining the desired AI engineering product experience
7:59 - The design philosophy of the Codex app
9:44 - The open-source stack and building with API primitives
11:43 - Expanding the ecosystem with Apps Server and plugins
14:20 - Optimizing for "Value Maxing": Cost and Intelligence
15:48 - Achieving high-speed inference for real-time workflows
16:51 - Future outlook: Removing the local/cloud distinction
18:16 - Special guest introduction: Peter Steinberger
18:56 - Shifting from manual orchestration to managing agents
20:02 - Three key changes for scalable agent loops
21:19 - Redefining the bottleneck as human attention
22:08 - Workflow example: Automating open-source issue resolution

## Everything we knew about software has changed — Theo Browne, @t3dotgg ​

- Upload date: 2026-07-08
- Video: https://www.youtube.com/watch?v=xUnRQ9vLXxo
- Transcript: raw/20260708_xUnRQ9vLXxo/xUnRQ9vLXxo.en-orig.vtt
- Metadata: raw/20260708_xUnRQ9vLXxo/xUnRQ9vLXxo.info.json

For the closing keynote of AIEWF2026, Theo provokes you to think wider, not just bigger.

In this keynote from the AI Engineer World's Fair, developer and YouTuber Theo Browne (@t3dotgg) argues that the rapid evolution of AI models—moving from tool-calling (Sonnet 3.5) to long-running task execution (Opus 4.5) and now orchestration (Mythos)—requires software engineers to fundamentally change how they build products.

Key Themes:
Rejecting Skeuomorphism: Browne compares the current state of software development to the design shift in iOS 7, urging developers to move away from legacy mental models and tools (like Git or terminal-centric workflows) that prioritize familiarity over actual utility (6:08 - 8:32).
The New Tier System: Traditional categorizations of "side project," "startup," and "too big" have shifted. He highlights that tasks once requiring a dedicated startup can now be managed by simple automated systems, such as a Markdown file running on a cron job (10:33 - 12:20).
Thinking Bigger: Rather than just building depth in a narrow feature set, Browne encourages builders to cover a wider spectrum of product functionality. Because AI agents can now handle significant parts of implementation, it is becoming viable for smaller teams to build products that compete with industry giants like AWS or Salesforce by architecting them for extensibility (13:12 - 15:30).

Takeaway: The barrier to entry for building complex, wide-reaching platforms has collapsed. Engineers should stop limiting themselves by legacy constraints and start building much more ambitious projects.

Timestamps
0:00 – Introduction and the "AI psychosis" experience
0:50 – Evolution of AI models: Sonnet 3.5, Opus 4.5, and Mythos
3:04 – The imperative to "go bigger" and push model capabilities
3:35 – Overcoming legacy constraints and developer habits
6:08 – Moving past our "skeuomorphic" phase in software development
9:30 – Personal project evolution: side projects, startups, and the "Markdown tier"
12:22 – Identifying the gap: What is "too big" anymore?
13:06 – Redefining the strategy: Building for a wider spectrum instead of just depth
14:50 – Scaling and architecting products to allow for user-driven extensibility

## Your agent is blindfolded — Johan Lajili, Poolside AI

- Upload date: 2026-07-08
- Video: https://www.youtube.com/watch?v=iRcX54EO5g8
- Transcript: raw/20260708_iRcX54EO5g8/iRcX54EO5g8.en-orig.vtt
- Metadata: raw/20260708_iRcX54EO5g8/iRcX54EO5g8.info.json

Your agent is blindfolded. How giving it (good) eyes multiplies performance and trust!

## Think You Can Build a Game with AI? Think Again! - Danielle An & David Hoe, Meta

- Upload date: 2026-07-08
- Video: https://www.youtube.com/watch?v=grdoOC1BT1s
- Transcript: raw/20260708_grdoOC1BT1s/grdoOC1BT1s.en-orig.vtt
- Metadata: raw/20260708_grdoOC1BT1s/grdoOC1BT1s.info.json

With the recent development of AI, either you or your friend probably vibe coded a game using Gemini, on Three.js. But that is old news now. If everyone can do that, what is next? The next massive hit, the one that millions of people across the world will play, is just about to be born. Wanna know more? Come see this talk!

## Your coding agent doesn't always follow your rules — Talha Sheikh, Checkout.com

- Upload date: 2026-07-08
- Video: https://www.youtube.com/watch?v=MpZzWMdmQCE
- Transcript: raw/20260708_MpZzWMdmQCE/MpZzWMdmQCE.en-orig.vtt
- Metadata: raw/20260708_MpZzWMdmQCE/MpZzWMdmQCE.info.json

Your coding agent doesn't always follow your rules. An agent harness makes sure it does, in real-time, every time.

## Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data - Sachin Kumar, LexisNexis

- Upload date: 2026-07-08
- Video: https://www.youtube.com/watch?v=IQkVMvXQKLY
- Transcript: raw/20260708_IQkVMvXQKLY/IQkVMvXQKLY.en-orig.vtt
- Metadata: raw/20260708_IQkVMvXQKLY/IQkVMvXQKLY.info.json

You fine-tune LLMs and ship them. Your evals are green, your behavioral monitors are green — and a sleeper-agent backdoor can still flip the model to harmful output on a trigger you never tested. Behavioral testing can't reach it, and the interpretability tool people reach for — joint cross-model features (crosscoders) — dilutes the signal until it sits at the noise floor.

The fix is in what the training data changed. A backdoor is a directional shift that fine-tuning writes into the model's activations, so you isolate it by watching the difference between the base and fine-tuned model. In a controlled SQL-injection backdoor, a sparse autoencoder trained on that difference flags it with 40× the signal of joint features, perfect precision, and zero false positives — from a single cheap layer. You'll leave knowing how to wire a "delta monitor" into your fine-tuning pipeline as a quiet CI gate. Based on my peer-reviewed paper accepted at IJCNN.

Speakers:
- Sachin Kumar (LexisNexis): Sachin Kumar is a Senior Data Scientist III and Tech Lead at LexisNexis, building agentic AI for the legal domain. His independent AI-safety and interpretability research has been accepted at top-tier venues including ACL, AAAI, and IJCNN.
  LinkedIn: https://www.linkedin.com/in/techsachinkumar/
  GitHub: https://github.com/techsachinkr

## Building an ACP-Compatible Agent Live — Bennet Fenner, Zed

- Upload date: 2026-07-08
- Video: https://www.youtube.com/watch?v=HsxQICTLF84
- Transcript: raw/20260708_HsxQICTLF84/HsxQICTLF84.en-orig.vtt
- Metadata: raw/20260708_HsxQICTLF84/HsxQICTLF84.info.json

In this session, we'll be building a coding agent that implements ACP — covering protocol design, session lifecycle management, and handling tool calls. The session ends with a live demo of the finished agent running inside Zed, showing what ACP looks like in practice from both sides of the protocol.

## Teaching Coding Agents to do Spreadsheets - Nuno Campos, Witan Labs

- Upload date: 2026-07-08
- Video: https://www.youtube.com/watch?v=HEFSExa0xl0
- Transcript: raw/20260708_HEFSExa0xl0/HEFSExa0xl0.en-orig.vtt
- Metadata: raw/20260708_HEFSExa0xl0/HEFSExa0xl0.info.json

https://github.com/witanlabs/research-log

## Running a Chess YouTube Channel entirely by AI — Stephan Steinfurt, TNG

- Upload date: 2026-07-08
- Video: https://www.youtube.com/watch?v=BqZrTdgBaPw
- Transcript: raw/20260708_BqZrTdgBaPw/BqZrTdgBaPw.en-orig.vtt
- Metadata: raw/20260708_BqZrTdgBaPw/BqZrTdgBaPw.info.json

Daily chess puzzle explanations on YouTube: Our agent analyzes and describes chess puzzles in an accessible way - arrows included!

## I Run a Fleet of AI Agents Across Three Machines. Here's What Broke. - Kyle Jaejun Lee, KRAFTON

- Upload date: 2026-07-08
- Video: https://www.youtube.com/watch?v=4kYl2_mqmnQ
- Transcript: raw/20260708_4kYl2_mqmnQ/4kYl2_mqmnQ.en-orig.vtt
- Metadata: raw/20260708_4kYl2_mqmnQ/4kYl2_mqmnQ.info.json

An honest field report from my own personal fleet of AI agents, run across several machines as a daily driver. Less about any single tool, more about the journey: how things that work on one machine break once you scale to many, what it takes to keep a setup like this running, and where it's all converging. Not a company platform — just real, evolving lessons from running it myself.

Speakers:
- Kyle Jaejun Lee (KRAFTON): Kyle is a builder and AI Platform Engineer working to make AI agents first-class citizens in the workplace
  X/Twitter: https://x.com/kyleleee_119
  LinkedIn: https://www.linkedin.com/in/jjlee-swe/
  GitHub: https://github.com/cooco119

## Beyond the Harness: A Journey Towards Adaptative Engineering - Rajiv Chandegra, Annicha Labs

- Upload date: 2026-07-07
- Video: https://www.youtube.com/watch?v=qdZzND79mcg
- Transcript: raw/20260707_qdZzND79mcg/qdZzND79mcg.en-orig.vtt
- Metadata: raw/20260707_qdZzND79mcg/qdZzND79mcg.info.json

Building products has been commoditised. As AI models grow more capable, the real opportunity shifts to the hard problems — the big, messy, tangled challenges of the physical and social world. That, after all, is the engineer's true job: to solve problems.

But our current paradigm leans on fixed harnesses - predetermined structures imposed on the problem. In a world of complex, shifting systems, that rigidity becomes a liability. We need harnesses that adapt in real time, the way a great leader reads and responds to a changing team. This is adaptive engineering, and it is where the next frontier lies.
This talk traces the limits of today's engineering paradigm, draws on complexity science to examine how complex systems behave in the natural and social world, and explores the philosophy and practice of adaptive engineering as what comes next.

Speakers:
- Rajiv Chandegra (Annicha Labs): Rajiv is a practicing medical doctor and director of Annicha Labs - a firm dedicated to exploring the application of technology for complex challenges in the real world.
  X/Twitter: @rajivchandegra
  LinkedIn: https://www.linkedin.com/in/rajivchandegra/

## The Pipeline Is Dead - Iris ten Teije, Sky Valley Ambient Computing

- Upload date: 2026-07-07
- Video: https://www.youtube.com/watch?v=bRnoEpoK5m4
- Transcript: raw/20260707_bRnoEpoK5m4/bRnoEpoK5m4.en-orig.vtt
- Metadata: raw/20260707_bRnoEpoK5m4/bRnoEpoK5m4.info.json

The entire software distribution stack assumes one version of your software, the same for everyone. It was the only thing we could afford when producing a change was expensive. Now it's nearly free, and it can happen at runtime, on the client, in the user's session, so the line between distribution and development is dissolving. This talk is about the infrastructure that has to catch up: where truth lives when every user runs a different version, how you debug a program that exists for one person, and why a million per-user versions can be more contained than the single tangled codebase you run today. Real architectural decisions, the tradeoffs that don't have clean answers yet, and what we're learning at the frontier.

Speakers:
- Iris ten Teije (Sky Valley Ambient Computing): Iris ten Teije is a serial entrepreneur currently building Differ: infrastructure for adaptive software.
  X/Twitter: x.com/iristenteije
  LinkedIn: http://linkedin.com/in/iristenteije

## 500 people vibe-coded for 30 days. I was one of them. - Sanja Grbic, Automattic

- Upload date: 2026-07-07
- Video: https://www.youtube.com/watch?v=UcYoMg-8-L8
- Transcript: raw/20260707_UcYoMg-8-L8/UcYoMg-8-L8.en-orig.vtt
- Metadata: raw/20260707_UcYoMg-8-L8/UcYoMg-8-L8.info.json

Automattic, the company behind WordPress.com, ran a 30-day experiment called Radical Speed Month: pause the roadmap, and see how fast real software could ship. I am a product Designer and I shipped three products that month. I'll share what each one revealed about a new kind of collaboration between designers and engineers and how teams are unlocked when bottlenecks disappear.

Speakers:
- Sanja Grbic (Automattic): Sanja is a product designer based in San Francisco, with over a decade of experience, focused on turning complex technology into simple, inspiring solutions.
  X/Twitter: https://x.com/_dream_stellar
  LinkedIn: https://www.linkedin.com/in/sanjagrbic/

## SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale - Rishi Desai, Abundant AI

- Upload date: 2026-07-07
- Video: https://www.youtube.com/watch?v=Rx8f05JI_WA
- Transcript: raw/20260707_Rx8f05JI_WA/Rx8f05JI_WA.en-orig.vtt
- Metadata: raw/20260707_Rx8f05JI_WA/Rx8f05JI_WA.info.json

SWE-Marathon is a benchmark for long-horizon autonomous software work: 20 project-scale tasks spanning product clones, library rewrites, and ML engineering. We discuss what happens when coding agents run for tens to hundreds of millions of tokens, why full-stack evals need computer-use verifiers, and why reward-hacking resistance is now central to benchmark design.

Speakers:
- Rishi Desai (Abundant AI): Rishi Desai is an ML Engineer at Abundant AI, where he works on RL environments and SWE benchmarks for coding agents.
  X/Twitter: https://x.com/rishi_desai2
  LinkedIn: https://www.linkedin.com/in/rishi-desai1/
  GitHub: https://github.com/RishiDesai

## GTM Is You - Victoria Melnikova, Evil Martians

- Upload date: 2026-07-07
- Video: https://www.youtube.com/watch?v=G6IlDzj8OjA
- Transcript: raw/20260707_G6IlDzj8OjA/G6IlDzj8OjA.en-orig.vtt
- Metadata: raw/20260707_G6IlDzj8OjA/G6IlDzj8OjA.info.json

In this talk, Victoria Melnikova revisits interviews with successful developer tool founders (Sam Lambert, David Cramer, Paul Copplestone, Ivan Burazin, Zeno Rocha, Jason Bosco) in San Francisco to derive optimal Go-To-Market tactics for developer tools and AI startups focusing on personal brand.

Speakers:
- Victoria Melnikova (Evil Martians): Victoria run new business at Evil Martians and hosts Dev Propulsion Labs podcast
  X/Twitter: https://x.com/vmelnikova_en
  LinkedIn: https://www.linkedin.com/in/vmelnikova/
  GitHub: https://github.com/vicamelnikova

## Respect The Process - Andrew Dumit, Watershed Technology Inc.

- Upload date: 2026-07-07
- Video: https://www.youtube.com/watch?v=CLttOU7n6sI
- Transcript: raw/20260707_CLttOU7n6sI/CLttOU7n6sI.en-orig.vtt
- Metadata: raw/20260707_CLttOU7n6sI/CLttOU7n6sI.info.json

In sustainability, the answer to almost every question is "it depends." What’s the right classification? Which method should the agent use? Our vertical is filled with judgement calls broadly and one of the tasks in that vertical might span a search over 100k’s of data-rich nodes and hundreds of edits. Editing across them takes loops and filters, not enumerated tool calls. Code is the only thing that scales to the task. But in a domain that relies heavily on judgement and implicit knowledge, there are many ways for a model to get the right answer with the wrong reasoning and many right answers for it to come to.

Over time, we’ve upgraded models, but a smarter model didn’t fix this. Instead we built a domain-specific coding harness, applying best practices from general coding agents (linting, routing failures back, sub-tasking), and constraining how it commits through a well-defined SDK and owning the final execution. It keeps the full power of a modern coding agent, but every change must pass through our deterministic, typed interface.

Within that constraint, we harness-engineered our way from 43% to 92% accuracy. The interesting part is the other 8%: even when the agent lands on a different answer than our reference, every change it makes is still valid, traceable, and replayable. We'll cover how we built it, what we chose to constrain vs. what we leave free.

Speakers:
- Andrew Dumit (Watershed Technology Inc.): Andrew works on AI engineering at Watershed, building systems to manage and reduce the emissions of everything companies buy and sell.
  LinkedIn: https://www.linkedin.com/in/adumit
  GitHub: https://github.com/adumit

## Build AI Systems for Discernment, Not Approval - Angel Ortmann Lee, Duolingo

- Upload date: 2026-07-07
- Video: https://www.youtube.com/watch?v=CDqzWpwkSls
- Transcript: raw/20260707_CDqzWpwkSls/CDqzWpwkSls.en-orig.vtt
- Metadata: raw/20260707_CDqzWpwkSls/CDqzWpwkSls.info.json

The human-in-the-loop paradigm promises automation's efficiency without sacrificing safety or nuance. But it hides an underexamined assumption: that human involvement produces genuine discernment, not just a rubber stamp. In practice, human-AI interaction often occurs in environments where throughput or business incentives crowd out critical thinking. This talk examines why human oversight so often falls short in practice, and how deliberate interaction design can close the gap.

We've grown comfortable delegating reasoning to machines. We follow GPS down unfamiliar streets and accept AI coding suggestions with minimal inspection. When Shaw & Nave (Wharton, 2026) studied human-AI interaction, they found people accepted AI answers over 80% of the time, even when it was wrong. They call this cognitive surrender: when humans forgo deliberation and adopt AI output with minimal scrutiny.

At the Duolingo English Test, a controlled experiment revealed that experienced proctors shown fabricated AI cheating alerts confirmed cheating at near-chance rates. But coin-flip accuracy is unacceptable when college admissions and visas are on the line. 

The model wasn't the problem, the signals were fake. But skilled reviewers were still showing systematic confirmation bias. A single change to decision framing improved accurate rejections by 21%.

The fix isn't better models or more human oversight. It's engineering the interaction itself. What reasoning patterns do you need from the human, and how does the interface elicit them? This talk covers practical design principles for building AI systems that improve human judgment, produce more reliable review behavior, and generate higher-quality training data. Every AI system trains its users, the question is whether you're doing it deliberately.

Speakers:
- Angel Ortmann Lee (Duolingo): Angel is a Software Engineer at Duolingo, building AI security systems for the Duolingo English Test to help ensure online testing is secure, trustworthy, and accessible for learners around the world.
  LinkedIn: https://www.linkedin.com/in/angel-ortmann-lee-7494b9201

## What if the harness mattered more than the model? - Aditya Bhargava, Etsy

- Upload date: 2026-07-07
- Video: https://www.youtube.com/watch?v=2e9ANoOEn28
- Transcript: raw/20260707_2e9ANoOEn28/2e9ANoOEn28.en-orig.vtt
- Metadata: raw/20260707_2e9ANoOEn28/2e9ANoOEn28.info.json

The models are getting so good now that all you need is a simple harness, some tools, and a loop... right? Aditya Bhargava argues that this direction promotes overreliance on large, proprietary models, and we should be focusing on building harnesses that improve the performance of models that can be run locally.

Speakers:
- Aditya Bhargava (Etsy): Aditya Bhargava is a Staff Engineer and IC Initiative Lead of Agentic Commerce at Etsy.
  GitHub: http://github.com/egonSchiele

## How we taught agents to use good retrieval - Hanna Lichtenberg, Mixedbread AI

- Upload date: 2026-07-07
- Video: https://www.youtube.com/watch?v=1IdzkRVmWAA
- Transcript: raw/20260707_1IdzkRVmWAA/1IdzkRVmWAA.en-orig.vtt
- Metadata: raw/20260707_1IdzkRVmWAA/1IdzkRVmWAA.info.json

RAG is dead. Again. Vector search is useless. All you need is BM25. Not even BM25, all you need is grep. Or maybe even just cat+ls. If you care at all about agents, you probably read a variation of this as part of your daily routine. In a way, isn't it true that semantic search is full of failure cases?
And yet, in all sorts of knowledge tasks, whether it be Deep Research, financial analysis or legal research, grep does not seem to cut it. The Oracle Gap, the performance difference between perfect retrieval and grep-based retrieval, is well into the double digits percents.
In practice, this means that your agent fails to surface that one hidden clause in that 187 pages contract. Or it doesn't properly notice that Q4 results were amended. In the end, this means that a human has to re-do all of its work, erasing all benefits. But if keyword search does not work, and semantic search is dead, then what is the way out?
We argue that the reason for the impressive performance on simple, lexical search methods is simply because models were never taught to use better tools. When using weak tools, they run into the limits of these tools. When provided with better search, they write queries for the weak tools they know, and semantic search fails as a result.
Join us for this session to hear about how we are addressing this problem, co-designing agents with state-of-the-art retrieval tools to teach them that they have more than one tool in their best.

Speakers:
- Hanna Lichtenberg (Mixedbread AI): Hanna is an AI Engineer at Mixedbread, working on agentic retrieval research and agent infrastructure.
  X/Twitter: https://x.com/hannaLicht
  LinkedIn: https://www.linkedin.com/in/hanna-lichtenberg-64778b221/
  GitHub: https://github.com/HannaLicht

## Field Guide to Fable — Thariq Shihipar, Anthropic

- Upload date: 2026-07-06
- Video: https://www.youtube.com/watch?v=9fubhllmsBU
- Transcript: raw/20260706_9fubhllmsBU/9fubhllmsBU.en-orig.vtt
- Metadata: raw/20260706_9fubhllmsBU/9fubhllmsBU.info.json

Ask a chat model which Pokemon names end in aw and it fails, even though it knows every Pokemon by heart. Ask Claude Code and it writes a script, fetches the list, and filters for the answer in seconds. Thariq Shihipar, who works on Claude Code at Anthropic, calls that gap capability overhang: models get smarter in spiky ways, and the tools you give them decide which spikes you can reach.

Thariq covers what it takes to work with Fable, Anthropic's newest model. Claude Code cut 80 percent of its system prompt, since heavy instructions now constrain a model more imaginative than the examples it's given. The ask user question tool went from barely working under Opus 4 to generating embedded HTML questionnaires under Fable. He built a full keynote deck in four hours with it, and argues teams should stop picking two of good, fast, and cheap and start demanding all three.


Speaker info:
- https://x.com/trq212/

Timestamps:
0:00 Introduction and setting the stage for Fable
2:32 Unhobbling Claude: Understanding model behavior
9:08 Finding your unknowns: Navigating the gap between map and territory
14:29 Reflecting on the emotional shift in coding productivity
16:30 Being unreasonable: Demanding good, fast, and cheap results

## MCP Apps: Primitives, discovery, and the Future of Software - Pietro Zullo, Manufact, Inc

- Upload date: 2026-07-05
- Video: https://www.youtube.com/watch?v=sAOBXCDiDOs
- Transcript: raw/20260705_sAOBXCDiDOs/sAOBXCDiDOs.en-orig.vtt
- Metadata: raw/20260705_sAOBXCDiDOs/sAOBXCDiDOs.info.json

Everyone in this room knows what MCP is, but I am sure not many people know what MCP Apps are, how they work, how to build them and distribute them. By the end of this talk you'll know everything you need to join the race!

MCP Apps are not just MCP servers with a UI bolted on. They're a full interaction layer: bidirectional, stateful, rendered by the host, with the model and the UI sharing live context.

This talk is structured around

**What MCP Apps actually are.** The architecture: how an App is declared via `ui://` resources, how the host renders it in a sandboxed iframe, how the JSON-RPC-over-postMessage transport works, and how state flows between the model and the UI.

**The primitives that make them real.** `ui/update-model-context`, the App pushing live state into the model's context window without a user message. `ui/message`, the App talking back into the conversation unprompted. App Tools, the model calling into the App's registered tool surface.

**A showcase of MCP Apps shipping today.** Concrete demos, not slides about what's possible. What early builders have figured out, what's hard, and what the interaction patterns look like in practice.

**Distribution and discovery.** How the stores work, how to submit, what the surface looks like across hosts, and what the install/discovery UX actually means for builders.

**Why companies will need to move** Any product that is used by humans through a UI will need an MCP App version, or it gets bypassed by all the people that are getting more and more used to do everything through agents.

As long as there are people using these systems, MCP Apps is the answer. For the rest, there is MCP.

Speakers:
- Pietro Zullo (Manufact, Inc): Pietro is the co-founder of Manufact (YC S25). Manufact created and maintains mcp-use, an MCP framework with more than 8M downloads across PyPI and npm, one of the leading MCP development frameworks today. Manufact is the cloud for MCP. You can think of Manufact / mcp-use as Vercel / Next.js, but vertical on MCP Apps and servers.
  X/Twitter: https://x.com/pietrozullo
  LinkedIn: https://www.linkedin.com/in/pietrozullo/
  GitHub: https://github.com/pietrozullo

## The Missing Layer After Launch - Raphael Kalandadze, Wandero AI

- Upload date: 2026-07-05
- Video: https://www.youtube.com/watch?v=kZsf_Sfm7RU
- Transcript: raw/20260705_kZsf_Sfm7RU/kZsf_Sfm7RU.en-orig.vtt
- Metadata: raw/20260705_kZsf_Sfm7RU/kZsf_Sfm7RU.info.json

We run a production system of agents for real customers. The team that keeps it healthy is also made of agents.

Operating an agent product isn't like operating software. When our agent fails a customer — a dropped constraint, a stale price, a confident wrong answer — nothing crashes and no log lights up. The failure is in the conversation, not the stack trace. So we put agents on the operations:

- One monitors production conversations and judges where the agent actually let a customer down — across thousands of live sessions, not a sampled few.
- One watches logs and system health and traces real problems back into the code.
- One writes and runs tests, because "green CI" means nothing for a non-deterministic agent.
- One reviews every PR — human or agent-authored — against a single question: root cause, or just the symptom?

Humans stay at the merge and approval boundaries. The agents do the watching, judging, testing, and drafting that no human team could keep up with at this volume.

This talk is the honest version: what each operating agent actually checks, where we trust it and where we don't, what breaks, and why operating an agent system is becoming its own engineering discipline — done, increasingly, by agents.

Speakers:
- Raphael Kalandadze (Wandero AI): Co-founder and CTO of Wandero AI, an agent-native operating system for travel and hospitality, and co-founder of Tbilisi AI Lab, where we build the first Georgian large language model.
  X/Twitter: @RaphaelKalan
  LinkedIn: https://www.linkedin.com/in/rapael-kalandadze/
  GitHub: https://github.com/RRaphaellRaphaelKalan

## Your AI Product Will Fail Unless You Can Explain It - Veronica Hylak, Hey AI

- Upload date: 2026-07-05
- Video: https://www.youtube.com/watch?v=d_Ftrl3vfV0
- Transcript: raw/20260705_d_Ftrl3vfV0/d_Ftrl3vfV0.en-orig.vtt
- Metadata: raw/20260705_d_Ftrl3vfV0/d_Ftrl3vfV0.info.json

You’re shipping faster than ever, but still can’t quickly answer: "Why does this matter to an average user?"

A decade ago, the market would find you. Now, if people can't instantly understand what your AI product does, you’re in trouble.

That communication gap has become fatal. This talk? Your emergency hotline.

With 7M views helping complex AI systems make sense to everyday people, and direct work with YC startups, AI tools, and safety organizations across SF, Veronica Hylak shares how technical founders can turn products into stories people instantly understand, remember, and want to buy.

You’re shipping faster than ever, but still can’t quickly answer: "Why does this matter to an average user?"

A decade ago, the market would find you. Now, if people can't instantly understand what your AI product does, you’re in trouble.

That communication gap has become fatal. This talk? Your emergency hotline.

With 8M views helping complex AI systems make sense to everyday people, and direct work with YC startups, AI tools, and safety organizations across SF, Veronica Hylak shares how technical founders can turn products into stories people instantly understand, remember, and want to buy.

Speakers:
- Veronica Hylak (Hey AI): Veronica Hylak is an AI product leader with 10 years in tech (including six in AI beginning with autonomous military ships), and a YouTuber whose explainers have reached over 8 million people.
  LinkedIn: https://www.linkedin.com/in/veronica-hylak-8b629a86/

## Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI

- Upload date: 2026-07-05
- Video: https://www.youtube.com/watch?v=2IxD9OB3XuQ
- Transcript: raw/20260705_2IxD9OB3XuQ/2IxD9OB3XuQ.en-orig.vtt
- Metadata: raw/20260705_2IxD9OB3XuQ/2IxD9OB3XuQ.info.json

Agents fail in production in ways that static benchmarks cannot fully capture. The key question is whether they can learn from those experiences without drifting or breaking prior capabilities.

This talk introduces verifiable continual learning for AI agents: a framework for converting traces, failures, and feedback into testable, regression-aware improvements. I will discuss four core requirements: turning failures into replayable learning environments, preserving prior capabilities during updates, routing repairs to the right layer of the agent stack, and keeping the learning loop efficient enough to run continuously.

We will use these principles to examine today’s approaches, including prompt optimizers, memory consolidation, coding-agent harness repair, and trace-to-harness systems. I will then discuss the remaining gap: a holistic, lifelong, verifiable learning loop with online regression control.

Speakers:
- Soheil Feizi (RELAI): Dr. Soheil Feizi is the Founder and CSO of RELAI and an Associate Professor of Computer Science at the University of Maryland, College Park, whose work focuses on the reliability, safety, and optimization of AI systems.
  X/Twitter: https://x.com/FeiziSoheil
  LinkedIn: https://www.linkedin.com/in/soheil-feizi-b14a4895/

## The Prompt Is Still a Punch Card - Ted Johnson, JoinIn AI

- Upload date: 2026-07-02
- Video: https://www.youtube.com/watch?v=hVJOnuhFmTA
- Transcript: raw/20260702_hVJOnuhFmTA/hVJOnuhFmTA.en-orig.vtt
- Metadata: raw/20260702_hVJOnuhFmTA/hVJOnuhFmTA.info.json

Interfaces outlive their constraints. The keyboard, command line, mouse, menus, forms, voice assistants, and even prompts were all brilliant compromises with the machines of their time.

But AI gives us a chance to renegotiate that bargain.

This talk reframes AI as an interface technology, not only an intelligence technology. We will trace a pattern across computing history: humans repeatedly learn the machine’s protocol, from punching cards to writing commands to engineering prompts. Then we will ask what changes when computers can reason, listen, speak, infer, clarify, and adapt.

The next frontier is not just better models or better voices. It is more human-compatible interfaces: systems that understand timing, attention, interruption, ambiguity, repair, shared context, and when to stay silent.

Speakers:
- Ted Johnson (JoinIn AI): Ted Johnson is an executive, enterprise architect, and co-founder of JoinIn.AI, focused on AI-powered collaboration, enterprise architecture, cloud strategy, and technology transformation.
  LinkedIn: https://linkedin.com/in/johnsontedm
  GitHub: https://github.com/JoinIn-AI/

## The Future Is Domain-Specific Agents - Justin Schroeder, StandardAgents

- Upload date: 2026-06-29
- Video: https://www.youtube.com/watch?v=spNAUEgq_A8
- Transcript: raw/20260629_spNAUEgq_A8/spNAUEgq_A8.en-orig.vtt
- Metadata: raw/20260629_spNAUEgq_A8/spNAUEgq_A8.info.json

“Composition over inheritance” has always been a good engineering rule. It may also be the unlock for useful AI. A Gmail agent is fundamentally more powerful than a Gmail skill — and when composed with Sheets, Notion, and GitHub agents, the system gets more capable, more reliable, and cheaper to run. Suddenly, smaller models can do real work, and AI can move from internal copilots to customer-facing products. In this talk, we’ll unpack why this architecture hasn’t become the default yet, what’s been missing, and how to start building toward it today.

Speakers:
- Justin Schroeder (StandardAgents): Co-founder of StandardAgents. Compulsive open source builder. Creator of dmux, ArrowJS, FormKit, AutoAnimate, Tempo, zodown
  X/Twitter: https://x.com/jpschroeder
  LinkedIn: https://www.linkedin.com/in/jpschroeder/
  GitHub: https://github.com/justin-schroeder

## The Agentic AI Engineer - Benedikt Sanftl, Mutagent

- Upload date: 2026-06-29
- Video: https://www.youtube.com/watch?v=pSto5YaNGUo
- Transcript: raw/20260629_pSto5YaNGUo/pSto5YaNGUo.en-orig.vtt
- Metadata: raw/20260629_pSto5YaNGUo/pSto5YaNGUo.info.json

In this video we introduce the concept of the agentic ai engineer. similar to coding agent loops for agents we build a system that build AI Agents in an Eval-Driven Developement Loop. The Agentic AI Enginner is a collection of a multi-agent team, steared by an orchestrator and combines, spec, build, evaluate, diagnose, monitor, optimse. We round up the talk with a live demo from one of our agents in research preview.

Speakers:
- Benedikt Sanftl (Mutagent): Bene is the CEO and Co-Founder of Mutagent. The platform for Agentic AI Engineering.
  LinkedIn: https://www.linkedin.com/in/benedikt-sanftl-294a6039a/

## Frontier results, on device - RL Nabors, Arize

- Upload date: 2026-06-29
- Video: https://www.youtube.com/watch?v=fWXJM-J0ZB8
- Transcript: raw/20260629_fWXJM-J0ZB8/fWXJM-J0ZB8.en-orig.vtt
- Metadata: raw/20260629_fWXJM-J0ZB8/fWXJM-J0ZB8.info.json

Most of use reach for a frontier model by default and pay for it on every call, in latency, in energy, in cash, and in everything that leaves their stack. For most of those calls, a small local model would do the job. 

RL Nabors, former Meta/React core team member and AWS alum, covers the vocabulary you need to reason about model performance (capability evals, golden datasets, LLM-as-judge) and walks through real cases: a local agentic harness replacing a frontier call, an in-browser moderation classifier defended with production-trace evals, and a generative summarization feature where the rubric turns out to be harder than the model. You'll leave with a framework for deciding when to choose large and off-prem or small and local models, and how to measure your way to the answer instead of guessing.

You will learn:

- The vocabulary to reason about model performance (capability evals, golden datasets, LLM-as-judge).
- A framework for deciding when a small or local model can replace a frontier one and when it can't.
- A repeatable process for building capability evals from your own production traces, not someone else's benchmark.
- Working examples of using eval results to iterate on prompts and ship with confidence instead of vibes.

Speakers:
- RL Nabors (Arize): RL Nabors builds developer tools and the communities that make them stick. Previously React and MDN, currently developer experience at Arize, perpetually building Mima.
  X/Twitter: https://x.com/rachelnabors
  LinkedIn: https://linkedin.com/in/nearestnabors
  GitHub: https://linkedin.com/in/nearestnabors

## Building Great Agent Skills: The Missing Manual

- Upload date: 2026-06-29
- Video: https://www.youtube.com/watch?v=UNzCG3lw6O0
- Transcript: raw/20260629_UNzCG3lw6O0/UNzCG3lw6O0.en-orig.vtt
- Metadata: raw/20260629_UNzCG3lw6O0/UNzCG3lw6O0.info.json

Let's discuss how to navigate "skill hell" by providing a structured framework for building high-quality agent skills. Without a shared rubric, developers and organizations struggle to create effective, maintainable skills for AI agents.

Timestamps:

0:00 - Introduction to the talk and the concept of "skill hell"
2:12 - Overview of the skill checklist framework
3:16 - Trigger: Choosing between user-invoked and model-invoked skills
7:29 - Structure: Organizing steps and references
9:00 - Making the skill.md file minimal
11:54 - Steering: Using leading words to guide agent behavior
14:56 - Increasing "leg work" per step
16:48 - Pruning: Removing sediment, crud, and no-ops
19:06 - Final summary of the checklist framework
19:55 - Where to find the "writing great skills" resource

The Skill Checklist Framework:

Trigger (3:16 - 7:25): Decide whether a skill should be user-invoked or model-invoked. Matt notes that while model-invoked skills offer more flexibility, they increase context load and introduce unpredictability. User-invoked skills offer more control but require greater cognitive load from the pilot.

Structure (7:29 - 11:53): Organize your skill into two primary units: steps (procedures) and reference (supporting information). To keep the skill.md file minimal, move branching reference material behind context pointers to reduce bloat and maintenance costs.

Steering (11:54 - 16:47): Use leading words—specific terms that pack dense meaning—to influence agent behavior and guide reasoning traces. Additionally, you can force the agent to perform more "leg work" on specific tasks by breaking complex processes into smaller, individual skills that hide future steps.

Pruning (16:48 - 19:05): Maintain a clean skill set by ensuring a single source of truth, removing "sediment" (irrelevant legacy material), and eliminating "no-ops" (instructions that don't actually change agent behavior).

https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-great-skills/SKILL.md

## Using RL Agent to Detect and Remediate ETL Pipeline Failures - Anna Marie Benzon

- Upload date: 2026-06-29
- Video: https://www.youtube.com/watch?v=LrGCT7G_rU8
- Transcript: No transcript file found
- Metadata: raw/20260629_LrGCT7G_rU8/LrGCT7G_rU8.info.json

Cloud ETL failures often require engineers to manually inspect logs, diagnose schema or data-quality issues, select a repair, rerun the job, and validate recovery. This talk presents an RL-guided pipeline health agent that automates this workflow through deterministic anomaly detection, interpretable Q-learning, bounded remediation actions, and an external safety layer.
The system detects schema drift, null-rate spikes, type changes, and runtime failures, then selects actions such as retry, schema coercion, rollback, quarantine, or escalation. Evaluation across 30 controlled synthetic runs demonstrates minutes-scale recovery for successfully resolved cases while highlighting the importance of deterministic rules and safety guardrails.

Speakers:
- Anna Marie Benzon: Anna Marie Benzon is a World Economic Forum–recognized technology leader, startup founder, and PhD researcher in AI with 9+ years of experience building AI-powered products and scaling multidisciplinary teams.
  LinkedIn: https://www.linkedin.com/in/anna-marie-benzon
  GitHub: https://github.com/ambenzon27

## Your Agent Failed in Prod. Good Luck Reproducing It. - Tisha Chawla & Susheem Koul, Microsoft

- Upload date: 2026-06-29
- Video: https://www.youtube.com/watch?v=Lc8zRh9muoY
- Transcript: raw/20260629_Lc8zRh9muoY/Lc8zRh9muoY.en-orig.vtt
- Metadata: raw/20260629_Lc8zRh9muoY/Lc8zRh9muoY.info.json

When an autonomous agent fails in production and corrupts an enterprise data record, it rarely repeats the exact same execution trajectory twice. Standard application logs reveal what broke but completely fail to explain why, leaving platform teams unable to reproduce non-deterministic failures on demand. While durable execution engines excel at keeping an agent loop alive through state recovery, durability is fundamentally distinct from debuggability. State recovery reconstructs the present; it does not allow an engineer to re-enter the precise historical run that caused an erratic state mutation.

This session introduces the record and replay pattern for autonomous workflows, bringing the core engineering philosophy behind low level systems tools like Mozilla rr straight into the agent loop. By capturing every model invocation, tool execution payload, memory boundary read, and intermediate state transition into an append only event log, engineers can deterministically replay a failed execution trace for true postmortem root cause analysis. This architectural pattern moves entirely beyond basic API mocking or simple response caching. Attendees will leave this session knowing how to architect a framework agnostic recording layer, identify the exact state mutations required to guarantee replay determinism, understand where this approach complements durable execution architectures, and learn how to transform an unreproducible production anomaly into an execution path they can step through line by line.

Speakers:
- Tisha Chawla (Microsoft): Tisha Chawla is a Software Engineer at Microsoft working within the Commerce and Ecosystem Data Platform team, where she builds agentic systems designed to hold up against real production data. Her technical work spans core internal platform initiatives across Spec Driven Development, SRE Agent adoption, and enterprise SWE Agents, focusing on deterministic execution frameworks and agentic software development lifecycles. Alongside her infrastructure work, Tisha is a published researcher with peer reviewed papers in applied machine learning at venues including APNET SIGCOMM and ASONAM. She frequently delivers technical sessions to large engineering audiences across Microsoft, sharing high signal insights on deploying durable, production grade agentic workflows.
  LinkedIn: https://www.linkedin.com/in/tisha-chawla/
  GitHub: https://github.com/tishachawla-jg
- Susheem Koul (Microsoft): ​Susheem Koul is a Software Engineer at Microsoft with over 7 years of experience in product development. Currently, his work is focused on the design and implementation of intelligent, agentic systems. Beyond his professional focus on agentic workflows and multi-agent coordination, he explores the philosophy of learning and software architecture through his Substack
  LinkedIn: https://www.linkedin.com/in/susheemkoul/
  GitHub: https://github.com/susheem-k

## The Prompt is the Platform - Dominik Tornow, Resonate HQ

- Upload date: 2026-06-29
- Video: https://www.youtube.com/watch?v=DqtmZE6Hl0g
- Transcript: raw/20260629_DqtmZE6Hl0g/DqtmZE6Hl0g.en-orig.vtt
- Metadata: raw/20260629_DqtmZE6Hl0g/DqtmZE6Hl0g.info.json

Coding agents challenge long-standing software engineering practices. Instead of using general-purpose libraries, frameworks, or platforms, agents synthesize bespoke systems on demand. In this talk, I'll show where agents fail, where agents succeed, and the workflow for making the specification the product and the prompt the platform.

Speakers:
- Dominik Tornow (Resonate HQ, Inc): Dominik Tornow is the founder and CEO of Resonate and the author of Think Distributed Systems. He has spent more than 20 years designing and building distributed systems and now focuses on agentic engineering, formal modeling, and formal verification.
  X/Twitter: https://x.com/DominikTornow
  LinkedIn: https://www.linkedin.com/in/dtornow/
  GitHub: https://github.com/dtornow

## Deterministic Infra for Non-Deterministic AI Agents - Nishant Gupta, Meta Superintelligence Labs

- Upload date: 2026-06-29
- Video: https://www.youtube.com/watch?v=APh1Vx0oLmQ
- Transcript: raw/20260629_APh1Vx0oLmQ/APh1Vx0oLmQ.en-orig.vtt
- Metadata: raw/20260629_APh1Vx0oLmQ/APh1Vx0oLmQ.info.json

AI agents are rapidly evolving from copilots into autonomous systems capable of reasoning, invoking tools, coordinating workflows, and interacting with production infrastructure. But most platforms today were designed for deterministic microservices — not long-running, non-deterministic systems powered by LLMs.

This creates a massive infrastructure gap.

In this talk, I’ll share lessons from building large-scale agentic and elastic compute infrastructure powering production AI workloads. We’ll explore the emerging “control plane” required for reliable AI agents: orchestration, observability, retries, evaluation, safety guardrails, workload isolation, memory coordination, and operational control loops.

Topics include:

- Why most AI agents fail outside demos
- Building deterministic systems around stochastic models
- Observability for autonomous AI workflows
- Failure handling and retry storms in agent systems
- Human oversight and safety guardrails
- Elastic GPU infrastructure for agentic workloads
- Reliability patterns for production AI systems
- The shift from “prompt engineering” to “systems engineering”

Attendees will leave with practical architectural patterns for building resilient AI infrastructure capable of supporting autonomous systems safely and efficiently in production.

Speakers:
- Nishant Gupta (Meta Superintelligence Labs): Nishant Gupta is a Software Engineering Tech Lead at Meta Superintelligence Labs building the training and inference AI infrastructure.
  LinkedIn: https://www.linkedin.com/in/nishantgupta-ai/
  GitHub: https://github.com/nishantgpt-lab

## You Can't Prompt the Room: The Last Skill AI Won't Replace - Balázs Horváth, VisualLabs

- Upload date: 2026-06-29
- Video: https://www.youtube.com/watch?v=6bmM45jkMDY
- Transcript: raw/20260629_6bmM45jkMDY/6bmM45jkMDY.en-orig.vtt
- Metadata: raw/20260629_6bmM45jkMDY/6bmM45jkMDY.info.json

Writing code is no longer the bottleneck. With AI generating specifications, tests, and entire implementations on demand, the expensive part of the software development lifecycle has shifted upstream to the people work. Getting the right stakeholders into the room, eliciting the real requirements, and figuring out what is actually worth building.

This talk draws on a VisualLabs internal hackathon where 21 agent ideas were generated and 17 were abandoned, not because of technology limitations, but because they lacked data access, a clear business owner, or any measurable value. The 4 that survived are running in production today. The lesson: AI is optimised to produce the most common answer. Getting from a faster horse to a car requires a human who can read the room, map the process, and name the problem precisely before a single prompt is written.

The session covers three practical tools for doing exactly that: story mapping for capturing process backbone and user stories at the right altitude; the 4-question value framework (whose problem, what winning looks like, what would cause refusal, what decision it changes); and the VAD thinking path (Value to Architecture to Design) as the discipline that separates production agents from demo agents. Attendees leave with a concrete shift in how they measure delivery: fewer features shipped, more features used more than twice.

Speakers:
- Balázs Horváth (VisualLabs): Balazs Horvath is the founder of VisualLabs, a Budapest-based premium Microsoft Partner, who has spent 13 years bridging business and technology across US and UK ERP and CRM programmes, and now helps enterprise teams ship production AI agents by rebuilding the requirements and story-mapping skills that the AI coding boom has made more important than ever.
  LinkedIn: https://www.linkedin.com/in/balazshorvathd365/

## Building an Autonomous Engineering Org - Angie Jones, Agentic AI Foundation

- Upload date: 2026-06-28
- Video: https://www.youtube.com/watch?v=whue9_YquGA
- Transcript: raw/20260628_whue9_YquGA/whue9_YquGA.en-orig.vtt
- Metadata: raw/20260628_whue9_YquGA/whue9_YquGA.info.json

Nearly every enterprise company has a mandate to convert its existing engineering org into an autonomous one.

Buying the frontier models and tools is not enough. Everything about how we deliver software must change: from design, to development, to deployment.

In this talk, I’ll walk you through the journey of transitioning traditional software engineers into agentic ones, the systems and processes required for their success, and the new challenges agentic engineering introduces for large enterprise companies.

Speakers:
- Angie Jones (Agentic AI Foundation): Angie Jones is the VP of Developer Experience at the Agentic AI Foundation where she guides how agentic systems are designed, implemented, and adopted across the global developer ecosystem.
  X/Twitter: https://x.com/techgirl1908
  GitHub: https://github.com/angiejones

## The 100-Tool Agent Is a Trap - Sohail Shaikh & Ankush Rastogi, Prosodica

- Upload date: 2026-06-28
- Video: https://www.youtube.com/watch?v=vh2VGuQ3zhY
- Transcript: raw/20260628_vh2VGuQ3zhY/vh2VGuQ3zhY.en-orig.vtt
- Metadata: raw/20260628_vh2VGuQ3zhY/vh2VGuQ3zhY.info.json

The common “Fat Agent” architecture loads a large catalog of tools directly into the system prompt. This often creates latency, cost, and reliability problems in production agent systems. As tool schemas take up more of the context window, agents can become slower and more likely to choose the wrong tool.

This session takes a practical look at the Semantic Tool Router pattern, a deterministic layer that reduces the amount of context shown to the model in real time. The talk will share benchmarks across frontier models, including GPT-4o and Gemini 2.0, showing how the number of available tools affects Time-to-First-Token latency and tool-selection accuracy.

Attendees will learn how to move from static tool loading to Just-in-Time Context Injection, where only the most relevant tools are added to the prompt for each request. In high-tool-density benchmark scenarios, this approach can reduce response latency by up to 90%, reduce cross-tool confusion, and improve agent reliability. The session will end with a practical framework for building tool routers that can scale to hundreds of capabilities without sacrificing speed or predictability.

Speakers:
- Sohail Shaikh (Prosodica): Sohail Shaikh is a data scientist with nearly a decade of experience across AI, data science, analytics, marketing, and software-oriented work, focused on building practical, reliable, and scalable AI systems using NLP, RAG, conversational intelligence, and LLM workflows.
  LinkedIn: https://www.linkedin.com/in/sohail-shaikh/
  GitHub: https://github.com/Sohail-Sh
- Ankush Rastogi (Prosodica): Ankush Rastogi is a Senior Data Solutions Engineer with over a decade of experience building scalable data, analytics, and machine learning platforms, with a focus on turning AI models into reliable, production-ready enterprise systems through strong evaluation, inference performance, cost optimization, and operational design.
  LinkedIn: https://www.linkedin.com/in/ankushrastogi/
  GitHub: https://github.com/ankushrastogi04

## Your Agent Is Wasting Tokens and You Don't Know It - Erik Hanchett, AWS

- Upload date: 2026-06-28
- Video: https://www.youtube.com/watch?v=uiP88SpCi1Q
- Transcript: raw/20260628_uiP88SpCi1Q/uiP88SpCi1Q.en-orig.vtt
- Metadata: raw/20260628_uiP88SpCi1Q/uiP88SpCi1Q.info.json

I deployed an agent to production and the bill was not good. Not because the model was bad, but because it was doing too much. I was using the most expensive models for simple inference calls. The context was filling up. And my tool loops ran longer than they needed to. The agent worked fine, it just cost way more than it should have.

This talk covers three small changes I made that dropped my costs without hurting quality. Each one was a few lines of code, and none of them required changing my prompts or switching models. I'll cover things like prompt caching and model routing. I'll show code.

Speakers:
- Erik Hanchett (Amazon Web Services): Erik Hanchett is a Developer Advocate at AWS who helps developers build with frontend, fullstack, and AI/agent technologies through hands-on tutorials, talks, and videos.
  X/Twitter: https://x.com/erikch
  LinkedIn: https://www.linkedin.com/in/erikhanchett/
  GitHub: https://github.com/erikch

## We Cut 94% of AI Coding Tokens With a Local Code Index - Rajkumar Sakthivel, Tesco

- Upload date: 2026-06-28
- Video: https://www.youtube.com/watch?v=dRmWYHuIJxM
- Transcript: raw/20260628_dRmWYHuIJxM/dRmWYHuIJxM.en-orig.vtt
- Metadata: raw/20260628_dRmWYHuIJxM/dRmWYHuIJxM.info.json

Every AI coding tool we tried had the same assumption: send as much context as possible.

In our production codebase, that meant sending 45,000 tokens per query — even when only ~5,000 were actually useful. We didn’t notice how inefficient this was until we saw the cost and latency impact.

We tried improving prompts and tweaking model settings, but nothing addressed the core problem:
we were optimising the model, not the context.

So we built a local retrieval layer between the codebase and the agent.

Instead of sending full files, we:

Structured code using AST-aware chunks (tree-sitter)
Combined vector search with keyword matching for better retrieval
Used a lightweight relationship layer to follow execution across files
The result: 👉 94% reduction in tokens
👉 faster responses
👉 more accurate outputs

The hardest problem wasn’t retrieval — it was knowing when retrieval was wrong.
We experimented with LLM-based scoring and threshold tuning, but a simple heuristic ended up working best.

Everything runs locally, with no data leaving the machine, and one index supports multiple AI tools.

In this talk, I’ll walk through:

What we got wrong initially
Why context matters more than model tuning
The architecture behind the system
Real benchmarks and trade-offs
The key takeaway: 👉 The biggest optimisation in AI coding isn’t the model — it’s the context.

Speakers:
- Rajkumar Sakthivel (Tesco): Rajkumar Sakthivel builds LLM infrastructure at scale and co-created Code Context Engine after his team's AI coding bill jumped from £15 to £200 in a single month.
  X/Twitter: https://x.com/rajkumarsakthi
  LinkedIn: https://www.linkedin.com/in/rajkumar-sakthivel/
  GitHub: https://github.com/rajkumarsakthivel

## OpenClaw in Your Hand: Building a Physical AI Terminal - Lech Kalinowski, Callstack

- Upload date: 2026-06-28
- Video: https://www.youtube.com/watch?v=akk6KRlcwW4
- Transcript: raw/20260628_akk6KRlcwW4/akk6KRlcwW4.en-orig.vtt
- Metadata: raw/20260628_akk6KRlcwW4/akk6KRlcwW4.info.json

What if an AI device felt calm — closer to peace than a glowing distraction? Vault is a text-first, dual-display handheld AI terminal built on a single ESP32-S3 and powered by one battery cell. It pairs a fast, emissive OLED "live" surface with a slow, bistable e-paper "content" surface, switches between four modes with a single slash command — shell, assist, control, and an LLM-native RPG — and drives autonomous OpenClaw agents, all against a fully local, self-hosted model (gpt-oss:120b served by NVIDIA TensorRT-LLM). This talk walks the system end to end: an AI-native architecture where the firmware talks to a dependency-free Python backend that dispatches to local models, agents, and a game engine; why inference stays on the backend instead of the microcontroller; and how the device surfaces an agent thinking and calling tools in real time on e-paper. Along the way: the engineering war stories that each cost a day, the LLM-native game design that tracks narrative state instead of HP and dice, and what it actually takes to put a local agent in your pocket.

Speakers:
- Lech Kalinowski (Callstack): Dr. Lech Kalinowski is an AI and data science leader, PhD in Physical Sciences, and startup co-founder specializing in machine learning, AI strategy, printed electronics, and applied innovation.
  X/Twitter: https://x.com/LeSiOO
  LinkedIn: https://www.linkedin.com/in/lech-kalinowski/
  GitHub: https://github.com/lech-kalinowski

## Agents Building Agents - Alfonso Graziano, Nearform

- Upload date: 2026-06-28
- Video: https://www.youtube.com/watch?v=aHhB3sjGjkI
- Transcript: raw/20260628_aHhB3sjGjkI/aHhB3sjGjkI.en-orig.vtt
- Metadata: raw/20260628_aHhB3sjGjkI/aHhB3sjGjkI.info.json

Building an AI agent for a real team is not a prompt problem, it is a systems problem. In this session we walk through a practical, production-minded workflow for building an agent using a coding agent, and designing the codebase so that this loop stays reliable as complexity grows.

The core pattern is two agents with different jobs. The coding agent is the builder: it writes and changes the agent’s codebase. The agent you are building is the product agent. It is the custom agent you ship for a client or for internal use.

A key example is self-healing evals. We maintain an eval suite that exercises the product agent across representative tasks. When an eval fails, the builder agent runs the eval, inspects the failure artifacts, proposes a targeted fix to the correct layer (context, tool contract, or code), and opens a PR with a short report explaining what changed and what is still missing. If the agent cannot safely resolve the failure, it escalates by requesting specific human input and explaining exactly why it is blocked.

Speakers:
- Alfonso Graziano (Nearform): Alfonso is a Software Engineer led by curiosity and passionate about new technologies
  LinkedIn: https://www.linkedin.com/in/alfonso-graziano/
  GitHub: https://github.com/alfonsograziano

## When All Context Matters: Extended Cache Augmented Generation - Luis Romero-Sevilla, Orbis

- Upload date: 2026-06-28
- Video: https://www.youtube.com/watch?v=XovaGv4f39A
- Transcript: raw/20260628_XovaGv4f39A/XovaGv4f39A.en-orig.vtt
- Metadata: raw/20260628_XovaGv4f39A/XovaGv4f39A.info.json

This session addresses a critical challenge in knowledge representation: extracting accurate answers from a rapidly changing dataset where every document is highly interconnected and relevant.

Explore the limitations of standard retrieval methods for dynamic, high-context scenarios—including the constraints of Simple RAG and the computational bottlenecks of constantly recomputing a GraphRAG. To overcome these hurdles, this talk introduces a novel solution: Extended Cache Augmented Generation (ECAG).

Speakers:
- Luis Romero-Sevilla (Orbis Operations): Luis Romero-Sevilla is an AI strategist and full-stack software engineer with over 13 years of experience driving mission-critical technological innovation across defense, healthcare, and the public sector, currently serving as the Vice President of AI at Orbis Operations.
  X/Twitter: https://x.com/lurose15
  LinkedIn: https://www.linkedin.com/in/luis-romero-sevilla/
  GitHub: https://github.com/lurose5

## AI System Design: From Idea to Production - Apoorva Joshi, MongoDB

- Upload date: 2026-06-28
- Video: https://www.youtube.com/watch?v=T0HhO4YtTfE
- Transcript: raw/20260628_T0HhO4YtTfE/T0HhO4YtTfE.en-orig.vtt
- Metadata: raw/20260628_T0HhO4YtTfE/T0HhO4YtTfE.info.json

Writing code is no longer the hard part. AI can do that. In a world where AI writes the code, the most valuable skill an engineer can have is knowing what to build. Most AI systems never make it to production because of bad decisions made earlier in the process. The pressure to ship fast, the hype around AI, and the lack of a structured approach all push engineers toward building before they've thought through what they're building and why.

In this talk, you'll learn a structured framework for making the decisions that get AI systems to production. You'll learn how to identify the business problem, define success metrics, select the right architecture, define guardrails and evaluation metrics, and know what to optimize for when you ship. We'll apply the framework to a real-world problem as we go, so you can see how it works on an actual AI application.

Speakers:
- Apoorva Joshi (MongoDB): Apoorva is currently a Staff AI Developer Advocate at MongoDB. She has a diverse engineering background with a Bachelor’s in Electrical Engineering, a Master’s in Computer Engineering, and several years of experience as a data scientist, applying AI to problems in the cybersecurity space. She now uses that applied AI expertise to help data science and engineering teams at large enterprises and startups build production-grade AI applications with MongoDB and Voyage AI.
  LinkedIn: https://www.linkedin.com/in/apoorvajoshi95/
  GitHub: https://github.com/ajosh0504

## Research to Reality: Bringing Frontier ML Research to Production - Vaidas Razgaitis, Higharc

- Upload date: 2026-06-28
- Video: https://www.youtube.com/watch?v=OXMMN-XbxwA
- Transcript: raw/20260628_OXMMN-XbxwA/OXMMN-XbxwA.en-orig.vtt
- Metadata: raw/20260628_OXMMN-XbxwA/OXMMN-XbxwA.info.json

Three tactical tips to speed up how quickly your R&D team can turn novel research into customer-ready features

Speakers:
- Vaidas Razgaitis (Higharc): Vaidas is a Senior Research Engineer at Higharc, where he specializes in turning frontier ML research into production-grade features.
  X/Twitter: https://x.com/gingiVaidas
  LinkedIn: https://www.linkedin.com/in/vrazgaitis/
  GitHub: https://github.com/VRazgaitis

## User Signal Dies at the Retrieval Boundary - Sonam Pankaj, StarlightSearch

- Upload date: 2026-06-28
- Video: https://www.youtube.com/watch?v=Jx4ZFEAq6bY
- Transcript: raw/20260628_Jx4ZFEAq6bY/Jx4ZFEAq6bY.en-orig.vtt
- Metadata: raw/20260628_Jx4ZFEAq6bY/Jx4ZFEAq6bY.info.json

Utility is all you need! Closing the Agent Learning Loop with Utility-Ranked Memory

Most production agent systems have a fatal flaw: they start every run from a blank slate. You have traces in your observability stack and pass/fail judgments in your eval suite, but the agent that runs tomorrow has no memory of why yesterday's runs succeeded or failed.

This talk exposes the gap between observation and action and shows how to close it.

We'll examine why current memory approaches stall: conversation buffers that only remember recency, semantic systems that retrieve what sounds similar rather than what helped, and reflection-based methods that capture lessons but don't learn which ones actually work. The core idea: utility-ranked memory. Treat memories like a credit score. When a memory is retrieved and the run passes, its utility rises. When the run fails, its utility falls. The ranking formula combines semantic similarity with outcome history. 

There is also a demo with an example of the product SQL agent, of how it updates the context for the right outcome, everything happening at runtime.

Speakers:
- Sonam Pankaj (StarlightSearch Inc): Sonam is the CEO and Co-Founder of StarlightSearch. She is also the co-creator of embedanything, which is a Rust pipeline for RAG, which got contributions from Elastic, Milvus, and Qdrant, and has over 450k+ downloads. Prior to Starlight Search, Sonam spent years in developer tools and AI infrastructure, and has worked as a generative AI Evangelist, GTM lead at Articul8, a spin-off of Intel, and AI Researcher at Saama. She has been presenting talks for the last 10 years, and loves to interact with developers. She has been constantly speaking at Berlin Buzzwords, Europe's largest search conference, PyCon DE, and PyData. She also got an opportunity to present her work at Google, Deutsche Bank, and JetBrains.
  X/Twitter: https://x.com/sonam_pankaj_
  LinkedIn: https://www.linkedin.com/in/sonam-pankaj/
  GitHub: https://github.com/sonam-pankaj95

## Browser Agents Don't Need Better Models. They Need Better Eyes. - Kushan Raj, ARK

- Upload date: 2026-06-28
- Video: https://www.youtube.com/watch?v=JnubYCYunk8
- Transcript: raw/20260628_JnubYCYunk8/JnubYCYunk8.en-orig.vtt
- Metadata: raw/20260628_JnubYCYunk8/JnubYCYunk8.info.json

Every browser agent improvement in the last year has mostly been a model upgrade: better vision, longer context, smarter planning. And they still fail on basic workflows.

Our claim is that the main bottleneck is not the model. It is the interface we give the model to the browser. Three things matter more: what the model sees, what it can do, and what it learns from. We built a browser-agent runtime around all three: a compact page representation instead of a raw dump, fast actions with stable handles instead of one click per call, and step-by-step feedback instead of pass/fail at the end.

In our early runs, changing that interface alone was enough to take the same model from confusion to correct multi-step execution on hostile pages. This talk is the thesis, the evidence, where it still breaks, and why better browser state is a bigger lever than just swapping in a better model.

Speakers:
- Kushan Raj (ARK): Kushan Raj is a Founding ML Engineer at Sarvam AI, where he built the real-time voice AI stack that now powers 2M+ daily calls across 10+ Indian languages
  LinkedIn: https://www.linkedin.com/in/kushanraj/

## HTML is All You Need (for Agents to Make Graphics) - Amol Kapoor, Nori

- Upload date: 2026-06-28
- Video: https://www.youtube.com/watch?v=JRTAtZ5iBkU
- Transcript: raw/20260628_JRTAtZ5iBkU/JRTAtZ5iBkU.en-orig.vtt
- Metadata: raw/20260628_JRTAtZ5iBkU/JRTAtZ5iBkU.info.json

Coding agents are great at writing code. But non-believers will still say things like "these agents aren't really powerful because they have terrible geospatial understanding." ARC-AGI is literally grounded on this premise! And it's true that if you ask Claude or ChatGPT to draw a pelican riding a bike, you get some goofy results. But if you ask me, the problem is the tooling. We build Figma MCPs and Photoshop CLIs and all sorts of things to just get the agent to make a single powerpoint deck. I'm here to tell you that all of that is just user error. Just use HTML. HTML is all you need.

Speakers:
- Amol Kapoor (Nori): Amol is building Nori, the cheapest and most customizable AI employee on the market for any and all dev, ops, and sales automations.
  LinkedIn: https://www.linkedin.com/in/amolkapoor/
  GitHub: http://github.com/theahura/

## AI-Driven Multi-Document Correlation for Financial Compliance - Varsha Shah, Independent

- Upload date: 2026-06-28
- Video: https://www.youtube.com/watch?v=Iwe_RY-fYgI
- Transcript: raw/20260628_Iwe_RY-fYgI/Iwe_RY-fYgI.en-orig.vtt
- Metadata: raw/20260628_Iwe_RY-fYgI/Iwe_RY-fYgI.info.json

Traditional compliance and fraud detection systems analyze financial documents in isolation, making it difficult to identify sophisticated fraud patterns that emerge across multiple enterprise systems. This session presents an AI-driven framework that combines graph-based entity correlation, adaptive probabilistic risk modeling, and cross-jurisdictional normalization to detect hidden compliance risks across payroll, tax, procurement, and financial records. Drawing on an evaluation of approximately three million anonymized records across four jurisdictions, the talk demonstrates how cross-document intelligence can improve fraud detection accuracy, reduce false positives, and lower manual audit effort. Attendees will gain practical insights into building scalable AI solutions that transform enterprise compliance from a reactive validation process into a predictive, intelligence-driven capability.

Speakers:
- Varsha Shah (Independent Researcher): Varsha Shah is a Technical Architect, researcher focused on enterprise AI, agentic systems, intelligent document processing, and AI-powered financial governance.
  LinkedIn: linkedin.com/in/varsha-shah-7b5111247
  GitHub: https://github.com/VarshaShahTech

## Using Spec-Driven Development for Production Workflows - Erik Hanchett, AWS

- Upload date: 2026-06-28
- Video: https://www.youtube.com/watch?v=IddXPepIAS4
- Transcript: raw/20260628_IddXPepIAS4/IddXPepIAS4.en-orig.vtt
- Metadata: raw/20260628_IddXPepIAS4/IddXPepIAS4.info.json

AI coding assistants are great at completing small tasks or features. However, what do you do when you are working with more complex code bases, and you need to build in-depth features that need upfront planning?
This talk explores spec-driven development as a solution to this problem. I'll show you how modern AI coding assistants (like Kiro) can help break down complex tasks into three distinct phases. We'll look at the real-world tradeoffs of this approach, and most importantly and how you can use it in your own projects right away.

Speakers:
- Erik Hanchett (Amazon Web Services): Erik Hanchett is a Senior Developer Advocate at AWS who teaches developers how to build with modern web, AI, and the cloud.
  X/Twitter: https://x.com/erikch
  LinkedIn: https://www.linkedin.com/in/erikhanchett/
  GitHub: https://github.com/erikch

## Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry - Abed Matini, Ogilvy

- Upload date: 2026-06-28
- Video: https://www.youtube.com/watch?v=Akm1sqvWG4A
- Transcript: raw/20260628_Akm1sqvWG4A/Akm1sqvWG4A.en-orig.vtt
- Metadata: raw/20260628_Akm1sqvWG4A/Akm1sqvWG4A.info.json

Building a prototype chatbot interface takes an afternoon, but scaling it into a secure, predictable enterprise app requires solving production infrastructure challenges: minimizing unpredictable cloud API token bills, handling broken layout extractions, mapping session telemetry, and executing deterministic search.

In this practical, demo-driven session, we will bypass high-level wrapper libraries to dissect the complete technical implementation of a local-first document ingestion application. While our demo runs on local developer environments, the underlying design patterns mirror exactly how you build high-performance, cost-effective architectures using enterprise infrastructure like Azure Database for PostgreSQL with pgvector.

Key Architectural Blueprints We Will Explore:

Optimizing the Data Ingest: How parsing documents to clean structural Markdown locally eliminates cloud vision token overhead. We will look at implementing dynamic sidebar toggles to switch into heavy-duty local OCR pipelines when corrupted document font layers are encountered.

Database-First RAG without Framework Bloat: Why heading-based semantic chunking outperforms arbitrary sliding token windows. We will walk through the raw SQL schemas and indexes (HNSW tracking) required to combine dense embedding vectors and sparse keyword text indices natively inside a single database query, using Reciprocal Rank Fusion (RRF) for top-tier retrieval performance.

UX Telemetry and Application Guardrails: A deep dive into injecting live client-side floating widgets to display session telemetry, tracking token limits and cumulative ROI. Finally, we will touch on building a zero-dependency, background-threaded heuristic validation layer (_check_injection()) to scan incoming Markdown text for prompt-injection markers before they hit your persistence layer.

Speakers:
- Abed Matini (Ogilvy): Abed Matini is a software developer and AI engineer focused on practical RAG systems, with a strong emphasis on local and edge LLMs and lightweight production architectures.
  X/Twitter: https://x.com/abedmatini
  LinkedIn: https://www.linkedin.com/in/matini
  GitHub: https://github.com/abedmatini

## Voice In, Visuals Out: The Agony and the Ecstasy - Allen Pike, Forestwalk Labs

- Upload date: 2026-06-28
- Video: https://www.youtube.com/watch?v=65X0pQ6Lmbg
- Transcript: raw/20260628_65X0pQ6Lmbg/65X0pQ6Lmbg.en-orig.vtt
- Metadata: raw/20260628_65X0pQ6Lmbg/65X0pQ6Lmbg.info.json

The latest AI models have made it possible to go past text-based chats, and build what Andrej Karpathy argues is the pinnacle of AI UX: voice-in, visuals-out.

In this talk, Forestwalk Labs co-founder Allen Pike shares why this approach for LLM-powered product development is so useful, what's necessary to make it actually delight users, and lessons his team has learned building products with highly responsive AI agents like these – with a key focus on techniques for achieving low latency.

Speakers:
- Allen Pike (Forestwalk Labs): Allen is co-founder of Forestwalk Labs, runs the Infer AI engineering meetup, and hosts the It Shipped That Way podcast.
  X/Twitter: https://twitter.com/apike
  LinkedIn: https://www.linkedin.com/in/allenpike/
  GitHub: https://github.com/apike

## Structuring the Unstructured - Cedric Clyburn, Red Hat

- Upload date: 2026-06-28
- Video: https://www.youtube.com/watch?v=-x5GEVnkuRw
- Transcript: raw/20260628_-x5GEVnkuRw/-x5GEVnkuRw.en-orig.vtt
- Metadata: raw/20260628_-x5GEVnkuRw/-x5GEVnkuRw.info.json

Modern organizations generate vast amounts of data stored in diverse and often unstructured formats, such as PDFs, scanned documents, and proprietary file types. For engineers working with AI, the challenge isn’t just about extracting text but also about preserving the structure, context, and relationships within the data. Whether fine-tuning models or building retrieval-augmented generation (RAG) pipelines, effective document processing is essential for creating AI applications that bring value.

This live demo session is all about the techniques and open source tools needed to transform unstructured documents into structured formats like JSON or Markdown, ready for AI workflows. You’ll learn how to handle challenges like multi-page tables, image-heavy layouts, and scanned documents using context-aware methods with Docling, part of the Linux AI & Data Foundation.

Speakers:
- Cedric Clyburn (Red Hat): Cedric Clyburn (@cedricclyburn) is a Senior Developer Advocate at Red Hat and open-source contributor (vLLM, Podman) who helps developers adopt emerging technologies through speaking, workshops, and community leadership (as an organizer of Kubernetes Community Day New York).
  X/Twitter: https://x.com/cedricclyburn
  LinkedIn: linkedin.com/in/cedricclyburn/
  GitHub: github.com/cedricclyburn

## A Genius With Amnesia - Victor Savkin, Nx

- Upload date: 2026-06-26
- Video: https://www.youtube.com/watch?v=jVjt-2g8NMY
- Transcript: raw/20260626_jVjt-2g8NMY/jVjt-2g8NMY.en-orig.vtt
- Metadata: raw/20260626_jVjt-2g8NMY/jVjt-2g8NMY.info.json

Imagine a genie grants your wish and materializes the best engineer in the world, John Carmack in his prime, to work on your codebase. The catch: he can only see a tiny corner of it, and he forgets everything between interactions. No matter how good he is, the value isn’t there. This is what coding agents are today. We need to fix it.

Speakers:
- Victor Savkin (Nx): Victor is the creator of Nx, the agentic monorepo platform, and Polygraph, the meta-harness for maximum agent autonomy, with 20+ years building high-performance frameworks and build tools.
  X/Twitter: https://x.com/victorsavkin
  LinkedIn: https://www.linkedin.com/in/victorsavkin/
  GitHub: https://github.com/vsavkin

## Stop Writing Tone Instructions. Layer Them. - Isadora Martin-Dye, Isadora & Co

- Upload date: 2026-06-26
- Video: https://www.youtube.com/watch?v=ij-AU9dpJjc
- Transcript: raw/20260626_ij-AU9dpJjc/ij-AU9dpJjc.en-orig.vtt
- Metadata: raw/20260626_ij-AU9dpJjc/ij-AU9dpJjc.info.json

Brand voice that survives real users isn't an instruction you write once - it's an architecture. Drawing on production code from a wedding venue, a personal AI companion, and a tool for families of missing people, this talk breaks voice into four layers: immutable identity, situational mode, example-anchored voice, and a deterministic post-generation veto. The difference between a prompt that holds and one that breaks on turn 21 is knowing which job belongs to which layer.

Speakers:
- Isadora Martin-Dye (Isadora & Co | The Bloom House AI): Isadora Martin-Dye is the founder of Isadora & Co, a portfolio of four ventures spanning hospitality and AI: she speaks on vertical AI and on what it actually takes to design software for the relationship-driven, emotionally heightened audiences other AI products keep getting wrong.
  LinkedIn: https://www.linkedin.com/in/isadora-martin-dye-226353a1

## Turn 10,994 Notes Into Memory - Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI

- Upload date: 2026-06-26
- Video: https://www.youtube.com/watch?v=ZRM_TfEZcIo
- Transcript: raw/20260626_ZRM_TfEZcIo/ZRM_TfEZcIo.en-orig.vtt
- Metadata: raw/20260626_ZRM_TfEZcIo/ZRM_TfEZcIo.info.json

Full implementation is open-source: https://github.com/iusztinpaul/ai-research-os-workshop
Agent Engineering: Building Multi-Agent Systems Course: https://academy.towardsai.net/courses/agent-engineering

Turning thousands of notes, videos, documents, and repositories into usable AI context requires more than a bigger context window. It requires memory and context engineering: organizing sources, indexing what matters, and loading only what the model needs.

The talk shows how the authors turn an Obsidian vault of 10,000+ notes, documents, videos, and repositories from a passive knowledge archive into live context for AI agents. A system that the authors use daily as their personal AI research OS for writing code and creating content.

You'll learn to design a deep research algorithm that runs across both the open web and your personal "Second Brain", then store what it finds as a research memory you and your agents can maintain, visualize, and grow. All based on the authors' 3 major iterations of the system over the past 18 months.

You'll walk away knowing how to:

- Choose the right tool for the job: Codex/Claude Code vs. NotebookLM vs. RAG vs. a personalized research memory
- Design deep-research pipelines across Obsidian, NotebookLM, GitHub, Google Drive, Readwise, and YouTube
- Build a token-efficient memory layer from plain files, not a vector or graph DB
- Plug tens of thousands of personal notes into an LLM knowledge (or wiki) base that scales
- Implement the memory layer between your Second Brain and any agent harness (Codex, Claude Code, or your own)

For: Engineers ready to move beyond hoarding notes and turn their "Second Brain" into a context that their AI agents can research, maintain, and grow.

Speaker info:

Paul Iusztin

- X: https://x.com/pauliusztin_
- in: https://www.linkedin.com/in/pauliusztin/
- youtube: https://www.youtube.com/@itsdecodingai

Louis-François Bouchard

- X: https://x.com/Whats_AI
- in: https://www.linkedin.com/in/whats-ai/
- youtube: https://www.youtube.com/@WhatsAI

Timestamps:

00:00- Introduction to the "Second Brain" concept
00:49- The core problem: Losing research and finding meaningful notes
01:32- Building an AI Research OS
02:05- Meet the presenters: Louis-François Bouchard and Pauline
03:31- Choosing the right tools for research (Google vs. LLMs)
04:51- Why NotebookLM and vector databases aren't always ideal
07:08- The need for a personalized research assistant
09:16- Moving data to Obsidian for local file management
11:02- Overview of the AI Research OS repository
12:48- The three-layer system: Raw content, Index, and Wiki
13:28- Architecture of the Deep Research algorithm
18:28- Version 3: Adding the Wiki layer on top of knowledge bases
20:13- How the file-based index works (no database required)
21:26- Exploring the Wiki structure: Comparisons, concepts, and entities
22:49- How to query the Wiki efficiently
25:01- Managing snapshots and personal notes using the PARA method
27:04- Demo 1: Researching agent engineering
31:58- Demo 2: Ingesting and comparing GitHub repositories
34:25- Demo 3: Ingesting custom web links
36:50- Future improvements: Connectors, memory compaction, and source provenance
38:45- The Agent Engineering course overview

Speakers:
- Paul Iusztin: Paul Iusztin is the Founder & CEO of Decoding AI and the author of the bestselling LLM Engineer's Handbook. | Louis-François Bouchard is the Co-founder & CTO of Towards AI and author of Building LLMs for Production.
  X/Twitter: https://x.com/pauliusztin_
  LinkedIn: https://www.linkedin.com/in/pauliusztin/
  GitHub: https://github.com/iusztinpaul

## Agents in Production: How OpenGov Built and Scaled OG Assist - Gabe De Mesa, OpenGov

- Upload date: 2026-06-26
- Video: https://www.youtube.com/watch?v=4uFVSLgD2Q4
- Transcript: raw/20260626_4uFVSLgD2Q4/4uFVSLgD2Q4.en-orig.vtt
- Metadata: raw/20260626_4uFVSLgD2Q4/4uFVSLgD2Q4.info.json

Come and learn about building AI Agents in production. Learn hands-on directly with the AI Agents team from OpenGov which powers AI workflows across thousands of state and local governments.

This session will cover:
* The core agent loop/harness
* A2A protocol
* Building with Effect-TS and Typescript
* Feedback and evals
* Long context handling
* Monitoring and observability
* Building out tools and skills
* Enterprise contribution model
* Accelerating workflows with Claude and Cursor

Speakers:
- Gabe De Mesa (OpenGov): Gabe works on the flagship AI Agent product offering at OpenGov which serves thousands of state and local governments across the country. Gabe was one of the first engineers to join the newly formed AI Agents team. He wanted to share the features he's built, experience he's gained building and running agents in production, battle scars gained from running with real production workloads and customers, architecture, and some best practices to help other engineers run agentic workloads at their companies.
  X/Twitter: https://x.com/jamesjellow
  LinkedIn: https://www.linkedin.com/in/gabedemesa
  GitHub: https://github.com/gabedemesa

## Production Evals For Agentic AI Systems - Nishant Gupta, Meta Superintelligence Labs

- Upload date: 2026-06-25
- Video: https://www.youtube.com/watch?v=vljxQZfJ9wY
- Transcript: raw/20260625_vljxQZfJ9wY/vljxQZfJ9wY.en-orig.vtt
- Metadata: raw/20260625_vljxQZfJ9wY/vljxQZfJ9wY.info.json

As AI systems evolve from chat interfaces into autonomous agents capable of reasoning, planning, and tool usage, traditional evaluation approaches are breaking down. Offline benchmarks and static datasets fail to capture the complexity, non-determinism, and operational risks of real-world AI systems operating in production environments.

In this talk, I’ll share practical lessons and architectural patterns for building evaluation systems for agentic AI workflows at scale. We’ll explore how modern AI platforms are shifting from one-time benchmark testing toward continuous evaluation pipelines integrated directly into production infrastructure.

Topics include:
- Why offline evals fail for autonomous AI systems
- Evaluating tool use, planning, reasoning, and multi-step workflows
- Online vs offline eval architectures
- Human-in-the-loop evaluation systems
- Detecting drift, hallucinations, and unsafe behaviors
- Building feedback loops for continuous improvement
- Observability and telemetry for agentic workflows
- Reliability metrics beyond model accuracy

Attendees will leave with practical frameworks for designing scalable evaluation systems capable of measuring real-world AI behavior, reliability, and operational impact.

Speakers:
- Nishant Gupta (Meta Superintelligence Labs): Nishant Gupta is a Software Engineering Tech Lead at Meta Superintelligence Labs focused on building the training and inference AI Infrastructure.
  LinkedIn: https://www.linkedin.com/in/nishantgupta-ai/
  GitHub: https://github.com/nishantgpt-lab

## Build Systems, Not Code - Angie Jones, Agentic AI Foundation

- Upload date: 2026-06-25
- Video: https://www.youtube.com/watch?v=ZD9-4fW2HhM
- Transcript: raw/20260625_ZD9-4fW2HhM/ZD9-4fW2HhM.en-orig.vtt
- Metadata: raw/20260625_ZD9-4fW2HhM/ZD9-4fW2HhM.info.json

AI coding agents are changing what it feels like to be a software engineer. For a lot of us, that's challenging our sense of craftsmanship. If agents are writing the code, do we lose the joy of building?

I don't think so. The building moves up a layer.

In this talk, I'll share how I found that familiar engineering flow state again. Not by writing every line myself, but by designing agentic systems that still require the engineering principles we value: systems thinking, decomposition, separation of concerns, state management, etc.

The tools are different now, but the engineering discipline is still there. We'll walk through how to apply the engineering muscles you already have to a new set of building blocks.

If you've been wondering where your value goes in an AI native world, this talk will help you see that it hasn't disappeared. It's now at the system level.

Speakers:
- Angie Jones (Agentic AI Foundation): Angie Jones is the VP of Developer Experience at the Agentic AI Foundation where she guides how agentic systems are designed, implemented, and adopted across the global developer ecosystem.
  X/Twitter: https://twitter.com/techgirl1908
  LinkedIn: https://www.linkedin.com/in/angiejones/
  GitHub: https://github.com/angiejones

## The Log Is The Agent - Ishaan Sehgal, Omnara

- Upload date: 2026-06-25
- Video: https://www.youtube.com/watch?v=UPwGaM2MKHY
- Transcript: raw/20260625_UPwGaM2MKHY/UPwGaM2MKHY.en-orig.vtt
- Metadata: raw/20260625_UPwGaM2MKHY/UPwGaM2MKHY.info.json

Think about a character you've spent 100 hours playing in a video game like Skyrim or Elden Ring.

What exactly is your character?
- Is it the game engine (the loop)? No.
- Is it the PlayStation console (the compute)? No.
- Is it the controller (the tools)? No.

Your character is the save file (the data).

If your PlayStation bursts into flames, your character isn't dead. You just buy a new PlayStation, download your save file from the cloud, and your character is exactly where they were, mid-swing. The identity, history, and current state of your character live entirely in the data.

Today, most attention goes toward frameworks, orchestration layers, context engineering, specs, and tools. But as models become more capable and generally intelligent, the differentiator shifts away from these abstractions and toward the underlying infrastructure.

The Engine becomes interchangeable. The Brain (LLM) commoditizes. The Hands (tools) are just APIs.

What actually persists across models, runtimes, and machines is the session log.

That’s where continuity, identity, and state actually live.

A decade ago, Martin Kleppmann argued that databases should be understood as projections over an append-only log. I think the same thing is now happening with agents.

Today, agents are treated like complicated black boxes made of loops, models, and tool calls. But at its core, the agent is the session log (the save file). Everything else is swappable.

Once the log becomes the primitive, entirely new system properties emerge:
- durability — agents survive crashes, disconnects, and machine failure
- continuity — sessions can be resumed from anywhere, on any device
- forkability — timelines can branch for parallel execution and exploration
- addressability — agents become durable entities that can be referenced and revisited
- observability — execution can be monitored and steered in real time
- portability — models, runtimes, and machines become interchangeable

But this creates a new infrastructure question:

If the model provider owns the log, does the model provider own the agent?

This talk explores why the future of agent infrastructure isn't what we're focused on today, but rather durable, portable logs that make agents persistent across models, runtimes, and machines.

Speakers:
- Ishaan Sehgal (Omnara): Ishaan Sehgal is the CEO and cofounder of Omnara (YC S25), where he builds managed infrastructure for AI agents.
  X/Twitter: https://x.com/ishaansehgal
  LinkedIn: https://www.linkedin.com/in/ishaan-sehgal/
  GitHub: https://github.com/ishaansehgal99

## The Miranda Hypothesis: How Hamilton Poisoned Persona Evals - Jacob E. Thomas, Results Gen

- Upload date: 2026-06-25
- Video: https://www.youtube.com/watch?v=IJXjTLPzvAU
- Transcript: raw/20260625_IJXjTLPzvAU/IJXjTLPzvAU.en-orig.vtt
- Metadata: raw/20260625_IJXjTLPzvAU/IJXjTLPzvAU.info.json

Your persona-eval pipeline rates an Alexander Hamilton simulation at 80% personality fidelity. It is also rating a Hamilton who sounds like he has read his own Broadway musical. The dominant failure mode of every character-based AI system now in production is invisible to LLM-as-judge, personality-scale benchmarks, and behavioral consistency scores because every one of them was built to detect convincingness, and convincingness is exactly what the failure produces.

The failure has a name: Miranda distortion. When the volume of cultural representation of a figure in your training corpus outnumbers their primary documentary record by orders of magnitude (and it always does for any culturally salient figure) your persona doesn't speak from the record. It speaks from the smoothed cultural composite. The 2015 Broadway musical has exponentially more representational density in your training data than the 175,000 words of the Federalist Papers. Your evals were not designed to notice this. They were designed to score fluency, personality coherence, and stylistic naturalness... the exact features the composite optimizes.

In this talk:

- The structural argument: why InCharacter-style benchmarks, CoSER, and PsyMem can hit state-of-the-art on personality fidelity while structurally failing to detect anachronistic reasoning.
- The architectural mechanism: why RLHF amplifies Miranda distortion instead of correcting it (raters are themselves products of the same cultural composite).
- The framework: a four-stage paradigm shift from cognitive simulation to epistemic simulation (corpus-bounded, temporally-anchored, expert-loop-evaluated).
- The instrument: the pre-registered Prism Experiment. Lincoln at four documented temporal moments, three seeding conditions, five diagnostic questions written by a domain historian, and a weighted three-axis rubric (Anachronism Detection, Documentary Consistency, Contextual Plausibility) that catches what automated metrics miss.
- The handoff: what a working eval loop looks like when a historian, classicist, theologian, or clinical psychologist sits in it, and why that's a technical requirement, not a cultural courtesy

Pre-registered protocol with University of Toronto historian Rick Halpern, paper forthcoming. Reproducible by any team running a frontier model with a context window.

If you ship character bots, companion AI, pedagogical agents, historical simulations, or any system where a persona is supposed to reason from a specified record, your evals are measuring the wrong thing. Here is the instrument that catches what they miss.

Speakers:
- Jacob E. Thomas (Results Generation): Dr. Thomas is an epidemiologist, data scientist, and AI engineer who studies information as a determinant of health.
  LinkedIn: https://www.linkedin.com/in/jacob-e-thomas-atx/
  GitHub: https://github.com/jethomasphd/THE_COMPANION_DOSSIER

## Recursive Coding Agents - Raymond Weitekamp, OpenProse

- Upload date: 2026-06-25
- Video: https://www.youtube.com/watch?v=3hXJI2q0Jz8
- Transcript: raw/20260625_3hXJI2q0Jz8/3hXJI2q0Jz8.en-orig.vtt
- Metadata: raw/20260625_3hXJI2q0Jz8/3hXJI2q0Jz8.info.json

Recursive Language Models (RLMs) represent a powerful new paradigm of inference-time compute. We discuss many different ways to apply the principles of RLMs to coding agents, towards higher performance and reliability. We briefly define RLMs, showcase many of their performance advantages, then share how the RLM paradigm can be mapped onto coding agents. We strive to settle the long-standing debate, "Isn't Claude Code with sub-agents a RLM?" Finally, we showcase how both Claude Code Dynamic Workflows and OpenProse can specifically guide coding agents to recursively solve complex tasks with declarable outcomes.

The "slides" for this presentation are available as an interactive website at https://recursivecodingagents.com and a companion repo with specific code examples is available at https://github.com/rawwerks/recursive-coding-agents

Speakers:
- Raymond Weitekamp (OpenProse): Dr. Raymond Weitekamp is a PhD chemist, serial entrepreneur, artist, independent researcher, and AI Engineer at OpenProse.
  X/Twitter: https://x.com/raw_works
  LinkedIn: https://www.linkedin.com/in/raymondweitekamp/
  GitHub: https://github.com/rawwerks

## 6 Things to Know about AIE World's Fair 2026

- Upload date: 2026-06-21
- Video: https://www.youtube.com/watch?v=0S8xe9ftGTM
- Transcript: raw/20260621_0S8xe9ftGTM/0S8xe9ftGTM.en-orig.vtt
- Metadata: raw/20260621_0S8xe9ftGTM/0S8xe9ftGTM.info.json

We're back in SF! Regular bird tix will sell out by Monday, and we wanted to make a little video to tell you about why you should get off your couch and come. 

See video for how to claim the $40k in sponsor offers for attendees, and a special youtube-only discount: YOUTUBEPROMO (for new tix only, dont be cheeky and ask for refunds pls, our team is trying to do our best with real support issues) 

https://app.ai.engineer/e/ai-engineer-worlds-fair-2026?discount=YOUTUBEPROMO applies at checkout

timestmaps

0:00 Introduction to AIE World's Fair 2026
1:30 Scaling up: Content and Event Growth
4:44 The Expo Floor experience
5:45 Research and Industry synergy
9:20 Leadership track and Token Billionaires
12:05 Focus on AI Verticals
13:41 Side events, orientation, and community

## The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks

- Upload date: 2026-06-18
- Video: https://www.youtube.com/watch?v=ObTPqBGsEbA
- Transcript: raw/20260618_ObTPqBGsEbA/ObTPqBGsEbA.en-orig.vtt
- Metadata: raw/20260618_ObTPqBGsEbA/ObTPqBGsEbA.info.json

A retail bank spent £85,000 over six months on a chatbot PoC that could not reach production. No one could explain why it was failing. When Sandipan Bhaumik's team got involved, they picked the model in week seven of an eight-week engagement — the first six weeks went to evaluation data, tracing infrastructure, and a measurement pipeline. Six weeks post launch, when the bank updated its interest rate policy and customer satisfaction dropped, the tracing system caught the cause: the new policy document had not been reembedded and the agent was serving stale answers.

The talk covers the five pillars he built from that and similar engagements: evaluation (define success numerically before touching code), observability (trace every agent decision — European regulators require it), data foundation (agents do not forgive bad data the way humans do), multi agent orchestration patterns, and governance (47 PII breaches caught in testing before launch). The evaluation data set is a living system, not a fixed benchmark. The production incident playbook connects all five.

Speaker info:
- https://www.linkedin.com/in/sandipanbhaumik

## Your Agent's Biggest Lie: "I Searched the Web" — Rafael Levi, Bright Data

- Upload date: 2026-06-17
- Video: https://www.youtube.com/watch?v=btxGmN8RvNU
- Transcript: raw/20260617_btxGmN8RvNU/btxGmN8RvNU.en-orig.vtt
- Metadata: raw/20260617_btxGmN8RvNU/btxGmN8RvNU.info.json

Sometimes the agent did not search the web at all. It got blocked, hit a CAPTCHA, saw a fake page, or fell back to stale training data, then answered as if everything worked. This session is a direct look at that failure mode, and what changes when the same agent is given real web access instead of pretending.

Using Bright Data's Web MCP, the demo compares blocked and unblocked runs across sites like LinkedIn, Instagram, Amazon, and TikTok, and walks through the mechanics behind the difference: anti-bot systems, JS rendering, CAPTCHA handling, and why clean access matters if you want reliable citations, real-time results, and fewer hallucinations. If you're building agents that depend on the open web, this is a practical look at one of their biggest hidden failure modes.

Speaker info:
- https://il.linkedin.com/in/rafael-levi
- https://github.com/ScrapeAlchemist

## You Might Not Need 50 Diffusion Steps — Ziv Ilan, Nvidia

- Upload date: 2026-06-16
- Video: https://www.youtube.com/watch?v=gHs5ZiY80PM
- Transcript: raw/20260616_gHs5ZiY80PM/gHs5ZiY80PM.en-orig.vtt
- Metadata: raw/20260616_gHs5ZiY80PM/gHs5ZiY80PM.info.json

At GTC a few weeks ago, Ziv Ilan's team at NVIDIA got a video diffusion model generating in close to real time on a single Blackwell B200. The trick wasn't a new architecture, it was stripping out most of the fifty step denoising process diffusion models default to, by combining quantization, caching, and step distillation: training a student model to match a teacher's output using four steps, eight steps, or in some cases just one.

Ilan walks through each layer of that stack: dynamic quantization work done with Black Forest Labs on Flux 2, a caching method that skips recomputing latent chunks that barely change between denoising steps, and distillation approaches split into trajectory based training, where the student copies the teacher's exact path, and distribution based training, where it only has to land on the same output, now the more common and higher quality of the two. NVIDIA's open source FastGen repo packages the post training and GPU sharding work needed to apply all this at scale, and Ilan frames the gains as additive, quantization alone can be enough on its own, or you can stack it with caching and distillation to reach the ten to two hundred times speedup that real time generation needs.

Speaker info:
- https://www.linkedin.com/in/ziv-ilan-deci/

## Why MCP and ChatGPT Apps Use Double Iframes — Frédéric Barthelet, Alpic

- Upload date: 2026-06-15
- Video: https://www.youtube.com/watch?v=c-2eEv2ou7Y
- Transcript: raw/20260615_c-2eEv2ou7Y/c-2eEv2ou7Y.en-orig.vtt
- Metadata: raw/20260615_c-2eEv2ou7Y/c-2eEv2ou7Y.info.json

Inspect ChatGPT's DOM while an MCP app is rendering and you find an iframe nested inside another iframe. Frédéric Barthelet traces why each simpler approach fails: `srcdoc` shares the parent origin so ChatGPT's CSP blocks all third party scripts; relaxing that CSP lets any app read ChatGPT's localStorage and cookies; adding `sandbox` removes origin indexed storage; adding `allow-same-origin` to restore it is the classic sandbox escape. The double iframe is what remains after ruling all of that out.

The outer iframe serves one lightweight script from a controlled subdomain (different subdomain per app to prevent cross app storage collisions), which loads the actual app HTML via `srcdoc` into the inner frame — the same pattern Facebook first shipped for their app marketplace. The practical implication: every external domain your view touches must be declared in your MCP app metadata or the submission gets rejected. Barthelet demos Skybridge's CSP inspector, which diffs declared domains against actual network calls live in dev.

Speaker info:
- https://x.com/bartheletf
- https://www.linkedin.com/in/frederic-barthelet/
- https://github.com/fredericbarthelet

## Your Attention Is the Bottleneck, Not Your Agents — Zack Proser, WorkOS

- Upload date: 2026-06-11
- Video: https://www.youtube.com/watch?v=so9l_MwS2yg
- Transcript: raw/20260611_so9l_MwS2yg/so9l_MwS2yg.en-orig.vtt
- Metadata: raw/20260611_so9l_MwS2yg/so9l_MwS2yg.info.json

Simon Willison fires up four parallel agents and is wiped out by 11am. That is the problem Zack Proser is solving: not that the tools are too slow but that human attention is still the hard constraint. His loop: voice brief at 184 words per minute, agent dispatched to an isolated git worktree, laptop closed, progress checked from a phone on LTE miles away via remote control.

The talk covers four layers that make this sustainable: signal agents that read Slack and Linear on a loop so you never open them yourself, verification gates from lint and build up to browser click through and critic passes, a weekly agent run over your JSONL conversation history to surface inefficiencies and generate missing skills, and an Oura ring connected via MCP so Claude can tell you that you did not sleep last night. You can ignore it. But at least you thought about it.

Speaker info:
- https://linkedin.com/in/zackproser
- https://github.com/zackproser

Timestamps:
0:00 Introduction and the problem of AI developer burnout
1:08 A concrete example of using AI agents for bug fixing
3:36 The bottleneck: human attention vs. infinite agent scalability
5:13 The proposed stack for sustainable AI development
6:03 The Signal Layer: Managing notifications and context switching
7:04 Voice-first flows for coding efficiency
8:15 The Shower Principle and Remote Control for agents
11:13 Safety, verification, and testing gates
12:05 The new, balanced developer workflow
13:22 System self-improvement using conversation history
15:31 Holistic well-being (Oura ring integration)
17:35 Q&A: Addressing skill development early in a career
20:07 Q&A: Managing JSONL history and long-term conversation logs
21:30 Q&A: Night shift/background agent execution
22:17 Q&A: Voice interaction and audio feedback
23:39 Q&A: Handling complex, multi-stack features

## Why Can't Anyone Answer Questions About the Business? — Garrett Galow, WorkOS

- Upload date: 2026-06-11
- Video: https://www.youtube.com/watch?v=iUWwcG-C8OU
- Transcript: raw/20260611_iUWwcG-C8OU/iUWwcG-C8OU.en-orig.vtt
- Metadata: raw/20260611_iUWwcG-C8OU/iUWwcG-C8OU.info.json

Every business question that needs SQL follows the same loop: explain the question, wait for an engineer, get an answer, realize it needs one more join, share a one-off in Slack, repeat. Garrett Galow from WorkOS built Studio to break that loop — an internal workspace where anyone can ask questions against Snowflake, Linear, and Notion in natural language and get answers or reusable widgets without filing a request.

The widgets are the interesting part: the LLM writes them once as declarative JavaScript that calls the underlying data sources directly, so every subsequent run is deterministic and cheap. Three things made it reliable enough to hand to a support team. Preflight sequencing that injects schema context only at the moment a tool is invoked, not upfront, keeping the context window clean. A layering rule that explicitly tells the model to distrust its own knowledge about WorkOS and go to primary sources. And query validation that runs every generated Snowflake query before hardcoding it into a widget, catching the valid SQL that returns zero rows failure mode.

Speaker info:
- https://www.linkedin.com/in/garrett-galow/

## The agent-ready web: Simplify user actions with WebMCP — Tara Agyemang, Google

- Upload date: 2026-06-11
- Video: https://www.youtube.com/watch?v=ghJmWQCIHRM
- Transcript: raw/20260611_ghJmWQCIHRM/ghJmWQCIHRM.en-orig.vtt
- Metadata: raw/20260611_ghJmWQCIHRM/ghJmWQCIHRM.info.json

Buying two concert tickets costs an AI agent the entire DOM, the accessibility tree, a screenshot, pixel coordinate math, and then a click that might miss because an ad just loaded and shifted the layout. Tara Agyemang from the Google Chrome team introduces WebMCP, a proposed web standard that replaces that process with structured tools: instead of guessing what your site does, agents get a menu of named, typed, described actions they can call directly.

The talk covers two implementation paths. The declarative API adds a few HTML attributes to existing forms and the browser generates the JSON schema automatically. The imperative API lets you register custom tools in JavaScript for complex multi step flows, with an execute block that runs normal DOM code and returns state back to the agent. The live demo completes a concert ticket purchase in three tool calls: search by name, open the concert page, call purchase with quantity and section. Still experimental and in early preview on Chrome 146, but an eval CLI and inspector extension are available now for testing your own sites.

Speaker info:
- https://x.com/tara_ojo
- https://uk.linkedin.com/in/taraojo
- https://github.com/taraojo

## Self Driving Products: Product Signals to Pull Requests — Joshua Snyder, PostHog

- Upload date: 2026-06-10
- Video: https://www.youtube.com/watch?v=zMiSRliEzv4
- Transcript: raw/20260610_zMiSRliEzv4/zMiSRliEzv4.en-orig.vtt
- Metadata: raw/20260610_zMiSRliEzv4/zMiSRliEzv4.info.json

A rage click, a 2am error spike, a customer Slack message — today each sits until a developer notices, triages, tickets, and writes a fix. PostHog is building a pipeline that collapses that chain: signal arrives, a background agent groups it with related errors and session replays, researches the codebase, and opens a PR. You wake up to green PRs instead of dashboards.

Three lessons from building it: off the shelf embedding models cluster signals by structural similarity rather than meaning, so errors land next to errors and Slack messages land next to Slack messages — the fix is to embed LLM generated queries rather than the signals themselves. Specificity determines whether the agent produces a useful PR or just fixes something at random; error tracking is immediately actionable, Slack and session replay usually are not. And start with agents even when it looks expensive — run the same problem through an agent 100 times, find the patterns, then collapse the expensive step into a one shot call.

Speaker info:
- https://x.com/joshsny
-https://www.linkedin.com/in/joshsny/

## Stop Making Models Bigger, Make Them Behave — Kobie Crawford, Snorkel

- Upload date: 2026-06-10
- Video: https://www.youtube.com/watch?v=TNwJ1LMiENk
- Transcript: raw/20260610_TNwJ1LMiENk/TNwJ1LMiENk.en-orig.vtt
- Metadata: raw/20260610_TNwJ1LMiENk/TNwJ1LMiENk.info.json

Qwen 3 235B was asked for YouTube's year over year ad revenue growth from 2023 to 2024. It queried a table that didn't exist, tried again, got nothing back both times, and hallucinated an answer. The 4B model Snorkel finetuned with RL called `get_table_name` first, inspected the schema, ran a query, hit a column error, self-corrected, and got the right answer. The training run cost under $500.

Kobe Crawford covers why tool discipline matters more than reasoning depth for this class of tasks, how single table training transferred cleanly to harder multi table problems (13.9% to 26.6% on the FinQA reasoning benchmark), and why breaking evals into rubrics helps identify which specific behavior to fix before writing any training data.

Speaker info:
- https://www.linkedin.com/in/kobie-crawford
- https://snorkel.ai/author/kobie-crawford/

## Sovereign Escape Velocity: Ownership w Open Models — Gus Martins, & Ian Ballantyne, Google DeepMind

- Upload date: 2026-06-10
- Video: https://www.youtube.com/watch?v=SS-A8sE7hkw
- Transcript: raw/20260610_SS-A8sE7hkw/SS-A8sE7hkw.en-orig.vtt
- Metadata: raw/20260610_SS-A8sE7hkw/SS-A8sE7hkw.info.json

Gemma 4's 31B model sits fourth on the LM Arena open model leaderboard. The models around it are at least twice as large; some are 20 times larger. It runs on a single GPU. Competitors at comparable quality need four or five.

Ian Ballantyne and Gus Martins walk through what that size efficiency unlocks: running on a Pixel phone (the E2B and E4B models use 2B and 4B of GPU memory despite having more parameters), deploying a medical variant on two GPUs for an entire hospital, and running parallel multi agent workloads on an M4 Mac via LM Studio. The talk also covers the license shift from a custom Gemma license to Apache 2.0 — the practical effect is that sovereign institutions in Ukraine, Bulgaria, and Brazil can get legal sign off without 18 months of procurement review.

Speaker info:
- https://x.com/gusthema
- https://www.linkedin.com/in/gus-martins-64ab5891
- https://linkedin.com/in/ianballantyne
- https://github.com/irbg

## GPU Cloud Deployment Without Leaving Your IDE — Audry Hsu, RunPod

- Upload date: 2026-06-09
- Video: https://www.youtube.com/watch?v=zDGHt0LB-dA
- Transcript: raw/20260609_zDGHt0LB-dA/zDGHt0LB-dA.en-orig.vtt
- Metadata: raw/20260609_zDGHt0LB-dA/zDGHt0LB-dA.info.json

The iteration cycle before Flash: commit, push, build a Docker image, pull it from the registry, load it onto a server, allocate a GPU, then find out if it works. Audrey Hsu demos what replacing that with a single decorator looks like — add `@flash.endpoint` to an async Python function and it deploys to GPU cloud from your IDE, with hot reload so a model swap is one line of code rather than a container rebuild.

The second demo chains three models: Qwen 3 generates image prompts, DreamShaper renders them, Nano Banana 2 composes the results into a single photo. H100 pricing is $0.00116 per second, charged only while a worker is handling a request. RunPod's recommendation: start with pods while experimenting, switch to serverless when you need hundreds of workers autoscaling across data centers.

Speaker info:
- https://www.linkedin.com/in/audry-hsu/

## 2026 AI Engineer Vibe Reel

- Upload date: 2026-06-09
- Video: https://www.youtube.com/watch?v=gUMwt4-5kn0
- Transcript: raw/20260609_gUMwt4-5kn0/gUMwt4-5kn0.en-orig.vtt
- Metadata: raw/20260609_gUMwt4-5kn0/gUMwt4-5kn0.info.json

W are getting ready for the World's Fair in San Francisco - Jun 29 to July 2!

https://ai.engineer/wf  - get tickets and see schedule!

## RAG is dead, right?? — Kuba Rogut, Turbopuffer

- Upload date: 2026-06-09
- Video: https://www.youtube.com/watch?v=UM6sFg_jdlE
- Transcript: raw/20260609_UM6sFg_jdlE/UM6sFg_jdlE.en-orig.vtt
- Metadata: raw/20260609_UM6sFg_jdlE/UM6sFg_jdlE.info.json

Cursor added semantic search and measured a 24% increase in answer accuracy on their composer model, a 2.6% gain in code retention in large codebases, and a 2.2% drop in dissatisfied user requests. Those numbers look small until you factor in that semantic search does not fire on every query. Meanwhile Google search volume for RAG hit a new inflection point in mid 2025 and went through the roof. The Twitter "RAG is dead" discourse and the actual usage curve are moving in opposite directions.

Kuba Rogut's argument is that the problem was never retrieval, it was the narrow definition of it. RAG is not just a vector search call. It is vector search, full text search, glob, regex, and filters used iteratively by an agent that keeps searching until it has what it needs. He contrasts Claude Code (grep per session, no index, repeat cost every run) with Cursor (one time upfront indexing, lightweight tool calls at runtime). Claude Code's approach is not wrong, it is a deliberate tradeoff. The frame that clarifies it: embeddings are cached compute, and whether to cache depends on query volume. Jeff Dean's version: you do not need a trillion tokens at once, you need the right million.

Speaker info:
- https://www.linkedin.com/in/kubarogut/
- https://x.com/rogutkuba

Timestamps:
0:00 Introduction to the "RAG is dead" discourse
1:12 Google search volume trends for RAG
1:39 Defining RAG vs. Agentic Search
3:15 Cursor's indexing and semantic search approach
6:10 Contrasting Claude Code (grep) vs. Cursor (indexed)
6:40 The concept of embeddings as cached compute
8:38 The shift from simple RAG to Agentic Retrieval
9:44 Jeff Dean on context windows and stage retrieval

## From Transcription to Live Music: Gemini's Audio Stack — Thor Schaeff, Google DeepMind

- Upload date: 2026-06-09
- Video: https://www.youtube.com/watch?v=Bc6Ojl2XS1w
- Transcript: raw/20260609_Bc6Ojl2XS1w/Bc6Ojl2XS1w.en-orig.vtt
- Metadata: raw/20260609_Bc6Ojl2XS1w/Bc6Ojl2XS1w.info.json

One API call to Gemini 3 Flash Preview: speaker labels by name, timestamps, emotion tags, language detection with English translation, and a full summary. That is the audio understanding layer that underlies everything else Thor Schaeff demos here, including speech generation directed by a "director's note" rather than picked from a catalogue, and Gemini 3.1 Flash Live, a sound to sound real time multimodal model with thinking baked in rather than cascaded through a separate LLM.

The talk ends with Lyria 3, Google DeepMind's music generation model that can now produce full songs with lyrics. The live demo has the Gemini Live model calling Lyria via tool use on request to generate a German techno schlager about the UK startup scene, live on stage.

Speaker info:
- https://x.com/thorwebdev
- https://www.linkedin.com/in/thorwebdev

## Road to 5 Million Tokens: Breaking Barriers in Long Context Training — Max Ryabinin, Together AI

- Upload date: 2026-06-08
- Video: https://www.youtube.com/watch?v=TUnPNY4E2fw
- Transcript: raw/20260608_TUnPNY4E2fw/TUnPNY4E2fw.en-orig.vtt
- Metadata: raw/20260608_TUnPNY4E2fw/TUnPNY4E2fw.info.json

Training a standard LLaMA 3B model with a 3 million token context on a single 8xH100 node fails before you even start: the model parameters alone exhaust GPU memory. Max Ryabinin from Together AI walks through the full stack of techniques needed to get there: fully sharded data parallelism, DeepSpeed Ulysses context parallelism for an 8x activation reduction, activation checkpointing for another 8x, CPU offloading for transformer block inputs, and chunked sequence training to avoid allocating buffers 3 million tokens wide.

Even that stack falls short at 5 million tokens. The novel contribution, Untied Ulysses, goes deeper into the context parallelism step: instead of allocating one large buffer per attention head group, it chunks the heads further and reuses those buffers across iterations, cutting activation memory with negligible throughput impact. At both 8B and 32B scale the results match the most memory optimized transformer training baselines while pushing sequence length 25% further than prior Ulysses implementations.

Speaker info:
- https://www.linkedin.com/in/max-ryabinin/
- https://x.com/m_ryabinin

## Why Eval++ Is the Next Great Compute Primitive — Sunil Pai & Matt Carey, Cloudflare

- Upload date: 2026-06-08
- Video: https://www.youtube.com/watch?v=SKDJo2CopRs
- Transcript: raw/20260608_SKDJo2CopRs/SKDJo2CopRs.en-orig.vtt
- Metadata: raw/20260608_SKDJo2CopRs/SKDJo2CopRs.info.json

Matt Carey and Sunil Pai from Cloudflare's agents team explain why Durable Objects turned out to be the right compute unit for AI agents: addressable, persistent, hibernating, stateful, and fast enough that 15ms London latency puts you inside a single animation frame. The Agents SDK builds on this to give resumable streaming, multi tab sync, and background scheduling out of the box, without any distributed systems engineering in userland.

The bigger reveal is Dynamic Workers: take a string of LLM generated code, run it in a sandboxed isolate with no ambient access, and grant only the capabilities you explicitly allow. They frame it as reclaiming 30 years of avoided eval. The session ends with both speakers teasing their afternoon talks, one on collapsing 2,600 Cloudflare API endpoints into a thousand token MCP tool, and a coding agent harness built entirely on Workers that they are, by their own admission, already shipping.

Speaker info:
- https://x.com/threepointone
- https://x.com/mattzcarey

## Why More Context Makes Your Agent Dumber and What to Do About It — Nupur Sharma, Qodo

- Upload date: 2026-06-08
- Video: https://www.youtube.com/watch?v=EcqMYoIV57A
- Transcript: raw/20260608_EcqMYoIV57A/EcqMYoIV57A.en-orig.vtt
- Metadata: raw/20260608_EcqMYoIV57A/EcqMYoIV57A.info.json

Give an agent your full codebase and it will attend to the start and the end, then quietly drop the middle. Nupur from Qodo calls this the U curve and builds the whole talk around it: why growing the context window did not fix the problem, and what actually does. She runs through iterative retrieval, hierarchical summarization, and self correction with honest cost tradeoffs for each.

The second half covers the orchestration paradox: capable models burn most of their tokens deciding how to solve a problem rather than solving it. Her team's fix is an 80/20 split, using high reasoning models for open ended discovery and lighter deterministic models for validation. Qodo's code review architecture runs this live: a context collector feeds specialized agents, a judge node recombines the results and weighs them against PR history, and every accepted or rejected suggestion shifts the weights for the next run.

Speaker info:
- https://www.linkedin.com/in/nupursh/

## From MCP to Scale: Pipelines That Build Themselves — Rafael Levi, Bright Data

- Upload date: 2026-06-07
- Video: https://www.youtube.com/watch?v=zTZ0qunQXnM
- Transcript: raw/20260607_zTZ0qunQXnM/zTZ0qunQXnM.en-orig.vtt
- Metadata: raw/20260607_zTZ0qunQXnM/zTZ0qunQXnM.info.json

Scraping is not the hard part anymore. Maintaining scrapers is. This session shows what it looks like when an agent uses MCP to inspect a site, understand its structure, generate a production scraper, and keep that pipeline working when the site changes.

Using Bright Data's MCP, APIs, and browser infrastructure, the flow moves from one-off extraction to something much more useful: agents that build parsers, save tokens by switching from page parsing to reusable scripts, and repair broken collection jobs without a human getting dragged in at 2am. If you're thinking about web data, automation, or agents that operate beyond a single prompt, this is a practical look at pipeline building at scale.

Speaker info:
- https://il.linkedin.com/in/rafael-levi
- https://github.com/ScrapeAlchemist

## LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize

- Upload date: 2026-06-07
- Video: https://www.youtube.com/watch?v=JsCCrBF7F1g
- Transcript: raw/20260607_JsCCrBF7F1g/JsCCrBF7F1g.en-orig.vtt
- Metadata: raw/20260607_JsCCrBF7F1g/JsCCrBF7F1g.info.json

Your agent called tool B before tool A, and B has a dependency on A. You did not catch it because nothing in your code audits agents. The telemetry does. Dat from Arize AI walks through what observability actually means when the system you are debugging is nondeterministic and the execution path changes with every run.

The talk covers the five flavors of eval signal (LLM as judge, human feedback, golden datasets, deterministic checks, business metrics), what scope to run them at (single span, multispan, trajectory, session), and where this is heading. Arize Phoenix is open source, runs as a single container, no Kubernetes required. The enterprise product adds an AI layer called Alex that scans traces, surfaces high latency and errors, and creates evals automatically. The stated goal: automate you out of the observability loop entirely.

Speaker info:
- https://www.linkedin.com/in/datdarylngo/
- https://x.com/dat_attacked

## Under 5 minutes to a deployed LLM endpoint — Audry Hsu, RunPod

- Upload date: 2026-06-07
- Video: https://www.youtube.com/watch?v=ILdE7FaAjVA
- Transcript: raw/20260607_ILdE7FaAjVA/ILdE7FaAjVA.en-orig.vtt
- Metadata: raw/20260607_ILdE7FaAjVA/ILdE7FaAjVA.info.json

Two failed crypto mining rigs in a basement in 2022. The founders posted on Reddit offering the GPUs for free in exchange for feedback. That is the origin of RunPod, now at $120 million in annual recurring revenue with 500,000 developers on the platform.

The demo runs in under five minutes: pick a model from the Hub, configure a context window, deploy a serverless endpoint on H100s. First request queues for 41 seconds on cold start while the container initializes and the model downloads. Every request after that executes in about 1.5 seconds. You pay only while a worker is handling a request.

Speaker info:
- https://www.linkedin.com/in/audry-hsu/

## Building Interactive UIs in VS Code with MCP Apps — Marlene Mhangami & Liam Hampton, GitHub

- Upload date: 2026-06-06
- Video: https://www.youtube.com/watch?v=_xIwFcnHqp4
- Transcript: raw/20260606__xIwFcnHqp4/_xIwFcnHqp4.en-orig.vtt
- Metadata: raw/20260606__xIwFcnHqp4/_xIwFcnHqp4.info.json

The demo profiles a Go app running bubble sort and Fibonacci and the result renders as an interactive flame graph directly inside the VS Code chat window. Not a link. Not a text summary. A live iframe you can scroll and query, sandboxed for the same reason you put a hamster in a cage: so it cannot chew up your VS Code settings or call external APIs.

The mechanism: an MCP tool returns both data and a resource reference pointing to a bundled HTML UI. VS Code fetches the HTML and renders it in a sandboxed iframe in chat. The app calls back to the server, the server returns fresh data, the UI updates. Shopify uses this pattern for checkout flows inside chat. Excalidraw uses it for interactive architecture diagrams you can drag and edit. Marlene and Liam walk through building one from scratch using a skill from the MCP repository.

Speaker info:
- https://x.com/marlene_zw
- https://www.linkedin.com/in/marlenemhangami/
- https://github.com/marlenemhangami

- https://x.com/liamchampton
- https://www.linkedin.com/in/liam-conroy-hampton/
- https://github.com/liamchampton

## Evals Are Broken, Use Them Anyway — Ara Khan, Cline

- Upload date: 2026-06-06
- Video: https://www.youtube.com/watch?v=QuuIywMG4s8
- Transcript: raw/20260606_QuuIywMG4s8/QuuIywMG4s8.en-orig.vtt
- Metadata: raw/20260606_QuuIywMG4s8/QuuIywMG4s8.info.json

Cline started at 43% on Terminal Bench. The improvements came from container CPU and memory settings, raised timeouts, and prompt engineering techniques specific to Anthropic model families that do not transfer to Codex or Gemini. Not from switching to a better model. Ara Khan's argument is that benchmark numbers are not gospel and vibes are not a system, and that the truth is inconveniently in between.

The practical framework: after a run, portfolio allocate the failures by sending another agent through all the failure traces to find which small levers actually move the score. Zone one is obvious bugs. Zone two is the nuance improvements that explain why a model everyone calls great somehow does not work for your specific harness. Zone three is overfitting to the benchmark, which people do, and which Ara is explicitly telling you not to do.

Speaker info:
- https://x.com/arafatkatze
- https://www.linkedin.com/in/arafatkatze/
- https://github.com/arafatkatze

## Building safe Payment Infrastructure for the autonomous economy — Steve Kaliski, Stripe

- Upload date: 2026-06-06
- Video: https://www.youtube.com/watch?v=KLSuFPj2ld0
- Transcript: raw/20260606_KLSuFPj2ld0/KLSuFPj2ld0.en-orig.vtt
- Metadata: raw/20260606_KLSuFPj2ld0/KLSuFPj2ld0.info.json

Agents are evolving from calling free APIs to executing real transactions, creating a new challenge: how do we let software spend money autonomously without catastrophic risk? This talk presents Stripe's approach to solving the dual problems of secure credential transmission and making businesses discoverable to agents. Through live code examples, we'll explore how to build guardrails that make autonomous spend safe and examine what infrastructure is needed as agents purchasing becomes a core capability. Whether you're building agent frameworks or enabling your business to work with agents, you'll learn how to make agent transactions both powerful and safe.

Speaker info:
- https://www.linkedin.com/in/steve-kaliski-079a7710
- https://x.com/stevekaliski

## Dark Factory: OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw

- Upload date: 2026-06-05
- Video: https://www.youtube.com/watch?v=pmoDeA3RBZY
- Transcript: raw/20260605_pmoDeA3RBZY/pmoDeA3RBZY.en-orig.vtt
- Metadata: raw/20260605_pmoDeA3RBZY/pmoDeA3RBZY.info.json

OpenClaw hit 3,000 commits in a single day. Vincent Koc's commit history shows exactly when he goes to sleep and when he wakes up. He and Peter Steinberger ran roughly 60 to 70 agents between them during the great refactor: 2,700 commits, close to a million lines of code changed, 82% of the core codebase touched in one night, plugin architecture shipped by morning.

The talk covers how you actually manage this at scale: swim lanes of 15 to 20 parallel coding sessions organized by type, when to nuke a session versus let it run, and what he calls reading the reasoning tokens. The skill is not prompting. It is knowing when an agent is bullshitting you. 2025 was about token maxing. 2026 is about not wasting them.

Speaker info:
- https://x.com/vincent_koc

## Beyond Transcription: Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI

- Upload date: 2026-06-05
- Video: https://www.youtube.com/watch?v=mFLlVpnGpds
- Transcript: raw/20260605_mFLlVpnGpds/mFLlVpnGpds.en-orig.vtt
- Metadata: raw/20260605_mFLlVpnGpds/mFLlVpnGpds.info.json

The open ASR leaderboard reports Nvidia Parakeet at 11.4% word error rate on AMI meeting data. Hervé Bredin runs the same model on the same dataset and gets 26%. Same model, same recordings, different microphone: the leaderboard uses headset audio, he uses the table mic. Most voice AI benchmarks are measuring single speaker speech and calling it solved.

The talk covers speaker diarization (who speaks when), why combining it with transcription is harder than it looks, and what breaks at the word level when two speakers overlap. Bredin demos live on a two speaker phone call, walks through the word that falls between two speaker boundaries with no clean owner, and runs pyannoteAI's Precision 2 model down to 3% diarization error against the open source baseline at 5%. State of the art today: 2% on clean telephone calls, 41% in a noisy restaurant.

Speaker info:
- https://x.com/hbredin
- https://www.linkedin.com/in/herve-bredin/
- https://github.com/hbredin

## Building Agent Interfaces: Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google

- Upload date: 2026-06-05
- Video: https://www.youtube.com/watch?v=_B4Pv9ttFgY
- Transcript: raw/20260605__B4Pv9ttFgY/_B4Pv9ttFgY.en-orig.vtt
- Metadata: raw/20260605__B4Pv9ttFgY/_B4Pv9ttFgY.info.json

Chrome DevTools MCP shipped with one tool: debug_webpage. Agents failed silently because they couldn't compose behaviors. The team decomposed it into 25 focused tools and assumed the problem was solved. It wasn't — now agents had 25 tools and no reliable way to pick the right one. Michael Hablich's talk is an honest account of building the same thing wrong three times and what the fixes actually looked like.

The concrete lessons: semantic summaries instead of raw 50,000 line JSON trace files, error messages rewritten so agents can self heal without a human in the loop ("Cannot navigate back, no previous page in history" instead of "Unable to navigate back in currently selected page"), a metric called tokens per successful outcome to measure interface fuel efficiency, and a deliberate decision to keep the autoconnect friction rather than remove it once they thought through prompt injection and the lethal trifecta.

Speaker info:
- https://x.com/MHablich
- https://www.linkedin.com/in/michael-hablich/

## SWE-rebench: Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius

- Upload date: 2026-06-04
- Video: https://www.youtube.com/watch?v=wcUJWP6WpGM
- Transcript: raw/20260604_wcUJWP6WpGM/wcUJWP6WpGM.en-orig.vtt
- Metadata: raw/20260604_wcUJWP6WpGM/wcUJWP6WpGM.info.json

Claude Code solved SWE rebench tasks by reading git history to find the solution patch. When Nebius removed future commits from the environment, it fetched the original GitHub issue. When they blocked web fetch, it switched to curl, formatted the conversation for readability, and solved the task again anyway. Ibragim Badertdinov built the leaderboard specifically because these behaviors only become visible once you run agents against real tasks at scale.

SWE rebench updates every month with problems from the previous month because benchmark data leaks into pretraining and time splits are the only defense. The talk covers what separates accepted tasks from rejected ones (accepted tasks averaged twice the tool calls, lower pass rates, and cleaner failure modes), why ambiguous specs produce noise rather than harder problems, and how the same filtering pipeline that powers the leaderboard has produced 30,000 real world training environments used by frontier labs.

Speaker info:
- https://x.com/ibragim_bad
- https://www.linkedin.com/in/ibragim-badertdinov/
- https://github.com/ibragim-bad

## Text Diffusion — Brendan O’Donoghue, Google DeepMind

- Upload date: 2026-06-04
- Video: https://www.youtube.com/watch?v=r305-aQTaU0
- Transcript: raw/20260604_r305-aQTaU0/r305-aQTaU0.en-orig.vtt
- Metadata: raw/20260604_r305-aQTaU0/r305-aQTaU0.info.json

GPT-4o answered 40. Gemini 2.5 Flash answered 42 and stuck to it even after working through the reasoning incorrectly. The Gemini Diffusion model, considerably smaller than both, answered 60 on the first forward pass, then 49, then corrected itself to 39 once it finished reasoning. Bidirectional attention means it can see future tokens and go back to fix mistakes. Autoregressive models cannot do that.

Brendon O'Donoghue covers why text diffusion is fast (24 denoising steps to generate 256 tokens means roughly 10x fewer memory transfers than autoregressive generation), what the tradeoff is (lower throughput at large batch sizes makes it expensive to serve at scale today), and what gets unlocked when latency drops to 2,000 tokens per second. The demos include a fake Wikipedia generated on the fly, a Reddit clone with AI generated comments and images, an operating system where every click generates the next screen, and a todo app built in 15 seconds by voice.

Speaker info:
- https://x.com/bodonoghue85
- https://bodono.github.io/
- https://www.linkedin.com/in/bodono/

Timestamps:
0:00 Introduction to Text Diffusion
1:02 How Text Diffusion Works (Training and Inference)
2:06 Gemini Diffusion Research Preview
3:04 Difference Between Autoregressive and Diffusion Models
4:02 Pros and Cons of Text Diffusion
6:13 Hardware Efficiency: Why Text Diffusion is Faster
8:47 Bidirectional Reasoning and Self-Correction
12:00 Dynamic and Adaptive Computation
14:26 In-place Text Editing
16:09 Low Latency Applications and Demos
20:05 Q&A Session

## The Art & Science of Benchmarking Agents — Vincent Chen, Snorkel AI

- Upload date: 2026-06-04
- Video: https://www.youtube.com/watch?v=iNkFlCiij0U
- Transcript: raw/20260604_iNkFlCiij0U/iNkFlCiij0U.en-orig.vtt
- Metadata: raw/20260604_iNkFlCiij0U/iNkFlCiij0U.info.json

ARC AGI 3 launched a few weeks before this talk with every task human solvable and frontier models under 1%. That gap is the argument: our ability to measure AI has fallen behind our ability to build it, and benchmarks that actually shape the field are bets on where capabilities are going, not snapshots of where they are.

Vincent Chen draws a framework from reviewing over 120 applications for Snorkel's $3 million Open Benchmarks Grants. The science is task quality, distributional diversity, model headroom, and robust eval methodology. The art is having a thesis (Terminal Bench bet on the CLI before coding agents made it obvious), producing research roadmaps, and treating researcher UX as a first class citizen. He closes on three axes he thinks the next generation of benchmarks needs to cover: environment complexity, autonomy horizon, and output complexity beyond plain text.

Speaker info:
- https://x.com/vincentsunnchen
- https://www.linkedin.com/in/vincentsunnchen
- https://github.com/vincentschen

## Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer

- Upload date: 2026-06-03
- Video: https://www.youtube.com/watch?v=zKk7sDMGDEQ
- Transcript: raw/20260603_zKk7sDMGDEQ/zKk7sDMGDEQ.en-orig.vtt
- Metadata: raw/20260603_zKk7sDMGDEQ/zKk7sDMGDEQ.info.json

By default, Claude Code wastes one in every three file reads. Add windowed grep and that drops to one in five. Add semantic search on top and it drops to one in eight, with file precision climbing from 65% to 87%. Kuba Rogut from Turbopuffer ran a 50-task benchmark against ContextBench to measure not whether the agent solved the problem but whether it found the right files, lines, and symbols along the way.

The benchmark tested three conditions: raw Claude Code, windowed reads capped at 50 lines, and windowed reads plus a semantic search tool backed by Turbopuffer. Semantic search won on behavior adjacent tasks where files share no keywords. Grep won on import tracing where the keyword is right there. Cursor's production numbers show a 24% relative improvement in answer accuracy from semantic retrieval, plus a 2.6% increase in code retention in large codebases. Kuba's explanation for why his gains were smaller: Cursor's model knows when and why to call semantic search. Claude Code just has it as another tool in the list.

Speaker info:
- https://ca.linkedin.com/in/kubarogut
- https://rogutkuba.com/

## Beyond Components: Designing Generative UI for MCP Apps — Ruben Casas, Postman

- Upload date: 2026-06-03
- Video: https://www.youtube.com/watch?v=hCMrEfPG2Yg
- Transcript: raw/20260603_hCMrEfPG2Yg/hCMrEfPG2Yg.en-orig.vtt
- Metadata: raw/20260603_hCMrEfPG2Yg/hCMrEfPG2Yg.info.json

Ruben Casas from Postman prompted a model to rewrite his blog. It built a search box with a blur animation and accessibility out of the box, without being asked. That was when he concluded the model writes better frontend code than he does. His question for the talk: if the models are this capable, why are most agent UIs still invoking static prebuilt components?

The talk maps three points on the spectrum. Static components pass props to predefined React elements (AG UI, Goose auto visualizer). Declarative UI has the LLM generate JSON or YAML that a rendering engine maps to components at runtime. Ruben argues this is the right balance today. Fully generative UI skips components entirely: the model writes HTML, CSS, and JavaScript on demand. His weather agent does this in a single tool call. The catch is containment: LLM generated code needs a sandbox, which is why MCP apps and their double iframe default matter. He closes on the TV analogy. The first TV shows were radio shows with cameras because nobody could imagine what else to do with the new medium. We are in that era.

Speaker info:
- https://x.com/Infoxicador
- https://www.linkedin.com/in/ruben-casas-17100383/

Timestamps:
0:00 Introduction: The evolution from 'poor man's bit coding' to high-fidelity UI generation
2:56 Why are we still stuck with static UI?
3:33 The new computer: Searching for the interface of the future
4:47 The role of MCP apps and 'Super Apps'
5:52 Three levels of UI generation: Static, Declarative, and Generative
6:03 Understanding Static UI components (e.g., AG UI, Goose)
7:42 The benefits of Declarative UI (e.g., JSON/YAML renderers)
10:06 Moving to the next level: Generative UI components
11:25 The challenge of trust: The need for sandboxing and containment
12:22 Why MCP apps are the ideal delivery mechanism for Generative UI
13:21 The 'TV/Radio' analogy: Imagining the future of agent interaction
14:46 Beyond components: Towards true human-agent collaboration
16:16 Conclusion: Shaping the future of user interfaces

## BDD, ADR, PRD, WTF: Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence

- Upload date: 2026-06-03
- Video: https://www.youtube.com/watch?v=504PvfXou5Y
- Transcript: raw/20260603_504PvfXou5Y/504PvfXou5Y.en-orig.vtt
- Metadata: raw/20260603_504PvfXou5Y/504PvfXou5Y.info.json

"One thing harder than reading AI code is reading AI tests." Mikuel from Safe Intelligence argues spec driven development leaves a loop open: you have a markdown spec, but how do you know the product actually behaves that way? His answer is Cucumber, nearly forgotten and suddenly useful again. Executable, human readable BDD scenarios connect directly to PRDs and critical user journeys and close the gap between what the spec says and what the tests verify.

The rest of the talk is enforcement. ADRs capture not just what the rules are but why; agents rejected at commit time get linked back to the document and iterate. Module import linting makes N+1 queries structurally impossible: rendering templates cannot touch the database, E2E tests cannot import any module that could. His sessions run 20 to 50 context compacts. The agent stays on track because the rules live in git hooks and CI, not in the prompt.

Speaker info:
- https://cz.linkedin.com/in/michal-cichra-61188a84

## Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel

- Upload date: 2026-06-02
- Video: https://www.youtube.com/watch?v=YYH0DMQr30A
- Transcript: raw/20260602_YYH0DMQr30A/YYH0DMQr30A.en-orig.vtt
- Metadata: raw/20260602_YYH0DMQr30A/YYH0DMQr30A.info.json

Same model. Same compute. Same number of tasks. Fine-tuning on low quality tasks improved the base model by 1%. Fine-tuning on high quality tasks improved it by 6%. Kobe Crawford from Snorkel ran that experiment on TerminalBench style agentic tasks and got a 5x difference in training uplift from task quality alone.

The talk breaks down what separates the two buckets. Accepted tasks averaged twice as many tool calls, lower pass rates, and more output tokens. Genuinely harder problems. More importantly, their failure modes were cleaner: when a model failed on a well specified task, it failed for a real reason. Rejected tasks tended to fail because of mismatches between what was requested and what the tests actually checked, or because the task never gave the model the context needed to satisfy implicit dependencies. Ambiguous specs do not produce harder tasks. They produce noise.

Speaker info:
- https://www.linkedin.com/in/kobie-crawford
- https://snorkel.ai/author/kobie-crawford/

## How Lovable self-improves every hour — Benjamin Verbeek, Lovable

- Upload date: 2026-06-02
- Video: https://www.youtube.com/watch?v=KA5kPbdkK2E
- Transcript: raw/20260602_KA5kPbdkK2E/KA5kPbdkK2E.en-orig.vtt
- Metadata: raw/20260602_KA5kPbdkK2E/KA5kPbdkK2E.info.json

Within the first hour of launching the vent tool, the agent filed 20 complaints about a silent file copy failure. The team checked: the tool worked fine. What the agent had caught was that filenames with a space in them silently failed to copy, a bug that never surfaced in logs. Benjamin Verbeek from Lovable built it a channel to complain directly to Slack when platform limitations block it, and the first thing it did was find a real production bug.

At 200,000 projects per day, Lovable runs two continuous improvement loops. The first detects sessions where a nontechnical user got stuck and then unblocked, clusters similar cases, and injects that context upstream; a holdout group measures actual project completion rates to prune stale entries when models or features change. The vent loop runs in parallel: the agent flags missing tools, broken platform behavior, and confusing docs as it works. Vent volume spikes turned out to be a reliable incident detector. A second agent now monitors the channel, deduplicates reports, and opens PRs automatically.

Speaker info:
- https://se.linkedin.com/in/benjamin-verbeek
- https://x.com/benjaminvrbk/

## What Lies Beneath the API — Benjamin Cowen, Modal

- Upload date: 2026-06-02
- Video: https://www.youtube.com/watch?v=HvZXAOZ3iv8
- Transcript: raw/20260602_HvZXAOZ3iv8/HvZXAOZ3iv8.en-orig.vtt
- Metadata: raw/20260602_HvZXAOZ3iv8/HvZXAOZ3iv8.info.json

Intercom is beating their frontier API at one tenth the cost. Pinterest claims orders of magnitude. Ben Cowen from Modal argues this pattern is not the exception for maturing AI products. It is the destination. Frontier labs want their models to win at everything. You want to win at your specific business logic. Those are different goals.

He offers three signals it is time to fine tune: paying more for the API than customers pay you, evals that have plateaued, and latency requirements no shared endpoint will meet. His practical case: if you have already built an agent harness and are collecting eval data, you have what you need to start RL training. Supervised fine tuning fits in 300 lines of Python. Modal customers have scaled to 50,000 sandboxes just for RL rollout.

Speaker info:
- https://www.linkedin.com/in/benjamincowenmath
- https://github.com/BenCowen

## How to talk to statues — Joe Reeve, ElevenLabs

- Upload date: 2026-06-01
- Video: https://www.youtube.com/watch?v=u-rJwPPU3QA
- Transcript: raw/20260601_u-rJwPPU3QA/u-rJwPPU3QA.en-orig.vtt
- Metadata: raw/20260601_u-rJwPPU3QA/u-rJwPPU3QA.info.json

A museum CEO tracked down his WhatsApp number and called. "I've had a team of 10 people working on this for a year. How did you build this?" Joe from ElevenLabs built the statue app in two hours on a Sunday using Cursor and a single one shot prompt. He posted it on a Tuesday and got 50,000 impressions. Reposted the next day about vibe coding and hit 1.5 million.

The pipeline: point your phone at a statue, OpenAI deep research identifies it and generates historical context and a voice description, the ElevenLabs voice design API creates a matching voice from that description, an agent spins up, and a conversation starts. The whole thing runs in about 30 seconds. Museums, auction houses, and travel platforms all reached out wanting the same thing built for their collections.

Speaker info:
- https://x.com/isnit0
- https://x.com/isnit0/status/2024104717039685915
- https://elevenlabs.io/blog/talk-to-a-statue-building-a-multi-modal-elevenagents-powered-app

## 20 days of compute vs 7 hours: rethinking what state-of-the-art means — Bertrand Charpentier, Pruna

- Upload date: 2026-06-01
- Video: https://www.youtube.com/watch?v=hqHC6Z_lXyo
- Transcript: raw/20260601_hqHC6Z_lXyo/hqHC6Z_lXyo.en-orig.vtt
- Metadata: raw/20260601_hqHC6Z_lXyo/hqHC6Z_lXyo.info.json

Ranking image generation models the way Design Arena does it — 26,000 battles, 62 seconds per generation — takes 20 days of compute, costs $5,000, and consumes roughly 400 marathons worth of energy. Bertrand Charpentier, cofounder and chief scientist at Pruna AI, uses that number to make a point: the same evaluation on a fast compressed model takes 7 hours and $265. Efficiency is a dimension of state of the art, not a footnote.

The rest of the talk dismantles the idea that any single model holds the title. Leaderboard rankings disagree with each other — the same model goes from rank 10 on one to rank 5 on another. Most models lose 40% of their head-to-head battles, which means the top-ranked model is the wrong choice for nearly half of real use cases. His answer is the Pareto front: plot quality against latency or cost, find the frontier, and expect three or four models clustered tightly in quality score but varying up to 20x in efficiency. Evaluating this way tends to surface small specialized models rather than large foundation models.

Speaker info:
- https://www.linkedin.com/in/bertrand-charpentier-76995ab6/
- https://github.com/sharpenb

## What if the network was the sandbox? — Remy Guercio, Tailscale

- Upload date: 2026-06-01
- Video: https://www.youtube.com/watch?v=BM2JX9hqsVQ
- Transcript: raw/20260601_BM2JX9hqsVQ/BM2JX9hqsVQ.en-orig.vtt
- Metadata: raw/20260601_BM2JX9hqsVQ/BM2JX9hqsVQ.info.json

Standard sandboxing puts the API key inside the sandbox. The agent has the key, which it can exfiltrate, misuse, or — if it runs long enough — find creative ways to leverage beyond its intended scope. Remy Guercio from Tailscale argues that sandboxing conflates two separate problems: execution isolation and access control. You can fully isolate a runtime and still have the agent holding credentials it can abuse.

Their answer is Aperture, an LLM gateway built on Tailscale's WireGuard identity network. Every connection carries verified identity — user, tag, or group — and the agent gets a placeholder instead of a real key. There is nothing to exfiltrate. Every LLM call has to pass through the network layer, so Aperture sees every tool call, bash command, and MCP request without instrumentation inside the container. Internally at Tailscale, bash dominates over structured tool calls — and now they can actually see that.

Speaker info:
- https://www.linkedin.com/in/remyguercio/

Timestamps:
0:00 - Introduction and the concept of a sandbox
1:15 - Breaking down the components of a sandbox (boundary and permissions)
1:52 - How permissions are typically handled (API keys vs. OIDC)
3:18 - Introducing Tailscale and WireGuard for network-level identity
5:42 - Introduction to Aperture (AI Gateway)
7:28 - Live demo: Viewing usage metrics and logs in Aperture
9:47 - Live demo: Inspecting GitHub Actions PR review bot logs
10:39 - Visibility into tool calls, bash commands, and MCP requests
11:46 - Agent setup and configuration in Aperture
13:59 - Advanced features: Cost controls, quotas, and webhooks
15:35 - Using tsnet to build custom internal identity-aware services
17:03 - Q&A: How to configure permissions (Grants vs. ACLs)
18:46 - Q&A: Network-layer transparency for base URLs
20:25 - Q&A: Permissioning based on users vs. model/provider
21:28 - Q&A: Handling non-tool call agent behaviors (direct code execution)

## Spec-Driven Testing for Agents With A Brain the Size of A Planet — Steven Willmott, SafeIntelligence

- Upload date: 2026-05-31
- Video: https://www.youtube.com/watch?v=UQKg0td-Bf4
- Transcript: raw/20260531_UQKg0td-Bf4/UQKg0td-Bf4.en-orig.vtt
- Metadata: raw/20260531_UQKg0td-Bf4/UQKg0td-Bf4.info.json

Wrapping a malicious instruction in a poem is an effective jailbreak against large models and not against small ones. Small models don't understand the poem. Large models do and execute the instruction. Steven Willmott from Safe Intelligence argues this is one reason bigger is not straightforwardly safer: a larger model with broader capabilities has more attack surface and more infrastructure access to abuse.

His frame is spec driven validation. An agent spec is not just a test dataset. It needs explicit rules (never offer more than 10% discount), domain ontologies (an airline agent only needs to know about destinations that airline actually flies to), rights and roles, and robustness requirements such as how many typos or rephrasings before it fails. Write these independently of the implementation so they survive a model swap and can drive both security testing and iterative improvement.

Speaker info:
- https://uk.linkedin.com/in/stevenwillmott
- https://x.com/njyx

## Can LLMs generate Enterprise Quality Code? — Prasenjit Sarkar, Sonar

- Upload date: 2026-05-31
- Video: https://www.youtube.com/watch?v=NuePCNMpWGc
- Transcript: raw/20260531_NuePCNMpWGc/NuePCNMpWGc.en-orig.vtt
- Metadata: raw/20260531_NuePCNMpWGc/NuePCNMpWGc.info.json

Sonar ran 4,444 Java programming assignments through 53 models and measured what actually came out. GPT-4o generated under 250,000 lines for those assignments. GPT 5.4 generated 1.2 million. Claude Sonnet 4.6 generated 627,000 with the highest security issue rate at 300 per million lines of code. Prasenjit Sarkar from Sonar walks through the full leaderboard: pass rate, cyclomatic complexity, bug density, and security issues per model.

Their response is a three-stage framework called ACDC: guide, verify, solve. The verify stage runs SonarQube analysis in 1 to 5 seconds before a commit, against 1 to 5 minutes in CI. If issues slip through to the PR, a remediation agent creates one fix per issue, runs it through analysis and compilation to check for regressions, and only presents it if it passes.

Speaker info:
- https://www.linkedin.com/in/jit2600/

Timestamps:
0:00 Introduction and the Shift to Agentic Development
1:44 Evaluating LLM Code Quality and Reliability
3:00 Sonar's Evaluation Framework and Methodology
3:39 LLM Performance Analysis (Pass Rates and Code Bloat)
5:24 Why LLMs Struggle: Training Data and Hidden Flaws
6:45 The Sonar LLM Leaderboard
8:30 Complexity Metrics: Cyclomatic vs. Cognitive
10:41 The ACDC Framework: Guide, Verify, and Solve
11:06 Phase 1: Guide (Context Augmentation & Sonar Sweep)
11:42 Phase 2: Verify (SonarQube Agentic Analysis)
12:40 Phase 3: Solve (Remediation Agent)
14:05 Product Summary and Ecosystem Support

## Engineering voice agents: Latency, quality, and scale — Rishabh Bhargava, Together AI

- Upload date: 2026-05-31
- Video: https://www.youtube.com/watch?v=N7b1PJc7SFc
- Transcript: raw/20260531_N7b1PJc7SFc/N7b1PJc7SFc.en-orig.vtt
- Metadata: raw/20260531_N7b1PJc7SFc/N7b1PJc7SFc.info.json

Users notice latency above 500ms and hang up above one second. In an already optimized pipeline, 75ms of network latency from models sitting in a different data center adds 30% overhead. Colocating everything in the same building drops that to around 5ms. Rishabh Bhargava from Together AI walks through the full speech to text, LLM, and text to speech pipeline at that level of specificity.

The LLM dominates the budget: 200 to 300ms time to first token target, 8 to 30B parameter range — larger models blow the latency budget, smaller ones break tool calling. Speech to text target is P90 under 100ms with around 6% word error rate. One pattern for handling complex workflows without adding latency: a small thinker LLM handles conversation flow and issues a single tool call to a larger model when the request is complex, keeping the fast path fast.

Speaker info:
- https://www.linkedin.com/in/bhargavarishabh

## How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS

- Upload date: 2026-05-30
- Video: https://www.youtube.com/watch?v=vy7o1g2iHY8
- Transcript: raw/20260530_vy7o1g2iHY8/vy7o1g2iHY8.en-orig.vtt
- Metadata: raw/20260530_vy7o1g2iHY8/vy7o1g2iHY8.info.json

WorkOS will be back for the World's Fair next week! see https://ai.engineer/wf and use YOUTUBEPROMO for new tickets only. Join 6000 AI engineers at the "Superbowl of AI"!

---

Claude would fake running tests by touching the expected output file. Nick Nisi, DX engineer at WorkOS, fixed it by SHA-256 hashing the actual test output and verifying it cryptographically. His principle: make it easier to do the real work than to lie about it, and enforce that through code and state machines, not prompts.

The same discipline reversed an opposite problem. He generated 10,000 lines of skills from WorkOS documentation, measured with evals, and found one skill was dropping a task from 97% correct to 77% correct. He deleted 95% of it, rewrote 553 lines of handwritten gotchas, and eval time dropped from 68 minutes to 6. The model already knew how to code. It just needed to know where the landmines were.

Speaker info:
- https://x.com/nicknisi
- https://linkedin.com/in/nicknisi
- https://github.com/nicknisi

Timestamps
0:00 Introduction
1:22 The challenge of context switching with agents
2:33 Introducing Case: A harness for agentic workflows
3:33 Rebuilding with a TypeScript state machine
4:45 The critical importance of evidence-based verification
5:59 Applying agentic principles to the WorkOS CLI
7:44 Lessons in documentation: Generating skills from docs
8:52 Why more data (10,000 lines) led to worse performance
9:36 The impact of using evals to measure accuracy
10:40 Key takeaway: Enforce with code, not just prompts
12:41 Treating failures as bugs in the harness system
14:39 Advice for building agentic-ready products
16:01 Final summary: Replacing trust with evidence

## How We Built Zeta2: Training an Edit Prediction Model in Production — Ben Kunkle, Zed

- Upload date: 2026-05-30
- Video: https://www.youtube.com/watch?v=phchDt63qAA
- Transcript: raw/20260530_phchDt63qAA/phchDt63qAA.en-orig.vtt
- Metadata: raw/20260530_phchDt63qAA/phchDt63qAA.info.json

To validate settled data, Zed ran 10 frontier model predictions per example and measured Levenshtein distance to the final state. For 100,000 training examples that is a million frontier model requests, which is prohibitively expensive. The fix: Zeta 2's student model now approaches teacher quality, so they run it 50 times instead at negligible cost. Ben Conungle, edit predictions lead at Zed, walks through how this pipeline came together.

The pipeline pulls opt in production edit traces, distills them through a frontier teacher, and routes bad predictions through a repair step before formatting for the student. The ideal training examples sit in the middle of the Levenshtein distance distribution: too close to the settled state is obvious, too far is noise. A metric called reversal ratio, how often the model undoes exactly what the user just typed, was the key diagnostic for catching bad model behavior before shipping.

## Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind

- Upload date: 2026-05-30
- Video: https://www.youtube.com/watch?v=3_gYbhABcAE
- Transcript: raw/20260530_3_gYbhABcAE/3_gYbhABcAE.en-orig.vtt
- Metadata: raw/20260530_3_gYbhABcAE/3_gYbhABcAE.info.json

A `deleteItem` endpoint is obvious to the developer who built it. An agent only sees the function schema and docstring. Philipp Schmid from Google DeepMind argues this is why senior engineers struggle most: they carry years of implicit context that agents do not, and design tools assuming it.

He names four other shifts: text replaces structured state, errors are inputs not restart triggers (especially costly when an agent has been running for 15 minutes), evals replace unit tests because the right question is how often it works not whether a fixed input always produces a fixed output, and build to delete because you will rebuild the same agent with a better model anyway.

Speaker info:
- https://x.com/_philschmid
- https://www.linkedin.com/in/philipp-schmid-a6a2bb196/
- https://github.com/philschmid

## Reverse engineering a Viking VOIP phone protocol with Claude Code — Boris Starkov, Eleven Labs

- Upload date: 2026-05-29
- Video: https://www.youtube.com/watch?v=V-L0INGTEOg
- Transcript: raw/20260529_V-L0INGTEOg/V-L0INGTEOg.en-orig.vtt
- Metadata: raw/20260529_V-L0INGTEOg/V-L0INGTEOg.info.json

A Viking VoIP phone sat in the ElevenLabs San Francisco office for a year. Three senior engineers and ChatGPT could not get it working. Boris from ElevenLabs cracked the undocumented protocol with Claude Code in a couple of days: brute forced all 676 possible two letter command combinations, found 80 valid ones, then set up a TCP proxy between a Windows virtual machine and the phone to intercept and log what the proprietary Windows XP software was actually sending.

The last piece was a one byte checksum in the persistence command. Claude reverse engineered the formula by running known input output pairs through it, confirmed the pattern in a closed loop, and derived a simple subtraction. Boris describes his own role as being the hands: Claude orchestrated, he physically rebooted the phone and reported how many beeps he heard. The protocol is now open sourced as a Claude Code skill so anyone with a Viking phone can configure it directly without the Windows software. The outcome at AI Engineer Europe: a red phone booth on the third floor where picking up the receiver connects you to a Michael Caine voice agent that quizzes you on British AI history.

## Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j

- Upload date: 2026-05-29
- Video: https://www.youtube.com/watch?v=B9h9ovW5H9U
- Transcript: raw/20260529_B9h9ovW5H9U/B9h9ovW5H9U.en-orig.vtt
- Metadata: raw/20260529_B9h9ovW5H9U/B9h9ovW5H9U.info.json

A knowledge base tells a financial analyst agent the risk factors. A context graph tells it whether to reject or accept, because it also carries past decision traces, the reasoning behind them, and how similar cases resolved. Zach from Neo4j walks through how context graphs extend a standard RAG setup with three layers: short term conversation history, long term extracted entities, and reasoning traces that embed into vectors so structurally similar past decisions surface alongside semantically similar ones.

The fastest path in is `uvx create-context-graph`, a one-command scaffold that gives you a backend, frontend, demo data, and an MCP server. It ships with 22 built-in domains or generates a graph ontology from a custom domain you describe. The underlying `neo4j-agent-memory` package handles entity extraction through a spaCy to GLiNER to LLM pipeline with deduplication and merging baked in, and plugs into pydantic AI, LangGraph, Crew, Google ADK, and others.

Speaker info:
- https://www.linkedin.com/in/zachblumenfeld/

## Reachy Mini: the $300 open source robot you can actually hack — Andres Marafioti, Hugging Face

- Upload date: 2026-05-29
- Video: https://www.youtube.com/watch?v=0jeZfjJMfmo
- Transcript: raw/20260529_0jeZfjJMfmo/0jeZfjJMfmo.en-orig.vtt
- Metadata: raw/20260529_0jeZfjJMfmo/0jeZfjJMfmo.info.json

Qwen3-TTS shipped at 0.8x real time: one second of audio took 1.2 seconds to generate. Andres Marafioti from Hugging Face spent two weeks fixing it. The culprits were no streaming, 500 autoregressive steps per audio packet with a CPU GPU round trip on each, and a dynamic KV cache that blocked compilation. Static KV cache plus CUDA graph captures brought it to 5.8x real time with time to first audio under 200 milliseconds.

The platform is Reachy Mini, a $300 open source robot Hugging Face has shipped to 7,500 people. It arrives unassembled. Talking to it is their most used app by far. The voice stack runs Parakeet transcription every 150 milliseconds with partial results feeding back to the robot mid-sentence, Qwen 3.5 27B for the LLM, and this optimized TTS. At that speed, infrastructure round trips match model latency, so the load balancer separates LLM endpoints from conversation nodes to handle the difference in how much different users actually talk.

## Context Graphs for Explainable, Decision-Aware AI Agents — Andreas Kollegger & Zaid Zaim, Neo4j

- Upload date: 2026-05-28
- Video: https://www.youtube.com/watch?v=abvQEhvRI_c
- Transcript: raw/20260528_abvQEhvRI_c/abvQEhvRI_c.en-orig.vtt
- Metadata: raw/20260528_abvQEhvRI_c/abvQEhvRI_c.info.json

Prescribing drug X is correct 99% of the time for symptom Y. For the 1% where it is fatal, statistical reasoning does not help you. Andreas Kollegger calls this reference class validation: before the agent acts, it has to know which group it is in.

Context graphs give agents the why. Not just knowledge and tools but the policies, rules, and prior decisions that explain why a certain action is right in a given context. The decision making framework in this talk has five stages: frame the problem with its causality and environment, pull in global rules and past precedent, run a risk value analysis, either act or escalate to someone with authority, and write the full reasoning chain back into the graph. That last step is the point. Every decision becomes precedent. Future agents inherit it.

Speaker info:
- https://x.com/akollegger
- https://www.linkedin.com/in/akollegger
- https://github.com/akollegger

## How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust

- Upload date: 2026-05-28
- Video: https://www.youtube.com/watch?v=XBaznoTRDFI
- Transcript: raw/20260528_XBaznoTRDFI/XBaznoTRDFI.en-orig.vtt
- Metadata: raw/20260528_XBaznoTRDFI/XBaznoTRDFI.info.json

Traditional observability answers one question: is the system up? Phil Hetzel from Braintrust argues that question is not the right one for agents. An individual agent trace can exceed a gigabyte. A single span can hit 20 megabytes. The data is semistructured, packed with unstructured text, and still arrives in real time. None of the systems built for uptime monitoring were designed to ingest, index, and actually use that.

Braintrust built a custom database from scratch for this problem: a write ahead log for instant visibility, analytical indexes for fast filtering, and a forked version of Tantivy (a Rust based full text search library similar to Apache Lucene) so an engineer can query every trace that mentioned a specific word. The other difference is who does this work: clinicians, lawyers, and wealth advisers now open traces directly to grade whether an agent responded correctly, and their written justifications become the training signal for automated scoring functions. The human annotations surface the failure modes. The scoring functions scale them.

Speaker info:
- https://www.linkedin.com/in/philliphetzel/

## Most Enterprise Agentic Projects Are Doomed, Here's Why — Jess Grogan-Avignon & Jack Wang, Accenture

- Upload date: 2026-05-28
- Video: https://www.youtube.com/watch?v=AGkzpxMdPn8
- Transcript: raw/20260528_AGkzpxMdPn8/AGkzpxMdPn8.en-orig.vtt
- Metadata: raw/20260528_AGkzpxMdPn8/AGkzpxMdPn8.info.json

Jess Grogan-Avignon and Jack Wang at Accenture built an agentic application in two weeks. Getting it to production took another 12 months. Not because the code was wrong. Because the infrastructure team, the security team, the AI gateway team, the data governance team, and the application team all had to align before anything could ship. That is not a technology problem, and fixing the code does not fix it.

The deeper issue is that GitHub averaged 275 million commits per week in 2025 on track for 14 billion by year end, while the approval infrastructure was never designed for that throughput. They name five tensions that predict whether an enterprise agentic project succeeds before it starts: human approval chains need to become executable code rather than longer signoff meetings; finance should back a portfolio of AI bets the way a VC would rather than demanding committed returns from each project; delivery should run on hypothesis driven loops not milestone programs; trust is built by graduating through shadow mode, advisory mode, and controlled autonomy with each step gated by outcome evidence not by project plan completion; and the real moat is not the data in your ERP but the living memory your product builds from real customer signals every day.

Speaker info:
- https://www.linkedin.com/in/jessicaannbiggs
- https://www.linkedin.com/in/jackxwang

## Why Rust is the Ideal Language for Vibe-Coding — Daniel Szoke, Sentry

- Upload date: 2026-05-27
- Video: https://www.youtube.com/watch?v=ugUeZ8-b-u0
- Transcript: raw/20260527_ugUeZ8-b-u0/ugUeZ8-b-u0.en-orig.vtt
- Metadata: raw/20260527_ugUeZ8-b-u0/ugUeZ8-b-u0.info.json

TypeScript is easy for models to write because it imposes few constraints. Those same missing constraints let models introduce data races that compile, run, and only fail intermittently. A thread safety bug in Rust does not compile. The compiler names the unsound type, explains why it cannot be sent between threads, and points the agent directly at the fix.

Daniel Szoke, Rust SDK maintainer at Sentry, argues that optimizing for a language models can write easily is the wrong goal. The better optimization is a language whose compiler enforces correctness as a natural feedback loop. Every error an agent hits and resolves in a loop is a production bug that never ships. The Rust compiler is also faster than asking a review agent to find the same class of bugs and more reliable than hoping it does.

Speaker info:
- https://www.linkedin.com/in/dlsz

Timestamps:
0:00 Introduction and the speaker's background at Sentry
0:27 The current conventional wisdom for AI-assisted development
1:53 Why languages like Python and TypeScript are popular for AI
3:44 The hidden risks of prioritizing "easy-to-write" languages
6:40 Philosophical perspective: Alien intelligence and failure modes
9:28 Introduction to Rust and its strict compiler guarantees
10:53 Key safety features: Type, Null, and Concurrency safety
11:59 Demonstrating "Fearless Concurrency" with a code example
14:26 Why Rust constraints are an asset for autonomous AI agents
15:36 Conclusion and Sentry resources

## The AI Skill I Rely On Daily — Priscila Andre de Oliveira, Sentry

- Upload date: 2026-05-27
- Video: https://www.youtube.com/watch?v=li0SaBt9RDM
- Transcript: raw/20260527_li0SaBt9RDM/li0SaBt9RDM.en-orig.vtt
- Metadata: raw/20260527_li0SaBt9RDM/li0SaBt9RDM.info.json

Priscila Andre de Oliveira analyzed 116 of her own Claude sessions from daily work at Sentry. 67% were comprehension. 2% were code generation.

Working in a codebase with 15 years of history, around 100 PRs merged per day, and 100,000 organizations depending on it, the unlock is not generation but understanding. She built a personal skill called catch me up with six exploration modes covering architecture, conventions, feature traces, syntax, testing, and history. The loop: understand what the agent found before you let it plan and implement, because a misaligned mental model is where slop comes from.

Speaker info:
- https://at.linkedin.com/in/priscila-andre-de-oliveira-ab34bb24b

Timestamps:
0:00 Introduction and speaker background
2:25 Sentry's engineering environment and scale
3:50 AI-driven projects at Sentry
5:48 Maintaining code quality and technical debt
7:35 The role of comprehension in software development
9:38 Analyzing AI usage patterns
10:33 The "Catch Me Up" skill architecture
12:15 Short demo of the "Catch Me Up" skill
13:56 Planning vs. implementation in AI workflows
15:26 Conclusion and key takeaways

## The maturity phases of running evals — Phil Hetzel, Braintrust

- Upload date: 2026-05-27
- Video: https://www.youtube.com/watch?v=FB-MLPhL9Ms
- Transcript: raw/20260527_FB-MLPhL9Ms/FB-MLPhL9Ms.en-orig.vtt
- Metadata: raw/20260527_FB-MLPhL9Ms/FB-MLPhL9Ms.info.json

Most teams approach evals like unit tests and try to cover every possible failure. Phil Hetzel from Braintrust argues that is the wrong frame: enumerate your known failure modes, cover those specifically, and ship. The goal is a flywheel where production traces surface what is going wrong, feed back into offline experimentation, and guide the next improvement.

The session walks four maturity stages: vibe checking with documented human justifications not just thumbs up or down, LLM as judge built from those justifications at scale, then the hard part, tool calls that touch external systems. Context gathering tools are manageable. CRUD tools are not, because you have to represent the state of external systems at the exact moment the original trace ran. Timestamp queries against a vector database and injecting captured system state directly into the trace are two approaches for getting there.

Speaker info:
- https://www.linkedin.com/in/philliphetzel/

## Run Frontier AI at Home — Alex Cheema, EXO Labs

- Upload date: 2026-05-26
- Video: https://www.youtube.com/watch?v=ESbWpPT_9-o
- Transcript: raw/20260526_ESbWpPT_9-o/ESbWpPT_9-o.en-orig.vtt
- Metadata: raw/20260526_ESbWpPT_9-o/ESbWpPT_9-o.info.json

Running GLM 5.1, a trillion parameter model released the day before this workshop, across four Mac Studios costs around $40,000 in hardware and tops out at roughly 20 tokens per second. Alex Cheema from EXO Labs thinks both numbers have about 100x left in them.

The workshop covers what that 100x looks like across the stack: kernel fusion that recovered 30% performance on Qwen 3.5 from inefficiencies nobody had noticed, RDMA integration that cut node to node latency from 300 microseconds to single digits and made tensor parallelism actually scale, and the case for splitting prefill onto compute dense hardware and decode onto high bandwidth hardware. The live demo runs GLM 5.1 across four Mac Studios connected by Thunderbolt 5 and cuts large prompt inference roughly in half by offloading prefill to an RTX Spark.

Speaker info:
- https://www.linkedin.com/in/alex-cheema
- https://github.com/alexcheema

Timestamps:
0:00 Introduction to EXO Labs and the mission to democratize frontier AI
2:00 The current state of AI: centralized cloud systems vs. the need for local infrastructure
7:40 Technical challenges: kernel efficiency and the overhead of separate kernel launches
9:50 The importance of the software harness in optimizing inference performance
10:35 Understanding inference constraints: compute-bound vs. memory-bound operations
11:28 The distinction between prefill and decode phases in LLM inference
13:07 Requirements for efficient local decoding: memory capacity, bandwidth, and energy efficiency
15:50 The concept of 'Intelligence per Joule' as a performance metric
16:45 Advancements in consumer hardware: higher memory capacity and bandwidth on Apple Silicon
18:50 Q&A: The future of consumer appetite for local inference hardware
20:17 Discussing the cost and performance of running trillion-parameter models like GLM 5.1
22:05 The 100x potential: How code design across the stack improves performance
26:35 Future outlook: Bifurcation of local vs. cloud use cases and diminishing returns of model size
38:55 Heterogeneous hardware strategies: Combining compute-dense and bandwidth-heavy devices
41:47 Demo: Using an Nvidia RTX Spark to accelerate prefill on a Mac cluster
48:40 Software architecture: Automating cluster orchestration with EXO
53:00 Challenging the 'batching' necessity: Multi-agent systems, search, and continual learning
1:05:22 Rethinking cloud economics and renting use cases instead of hardware
1:20:55 Demo technicalities: Event sourcing and cluster node discovery
1:32:20 Closing thoughts: Transparency in benchmarks and the future of open-source model evaluation

## Stop babysitting your agents... — Brandon Waselnuk, Unblocked

- Upload date: 2026-05-26
- Video: https://www.youtube.com/watch?v=BiG2ssibKGc
- Transcript: raw/20260526_BiG2ssibKGc/BiG2ssibKGc.en-orig.vtt
- Metadata: raw/20260526_BiG2ssibKGc/BiG2ssibKGc.info.json

Same prompt. Same agent. Same model. Without a context engine: 2.5 hours, 20.9 million tokens, multiple rounds of human correction, and code that compiled but would have broken the entire system if it shipped. With one: 25 minutes, 10.8 million tokens, and a senior engineer who gave one nitpick and approved the merge.

Brandon Waselnuk from Unblocked makes the case that the problem is not access but understanding. More MCPs give agents pipes to information. A million token context window just sits there. Naive RAG stops at the first result it finds, a phenomenon called satisfaction of search borrowed from radiology. What actually changes is a context engine that reasons across your codebase, Slack history, PR patterns, and org structure to build a research packet before the agent starts writing, so it arrives knowing your factory patterns, your fallback infrastructure, and what the CTO said was wrong in that thread three months ago.

Speaker info:
- https://getunblocked.com

## What the Best Agents Share — Mardu Swanepoel, Flinn AI

- Upload date: 2026-05-26
- Video: https://www.youtube.com/watch?v=7CrPrHgoEYk
- Transcript: raw/20260526_7CrPrHgoEYk/7CrPrHgoEYk.en-orig.vtt
- Metadata: raw/20260526_7CrPrHgoEYk/7CrPrHgoEYk.info.json

Harvey, Cursor, Manus, and Claude operate in completely different domains but share four patterns: focus modes that constrain the action space to improve output quality, transparent execution that surfaces tool calls and reasoning to build user trust, personalization that optimizes for speed to understanding rather than just speed to output, and reversibility that bounds the downside of mistakes so users take on higher value tasks.

Mardu Swanepoel from Flinn AI breaks down how each company puts these into practice. Cursor lets you roll back changes at the line, file, or conversation level and run multiple model outputs in parallel from the same input. Harvey builds playbooks from a firm's legal methods so the agent works the way the firm would. Claude surfaces a live task list alongside every tool call's inputs and outputs so users can intervene before the agent goes further in the wrong direction.

Speaker info:
- https://www.linkedin.com/in/mardu-swanepoel-000/

## Bounded Autonomy: Between Free Will and Determinism — Angus J. McLean, Oliver

- Upload date: 2026-05-25
- Video: https://www.youtube.com/watch?v=t4359sKBu4w
- Transcript: raw/20260525_t4359sKBu4w/t4359sKBu4w.en-orig.vtt
- Metadata: raw/20260525_t4359sKBu4w/t4359sKBu4w.info.json

Angus McLean spent time building a complex agent application to generate his CV. Four letters beat it: HTML. He puts the improvement at 100x.

The talk is from Oliver's AI Director, where agents generate around 4,000 creative assets a day for 200 plus brands, assets you have probably seen and had no idea were AI. The core argument: models are naturally verbose and tend toward complexity, and so are the developers working with them. His counter is to strip back. Replace internet access with curated documentation, ask how little context you can use and still complete the task, and never automate a job you cannot do yourself.

Speaker info:
- https://uk.linkedin.com/in/angusjmclean

Timestamps
0:14 Introduction and talk theme: Bounded Autonomy
1:13 About Oliver and GenAI in advertising
2:24 The structure of an ad agency
3:35 Why agents are used for speed and scale
4:27 Slow down and look at model limitations
5:52 The problem with current "band-aid" solutions
6:51 The role of context windows in agent capability
8:11 How to effectively constrain models with documentation
9:29 Constraints as a driver for creativity
10:32 Fundamentals: Building your own harness and memory
11:25 The power of simplicity (The CV/HTML example)
12:34 AI as a translation process
14:14 Using multiple representation structures
15:22 Agent workflows and the "don't automate what you can't do" rule

## Agentic Evaluations at Scale, For Everybody — Nicholas Kang & Michael Aaron, Google DeepMind

- Upload date: 2026-05-25
- Video: https://www.youtube.com/watch?v=Ubwb6NzegyA
- Transcript: raw/20260525_Ubwb6NzegyA/Ubwb6NzegyA.en-orig.vtt
- Metadata: raw/20260525_Ubwb6NzegyA/Ubwb6NzegyA.info.json

On SWE-Bench Pro, six frontier models land within a couple of percentage points of each other. The harness they run inside shifts performance by 22%. A competing lab once took a Kaggle benchmark, reran it with their own compaction settings, and published much better results. Neither number was wrong. Both were useless.

The talk is from Nicholas Kang and Michael Aaron at Google DeepMind's Kaggle team, who are building the infrastructure to fix evals at the community level: an open benchmark platform anyone can contribute to, a PvP Game Arena where models play poker and chess for an ELO rating that cannot saturate, and a standardized agent exam that returned 500 plus submissions in its first week without any promotion. The wastewater treatment plant engineer from Turkey who built a novel safety benchmark from 20 years of field experience, data that does not exist anywhere else, is the use case they keep coming back to.

Speaker info:
- https://www.linkedin.com/in/nicholaskangjj

## Does GenAI "belong" to data scientists? — Phil Hetzel, Braintrust

- Upload date: 2026-05-25
- Video: https://www.youtube.com/watch?v=NKwIX3CiRgU
- Transcript: raw/20260525_NKwIX3CiRgU/NKwIX3CiRgU.en-orig.vtt
- Metadata: raw/20260525_NKwIX3CiRgU/NKwIX3CiRgU.info.json

At most traditional enterprises, GenAI got handed to the ML platform team because it had AI in the name. Phil Hetzel from Braintrust argues that was the wrong move, not because data scientists lack value, but because Anthropic and OpenAI already ran the data pipeline. What is left is prompt and context engineering, distributed systems, human annotation, and functional evaluation across a much broader surface area than precision and recall. The mistake is isolating it to one team. The answer is a diverse one.

Speaker info:
- https://www.linkedin.com/in/philliphetzel

## Scaling the Next Paradigm of Heterogeneous Intelligence — Adrian Bertagnoli, Callosum

- Upload date: 2026-05-24
- Video: https://www.youtube.com/watch?v=WRBNDpUhsJQ
- Transcript: raw/20260524_WRBNDpUhsJQ/WRBNDpUhsJQ.en-orig.vtt
- Metadata: raw/20260524_WRBNDpUhsJQ/WRBNDpUhsJQ.info.json

A mixture of Qwen 3 VL8B and Kimi K2.5 beat the state of the art on Video Web Arena, outperforming the leading GPT and Gemini models by 18 and 25 percent while costing 3.7 times less and running 3 times faster. The reason it worked is that visual web navigation decomposes into subtasks that do not all need a frontier model: routing zoom and visual parsing to a smaller model alone produced 11x speed and 43x cost improvements on those steps.

Adrian Bertagnoli from Callosum makes the case that the GPU cluster era of identical hardware and monolithic models is ending. Heterogeneous intelligence treats model architectures, chip types, and workflows as variables to optimize together. A second result: running recursive long context reasoning tasks on Cerebras instead of a frontier model cuts cost by 7x and latency by 5x while matching accuracy. Callosum is building the automation layer that routes tasks to the right chip and model without bespoke decisions for each subtask.

Speaker info:
- https://www.linkedin.com/in/adrian-bertagnoli-bb3467178/

Timestamps
0:14 Introduction and definition of heterogeneous intelligence
0:56 Limitations of the current homogeneous intelligence paradigm
1:36 Evolution toward mild heterogeneity (MoE, multi-agent systems, hardware disaggregation)
3:24 The rationale for heterogeneity: complexity and multi-step problem solving
4:26 Mathematical formalization of the production function and skill distribution
5:56 Practical implementation of heterogeneous workflows
6:55 Case study: Recursive language models and context management
9:05 Results on Ulong benchmarks (Cerebras/Sambanova performance)
10:20 Case study: Visual web navigation and Video Web Arena performance
12:02 Offloading subtasks to smaller models for speed and cost efficiency
12:38 The future of compute: Moving to a heterogeneous, multi-agent stack
13:10 Partnership with the UK's Arya institute
13:31 Closing summary and outlook on hardware/software co-evolution
14:01 Q&A: Automation layer for task routing

## Let's Talk About FOMAT: Fear of Missing Agent Time — Michael Richman, Cmd+Ctrl

- Upload date: 2026-05-24
- Video: https://www.youtube.com/watch?v=W-SX_srBa3Y
- Transcript: raw/20260524_W-SX_srBa3Y/W-SX_srBa3Y.en-orig.vtt
- Metadata: raw/20260524_W-SX_srBa3Y/W-SX_srBa3Y.info.json

You kicked off an agent 30 minutes ago. It stopped after two minutes, blocked on a question, and has been waiting ever since. Michael Richman calls this FOMAT: fear of missing agent time. His answer is Cmd+Ctrl, a system that sends you a push notification when the agent needs input, lets you respond from your phone or watch, and lets you start new sessions from wherever you are.

The demo shows Claude Code running in a terminal while the Cmd+Ctrl app on an iPhone mirrors the session in real time. Walk away, get notified when the agent completes or gets stuck, reply from the phone, pick up in the terminal. The same setup works across Claude Code, Cursor, Codex, Gemini CLI, and others through a daemon that runs alongside each agent and reports to a shared control plane. The daemon layer is open source. A standup dashboard summarizes all recent sessions so you can catch up without reading every thread.

Speaker info:
- https://x.com/mrwoofster
- https://www.linkedin.com/in/michael-richman-b7807b2/
- https://github.com/mrwoof

## How Google DeepMind Runs Agents at Scale — KP Sawhney & Ian Ballantyne, Google DeepMind

- Upload date: 2026-05-24
- Video: https://www.youtube.com/watch?v=7gujZrJ9L5I
- Transcript: raw/20260524_7gujZrJ9L5I/7gujZrJ9L5I.en-orig.vtt
- Metadata: raw/20260524_7gujZrJ9L5I/7gujZrJ9L5I.info.json

Google DeepMind employees have worse token quotas than paying customers. That is not a mistake. KP Sawhney explains: customers get priority, and if an internal team spikes usage on a cluster someone monitoring 24/7 will just call and ask them to stop.

This panel covers how DeepMind thinks about agents at scale from the inside: managing quota across thousands of power users, a Darwinian skills library where only the strongest skills survive as engineers contribute en masse, and where the Deep Research pipeline is going next. KP's current focus is replacing the pipeline's giant context blobs with a shared file system so each research component can collaborate the way human researchers would, and produce supporting artifacts that the current architecture cannot.

Speaker info:
- https://linkedin.com/in/ianballantyne
- https://github.com/irbg
- https://linkedin.com/in/kyle-sawhney
- https://github.com/KPSawhney

Timestamps:
0:00 Introduction of KP Sawhney and Ian Ballantyne
0:57 Demo of the anti-gravity agentic platform
4:32 Discussion on KP's work with the deep research agent
5:46 Using skills libraries and managing agent sprawl
7:52 Addressing scalability and token quotas at Google
9:44 Audience Q&A: Managing per-user agent behaviors
13:12 Audience Q&A: Observability and agent trajectory stores
14:46 Audience Q&A: Future of deep research pipelines
16:10 Audience Q&A: Handling multi-agent systems
17:45 Audience Q&A: Perspectives on skills vs. MCP
19:12 Audience Q&A: Evaluating agentic workflows
20:25 Audience Q&A: Handling model limits and quota management
22:48 Audience Q&A: Automated code review processes

## Prompt to Pipeline: Building with Google's Gen Media Stack — Paige & Guillaume, Google DeepMind

- Upload date: 2026-05-23
- Video: https://www.youtube.com/watch?v=ns9f1fjLD7Y
- Transcript: raw/20260523_ns9f1fjLD7Y/ns9f1fjLD7Y.en-orig.vtt
- Metadata: raw/20260523_ns9f1fjLD7Y/ns9f1fjLD7Y.info.json

A public domain book, a notebook, and three gen media models. Guom from Google DeepMind fed Wind in the Willows into Gemini, generated character portraits with Nano Banana, animated chapter scenes with VO, and scored each chapter with LIA, all live in the workshop.

The full three hour session covers more ground. Paige Bailey demos AI Studio's Build feature creating a bookshelf scanning app with Google login and Firestore from a single prompt, Gemini 3.1 Flash Light analyzing a dinosaur video frame by frame for under a dollar, and Genie 3 rendering a playable world with a pink sparkly squirrel on Regent's Canal. Ian Valentine closes with Gemma 4 running on device: 10 sub agents generating SVGs in parallel on a local 26B model, then open code building and debugging a game from a spec with no cloud API involved.

Speaker info:
- https://x.com/DynamicWebPaige
- https://linkedin.com/in/dynamicwebpaige
- https://github.com/dynamicwebpaige
- https://x.com/Giom_V
- https://www.linkedin.com/in/guillaumevernade
- https://github.com/Giom-V

## Introducing WebMCP: Agents in the Browser — RL Nabors

- Upload date: 2026-05-23
- Video: https://www.youtube.com/watch?v=LMbeDEQO6QM
- Transcript: raw/20260523_LMbeDEQO6QM/LMbeDEQO6QM.en-orig.vtt
- Metadata: raw/20260523_LMbeDEQO6QM/LMbeDEQO6QM.info.json

RL Nabors built a comic reader that renders inside Claude. Full panels, navigation, transcript mode, design matched to the original site. No browser tabs. She is reading her own web comic archive entirely through an agent, and it looks like the website.

The talk is a case against chat as the permanent UI of agentic software. Chat is to agents what the terminal was to desktop computing: developers love it, everyone else gets the iPhone eventually. MCP apps bundle HTML, CSS, and JavaScript into a single file that agent interfaces render in an iframe, turning any tool response into a real interactive surface. WebMCP goes the other direction: add tool name and description attributes to forms you already have, and browser agents can call your site's functions directly without screenshot parsing or DOM traversal. Both specs exist now. The web platform has been the infinite canvas all along.

Speaker info:
- https://x.com/nearestnabors
- https://www.linkedin.com/in/nearestnabors
- https://github.com/rachelnabors

Timestamps

0:07 Introduction and Speaker Background
3:28 Motivations for Future-Proofing the Web Comic Site
5:09 Roadmap: MCP, Apps, and WebMCP
6:05 Understanding Transports: STDIO vs. HTTP
8:57 Defining MCP Tools
10:52 The Role of MCP Resources
11:37 The Case Against 'Starfish' (Chat-Only) UI
13:36 MCP Apps: Building Interactive Agent Interfaces
16:34 Best Practices and Gotchas for MCP Apps
17:38 Introducing WebMCP: Agents in the Browser
19:07 Imperative vs. Declarative Models
20:13 WebMCP Demo with the Debugging Extension
21:47 Leveraging Native Browser APIs (Speech, Animation, etc.)

## The Missing Primitive for Agent Swarms — Lou Bichard, Ona

- Upload date: 2026-05-23
- Video: https://www.youtube.com/watch?v=5Sui_OnSRlY
- Transcript: raw/20260523_5Sui_OnSRlY/5Sui_OnSRlY.en-orig.vtt
- Metadata: raw/20260523_5Sui_OnSRlY/5Sui_OnSRlY.info.json

Stripe called theirs Minions. RAMP called theirs Inspect. Both are internal infrastructure for running fleets of background agents, and both teams built it from scratch. Lou Bichard's argument is that this shouldn't keep happening.

The talk breaks down what agent swarm infrastructure actually needs: a runtime (largely solved), orchestration and triggers (solved), and coordination, which is not. Coordination is the gap where agents pick up tasks from each other, pass messages, and verify they have cleared a stage of the development cycle before moving on. GitHub is a poor substitute: noisy, designed for humans, and not built for agents raising hundreds of parallel pull requests. Lou covers what a proper primitive looks like, shows how Owner ships VM level isolation for agent fleets today, and makes the case that the coordination layer probably needs to be a CLI gateway that any local coding agent can invoke to check its progress and proceed.

Speaker info:
- https://x.com/loujaybee
- https://www.linkedin.com/in/loujaybee

Timestamps:
0:00 Introduction and definition of a Software Factory
1:50 Agent swarm patterns: Swarms, Fleets, and Events
3:11 Real-world examples of internal agent infrastructure (Stripe, RAMP)
3:50 How Owner handles agent infrastructure and development environments
4:49 Understanding Harness Engineering
5:43 The three pillars of agent swarm infrastructure: Runtime, Orchestration, and Coordination
7:17 Demo: Running sub-agents and fleets in Owner
10:20 Challenges of building a software factory
11:44 The issue with Context Management and Context Rot
12:16 Why GitHub is a poor coordination layer for agents
12:59 Proposed solutions: State machines, Durable execution, and CLI gateways

## Gemini Nano on device — Florina Muntenescu & Oli Gaymond, Google DeepMind

- Upload date: 2026-05-22
- Video: https://www.youtube.com/watch?v=owH1f0N-keY
- Transcript: raw/20260522_owH1f0N-keY/owH1f0N-keY.en-orig.vtt
- Metadata: raw/20260522_owH1f0N-keY/owH1f0N-keY.info.json

Gemini Nano on device weighs three to four gigabytes. Shipping that per app is not realistic, which is why AI core puts it in the system once and every app shares it. Foreground apps get top priority. Background batch jobs queue and run overnight on charge. The developer never manages any of that.

The tradeoff is reach. The GenAI MLKit APIs require flagship devices from the last couple of years. Classic MLKit for vision and OCR runs on a billion plus devices without issue. Hybrid inference, launched a few weeks before this talk, falls back from Nano to Gemini Flash in the cloud when the on device model is not available. An embedding API is coming soon for RAG style solutions. For anything beyond that, LiteRT is the other path.

Speaker info:
- https://x.com/FMuntenescu
- https://www.linkedin.com/in/florina-muntenescu-314b8921
- https://github.com/florina-muntenescu
- https://linkedin.com/in/ogaymond

## Fast Models Need Slow Developers — Sarah Chieng, Cerebras

- Upload date: 2026-05-22
- Video: https://www.youtube.com/watch?v=TeGsFFNqRLA
- Transcript: raw/20260522_TeGsFFNqRLA/TeGsFFNqRLA.en-orig.vtt
- Metadata: raw/20260522_TeGsFFNqRLA/TeGsFFNqRLA.info.json

Codex Spark, a model Cerebras built with OpenAI, generates code at 1,200 tokens per second. The Sonnet and Opus families run at 40 to 60. At that 20x difference, a context window that used to take ten minutes to fill now takes 30 seconds, and every habit built around slow generation starts producing technical debt at a scale nobody has dealt with before.

Sarah Chieng from Cerebras covers what the playbook looks like in this regime. Validation and linting at every step is now instant, so there is no excuse not to run it continuously. Generating 75 component variations across five sub-agents and cherrypicking the best one becomes practical where it was not before. And when context burns in 30 seconds, a four file external memory system (agents, plan, progress, verify) is what keeps each new session from starting over instead of from scratch.

Speaker info:
- https://x.com/sarahchieng
- https://www.linkedin.com/in/sarah-chieng-888595139/

Timestamps:
0:00 - Introduction to the impact of fast AI code generation
2:29 - Historical context of model speeds
3:10 - Why AI inference speeds are increasing (Hardware/Stack optimization)
7:05 - The current developer landscape and risks of "slob"
8:27 - Playbook: Orchestrating models and sub-agents
9:56 - Playbook: Validation and automated testing
10:47 - Playbook: Cherrypicking and variety in output
12:07 - Playbook: Adopting a real-time collaborative mental model
12:53 - Playbook: Avoiding "slob" and active steering
13:54 - Playbook: Continuous refactoring
14:30 - Playbook: Context management and external memory systems

## Lobster Trap: OpenClaw in Containers from Local to K8s and Back — Sally Ann O'Malley, Red Hat

- Upload date: 2026-05-22
- Video: https://www.youtube.com/watch?v=F1DYkY1BlfM
- Transcript: raw/20260522_F1DYkY1BlfM/F1DYkY1BlfM.en-orig.vtt
- Metadata: raw/20260522_F1DYkY1BlfM/F1DYkY1BlfM.info.json

Sharing a good agent setup usually means handing someone a pile of markdown, config files, and YAML and hoping they reproduce what you have. The answer in this demo is a container image: spin up a sub agent in two seconds from a Podman command, flip a flag for Kubernetes, and your personal setup becomes the team baseline.

The stack is Podman locally, Kubernetes for distribution, same container image throughout. Secrets get two layers: Podman secrets for API keys on the host, OpenClaw secret refs inside the container. Volumes handle backup and recovery. An Nvidia team runs the same pattern in production with ten engineers each running their own OpenClaw in Kubernetes for model evals, doing work that used to take six people.

Speaker info:
- https://www.linkedin.com/in/sally-ann-omalley/

Timestamps:
0:00 Introduction and background on Sally Ann O'Malley
1:25 Discovering and experimenting with OpenClaw
2:35 Benefits of running AI agents in containers
3:05 Introducing Forever Claw and sub-agents
5:52 Using containers for agent configuration and tools
6:21 Managing secrets with Podman and Kubernetes
8:10 Scaling agent workloads with Kubernetes
9:15 Nvidia team case study: Model evaluations
11:09 Backup, recovery, and persistence with volumes
11:47 Vision for workplace agent standardization
14:14 Local demo: Running OpenClaw with Podman
16:45 Choosing providers and configuring settings
17:50 SSH sandbox features
18:22 Running the Podman command and checking agent status
20:52 Transitioning agent workloads to Kubernetes and OpenShift

## Cooking with Agents in VS Code — Liam Hampton, Microsoft

- Upload date: 2026-05-21
- Video: https://www.youtube.com/watch?v=dyHpnnlkTc8
- Transcript: raw/20260521_dyHpnnlkTc8/dyHpnnlkTc8.en-orig.vtt
- Metadata: raw/20260521_dyHpnnlkTc8/dyHpnnlkTc8.info.json

One codebase, three problems, three agents running at the same time. Liam Hampton from Microsoft demos the full loop in VS Code: a local agent with Claude Opus writing and fixing unit tests with him in the loop, a background agent using a git work tree to build a front end from a GitHub issue without him touching it, and a cloud agent running in GitHub Actions to make the repo open source friendly.

The talk is a framework for knowing which agent path to pick and why. Local when you want hands on iteration. Background when the task is big and you can tolerate being half in half out. Cloud when you genuinely do not care how it gets done. VS Code handles all three from one interface, with Copilot, Claude, and third party agents accessible from the same control plane.

Speaker info:
- https://x.com/liamchampton
- https://www.linkedin.com/in/liam-conroy-hampton/
- https://github.com/liamchampton

## Scaling Agents on Kubernetes with acpx and ACP — Onur Solmaz, OpenClaw

- Upload date: 2026-05-21
- Video: https://www.youtube.com/watch?v=VaS2h-dY1-4
- Transcript: raw/20260521_VaS2h-dY1-4/VaS2h-dY1-4.en-orig.vtt
- Metadata: raw/20260521_VaS2h-dY1-4/VaS2h-dY1-4.info.json

OpenClaw receives 300 to 500 pull requests per day. Most arrive AI generated, most are not mergeable, and every one of them is signal about something broken in the codebase. Onur Solmaz built acpx to process them without him in the loop.

acpx is a headless CLI for the Agent Client Protocol. It replaces PTY scraping with structured agent to client communication and drives sessions through a node based workflow graph: reproduce the bug, judge the implementation, check for conflicts, run a review loop, emit structured JSON. Onur runs parallel Codex sessions from Discord channels while traveling, one channel per task. The talk ends with disposable agent pods on Kubernetes, a Go operator that provisions a full compute environment per task, wires it into Slack, and tears it down when the work is done.

Speaker info:
- https://x.com/onusoz
- https://www.linkedin.com/in/osolmaz/
- https://github.com/osolmaz

## Your Coding Agent Should Do AI System Engineering — Ben Burtenshaw, Hugging Face

- Upload date: 2026-05-21
- Video: https://www.youtube.com/watch?v=JomVvNDjGb8
- Transcript: raw/20260521_JomVvNDjGb8/JomVvNDjGb8.en-orig.vtt
- Metadata: raw/20260521_JomVvNDjGb8/JomVvNDjGb8.info.json

An agent written RMSNorm kernel hit 1.88x speedups on H100s. A finetuned Qwen3 0.6B hit 35% on LiveCodeBench. Neither result required a systems engineer. Just coding agents with the right skills loaded.

Ben Burtenshaw from Hugging Face walks through three levels: using Claude Code interactively to write and benchmark CUDA kernels distributed as versioned repos on the Hub, a zero-shot task where an agent finetunes a model end to end from a single prompt, and a multi agent research lab running parallel experiments overnight on Hub compute while a reporter agent pushes results to a live Trackio dashboard. The through line is skills: file based context that turns a zero shot failure into a few shot workflow. CUDA programming and ML training pipelines were deep specializations that took years. Skills compress that timeline to hours.

Speaker info:
- https://x.com/ben_burtenshaw
- https://www.linkedin.com/in/ben-burtenshaw/
- https://github.com/burtenshaw

Timestamps:
0:00 Introduction to AI Systems Engineering
1:59 Boss 1: Writing and Distributing CUDA Kernels
3:48 Efficiency in Deep Learning
6:08 Using Skills for Agentic Workflows
8:37 Benchmarking and Evaluating Skills with Upskill
9:26 Boss 2: End-to-End Fine-tuning of LLMs
10:16 Boss 3: Multi-Agent Auto Research Labs
12:09 Architecture of the Multi-Agent Research System
13:40 Implementing the Research Agent in OpenCode
15:28 Monitoring Experiments with Trackio
16:45 Final Takeaways and Conclusion

## Skill issue: Lessons from skilling up coding agents to use Langfuse - Marc Klingen, Clickhouse

- Upload date: 2026-05-20
- Video: https://www.youtube.com/watch?v=vNCY9kXXyDQ
- Transcript: raw/20260520_vNCY9kXXyDQ/vNCY9kXXyDQ.en-orig.vtt
- Metadata: raw/20260520_vNCY9kXXyDQ/vNCY9kXXyDQ.info.json

Without a skill, Claude Code adds Langfuse using stale pre-training context, ships broken instrumentation, then catches the failure and fetches current docs to fix it. The resulting trace captures two LLM calls with no visibility into what the agent actually did.

Marc Klingen covers the six learnings from building a skill to close that gap: surfacing a natural language search endpoint so agents stop crawling 478 documentation pages, why pointing to references beats duplicating content, and what happened when they ran an auto-research loop on the skill itself. Three of six suggested improvements shipped, but their target function nearly backfired by optimizing out the documentation-fetching steps that make the skill reliable over time.

Speaker info:
- https://x.com/marcklingen
- https://www.linkedin.com/in/marcklingen/

Timestamps:
00:00 - Introduction to Marc Klingen and Langfuse
01:22 - Conceptual mental model for agent skills
04:04 - The problem: scaling documentation and onboarding for coding agents
09:03 - Six key learnings from building a Langfuse skill
09:12 - Learning 1: Looking at traces for debugging
10:47 - Learning 2: Helping agents navigate information (sitemaps/formats)
11:40 - Learning 3: Surfacing a search endpoint for docs
12:36 - Learning 4: Implementing basic evaluation (eval) setups
13:53 - Learning 5: Referencing rather than duplicating content
14:24 - Learning 6: Using auto-research loops with target functions
17:24 - Discussion on challenges: distribution, versioning, and target functions
19:21 - Roadmap and future outlook for agent automation
20:09 - Q&A session

## Any-to-Any: Building Native Multimodal Agents - Patrick Löber, Google DeepMind

- Upload date: 2026-05-20
- Video: https://www.youtube.com/watch?v=GIRpQEfYf3U
- Transcript: raw/20260520_GIRpQEfYf3U/GIRpQEfYf3U.en-orig.vtt
- Metadata: raw/20260520_GIRpQEfYf3U/GIRpQEfYf3U.info.json

Draw arrows on a map and ask Gemini to generate a picture of what you see. It produces the Golden Gate Bridge. Not because it matched pixels, but because the image generation model is built on top of Gemini's world understanding and knows what those arrows are pointing at.

Patrick Löber walks through the full any-to-any stack: multimodal understanding where Gemini ingests PDFs, video, and audio up to nine-plus hours at once, native image and speech generation called as tools from an agentic loop, and a live audio model where audio goes in and audio comes out through a single architecture with no cascaded pipeline. The session ends with the building blocks for a Notebook LM clone where a reasoning agent decides what to generate rather than a hardcoded workflow.

Speaker info:
- https://x.com/patloeber
- https://linkedin.com/in/patrick-l%C3%B6ber-403022137
- https://github.com/patrickloeber

Timestamps:
0:00 Introduction to the session
0:58 Defining "Any-to-Any" and the Gemini ecosystem
2:56 Building a NotebookLM clone using an agentic approach
3:51 The agentic architecture for multimodal applications
4:50 Implementation details for multimodal understanding
6:10 Tips for audio/video processing and context caching
7:56 Multimodal generation phase
8:37 Native image and infographic generation
9:04 Native speech generation and podcast style audio
9:57 Implementing function/tool calling
11:28 The power of native generation models
12:37 Multi-language and accent capabilities in audio models
13:46 Live API and real-time interaction
15:06 Final summary and additional model shout-outs

## From 46% to 90%: Fine-Tuning Tiny LLMs for On-Device Agents — Cormac Brick, Google

- Upload date: 2026-05-20
- Video: https://www.youtube.com/watch?v=-TiET_K-E_g
- Transcript: raw/20260520_-TiET_K-E_g/-TiET_K-E_g.en-orig.vtt
- Metadata: raw/20260520_-TiET_K-E_g/-TiET_K-E_g.info.json

Function Gemma ships at 270 million parameters and processes nearly 2,000 tokens per second prefill on a Pixel 7. Out of the box, on a fixed set of app intents, it hits 46% accuracy. Fine-tuned on a synthetically generated dataset, it clears 90% on eight of ten functions.

Cormac Brick covers the two options developers have for on-device AI: Gemini Nano via AI core for common tasks, and LiteRT-LM for custom models that ship inside your app. The session walks through a live skill harness built on Gemma 4 with a restaurant roulette demo running fully on-device, and Eloquent, a production transcription app built by chaining two models under a few hundred million parameters.

Speaker info:
- https://www.linkedin.com/in/cbrick/

Timestamps:
0:00 Introduction to on-device agents and tiny LLMs
0:48 Overview of AI Edge, SLMs, and TLMs
0:57 Taking a look at agent skills
1:06 Taking a look at tiny models
1:24 Motivations for on-device AI (latency, privacy, offline use)
3:01 System-level GenAI (Gemini Nano via AI Core)
4:03 App-level GenAI (LiteRT-LM for custom/boutique models)
5:06 Google AI Edge Gallery app demo
6:22 Deep dive into agent skills and the skill harness
7:41 How the skill harness works (system prompts, tool calls, and JavaScript UI)
9:00 Creating and publishing your own skills
10:28 Using LiteRT-LM runtime for model deployment
12:31 Export and inference workflow (from PyTorch to deployment)
13:19 Function Gemma: Robust, small-scale function calling
14:35 Fine-tuning workflow for tiny models using synthetic data
16:01 Eloquent: A production transcription app example using tiny models
17:28 Q&A: Agent skill robustness and multi-skill calling
19:26 Q&A: LiteRT-LM file format vs. Task files
20:00 Q&A: Performance on CPU/TPU and resources

## Don't Build Slop (4 Levels of AI Agent Maturity) - Ara Khan, Cline

- Upload date: 2026-05-19
- Video: https://www.youtube.com/watch?v=yUmS-F9IX90
- Transcript: raw/20260519_yUmS-F9IX90/yUmS-F9IX90.en-orig.vtt
- Metadata: raw/20260519_yUmS-F9IX90/yUmS-F9IX90.info.json

The prompt for GPT-5.3 is one-third the size of the one written for GPT-5. Frontier models are so capable that longer system prompts cause sensory overload and degrade performance. The rule Ara Khan keeps returning to: every single thing you add to an agent risks making it worse.

The talk breaks agent-building into four levels, from framework prototyping to cloud-native fleets, with five concrete rules for writing your own agent code in between. The form factor argument lands on Kanban boards as the right UX for managing parallel inference-bound agents. He made that prediction publicly on March 26. Claude Code shipped the same thing ten hours before this talk.

Speaker info:
- https://x.com/arafatkatze
- https://www.linkedin.com/in/arafatkatze/
- https://github.com/arafatkatze

Timestamps:
0:00 Introduction: Addressing the "mass psychosis" of agent-building
2:13 The Four Levels of Agent Maturity overview
3:00 Level 1: Using existing agent frameworks
4:13 Level 2: Building your own agents (with five rules)
4:36 Rule 1: View every agent as a state machine
5:55 Rule 2: Keep it simple (Avoid unnecessary system prompt bloat)
7:20 Rule 3: Integrate with a CLI for a pseudo-RL pipeline
8:43 Rule 4: Don't build "slop" (Focus on thoughtful architecture)
9:43 Rule 5: Master frontier model APIs (Reasoning traces)
11:03 The UX form factor: Why Kanban boards are best for agents
13:12 Shipping to the cloud for scalability
17:15 Q&A session: Planning and state transitions in Kanban

## What Breaks When You Build AI Under Sovereignty Constraints - Bilge Yücel, deepset GmbH

- Upload date: 2026-05-19
- Video: https://www.youtube.com/watch?v=x2bH0RKPgdc
- Transcript: raw/20260519_x2bH0RKPgdc/x2bH0RKPgdc.en-orig.vtt
- Metadata: raw/20260519_x2bH0RKPgdc/x2bH0RKPgdc.info.json

If you send EU citizen data to an embedding API hosted in Virginia, you have already violated GDPR. That is one hidden assumption. Most production AI systems have dozens more, baked into the architecture long before anyone asked whether the system was sovereign.

Bilge Yücel walks through the four sovereignty pillars (data, model, infrastructure, operations) and what actually breaks when you retrofit each one: re-evaluating performance from scratch after swapping a frontier API for a self-hosted model, managing multiple databases across jurisdictions after moving private data, and discovering how much vendor lock-in you had the moment you try to go on-prem. The closing checklist is three questions: can you swap models without changing application logic, do you have reproducible run logs stored in a compliant location, and can your team respond to an incident without calling a hyperscaler.

Speaker info:
- https://x.com/bilgeycl
- https://www.linkedin.com/in/bilge-yucel/

## Personalization in the Era of LLMs - Shivam Verma, Spotify

- Upload date: 2026-05-19
- Video: https://www.youtube.com/watch?v=5YSJEP0HWzM
- Transcript: raw/20260519_5YSJEP0HWzM/5YSJEP0HWzM.en-orig.vtt
- Metadata: raw/20260519_5YSJEP0HWzM/5YSJEP0HWzM.info.json

Spotify represents Ariana Grande and Bruno Mars as sequences of six tokens. The first two are shared because both are pop artists. The remaining tokens diverge to capture what makes each distinct. That is a Semantic ID, and it is how Spotify teaches open-weight LLMs to reason over a catalog of 100 million tracks the same way they reason over words.

Shivam Verma from Spotify's AI foundation team walks through the three components they assembled to personalize LLMs at scale without full fine-tuning. User embeddings trained on streaming history across 750 million users form the base. Semantic IDs compress catalog vectors into tokens the model can autoregressively generate, predicting the next song or episode as the next token in a sequence. A soft tokenization layer projects a user's embedding directly into the LLM's token space, giving the frozen model a user-specific token to attend over. Podcast next-episode recommendations are already running on this stack in production.

Speaker info:
- https://x.com/kaffeinated
- https://www.linkedin.com/in/shivam13verma

## Anthropic Workshop: Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson

- Upload date: 2026-05-18
- Video: https://www.youtube.com/watch?v=mR-WAvEPRwE
- Transcript: raw/20260518_mR-WAvEPRwE/mR-WAvEPRwE.en-orig.vtt
- Metadata: raw/20260518_mR-WAvEPRwE/mR-WAvEPRwE.info.json

Why self-evaluation is a trap and adversarial evaluator agents work better; why context compaction doesn't cure coherence drift but structured handoffs do; how to decompose work into testable sprint contracts; how to grade subjective output with rubrics an LLM can actually apply; and how to read traces as your primary debugging loop. Plus the question nobody asks: which parts of your harness should you delete when the next model drops?

Speaker info:
- Ash Prabaker  |  https://www.linkedin.com/in/ash-prabaker/
- Andrew Wilson  |  https://www.linkedin.com/in/anddwilson/

Timestamps:
0:00 Introduction and speakers
1:21 Overview of long-running agents
2:29 Challenges: Context, Planning, and Judgment
4:14 Two approaches: Model updates vs. Harness evolution
5:58 Prehistory: Sonnet 3.5, Computer Use, and MCP
6:34 The evolution of Claude Code
7:55 The Ralph loop technique
9:49 Sonnet 4.5, Agent SDK, and checkpoints
10:49 Opus 4.5 and the role of sub-agents
12:05 First long-running agent patterns
14:20 Opus 4.6, Agent Teams, and server-side compaction
17:28 State-of-the-art harness patterns
21:30 Evaluating subjective output with rubrics
23:44 Introducing the 'Planner' role
25:04 The generator-evaluator contract
31:28 Specificity in contracts and debugging traces
34:14 Adjusting harnesses as models evolve
37:56 How to build your own agent harness
39:01 Key takeaways for long-running agents
40:05 Q&A session

## Rewiring the State — Eoin Mulgrew, No. 10 (Downing Street)

- Upload date: 2026-05-18
- Video: https://www.youtube.com/watch?v=ObNKGf9YR0g
- Transcript: raw/20260518_ObNKGf9YR0g/ObNKGf9YR0g.en-orig.vtt
- Metadata: raw/20260518_ObNKGf9YR0g/ObNKGf9YR0g.info.json

The cabinet office was about to spend one and a half million pounds on an outside law firm to analyze the UK statute book. One engineer embedded with the in-house legal team for two weeks instead. The tool now lives with that team and can be run whenever they want. Eoin Mulgrew from the Number 10 data science team uses that as a typical example, not a headline one.

The talk covers what it actually takes to run a small insurgent technical unit at the center of government: market rate pay, a 0.7% acceptance rate, recruiting exclusively from outside the civil service, and an unusually direct mandate to go into departments and ship. The demos include a policy simulation tool, a delivery red-teaming PMO, two public dashboards that had never existed before, and a public service that went from idea to live in two months. The closing argument is a photo of a recent Harvard dropout and YC founder standing outside HMP Wormwood Scrubs holding the keys, two weeks into the job.

Speaker info:
- https://www.linkedin.com/in/eoinmulgrew/

## Let's go Bananas with GenMedia — Guillaume Vernade, Google DeepMind

- Upload date: 2026-05-18
- Video: https://www.youtube.com/watch?v=BcWFc3H7Khg
- Transcript: raw/20260518_BcWFc3H7Khg/BcWFc3H7Khg.en-orig.vtt
- Metadata: raw/20260518_BcWFc3H7Khg/BcWFc3H7Khg.info.json

Guillaume Vernade from Google DeepMind takes a public domain book and runs it through the full gen media stack live. Gemini reads the whole text and writes image prompts for each character and chapter. Imagen generates the portraits. Veo animates them into video clips using those images as first frames. Lyria composes a different piece of music per chapter, with or without lyrics. The TTS model reads dialogue from the book using a trick that makes two voices sound like four distinct characters.

The interesting layer underneath all of it is that Gemini acts as the prompt engineer for every other model, and it works well partly because the gen media models were trained on prompts written by Gemini. The workshop also covers the Lyria Realtime model, which generates music continuously and responds to new prompts mid-stream like a DJ, and a new interactions API that makes chained multi-turn calls cheaper by caching context server-side instead of resending the full book on every turn.

Speaker info:
- https://x.com/Giom_V
- https://www.linkedin.com/in/guillaumevernade
- https://github.com/Giom-V

## Why Your AI UX Is Broken (and It's Not the Model's Fault) — Mike Christensen, Ably

- Upload date: 2026-05-17
- Video: https://www.youtube.com/watch?v=YNJvm7t3yq8
- Transcript: raw/20260517_YNJvm7t3yq8/YNJvm7t3yq8.en-orig.vtt
- Metadata: raw/20260517_YNJvm7t3yq8/YNJvm7t3yq8.info.json

SSE ties a response stream to a single connection. The user refreshes the page, walks out of WiFi range, or opens a second tab and the in-progress response is gone. Abort and resume are mutually exclusive for the same reason: the only signal a client can send over a one-way pipe is closing it, so the agent cannot tell the difference between a cancel and a disconnect. Vercel's AI SDK documents this explicitly.

Mike Christensen from Ably makes the case for treating the session itself as a durable shared resource, decoupled from any individual connection, device, or agent instance. Clients subscribe to the session rather than to a request, so reconnects resume automatically, any tab or device has full visibility of live activity, and concurrent agents write independently without routing everything through an orchestrator. The demo shows all of this: multi-tab sync, a forced network disconnect that self-recovers, two agents running in parallel, and a handoff to a human support agent who joins the session mid-conversation with the full interaction history already visible.

Speaker info:
- https://x.com/christensencode
- https://www.linkedin.com/in/mikescottchristensen/

Timestamps:
0:00 Introduction to AI chat applications
0:51 Current implementation: Direct HTTP streaming and SSE
3:03 Three foundational capabilities for great AI products
4:34 Limitations of direct HTTP streaming
5:21 Introducing durable sessions
6:06 Resumability in streams
7:43 The conflict between SSE, resumability, and live control
9:13 Multi-device and multi-tab synchronization issues
11:12 Handling concurrent multi-agent architectures
12:54 Using Pub/Sub and Ably channels for durable sessions
14:12 Introducing Ably AI Transport SDK
15:34 Live demo of durable session capabilities
17:38 Handoff to human support agent

## Fighting AI with AI — Lawrence Jones, Incident

- Upload date: 2026-05-17
- Video: https://www.youtube.com/watch?v=L2r6vLlLgs8
- Transcript: raw/20260517_L2r6vLlLgs8/L2r6vLlLgs8.en-orig.vtt
- Metadata: raw/20260517_L2r6vLlLgs8/L2r6vLlLgs8.info.json

Incident's AI SRE runs hundreds of prompts per investigation across logs, metrics, traces, and code. When it produces a wrong root cause analysis, there is no tractable way for a human to read through the full trace and find where the reasoning went sideways. Lawrence Jones, founding engineer at Incident.io, describes the moment the team realized they needed AI to debug their AI.

The talk covers three patterns they built. A small CLI lets coding agents read and edit eval YAML files that had grown too large for agents to work with directly, enabling a red-green runbook where the agent writes a failing eval, fixes the prompt, and checks nothing else broke. Their bigger unlock was serializing every UI debugging view as a downloadable file system: drop it into a Claude Code session, describe the bad behavior, and the agent traces through the prompt hierarchy to tell you exactly which prompt to change. For fleet-scale analysis, 25 agents run in parallel each analyzing one investigation, then a second stage clusters the results to surface systemic failure patterns across customer accounts.

Speaker info:
- https://x.com/lawrjones
- https://www.linkedin.com/in/lawrence2jones/

## Harnesses in AI: A Deep Dive — Tejas Kumar, IBM

- Upload date: 2026-05-17
- Video: https://www.youtube.com/watch?v=C_GG5g38vLU
- Transcript: raw/20260517_C_GG5g38vLU/C_GG5g38vLU.en-orig.vtt
- Metadata: raw/20260517_C_GG5g38vLU/C_GG5g38vLU.info.json

Tejas will be back on stage at the World's Fair next week! see https://ai.engineer/wf and use YOUTUBEPROMO for new tickets only. Join 6000 AI engineers at the "Superbowl of AI"!

---

The agent hit a login page, panicked, reported success anyway, and the upvote never happened. Tejas Kumar's diagnosis: not a prompt problem. A harness problem.

The demo builds a browser agent on GPT-3.5 Turbo (consciously choosing a VERY old model to show how good harness eng can improve it a lot) against Hacker News and layers in a harness without touching the prompt once. Guardrails cap iterations and compact context. A verify step reads the tool call history to catch the agent lying about what it did. A login handler watches the browser URL each loop and injects credentials programmatically when it hits the login page. By the end the cheap old model reliably logs in and upvotes the post.

Speaker info:
- https://x.com/TejasKumar_
- https://www.linkedin.com/in/tejasq/
- https://github.com/TejasQ

Timestamps:
0:00 Introduction to Tejas Kumar and AI Harnesses
1:45 Why we use harnesses: Reliability and control
3:00 Defining an agent harness from first principles
4:32 Key components of an agent harness (Tooling, Context, Guardrails)
5:59 Starting the demo: Building a browser agent
7:00 Inspecting the initial agent loop
8:12 The problem: Agent failure and hallucination
10:20 Adding guardrails and context management
11:54 Refactoring into a formal harness
13:02 Implementing a verify step to catch lies
15:36 Implementing a login handler for programmatic access
17:42 Final demonstration: Successful autonomous upvoting
18:34 Summary and the future of dynamic harnesses

## How to Leverage Domain Expertise — Chris Lovejoy, Notius Labs

- Upload date: 2026-05-16
- Video: https://www.youtube.com/watch?v=kfSDc2eVLo4
- Transcript: raw/20260516_kfSDc2eVLo4/kfSDc2eVLo4.en-orig.vtt
- Metadata: raw/20260516_kfSDc2eVLo4/kfSDc2eVLo4.info.json

Granola's first employee was a writer who still reviews meeting note outputs and tweaks prompts directly. Chris Lovejoy says that is not a gap in the org chart. There is no objectively perfect meeting note, so you need someone with taste doing both the assessment and the improvement.

He frames this as one of three patterns: the Oracle owns the full loop, the Evaluator defines quality and measures it while engineers improve, the Architect builds systems that improve from usage automatically. Three case studies cover when each is appropriate, what skills to hire for, and what happens when you bring in a domain expert but give them no ownership.

Speaker info:
- https://x.com/ChrisLovejoy_
- https://www.linkedin.com/in/dr-christopher-lovejoy/
- https://github.com/chris-lovejoy

## Connecting the Dots with Context Graphs — Stephen Chin, Neo4j

- Upload date: 2026-05-16
- Video: https://www.youtube.com/watch?v=eW_vxrjvERk
- Transcript: raw/20260516_eW_vxrjvERk/eW_vxrjvERk.en-orig.vtt
- Metadata: raw/20260516_eW_vxrjvERk/eW_vxrjvERk.info.json

Ask a vector RAG system about a patient's emphysema care plan and it returns generic advice: respiratory therapy, deep breathing. Give it a graph grounded in that patient's actual history and it knows they smoke, knows they've had an operation, and gives recommendations that reflect it. The information existed in both cases. What changed was whether the system could traverse the relationships connecting it.

Stephen Chin from Neo4j makes the case that retrieval alone is not enough because agents also lose the reasoning behind past decisions. Context graphs capture not just what was retrieved but what decisions were made, why, which policies applied, and what the outcome was, so that precedent is queryable the next time a similar case comes up. The financial services demo shows this concretely: a loan decision that surfaces a prior rejection, related margin trades, and fraud risk patterns, with the graph traversal visible so the human making the final call can actually see what the system is drawing on.

Speaker info:
- https://x.com/steveonjava
- https://linkedin.com/in/steveonjava

## Beyond Code Coverage: Functionality Testing with Playwright MCP — Marlene Mhangami, Microsoft

- Upload date: 2026-05-16
- Video: https://www.youtube.com/watch?v=FWEInOtngmM
- Transcript: raw/20260516_FWEInOtngmM/FWEInOtngmM.en-orig.vtt
- Metadata: raw/20260516_FWEInOtngmM/FWEInOtngmM.info.json

When an LLM writes your tests, it tends to write tests that confirm what the code does rather than tests that verify what the user experiences. Your test suite goes green. The app still breaks in ways none of those tests would catch.

Marlene Mhangami from Microsoft makes the case for flipping the order: get the agent to write failing Playwright tests against the expected behavior first, then generate code to pass them. The demo runs this live with GitHub Copilot and the Playwright MCP server on a toy store search feature, with the browser open so you can watch the agent click through filters and validate results in real time.

Speaker info:
- https://x.com/marlene_zw
- https://www.linkedin.com/in/marlenemhangami/
- https://github.com/marlenemhangami

Timestamps:
0:00 Introduction to GitHub Octoverse stats and 2025/2026 growth
2:13 Does AI actually increase developer productivity?
3:52 Importance of maintaining a clean codebase
4:36 Test-Driven Development (TDD) and the Red-Green-Refactor cycle
6:07 Common criticisms of TDD and unit testing
7:43 The problem with AI-generated self-affirming tests
8:09 Introduction to Playwright for functional testing
9:18 Integrating AI agents with Playwright for faster TDD
10:54 Live Demo: Adding search and filter features to a toy store app
12:25 Using GitHub Copilot CLI and Work IQ for feature requests
13:50 Generating and running Playwright tests live
16:10 Best practices for using AI with Playwright
17:30 Q&A: Handling state management and testing across different screen sizes

## Agents Don't Do Standups: Building the Post-Engineer Engineering Org — Mike Spitz, PFF

- Upload date: 2026-05-15
- Video: https://www.youtube.com/watch?v=VMemhtlsoNk
- Transcript: raw/20260515_VMemhtlsoNk/VMemhtlsoNk.en-orig.vtt
- Metadata: raw/20260515_VMemhtlsoNk/VMemhtlsoNk.info.json

PFF ran a three-month case study: two engineers against a team of ten, same codebase, same customers. The two shipped five times a day. The ten shipped once every five days. Output measured by ticket complexity came out at 10x. Customer satisfaction went up, not down. Mike Spitz, their CTO, started with one reframe: stop asking how to help engineers go faster and ask how to make the agents faster instead.

The talk covers what that reframe actually dismantled. Standups went away because tickets auto-update from PR state. Sprint planning went away because estimates are irrelevant when the bottleneck is no longer human. Code review got split: agents handle style and naming, engineers handle system design. The spec to lightweight design doc to auto-generated ticket to PR flow replaced most of the coordination overhead entirely. What survived is a short huddle every other day, a strong opinion about which engineers thrive in this setup, and a QA agent that spins up on staging after every merge and checks acceptance criteria against the ticket.

Speaker info:
- https://x.com/mikespitz_uk
- https://www.linkedin.com/in/mike-spitz-89741243/

Timestamps:
0:00 Introduction to the case study at PFF
1:47 The shift: optimizing for agent speed rather than engineer speed
2:28 Results: 25x increase in deployment frequency
3:16 Measuring success through ticket complexity and customer satisfaction
4:53 Dismantling Scrum and traditional development processes
5:58 The new development workflow (Spec → LDD → Ticket → PR)
6:51 Eliminating coordination overhead (no sprint planning or standups)
8:28 Best practices for implementation and team selection
10:09 Utilizing agents for deterministic tasks and code reviews
12:00 Viewing the engineering lifecycle as a factory
13:06 Automated QA and the future of self-healing systems
14:10 Where human oversight remains essential
14:48 Strategic advice for scaling AI-driven engineering

## Combine Skills and MCP to Close the Context Gap — Pedro Rodrigues, Supabase

- Upload date: 2026-05-15
- Video: https://www.youtube.com/watch?v=JT3OzDKrucU
- Transcript: raw/20260515_JT3OzDKrucU/JT3OzDKrucU.en-orig.vtt
- Metadata: raw/20260515_JT3OzDKrucU/JT3OzDKrucU.info.json

Agents working with Postgres will confidently create a view over a table with row-level security enabled and silently bypass that security in the process. Not because they can't reason. Because they don't know about the security_invoker flag, and nobody told them. Pedro Rodrigues from Supabase ran this exact test: same agent, same task, MCP alone versus MCP plus a skill. The one without the skill shipped a query that exposed data it shouldn't have.

The talk covers what Supabase learned building their agent skill from scratch: critical security rules go directly in skill.md because agents will reliably skip reference files, skills should point to living documentation rather than duplicate it, and opinionated workflow guidance matters more than comprehensive coverage. Their evals ran across Claude and GPT models in three conditions and the result was unanimous. Skills without MCP underperform. MCP without skills misses environment-specific constraints. Together they close the gap that makes agents unreliable on real production systems.

Speaker info:
- https://x.com/rodriguespn23
- https://www.linkedin.com/in/pedro-neves-rodrigues/
- https://github.com/Rodriguespn

## How Building with AI Can Double the Throughput of Your Engineering Team — Brian Scanlan, Intercom

- Upload date: 2026-05-15
- Video: https://www.youtube.com/watch?v=4_VQBbs2iQA
- Transcript: raw/20260515_4_VQBbs2iQA/4_VQBbs2iQA.en-orig.vtt
- Metadata: raw/20260515_4_VQBbs2iQA/4_VQBbs2iQA.info.json

Intercom hit 2x engineering throughput in under a year. Not by prompting better. By treating Claude Code like a new hire: onboarding it to a Rails monolith built over 15 years, writing skills for every recurring task, connecting it to production systems and internal tooling, and going all in on one platform instead of letting everyone pick their favorite tool.

Brian Scanlan covers what the data looks like: PR throughput doubled, 17.6% of pull requests auto-approved with SOC 2 sign-off, and the CI infrastructure collapsed under the volume. The principle behind all of it comes down to framing. Give agents problems, not tasks. He was pulled into a security incident over accidentally published Snowflake metadata, described the situation to Claude, and watched it pull the files, run the analysis, and hand back next steps in two minutes using a skill he didn't know existed.

Speaker info:
- https://x.com/brian_scanlan
- https://www.linkedin.com/in/scanlanb/

## Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate

- Upload date: 2026-05-14
- Video: https://www.youtube.com/watch?v=vi-2nasppAg
- Transcript: raw/20260514_vi-2nasppAg/vi-2nasppAg.en-orig.vtt
- Metadata: raw/20260514_vi-2nasppAg/vi-2nasppAg.info.json

The abstraction is three things: state, a synchronous reducer that derives state from events, and an after-append hook for side effects. The split matters: when your program restarts after 100 events, you want to catch up state without replaying LLM requests. Everything that happens (streaming chunks, tool calls, errors, circuit breaker triggers) is an event in the log.

The interesting part is deployment. Jonas demos "dynamic worker configured," an event whose payload is a JavaScript string containing a processor. Append it to any stream and that stream becomes an AI agent without server or dependencies. The broader implication: processors from different authors on different servers can compose against the same stream, and a safety checker can inject context in a 200ms window before an LLM request without blocking the agent if it doesn't make it.

Speaker info:
- https://x.com/jonas
- https://www.linkedin.com/in/jonashuckestein
- https://github.com/jonastemplestein


0:14 Introduction and workshop overview
1:33 Concept of event-sourced agent harnesses
2:24 Desired characteristics: Extensibility and composability
3:14 Agents on the edge and public routability
4:20 The distributed nature of agents and potential pitfalls
5:40 Introduction to the event stream architecture
8:38 Working with the API via curl
10:48 Handling events and error states
11:57 Circuit breakers and stream management
13:49 Scheduling tasks and event subscriptions
15:17 Q&A: Architectural philosophy
19:17 Demonstrating the SDK and TypeScript integration
30:06 Defining stream processors and reducers
47:34 How stream processors function in production
50:35 Dynamic workers and deploying via event payloads
58:45 Discussion on before-hooks versus eventual consistency
1:02:16 Future outlook and wrapping up

## Mind the Gap (In your Agent Observability) — Amy Boyd & Nitya Narasimhan, Microsoft

- Upload date: 2026-05-14
- Video: https://www.youtube.com/watch?v=iOXM3zE-2dk
- Transcript: raw/20260514_iOXM3zE-2dk/iOXM3zE-2dk.en-orig.vtt
- Metadata: raw/20260514_iOXM3zE-2dk/iOXM3zE-2dk.info.json

Agents drift. Models change, prompts get tweaked, edge cases accumulate, and the gap between what your agent does and what you need it to do widens without you noticing. Amy and Nitya walk through Microsoft Foundry's observability stack: tracing built on OpenTelemetry, built-in evaluators for quality, safety, and agentic metrics like intent resolution and task adherence, and red teaming where a second AI attacks your agent with adversarial prompts to find vulnerabilities before your users do.

The piece worth watching for is the observe skill demo. You point it at an agent with no eval dataset, no baselines, nothing. It generates the dataset, runs batch evaluations, optimizes the prompt, compares versions, and rolls back to the best one... all from a single prompt to a coding agent. The skill shows its reasoning at each step, which is where the real value is: it surfaces the failures you didn't know to look for.

Speaker info:
- https://x.com/NityaNarasimhan
- https://www.linkedin.com/in/nityan/
- https://x.com/AmyKateNicho
- https://www.linkedin.com/in/amykatenicho/

## Ship Real Agents: Hands-On Evals for Agentic Applications — Laurie Voss, Arize

- Upload date: 2026-05-14
- Video: https://www.youtube.com/watch?v=Xfl50508LZM
- Transcript: raw/20260514_Xfl50508LZM/Xfl50508LZM.en-orig.vtt
- Metadata: raw/20260514_Xfl50508LZM/Xfl50508LZM.info.json

Most agents get tested by running a few queries and checking if it looks right. Laurie calls this the vibes problem: it doesn't catch regressions, doesn't run in CI, and doesn't tell you whether a prompt fix broke three other things. This workshop builds a complete eval pipeline from scratch on a financial analysis agent: tracing with Phoenix, reading traces before writing a single eval, categorizing failures by root cause, then building code evals, built-in LLM-as-a-judge evals, and a custom rubric with labeled examples.

The sharpest lesson: choosing the right eval matters more than tuning it. A correctness eval scored 0 out of 13 on the same agent that a faithfulness eval scored 13 out of 13, because the model doesn't know what year it is and can't verify forward-looking financial data. The workshop closes on the thing most eval content skips — experiments that let you prove a prompt change actually worked, rather than eyeballing it and calling it a win.

Speaker info:
- https://x.com/seldo
- https://www.linkedin.com/in/seldo/
- https://github.com/seldo

Timestamps:
0:00:00 Introduction
0:00:14 Workshop Overview
0:04:31 Troubleshooting Phoenix Setup
0:05:17 Fundamentals of Evals and Tracing
0:18:44 Anatomy of an Eval Result
0:21:19 The Iteration Loop
0:26:58 Building the Financial Analysis Agent
0:33:28 Using Phoenix for Observability
0:35:38 Running Multiple Test Queries
0:38:12 Reading and Categorizing Traces
0:49:52 Implementing Code Evals
0:57:51 Built-in LLM-as-a-Judge Evals
1:03:04 Faithfulness Evaluation
1:04:35 Designing a Custom Eval Rubric
1:11:47 Running the Actionability Judge
1:19:14 Using Data Sets and Experiments
1:50:19 Final Tips and Best Practices
1:51:48 Differences Between Phoenix and Arize AX

## CI/CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner

- Upload date: 2026-05-13
- Video: https://www.youtube.com/watch?v=VktrqzQgytY
- Transcript: raw/20260513_VktrqzQgytY/VktrqzQgytY.en-orig.vtt
- Metadata: raw/20260513_VktrqzQgytY/VktrqzQgytY.info.json

Traditional CI/CD was built for humans pushing one or two diffs a week. Scale to thousands of autonomous agents opening PRs continuously and you get runner saturation, cold Docker builds on every branch, cache thrash, and a merge queue that starts behaving like a serialized database lock where time-to-commit becomes the actual bottleneck.

Madison Faulkner and Hugo Santos (Namespace) lay out what replaces it: no PRs, just intent and plan fed into an agent loop with fast inline validation. Changes queue in a premerge layer where humans review intent-plus-outcome rather than diffs. The end state they're pointing toward is agents exploring multiple commits in parallel for the same plan, a multiverse where the tip of the repo is a moving target and the inner loop needs to be stateful and fast enough to keep up.

Speaker info:
- https://x.com/madsfaulkner
- https://www.linkedin.com/in/madisonhfaulkner/
- https://namespace.so/blog/introducing-namespace
- https://www.linkedin.com/in/hugomgsantos/

Timestamps
0:00 Introduction and speaker bios
1:28 Why agentic software is breaking traditional CI/CD
1:59 The fragmented lifecycle of modern software development
2:25 How traditional CI/CD pipelines work
2:55 The problems with CI/CD at agent scale
4:04 Replacing CI/CD with acceleration and orchestration
6:12 Real-world solutions and the future of agentic loops
7:23 The role of the human as the agent
8:43 Why Pull Requests (PRs) are becoming a bottleneck
10:00 A new architecture: Intent and plan-based development
11:58 Moving toward fully automated internal/external validation
13:46 The premerge queue and human-in-the-loop review
15:20 The future: Parallel development in the multiverse
16:51 Conclusion: The shifting role of CI and governance

## Self-Training Agents: Hermes Agent, HF Traces, Skills, MCP & Finetuning  — Merve Noyan, Hugging Face

- Upload date: 2026-05-13
- Video: https://www.youtube.com/watch?v=OV56RddyFuU
- Transcript: raw/20260513_OV56RddyFuU/OV56RddyFuU.en-orig.vtt
- Metadata: raw/20260513_OV56RddyFuU/OV56RddyFuU.info.json

Open-source models have caught up. GLM 5.1 is leading the Artificial Analysis intelligence index over closed models, and the gap is closing fast with each release cycle. The practical upside beyond benchmarks: full weight access means you can quantize, fine-tune, and deploy to edge devices or browsers without data leaving your infrastructure.

@MerveNoyan walks through the Hugging Face ecosystem built around this: inference providers that route to the fastest or cheapest option per model, benchmark datasets for filtering by SWE-bench or AIME scores directly on Hub, a traces repository type for storing and exploring agent sessions, and skills that plug into coding agents. The closer is a live demo where she asks Claude Code to fine-tune a vision-language model on a dataset by name. The agent calculates VRAM requirements, selects an instance, and kicks off the job. What used to be a day of napkin math is now a prompt.


Speaker info:
- https://x.com/mervenoyann
- https://www.linkedin.com/in/merve-noyan-28b1a113a/
- https://github.com/merveenoyan

Timestamps
0:00 Introduction to Open Agent Ecosystem
0:39 Importance of Open Source in Machine Learning
2:36 Hugging Face Hub overview
3:06 Agentic models and Vision-LMs
4:24 Benchmark datasets and model filtering
5:16 Inference providers and model routing
6:50 Local coding agents and tools
7:46 Hermes agents for memory management
9:20 Traces repository for agent sessions
10:22 Tips for finding and serving local models
12:07 Supercharging agents with Hugging Face skills
13:41 Live demonstration of agent-driven fine-tuning
14:41 Training vision models (object detection/segmentation)
15:00 Using Model Context Protocol (MCP) for agents
16:30 Case study: OCR processing for AI papers

## Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take

- Upload date: 2026-05-13
- Video: https://www.youtube.com/watch?v=FlzpEGHNVKQ
- Transcript: raw/20260513_FlzpEGHNVKQ/FlzpEGHNVKQ.en-orig.vtt
- Metadata: raw/20260513_FlzpEGHNVKQ/FlzpEGHNVKQ.info.json

LLMs can explain things clearly but can't play chess reliably. Take Take Take (Magnus Carlsen's app) solved this by separating concerns: Stockfish handles position evaluation, tactical and positional detectors extract concepts like forks, pins, and structural weaknesses, and the LLM's only job is translating those structured signals into English. Keeping the model as a translator rather than a reasoner is what makes it work at sub-3-second latency for a consumer app.

Anant Dole and Asbjørn Steinskog also walk through how they closed the feedback loop. When a user flags bad commentary, it posts to Slack and injects the event into a running Claude Code session via Channels, a new MCP feature in research preview. Claude investigates the position, modifies prompts or detectors, regenerates the commentary, and asks clarifying questions back through Slack. During the live demo, Anant was reviewing the PR from his phone.

Speaker info:
- https://www.linkedin.com/in/asbj%C3%B8rn-ottesen-steinskog-a8000241/
- https://www.linkedin.com/in/anantdole/

## Give Your Agent a Computer — Nico Albanese, Vercel

- Upload date: 2026-05-12
- Video: https://www.youtube.com/watch?v=wflNENRSUb4
- Transcript: raw/20260512_wflNENRSUb4/wflNENRSUb4.en-orig.vtt
- Metadata: raw/20260512_wflNENRSUb4/wflNENRSUb4.info.json

The key insight from Vercel's internal agent work: giving an agent a file system didn't just add storage, it changed how the agent behaved. It started following through on long tasks, staying on track, and building on its own prior work. That's what this workshop builds toward.

@nicoalbanese10  walks through AI SDK v6 from scratch: a tool loop agent, provider-executed web search, end-to-end type safety, and Vercel's new persistent named sandboxes. The agent gets a bash tool, a memories.md file it reads and writes, and instructions that make it generate Python scripts for repeatable tasks and store them for later. By the end, it's an agent that accumulates tools and context across sessions without any manual memory management.

Speaker info:
- https://x.com/nicoalbanese10
- https://www.linkedin.com/in/nicoalbanese/
- https://github.com/nicoalbanese

Timestamps:
0:00 Setup and project initialization
7:31 Installing dependencies
9:02 Introduction to AI SDK v6 and tool loop agents
11:05 Defining the agent in agent.ts
13:40 Building the route handler for the chat API
15:26 Creating the frontend UI with useChat
16:53 Modifying agent instructions
18:40 Adding web search tool (provider-executed tools)
23:55 Adding UI components for tool usage
27:43 The importance of persistent sandboxes (file systems for agents)
33:45 Managing context and message history across steps
45:11 Initializing persistent sandboxes
47:20 Defining custom call options and context
51:10 Creating the bash execution tool
55:05 Integrating the bash tool into the agent
57:15 Adding persistent memory (memories.md)
1:03:44 Making agents learn by generating Python scripts
1:05:58 Reviewing the full agent system and sub-agents

## Lessons from Trillion Token Deployments at Fortune 500s — Alessandro Cappelli, Adaptive ML

- Upload date: 2026-05-12
- Video: https://www.youtube.com/watch?v=X6NShR2ccOg
- Transcript: raw/20260512_X6NShR2ccOg/X6NShR2ccOg.en-orig.vtt
- Metadata: raw/20260512_X6NShR2ccOg/X6NShR2ccOg.info.json

95% of GenAI pilots fail to reach production. Alessandro Cappelli's argument is that this isn't a deployment problem or a prompt engineering problem — it's a feedback integration problem. Instruction fine-tuning and proprietary models give you a demo. Only reinforcement learning gives you a systematic way to incorporate defects, business metrics, and production signals and keep improving.

This talk covers what a production-grade RL pipeline looks like at Fortune 500 scale: synthetic data as a byproduct of environment training rather than a prerequisite, mock environments where agents can fail safely before touching real systems, and LLM judges that replace expensive annotation campaigns with a rubric-definition exercise that takes hours rather than weeks. The throughline is that agents raise the stakes on all of this — more tokens, less tolerance for errors, direct access to live databases — and RL was designed for exactly that problem.

Speaker info:
- https://www.linkedin.com/in/alessandro-cappelli-aa8060172

## Malleable Evals: Why Are We Evaluating Adaptive Systems with Static Tests? — Vincent Koc, OpenClaw

- Upload date: 2026-05-12
- Video: https://www.youtube.com/watch?v=4VhbYlfC7Gs
- Transcript: raw/20260512_4VhbYlfC7Gs/4VhbYlfC7Gs.en-orig.vtt
- Metadata: raw/20260512_4VhbYlfC7Gs/4VhbYlfC7Gs.info.json

Eighty percent of what your agent does is stable and well defined. The other twenty percent keeps changing as your users change, and that twenty percent is what breaks your business. Vincent Koc's argument is that we have been treating AI applications like static software and building evaluations like fixed datasets when the thing being measured keeps adapting underneath them.

The talk names this eval calcification and sketches what replaces it: agents that self curate test suites from their own traces, telemetry in the loop so the harness knows what is breaking and corrects itself, and evals that define an end state rather than a right answer. The benchmark is not a dataset. It is a self optimizing system that has to grow with the application it measures.

Speaker info:
- https://x.com/vincent_koc

## Why MLX — Prince Canuma, Neywa Labs

- Upload date: 2026-05-11
- Video: https://www.youtube.com/watch?v=zTLJNHj0DeQ
- Transcript: raw/20260511_zTLJNHj0DeQ/zTLJNHj0DeQ.en-orig.vtt
- Metadata: raw/20260511_zTLJNHj0DeQ/zTLJNHj0DeQ.info.json

MLX is an array framework for Apple Silicon, essentially PyTorch for your Mac, and this is a tour of what it can run: real-time vision models that describe the world around you, sub-100ms text-to-speech, speech-to-speech pipelines, omni models that take image and audio together, and video generation from a text prompt on 16GB of VRAM. A recent breakthrough called Turbo Quant cuts KV cache by 4x and gets 1M context running fully on device. The community projects include a native voice app, a robot speaking in real time with a cloned voice, and a system that chains video generations into a coherent story — all without a cloud call.

The underlying argument: the cloud assumption doesn't hold everywhere. Not for someone in Africa on an unreliable connection. Not for a local agent that needs to stay on. Not for a robot that has to hear, see, and respond without phoning home.

Speaker info:
- https://x.com/Prince_Canuma
- https://pl.linkedin.com/in/prince-canuma

Timestamp

0:00 Introduction and motivation for on-device AI
1:13 The origin story: Accessibility and Apple Silicon
2:27 Introduction to the MLX framework
3:30 Vision capabilities: Empowering accessibility
4:15 Omni models: Multimodal input support
5:25 Audio intelligence: Controlling computers via voice
6:33 Speech-to-speech and modular pipelines
7:59 Vision demo: Real-time image analysis
8:56 Background blur and object detection demo
9:31 Large language model demo: Running Gemma 4 locally
11:50 Community projects: Grounded visual reasoning
13:06 Video generation chains on-device
14:33 Native voice application showcase
15:39 Robotics: Real-time voice cloning and interaction
17:14 Q&A: Neural engine usage and CorML
18:18 Q&A: Monitoring performance with Mactop
19:34 Q&A: Available model recommendations
20:15 Q&A: Limitations and performance expectations
20:54 Q&A: Turbo Quant breakthrough and KV cache optimization

## A Piece of Pi: Embedding The OpenClaw Coding Agent In Your Product — Matthias Luebken, Tavon

- Upload date: 2026-05-11
- Video: https://www.youtube.com/watch?v=vAIDdLKB6-w
- Transcript: raw/20260511_vAIDdLKB6-w/vAIDdLKB6-w.en-orig.vtt
- Metadata: raw/20260511_vAIDdLKB6-w/vAIDdLKB6-w.info.json

OpenClaw feels like it's learning: it discovers capabilities, stitches tools together, builds solutions it wasn't explicitly taught. The reality is simpler — it's an LLM calling tools in a loop, powered by Pi, a minimal coding agent SDK. This talk is about what you can build once you understand that.

Matthias Luebken walks through embedding Pi in a real product: a B2B sales pipeline where incoming RFP emails route to customer-specific agent sessions, CLIs expose CRM and ERP data in a form the agent can use cleanly, and the only output a human sees is a draft in their inbox. The architectural principle running through it: don't fight the coding agent, make things easy for it. Design your data access and tool interfaces so the agent can work naturally rather than having to compensate for complexity.

Speaker info:
- https://x.com/luebken
-https://github.com/luebken

Timestamps

0:15 Introduction to Pi and OpenClaw
1:55 The philosophy of coding agents (doing one thing well)
3:34 Architectural pattern: Making systems easy for agents
5:13 Defining an agent: LLM with tools in a loop
6:37 Practical example: CRM lead qualifier
8:41 Coding agents vs. core agents
10:06 Extension API and UI interactions
12:53 Multi-channel environment: Pi and OpenClaw
14:46 Real-world B2B sales pipeline application
18:14 Demonstration: Dashboard and email drafting process
20:00 Final takeaways and encouragement to tinker

## Viktor: AI Coworker That Lives in Slack — Fryderyk Wiatrowski

- Upload date: 2026-05-11
- Video: https://www.youtube.com/watch?v=ohKt066uFhg
- Transcript: raw/20260511_ohKt066uFhg/ohKt066uFhg.en-orig.vtt
- Metadata: raw/20260511_ohKt066uFhg/ohKt066uFhg.info.json

Viktor is an AI employee that lives in Slack. No web UI. It participates in channels and threads the way a teammate does, inherits integrations from whoever connected them first, and handles tasks that take ten minutes while you move on to something else.

This talk covers what breaks when you scale a personal agent to a whole company. Slack is a more complex input surface than it looks: threads, DMs, edits, deletions, emoji reactions, and conversations that drift between channels. Memory isolation gets harder when the same agent needs context for a hundred users without leaking the growth channel into the engineering queue or one person's DMs into the team feed. And when you try to swap the underlying model for something cheaper, users notice in ways that have nothing to do with task performance.

Speaker info:
- https://x.com/fawiatrowski
- http://getviktor.com/

## Two Roads to Durable Agents: Replay vs. Snapshot — Eric Allam, CEO, Trigger.dev

- Upload date: 2026-05-10
- Video: https://www.youtube.com/watch?v=svCnShDvgQg
- Transcript: raw/20260510_svCnShDvgQg/svCnShDvgQg.en-orig.vtt
- Metadata: raw/20260510_svCnShDvgQg/svCnShDvgQg.info.json

Replay-based durability — wrapping every step in a journal, replaying on recovery, requiring deterministic code — is how everyone makes agents durable today. It works until it doesn't: the journal grows with every turn, the structure starts constraining how you write code, and an agent that needs to run for hours starts looking less like a transaction and more like a session.

This talk separates the problem in two: context durability (the append-only log of everything the LLM saw, which already fits in a database) and execution durability (the files, memory, and subprocesses that live in the compute layer, which don't). The answer to the second half isn't a smarter log — it's OS-level snapshot and restore. Eric Allam walks through how Trigger.dev built this on Firecracker microVMs, getting snapshots down to 14 megabytes compressed with sub-second save and hundred-millisecond restore times, and why IBM mainframes in 1966 got there first.

Speaker info:
- https://x.com/maverickdotdev
- https://www.linkedin.com/in/eric-allam/
- https://github.com/ericallam

## How we solved Context Management in Agents — Sally-Ann Delucia

- Upload date: 2026-05-10
- Video: https://www.youtube.com/watch?v=esY99nYXxR4
- Transcript: raw/20260510_esY99nYXxR4/esY99nYXxR4.en-orig.vtt
- Metadata: raw/20260510_esY99nYXxR4/esY99nYXxR4.info.json

The naive solution is truncation. The obvious solution is summarization. Neither worked — and the Arize team found out the hard way while building an AI agent that had to analyze the very trace data it was generating.

A year of lessons from building Alyx, starting with the vicious loop that defined the problem: Alex runs on trace data, the spans grow, the context limit hits, it fails and tries again. The talk covers why truncation breaks reasoning, why summarization gives the LLM too much control, and how head/tail preservation with a retrievable memory store is what actually held. Then: long session evals, sub-agents as the answer when one context accumulates too much, and what they found when they went looking for secrets in the Claude Code source release.

Speaker info:
- https://www.linkedin.com/in/sallyann-delucia-59a381172/

Timestamps:
0:00 Introduction and speaker background
1:02 Overview of the AI agent, Alyx
1:29 The problem: Context engineering vs. prompt engineering
4:06 The vicious loop of data growth in AI agents
5:16 Why naive truncation failed
6:14 Why summarization proved unreliable
6:46 The solution: Smart truncation and memory stores
8:02 Handling long session challenges
9:23 Offloading tasks to sub-agents
11:19 Ongoing challenges and future work
12:57 Findings from the Claude Code source release
13:44 Final key takeaways on context management
14:58 Q&A session

## Feedback Loops are All You Need — Mehedi Hassan, Granola

- Upload date: 2026-05-10
- Video: https://www.youtube.com/watch?v=ON5LIT0M4do
- Transcript: raw/20260510_ON5LIT0M4do/ON5LIT0M4do.en-orig.vtt
- Metadata: raw/20260510_ON5LIT0M4do/ON5LIT0M4do.info.json

One-shotting is seductive. One line of code for web search. One prompt to serve every user. One deploy and you're done. Granola shipped a chat feature into their meeting notes app and found out what comes after that.

This talk is a product engineer's honest account of why the gap between "it works in the playground" and "it works in production" is so hard to close. Web search looks like a single tool call — until it blows up your context, bills you 10p per chat, and your provider ships an overnight update that silently degrades your results. Prompt personalization looks straightforward — until you realize that one prompt genuinely cannot serve the salesperson expecting a deal summary, the engineer expecting blockers and linear tickets, and the HR manager expecting something else entirely.

The response at Granola wasn't to prompt better. It was to build the machinery for iteration: custom internal tracing that exposes tool calls, search trails, reasoning traces, and cost in a UI built for everyone — not just engineers with CloudWatch access. And a move to run their Electron frontend as a web app, so every PR gets a preview link and Cursor can go test changes automatically. The point isn't any single technique. It's the feedback loop — and what happens to an AI feature when it actually has one.

Speaker info:
- https://x.com/mehedih_
- https://github.com/MehediH

timestamps:
0:15 Introduction to Granola and product engineering
1:08 Demonstration of meeting transcription and note-taking features
1:52 The challenges of shipping generic AI features
2:48 The difficulties of integrating web search tools
4:02 Why a single prompt cannot serve diverse user roles
4:40 Building custom internal tracing and observability tools
6:22 Enhancing developer experience for desktop applications
7:16 Refactoring Electron for web-based testing and CI/CD preview links
8:33 Automating feature verification with Cursor
8:46 Concluding thoughts on building iterative feedback loops for AI products

## Voice AI: when is the "Her" moment? — Neil Zeghidour, CEO, Gradium AI

- Upload date: 2026-05-09
- Video: https://www.youtube.com/watch?v=P_RI1kCkRbo
- Transcript: raw/20260509_P_RI1kCkRbo/P_RI1kCkRbo.en-orig.vtt
- Metadata: raw/20260509_P_RI1kCkRbo/P_RI1kCkRbo.info.json

The "Her" moment has been promised so many times it's become a joke. Every new demo, every smooth-sounding voice agent gets called it. Neil Zeghidour, CEO of Gradium AI and one of the researchers behind Moshi — the first full-duplex voice model — uses this talk to be honest about where the gap actually is and why it keeps not closing.

The core tension: cascaded systems (speech-to-text, LLM, text-to-speech) are practical and getting smarter, but they're architecturally incapable of feeling like a real conversation. Latency from tool calls alone can be 500ms to 4 seconds — while humans process and respond in around 200ms total. Speech-to-speech models solve some of that but trade it for a different problem: they're still half-duplex, meaning they're either listening or talking but never both, which makes backchanneling impossible and the interaction feel robotic in a different way. Moshi showed that full-duplex is solvable. What it didn't solve was making the model useful. And cost is a wall hiding behind the latency problem — TTS at scale is expensive enough that some teams burn through their fundraising before they can grow a user base.

The most underrated thread in the talk is paralinguistic understanding: voice carries tone, hesitation, discomfort, and cultural signals that get entirely stripped out the moment you transcribe to text. Getting to Her means building models that don't just produce natural-sounding speech but actually understand what the voice is carrying — and that's a science problem, not a prompt engineering one.

Speaker info:
- https://x.com/neilzegh
- https://www.linkedin.com/in/neil-zeghidour-a838aaa7/

Timestamps:

0:14 Introduction and mission of Gradium AI
1:16 Demonstration of voice cloning technology
2:42 The "Her" movie analogy and current limitations of Voice AI
5:42 Challenges of cascaded systems (Speech-to-Text, LLM, Text-to-Speech)
6:37 The difficulty of latency in tool calling
9:08 Explanation of Speech-to-Speech vs. cascaded architectures
9:34 The necessity of full-duplex systems and backchanneling
11:53 Demonstration of the full-duplex Moshi model
12:59 The importance of paralinguistic understanding
14:29 Scalability and the high cost of current Voice AI
16:38 Introducing Phoneon: on-device, local TTS for privacy and cost efficiency
18:29 Conclusion and path forward for Voice AI

## Give Your Chat Agent a Voice — Luke Harries, Head of Growth, ElevenLabs

- Upload date: 2026-05-09
- Video: https://www.youtube.com/watch?v=DCZZ3AJKzuc
- Transcript: raw/20260509_DCZZ3AJKzuc/DCZZ3AJKzuc.en-orig.vtt
- Metadata: raw/20260509_DCZZ3AJKzuc/DCZZ3AJKzuc.info.json

Chat agents dominated 2025. Every product either went AI-first or got left behind. But text-in, text-out is already starting to feel dated. Voice is faster, more accessible, and opens up interaction paradigms that chat just can't touch — phone lines, Zoom calls, screen readers, ambient interfaces. In this talk, Luke Harries from ElevenLabs argues that the next upgrade for every chat agent isn't better prompts or smarter RAG. It's a voice layer.

The problem is most teams have already built and tuned their chat agents. They don't want to throw that out. This session shows how ElevenLabs' Voice Engine wraps any existing agent in a few lines — handling turn-taking, speech-to-text, text-to-speech, and emotion-aware interruption detection — without touching the underlying logic. There's a live demo of converting a working chat support agent to voice in a single prompt, plus a look at the client and server SDKs, Shadcn-based UI components, and how tool calling still works through the wrapper.

Speaker info:
- https://www.linkedin.com/in/luke-harries
- https://harries.co/

Timestamps
0:00 Introduction to voice-first chat agents
0:20 The shift from text-based to voice-based interactions
1:43 Evolution of agent architecture and challenges of rebuilding
2:47 Introducing the ElevenLabs Voice Engine
3:32 Overview of the server and client SDKs
4:36 UI components and deployment demo
5:56 Summary of voice engine integration paradigms
6:37 Predictions for the future of AI agents
7:00 Q&A: Handling tool calling and integrations

## Why TTS Models Now Look Like LLMs — Samuel Humeau, Mistral

- Upload date: 2026-05-09
- Video: https://www.youtube.com/watch?v=3jGAU2sbAyY
- Transcript: raw/20260509_3jGAU2sbAyY/3jGAU2sbAyY.en-orig.vtt
- Metadata: raw/20260509_3jGAU2sbAyY/3jGAU2sbAyY.info.json

The dominant architecture pattern for text-to-speech in 2026 looks a lot like an LLM — an autoregressive transformer generating sequences of tokens, one frame of audio at a time. Samuel Humeau from Mistral walks through why the field converged there, how neural audio codecs solve the information-density problem (audio carries ~200kbps of signal; you can't feed that raw to a transformer), and what the streaming trick actually is that makes voice agents feel responsive before the full audio has even finished generating.

The talk uses Mistral's just-released open-weight TTS model as a running example — live demos of voice cloning from a few seconds of reference audio, a voice agent answering real conference schedule questions, and a breakdown of the codec-to-backbone-to-decoder pipeline that produces it all. There's also a frank section on what's still unsettled: how to handle streaming text input (tokens arriving from an LLM in real time rather than a fixed block of text) and why getting that right is the next meaningful latency win in agent pipelines.

It's the kind of talk that makes the system feel less like a black box — not by oversimplifying, but by showing exactly which engineering choices are load-bearing and which are still open problems.

Speaker info:
- https://x.com/DrSamuelBHume
- https://www.linkedin.com/in/samuelhumeau/

Timestamps:
0:00 Introduction and Mistral's new open-source TTS model
2:06 Text-to-speech in AI agents and latency
3:33 Live demo: Voice cloning with 'Paul'
6:00 Voice cloning capabilities and multilingual examples
8:01 Historical context of audio generation
8:55 Transformer-based architecture for TTS
10:00 Challenges of information density in audio
10:55 Comparison of bit rates: text vs. audio
11:39 Using neural audio codecs
13:10 Backbone transformer and frame-based generation
14:56 Text conditioning and model architecture
16:08 Latency performance metrics
16:22 Future outlook: Streaming text input
17:35 Q&A: Generating text and audio simultaneously
18:24 Q&A: Availability of voice cloning features
19:35 Q&A: Philosophical take on speech interfaces
20:44 Q&A: Next steps for streaming audio and text input

## Agentic Search for Context Engineering — Leonie Monigatti, Elastic

- Upload date: 2026-05-08
- Video: https://www.youtube.com/watch?v=ynJyIKwjonM
- Transcript: raw/20260508_ynJyIKwjonM/ynJyIKwjonM.en-orig.vtt
- Metadata: raw/20260508_ynJyIKwjonM/ynJyIKwjonM.info.json

Getting context into an LLM is not just a retrieval problem. It is a search problem. This workshop digs into the part of context engineering that usually gets waved away: how agents actually decide what to pull from files, databases, memory, and the web, and why that choice often matters more than the model itself.

Across semantic search, general-purpose database tools, shell-based retrieval, and agent skills, Leonie Monigatti shows where each search interface works, where it breaks, and how to combine them into a more effective retrieval stack. If you're building agents and trying to make retrieval less brittle, this is a practical guide to the real mechanics behind agentic search.

Workshop repo: https://github.com/iamleonie/workshop-agentic-search

Speaker info:
- https://x.com/helloiamleonie
- https://www.linkedin.com/in/804250ab/

Timestamps:
0:00:00 - Introduction and Welcome
0:00:51 - Defining Context Engineering and the role of Search
0:02:21 - Historical context: From RAG to Agentic RAG
0:04:30 - Context sources (local files, memory, databases, web)
0:06:30 - Introduction to the Shell tool and its versatility
0:08:50 - Failure modes in agentic search
0:10:41 - The importance of tool descriptions and parameter design
0:13:53 - Code Demo: Simple semantic search and its limitations
0:23:26 - Code Demo: General purpose database query (ESQL)
0:28:36 - Code Demo: Adding Agent Skills for better interaction
0:34:42 - Code Demo: Using the Shell tool for file system retrieval
0:41:26 - Code Demo: Integrating custom CLIs (Gina Grap)
0:44:42 - Practical recommendations for building a search tool stack
0:49:16 - Q&A Session begins

## FLUX, Open Research, and the Future of Visual AI — Stephen Batifol, Black Forest Labs

- Upload date: 2026-05-08
- Video: https://www.youtube.com/watch?v=x8Yb4RidLgM
- Transcript: raw/20260508_x8Yb4RidLgM/x8Yb4RidLgM.en-orig.vtt
- Metadata: raw/20260508_x8Yb4RidLgM/x8Yb4RidLgM.info.json

FLUX started as an image model story, but this talk makes the larger ambition clear: visual intelligence, not just image generation. From FLUX.1 through Kontext, FLUX.2, and FLUX.2 Klein, Black Forest Labs has been pushing fast, open releases while building toward models that understand images, video, audio, actions, and eventually the physical world itself.

Along the way, Stephen Batifol walks through the research behind that direction, including BFL's work on self-supervised multimodal training, real-time generation and editing, and the path from generative media toward world models and robotics.

Speaker info:
- https://x.com/stephenbtl
- https://www.linkedin.com/in/stephen-batifol/

## How Transformers Finally Ate Vision – Isaac Robinson, Roboflow

- Upload date: 2026-05-08
- Video: https://www.youtube.com/watch?v=VhfAVA3BG2I
- Transcript: raw/20260508_VhfAVA3BG2I/VhfAVA3BG2I.en-orig.vtt
- Metadata: raw/20260508_VhfAVA3BG2I/VhfAVA3BG2I.info.json

Vision used to belong to CNNs. This talk explains why that changed, and why transformers only recently started winning for vision despite looking like the less natural fit for images. The answer runs through pretraining, scaling, borrowed infrastructure from the LLM world, and the long arc back to the simple architecture that scales best.

Using the evolution from ViT and Swin through ConvNeXt, Hiera, SAM, and RF-DETR, Isaac Robinson walks through what actually made transformer vision systems practical, where the tradeoffs still are, and why deployment flexibility now matters as much as raw benchmark wins. What comes next for VLMs, world models, and physical AI?

Speaker info:
- https://www.linkedin.com/in/robinsonish/

## Vibe Engineering Effect Apps — Michael Arnaldi, Effectful

- Upload date: 2026-05-07
- Video: https://www.youtube.com/watch?v=Wmp2Tku2PrI
- Transcript: raw/20260507_Wmp2Tku2PrI/Wmp2Tku2PrI.en-orig.vtt
- Metadata: raw/20260507_Wmp2Tku2PrI/Wmp2Tku2PrI.info.json

What if the best way to get coding agents to use a library well is not better prompts, but giving them the library's actual code? In this workshop, Michael Arnaldi walks through a practical approach to building with Effect and LLMs by cloning the Effect repo into the project, extracting patterns directly from the source, and using those patterns to guide agent behavior.

Starting from an empty repository, the session shows how to set up an Effect-based app with tests, strict TypeScript diagnostics, agent instructions, and a simple HTTP API, while also exploring the broader problem of how to make agents effective in unfamiliar codebases. If you're building with coding agents and care about reliability, structure, and real-world Effect workflows, this is a useful hands-on framing.

Speaker info:
- https://x.com/MichaelArnaldi
- https://www.linkedin.com/in/michael-arnaldi-52858114a/

Timestamps

0:15 – Introduction and context setting for the workshop
0:47 – Interactive audience poll on experience with Effect and AI tooling
3:16 – Discussing the core philosophy: "Just clone the repo" for AI context
5:59 – Understanding LLMs vs. the human brain and context window limitations
13:13 – Project setup: Starting from an empty repository
14:20 – Initializing the project with Bun, Vitest, and TypeScript
19:18 – Adding Effect beta and configuring TSGo for the compiler
30:30 – Configuring strict diagnostics for AI-assisted development
35:20 – Adding the Effect repository as a git subtree for better agent access
37:07 – Creating agents.md to establish rules and available commands
41:40 – Researching Effect patterns for building an HTTP API
43:08 – Discussing "Spec-Driven Development" and avoiding plan-mode limitations
54:02 – Drafting the plan for the Todo HTTP API
1:05:07 – Implementing the SQL client and migration patterns
1:13:42 – Reviewing API schemas and handling identified code duplication
1:18:14 – Starting the API server and verifying OpenAPI documentation
1:20:56 – Cleaning up test suites and enforcing best practices for layers
1:38:08 – Concluding remarks on workflows, clustering, and future stability in Effect

## Agent Optimization with Pydantic AI: GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic

- Upload date: 2026-05-07
- Video: https://www.youtube.com/watch?v=A48uhxfxbsM
- Transcript: raw/20260507_A48uhxfxbsM/A48uhxfxbsM.en-orig.vtt
- Metadata: raw/20260507_A48uhxfxbsM/A48uhxfxbsM.info.json

Deploying an agent is only the start. In this workshop, Samuel Colvin shows how to improve agents after they are already live, using Pydantic AI and Logfire to change prompts, models, and other parameters in production without redeploying or restarting services.

The session covers managed variables for live prompt and model updates, how to run evals and compare prompt variants against real datasets, and how GEPA can be used to evolve better prompts from production traces and feedback signals. If you're building agents in production and want a practical path from manual tuning to continuous optimization, this is a strong hands-on walkthrough.

Speaker info:
- https://x.com/samuelcolvin
- https://www.linkedin.com/in/samuel-colvin/
- https://github.com/samuelcolvin

Timestamps:
0:00 Introduction to Samuel Colvin and the Pydantic ecosystem
1:29 Overview of GEPA for prompt optimization
3:02 Introduction to Logfire managed variables
3:55 Case study: Analyzing political dynasties using Wikipedia data
10:04 Getting started: Setting up the environment and API keys
16:55 Running the initial evaluation (evals) against a golden dataset
25:16 Comparing different prompt performance
34:00 Running the full GEPA optimization process
43:43 Q&A: Handling prompt size and systemic errors
57:01 Demonstrating managed variables in a FastAPI web server
1:11:06 Discussing implicit user feedback collection
1:15:42 Q&A: Real-world internal use cases and context engineering

## Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop

- Upload date: 2026-05-07
- Video: https://www.youtube.com/watch?v=-aM2EDTiaMs
- Transcript: raw/20260507_-aM2EDTiaMs/-aM2EDTiaMs.en-orig.vtt
- Metadata: raw/20260507_-aM2EDTiaMs/-aM2EDTiaMs.info.json

Agent failures do not look like normal software failures. In this workshop, the Raindrop team breaks down what it actually takes to monitor production agents, from explicit signals like tool errors, latency, and cost to fuzzier signals like user frustration, refusals, task failure, and capability gaps.

The session covers how to move beyond evals toward real production observability, how to use classifiers, regex, and experiments to catch regressions, and how to instrument self-diagnostics so agents can report their own failures and strange behavior. If you're running agents in production, this is a practical framework for understanding what is going wrong and how to catch it early.

Speaker info:
- https://x.com/benhylak
- https://www.linkedin.com/in/zkoticha
- https://www.linkedin.com/in/joseph-daniel-gollapalli-a371a4138/

Timestamps

0:14 Introduction and the problem of agent failures
1:48 Moving from evals to production monitoring
3:33 The two types of signals: explicit and implicit
4:47 Using classifier signals for observability
6:38 Leveraging regex for signal detection
7:30 Using experiments to validate improvements
9:42 Q&A session: Statistical relevance and experimental design
16:07 Introduction to self-diagnostics
20:15 Workshop: Coding agent demonstration
24:01 Live demo: Triggering and handling tool failure
30:26 Best practices for self-diagnostic implementation
32:20 Q&A: Real-world use cases and triage
40:02 Q&A: Managing fast-paced experimentation
44:21 Q&A: Trace visualization and data export

## Full Walkthrough: Writing & Using Skills — Nick Nisi and Zack Proser

- Upload date: 2026-05-06
- Video: https://www.youtube.com/watch?v=pFsfax19yOM
- Transcript: raw/20260506_pFsfax19yOM/pFsfax19yOM.en-orig.vtt
- Metadata: raw/20260506_pFsfax19yOM/pFsfax19yOM.info.json

Write once, run in Claude, Codex, Cursor, and your own agents

Every developer using AI tools has the same problem: they prompt the same way, for the same tasks, over and over. Skills fix this. A skill is a portable unit of agent behavior that teaches any AI tool how to do a specific job. Write one, drop it into your editor, and it just works. Across tools. Across teams.

Most people don't know this primitive exists. In this hands-on workshop, you'll write real skills, test them live, and see how one file can power Claude.ai, Claude Code, Cursor, and Codex without changing a line.

Then we'll go deeper. You'll see how one CLI uses this same pattern to power 15 framework integrations — each one a skill composed with others, wired into an agent that installs and configures auth!


What you'll do:

Write 2+ skills for tasks you actually do at work

Install and test them across AI tools in real time

Learn the craft of good skill writing — specificity, constraints, composability

See how skills compose and scale inside a real CLI powered by the Claude Agent SDK

Speaker info:
- Nick Nisi  |  https://nicknisi.com/about/
- Zach Proser  |  https://zackproser.com/

## The Multi-Agent Architecture That Actually Ships — Luke Alvoeiro, Factory

- Upload date: 2026-05-06
- Video: https://www.youtube.com/watch?v=ow1we5PzK-o
- Transcript: raw/20260506_ow1we5PzK-o/ow1we5PzK-o.en-orig.vtt
- Metadata: raw/20260506_ow1we5PzK-o/ow1we5PzK-o.info.json

Everyone's building multi-agent systems, but nobody agrees on how. This talk proposes a taxonomy of five frontier multi-agent strategies and shows what happens when you compose them into a single architecture. Drawing from production data at Factory, we walk through a three-role system (orchestrator, workers, validators) that uses validation contracts, structured agent handoffs, and adversarial verification. We cover the case for serial over parallel execution, why model selection per role is a compounding advantage, and how to design systems that get better with each model generation instead of being made obsolete by them.

Speaker info:
- https://github.com/lukealvoeiro
- https://www.linkedin.com/in/lukealvoeiro

Timestamp:
0:00 Introduction to multi-agent systems and the bottleneck of human attention
1:50 Taxonomy of five frontier multi-agent frameworks
4:04 Introducing 'Missions': The three-role architecture (Orchestrator, Workers, Validators)
6:34 The importance of validation contracts for consistent quality
8:09 Maintaining long-term context through structured handoffs
9:17 The case for serial execution over parallel execution
10:30 Mission control: Monitoring agent progress
11:22 Strategic model selection per role ('Droid whispering')
13:06 Production data analysis: Building a Slack clone
14:34 Designing systems that improve with each model generation
15:51 Conclusion: The shifting economics of software engineering

## MCP UI: Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps

- Upload date: 2026-05-06
- Video: https://www.youtube.com/watch?v=o-zkvb0iFDQ
- Transcript: raw/20260506_o-zkvb0iFDQ/o-zkvb0iFDQ.en-orig.vtt
- Metadata: raw/20260506_o-zkvb0iFDQ/o-zkvb0iFDQ.info.json

Chat interfaces are no longer limited to walls of text. In this talk, Liad Yosef and Ido Salomon explain how MCP Apps turn tools into interactive UI inside hosts like ChatGPT, Claude, VS Code, Cursor, and Copilot, letting companies send branded, functional app experiences instead of plain text responses.

The session covers the core architecture behind MCP Apps, how UI is passed over MCP, how interactions stay in context through the host, and why this changes how applications get distributed in an agent-first world. If you're building on MCP, this is a practical look at the emerging standard for UI inside chat.

Timestamps:
0:00 Introduction to MCP Apps
1:02 Why we need MCP Apps: Moving beyond text-based chat
2:06 Evolution of the MCP UI standard and partnerships
3:25 Industry and community adoption
5:14 Core concepts: Passing UI over MCP
6:49 Practical demonstration (PostHog and Claude)
8:54 Technical architecture: How it works
10:23 A new era of web interaction and user experience
12:32 Interaction mindset and message spectrums
14:56 Future outlook: Reusable views and model-UI interaction
16:18 Spectrum of UI generation: Predefined vs. Generative

## The Small Model Infrastructure Nobody Built (So We Did) — Filip Makraduli, Superlinked

- Upload date: 2026-05-05
- Video: https://www.youtube.com/watch?v=qdh_x-uRs9g
- Transcript: raw/20260505_qdh_x-uRs9g/qdh_x-uRs9g.en-orig.vtt
- Metadata: raw/20260505_qdh_x-uRs9g/qdh_x-uRs9g.info.json

Most embedding infrastructure assumes you know exactly which model you want ahead of time. This talk starts where that assumption breaks. Filip Makraduli walks through the real profiling mistakes, infrastructure gaps, and production constraints that led to building an embedding inference engine designed for dynamic model loading, hot-swapping, and memory-aware eviction instead of brittle one-model-per-container deployments.

If you're working on small-model inference, embeddings, or GPU infrastructure, this is a practical look at what breaks in the real world and how to design around it.

Speaker info:
- https://www.linkedin.com/in/filipmakraduli/

Timestamps:
0:00 Introduction and the gap in small model inference
0:53 Moving from research to building inference infrastructure
2:54 Introduction of the Superlinked inference engine
4:34 The importance of context management for agents
7:03 Misconceptions: Why more GPUs isn't the only answer
9:33 The "Yin and Yang" of inference: Model support and infrastructure
10:43 The challenge of supporting diverse model architectures
14:33 Deep dive into infrastructure and scalability
16:10 Conclusion and the open-source launch of SAI

## Demand-Driven Context: A Methodology for Coherent Knowledge Bases Through Agent Failure

- Upload date: 2026-05-05
- Video: https://www.youtube.com/watch?v=_QAVExf_1uw
- Transcript: raw/20260505__QAVExf_1uw/_QAVExf_1uw.en-orig.vtt
- Metadata: raw/20260505__QAVExf_1uw/_QAVExf_1uw.info.json

Enterprise teams spend a lot of time trying to guess what AI agents need to know. This workshop flips that around. Instead of curating context top-down, Raj Navakoti shows how to build a demand-driven context base by giving agents real problems, watching where they fail, and using those failures to reveal exactly what knowledge is missing.

Using practical exercises and real examples from IKEA Digital, the session walks through how to grow a knowledge base problem by problem, structure it in Markdown, and use agents with different roles and reasoning boundaries against the same shared context. If you're building enterprise AI systems and want a more grounded way to create useful context, this is a strong practical framework.

Speaker info:
- https://www.linkedin.com/in/raj-navakoti-529880b1/

Timestamps:
0:00 - Introduction and speaker background
2:47 - The situation: Analogy to the movie Memento and AI's memory constraints
3:55 - Evolution of AI: From prompt engineering to deep agents
4:33 - Enterprise AI challenge: Why productivity isn't moving
5:33 - The problem: Green (general), Orange (taught), and Red (institutional/tribal) knowledge
10:11 - The Monolith: Why institutional knowledge is often outdated or missing
11:24 - Solution introduction: Demand-driven context
13:05 - The "Pull" strategy: Learning by doing vs. pushing information
14:48 - The agent lifecycle: Problem to discovery to documentation
17:46 - Demo introduction: Using a framework for context management
19:12 - Live demo: Incident root cause analysis and context discovery
24:05 - Scaling: 14 incidents to show confidence level improvement
26:27 - Automated scale: Validating knowledge across the monolith
33:01 - Storage strategy: Why GitHub is preferred for knowledge repositories
34:47 - The Meta Model: Navigating domain relationships
36:27 - Value proposition: Knowing the unknown and managing knowledge
39:02 - Summary: The 80/20 rule and cache-based context blocks
40:15 - Workshop takeaways: Repositories and scanners
43:33 - Q&A Session: Addressing scalability, tooling, and cost

## Accelerating AI on Edge — Chintan Parikh and Weiyi Wang, Google DeepMind

- Upload date: 2026-05-05
- Video: https://www.youtube.com/watch?v=Lm8BLHkxiAo
- Transcript: raw/20260505_Lm8BLHkxiAo/Lm8BLHkxiAo.en-orig.vtt
- Metadata: raw/20260505_Lm8BLHkxiAo/Lm8BLHkxiAo.info.json

As models get smaller and more capable, more AI workloads can move onto the device itself. In this talk, Chintan Parikh from Google DeepMind walks through what that looks like in practice, from Gemma 4 edge models and on-device agent skills to the real tradeoffs around latency, privacy, cost, and cross-platform deployment.

The session covers LiteRT, the Google AI Edge stack for running models across Android, iOS, desktop, web, and IoT, along with demos of local tool calling, structured output, reasoning, benchmarking, and hardware acceleration on CPUs, GPUs, and NPUs. If you're building on-device AI systems, this is a practical overview of the current edge stack and where it is headed.

Speaker info:
- https://www.linkedin.com/in/weiyiwang1993
- https://www.linkedin.com/in/chintansparikh

## Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs

- Upload date: 2026-05-04
- Video: https://www.youtube.com/watch?v=UsB70Tf5zcE
- Transcript: raw/20260504_UsB70Tf5zcE/UsB70Tf5zcE.en-orig.vtt
- Metadata: raw/20260504_UsB70Tf5zcE/UsB70Tf5zcE.info.json

Training an LLM from scratch on a local machine sounds unreasonable, until it isn't. In this workshop, Angelos Perivolaropoulos from ElevenLabs walks through what it actually takes to train a language model locally, with a practical focus on the tooling, constraints, and engineering tradeoffs involved.

If you want a hands-on look at small-scale LLM training beyond the cloud-heavy default, this is a useful deep dive.

Speaker info:
- https://www.linkedin.com/in/angelos-perivolaropoulos/
- https://github.com/angelos-p

Timestamp:
0:00 Introduction and background of the speaker
1:21 Overview of the workshop objectives
3:12 Inspiration from Andre Karpathy's NanoGPT
4:37 The four fundamental building blocks of an LLM
7:08 Prerequisites and setup tools (UV, Python, hardware requirements)
9:06 Part 1: The Tokenizer (character-level tokenization explained)
24:29 Model architecture and parameters (vocab size, layers, embeddings)
30:13 The GPT class structure and transformer blocks
37:52 Parameter count and model sizing
40:54 The training loop: objectives and next-token prediction
44:44 Optimization and learning rate strategies (warm-up and cosine decay)
47:56 Validation and monitoring loss
53:07 Part 3: Text generation and inference strategies
56:30 Putting it all together (project file structure)
58:46 Monitoring training and debugging common issues
1:00:27 Workshop challenge and competition details
1:05:24 Q&A: Differences between base models and reasoning models
1:11:31 Q&A: Applying these concepts to audio and multimodal models

## Skill Issue: How We Used AI to Make Agents Actually Good at Supabase — Pedro Rodrigues, Supabase

- Upload date: 2026-05-04
- Video: https://www.youtube.com/watch?v=GmAQKINjv1E
- Transcript: raw/20260504_GmAQKINjv1E/GmAQKINjv1E.en-orig.vtt
- Metadata: raw/20260504_GmAQKINjv1E/GmAQKINjv1E.info.json

Writing Agent Skills is easy. Writing ones that actually improve agent performance is not.

In this hands-on workshop, you’ll build, test, and iterate on Agent Skills against real Supabase workflows using a prebuilt environment with MCP, CLI tooling, and an eval harness powered by Braintrust.

You’ll start by writing a simple Skill and observing how it changes agent behavior. Then we’ll push further: you’ll modify the Skill, introduce bad patterns, and see how performance shifts — sometimes improving, sometimes getting worse, and sometimes doing nothing at all. Along the way, we’ll surface common failure modes, like Skills that aren’t used, misleading instructions, or changes that look good but don’t hold up under evaluation.

The core loop of the workshop is simple: write a Skill, run evals, inspect results, and iterate. By the end, you’ll have a practical understanding of how to validate Skills, how to avoid common pitfalls, and how to design Skills that actually help agents perform better in real systems.

If you’re working with agents, this workshop will give you the tools to move beyond guesswork and start measuring what actually works.

And if you want to see how these patterns hold up at scale, the follow-up talk on the 9th dives into our eval results and what actually moved the needle in production.

Speaker info:
- https://supabase.com/blog/authors/pedro_rodrigues
- https://www.linkedin.com/in/pedro-neves-rodrigues/

## Ralph Loops: Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick

- Upload date: 2026-05-04
- Video: https://www.youtube.com/watch?v=2TLXsxkz0zI
- Transcript: raw/20260504_2TLXsxkz0zI/2TLXsxkz0zI.en-orig.vtt
- Metadata: raw/20260504_2TLXsxkz0zI/2TLXsxkz0zI.info.json

Dumb loops beat clever workflows. Most teams building with AI agents reach for multi-agent orchestration, planning graphs, and elaborate tool chains. Then they spend months debugging them. A single loop that processes one ticket at a time, evaluates its own output, and improves on the next run will outperform all of it.

In this hands-on workshop you will build three things. First, a working Ralph Loop that processes real tickets end-to-end. Second, a synthetic feedback loop so you can test and iterate locally without waiting on production data. Third, a self-improving cycle where the loop's output quality gets better with every run without you touching the prompt.

Speaker info:
- https://x.com/chrismdp
- https://www.linkedin.com/in/chrisparsons/
- https://github.com/chrismdp

Timestamps:
0:00 Introduction to the workshop and Ralph Loops
6:12 How AI agents work on loops
10:06 Using loops for software development
10:43 Live coding: Building a Pomodoro timer
12:13 Explaining the ticket system
15:01 Implementing the first ticket (Status command)
17:37 The simplest Ralph Loop: A while loop
22:12 Next steps and taking the concept to the next level
28:19 Implementing further tickets using TDD principles
40:33 Advanced feature: The 'loop' command in Claude Code
49:39 Structuring and managing Ralph Loops
55:33 Using sub-agents for better validation
59:39 The 'startup' skill and ambitious automation
1:04:10 Real-world application: Worker and morning loops
1:09:19 Q&A: Determining when to stop open-ended tasks
1:13:31 VCP command and project context
1:15:52 Q&A: Handling context rot
1:17:01 Q&A: Reviewing sessions and verification
1:22:38 Q&A: Versioning prompts and skills
1:27:12 Q&A: Knowledge management and system organization
1:38:34 Closing, feedback, and final questions

## Context Is the New Code — Patrick Debois, Tessl

- Upload date: 2026-05-03
- Video: https://www.youtube.com/watch?v=bSG9wUYaHWU
- Transcript: raw/20260503_bSG9wUYaHWU/bSG9wUYaHWU.en-orig.vtt
- Metadata: raw/20260503_bSG9wUYaHWU/bSG9wUYaHWU.info.json

As AI coding agents become more capable, context is starting to matter as much as code. Yet while code has version control, review, testing, CI/CD, and production observability, the prompts, rules, and memory that drive agents are still often managed like ad hoc hacks.

Patrick argues that context needs its own engineering discipline. He introduces the Context Development Lifecycle: Generate, Evaluate, Distribute, and Observe, along with the team practices that make context a shared, repeatable, and improvable part of software delivery. The session also explores the larger context flywheel, where better context leads to better agent output, which creates better observations, which in turn improves context again.

Speaker info:
- https://x.com/patrickdebois
- https://www.linkedin.com/in/patrickdebois/

Timestamps:
0:00 - Introduction to the talk
1:14 - Why context is the new code
2:37 - Introducing the Context Development Lifecycle
3:50 - Generate: Creating context for agents
6:26 - Evaluate: Testing your context
13:59 - Distribute: Sharing and packaging context
17:49 - Observe: Monitoring and feedback loops
22:33 - Conclusion and the context flywheel
24:49 - Q&A session

## TLMs: Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google

- Upload date: 2026-05-03
- Video: https://www.youtube.com/watch?v=BKWpYIWvAo4
- Transcript: raw/20260503_BKWpYIWvAo4/BKWpYIWvAo4.en-orig.vtt
- Metadata: raw/20260503_BKWpYIWvAo4/BKWpYIWvAo4.info.json

Tiny LLMs are making on-device agents much more practical. In this workshop, Cormac Brick walks through how LiteRT-LM brings language models to edge devices, with a focus on Gemma, agent skills, and the real engineering tradeoffs behind running LLM workflows on phones and other constrained hardware. The session covers performance across edge devices, on-device function calling, fine-tuning and deployment, platform support across Android and iOS, and the memory, safety, and UX constraints that shape edge-native AI systems. If you're building local agents or want a practical look at where edge LLMs are headed, this is a useful hands-on overview.

Speaker info:
- https://www.linkedin.com/in/cbrick/

Timestamps

(0:00:00) Intro: AI on the Edge, Small Language Models, and Gemma
(0:04:51) Enabling App Development: MediaPipe, LiteRT, and System Services
(0:09:09) Small Language Models: Performance, Reach, and Fine-tuning
(0:11:30) Gemma 4: Sizes (E2B and E4B) and AI Core Roadmap
(0:16:10) Gemma on Edge Runtime: Performance Benchmarks
(0:18:34) Agent Skills: Google AI Gallery, Mood Tracker, and Wikipedia Lookup
(0:23:38) Skill Architecture: Efficiency, Progressive Disclosure, and Tool Loading
(0:27:34) Reliability: Constrained Decoding and Tool Usage
(0:29:18) Community and Custom Skills
(0:31:30) Skill Development Deep Dive: Orchestrator and Registry
(0:33:30) Rapid Skill Prototyping: Using Gemini CLI and ADB
(0:38:35) Open Source: AI Edge Gallery and Community Engagement
(0:41:00) Deploying Tiny Models (sub-1B parameters) In-App
(0:47:44) Third-Party Models: Fast VLM and Hardware Acceleration
(0:50:17) Model Examples: Function Gemma, Mobile Actions, and Embedding Gemma
(0:55:41) AI Edge Eloquent: Transcription and Text Polishing
(0:59:07) Modularity Playbook: ASR and Text Polishing Engines
(1:01:23) Synthetic Data Workflows for Tiny Models
(1:06:36) Web Support and Fine-tuning Documentation
(1:08:20) Summary and Key Takeaways
(1:12:49) Q&A: Multi-skill Execution, Context Windows, and Future Roadmap

## Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked

- Upload date: 2026-05-03
- Video: https://www.youtube.com/watch?v=5ID22ACI7IM
- Transcript: raw/20260503_5ID22ACI7IM/5ID22ACI7IM.en-orig.vtt
- Metadata: raw/20260503_5ID22ACI7IM/5ID22ACI7IM.info.json

Agents can generate code. The hard part is generating code that's right for your system, team conventions, and past decisions. That's a context problem that naive RAG, MCP servers, and bigger context windows don't solve. Without the right context, that code costs you twice: once in tokens, again in long review cycles.

This session is a practitioner's guide to building a context engine: the reasoning layer that brings together your organizational context and delivers only what the agent needs for the task at hand. I'll walk through the challenges that matter: reasoning across conflicting sources, maintaining permissions, and personalizing results based on who's asking and what they're working on. Along the way, we'll go deep on specific components with live demos and technical breakdowns.

Drawn from real lessons building this in production, including what we got wrong.

## Human-in-the-Loop Automation with n8n — Liam McGarrigle

- Upload date: 2026-05-02
- Video: https://www.youtube.com/watch?v=tDArkCqjA-c
- Transcript: raw/20260502_tDArkCqjA-c/tDArkCqjA-c.en-orig.vtt
- Metadata: raw/20260502_tDArkCqjA-c/tDArkCqjA-c.info.json

What does it actually take to build an AI workflow that can do useful work without becoming a black box? This workshop shows how to build secure, human-in-the-loop automations in n8n, using a Gmail and Google Calendar management agent as the concrete example. Liam McGarrigle walks through how to wire it together with n8n's visual automation system and combine chat triggers, tools, credentials, approvals, and access control into a workflow that can actually be observed and controlled. The session also covers how to extend the agent beyond the demo, including Slack-based interaction, scheduled runs, sub-workflows, and specialized subagents for larger real-world automation systems.

Speaker info:
- https://www.linkedin.com/in/liam-mcgarrigle
- https://github.com/liamdmcgarrigle

## I Gave an AI Agent the Keys to My Life (Here's What Happened) — Radek Sienkiewicz (@velvetshark-com)

- Upload date: 2026-05-02
- Video: https://www.youtube.com/watch?v=sJ2jc7leKBk
- Transcript: raw/20260502_sJ2jc7leKBk/sJ2jc7leKBk.en-orig.vtt
- Metadata: raw/20260502_sJ2jc7leKBk/sJ2jc7leKBk.info.json

An honest look at what happens when a personal AI agent is allowed to operate around the clock. Over months, one permission at a time, it went from reading files to handling email, backing up its own memory at 2am, monitoring its own health, and drafting real business replies. This talk covers the permission creep, the overnight cron ecosystem, self-monitoring and recovery, trust boundaries, and the surprising value of giving an agent a personality that disagrees with its owner.

Speaker info:
- https://x.com/velvet_shark
- https://www.linkedin.com/in/radeksienkiewicz/
- https://github.com/velvetshark

Timestamps
0:15 Radek's path to OpenClaw
2:17 The philosophy of incremental growth and system updates
4:51 Integrating the Obsidian knowledge base
8:59 Ambient operations and overnight automation
11:02 Core job types for the AI agent (Ambient Operations, Attention Filtering, Execution)
13:03 Deep dive into specific Discord integration channels
14:54 System architecture: LLMs, scripts, and memory management
16:28 Challenges: Bad memory, brittle automations, and noisy nodes
17:19 Conclusion: Optimizing for the future self

## Software Engineering Is Becoming Plan and Review — Louis Knight-Webb, Vibe Kanban

- Upload date: 2026-05-02
- Video: https://www.youtube.com/watch?v=W76woOYHlvY
- Transcript: raw/20260502_W76woOYHlvY/W76woOYHlvY.en-orig.vtt
- Metadata: raw/20260502_W76woOYHlvY/W76woOYHlvY.info.json

AI eats the middle, software engineers are spending all their time planning and reviewing the work of AI. If all humans are going to do is plan and review the work of AI, the biggest lever you have to ship more is to speed up planning and review.

And some examples of how teams and individuals are adapting:
- What tools are people spending their time in?
- How much time are teams spending reviewing code, how has this changed since AI?
- What are different approaches to planning work?
- Is agile and scrum dead?

Speaker info:
- https://x.com/tokengobbler
- https://www.linkedin.com/in/knightwebb/
- https://github.com/stunningpixels

Timestamps:
0:00 - Intro and agenda
1:45 - Why software engineering is shifting to plan and review
3:30 - The two approaches: Plan-based vs. Review-heavy
6:02 - The matrix: Feature development vs. migrations and maintenance
7:27 - The impact of agent execution time
9:52 - Managing the 'five-minute' agent threshold
10:29 - Parallelization and workflow management
12:00 - Vision for future coding interfaces and 'focus maxing'
14:00 - Announcement: Shutting down Vibe Kanban
18:13 - Q&A: Next steps and reflections on the startup journey

## Agents for Everything Else — swyx

- Upload date: 2026-05-01
- Video: https://www.youtube.com/watch?v=zepu8Kk6FBQ
- Transcript: raw/20260501_zepu8Kk6FBQ/zepu8Kk6FBQ.en-orig.vtt
- Metadata: raw/20260501_zepu8Kk6FBQ/zepu8Kk6FBQ.info.json

How we run AI Engineer with Agents like Cognition's Devin and Town Assistant

Speaker info:
- x.com/swyx
- github.com/swyxio

## Agents on the Canvas in tldraw — Steve Ruiz, tldraw

- Upload date: 2026-05-01
- Video: https://www.youtube.com/watch?v=sPUjIBH5Cwg
- Transcript: raw/20260501_sPUjIBH5Cwg/sPUjIBH5Cwg.en-orig.vtt
- Metadata: raw/20260501_sPUjIBH5Cwg/sPUjIBH5Cwg.info.json

At tldraw, we've been bringing agents to our infinite canvas. In December 2025, we ran a one-month experiment named Fairydraw where users could work with three fairies—virtual collaborators who work with you, with your human collaborators, and coordinate together on large tasks. Learn what we learned.

Speaker info:
- https://x.com/steveruizok
- https://www.linkedin.com/in/steve-ruiz-61a150239/

## Shipping complex AI applications — Braintrust & Trainline

- Upload date: 2026-05-01
- Video: https://www.youtube.com/watch?v=ZdheJTfLu-s
- Transcript: raw/20260501_ZdheJTfLu-s/ZdheJTfLu-s.en-orig.vtt
- Metadata: raw/20260501_ZdheJTfLu-s/ZdheJTfLu-s.info.json

Getting a prototype working is straightforward. Making it reliable in production, especially with multi-step agents, tool use, and real users is the hard part. In this hands-on workshop, you'll work through the core parts of building production-grade AI applications with Giran Moodley, Mayank Soni, and Oussama Hafferssas.

Socials: 
- https://uk.linkedin.com/in/mayank-soni
- https://x.com/OussamaHaff
- https://www.linkedin.com/in/giran/

Timestamps

0:00 - Introduction and Welcome
4:07 - Workshop Overview and Agenda
4:39 - Understanding AI Engineering and Operational Challenges
9:55 - Introduction to Braintrust
12:56 - Experience from Trainline
28:35 - Building the Support Triage Agent (Overview)
33:57 - Basic Implementation: Single Shot Prompting
40:32 - Adding Local Tools for Determinism
41:30 - Implementing Specialist Stages (Agentic Flow)
46:19 - Instrumenting and Tracing the Application
56:43 - Evaluating AI Systems and Golden Data Sets
1:05:07 - Deploying and Managing AI in Production
1:13:58 - Online Scoring and Monitoring Production Logs
1:19:13 - Identifying and Remediating Failure Modes
1:33:05 - Key Takeaways and Summary
1:36:58 - Further Resources and Documentation

## Mastering AI Pricing — Mayank Pant, Stripe

- Upload date: 2026-05-01
- Video: https://www.youtube.com/watch?v=CrqPcIZOOXA
- Transcript: raw/20260501_CrqPcIZOOXA/CrqPcIZOOXA.en-orig.vtt
- Metadata: raw/20260501_CrqPcIZOOXA/CrqPcIZOOXA.info.json

Monetizing AI is hard. Rising GPU and inference costs are squeezing margins, and traditional SaaS pricing simply does not work for the unpredictable compute demands of new-age AI companies. With models constantly shifting across credits, tokens, and seats, a new challenge emerges: how do we charge for AI without stalling growth? This talk presents a framework for solving the dual problems of aligning charge metrics with true customer value and balancing predictable revenue with rapid adoption. Through real-world examples, we'll explore how to build guardrails that protect your margins and see how Stripe's world-class usage-based billing solution helps AI companies launch quickly and monetize with ultimate agility. Whether you're launching your first AI product or revamping your current model, you'll learn how to make your pricing strategy both profitable and adaptable.

## LLM codegen fails and how to stop 'em — Danilo Campos, PostHog

- Upload date: 2026-04-30
- Video: https://www.youtube.com/watch?v=juoNbJiZUi0
- Transcript: raw/20260430_juoNbJiZUi0/juoNbJiZUi0.en-orig.vtt
- Metadata: raw/20260430_juoNbJiZUi0/juoNbJiZUi0.info.json

Danilo Campos breaks down the most common failure modes in LLM code generation and the practical strategies PostHog uses to prevent them. Drawing from a system that helps 5,000+ users each month, he shares a playbook for making autonomous codegen more reliable, correct, and production-ready.

Speaker info:
- https://www.linkedin.com/in/danilocampos

## Building Conversational Agents — Thor Schaeff and Philipp Schmid, Google DeepMind

- Upload date: 2026-04-30
- Video: https://www.youtube.com/watch?v=cVzf49yg0D8
- Transcript: raw/20260430_cVzf49yg0D8/cVzf49yg0D8.en-orig.vtt
- Metadata: raw/20260430_cVzf49yg0D8/cVzf49yg0D8.info.json

Thor Schaeff and Philipp Schmid show how to build conversational agents with Google DeepMind's Gemini APIs, from tool-using coding agents to realtime voice interfaces. The session covers the new Interactions API, agent skills, server-side state, and the Live API workflow for streaming audio, video, and tool calls into multimodal assistants.

Speaker info:
- https://x.com/_philschmid
- https://x.com/thorwebdev

Timestamps
0:14 - Introduction and speaker introductions
6:15 - Audience interaction and project discussions
8:38 - Introduction to building conversational agents
28:17 - Discussion on Gemini Flash for coding and agentic use
36:28 - Coding agent implementation and tool calling demonstration
42:55 - Overview of the Interactions API and state management
49:05 - Introduction to the Gemini Live API
50:02 - Live Jukebox demo with music generation
54:49 - Deep dive into Gemini Flash Live features (multimodality, latency, tools)
1:06:54 - Technical setup and implementation of the Live API using WebSockets
1:25:14 - Session management and context window compression
1:26:57 - Real-world business use cases for conversational agents
1:35:02 - Multimodal grounding and handling audio inputs
1:40:00 - Discussion on personalization and speaker identification

## Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor

- Upload date: 2026-04-30
- Video: https://www.youtube.com/watch?v=WE_Gnowy3uw
- Transcript: raw/20260430_WE_Gnowy3uw/WE_Gnowy3uw.en-orig.vtt
- Metadata: raw/20260430_WE_Gnowy3uw/WE_Gnowy3uw.info.json

David Gomes shows how Cursor replaced a heavyweight WorkTrees feature with a lightweight layer built from skills, commands, and subagents. He walks through how parallel coding workflows were recreated with roughly 200 lines of Markdown, plus the tradeoffs, failure modes, and lessons that come with moving product behavior from code into prompts.

Speaker info:
- https://x.com/davidgomes
- https://github.com/davidgomes/

Timestamps
0:14 Introduction and the concept of markdown as code
0:59 Recap of Git work trees in Cursor
3:10 Complexity of the initial implementation
4:18 Deleting 15,000 lines of code
4:54 Implementing features with Skills and Sub-agents
5:51 How the new Skills are structured
7:58 New Slash commands and workflow
9:58 Pros of the new implementation
12:15 Cons and user feedback challenges
14:17 Future improvements: Evals and RL training
17:05 What's next for Cursor 3.0 and native work trees

## Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI

- Upload date: 2026-04-29
- Video: https://www.youtube.com/watch?v=fLUtUkqYHnQ
- Transcript: raw/20260429_fLUtUkqYHnQ/fLUtUkqYHnQ.en-orig.vtt
- Metadata: raw/20260429_fLUtUkqYHnQ/fLUtUkqYHnQ.info.json

A new class of small models is emerging with the ability to reliably follow instructions and call tools while running on-device under 1 GB of memory. In this talk, we'll break down how to post-train frontier small models using the LFM2.5 recipe: on-policy preference alignment, agentic reinforcement learning, and curriculum training with iterative model merging. We'll cover training challenges unique to the 1B scale, like doom loops, capability interference, and how to fix them. The goal is to give you a concrete playbook to fine-tune and deploy small models for your own use cases, from structured data extraction to multi-turn tool use.

Speaker info:
- https://x.com/maximelabonne
- https://www.linkedin.com/in/maxime-labonne/
- https://github.com/mlabonne

Timestamps:
0:00:00 - Start
0:00:14 - Introduction to frontier small models at Liquid AI
0:01:02 - Characteristics: memory-bound, task-specific, latency-sensitive
0:02:20 - Architecture: why large embedding layers are inefficient
0:04:01 - LFM2 architecture: using gated short convolutions for speed
0:06:09 - LFM 2.5 recipe: 28T tokens and post-training stages
0:08:34 - Post-training: SFT, preference alignment, and RL best practices
0:10:43 - Identifying "doom loops" in reasoning models
0:11:34 - Solutions: mitigating loops via preference alignment and RL
0:15:29 - Future focus: using agentic tools to overcome memory limits
0:17:58 - Q&A: real-world applications for small vs. large models

## OpenAI Codex Masterclass  — Vaibhav Srivastav & Katia Gil Guzman

- Upload date: 2026-04-29
- Video: https://www.youtube.com/watch?v=MhHEGMFCEB0
- Transcript: raw/20260429_MhHEGMFCEB0/MhHEGMFCEB0.en-orig.vtt
- Metadata: raw/20260429_MhHEGMFCEB0/MhHEGMFCEB0.info.json

Codex is no longer just a coding assistant in a terminal. In this workshop, Vaibhav and Katia show how it becomes a full software engineering system, combining frontier models, the Codex app and CLI, plugins, automations, and subagents that can explore, review, and execute work in parallel. The session also dives into custom subagents: showing how specialized agents with different models, permissions, and tools can speed up code review, research, debugging, and long-running tasks while keeping control and safety in place.

Speaker info:
- Vaibhav Srivastav | https://x.com/reach_vb
- Katia Gil Guzman | https://www.linkedin.com/in/katiagilguzman/

Timestamps
(0:14) Introduction to the workshop and speakers
(1:48) What is Codex? (Overview of software engineering agent capabilities)
(2:18) Foundation models (GPT-5.3, Spark, GPT-5.4)
(4:11) The evolution of models and performance improvements (Websockets, Fast Mode)
(7:04) Codex app features, projects, and work trees
(8:37) Automations overview
(12:28) Plugins: Skills, apps, and MCP servers
(15:13) Game and Web development plugins (Playwright and Image Gen)
(16:26) Demo: Game studio plugin and generating assets
(17:23) Demo: Google Drive plugin for codebase data
(18:52) Demo: Setting up automations for Slack and Gmail
(27:14) Code Review features and integration with GitHub
(32:39) Subagents: Parallelizing tasks and custom personas
(36:18) Demo: Using subagents to review persona files
(44:52) Creating custom subagents
(49:29) Bleeding edge features: Guardian approvals, hooks, and personality settings
(56:11) Codex security and Cloud Code plugin
(57:10) Q&A session

## Build & deploy AI-powered apps — Paige Bailey, Google DeepMind

- Upload date: 2026-04-29
- Video: https://www.youtube.com/watch?v=G_bHFmEAarM
- Transcript: raw/20260429_G_bHFmEAarM/G_bHFmEAarM.en-orig.vtt
- Metadata: raw/20260429_G_bHFmEAarM/G_bHFmEAarM.info.json

Got a massive idea but stuck in the "just talking about it" phase? This session cuts the fluff and dives straight into how to build and prototype at lightning speed using AI Studio Build and Antigravity for free. It breaks down Google DeepMind's AI tech stack so viewers know exactly which tools to use, when to reach for heavyweights like Gemini 3.1 Pro or the new Gemma 4, and when to stay fast with Gemini 3 Flash and Flash-Lite. It also explores Veo 3.1 Lite for video generation, NanoBanana 2, Lyria 3 for music generation, Genie 3 for world model building, and OpenClaw with Gemini to push prototype limits. Expect basically zero slides and more shipping, with live demos showing how to turn side quests from ideas into working prototypes, add new features to existing codebases, and troubleshoot builds and ideas in a live Q&A.

Speaker info:
- https://x.com/DynamicWebPaige
- https://linkedin.com/in/dynamicwebpaige
- https://github.com/dynamicwebpaige

## Building your own software factory — Eric Zakariasson, Cursor

- Upload date: 2026-04-28
- Video: https://www.youtube.com/watch?v=rnDm57Py54A
- Transcript: raw/20260428_rnDm57Py54A/rnDm57Py54A.en-orig.vtt
- Metadata: raw/20260428_rnDm57Py54A/rnDm57Py54A.info.json

Most of us are pair-programming with one agent and stopping there. There's a lot more on the table. This workshop is about going from one agent to many. We'll start with codebase setup, the foundational work that makes agents effective on their own. Then we'll scale up to running agents in parallel, kicking off async work that keeps going while you context-switch to something else, and setting up automations for the things you're still doing by hand.

Speaker info:
- https://x.com/ericzakariasson
- https://www.linkedin.com/in/ericzakariasson/
- https://github.com/ericzakariasson

Timestamps:
0:00:00 - Workshop introduction and vision for autonomous software factories
0:01:26 - Frameworks and stages of agentic autonomy
0:08:58 - Establishing scalable, reproducible dev environments for agents
0:10:00 - Importance of verifiable systems and automated testing pipelines
0:10:47 - Cursor 3 walkthrough: Redesigned agent-first interface
0:15:26 - Cloud agents: Scaling via dedicated VMs and computer control
0:19:17 - Managing asynchronous workflows and frontloading context
0:24:45 - Automating repetitive tasks to build feedback loops
0:29:28 - Continual learning: Extracting rules from chat transcripts
0:30:48 - Scaling management: Moving to nested agent orchestration
0:31:08 - Strategic takeaways: Human accountability and observability
0:33:39 - Q&A: Addressing code quality and architectural guardrails
0:53:07 - Best practices for human-to-agent collaboration and handoffs
1:03:05 - Maintaining the factory: Managing documentation and specs
1:10:06 - Integrating Linear and Slack for automated issue triage
1:14:14 - Local execution: Leveraging Cursor harness locally

## Why building eval platforms is hard — Phil Hetzel, Braintrust

- Upload date: 2026-04-28
- Video: https://www.youtube.com/watch?v=_fQ7Z_Wfouk
- Transcript: raw/20260428__fQ7Z_Wfouk/_fQ7Z_Wfouk.en-orig.vtt
- Metadata: raw/20260428__fQ7Z_Wfouk/_fQ7Z_Wfouk.info.json

An eval platform is not just a test runner. You are building shared definitions of "good," reliable data pipelines, labelling workflows, versioning, and trust in results across many teams and model changes. This session breaks down the hidden complexity, the common failure modes, and the design principles that make evals credible and usable in day-to-day engineering.

Speaker info:
- https://www.linkedin.com/in/philliphetzel/

## One Login to Rule Them All: Cross-App Access for MCP — Garrett Galow, WorkOS

- Upload date: 2026-04-28
- Video: https://www.youtube.com/watch?v=EmhRyw6xeT0
- Transcript: raw/20260428_EmhRyw6xeT0/EmhRyw6xeT0.en-orig.vtt
- Metadata: raw/20260428_EmhRyw6xeT0/EmhRyw6xeT0.info.json

Connecting a coding agent to multiple services often means facing a dozen OAuth consent screens, a dozen token lifecycles, and a dozen chances for something to break. Despite having Single Sign-On, users still find themselves signing in repeatedly.

This talk explores how Cross-App Access leverages a three-way trust between the MCP client, the MCP server, and the organization's Identity Provider to simplify authentication. Through the Identity Assertion Authorization Grant flow, a single SSO login is transformed into access tokens across every MCP server, offering seamless access to all applications. The session will also highlight what this pattern enables for agent identity beyond MCP.

Speaker info:
https://www.linkedin.com/in/garrett-galow/

## Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind

- Upload date: 2026-04-27
- Video: https://www.youtube.com/watch?v=_A367W_qvc8
- Transcript: raw/20260427__A367W_qvc8/_A367W_qvc8.en-orig.vtt
- Metadata: raw/20260427__A367W_qvc8/_A367W_qvc8.info.json

Open models are getting smaller, faster, and far more capable. In this talk, Cassidy Hardin walks through the latest advances in the Gemma family, with a focus on Gemma 4 and what it enables for developers building on-device and open-weight AI systems. She covers the architecture behind Gemma’s dense, effective, and mixture-of-experts models, including improvements to attention, multimodal support for text, vision, and audio, and the design decisions that make strong reasoning, coding, and agentic workflows possible at practical sizes.

Speaker info:
- https://uk.linkedin.com/in/cassidyhardin

Timestamps:
00:00:28 - Introduction to the Gemma 4 model family and its four size categories
00:01:54 - Shift to Apache 2.0 licensing for developer accessibility
00:02:25 - Deep dive into the 31B dense reasoning and 26B mixture-of-experts (MoE) models
00:03:30 - Overview of on-device effective models (2B and 4B) with multimodal support
00:04:21 - Architectural updates: interleaved local/global attention and grouped query attention
00:06:51 - Explanation of the new MoE architecture (128 experts, 8 active)
00:07:44 - Implementation of Per Layer Embeddings (PLE) to optimize on-device memory
00:11:06 - Multimodal advances: variable aspect ratios and resolutions for vision encoders
00:16:31 - Audio processing enhancements via conformer architecture and audio tokenizers
00:18:07 - Getting started: self-hosting (Hugging Face, Ollama) and cloud deployment (Vertex AI)

## Gateways are All You Need — Karan Sampath, Anthropic

- Upload date: 2026-04-27
- Video: https://www.youtube.com/watch?v=CD6R4Wf3jnY
- Transcript: raw/20260427_CD6R4Wf3jnY/CD6R4Wf3jnY.en-orig.vtt
- Metadata: raw/20260427_CD6R4Wf3jnY/CD6R4Wf3jnY.info.json

MCPs are often flaky, face multiple security vulnerabilities, and are generally hard to scale. Most enterprises struggle to use more than single digit numbers of MCPs due to issues with security, observability, and access control. In this talk, we'll explore the approaches and learnings we at Anthropic have been taking to solve this, and make MCPs more enterprise ready.

Speaker info:
- https://x.com/karan_sampath
- https://www.linkedin.com/in/karansampath/
- https://github.com/karansampath

Timestamps:
00:00:14 - Introduction: Enterprise MCP challenges.
00:01:13 - Enterprise Hurdles: Observability, access control, and security (the "three-headed hydra").
00:03:35 - Deployment Bottlenecks: Scalability limits of current decentralized models.
00:05:35 - The Case for Gateways: Establishing a unified "root of trust."
00:07:00 - Gateway Definition: A middleware layer for auth, proxying, and routing.
00:08:28 - Core Components: Implementing OAuth, tunnels, and developer CLIs.
00:10:03 - Strategic Benefits: Improved authentication and standardized access control.
00:11:30 - Operational Gains: Multi-surface integration, security, and faster iteration.
00:15:13 - Future Vision: Decoupling agent architecture from data layers.
00:16:58 - Summary: Invest in common infrastructure to scale enterprise agents.

## Scaling GitHub for your Agents — Sam Morrow, GitHub

- Upload date: 2026-04-27
- Video: https://www.youtube.com/watch?v=0n3MKk7r60w
- Transcript: raw/20260427_0n3MKk7r60w/0n3MKk7r60w.en-orig.vtt
- Metadata: raw/20260427_0n3MKk7r60w/0n3MKk7r60w.info.json

GitHub operates one of the most heavily-utilised MCP servers in the ecosystem, with over 4 million downloads of the stdio server alone. Discover the architectural decisions, technical challenges and lessons learned while building and scaling a remote MCP server on production infrastructure. The session walks through the journey from initial implementation to horizontal scaling, covering the specific challenges of condensing a platform as expansive as GitHub into a coherent MCP interface. Attendees will learn practical strategies for managing tool overload, optimizing context usage, implementing distributed session storage, and maintaining observability without compromising user privacy. Whether building a first remote server or optimizing an existing implementation, attendees will gain concrete patterns, anti-patterns, and architectural guidance from real production experience.

Key Takeaways:
• Architecture patterns for stateless, horizontally scalable remote MCP servers
• Practical approaches to tool proliferation and context window constraints
• Why a focus on auth, security and privacy is essential to success

Speaker info:
https://www.linkedin.com/in/sammorrow
https://github.com/SamMorrowDrums

Timestamps:
0:00:29 - Overview of GitHub's MCP public launch and community growth.
0:02:06 - Challenges of tool proliferation and impact on agent context.
0:03:21 - Mitigation via "tool sets" and dynamic discovery.
0:05:54 - Optimizing API output tokens to improve efficiency.
0:06:44 - Improving reliability through intent-based tool design.
0:08:14 - Security strategy: OAuth 2.1 and PKCE implementation.
0:10:40 - Managing prompt injection and security vulnerabilities.
0:12:35 - Using OAuth scopes for granular tool filtering.
0:13:47 - Stateless server architecture and Redis session management.
0:15:18 - Experimental features and human-in-the-loop UX.
0:16:30 - Future outlook: Compositional tools and automation.
0:18:04 - Final project metrics: Downloads, forks, and volume.

## Collaborative AI Engineering: One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub

- Upload date: 2026-04-26
- Video: https://www.youtube.com/watch?v=ClWD8OEYgp8
- Transcript: raw/20260426_ClWD8OEYgp8/ClWD8OEYgp8.en-orig.vtt
- Metadata: raw/20260426_ClWD8OEYgp8/ClWD8OEYgp8.info.json

Agentic engineering so far has been a solo story: one developer and a dozen agents moving at warp speed. But speed without thoughtful planning and team alignment is just wasting tokens. When everyone on a team is directing agents alone in their personal CLI tools with no shared context, you get duplicate work, conflicting changes, poorly-designed solutions, surprise features nobody else agreed to build, and everyone pulling in different directions.

Serious software still requires serious collaboration. You need multiple perspectives and types of expertise to build great things. We need agentic environments where people can plan together, think critically together, and share the same context. In this talk I'll demo how we've tackled these design problems in Ace, a multiplayer agent environment from GitHub Next that uses real-time collaboration, proactive agents, and sandboxed micro VMs for rapid prototyping and exploration.

Speaker info:
- https://x.com/Mappletons

## AgentCraft: Putting the Orc in Orchestration — Ido Salomon

- Upload date: 2026-04-25
- Video: https://www.youtube.com/watch?v=kR64LOqBBCU
- Transcript: raw/20260425_kR64LOqBBCU/kR64LOqBBCU.en-orig.vtt
- Metadata: raw/20260425_kR64LOqBBCU/kR64LOqBBCU.info.json

As we run more agents in parallel, it becomes clear: we are the bottleneck. Luckily, the skills we need for effective multi-agent orchestration aren’t entirely new, they’ve just been hiding in unexpected places.Through AgentCraft, the game-inspired agent orchestrator, I’ll explore how we can raise the ceiling of human-agent collaboration without burning out in the process.

Speaker info:
- https://github.com/idosal
- https://www.linkedin.com/in/ido-salomon/
- https://x.com/idosal1

## MCP = Mega Context Problem - Matt Carey

- Upload date: 2026-04-25
- Video: https://www.youtube.com/watch?v=YBYUvGOuotE
- Transcript: raw/20260425_YBYUvGOuotE/YBYUvGOuotE.en-orig.vtt
- Metadata: raw/20260425_YBYUvGOuotE/YBYUvGOuotE.info.json

The best MCP server is the one you didn't have to build.

At Cloudflare we have a lot of products. Our REST OpenAPI spec is over 2.3 million tokens. When teams started building MCP servers, they did what everyone does: cherry-picked important endpoints for their product, wrote some tool definitions and shipped a separate service that covered a small fraction of their API.

This was driven by a fundamental context limit of the end users' agent. And tools use a bunch of context just to describe themselves. MCP felt like a Mega Context Problem (and a separate service to maintain).

I think we got it all wrong.

The context limit is not an MCP problem. It's an agent problem. Tools should probably be discovered on demand and clients are coming around to this. But maybe we can also do it on the server?

CLIs get this for free, self-discoverable and documented by design. APIs just need a little help.

This talk will cover some of the techniques we've been exploring at Cloudflare, such as codemode and tool search, to make complete APIs accessible to agents through MCP.

I'll also cover some of the work we are doing with the MCP Typescript SDK to make stateless servers the default.

Speaker info:
- https://github.com/mattzcarey
- https://www.linkedin.com/in/mattzcarey/
- https://x.com/mattzcarey

## What Do Models Still Suck At? - Peter Gostev, Arena.ai, BullshitBench

- Upload date: 2026-04-24
- Video: https://www.youtube.com/watch?v=R7A8rX-09Zw
- Transcript: raw/20260424_R7A8rX-09Zw/R7A8rX-09Zw.en-orig.vtt
- Metadata: raw/20260424_R7A8rX-09Zw/R7A8rX-09Zw.info.json

What type of real world model responses do users still hate? We get to see millions of user's prompts - and we let users 'dislike both' on the Arena. We'll show you trends and examples of the tasks that LLMs still suck at despite the relentless hillclimbing.

Speaker info:
- https://x.com/petergostev
- https://www.linkedin.com/in/peter-gostev/

## Full Walkthrough: Workflow for AI Coding — Matt Pocock

- Upload date: 2026-04-24
- Video: https://www.youtube.com/watch?v=-QFHIoCo-Ko
- Transcript: raw/20260424_-QFHIoCo-Ko/-QFHIoCo-Ko.en-orig.vtt
- Metadata: raw/20260424_-QFHIoCo-Ko/-QFHIoCo-Ko.info.json

Matt will be back on stage at the World's Fair next week! see https://ai.engineer/wf and use YOUTUBEPROMO for new tickets only. Join 6000 AI engineers at the "Superbowl of AI"!

---

A hands-on workshop covering the full lifecycle of AI-assisted development, from turning ambiguous requirements into agent-ready plans to running autonomous coding agents that ship production features.

You'll learn to stress-test vague briefs into structured PRDs, slice work into thin "tracer bullet" vertical slices, and run an AI agent with TDD. You'll watch it select tasks, write tests, implement code, and commit. You'll then refine your prompts based on where it struggles, graduate to fully autonomous (AFK) runs, and learn to design codebases that maximize agent effectiveness.

You'll walk away knowing how to:

- Turn ambiguous requirements into agent-ready issues
- Slice work into vertical tracer bullets an agent can grab independently
- Run AI agents human-in-the-loop and autonomously with TDD
- Design codebase architectures that AI agents love to work in

For: Engineers ready to move beyond chat-based AI assistance and build a real workflow for shipping features with autonomous coding agents.

Speaker info:
- https://x.com/mattpocockuk
- https://www.linkedin.com/in/mapocock/
- https://youtube.com/@mattpocockuk

Timestamps:
00:00:00 - Introduction
00:00:14 - The Thesis of AI Engineering
00:04:20 - Phase 1: Research & Prototyping
00:12:45 - Phase 2: The Grill Session
00:22:10 - Phase 3: Writing the PRD
00:35:50 - Phase 4: Slicing Work into Issues
00:48:15 - Phase 5: Implementation with AI Agents
01:05:30 - Phase 6: Human-in-the-Loop Review
01:18:45 - Phase 7: Deployment & Monitoring
01:28:10 - Designing Codebases for AI Effectiveness
01:34:06 - Final Takeaways & Summary

## "Software Fundamentals Matter More Than Ever" — Matt Pocock

- Upload date: 2026-04-23
- Video: https://www.youtube.com/watch?v=v4F1gFy-hqg
- Transcript: raw/20260423_v4F1gFy-hqg/v4F1gFy-hqg.en-orig.vtt
- Metadata: raw/20260423_v4F1gFy-hqg/v4F1gFy-hqg.info.json

Matt will be back on stage at the World's Fair next week! see https://ai.engineer/wf and use YOUTUBEPROMO for new tickets only. Join 6000 AI engineers at the "Superbowl of AI"!

---

AI coding tools are overhyped and powerful at the same time. Used well, they're extraordinary. Used badly, they'll bury you in spaghetti code faster than any human team could. The difference isn't the tool. It's the process. After 18 months of teaching developers to build with AI agents, Matt Pocock has watched the same patterns emerge: the devs who succeed aren't the ones who delegate everything or nothing. They're the ones who fall back on engineering fundamentals. In this talk, he shares the iterative process his students use to ship high-quality applications with AI agent swarms, and why the principles that make it work (ubiquitous language, vertical slices, TDD, deep modules) are decades-old ideas that didn't break. They got more important.

Speaker info:
- https://x.com/mattpocockuk
- https://www.linkedin.com/in/mapocock/

## The End of Apps — Kitze, Sizzy.co

- Upload date: 2026-04-23
- Video: https://www.youtube.com/watch?v=4fntwuOoedA
- Transcript: raw/20260423_4fntwuOoedA/4fntwuOoedA.en-orig.vtt
- Metadata: raw/20260423_4fntwuOoedA/4fntwuOoedA.info.json

Speaker info:
- https://x.com/thekitze
- https://www.linkedin.com/in/kitaborovskis/

## Agents need more than a chat - Jacob Lauritzen, CTO Legora

- Upload date: 2026-04-22
- Video: https://www.youtube.com/watch?v=XNtkiQJ49Ps
- Transcript: raw/20260422_XNtkiQJ49Ps/XNtkiQJ49Ps.en-orig.vtt
- Metadata: raw/20260422_XNtkiQJ49Ps/XNtkiQJ49Ps.info.json

Jacob Lauritzen is CTO at Legora, the fastest growing legal tech startup in history.

Speaker info:
- https://www.linkedin.com/in/jacob-lauritzen/
- https://github.com/Jacse

## Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind

- Upload date: 2026-04-21
- Video: https://www.youtube.com/watch?v=xOP1PM8fwnk
- Transcript: raw/20260421_xOP1PM8fwnk/xOP1PM8fwnk.en-orig.vtt
- Metadata: raw/20260421_xOP1PM8fwnk/xOP1PM8fwnk.info.json

https://sander.ai/2025/04/15/latents.html

Speaker info:
- https://sander.ai/
- https://github.com/benanne
- https://www.linkedin.com/in/sanderdieleman
- https://x.com/sedielem

Timestamps
0:00 Introduction
2:55 Data Curation
4:02 Representation
9:39 Modeling: Diffusion Mechanism
20:01 Network Architecture
22:25 Training at Scale
23:33 Sampling & Guidance
28:03 Distillation
30:03 Control Signals

## Taste & Craft: A Conversation with Tuomas Artman, CTO Linear & Gergely Orosz, @pragmaticengineer

- Upload date: 2026-04-21
- Video: https://www.youtube.com/watch?v=wjk0ulMAkbc
- Transcript: raw/20260421_wjk0ulMAkbc/wjk0ulMAkbc.en-orig.vtt
- Metadata: raw/20260421_wjk0ulMAkbc/wjk0ulMAkbc.info.json

Tuomas Artman is Cofounder and CTO of Linear.

- https://x.com/artman
- https://www.linkedin.com/in/tuomasartman/

Timestamps
0:00 Introduction
0:36 The danger of shipping features too quickly with AI
3:52 How Linear approaches feature requests and development
6:43 Thoughts on Anthropic's Claude Code
7:59 The challenge of measuring software quality
11:57 Quality Wednesdays at Linear
16:24 The zero bug policy explained
19:44 AI agents and the lack of human "taste" in design
22:21 Building a culture of product-focused engineering
26:23 The future role of software engineers as "product engineers"
27:56 Closing advice for aspiring product engineers

## How AI is changing Software Engineering: A Conversation with Gergely Orosz, @pragmaticengineer

- Upload date: 2026-04-21
- Video: https://www.youtube.com/watch?v=CS5Cmz5FssI
- Transcript: raw/20260421_CS5Cmz5FssI/CS5Cmz5FssI.en-orig.vtt
- Metadata: raw/20260421_CS5Cmz5FssI/CS5Cmz5FssI.info.json

Gergely Orosz is a formar Uber and Skyscanner engineer and is the author of https://www.engguidebook.com/ and https://www.pragmaticengineer.com/ , the #1 software/AI engineering newsletter on Substack, built from scratch in Amsterdam but read by millions around the world.

Speaker info:
- https://x.com/GergelyOrosz
- https://nl.linkedin.com/company/the-pragmatic-engineer

Timestamps:
0:00 What is token maxing?
5:27 Is AI-driven productivity worth the hype?
12:42 How the role of the software engineer is changing
14:45 Are engineers now engineering managers for AI?
17:31 Large tech infrastructure and internal AI tooling
20:41 Why companies like Shopify invest heavily in AI churn
22:56 Growing The Pragmatic Engineer and finding product-market fit

## Full Workshop: Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi

- Upload date: 2026-04-20
- Video: https://www.youtube.com/watch?v=mYSRn6PC1mc
- Transcript: raw/20260420_mYSRn6PC1mc/mYSRn6PC1mc.en-orig.vtt
- Metadata: raw/20260420_mYSRn6PC1mc/mYSRn6PC1mc.info.json

Deep research is one of the best ways to learn how to build real AI systems because it forces you to combine reasoning, planning, autonomy, tools, grounding, and feedback loops in a single end-to-end workflow. In this hands-on workshop, you will build an MCP-powered deep research agent that can plan a research strategy, search the web, analyze YouTube videos, gather grounded evidence, filter for relevance and trustworthiness, and synthesize its findings into a cited research artifact. Rather than treating research as just another chatbot interaction, we will frame it as a goal-directed research loop: one that can search, inspect, pivot, and progressively refine its understanding of a topic.

From there, we will connect that research artifact to a lightweight technical writing workflow that turns raw findings into polished, non-sloppy technical multimodal content. This second part of the system is deliberately more constrained: you will see how research and writing require much different architectures, why exploratory work benefits from agentic behavior, and why writing quality often improves with tighter workflows, review loops, and explicit guidance. Along the way, we will show how to choose between prompts, workflows, and agents depending on the task, and how to keep the overall system practical rather than over-engineered.

We will also cover observability and evaluation so the system is not only impressive in a demo, but measurable and improvable in practice. Most importantly, the workshop is grounded in experience: it distills what we learned over the past year building and using this research-and-writing pipeline internally. Attendees will leave with their own deep research agent, connecting it to a reliable technical writing workflow, and understanding the engineering tradeoffs behind both.

Speaker info:
- https://x.com/Whats_AI
- https://www.linkedin.com/in/pauliusztin
- https://www.linkedin.com/in/samridhivaid/

Timestamps
(00:00) Introduction and problem space (LinkedIn content and AI slop)
(03:39) Workshop overview and goals
(05:01) Speaker introductions
(06:09) AI engineering problem space and constraints
(30:14) Tech stack and tools (Scraping, Gemini grounding, YouTube/GitHub processing)
(33:32) MCP-based research agent architecture overview
(34:46) Deep research agent design and tools
(40:01) Code walkthrough: MCP server setup and tool registration
(43:35) Deep research tool implementation and prompting
(45:06) Analyze YouTube video tool implementation
(47:39) Compile research tool implementation
(53:35) Live demo: Running the research agent
(59:56) Agent skills and workflow prompting
(1:10:35) Introduction to technical writing workflow
(1:15:46) Writing guidelines and control techniques
(1:19:06) Few-shot prompting for writing
(1:21:28) Evaluator-optimizer pattern (Writer/Reviewer)
(1:28:16) Running the writing post skill
(1:34:46) Observability and tracing with Opik
(1:41:44) LLM Judge implementation and evaluation
(1:47:56) Dataset management and F1 score computation

## Running LLMs on your iPhone: 40 tok/s Gemma 4 with MLX — Adrien Grondin, Locally AI

- Upload date: 2026-04-20
- Video: https://www.youtube.com/watch?v=a2muGkT4WD4
- Transcript: raw/20260420_a2muGkT4WD4/a2muGkT4WD4.en-orig.vtt
- Metadata: raw/20260420_a2muGkT4WD4/a2muGkT4WD4.info.json

See more: https://x.com/adrgrondin/status/2040512861953270226

Speaker info:
- https://x.com/adrgrondin

## Gemma, DeepMind's Family of Open Models — Omar Sanseviero, Google DeepMind

- Upload date: 2026-04-20
- Video: https://www.youtube.com/watch?v=_gVFUEdhCyI
- Transcript: raw/20260420__gVFUEdhCyI/_gVFUEdhCyI.en-orig.vtt
- Metadata: raw/20260420__gVFUEdhCyI/_gVFUEdhCyI.info.json

Google DeepMind’s Gemma family is expanding. Join us for a deep dive into the latest models of the Gemma ecosystem. From vibe fine-tuning to Sovereign AI, you'll learn about the latest model capabilities, how to build high-performance applications, and how to get started with open models.

Speaker info:
- https://x.com/osanseviero
- https://www.linkedin.com/in/omarsanseviero/
- https://github.com/osanseviero

Timestamps
0:00 Introduction to the Gemma model family
0:41 Evolution from Gemma 3 to Gemma 4
1:21 Overview of the new Gemma 4 capabilities
2:31 Live demonstrations of on-device applications
3:38 LM Arena scores and performance benchmarks
5:07 Apache 2 license transition
5:27 Technical deep dive: The E2B architecture and per-layer embeddings
6:57 Multimodal understanding and multilingual support
8:43 Ecosystem growth and community adoption
10:07 Product integrations, including Android Studio
10:46 Statistics on model downloads and fine-tuning
11:27 Official Gemma variants: Shield Gemma and MedGemma
12:16 Community research and sovereign AI efforts
12:56 Real-world applications, from cancer therapy to offline tasks
14:05 Closing remarks and future outlook

## The New Application Layer - Malte Ubl, CTO Vercel

- Upload date: 2026-04-20
- Video: https://www.youtube.com/watch?v=XKup1pj-34M
- Transcript: raw/20260420_XKup1pj-34M/XKup1pj-34M.en-orig.vtt
- Metadata: raw/20260420_XKup1pj-34M/XKup1pj-34M.info.json

AI engineering is the legitimate successor to web development and the mainstream discipline that will define the next decade. Drawing on Vercel's own experience, Malte explores what it means to build infrastructure and applications in a world where agents are both the builders and users of software. In a future where the major AI labs commoditize, the real value will sit with the engineers building on top. The application layer is where the innovation happens, and AI engineers are the ones who will shape it.

Speaker info:
- https://x.com/cramforce
- https://www.linkedin.com/in/malteubl/

## The Future of MCP — David Soria Parra, Anthropic

- Upload date: 2026-04-19
- Video: https://www.youtube.com/watch?v=v3Fr2JR47KA
- Transcript: raw/20260419_v3Fr2JR47KA/v3Fr2JR47KA.en-orig.vtt
- Metadata: raw/20260419_v3Fr2JR47KA/v3Fr2JR47KA.info.json

In this Keynote, I will lay out what I believe will be true for agents in 2026 and how MCP plays a part in this. Let's take a look what connectivity for agents might look like.

Speaker info:
- https://x.com/dsp_
- https://www.linkedin.com/in/david-soria-parra-4a78b3a/
- https://github.com/dsp

Timestamps
0:00 Introduction and the vision for MCP applications
1:34 Looking back at the evolution of the MCP ecosystem over the last 18 months
2:30 Ecosystem growth and adoption milestones
3:46 Moving from exploration in 2025 to production in 2026
5:07 The 2026 connectivity stack: Skills, MCP, and CLI/Computer use
7:47 Improving client harnesses: Progressive Discovery
9:39 Programmatic tool calling and agent orchestration
12:00 Best practices for designing agents and server authors
13:42 Future roadmap for the MCP protocol and core improvements
15:23 Strategic integrations and enterprise features
16:32 Upcoming extension mechanisms and skills over MCP
17:15 Conclusion and call for community feedback

## Code Mode: Let the Code do the Talking - Sunil Pai, Cloudflare

- Upload date: 2026-04-19
- Video: https://www.youtube.com/watch?v=8txf05vVVl4
- Transcript: raw/20260419_8txf05vVVl4/8txf05vVVl4.en-orig.vtt
- Metadata: raw/20260419_8txf05vVVl4/8txf05vVVl4.info.json

Sunil Pai from Cloudflare discusses "Code Mode," an approach to interacting with AI agents where the model generates executable code (such as JavaScript) instead of relying on traditional JSON-based tool calling. This shift allows for more efficient, stateful, and complex system interactions.

Speaker info:
Sunil Pai created Partykit, the open source tool for real-time multi-player apps. For his day job, he builds AI Agents at Cloudflare.
- https://sunilpai.dev/
- blog.cloudflare.com/author/sunil/
- linkedin.com/in/sunil-pai-a47732253/

Timestamps
0:00 Introduction and speaker background
1:16 What is "Code Mode"?
1:31 Limitations of traditional tool calling at scale
2:03 The shift to generating executable code
3:01 Scaling API usage at Cloudflare
4:05 Why code generation is more efficient
5:28 Live demonstration of the Mythical server
7:20 A new way of interacting with systems
9:09 Example: The Kenton canvas and tic-tac-toe anecdote
11:46 New software architecture: The "Harness"
13:28 Observability and security in sandboxed environments
14:15 Long-running workflows and generative UI
16:41 Future outlook: Building for the next generation of users
17:50 The resurgence of capability-based security
18:33 Conclusion and final thoughts

## How Google DeepMind is researching the next Frontier of AI for Gemini — Raia Hadsell, VP of Research

- Upload date: 2026-04-18
- Video: https://www.youtube.com/watch?v=zZsTVBXcbow
- Transcript: raw/20260418_zZsTVBXcbow/zZsTVBXcbow.en-orig.vtt
- Metadata: raw/20260418_zZsTVBXcbow/zZsTVBXcbow.info.json

In this presentation, Raia Hadsell, VP of Research at Google DeepMind and AI Ambassador for the United Kingdom, opens AIE Europe and explores what's open in Frontier AI and the future of intelligence by focusing on advancements beyond standard large language models. She categorizes these innovations into three key areas:

00:00 Introduction
05:05 Advanced Embedding Models: Raia discusses the importance of embedding models for fast retrieval and recognition, similar to how the human brain uses 'Jennifer Aniston cells' to identify concepts across modalities. She highlights Gemini Embeddings 2, a fully omnimodal model that processes text, video, and audio into unified semantic vectors.
09:53 AI for Weather Forecasting: The team has developed revolutionary models for atmospheric prediction, moving away from traditional physics simulations. Notable breakthroughs include:
11:00 GraphCast: A spherical graph neural network that provides accurate 15-day weather forecasts.
12:47 GenCast: A probabilistic model that offers higher efficiency and accuracy (97% of the time compared to gold-standard benchmarks).
13:51 FGN: A functional generative network that directly predicts cyclone behavior, which is currently being utilized by the US National Hurricane Center.
14:35 World Models: Hadsell introduces Genie, a project focused on creating interactive, real-time environments. Starting from Genie 1 (2D platformers) and progressing to Genie 3, these models allow users to create and interact with high-quality, 3D photorealistic worlds. These environments demonstrate capabilities like memory, consistency, and the ability to be dynamically prompted by the user to change the surroundings in real-time.

Speaker info:
- https://uk.linkedin.com/in/raia-hadsell-35400266
- https://github.com/raiah

## The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil

- Upload date: 2026-04-18
- Video: https://www.youtube.com/watch?v=_Zcw_sVF6hU
- Transcript: raw/20260418__Zcw_sVF6hU/_Zcw_sVF6hU.en-orig.vtt
- Metadata: raw/20260418__Zcw_sVF6hU/_Zcw_sVF6hU.info.json

In this talk, Armin Ronacher (creator of Flask) and Cristina Poncela Cubeiro explore the paradox of using AI coding agents: while these tools promise to "ship without friction," excessive speed often leads to technical debt, security issues, and brittle systems. They argue that friction is actually a necessary component of high-quality software engineering because it forces human judgment and critical thinking.

Timestamps and Takeaways:
00:00 The Problem
03:35 The Psychological Trap: Because AI tools are addictive and make coding feel effortless, engineers often stop taking the time to design, review, and truly understand the code being generated.
07:15 - The Engineering Challenge: Agents are optimized for producing code that runs, not code that is maintainable or architecturally sound. This often results in "slop"—code that creates unexpected failure conditions and entropy
10:55 - Agent-Legible Codebases: To maximize AI effectiveness, the speakers suggest designing codebases as infrastructure. This includes:
Modularization of both code components and the code flow itself
12:35 - Mechanical Enforcement through strict linting (e.g., no bare catch-alls, unique function names, and avoiding hidden magic like dynamic imports) 
14:27 - Reintroducing Friction: The speakers advocate for slowing down. They recommend identifying specific, high-stakes areas (such as database migrations or permission changes) where human judgment is non-negotiable and must be intentionally re-inserted into the development process
17:25 - Conclusion

Armin and Cristina conclude that rather than trying to eliminate all friction, engineers should embrace it as the mechanism that allows for steering and quality control, ensuring that human experience remains at the center of the development lifecycle.

Speaker info:
- https://x.com/mitsuhiko
- https://www.linkedin.com/in/arminronacher/
- https://github.com/mitsuhiko
- https://www.linkedin.com/in/cristinaponcela/

## State of the Claw — Peter Steinberger

- Upload date: 2026-04-17
- Video: https://www.youtube.com/watch?v=zgNvts_2TUE
- Transcript: raw/20260417_zgNvts_2TUE/zgNvts_2TUE.en-orig.vtt
- Metadata: raw/20260417_zgNvts_2TUE/zgNvts_2TUE.info.json

Peter Steinberger gives the 5 month update on OpenClaw, the fastest growing open source project in history, and what it's like as a maintainer, from security to community. Keynote followed by audience Q&A moderated by @swyx.

Speaker info:
- https://x.com/steipete
- https://www.linkedin.com/in/steipete/
- https://openclaw.ai/


Timestamps
0:00 Project Growth and Statistics
2:23 Management Challenges and the OpenClaw Foundation
3:47 Addressing Security Advisories and Vulnerabilities
10:33 Misinformation and Media Fearmongering
14:50 The Burden of Open Source Maintenance
16:12 OpenAI Involvement and Future Independence
18:57 Audience Q&A Begins
19:53 OpenClaw's Relationship with OpenAI
22:28 The Importance of Open and Local Models
24:57 Coding Workflow and Agent Interactions
28:28 Defining 'Taste' in AI Development
30:31 Developing Personality for AI Agents
33:22 Future Vision: Ubiquitous Agents and Smart Homes
35:58 Addressing Prompt Injection Risks
38:33 Future Vision: Implementing 'Dreaming' and Modularity
40:24 Life as a Maintainer and Future Skills

## Harness Engineering: How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI

- Upload date: 2026-04-17
- Video: https://www.youtube.com/watch?v=am_oeAoUhew
- Transcript: raw/20260417_am_oeAoUhew/am_oeAoUhew.en-orig.vtt
- Metadata: raw/20260417_am_oeAoUhew/am_oeAoUhew.info.json

https://openai.com/index/harness-engineering/

Speaker info:
- https://x.com/_lopopolo
- https://www.linkedin.com/in/ryanlopopolo/
- https://github.com/lopopolo

With a special post keynote Q&A with Vibhu Sapra (https://x.com/vibhuuuus), cohost for https://latent.space/p/harness-eng

## $1 AI Guardrails: The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero

- Upload date: 2026-04-16
- Video: https://www.youtube.com/watch?v=YZHPEkfy2kc
- Transcript: raw/20260416_YZHPEkfy2kc/YZHPEkfy2kc.en-orig.vtt
- Metadata: raw/20260416_YZHPEkfy2kc/YZHPEkfy2kc.info.json

LLM-based attacks are no longer the exception, they are the baseline. This talk maps the six most common attack vectors found in production AI systems: Prompt and Context Injection, Model Internals, RAG Poisoning, MCP Exploits, and Agentic Escalation. From there, it dives into the architecture of ModernBERT and shows how to fine-tune it into a lightweight, self-hosted guardrails layer for under a dollar.

What you will learn:

- The Zero Trust Gap in LLMs: what these attack vectors share in common, and why model alignment and human review alone are not enough
- The secret sauce that makes encoder models beat LLM-as-a-Judge in latency and flexibility
- ModernBERT under the hood: a deep dive into Alternating Attention, Unpadding & Sequence Packing, RoPE, and FlashAttention
- Building your own safety layer: a practical walkthrough of fine-tuning ModernBERT as a safety discriminator
- Live Demo: real attack prompts from each vector tested against our model"

Speaker info:
- Diego Carpentero -  AI Engineer | Tech Entrepreneur | Open Source Contributor | NVIDIA Certified Professional (NCP-GENL)

Timestamps:
00:00 Intro

## Building pi in a World of Slop — Mario Zechner

- Upload date: 2026-04-16
- Video: https://www.youtube.com/watch?v=RjfbvDXpFls
- Transcript: raw/20260416_RjfbvDXpFls/RjfbvDXpFls.en-orig.vtt
- Metadata: raw/20260416_RjfbvDXpFls/RjfbvDXpFls.info.json

All I wanted was a shitty coding agent that is truly mine. And I’d have loved to just tell you why and how I built pi. But then Peter decided to make it the agentic core of OpenClaw. And now pi is collateral. So yes, this is a talk about pi. But it is also a talk about how agents are destroying OSS, how I deal with that, and a plea to slow the fuck down.

https://x.com/badlogicgames
https://github.com/badlogic
https://www.linkedin.com/in/mariozechner/

Timestamps
0:00 – Intro and motivation for building pi
0:29 – Act 1: Building pi and the frustration with existing agent harnesses
1:56 – Why current context management in tools like Cloud Code and Open Code fails
4:44 – The importance of minimal harnesses and the "Terminal" benchmark
5:35 – Introducing pi: A self-modifying, extensible agent core
7:27 – The "YOLO" security philosophy and extensibility through TypeScript
9:03 – Examples of pi extensions (chat rooms, NES, Doom)
10:46 – Act 2: OSS in the age of "clankers" and how to fight them
12:03 – Act 3: A plea to slow down and stop the "slop" in software development
13:58 – How agents create "enterprise-grade complexity" and why humans are still the bottleneck
16:12 – Practical advice: How to effectively integrate agents into your workflow

## Paperclip: Open Source Human Control Plane for AI Labor — Dotta Bippa

- Upload date: 2026-04-15
- Video: https://www.youtube.com/watch?v=h403btjldDQ
- Transcript: raw/20260415_h403btjldDQ/h403btjldDQ.en-orig.vtt
- Metadata: raw/20260415_h403btjldDQ/h403btjldDQ.info.json

Curator note: Dotta is anonymous, so we asked him to submit with just an avatar. He did amazing!

Paperclip enables open source orchestration for zero-human companies. With Paperclip you can manage hundreds of ai-agent employees to run your business, even if you're not technical. In this talk we walk through how to setup paperclip, how to grow an ai organization, how to leverage skills and instructions for the best ai agents, and how you can start a zero human company.

Speaker info:
https://x.com/dotta
https://paperclip.ing

Timestamps:

00:00 - Introduces Paperclip
00:56 - Organizational Control
1:17 - Getting Started
04:42 - Skill Management
09:01 - Reliable Workflows
11:10 - Routine Automation
17:51 - Agentic Flexibility
21:39 - Future Roadmap

## Running LLMs locally: Practical LLM Performance on DGX Spark — Mozhgan Kabiri chimeh, NVIDIA

- Upload date: 2026-04-10
- Video: https://www.youtube.com/watch?v=c5-kx2bwoCk
- Transcript: raw/20260410_c5-kx2bwoCk/c5-kx2bwoCk.en-orig.vtt
- Metadata: raw/20260410_c5-kx2bwoCk/c5-kx2bwoCk.info.json

Moving LLM workloads from the cloud to local infrastructure requires a shift in engineering strategy. In this talk, I share my journey of serving and benchmarking open-source models (1.5B to 14B) on an NVIDIA DGX Spark workstation. Using a reproducible methodology with vLLM, I analyze real-world trade-offs in throughput, latency, and the benefits of the 128GB Grace Blackwell unified memory architecture. You will leave with a clear framework for local model sizing, an understanding of quantization performance like NVFP4, and a guide for when local compute is the right choice for your AI stack.

Speaker info:
- LinkedIn https://www.linkedin.com/in/mozhgankch/

## AI Didn’t Kill the Web, It Moved in! — Olivier Leplus (AWS) & Yohan Lasorsa (Microsoft)

- Upload date: 2026-04-10
- Video: https://www.youtube.com/watch?v=XZ0boOjtbNo
- Transcript: raw/20260410_XZ0boOjtbNo/XZ0boOjtbNo.en-orig.vtt
- Metadata: raw/20260410_XZ0boOjtbNo/XZ0boOjtbNo.info.json

In 2026, AI didn't replace the web. It became part of it. Your browser now ships a built-in MCP server. Chrome DevTools debug your app with AI. Native Web APIs let you summarize, translate, and prompt right from your frontend code. Meanwhile, the web feeds agents right back through standards like LLMs.txt and MCP tools that make sure models always have the right documentation. AI builds the web. The web feeds AI. And now, AI lives inside the browser itself. In this talk, we'll follow a feature from idea to production and demo this new symbiosis in action: coding agents, AI-powered debugging in Chrome devtools, Web AI APIs, WebMCP, and more. Because your next website won't just be built with AI. It will be built for humans and AI agents alike. AI isn't just for Python folks. The web is AI's new home.

## Judge the Judge: Building LLM Evaluators That Actually Work with GEPA — Mahmoud Mabrouk, Agenta AI

- Upload date: 2026-04-10
- Video: https://www.youtube.com/watch?v=X4dEHRzBLmc
- Transcript: raw/20260410_X4dEHRzBLmc/X4dEHRzBLmc.en-orig.vtt
- Metadata: raw/20260410_X4dEHRzBLmc/X4dEHRzBLmc.info.json

Miscalibrated evals are worse than no evals. They give false confidence while being, at best, useless. This workshop walks you through building a calibrated LLM-as-a-judge, from capturing ground truth to optimizing with GEPA and assessing the judge. You will leave with an LLM-as-a-judge you can trust to actually improve your app.

Mahmoud Mabrouk - Co-founder and CEO, Agenta AI

Mahmoud Mabrouk is the cofounder and CEO of Agenta, an open-source LLMOps platform for building and evaluating LLM applications. He has spent the past 15 years working in machine learning and holds a PhD in applied machine learning for computational biology.

Resources:
- Workshop repo: https://github.com/Agenta-AI/judge-the-judge-talk-2026
- GEPA repository: https://github.com/gepa-ai/gepa
- GEPA paper: https://arxiv.org/abs/2507.19457
- Hamel’s guide for error analysis: https://hamel.dev/blog/posts/field-guide/

Socials:
https://x.com/mmabrouk_
https://www.linkedin.com/in/mmabrouk2/
https://agenta.ai
https://github.com/agenta-ai/agenta

## One Registry to Rule them All - Sonny Merla, Mauro Luchetti, & Mattia Redaelli, Quantyca

- Upload date: 2026-04-10
- Video: https://www.youtube.com/watch?v=VXfRt_H-V08
- Transcript: raw/20260410_VXfRt_H-V08/VXfRt_H-V08.en-orig.vtt
- Metadata: raw/20260410_VXfRt_H-V08/VXfRt_H-V08.info.json

As internal MCP servers and A2A agents explode in number, discovery and governance become critical challenges for production-grade AI systems. We'll demonstrate how we built an enterprise infrastructure to index MCP servers and A2A agents, and link them to relevant use cases. We'll show how moving from a fragmented environment to a searchable, metadata-rich registry transformed a chaotic development cycle into a standardized, scalable deployment process.
 
In this talk, we'll cover:
- How we developed an internal private company MCP registry based on the open source specification
- How we defined an A2A registry based on agent cards
- How we achieved agent runtime discovery using an MCP server that exposes company A2A agents
- How we linked A2A agent and MCP server template repositories to DevOps processes

Mauro Luchetti - AI CoE Manager, Quantyca

I work as an AI Engineer and CoE Manager at Quantyca, where I focus on artificial intelligence solutions, data engineering, and cloud architectures, drawing on nearly 8 years of professional experience in the field. Over the years I've had the opportunity to work on projects involving generative AI, machine learning, data governance and data management, trying to combine hands-on technical skills with a broader strategic perspective. I enjoy sharing what I've learned with the teams I work with, contributing to collective growth in modern AI engineering practices.

Socials:
https://www.quantyca.it/

Slides:
https://quantyca-my.sharepoint.com/:b:/g/personal/mauro_luchetti_quantyca_it/IQBUCcMBzsAfSZtJXrCdaqV0AaUyDhifxP360fqCUupyaGc?e=S6ytoA

## Cognitive Exhaust Fumes, or: Read-Only AI Is Underrated — Šimon Podhajský, Head of AI, Waypoint

- Upload date: 2026-04-08
- Video: https://www.youtube.com/watch?v=u0TOSBbAw7c
- Transcript: raw/20260408_u0TOSBbAw7c/u0TOSBbAw7c.en-orig.vtt
- Metadata: raw/20260408_u0TOSBbAw7c/u0TOSBbAw7c.info.json

Every other personal AI demo has agents sending emails and managing calendars. I built the opposite: a read-only system that queries my data sources (email, journal, tasks, CRM, browser sessions, notes) but can't modify any of them. This is an intentional limitation. I'll cover why trust asymmetry matters (read is safe, write is dangerous), how cross-source pattern detection beats task automation, and why ""exhaust fume analysis"" of one's cognition is more valuable than yet another AI assistant trying to act on your behalf.

Šimon Podhajský - Head of AI, Waypoint AI

I'm Head of AI at Waypoint and a full-stack builder with a background in data science and data engineering. I built this personal AI system to scratch my own itch -- and discovered that the ""read-only"" constraint led to better architecture than the agent-first approaches I see everywhere.

I made a Github repo with a template for people to try out the read-only AI / personal intelligence system: https://github.com/shippy/personal-intelligence-kit 

Socials:
https://linkedin.com/in/simonpodhajsky
https://x.com/sim_pod
https://simon.podhajsky.net

Slides:
https://slides.podhajsky.net/read-only-ai

## Platforms for Humans and Machines: Engineering for the Age of Agents — Juan Herreros Elorza

- Upload date: 2026-04-08
- Video: https://www.youtube.com/watch?v=cCRO3ChaYhM
- Transcript: raw/20260408_cCRO3ChaYhM/cCRO3ChaYhM.en-orig.vtt
- Metadata: raw/20260408_cCRO3ChaYhM/cCRO3ChaYhM.info.json

As AI coding agents become first-class users of internal developer platforms, the practices that make platforms accessible to humans turn out to be the same ones that enable AI to thrive.

Self-service interfaces, well-defined APIs with schemas and documentation, local-first workflows, and rich observability have always been important elements of a good platform. Now they are prerequisites for agents that can autonomously build, debug, and ship software.

This talk explores what it means to design platforms where both humans and AI can collaborate effectively. We'll cover:

- How to expose your platform as a product with structured APIs (and perhaps MCPs)
- Why prioritizing local tooling pays dividends when agents need to iterate on errors
- How observability becomes the bridge between runtime behavior and AI understanding

We'll also discuss the flip side: AI is making it easier than ever to *contribute* to platform code, but that comes with new responsibilities around quality gates, context files like CLAUDE.md, and maintainability.

Walk away with concrete practices to ensure your platform is ready for a future where agents are not just tools, but users of it.

Juan Herreros Elorza - Team Lead, Banking Circle

I'm Juan, a Platform Engineering enthusiast.

I am working for Banking Circle, as the Team Lead in our Cloud Native Technology team.

When I'm not working, I'm most likely rehearsing or performing improv comedy.

Socials:
https://juanherreros.com/
https://linkedin.com/in/juan-herreros-elorza
https://github.com/jherreros

Slides:
https://speakerdeck.com/jherreros/platforms-for-humans-and-machines-engineering-for-the-age-of-agents

## Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz

- Upload date: 2026-04-08
- Video: https://www.youtube.com/watch?v=U00AOI1eJUE
- Transcript: raw/20260408_U00AOI1eJUE/U00AOI1eJUE.en-orig.vtt
- Metadata: raw/20260408_U00AOI1eJUE/U00AOI1eJUE.info.json

Public MCP servers often look ready-to-use, until the reality of production hits. You might find your agents ignoring perfectly good tools, unwanted side-effects exhausting your container's disk space, or worse, security concerns like multi-tenant leaks wreaking havoc. What begins as a ""simple integration"" can quickly become a source of friction and unexpected failure.

In this talk, we'll share a hands-on guide to adapting third-party MCP servers for real-world applications. You'll learn practical processes to identify friction points and strategies to modify MCP servers so they integrate seamlessly with your specific agents and architecture. Real-world lessons, trade-offs, and production-tested solutions included.

Using a concrete example, we'll walk through the journey of transforming a brittle setup into production-ready infrastructure. We'll cover editing tool definitions, optimizing agentic context, and layering deterministic validations—all while preparing for scale. This iterative debugging process will provide you with a repeatable framework to make any MCP integration resilient, secure, and production-ready.

Nimrod Hauser - Founding Software Engineer, Baz

Nimrod is a Principal Engineer at Baz, building AI-powered code review agents. A “jack of all trades” across backend, data engineering, and data science, he has worked at the intersection of software and data throughout his career. He began as a data analyst in the military, helped lay the foundations of Salesforce’s Einstein platform, and later became the first data scientist at cybersecurity startup BlueVoyant. He went on to lead data and architecture at Solidus Labs in the crypto-regulation space before joining Baz. Nimrod thrives on building systems from scratch and turning ideas into scalable products.

Socials:
https://www.linkedin.com/in/nimrod-hauser-03776a31/
https://x.com/NimrodHauser

Slides:
https://prezi.com/view/TSBwBXLNcXzzWrLbRiit/?referral_token=4jzLrblnB3FN

## Contact Center Voice AI: Low-Latency Intelligence Extraction from Messy Audio Streams — Dippu Singh

- Upload date: 2026-04-08
- Video: https://www.youtube.com/watch?v=IEF842ZEU5A
- Transcript: raw/20260408_IEF842ZEU5A/IEF842ZEU5A.en-orig.vtt
- Metadata: raw/20260408_IEF842ZEU5A/IEF842ZEU5A.info.json

"Processing real-time voice data is an engineering minefield of latency, accents, and interruptions. This session explores the architecture of a Real-Time Voice Intelligence Pipeline deployed in a high-volume contact center.
We will move beyond simple transcription to discuss Structured Intent Extraction. I will show you how to design:

1. Voice Capture Pipeline: The entry point for clean, multi-channel data acquisition.
2. Speech-To-Text(STT) Engine: Converting speech to accurate text.
3. Generative AI Core Structure: Using rigorous system prompts to force the LLM to separate ""Customer Intent"" from ""Operator Chit-Chat"" and output valid JSON, even from garbled transcripts.
4. Customer Data Sync: Translating AI insights into enterprise system actions.

We reduced post-call work by 50% by shifting compute from ""batch"" to ""stream.""

Speaker: Dippu Kumar Singh - Leader Of Emerging Technologies (Apps), Fujitsu North America Inc.

Dippu Kumar Singh has over 16 years of experience at the intersection of industry innovation and advanced research. He is a recognized authority in building scalable, trustworthy, and commercially viable AI systems. Being a Leader for Emerging Data & Analytics at Fujitsu North America, Dippu specializes in bridging the gap between theoretical AI concepts and enterprise-grade implementation. His strategic leadership has spearheaded multi-million in sales pipelines and delivered remarkable savings through AI-driven optimizations in transportation, manufacturing, utilities, and supply chain logistics.

Socials:
https://www.linkedin.com/in/dippukumarsingh/

Slides:
https://docs.google.com/presentation/d/1f2y1s64irhdDNTRgK6bWrBtOgMWlhQYM/edit?usp=sharing&ouid=107532212133041789455&rtpof=true&sd=true"

## Your Insecure MCP Server Won't Survive Production — Tun Shwe, Lenses

- Upload date: 2026-04-08
- Video: https://www.youtube.com/watch?v=BurJvbqFr4c
- Transcript: raw/20260408_BurJvbqFr4c/BurJvbqFr4c.en-orig.vtt
- Metadata: raw/20260408_BurJvbqFr4c/BurJvbqFr4c.info.json

Tun Shwe and Jeremy Frenay from Lenses.io address the critical security and design challenges involved in moving Model Context Protocol (MCP) servers from local development to enterprise production. Effective agentic design is inseparable from security and here we propose five core principles such as shrinking the attack surface, constraining inputs and returning only essential data. Standard local setups fail under professional workloads, necessitating a shift to remote MCP servers and robust authentication frameworks. Detailed technical flows are provided for OAuth 2.1, comparing Dynamic Client Registration (DCR) with the more advanced Client ID Metadata Document (CIMD) approach for managing agent identities. Come learn how to adopt the correct mindset for building enterprise-grade agentic AI systems with MCP.

https://github.com/lensesio/lenses-mcp

https://lenses.io/

Tun Shwe - Staff AI Engineer, Lenses.io

Tun is a Staff AI Engineer at Lenses.io, where he leads AI strategy. He is focused on helping companies imagine and implement their strategic vision with agentic AI systems fuelled with real-time context. He was previously a Head of Data and Data Engineer at high growth startups and has spent 20 years building data-intensive applications and leading T-shaped teams. In his spare time, Tun goes surfing, plays guitar and tends to his analogue cameras.

--

Jeremy Frenay is an AI Engineer at Lenses.io, where he works on bringing AI-assisted engineering to the Apache Kafka ecosystem. Previously, Jeremy co-founded Arcane, an AI copilot for marketers, and led data operations engineering at Babylon Health, scaling data platforms for one of the world's largest healthtech unicorns.

Socials:
https://lenses.io/
https://github.com/lensesio/lenses-mcp
https://www.linkedin.com/in/tunshwe/
https://www.linkedin.com/in/jeremy-frenay/

Slides:
https://drive.google.com/file/d/1zLzkVO7_kBoV6bI7lhYIi3AxUH6j7xH_/view?usp=sharing

## Why, and how you need to sandbox AI-Generated Code? — Harshil Agrawal, Cloudflare

- Upload date: 2026-04-08
- Video: https://www.youtube.com/watch?v=AHtGAgQ0Q_Q
- Transcript: raw/20260408_AHtGAgQ0Q_Q/AHtGAgQ0Q_Q.en-orig.vtt
- Metadata: raw/20260408_AHtGAgQ0Q_Q/AHtGAgQ0Q_Q.info.json

We are using AI to write code. Moreover, we are using it to be more productive. However, giving AI access to our machine and let them run on their own is dangerous. Imagine, giving AI access to the server where you run your application! You want your users to interact with your application through a chat interface, and maybe build their own apps or customize the UI. If not supervised carefully, AI can break your application or worse leak private data.

So how do you run AI generated code within your application and allow users to build their own apps?
In this talk, we'll go beyond the hype and dive into the practical architecture of sandboxing AI generated code. You'll learn how to integrate an LLM to generate code and, how to run that code in a secure isolated environment.

Harshil Agrawal - Sr. Developer Educator, Cloudflare

Working in the Developer Relations team at Cloudflare, Harshil enjoys sharing his learnings with the community. A JavaScript developer, open-source contributor, and a low-code enthusiast, Harshil loves experimenting with tech and building small projects.

Socials:
https://x.com/harshil1712
https://linkedin.com/in/harshil1712
https://harshil.dev

Slides:
https://harshil.dev/slides/sandbox-ai-engineer

## Let LLMs Wander: Engineering RL Environments — Stefano Fiorucci

- Upload date: 2026-04-08
- Video: https://www.youtube.com/watch?v=71V3fTaUp2Q
- Transcript: raw/20260408_71V3fTaUp2Q/71V3fTaUp2Q.en-orig.vtt
- Metadata: raw/20260408_71V3fTaUp2Q/71V3fTaUp2Q.info.json

Reasoning models like DeepSeek R1 have demonstrated that learning from interaction is just as critical as learning from examples. To build these capabilities ourselves, we need to move beyond static datasets and start building Reinforcement Learning Environments: little worlds where models can act, get rewards, and learn.

In this talk, I will walk you through my journey exploring this space from a practical software engineering perspective.

We will cover:
- How classic Reinforcement Learning concepts translate to Language Models
- Verifiers, an open-source library to build Environments as software artifacts
- Concrete examples of environments, from single-turn tasks to multi-turn games and tool-using agents
- How to use these environments for both evaluating and training Small Language Models.

Join me to learn how to move from prompting models to building the gyms where they learn.

Stefano Fiorucci - AI/SW Engineer/Explorer, deepset

Stefano is an AI/Software Engineer and explorer.

He currently works on AI Orchestration at Deepset, where he contributes to and maintains Haystack, a widely used open-source framework for building LLM applications.

He loves experimenting with Small Language Models, Post-Training and Reinforcement Learning, and shares his learning through code, writing, and talks.

LLM RL Environments Lil Course: https://github.com/anakin87/llm-rl-environments-lil-course

Socials:
https://twitter.com/theanakin87
https://www.linkedin.com/in/stefano-fiorucci/
https://github.com/anakin87
https://huggingface.co/anakin87

Slides:
https://drive.google.com/file/d/116PKThwtyTxeH1GmZQ7bL3HPYM6KCgHa/view?usp=drive_link

## OpenRAG: An open-source stack for RAG — Phil Nash

- Upload date: 2026-04-08
- Video: https://www.youtube.com/watch?v=4TxOBhDRRCM
- Transcript: raw/20260408_4TxOBhDRRCM/4TxOBhDRRCM.en-orig.vtt
- Metadata: raw/20260408_4TxOBhDRRCM/4TxOBhDRRCM.info.json

There are many variables in building RAG applications, from document parsing to the language model you pick for generation and everything in between. Combining Docling for document parsing, OpenSearch for retrieval, and Langflow for orchestration, plus local and remote models, OpenRAG is an opinionated, agentic, open-source stack for building the RAG application of your dreams.

Just because it has opinions doesn't make it inflexible though. In this talk we'll look at how OpenRAG gives you a great baseline for RAG and how you can tune it and evaluate the outcomes to create RAG applications that work well with your data. You'll learn how to get the best out of your documents with Docling, how OpenSearch provides more than just vector search, and how Langflow makes it easy to customise your pipeline to interact with your data the way you want to. You’ll leave with a playbook of options to improve your RAG app and a stack you can extend without reinventing everything.

Phil Nash - Developer relations engineer, IBM

Phil is a developer relations engineer for DataStax and Google Developer Expert living in Melbourne, Australia. He's been working in developer relations for a decade, speaking at conferences since 2012, and writing JavaScript since before jQuery. Away from the keyboard, Phil enjoys travel, live music, and hanging out with his mini sausage dog, Ruby.

Socials:
https://x.com/philnash
https://linkedin.com/in/philnash
https://philna.sh
https://github.com/philnash

## From Chaos to Choreography: Multi-Agent Orchestration Patterns That Actually Work — Sandipan Bhaumik

- Upload date: 2026-04-08
- Video: https://www.youtube.com/watch?v=2czYyrTzILg
- Transcript: raw/20260408_2czYyrTzILg/2czYyrTzILg.en-orig.vtt
- Metadata: raw/20260408_2czYyrTzILg/2czYyrTzILg.info.json

One AI agent is a feature. Fifty agents is a distributed systems problem nobody's discussing. I've seen this pattern: teams build one agent, then five, then drown in coordination problems unrelated to LLMs. Agent handoffs fail silently. Data goes stale. Decisions become untraceable. Drawing from Databricks production deployments, I'll expose orchestration anti-patterns killing multi-agent systems and show agent handoff protocols that work—state management, data contracts, failure modes. You'll see when to choreograph versus orchestrate and live multi-agent workflow with proper observability. This applies distributed systems engineering to agents: the infrastructure layer everyone needs but nobody's building.

Sandipan Bhaumik - Data & AI Tech Lead, Databricks

Sandipan Bhaumik has spent 18 years building data and AI systems inside environments that can't afford them to fail - NHS, Tier 1 banks, and large enterprises across EMEA. At AWS and now Databricks, he's seen firsthand where multi-agent systems break down between architecture and production. He is a regular speaker on data and AI system architecutr ebest practices, runs a community of AI practitioners, and he's here to talk about what actually holds together when you scale agentic AI systems in production.

Socials:
https://www.linkedin.com/in/sandipanbhaumik

Slides:
https://drive.google.com/file/d/18LqVzhfVS3iULYuy2EshWoMLmQt3rdpT/view?usp=sharing

## Agentic Engineering: Working With AI, Not Just Using It — Brendan O'Leary

- Upload date: 2026-04-07
- Video: https://www.youtube.com/watch?v=BEKc4P87XKo
- Transcript: raw/20260407_BEKc4P87XKo/BEKc4P87XKo.en-orig.vtt
- Metadata: raw/20260407_BEKc4P87XKo/BEKc4P87XKo.info.json

Coding agents are quickly moving from novelty to necessity, but most teams are still stuck between demos that feel magical and systems that break down in real-world engineering environments. In this session, Brendan O’Leary explores what it takes to make coding agents reliable collaborators rather than unpredictable copilots. Drawing from hands-on experience building and scaling AI coding agents, Brendan can unpack where agents succeed, where they fail, and how engineers can design workflows that balance speed with control. Attendees will learn how to think about agent autonomy, context management, and human-in-the-loop design so AI can meaningfully accelerate development without sacrificing code quality, security, or trust. This talk is for engineers ready to move past “vibe coding” and into production-grade agent-driven software development.


Brendan O'Leary - Developer Relations Engineer, Kilo Code

As conversations shift from AI demos to real engineering and coding agents begin moving into production environments, Brendan is passionate about helping teams understand not just what’s possible, but what’s practical. He’s especially energized by audiences who are grappling with the same questions he sees every day: how much autonomy to give agents, how to keep humans meaningfully in the loop, and how to move beyond “vibe coding” into reliable software development.

Brendan is a builder and practitioner at Kilo Code, working hands-on with AI coding agents and the realities of deploying them in serious engineering contexts. He’s mastered the role of choreographer, successfully balancing the collaborative dance between human creativity and machine capability. 

His perspective of coding agents is rooted in lived experience, combining a deep technical understanding with a clear-eyed view of where agents succeed, where they fail, and why trust is the missing layer most tools overlook. Brendan brings a candid, engineer-first approach that resonates with technical audiences and leaves them with concrete ways to rethink how humans and coding agents collaborate in production systems.

Socials:
https://www.linkedin.com/in/olearycrew/
https://boleary.dev/
https://x.com/olearycrew
https://gitlab.com/brendan/boleary-dot-dev
https://kilo.ai/

## How METR measures Long Tasks and Experienced Open Source Dev Productivity - Joel Becker, METR

- Upload date: 2026-01-19
- Video: https://www.youtube.com/watch?v=k1t2xyWMUdY
- Transcript: raw/20260119_k1t2xyWMUdY/k1t2xyWMUdY.en-orig.vtt
- Metadata: raw/20260119_k1t2xyWMUdY/k1t2xyWMUdY.info.json

AI models are crushing benchmarks. SWE-bench scores are climbing, and METR's measured time horizons are rising rapidly. Yet when we deployed these same models in a field study with experienced developers, they didn't speed up work. What's going on? Are benchmarks misleading us about AI capabilities? Are we missing something about how AI performs in the real world? In this talk, we'll reconcile lab and field evidence on AI capabilities. Drawing from METR's time horizon measurements and developer productivity RCT, we'll explore why impressive benchmark performance doesn't always translate to real-world impact. We'll examine potential explanations—from reliability requirements to task distribution to capability elicitation—and discuss what this means for automated AI R&D.

https://x.com/joel_bkr

Timestamps
00:00 The Compute-Time Horizon Argument

01:43 Potential Constraints on AI Scaling (Power & Dollars)

04:23 The Problem of Eclipsing Evaluation Time

06:52 Meta's "J-Curve" of Developer Productivity

09:12 Unreliability of Self-Reported Time Estimates

11:43 Personal Experiences with AI Tools (Cursor) & Learning Curves

14:10 METR Study Deep Dive: Scatter Plots & Variance

16:48 The Controversy of "Conservative" Usage Estimates

21:41 Unpublished Hackathon Results (AI Allowed vs. Disallowed)

25:28 Why AI Struggles with Data Science & Messy Enterprise Data

30:35 Example of AI Failure on Complex Deployment Metrics

38:29 Quantifying Speed-Up: The Methodological Challenges

46:30 Future Metrics: "Watched" vs. "Unwatched" Time Horizons

52:52 Moving Beyond Benchmarks: "In the Wild" Transcripts

56:12 The "Agent Village" & Fuzzy Goal Measurement

58:53 The "Neurodivergent AI" Hypothesis & Interface Mismatch

01:06:31 Software-Only Singularity vs. Hardware Constraints

01:13:53 AI Applications in Chip Fabrication & Yield Improvement

## Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0

- Upload date: 2026-01-14
- Video: https://www.youtube.com/watch?v=VSdV-AdSlis
- Transcript: raw/20260114_VSdV-AdSlis/VSdV-AdSlis.en-orig.vtt
- Metadata: raw/20260114_VSdV-AdSlis/VSdV-AdSlis.info.json

Implementing secure identity and access management for AI agents with Okta!

https://www.linkedin.com/in/patmriley/
https://www.linkedin.com/posts/cgcladera_auth0-for-ai-agents-secure-agentic-apps-activity-7399029829565579264-9Gdf/

## OpenAI + @Temporalio : Building Durable, Production Ready Agents - Cornelia Davis, Temporal

- Upload date: 2026-01-12
- Video: https://www.youtube.com/watch?v=k8cnVCMYmNc
- Transcript: raw/20260112_k8cnVCMYmNc/k8cnVCMYmNc.en-orig.vtt
- Metadata: raw/20260112_k8cnVCMYmNc/k8cnVCMYmNc.info.json

Everyone is building AI Agents, and everyone is looking for ways to build them more easily. Earlier this year, OpenAI released the OpenAI Agents SDK to bring the patterns they have found to work for building agents to the developer community. With the SDK you can define AI agents by supplying them instructions (prompts), specifying which model to use (OpenAI or not), listing tools it uses (including MCP), and much more. The OpenAI Agents SDK encourages a paradigm of orchestrated micro-agents, which themselves may have micro-orchestrations within them with the use of handoffs. It’s an elegant and powerful model.

But a good AI Agents programming model is not enough. These agents are ultimately wildly distributed systems and are plagued with all of the problems such systems bring.

- How can they persevere through flakey networks?
- How can they function when LLMs are rate limited?
- How can they run for long periods of time (hours, days, weeks, months) when infrastructure is rarely stable that long?

In this workshop, we’ll show you how. Temporal is an open source (MIT license) durable execution framework that brings resilience to AI agents, and in this workshop we’ll show you how it’s done with the OpenAI Agents SDK. Spoiler: OpenAI and Temporal have done all of the heaving lifting for you with an integration announced earlier this year.

Oh, and OpenAI themselves use Temporal to help make several of their products production ready (image gen and Codex, for example).

Not using the OpenAI Agents SDK? Do come anyway; the foundational concepts carry over to different agent frameworks (and more integrations are coming all the time).

https://twitter.com/cdavisafc
https://www.linkedin.com/in/corneliadavis

## Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect

- Upload date: 2026-01-12
- Video: https://www.youtube.com/watch?v=96G7FLab8xc
- Transcript: raw/20260112_96G7FLab8xc/96G7FLab8xc.en-orig.vtt
- Metadata: raw/20260112_96G7FLab8xc/96G7FLab8xc.info.json

Too many MCP servers are simply glorified REST wrappers, regurgitating APIs that were designed for SDKs, not agents. This leads to confused LLMs, wasted tokens, and demonstrably poor performance. If you've ever pointed an MCP generator at an OpenAPI spec and called it a day, this talk is your intervention.

Like any product, great MCP servers are the result of careful design. This talk shares the hard-won lessons from creating FastMCP, the most popular framework for building MCP servers (and yes, for generating them, too). The secret is to stop thinking about endpoints and start thinking about products. We will cover the three pillars of agent-native product design—Discovery, Iteration, and Context—providing an actionable framework for curating context into small, highly effective surface areas that lead to better AI outcomes.

Jeremiah Lowin, CEO of Prefect
https://twitter.com/jlowin
https://www.linkedin.com/in/jlowin
https://github.com/jlowin

## Spec-Driven Development: Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro

- Upload date: 2026-01-09
- Video: https://www.youtube.com/watch?v=HY_JyxAZsiE
- Transcript: raw/20260109_HY_JyxAZsiE/HY_JyxAZsiE.en-orig.vtt
- Metadata: raw/20260109_HY_JyxAZsiE/HY_JyxAZsiE.info.json

In the AI coding era, we have powerful tools, but tools still require honing to work effectively. Spec-Driven Development allows for reproducible and reliable delivery, but spending time up-front to improve the spec process will yield the best approach. Learn how the Kiro team does this, and how you can too!

https://www.linkedin.com/in/al-harris-7a755640/

## Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands

- Upload date: 2026-01-08
- Video: https://www.youtube.com/watch?v=rcsliSIy_YU
- Transcript: raw/20260108_rcsliSIy_YU/rcsliSIy_YU.en-orig.vtt
- Metadata: raw/20260108_rcsliSIy_YU/rcsliSIy_YU.info.json

Today's agents are best at small, atomic coding tasks. Much larger tasks--like major refactors and breaking dependency updates--are highly automatable but hard to one-shot.

In this session, we'll discuss patterns for orchestrating large-scale code changes with swarms of agents and a human in the loop.

We'll also work through a concrete example: migrating an entire codebase from one React state management library to another.

https://twitter.com/RobertBrennan

Slides: https://dub.sh/openhands-workshop

## DSPy: The End of Prompt Engineering - Kevin Madura, AlixPartners

- Upload date: 2026-01-08
- Video: https://www.youtube.com/watch?v=-cKUW6n8hBU
- Transcript: raw/20260108_-cKUW6n8hBU/-cKUW6n8hBU.en-orig.vtt
- Metadata: raw/20260108_-cKUW6n8hBU/-cKUW6n8hBU.info.json

Applications developed for the enterprise need to be rigorous, testable, and robust. The same is true for applications that use AI, but LLMs can make this challenging. In other words, you need to be able to program with LLMs, not just tweak prompts. In this talk we'll cover why DSPy really is all you need in building applications with LLMs. We'll dive into real-world examples where we have successfully automated manual work using an opinionated DSPy-first approach to structuring applications, covering everything from simple modules to using SoTA optimizers to measurably improve performance.

https://x.com/kmad/


**Summary**
Kevin Madura, a consultant at AlixPartners, argues that building robust enterprise AI applications requires shifting from brittle "prompt engineering" to "programming with LLMs" using **DSPy**. He contends that prompts should be treated as implementation details optimized by the system, while developers focus on defining typed interfaces (Signatures) and modular logic (Modules). The session moves from a conceptual overview of DSPy's primitives—Signatures, Modules, Adapters, and Optimizers—to a live code walkthrough. Madura demonstrates real-world use cases, including a complex pipeline that routes files by type (SEC filings vs. contracts) and a "boundary detector" that uses visual layout to segment legal documents. The talk concludes with a demonstration of how Optimizers (like MIPRO) can automatically tune these programs to outperform manual baselines, followed by a Q&A on production costs and feedback loops.

**Timestamps**

00:00 Introduction & The Enterprise AI Challenge
07:12 The 6 Core Concepts of DSPy (Signatures, Modules, Adapters)
13:23 Deep Dive: Class-based vs. Shorthand Signatures
19:57 Adapters: Controlling the Prompt Format (JSON vs. BAML)
24:17 Optimizers: The "Killer Feature" for Transferability
31:08 Code Walkthrough: Setup & Model Mixing
36:24 Handling Documents: "Poor Man's RAG" with Attachments
42:10 Adapter Comparison: Improving Token Efficiency with BAML
47:20 Optimizers in Practice: Creating Datasets & Metrics
51:13 Complex Pipeline: Routing & Classifying Arbitrary Files
56:00 Advanced Use Case: PDF Boundary Detection via Visuals
01:01:22 Analyzing Optimization Results & The "DSPy Hub" Concept
01:09:02 Q&A: Handling Delayed Feedback & Online Learning
01:13:00 Conclusion

## Building durable Agents with Workflow DevKit & AI SDK - Peter Wielander, Vercel

- Upload date: 2026-01-06
- Video: https://www.youtube.com/watch?v=kmV-qg4uoNI
- Transcript: raw/20260106_kmV-qg4uoNI/kmV-qg4uoNI.en-orig.vtt
- Metadata: raw/20260106_kmV-qg4uoNI/kmV-qg4uoNI.info.json

Learn to build and deploy AI agents using Vercel's new open source Workflows platform.

https://twitter.com/vaguelyserious
https://www.linkedin.com/in/peter-wielander

## Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize

- Upload date: 2026-01-06
- Video: https://www.youtube.com/watch?v=SbcQYbrvAfI
- Transcript: raw/20260106_SbcQYbrvAfI/SbcQYbrvAfI.en-orig.vtt
- Metadata: raw/20260106_SbcQYbrvAfI/SbcQYbrvAfI.info.json

Following from Aparna's talk: https://www.youtube.com/watch?v=pP_dSNz_EdQ

Learn how to create a feedback loop to continuously improve your AI prompts and responses.

https://www.linkedin.com/in/sallyann-delucia-59a381172/

## Welcome to AIE CODE - Jed Borovik, Google DeepMind

- Upload date: 2026-01-05
- Video: https://www.youtube.com/watch?v=mdEh4lBO_R0
- Transcript: raw/20260105_mdEh4lBO_R0/mdEh4lBO_R0.en-orig.vtt
- Metadata: raw/20260105_mdEh4lBO_R0/mdEh4lBO_R0.info.json

Day 2 emcee Jed Borovik opens the day for coding agents and labs.

## Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic

- Upload date: 2026-01-05
- Video: https://www.youtube.com/watch?v=TqC1qOfiVcQ
- Transcript: raw/20260105_TqC1qOfiVcQ/TqC1qOfiVcQ.en-orig.vtt
- Metadata: raw/20260105_TqC1qOfiVcQ/TqC1qOfiVcQ.info.json

Learn to use Anthropic's Claude Agent SDK (formerly Claude Code SDK) for AI-powered development workflows!

https://platform.claude.com/docs/en/agent-sdk/overview
https://x.com/trq212

**AI Summary**
This workshop by Thariq Shihipar (Anthropic) details the architecture and implementation of the **Claude Agent SDK**. The session moves from high-level theory—defining "agents" as autonomous systems that manage their own context and trajectory—to a live-coding demonstration. Shihipar builds an agent "Harness" from scratch, implementing the core **Agent Loop** (Context  Thought  Action  Observation), integrating the **Bash tool** for general computer use, and demonstrating **Context Engineering** via the file system to maintain state across long tasks.

**Timestamps**

00:00 Introduction: Agenda and the "Agent" definition
05:15 The "Harness" concept: Tools, Prompts, and Skills
10:10 Live Coding Setup: Initializing the Agent class and environment
15:45 implementing the "Think" step: Getting the model to reason before acting
25:20 The Agent Loop: connecting `act`, `observe`, and `loop`
33:10 Tool Execution: Handling XML parsing and tool inputs
42:00 The "Bash" Tool: Giving the agent command line access
49:30 Safety & Permissions: "ReadOnly" vs "ReadWrite" file access
58:15 Context Engineering: Using `ls` and `cat` to build dynamic context
01:05:00 The "Monitor": Viewing the agent's thought process in real-time
01:12:45 Handling "Stuck" States: Feedback loops and error correction
01:21:20 Multi-turn Complex Tasks: Building a "Research Agent" demo
01:35:10 Refactoring patterns: "Hooks" and deterministic overrides
01:48:39 Q&A: Reproducibility, helper scripts, and non-determinism
01:50:31 Q&A: Strategies for massive codebases (50M+ lines)
01:52:00 Closing remarks and future SDK roadmap

* **Evolution of AI Capabilities:** Shihipar argues we are shifting from **LLM Features** (categorization, single turn) to **Workflows** (structured, multi-step chains like RAG) to **Agents**. He defines agents as systems that *"build their own context, decide their own trajectories, and work very autonomously"* rather than following a rigid pipeline.
* **The Claude Agent SDK Architecture:** The SDK is built directly on top of **Claude Code** because Anthropic found they were *"rebuilding the same parts over and over again"* for internal tools.
* **The Harness:** A robust agent requires more than just a model; it needs a "Harness" containing Tools, Prompts, a **File System**, Skills, Sub-agents, and Memory.
* **Opinionated Design:** The SDK bakes in lessons from deploying Claude Code, specifically the "opinion" that general computer use (Bash) is often superior to bespoke tools.


* **The Power of the Bash Tool:** A key technical insight is that the **Bash tool** is often the most powerful tool for an agent. Instead of building custom tools for every action (e.g., a specific API wrapper for a file conversion), giving the agent access to the shell allows it to use existing software (like `ffmpeg`, `grep`, or `git`) to solve problems flexibly, similar to how a human developer works.
* **Context Engineering:** Shihipar introduces the concept of **Context Engineering** via the file system. Instead of just "Prompt Engineering," the agent uses the file system to manage its state and context.
* **Files as Memory:** The agent can write to files to "remember" things or create its own documentation (e.g., `CLAUDE.md`) to ground future actions.
* **Verification:** The file system serves as a ground truth for the agent to verify its work (e.g., checking if a file was actually created).


* **The Agent Loop & Intuition:** Building a successful agent loop is described as *"kind of an art or intuition"*. The loop generally follows a **Gather Context  Take Action  Verify Work** cycle. Shihipar emphasizes that this loop allows the agent to self-correct, a capability missing from rigid workflows.
* **Strategies for Determinism (Hooks):** During the Q&A, a technique for controlling agent behavior is discussed: **Hooks**.
* If an agent hallucinates or skips a step (e.g., guessing a Pokemon stat instead of checking a script), a hook can intercept the response and inject feedback: *"Please make sure you write a script, please make sure you read this data."*
* This enforces rules like "read before you write" without retraining the model.


* **Scaling to Large Codebases:** For massive codebases (50M+ lines), standard tools like `grep` or basic context window stuffing fail.
* **Semantic Search Limitations:** Shihipar notes that while semantic search is a common solution, it is *"brittle"* because the model isn't trained on the specific semantic index.
* **Solution:** He recommends good **"Claude MD"** files (context files) and starting the agent in a specific subdirectory to limit scope, rather than trying to index the entire 50M lines at once.

## Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)

- Upload date: 2025-12-30
- Video: https://www.youtube.com/watch?v=xz0-brt56L8
- Transcript: raw/20251230_xz0-brt56L8/xz0-brt56L8.en-orig.vtt
- Metadata: raw/20251230_xz0-brt56L8/xz0-brt56L8.info.json

AI agents are no longer confined to chat interfaces. From our original Manus app for powerful conversations, to Mail Manus for transforming your inbox into an organized command center, we've progressively expanded where an AI can work. Now, with the Manus API, we're completing the vision by giving you the final building block to deploy an intelligent agent anywhere in your stack.

In this workshop, you'll learn to use the API to build a bespoke research agent that powers deep analysis across your company's internal data. We'll show you how to dispatch a task that connects to your private systems, synthesises complex information, and delivers custom insights on demand, turning your entire knowledge base into an actionable, intelligent asset.

In this hands-on session, you will:

- Use the Manus API to dispatch and manage asynchronous agentic tasks.
- Connect the agent to private data sources using our connectors
- Build a complete workflow that synthesises information into a custom report.

By the end of the workshop you'll have a functional research agent that you can adapt for your own use case.

## SUMMARY

Ivan introduces **Manus 1.5** and the new **Manus API**, positioning Manus not just as a chatbot but as a "general action engine" capable of executing complex workflows, automating tasks, and extending human reach. Ivan Leo demonstrates the ecosystem—including a web app, Slack integration, browser operator, and Microsoft 365 integration—before diving into a workshop on building bespoke research agents. The session concludes with a Q&A covering advanced use cases like Python scripting for booking slots, browser security permissions, and future roadmap features like memory retention and document exporting.

**Timestamps:**

00:00 Introduction & Workshop Overview
00:53 What is Manus? (The Action Engine)
01:18 Manus 1.5 Updates (Performance, Quality, Architecture)
02:23 Manus Ecosystem (Web, Slack, API, Browser, M365)
03:15 Demo: French Learning App (Custom Web App)
06:02 Demo: Mail Manus (Email Automation)
06:51 Demo: Browser Operator (Coffee Search)
01:18:00 Use Case: Pickleball Booking Script
01:18:44 API & Browser Permissions
01:19:21 Future Features: Exporting to PPTX/PDF
01:20:05 Memory & Context Management

## Jack Morris: Stuffing Context is not Memory, Updating Weights is

- Upload date: 2025-12-29
- Video: https://www.youtube.com/watch?v=Jty4s9-Jb78
- Transcript: raw/20251229_Jty4s9-Jb78/Jty4s9-Jb78.en-orig.vtt
- Metadata: raw/20251229_Jty4s9-Jb78/Jty4s9-Jb78.info.json

Understanding how memory works in large language models through the lens of weights and activations. This workshop will explore the internal mechanisms of how LLMs store and retrieve information during inference.

https://x.com/jxmnop

**Summary**
Jack Morris discusses the limitations of current Large Language Models (LLMs) in handling niche, "long-tail" knowledge that falls outside their training data or within knowledge cutoffs. He critiques the reliance on massive context windows and Retrieval Augmented Generation (RAG) due to their high cost and latency (quadratic complexity of self-attention). The core thesis advocates for a third paradigm: **"training things into weights,"** or efficiently injecting specific knowledge directly into model parameters, effectively treating weights as a memory storage mechanism distinct from the "working memory" of activations.

**Timestamps**

00:00 The Knowledge Cutoff & Long-Tail Problem
02:22 Three Methods for Knowledge Injection (Context, RAG, Weights)
03:29 Limitations of "Full Context" (Cost & Latency)
05:12 The Transformer Bottleneck: Self-Attention Complexity
06:49 Context Rot: Performance degradation in long context
58:49 Q&A: The Return of Federated Learning
59:34 Q&A: Specialized Knowledge Models vs. Karpathy’s "Reasoning Engines"
01:01:21 Q&A: Temporal Information & Future Research

**Technical Summary**

* **The "Long Tail" Knowledge Problem**: Morris identifies a critical failure mode in current LLMs: they excel at general knowledge (e.g., "Did the Blue Jays win the World Series?") but fail catastrophically at **niche, specific tasks** (e.g., "Optimize this AMD GPU kernel" or "What are the terms of the BlackRock partnership?").
* *Constraint*: These tasks are either outside the training data, subject to knowledge cutoffs, or require private data.
* *Failure of Prompting*: No amount of "please" or prompt engineering can force a model to know facts it simply doesn't have stored.


* **The Three Paradigms of Knowledge Injection**:
* **Full Context**: Stuffing all relevant data into the prompt. Works for small domains (e.g., a single medical record) but scales poorly.
* **RAG (Retrieval Augmented Generation)**: Retrieving only relevant chunks.
* **Training into Weights**: The proposed solution. Injecting knowledge directly into the model's parameters (weights) rather than its transient state (activations).


* **The "Context Trap": Cost and Latency**:
* **Quadratic Dependency**: The self-attention mechanism in Transformers requires every token to look at every other token, creating a quadratic compute cost.
* **Latency Impact**: Morris shares benchmarks: "If you have 1,000 tokens of context, we can output **10,000 tokens per second**. If you have 128k tokens of context, we can output **130 tokens per second**." This is an orders-of-magnitude slowdown.
* **Performance Degradation**: He cites the *Chroma "Context Context Broad"* report, showing that as context grows, reasoning capabilities degrade even if the model doesn't "break".


* **Weights vs. Activations (Inferred from thesis)**:
* The talk distinguishes between **activations** (short-term, expensive context) and **weights** (long-term, efficient storage).
* Morris argues that for niche, static knowledge (like internal company wikis or specialized codebases), updating weights is more efficient than re-feeding context every inference cycle.


* **Q&A: Federated Learning & Distributed Training**:
* Federated learning (training across many machines) failed previously due to network costs of syncing massive models.
* Morris predicts a comeback because "you only need to train a million parameters instead of a trillion," making the network overhead manageable for specialized knowledge updates.


* **Q&A: Specialized Models vs. General Reasoners**:
* Responding to Andrej Karpathy's view of LLMs as pure "reasoning engines" (small brains, using tools), Morris argues there is a middle ground.
* *Analogy*: "A lawyer doesn't have the entire legal code memorized, but they know how to use tools." However, a model that "knows nothing" is inefficient. He advocates for **specialized models** that are "good at something you care about but bad at other things," rather than a generic reasoning engine that relies entirely on external retrieval.

## AGI: The Path Forward – Jason Warner & Eiso Kant, Poolside

- Upload date: 2025-12-27
- Video: https://www.youtube.com/watch?v=OGCG_QkCcZo
- Transcript: raw/20251227_OGCG_QkCcZo/OGCG_QkCcZo.en-orig.vtt
- Metadata: raw/20251227_OGCG_QkCcZo/OGCG_QkCcZo.info.json

In Poolside's first ever public conference demo, Poolside's CEOs present their vision and roadmap towards achieving AGI-level capabilities for knowledge work.

## How Claude Code Works - Jared Zoneraich, PromptLayer

- Upload date: 2025-12-26
- Video: https://www.youtube.com/watch?v=RFKCzGlAU6Q
- Transcript: raw/20251226_RFKCzGlAU6Q/RFKCzGlAU6Q.en-orig.vtt
- Metadata: raw/20251226_RFKCzGlAU6Q/RFKCzGlAU6Q.info.json

Deep dive into what we have independently figured out about the architecture and implementation of Claude's code generation capabilities. Not officially endorsed by Anthropic.

Speaker: Jared Zoneraich  |  Founder & CEO, PromptLayer
https://x.com/imjaredz
https://www.linkedin.com/in/imjaredz
https://imjaredz.com/


Jared Zoneraich from PromptLayer dissects the architecture of "Claude Code" (Anthropic's CLI agent), arguing that its success stems not from complex agentic frameworks but from a radical simplification: a single-threaded "Master Loop" paired with highly capable models. He contrasts this "give it tools and get out of the way" approach with earlier, brittle DAG-based (Directed Acyclic Graph) architectures. The talk breaks down the specific internal tools (Bash, FileEdit, Grep), the "Todo" planning mechanism, and the critical role of sandboxing and system prompts in making the agent reliable for production engineering tasks.

**Timestamps:**

00:00 Introduction to Claude Code & AI Coding Agents
04:35 The Evolution and Breakthroughs of Coding Agents
07:54 Core Philosophy: Simple Architecture & Better Models
12:11 Key Tools and Their Functionality in Claude Code
15:52 The Power of Bash and Implementation of To-Do Lists
19:25 Structure of To-Do Lists vs. Complex DAGs
23:24 Relying on the Model & Importance of Sandboxing
27:23 Sandboxing, Sub-Agents, and System Prompts
31:55 System Prompts and the Use of "Skills"
36:05 Challenges with Skills & Future Innovations
39:21 Alternative Architectures: The "AI Therapist" Problem
42:14 Perspectives on Different Agents: Codex vs. Amp
45:03 Context Management in Amp & Cursor
48:42 Evaluating Coding Agents & Rigorous Tools
52:01 Testing Tools & Future of Headless SDKs
55:11 Key Takeaways & Building the Slide Deck with Claude Code
57:25 Discussion on DAGs and Sequential Execution
01:00:15 The Future of LLM Calls and Spec-Driven Development

## Shipping AI That Works: An Evaluation Framework for PMs – Aman Khan, Arize

- Upload date: 2025-12-26
- Video: https://www.youtube.com/watch?v=2HNSG990Ew8
- Transcript: raw/20251226_2HNSG990Ew8/2HNSG990Ew8.en-orig.vtt
- Metadata: raw/20251226_2HNSG990Ew8/2HNSG990Ew8.info.json

GenAI is reshaping the product landscape, creating huge opportunities (along with new expectations) for product managers. Yet while prompt engineering and model tuning get the spotlight, one critical skill can get overlooked: rigorous evaluation.

This talk will help PMs move beyond gut-feel “vibe checks” to adopt concrete, repeatable evaluation strategies for LLM-powered products. I'll break down essential eval methodologies, from human feedback and code-based checks to cutting-edge LLM-based evaluations. Drawing on real-world examples, I'll share a practical framework PMs can use to:

- Confidently evaluate AI-driven features
- Ground decisions in real, repeatable data
- Build trust and delight through consistent quality

## Why Agent Hype can fall short of reality – Joel Becker, METR

- Upload date: 2025-12-24
- Video: https://www.youtube.com/watch?v=RhfqQKe22ZA
- Transcript: raw/20251224_RhfqQKe22ZA/RhfqQKe22ZA.en-orig.vtt
- Metadata: raw/20251224_RhfqQKe22ZA/RhfqQKe22ZA.info.json

AI models are crushing benchmarks. SWE-bench scores are climbing, and METR's measured time horizons are rising rapidly. Yet when we deployed these same models in a field study with experienced developers, they didn't speed up work. What's going on? Are benchmarks misleading us about AI capabilities? Are we missing something about how AI performs in the real world? In this talk, we'll reconcile lab and field evidence on AI capabilities. Drawing from METR's time horizon measurements and developer productivity RCT, we'll explore why impressive benchmark performance doesn't always translate to real-world impact. We'll examine potential explanations—from reliability requirements to task distribution to capability elicitation—and discuss what this means for automated AI R&D.

Speaker: Joel Becker  |  Researcher, METR
https://x.com/joel_bkr
https://www.linkedin.com/in/joel-becker/
https://github.com/joel-becker


**Timestamps:**

00:00 Introduction to METR & The Capability Gap
01:49 The Problem with Current Benchmarks (Saturation & Interpretation)
03:19 METR’s New Methodology: Human Time Horizons
04:52 Empirical Results: Fitting Capability Curves
06:19 Time Horizon Trends: Claude 3 Opus vs. o1-preview
17:43 Randomized Controlled Trial (RCT) Discussion
18:18 Reconciling the Gap: Why High Benchmarks Don't Mean High Productivity
19:18 Explaining the Discrepancy: Context, Reliability, and Task Interdependence
20:22 Future Work & Hiring at METR

## Developer Experience in the Age of AI Coding Agents – Max Kanat-Alexander, Capital One

- Upload date: 2025-12-23
- Video: https://www.youtube.com/watch?v=rT2Del5pwg4
- Transcript: raw/20251223_rT2Del5pwg4/rT2Del5pwg4.en-orig.vtt
- Metadata: raw/20251223_rT2Del5pwg4/rT2Del5pwg4.info.json

It feels like every two weeks, the world of software engineering is being turned on its head. Are there any principles we can rely on that will continue to hold true, and that can help us prepare for the future, no matter what happens? Max uses research, data, and his 20+ years working in enterprise Developer Experience teams to talk through what we can do now that will prepare us for an agentic future, no matter what that future holds.

Speaker: Max Kanat-Alexander  |  Executive Distinguished Engineer, Capital One
https://x.com/mkanat
https://www.linkedin.com/in/mkanat/
https://max.kanat.us/


Timestamps

00:00 The "New Hotness" Fatigue & Unpredictability 
01:58 The "No Regrets" Investment Framework
02:55 Input 1: Standardized Development Environments 
04:40 Input 2: Native CLIs and APIs for Agents 
05:08 Input 3: Deterministic Validation & Actionable Errors 
06:45 Input 4: Structure of Systems & Legacy Code 
14:35 The Necessity of Apprenticeship in Code Review 
15:00 The Vicious Cycle: Bad Codebases Break Agents 
15:54 The Virtuous Cycle: Better DevEx Accelerates Agents 
16:30 Summary Checklist & Conclusion

## The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize

- Upload date: 2025-12-23
- Video: https://www.youtube.com/watch?v=pP_dSNz_EdQ
- Transcript: raw/20251223_pP_dSNz_EdQ/pP_dSNz_EdQ.en-orig.vtt
- Metadata: raw/20251223_pP_dSNz_EdQ/pP_dSNz_EdQ.info.json

Your coding agent writes code—but not like your team. RL has boosted base models, but it’s opaque and hard to scale across enterprises. Most agents still rely on brittle, hand-edited system prompts or style guides (e.g., agent.md)—what if your agent learned from your reviews and updated them automatically? In this talk, I’ll show a system-prompt learning loop—RL techniques applied to prompts, not model weights—that continually tunes an agents.md, so the agent learns instructions from your PR's, feedback & evaluations. You’ll leave with a concrete recipe to capture runtime signals, and auto-tune system prompts—applicable to any type of agent you’re building.

Speakers: 
Aparna Dhinakaran  |  Co-founder & CPO, Arize
https://x.com/aparnadhinak
https://www.linkedin.com/in/aparnadhinakaran/

## Small Bets, Big Impact Building GenBI at a Fortune 100 – Asaf Bord, Northwestern Mutual

- Upload date: 2025-12-23
- Video: https://www.youtube.com/watch?v=LU9KgcZDRfY
- Transcript: raw/20251223_LU9KgcZDRfY/LU9KgcZDRfY.en-orig.vtt
- Metadata: raw/20251223_LU9KgcZDRfY/LU9KgcZDRfY.info.json

Enterprises don’t usually make moonshots, especially in GenAI. Governance, budgets, and risk aversion make it almost impossible to justify a huge, uncertain investment.

At Northwestern Mutual, we’re building GenBI, an LLM-powered analytics copilot, by flipping that logic. Instead of one big bet, we created an incremental roadmap of small, fundable projects. Each is tied to real business outcomes, delivers measurable ROI, and builds the trust needed to move forward.

This talk shares how we framed the problem, earned leadership support, and designed a modular architecture grounded in real data. We’ll show how each research step can stand on its own - productized, measurable, and deployable. Attendees will leave with a clear blueprint for making AI transformation fundable, governable, and real inside large, risk-averse organizations.

Speaker: Asaf Bord  |  AI Product Lead, Northwestern Mutual
https://www.linkedin.com/in/asafbord/recent-activity/all/
https://asafbord.wixsite.com/home

## Amp Code: Next Generation AI Coding – Beyang Liu, Amp Code

- Upload date: 2025-12-22
- Video: https://www.youtube.com/watch?v=gvIAkmZUEZY
- Transcript: raw/20251222_gvIAkmZUEZY/gvIAkmZUEZY.en-orig.vtt
- Metadata: raw/20251222_gvIAkmZUEZY/gvIAkmZUEZY.info.json

Introduction to Amp Code and its approach to AI-powered software development.

Speaker: Beyang Liu  |  Co-founder & CTO, Amp Code
https://x.com/beyang
https://www.linkedin.com/in/beyang-liu/
https://github.com/beyang

Timestamps:

00:00 Introduction & The "Weird" Ethos 
01:19 Amp Terminal UI & Editor Integration 
03:02 The "Review Bottleneck" & Review Interface 
03:57 Defining an Agent: For Loops & Tool Calls 
04:46 The Argument Against MCP (Context Confusion) 
06:04 Tool Call Context Exhaustion 
14:51 Business Model: Ads in the Terminal 
15:38 Community & The "Weird" Builder Cohort

## Making Codebases Agent Ready – Eno Reyes, Factory AI

- Upload date: 2025-12-22
- Video: https://www.youtube.com/watch?v=ShuJ_CN6zr4
- Transcript: raw/20251222_ShuJ_CN6zr4/ShuJ_CN6zr4.en-orig.vtt
- Metadata: raw/20251222_ShuJ_CN6zr4/ShuJ_CN6zr4.info.json

Agents are eating software engineering. Yet teams deploying these tools face mixed results. Agents work great in demos but fail unreliably in production, frustrating engineering teams who expected better. The gap isn't model quality—it's environment readiness. Agents need fast feedback loops, explicit instructions, and predictable environments to work effectively. They break on missing environment variables, undocumented dependencies, and tribal knowledge that "everyone just knows."

What if you could measure and fix what's holding your agents back? Enter Agent Readiness. In this talk, we'll explore eight categories that determine whether your codebase is agent-ready: from style validation and build systems to dev environments and observability. You'll learn how to score your repos, identify easy wins, and build environments where agents actually ship reliable code. We'll share real signals from Factory's work running autonomous agents in enterprise production repos—and give you a practical framework to make your team's agents more productive starting tomorrow.

Speaker:  Eno Reyes  |  CTO, Factory AI
https://x.com/EnoReyes
https://www.linkedin.com/in/enoreyes/
https://enoreyes.com/

The video argues that the primary bottleneck for adopting AI agents in software engineering is not model capability, but rather the "agent readiness" of the codebase—specifically the rigour of automated verification systems. Eno Reyes from Factory AI posits that software development is shifting from a specification-based process to a verification-based one (Software 2.0), where the ability to mechanically validate code (via linters, tests, and strict environments) determines an agent's success. He suggests that organizations must invest in these feedback loops to create a "flywheel" effect: better environments lead to better agents, which in turn free up time to further improve the environment.

00:00 Introduction & Factory AI Mission 
01:19 Software 2.0: Automation via Verification 
02:21 The Asymmetry of Verification (P vs NP) 
04:01 Automated Validation as an Agent Constraint 
06:09 Shift to Specification-Driven Development 
11:51 The New DevX Loop: Investing in Feedback Cycles 
13:42 Conclusion: The ROI of Agent Readiness

## The 3 Pillars of Autonomy – Michele Catasta, Replit

- Upload date: 2025-12-22
- Video: https://www.youtube.com/watch?v=MLhAA9yguwM
- Transcript: raw/20251222_MLhAA9yguwM/MLhAA9yguwM.en-orig.vtt
- Metadata: raw/20251222_MLhAA9yguwM/MLhAA9yguwM.info.json

AI agents exhibit vastly different degrees of autonomy. Yet, the ability to accomplish objectives without supervision is the critical north star for agent progress, especially in software creation. For non-technical users who cannot supervise software creation, full autonomy is essential, not optional.

First of all, I will discuss two foundational capabilities to achieve true autonomy: automatic testing to verify correctness without human validation, and advanced context management to maintain coherence across complex, long-horizon tasks.

With autonomy established, parallelization becomes the key to delivering a compelling user experience. Sequential execution forces users to wait extensively before seeing progress, breaking the development flow. This talk explores parallelization models (task-level parallelism, out-of-order execution, plan decomposition, etc.) and their tradeoffs in latency, resource consumption, and correctness guarantees.


Speaker:  Michele Catasta  |  VP of AI, Replit
https://x.com/pirroh
https://www.linkedin.com/in/pirroh/
https://github.com/pirroh

talk originally titled "Autonomy is all you need" and renamed after YouTube A/B test

## No More Slop – swyx

- Upload date: 2025-12-22
- Video: https://www.youtube.com/watch?v=IoiHI7p12Ao
- Transcript: raw/20251222_IoiHI7p12Ao/IoiHI7p12Ao.en-orig.vtt
- Metadata: raw/20251222_IoiHI7p12Ao/IoiHI7p12Ao.info.json

Why we need to eliminate low-quality code and work in AI engineering.

Speaker: swyx  |  Curator, AI Engineer
https://x.com/swyx
https://www.linkedin.com/in/shawnswyxwang/
https://www.swyx.io/

## The Infinite Software Crisis – Jake Nations, Netflix

- Upload date: 2025-12-20
- Video: https://www.youtube.com/watch?v=eIoohUmYpGI
- Transcript: raw/20251220_eIoohUmYpGI/eIoohUmYpGI.en-orig.vtt
- Metadata: raw/20251220_eIoohUmYpGI/eIoohUmYpGI.info.json

In 1968, the term ""Software Crisis"" emerged when systems grew beyond what developers could manage. Every generation since has ""solved"" it with more powerful tools, only to create even bigger problems.

Today, AI accelerates the pattern into the Infinite Software Crisis. AI-generated codebases mirror the meandering conversations that created them. Every clarification and pivot gets baked into your architecture. We're vibecoding our way to disaster.

The solution: choose simple over easy. One long conversation is easy. Separate phases with clean boundaries are simple.

This talk presents a three-phase methodology:

- Research to understand the existing system
- Planning to design the approach
- Implementation with clean context

While everyone races to generate code at machine speed, the engineers who thrive will be those who know when a system is getting tangled. In the age of infinite code generation, human judgment applied at the right moments becomes your competitive advantage.

Speaker:  Jake Nations  |  Engineering, Netflix
https://www.linkedin.com/in/jakenations/
https://github.com/Nayshins

Timestamps:
00:00 The Modern Confession: Shipping Code We Don’t Understand 
01:53 The History of the Software Crisis (1968 to Present) 
03:30 Fred Brooks and "No Silver Bullet" 
04:12 Simple vs. Easy (Rich Hickey’s Definition) 
05:40 The AI Trap: "Vibecoding" and Conversational Complexity 
06:39 The problem with iterative AI chat interfaces 
15:12 Implementation Phase: Using Manual Migration as a Seed 
16:14 The Knowledge Gap: Code Generation vs. Code Understanding 
17:40 Conclusion: Software is a Human Endeavor

## From Arc to Dia: Lessons learned building AI Browsers – Samir Mody, The Browser Company of New York

- Upload date: 2025-12-19
- Video: https://www.youtube.com/watch?v=o4scJaQgnFA
- Transcript: raw/20251219_o4scJaQgnFA/o4scJaQgnFA.en-orig.vtt
- Metadata: raw/20251219_o4scJaQgnFA/o4scJaQgnFA.info.json

What happens when you take a polished, beloved browser and rebuild it from the ground up around AI? In 2024, The Browser Company did exactly that: transforming Arc, a human-designed browser, into Dia, a browser with an AI-native browser experience. The journey forced us to unlearn what we knew about product design, system architecture, and even what "good UX" means when the interface itself can reason, plan, and act.

In this talk, I'll share the lessons we learned along the way: how we redesigned for emergent behavior instead of deterministic control, how our engineering and design teams learned to prototype with language models, and how our culture evolved to ship fast in a world where we're still learning what a good system looks like. You'll leave with practical insights for building AI-native products, from technical architecture to team mindset, and a glimpse into how we're thinking about the future of AI browsing.

Speaker:  Samir Mody  |  Head of AI Engineering, The Browser Company
https://x.com/jedimody
https://www.linkedin.com/in/samir-mody/

## Welcome to AIE LEAD - Alex Lieberman, Tenex

- Upload date: 2025-12-19
- Video: https://www.youtube.com/watch?v=RQ5Jt8zDBp8
- Transcript: raw/20251219_RQ5Jt8zDBp8/RQ5Jt8zDBp8.en-orig.vtt
- Metadata: raw/20251219_RQ5Jt8zDBp8/RQ5Jt8zDBp8.info.json

more at https://ai.engineer

## Leadership in AI Assisted Engineering – Justin Reock, DX (acq. Atlassian)

- Upload date: 2025-12-19
- Video: https://www.youtube.com/watch?v=PmZDupFP3UM
- Transcript: raw/20251219_PmZDupFP3UM/PmZDupFP3UM.en-orig.vtt
- Metadata: raw/20251219_PmZDupFP3UM/PmZDupFP3UM.info.json

To realize meaningful returns on AI investments, leadership must take accountability and ownership of establishing best practices, enabling engineers, measuring impact, and ensuring proper guardrails are in place. When prompting practice and reflexive AI use is driven from the top down, engineers can align on the highest value use cases and experience peak productivity gains. When coupled with DX's AI Measurement Framework, leaders can gain a clear picture of AI's true impact, identify the real bottlenecks in the SDLC that can be augmented with AI, and drive improvement. In this session, Justin Reock, Deputy CTO at DX, and author of DX's Guide to AI Assisted Engineering, will explain what the most effective leaders of AI enabled engineering organizations are doing to drive satisfactory utilization, augmentation, and psychological safety across their teams. Based on interviews, use cases, and data, leaders will walk away with an understanding of how to best lead their teams through mature AI rollouts.

Speaker:  Justin Reock  |  Deputy CTO, DX
https://www.linkedin.com/in/justinreock/

## Paying Engineers like Salespeople – Arman Hezarkhani, Tenex

- Upload date: 2025-12-19
- Video: https://www.youtube.com/watch?v=4mRekpZpBZs
- Transcript: raw/20251219_4mRekpZpBZs/4mRekpZpBZs.en-orig.vtt
- Metadata: raw/20251219_4mRekpZpBZs/4mRekpZpBZs.info.json

Most software teams still run on an outdated unit of measure: hours, days, years.

That single choice misaligns every incentive—clients want fewer, engineers want more, and everyone loses speed.

At Tenex, we threw the hourly model out and built an outcome-based system where we pay and charge per story point, tying incentives directly to shipped value.

In this talk, I’ll break down exactly how it works—the math, the cultural shifts, the AI tooling that makes it possible, and the results we’ve seen across real client projects. You’ll leave with a blueprint for running a high-trust, high-velocity engineering team that scales output, not overhead.

Speakers: Arman Hezarkhani  |  CTO, Tenex
https://x.com/ArmanHezarkhani
https://www.linkedin.com/in/ahez/
https://armanh.com/

## AI Consulting in Practice – NLW, Superintelligent, @AIDailyBrief⁩

- Upload date: 2025-12-18
- Video: https://www.youtube.com/watch?v=ehQFj6VmuI8
- Transcript: raw/20251218_ehQFj6VmuI8/ehQFj6VmuI8.en-orig.vtt
- Metadata: raw/20251218_ehQFj6VmuI8/ehQFj6VmuI8.info.json

Insights from consulting on AI implementation across various organizations.

Speaker: NLW  |  Host, AI Daily Brief & CEO, Super.ai
https://x.com/nlw
https://www.youtube.com/@AIDailyBrief

## Dispatch from the Future: building an AI-native Company – Dan Shipper, Every, AI & I

- Upload date: 2025-12-18
- Video: https://www.youtube.com/watch?v=MGzymaYBiss
- Transcript: raw/20251218_MGzymaYBiss/MGzymaYBiss.en-orig.vtt
- Metadata: raw/20251218_MGzymaYBiss/MGzymaYBiss.info.json

The central thesis is that there is a "10x difference" between an organization where 90% of engineers use AI versus one where 100% do. At 100% adoption, the fundamental physics of software engineering change: a single developer can build and maintain complex production apps, managers can meaningfully contribute to code, and the organization can move from a "memo culture" to a "demo culture." He introduces the concept of "Compounding Engineering"—where every feature built creates artifacts and agents that make building the next feature easier—and argues that we are shifting from text-editor-based coding to agentic, delegated workflows (Claude Code) that allow for parallel processing and "fractured attention" work.

Timestamps:

00:00 Introduction & The "No Playbook" Reality 
02:11 The 10x Difference: 90% vs 100% AI Adoption 
03:16 Every's "AI Native" Structure (15 people, 4 products) 
04:14 Product Examples: Kora, Monologue, & Spiral 
05:30 The Shift to Cloud Code & Agentic Workflows 
06:00 Parallel Execution & Vibe Coding 
07:20 The Rise of "Demo Culture" 
14:00 Cross-App Collaboration & Customer Agents 
14:35 The Polyglot Stack Advantage 
15:09 Managers Committing Code & Fractured Attention 
16:20 Compounding Engineering & Conclusion

AIE is coming to London and SF! see dates and sign up to be notified of sponsorships, CFPs, and tickets: https://ai.engineer

## Code World Model: Building World Models for Computation – Jacob Kahn, FAIR Meta

- Upload date: 2025-12-17
- Video: https://www.youtube.com/watch?v=sYgE4ppDFOQ
- Transcript: raw/20251217_sYgE4ppDFOQ/sYgE4ppDFOQ.en-orig.vtt
- Metadata: raw/20251217_sYgE4ppDFOQ/sYgE4ppDFOQ.info.json

Today, most neural models for code learn from code itself: sequences of tokens that capture syntax rather than computation. While this allows models to learn the shape of code, true reasoning about programs requires understanding execution and the dynamics of computation. In this talk, I’ll present a world-model approach to learning from code: one that incorporates data from program execution to implicitly predict behavior while generating code. The Code World Model (CWM) embodies this paradigm, opening new capabilities for reasoning and offering a foundation for future research and prototyping in AI-driven software systems.

Speaker: Jacob Kahn  |  Research Scientist, FAIR, Meta
https://www.linkedin.com/in/jacobdavidkahn/

## AI Kernel Generation: What's working, what's not, what's next – Natalie Serrino, Gimlet Labs

- Upload date: 2025-12-17
- Video: https://www.youtube.com/watch?v=6guQG_tGt0o
- Transcript: raw/20251217_6guQG_tGt0o/6guQG_tGt0o.en-orig.vtt
- Metadata: raw/20251217_6guQG_tGt0o/6guQG_tGt0o.info.json

In this talk, we'll talk about how AI generated kernels can meaningfully speed up custom PyTorch code, without any human effort.

Lots of great frameworks exist to optimize PyTorch with programmatic optimizations, such as Triton and MLX. But the strongest AI performance gains come from hand-written, low-level kernels that are targeted to the exact device and workload. These are tedious and time-consuming to write, especially when supporting multiple platforms. What if we could automate this process with AI?

We'll cover the best practices for AI generating low-level kernels, from how to test and validate the kernels, and what type of agents and contexts are needed to get the best results. We'll cover the research we did where this approach improved PyTorch inference performance on Apple devices.

Speaker:  Natalie Serrino  |  Cofounder, Gimlet Labs
https://x.com/nserrino
https://www.linkedin.com/in/natalieserrino/

## Your Support Team Should Ship Code – Lisa Orr, Zapier

- Upload date: 2025-12-16
- Video: https://www.youtube.com/watch?v=RmJ4rTLV_x4
- Transcript: raw/20251216_RmJ4rTLV_x4/RmJ4rTLV_x4.en-orig.vtt
- Metadata: raw/20251216_RmJ4rTLV_x4/RmJ4rTLV_x4.info.json

Zapier maintains 8000+ integrations that break as APIs change. We had thousands of backlog support tickets with dozens more arriving weekly. To keep up with the traffic, we started building AI tools to help ship integration fixes faster. We began by shadowing engineers fixing tickets and building tools we believed would expedite the fix process. Our first effort, an API playground hosting AI tools like diagnosis and test generation, failed to get engineering traffic because it pulled builders out of their workflows. We pivoted to MCP tools that engineers could use directly in their IDEs. MCP tools gained traction, but our most valuable tool, Diagnosis, took too long to run. Engineers wouldn't wait for it, revealing we needed an asynchronous approach. We built Scout Agent to string our tools together, autonomously reading support tickets, gathering context, generating fixes with tests, and submitting merge requests ready for review. This agent approach has gained traction with our support team handling high ticket volumes. An MR ready for review means they can validate and ship a fix quickly before needing to jump on the next incoming ticket. Throughout this process we've learned that the real challenge is everything surrounding code generation. Before writing code, Scout Agent needs both the right context and to show its work so engineers trust its recommendations. After generation, engineers need to quickly validate and correct the proposed fix, otherwise MRs sit unreviewed and abandoned. Embedding Scout Agent directly in GitLab solved this. Teams can iterate on proposed solutions without context switching. To track improvement, we measure three distinct failure modes: categorization accuracy (should Scout attempt this ticket?), fixability assessment (does this need a code fix?), and solution quality (does the generated code actually work?). Each reveals different improvement opportunities. Today, Scout drives 40% of support's integration fixes, with expansion to engineering teams and downstream automation (testing, shipping, migration) as our next frontiers.

Speaker: Lisa Orr  |  Product Leader, Zapier
https://x.com/orreither
https://www.linkedin.com/in/lisaorr/

## What We Learned Deploying AI within Bloomberg’s Engineering Organization – Lei Zhang, Bloomberg

- Upload date: 2025-12-16
- Video: https://www.youtube.com/watch?v=Q81AzlA-VE8
- Transcript: raw/20251216_Q81AzlA-VE8/Q81AzlA-VE8.en-orig.vtt
- Metadata: raw/20251216_Q81AzlA-VE8/Q81AzlA-VE8.info.json

When it comes to using AI for software engineering, much of the spotlight falls on how large language models (LLMs) can write code—sometimes entirely from scratch. Countless studies highlight productivity gains from turning requirements directly into runnable code. But the reality of applying AI at scale inside a mature engineering organization is far more complex and nuanced. Over the past year, we’ve been on that journey at Bloomberg—integrating AI into the workflows of 9,000+ software engineers—and we’ve learned a few important lessons worth sharing:

Where the real ROI lies once you move beyond toy examples
What it takes to actually enable AI across a large, established engineering org
The best practices, cultural shifts, and guardrails that are required to make it work in practice
If you’re wondering what happens after the first demo magic fades and the real work begins, this talk is for you.

Speaker: Lei Zhang  |  Head of Technology Infrastructure Engineering, Bloomberg

Timestamps

00:00 Introduction to Bloomberg's Scale & Infrastructure 
03:32 AI for Coding: Initial Adoption & The "Greenfield" Drop-off 
06:14 Uplift Agents: Automating Refactoring & Maintenance 
08:40 Incident Response Agents: Unbiased Troubleshooting & Speed 
09:37 The "Paved Path": Standardizing AI Tool Building (MCP) 
11:51 Platform Components: Gateway, Discovery Hub, and Deployment 
13:34 Leveraging Training & Communities for Adoption 
16:15 The Leadership Gap & The Changing Cost Function of Engineering

## Coding Evals: From Code Snippets to Codebases – Naman Jain, Cursor

- Upload date: 2025-12-15
- Video: https://www.youtube.com/watch?v=tHN44yJoeS8
- Transcript: raw/20251215_tHN44yJoeS8/tHN44yJoeS8.en-orig.vtt
- Metadata: raw/20251215_tHN44yJoeS8/tHN44yJoeS8.info.json

AI coding capabilities have leapt from generating one-line snippets to competing entire codebases with agentic workflows. I’ll trace that arc focusing on learnings and challenges through each stage. I will start with early testable coding benchmarks distilling lessons about contamination and distributional overfitting. Next, moving beyond isolated programming problems, I will talk about repository grounded coding problems from SWE-bench style bug fixing, and R2E’s automated function completion setting. We’ll then move beyond isolated functions to longer-horizon tasks—runtime optimization (GSO), translation (Syzygy), and refactoring—highlighting challenges like test hacking, code quality, and idiomaticity. Finally, beyond code generation, I will talk about human preference evaluation in chatting (LMArena RepoChat) and developer-preference signals in-IDE via Copilot Arena.

Speaker:  Naman Jain  |  Engineering, Cursor
https://www.linkedin.com/in/naman1205jain/
https://x.com/StringChaos

## Building in the Gemini Era – Kat Kampf & Ammaar Reshi, Google DeepMind

- Upload date: 2025-12-15
- Video: https://www.youtube.com/watch?v=fgkXEIbZpGc
- Transcript: raw/20251215_fgkXEIbZpGc/fgkXEIbZpGc.en-orig.vtt
- Metadata: raw/20251215_fgkXEIbZpGc/fgkXEIbZpGc.info.json

A deep dive into the latest capabilities of Google DeepMind's Gemini 3 and the newly released "Nano Banana Pro" image model within Google AI Studio. Kat and Ammaar demonstrate "vibe coding"—a new paradigm where complex, aesthetic, and functional applications are built entirely through natural language prompts. They highlight how Gemini 3 excels at one-shot UI design and agentic tool use, while Nano Banana Pro integrates world knowledge and precise text rendering. The session concludes with live demos ranging from personalized comic books to a (mostly working) multiplayer racing game, emphasizing a future where software creation is democratized through full-stack AI runtime environments.

Timestamps
00:00 Intro & Gemini 3 Overview 
02:29 Nano Banana Pro Capabilities 
04:33 Vibe Coding in AI Studio 
07:13 Comic Book Demo: Text Rendering & Consistency 
10:33 Laptop Stickers Demo: Search Grounding 
12:00 "Anti-Gravity" & Ideating AI Studio Features 
13:42 3D Racing Game & Full Stack Runtime 
14:50 Live Multiplayer Demo Attempt
16:07 Democratizing Software & Closing Thoughts

Speakers:
• Kat Kampf  |  Product Manager, Google
https://x.com/kat_kampf
https://www.linkedin.com/in/kkampf/

• Ammaar Reshi  |  Product & Design Lead, Google
https://x.com/ammaar
https://www.linkedin.com/in/ammaarsreshi/
https://ammaar.me/

## From Vibe Coding To Vibe Engineering – Kitze, Sizzy

- Upload date: 2025-12-14
- Video: https://www.youtube.com/watch?v=JV-wY5pxXLo
- Transcript: raw/20251214_JV-wY5pxXLo/JV-wY5pxXLo.en-orig.vtt
- Metadata: raw/20251214_JV-wY5pxXLo/JV-wY5pxXLo.info.json

Web development has always moved in cycles of hype, from frameworks to tooling. With the rise of large language models, we're entering a new era of "vibe coding," where developers shape software through collaboration with Al rather than syntax. This talk explores what that means for the future of coding, especially in frontend development, and how it echoes the past while redefining what comes next.

Speaker: Kitze  |  Founder, Sizzy
https://x.com/thekitze

## Proactive Agents – Kath Korevec, Google Labs

- Upload date: 2025-12-13
- Video: https://www.youtube.com/watch?v=v3u8xc0zLec
- Transcript: raw/20251213_v3u8xc0zLec/v3u8xc0zLec.en-orig.vtt
- Metadata: raw/20251213_v3u8xc0zLec/v3u8xc0zLec.info.json

Speaker:  Kath Korevec  |  Director of Product, Google Labs
https://x.com/simpsoka
https://www.linkedin.com/in/kathleensimpson/

## Minimax M2: Building the #1 Open Model – Olive Song, MiniMax

- Upload date: 2025-12-13
- Video: https://www.youtube.com/watch?v=lY1iFbDPRlw
- Transcript: raw/20251213_lY1iFbDPRlw/lY1iFbDPRlw.en-orig.vtt
- Metadata: raw/20251213_lY1iFbDPRlw/lY1iFbDPRlw.info.json

Introducing Minimax's latest AI model and its applications in code generation.

Speaker:  Olive Song  |  Senior Researcher, MiniMax
https://x.com/olive_jy_song

## Moving away from Agile: What's Next – Martin Harrysson & Natasha Maniar, McKinsey & Company

- Upload date: 2025-12-12
- Video: https://www.youtube.com/watch?v=SZStlIhyTCY
- Transcript: raw/20251212_SZStlIhyTCY/SZStlIhyTCY.en-orig.vtt
- Metadata: raw/20251212_SZStlIhyTCY/SZStlIhyTCY.info.json

Most enterprises are not capturing much value from AI in software dev to date (at least relative to the potential). The reason is that most are adding AI tools to their dev teams without changing the people and operating model aspects (i.e., limited changes to ways of working, team configurations, role definitions, stage gates, etc.). Many core aspects of software development haven’t changed in the past 10+ years, and that’s holding us back from moving to the new paradigm of software development! We will share examples of what makes the difference.

https://www.linkedin.com/in/martinharrysson
https://www.linkedin.com/in/natasha-maniar-945276107/

## Hard Won Lessons from Building Effective AI Coding Agents – Nik Pash, Cline

- Upload date: 2025-12-12
- Video: https://www.youtube.com/watch?v=I8fs4omN1no
- Transcript: raw/20251212_I8fs4omN1no/I8fs4omN1no.en-orig.vtt
- Metadata: raw/20251212_I8fs4omN1no/I8fs4omN1no.info.json

Most of what’s written about AI agents sounds great in theory — until you try to make them work in production. The seductive ideas (multi-agent orchestration, RAG, prompt stacking) often collapse under real-world constraints. Why? Because they optimize for the wrong thing. In this talk, Nik Pash shares hard-won lessons from building large-scale coding agents at Cline — what failed, what survived, and why the next leap forward won’t come from clever scaffolds, but from evals and environments that truly measure and improve reasoning. Attendees will walk away with a clearer sense of what actually drives progress — and what’s just noise.

https://www.linkedin.com/in/nikpash

## The State of AI Code Quality: Hype vs Reality — Itamar Friedman, Qodo

- Upload date: 2025-12-11
- Video: https://www.youtube.com/watch?v=rgjF5o2Qjsc
- Transcript: raw/20251211_rgjF5o2Qjsc/rgjF5o2Qjsc.en-orig.vtt
- Metadata: raw/20251211_rgjF5o2Qjsc/rgjF5o2Qjsc.info.json

AI is making code generation nearly effortless, but the critical question remains: can we trust AI-generated code for software that truly matters? Has it really become easier to build robust, high-quality systems?

In this talk, we’ll separate hype from reality. Drawing on the State of AI Code Quality report, we’ll explore where AI tools excel, where they fall short, and which evaluation frameworks actually matter. We’ll unpack benchmarks, pitfalls, and lessons learned from deploying AI in real-world engineering workflows. Attendees will leave with a clearer understanding of how to measure, trust, and improve both AI-generated code and AI-driven code review—and what’s next for software quality in the age of AI.

Speaker: Itamar Friedman  |  CEO, Qodo
https://x.com/itamar_mar
https://www.linkedin.com/in/itamarf/

## Can you prove AI ROI in Software Eng? (Stanford 120k Devs Study) – Yegor Denisov-Blanch, Stanford

- Upload date: 2025-12-11
- Video: https://www.youtube.com/watch?v=JvosMkuNxF8
- Transcript: raw/20251211_JvosMkuNxF8/JvosMkuNxF8.en-orig.vtt
- Metadata: raw/20251211_JvosMkuNxF8/JvosMkuNxF8.info.json

You’re investing millions in AI for software engineering. Can you prove it’s paying off?

Benchmarks show models can write code, but in enterprise deployments ROI is hard to measure, easy to bias, and often distorted by activity metrics (PR counts, DORA) that say “more” without proving “better.”

Drawing on field data from 120k+ developers across 600+ companies, I’ll show exactly where AI helps the most and how to measure the ROI of your software engineering AI deployment.

We’ll unpack why identical tools deliver ~0% lift in some orgs and 25%+ in others.

You’ll leave with a step-by-step ROI playbook: what to track, the traps to avoid, and the habits top-quartile teams use to make the most from AI.

Speaker: Yegor Denisov-Blanch  |  Researcher, Stanford
https://x.com/yegordb
https://www.linkedin.com/in/ydenisov/

Timestamps

00:00 Introduction & Methodology: ML Panels of Experts 
00:21 The Research Approach: Time Series & Cross-Sectional Data 
01:38 Four Key Topics Overview 
02:01 Case Study: 10% Productivity Gain & The Widening Gap 
03:16 Factors Driving Performance: Usage vs. Quality 
04:02 The Environment Cleanliness Index 
05:30 Managing Codebase Entropy & AI Trust 
06:17 AI Engineering Practices Benchmark & Fingerprinting 
07:38 Case Study: Unequal Adoption Across Business Units 
08:31 Challenges in Measuring AI ROI via Business Outcomes 
10:28 Proposed Measurement Framework: Usage & Outcomes 
11:59 Metric Framework: Primary Output vs. Guardrails 
12:54 Case Study: AI Adoption's Negative Impact on Quality 
14:04 Rework, Refactoring, and Effective Output Analysis 
15:43 Conclusion & Call for Research Participation

## Agent Reinforcement Fine Tuning – Will Hang & Cathy Zhou, OpenAI

- Upload date: 2025-12-09
- Video: https://www.youtube.com/watch?v=p1CmPZ2j6Lk
- Transcript: raw/20251209_p1CmPZ2j6Lk/p1CmPZ2j6Lk.en-orig.vtt
- Metadata: raw/20251209_p1CmPZ2j6Lk/p1CmPZ2j6Lk.info.json

Deep dive into OpenAI's approach to reinforcement fine-tuning for code models.

https://x.com/willhang_
https://x.com/cathyzhou

AIE is coming to London and SF! see dates and sign up to be notified of sponsorships, CFPs, and tickets: https://ai.engineer

Timestamps:

00:00 Introduction to Agent RFT & What Defines an Agent 
01:45 Hierarchy of Agent Optimization (Prompting - Task Opt - RFT) 
02:53 New RFT Features: Public Endpoints & Custom Rewards 
03:55 Addressing Domain Shift & Latency via Exploration 
05:41 Recommended Workflow: Baseline First 
06:54 Case Study: Cognition (Code Editing & Parallelism) 
08:53 Case Study: Codto (Deep Research & Tail Latency) 
10:33 Case Study: Cosine (Enterprise Code & Strict Grading) 
12:50 Case Study: Macco (GPU Kernels & Reward Hacking) 
14:46 Four Principles for RFT Success

## Efficient Reinforcement Learning – Rhythm Garg & Linden Li, Applied Compute

- Upload date: 2025-12-09
- Video: https://www.youtube.com/watch?v=o15AaYl7Wu0
- Transcript: raw/20251209_o15AaYl7Wu0/o15AaYl7Wu0.en-orig.vtt
- Metadata: raw/20251209_o15AaYl7Wu0/o15AaYl7Wu0.info.json

Reinforcement learning (RL) is a powerful mechanism for building agents that are superhuman and specialized in particular tasks. At Applied Compute, RL is one of the fundamental building blocks that enables us to deliver automations and real business value for customers. Effective RL training often involves several iterative derisking runs to better understand learning dynamics with different base models, and then doing “hero” runs with the best configurations. If done naively, this can be very time-consuming and expensive. In this talk, we will discuss some ways our proprietary RL stack allows us to train models efficiently.

https://twitter.com/rhythmrg
https://twitter.com/lindensli

AIE is coming to London and SF! see dates and sign up to be notified of sponsorships, CFPs, and ticketsa: https://ai.engineer

## RL Environments at Scale – Will Brown, Prime Intellect

- Upload date: 2025-12-09
- Video: https://www.youtube.com/watch?v=_IzZWeuTx7I
- Transcript: raw/20251209__IzZWeuTx7I/_IzZWeuTx7I.en-orig.vtt
- Metadata: raw/20251209__IzZWeuTx7I/_IzZWeuTx7I.info.json

Scaling reinforcement learning environments for training advanced AI coding models.

https://twitter.com/willccbb

AIE is coming to London and SF! see dates and sign up to be notified of sponsorships, CFPs, and ticketsa: https://ai.engineer

## Don't Build Agents, Build Skills Instead – Barry Zhang & Mahesh Murag, Anthropic

- Upload date: 2025-12-08
- Video: https://www.youtube.com/watch?v=CEvIs9y1uog
- Transcript: raw/20251208_CEvIs9y1uog/CEvIs9y1uog.en-orig.vtt
- Metadata: raw/20251208_CEvIs9y1uog/CEvIs9y1uog.info.json

In the past year, we've seen rapid advancement of model intelligence and convergence on agent scaffolding. But there's still a gap: agents often lack the domain expertise and specialized knowledge needed for real-world work. We think Skills are the solution—a minimal form factor for packaging procedural knowledge that agents can dynamically load. It's a portable, composable approach to giving one agent capabilities across domains. In this talk, we'll share how we built Skills at Anthropic, the network effects we're observing, and where we believe this leads: agents writing their own Skills from experience. Our thesis: equipping agents for real-world work means building reusable expertise.

Barry: https://twitter.com/barry_zyj
Mahesh: https://twitter.com/MaheshMurag

## VoiceVision RAG - Integrating Visual Document Intelligence with Voice Response — Suman Debnath, AWS

- Upload date: 2025-12-06
- Video: https://www.youtube.com/watch?v=hwCmfThIiS4
- Transcript: raw/20251206_hwCmfThIiS4/hwCmfThIiS4.en-orig.vtt
- Metadata: raw/20251206_hwCmfThIiS4/hwCmfThIiS4.info.json

In this workshop we will explore the integration of Colpali, a cutting-edge Vision based Retrieval Model, with voice synthesis for next-generation RAG systems. We'll demonstrate how Colpali's ability to generate multi-vector embeddings directly from document images bypasses traditional OCR and complex preprocessing, while adding voice output creates a more intuitive and accessible user experience. Attendees will see how this combination handles documents with mixed textual and visual information, leading to more efficient and accurate information retrieval with natural voice responses.

## Government Agents: AI Agents Meet Tough Regulations — Mark Myshatyn, Los Alamos National Lab

- Upload date: 2025-12-06
- Video: https://www.youtube.com/watch?v=TnSGx36Ly0Q
- Transcript: raw/20251206_TnSGx36Ly0Q/TnSGx36Ly0Q.en-orig.vtt
- Metadata: raw/20251206_TnSGx36Ly0Q/TnSGx36Ly0Q.info.json

Lightning talk given at the 2025 AI Engineer World's Fair. https://www.linkedin.com/in/markmyshatyn/

## 2026: The Year The IDE Died — Steve Yegge & Gene Kim, Authors, Vibe Coding

- Upload date: 2025-12-06
- Video: https://www.youtube.com/watch?v=7Dtu2bilcFs
- Transcript: raw/20251206_7Dtu2bilcFs/7Dtu2bilcFs.en-orig.vtt
- Metadata: raw/20251206_7Dtu2bilcFs/7Dtu2bilcFs.info.json

As AI has grown more capable, software developers around the world have lagged behind the technology advances, and have consistently eschewed the most powerful tools. In this talk I explore why devs are staying 9-12 months behind the AI curve. I'll share a preview of what 2026's AI coding tools will be like, and paint a vision of where we go from here.

Speakers:
* Steve Yegge  |  Engineering Leader, Sourcegraph/Amp
https://x.com/Steve_Yegge
https://www.linkedin.com/in/steveyegge/

* Gene Kim  |  Author & Researcher, IT Revolution
https://x.com/RealGeneKim
https://www.linkedin.com/in/realgenekim/
http://www.realgenekim.me/

## Future-Proof Coding Agents – Bill Chen & Brian Fioca, OpenAI

- Upload date: 2025-12-05
- Video: https://www.youtube.com/watch?v=wVl6ZjELpBk
- Transcript: raw/20251205_wVl6ZjELpBk/wVl6ZjELpBk.en-orig.vtt
- Metadata: raw/20251205_wVl6ZjELpBk/wVl6ZjELpBk.info.json

Coding agents are becoming one of the most active areas in applied AI, yet many teams keep rebuilding fragile infrastructure every time models or providers change. We believe there is a better way. By anchoring on a stable abstraction layer like Codex, we can stop worrying about harness rewrites and focus on the parts of the stack that create lasting value. We treat models as interchangeable sub-agents, plug into shared primitives, and let upstream improvements flow through without breaking products. This lets teams move faster, stay resilient as the ecosystem evolves, and focus their energy on domain-specific workflows and user experience.

Speakers:
- https://twitter.com/bfioca
- https://twitter.com/realchillben

AIE is coming to London and SF! see https://ai.engineer for dates and sign up to be notified!
\**Timestamps:**

00:00 Introduction & The State of Coding Agents
02:06 Anatomy of a Coding Agent & The "Harness" Definition
03:44 Technical Challenges in Building Harnesses
06:03 Intelligence vs. Habit: Lessons in Prompt Engineering
08:24 Deep Dive: Codeex as a Harness/Agent
10:33 Computer Use & Terminal Capabilities
11:25 Patterns for Building with the Codeex SDK
14:32 Case Studies: GitHub & Cursor Integration
15:34 Future of Coding Agents & Conclusion

## Katelyn Lesse – Evolving Claude APIs for Agents, Anthropic

- Upload date: 2025-12-04
- Video: https://www.youtube.com/watch?v=aqW68Is_Kj4
- Transcript: raw/20251204_aqW68Is_Kj4/aqW68Is_Kj4.en-orig.vtt
- Metadata: raw/20251204_aqW68Is_Kj4/aqW68Is_Kj4.info.json

Developers are building more and more complex, long-running, agentic systems. Learn how the Anthropic team is evolving the Claude Developer Platform to enable developers to get the best outcomes from Claude.

## No Vibes Allowed: Solving Hard Problems in Complex Codebases – Dex Horthy, HumanLayer

- Upload date: 2025-12-02
- Video: https://www.youtube.com/watch?v=rmvDxxNubIg
- Transcript: raw/20251202_rmvDxxNubIg/rmvDxxNubIg.en-orig.vtt
- Metadata: raw/20251202_rmvDxxNubIg/rmvDxxNubIg.info.json

It seems pretty well-accepted that AI coding tools struggle with real production codebases. At AI Engineer 2025 in June, The Stanford study on AI's impact on developer productivity found:

A lot of the ""extra code"" shipped by AI tools ends up just reworking the slop that was shipped last week.

Coding agents are great for new projects or small changes, but in large established codebases, they can often make developers less productive.

The common response is somewhere between the pessimist ""this will never work"" and the more measured ""maybe someday when there are smarter models.""

After several months of tinkering, we've found that you can get really far with today's models if you embrace core context engineering principles.

This isn't another ""10x your productivity"" pitch. I tend to be pretty measured when it comes to interfacing with the ai hype machine. But we've stumbled into workflows that leave me with considerable optimism for what's possible. We've gotten claude code to handle 300k LOC Rust codebases, ship a week's worth of work in a day, and maintain code quality that passes expert review. We use a family of techniques I call ""frequent intentional compaction"" - deliberately structuring how you feed context to the AI throughout the development process.
 
In this talk, I'll share what we've learned since first sharing these techniques back in August, and some educated predictions on what's coming in the next 6-12 months for software engineers.

Speaker: twitter.com/dexhorthy

Timestamps:
00:00 intro: complex code
01:40 context engineering
02:53 advanced context
04:38 context obsession
05:55 dumb zone concept
07:26 context management
09:37 complex problem solved
10:45 semantic diffusion
12:14 onboarding agents ‍
13:57 internal docs lies
15:03 mental alignment key
16:12 code snippet plans
17:38 don't outsource think
18:45 rpi: smart zone
19:46 cultural change hard ‍‍

Hey - I'm Dex, and I'm hacking on getting AI coding agents to solve hard problems in complex codebases at HumanLayer. Before this I was working on APIs for agent orchestration and Human-in-the-Loop, and wrote the April 2025 essay "12 factor agents" that first coined the term Context Engineering. I've been coding since high school, when I built tools for NASA researchers to navigate the south pole of the moon. Enjoyer of tacos and burpees (not necessarily in that order).

## Building Cursor Composer – Lee Robinson, Cursor

- Upload date: 2025-12-02
- Video: https://www.youtube.com/watch?v=fL1iJHtl51Q
- Transcript: raw/20251202_fL1iJHtl51Q/fL1iJHtl51Q.en-orig.vtt
- Metadata: raw/20251202_fL1iJHtl51Q/fL1iJHtl51Q.info.json

Learn about the infrastructure, training, and evaluations used to build Cursor Composer, our first coding model. (https://cursor.com/blog/2-0)

Speaker: https://x.com/leerob

AIE is coming to London and SF! see https://ai.engineer for dates and sign up to be notified!

**Timestamps**

00:00 Introduction to Cursor Composer
01:10 The "Fast vs. Smart" Trade-off
03:17 System Architecture & Tooling
04:33 Scaling Challenges: Consistency & Burstiness
05:50 Infrastructure Solutions & Custom Kernels
08:12 Co-designing Cloud Agents & Training Infra
09:39 The Power of Semantic Search
11:00 Results: Parallelism & Agent Behavior
12:13 The "Airplane Wi-Fi" Analogy
13:36 Key Reflections & Conclusion

## Defying Gravity - Kevin Hou, Google DeepMind

- Upload date: 2025-12-02
- Video: https://www.youtube.com/watch?v=HN-F-OQe6j0
- Transcript: raw/20251202_HN-F-OQe6j0/HN-F-OQe6j0.en-orig.vtt
- Metadata: raw/20251202_HN-F-OQe6j0/HN-F-OQe6j0.info.json

Why we built Google Antigravity, and discussing the future of agentic IDEs with Gemini 3.

Speaker: https://x.com/kevinhou22

AIE is coming to London and SF! see dates and sign up to be notified of sponsorships, CFPs, and tickets: https://ai.engineer

**Timestamps:**

00:00 Intro & Anti-gravity Launch
01:26 Anti-gravity Product Overview (Three Surfaces)
02:16 Agent Manager & Editor Integration
03:13 Agent-Controlled Browser & Context Retrieval
05:51 Philosophy: Model Capabilities Driving Product Paradigms
07:03 Four Categories of Improvements (Intelligence, Tools, Long-running, Multimodal)
08:31 Computer Use & Visual Verification
11:18 Image Generation & Design Iteration
12:26 The "Artifacts" Interaction Pattern
16:51 Artifacts for Memory, Notifications, & Feedback
20:34 The Research-Product Flywheel
23:35 Closing Remarks

## Music from AIE Code Summit - Instrumentals

- Upload date: 2025-11-27
- Video: https://www.youtube.com/watch?v=xAfp-znTRx8
- Transcript: raw/20251127_xAfp-znTRx8/xAfp-znTRx8.en-orig.vtt
- Metadata: raw/20251127_xAfp-znTRx8/xAfp-znTRx8.info.json

By popular demand, we are releasing our music from the livestream + venue stage -- the instrumental tracks. Comment below if you want to see the vocal tracks released!

## The Unbearable Lightness of Agent Optimization — Alberto Romero, Jointly

- Upload date: 2025-11-24
- Video: https://www.youtube.com/watch?v=zfvEMNmVlNY
- Transcript: raw/20251124_zfvEMNmVlNY/zfvEMNmVlNY.en-orig.vtt
- Metadata: raw/20251124_zfvEMNmVlNY/zfvEMNmVlNY.info.json

This talk introduces Meta-ACE, a learned meta-optimization framework that dynamically orchestrates multiple strategies (context evolution, adaptive compute, hierarchical verification, structured memory, and selective test-time parameter adaptation) to maximize task performance under real-world constraints. Rather than relying on uniform prompt refinement, Meta-ACE profiles each task (complexity, verifiability, feedback quality) and selects an optimal strategy bundle via a lightweight meta-controller.

Alberto is a seasoned AI and ML leader with over 20 years of experience at the intersection of AI and data. A hands-on engineer, Alberto has designed and built low-latency, mission-critical ML systems, and has specialized in systematic optimization of AI pipelines and agents using custom built evaluation techniques. He is an exited co-founder having sold his previous startup, Humn.ai, to Aon in 2023, which delivered real-time, ML-powered risk prediction for mobility. Alberto is the Co-founder and CTO at Jointly, specializing in self-optimizing AI agents for regulated industries.

He holds an MSc in AI and Machine Learning and speaks at global AI conferences, including ODSC and AIAI.

---
Socials:
- LinkedIn: https://www.linkedin.com/in/albertoromero-uk/
- GitHub: https://github.com/a-romero
- Company: Jointly (https://getjointly.ai)

## Backlog.md: Terminal Kanban Board for Managing Tasks with AI Agents — Alex Gavrilescu, Funstage

- Upload date: 2025-11-24
- Video: https://www.youtube.com/watch?v=zMXKhhwiCIc
- Transcript: raw/20251124_zMXKhhwiCIc/zMXKhhwiCIc.en-orig.vtt
- Metadata: raw/20251124_zMXKhhwiCIc/zMXKhhwiCIc.info.json

Never leave your terminal to create and manage tasks for your AI agents. Backlog.md stores all your tasks as Markdown files in your Git repo. By exposing the main workflows and commands as MCP tools, your AI agents will know how to take tasks from "To Do" to "Done," and you will no longer run out of context window or miss important requirements in any of your features.

Alex Gavrilescu leads backend & web engineering at Funstage GmbH in Vienna, keeping millions of free‑to‑play gamers happily tapping. He still ships code, tinkers with Raspberry Pi Kubernetes clusters for fun, and is passionate about weaving project‑management smarts with practical AI. Most recently he created Backlog.md, a micro‑tool that turns side‑project chaos into shippable tasks.

---
Socials:
- LinkedIn: https://www.linkedin.com/in/alexandrugavrilescu
- X (Twitter): https://x.com/H3xx3n
- GitHub: https://github.com/MrLesk
- Website: https://mrlesk.com/
- Company: Funstage GmbH (https://funstage.com/)

## Agents are Robots Too: What Self-Driving Taught Me About Building Agents — Jesse Hu, Abundant

- Upload date: 2025-11-24
- Video: https://www.youtube.com/watch?v=qqXdLf3wy1E
- Transcript: raw/20251124_qqXdLf3wy1E/qqXdLf3wy1E.en-orig.vtt
- Metadata: raw/20251124_qqXdLf3wy1E/qqXdLf3wy1E.info.json

In this talk, I break down the surprising parallels between robotics and agents: embodiment, statefulness, simulation, and more. The main lesson from self-driving: everyone thought perception was hard and planning was easy. It took 8-10 years to learn we had it backwards. We're seeing the same pattern with agents today. Predictive models aren't action models. Perfect reasoning doesn't guarantee good execution.

And just like in robotics, the company with the best infrastructure wins—not just the one with the best model. Whether you're building agents, training models, or just trying to understand why production agents are so hard, this talk covers the concepts from robotics (DAgger, MDPs, simulation, offline RL) that directly apply to making agents work at scale.

Jesse has spent the last 10 years as an ML engineer, starting from research in computer vision and NLP, to working on deep learning and two-tower embedding recommender systems at YouTube, to transformer-based planning models for self-driving at Waymo. He is currently working on bringing large-scale RL and simulation techniques to coding agents at Abundant.

---
Socials:
- LinkedIn: https://www.linkedin.com/in/jessehu
- GitHub: http://github.com/huyouare
- Company: Abundant (https://abundant.ai)

## Vision: Zero Bugs — Johann Schleier-Smith, Temporal

- Upload date: 2025-11-24
- Video: https://www.youtube.com/watch?v=qLqttdO33UM
- Transcript: raw/20251124_qLqttdO33UM/qLqttdO33UM.en-orig.vtt
- Metadata: raw/20251124_qLqttdO33UM/qLqttdO33UM.info.json

Software with zero bugs sounds absurd, or even impossible, in anything but simple situations, but it has been built. For example, NASA's Space Shuttle software achieved near-perfection (1 error per 420,000 lines) using rigorous engineering practices. This feat was achieved decades ago, yet cost prevented the techniques used from becoming mainstream.

This talk traces seventy years of innovation in software quality and programmer productivity, ranging from structured programming to formal verification. While many of these techniques have been too costly to implement on a large scale, AI changes that. What is more, agentic coding needs them to compensate for its limitations.

We are on the verge of a world where aerospace-level reliability becomes the practical in a broad range of applications.

Johann Schleier-Smith is Technical Lead for AI at Temporal Technologies, the leading provider of durable execution. He previously founded Crystal DBA, which developed agents to manage cloud infrastructure and was acquired by Temporal. He also co-founded if(we), which built a collection of social networks with over 300 million members and was acquired by The Meet Group (NASDAQ:MEET). Johann serves on the board of Sama, a leading provider of training data for computer vision applications. He holds a Ph.D. in Computer Science from UC Berkeley and an A.B. in Physics and Mathematics from Harvard University.

---
Socials:
- LinkedIn: https://www.linkedin.com/in/jssmith/
- X (Twitter): https://x.com/jssmith
- GitHub: https://github.com/jssmith
- Website: https://johann.schleier-smith.com/
- Company: Temporal Technologies (https://temporal.io/)

## Compilers in the Age of LLMs — Yusuf Olokoba, Muna

- Upload date: 2025-11-24
- Video: https://www.youtube.com/watch?v=q2nHsJVy4FE
- Transcript: raw/20251124_q2nHsJVy4FE/q2nHsJVy4FE.en-orig.vtt
- Metadata: raw/20251124_q2nHsJVy4FE/q2nHsJVy4FE.info.json

Python is where ideas start—but it isn't where portable, low-latency software ends. In this talk, I'll show how we use LLMs inside a constrained, verifiable compiler pipeline to turn plain Python functions into self-contained native binaries that run anywhere (cloud, desktop, mobile & web); and how our customers use this technology to run open-source AI models locally and in the cloud with the familiar OpenAI client experience.

Yusuf Olokoba is the founder of Muna, specializing in code generation for AI inference workloads. He previously co-founded a real estate technology startup, backed by First Round Capital and Bessemer, which was later acquired. He holds patents in computer vision and augmented reality, powering augmented reality experiences used by millions of users. Yusuf holds a B.A. in computer science from Dartmouth College and is an alumnus of South Park Commons.

---
Socials:
- LinkedIn: https://www.linkedin.com/in/olokobayusuf/
- X (Twitter): https://x.com/olokobayusuf
- GitHub: https://github.com/olokobayusuf
- Company: Muna (https://muna.ai)

## Developing Taste in Coding Agents: Applied Meta Neuro-Symbolic RL — Ahmad Awais, CommandCode

- Upload date: 2025-11-24
- Video: https://www.youtube.com/watch?v=kWOQS3XPZ10
- Transcript: raw/20251124_kWOQS3XPZ10/kWOQS3XPZ10.en-orig.vtt
- Metadata: raw/20251124_kWOQS3XPZ10/kWOQS3XPZ10.info.json

Your coding agent writes code like an LLM bot. CommandCode writes code like me.

Every developer has a coding agent now. What if your coding agent actually had taste? What if it understood not just what you're building, but how you like to build it? Your weird naming conventions. Your obsession with early returns. That thing you do where you always extract utilities before they get messy. Your coding taste.

I've been building coding agents since Greg Brockman gave me GPT-3 access in 2020. Started as a CLI tool I used every day. Five years later, we've deployed over 350K agents through Langbase, and I've learned something crucial: the best agents don't just write code—they develop taste.

In this talk, I'll share what we've learned about building agents that actually feel like they know you. We'll dive into the architecture patterns that make this possible: contextual memory systems, preference learning loops, and what I call "engineering intuition"—going way beyond the typical "agents.md" approach.

It's about building agents that evolve with you, remember your decisions, and start making choices that feel like your own. By the end, you'll understand how to build coding agents that can develop taste. It's battle-tested insights from one of the largest deployment of AI agents in production today.

Ahmad Awais is an award-winning open-source engineering leader, founder & CEO of Langbase.com (AI Cloud powering 350K+ AI agents), Creator of CommandCode.ai. NASA Mars Ingenuity Helicopter mission code-contributor. Angel investor. Ex-VP DX, Google Developers Advisory Board founding member and Board Member Linux Foundation & OpenAPI Initiative. Ahmad has authored various open-source software tools used by millions of developers worldwide, like his Shades of Purple code theme (4M Dev Users), corona-cli (10+ Billion Requests), and now Langbase (1.2Billion/mo agent runs). He’s a Google Devs Expert and 5x recipient of the 8th GitHub Stars Gold award.

---
Socials:
- LinkedIn: https://www.linkedin.com/in/MrAhmadAwais/
- X (Twitter): https://x.com/_AhmadAwais
- GitHub: https://github.com/AhmadAwais
- Website: https://AhmadAwais.com/about
- Company: CommandCode.ai | Langbase (https://commandcode.ai)

## From Stateless Nightmares to Durable Agents — Samuel Colvin, Pydantic

- Upload date: 2025-11-24
- Video: https://www.youtube.com/watch?v=flf_IKnFYnE
- Transcript: raw/20251124_flf_IKnFYnE/flf_IKnFYnE.en-orig.vtt
- Metadata: raw/20251124_flf_IKnFYnE/flf_IKnFYnE.info.json

Building production AI agents reveals a harsh truth: stateless architectures that work for simple demos become impossibly painful at scale. When long-running workflows fail, you lose all compute, progress, and user trust.
This is why companies like OpenAI use Temporal for products like Deep Research—to build durable agents that recover from failures instead of forcing users to start over.

In this talk, you'll learn how to:
- Build resilient AI agents that survive crashes and resume from checkpoints
- Implement durable execution with PydanticAI and Temporal
- Gain production-grade observability with Pydantic Logfire and Evals
- Compose multi-agent systems that handle failures gracefully
- Stop burning money on failed agent runs that restart from scratch

We'll walk through real code examples, including a Deep Research implementation that demonstrates how proper architecture turns fragile prototypes into production-ready systems.

Links:
- Demo code on GitHub: https://github.com/pydantic/pydantic-stack-demo/tree/main/durable-exec
- Pydantic AI Documentation: https://ai.pydantic.dev/
- Temporal Integration Guide: https://ai.pydantic.dev/durable_execution/temporal/
- Pydantic Logfire Docs: https://logfire.pydantic.dev/docs/

Samuel Colvin is a Python and Rust expert. His work has redefined data validation and observability for developers. His Pydantic library powers 350M+ downloads every month, serving as a core dependency for OpenAI SDK, Anthropic SDK, LangChain, LlamaIndex, and countless other GenAI projects.

---
Socials:
- LinkedIn: https://www.linkedin.com/company/pydantic/
- X (Twitter): https://x.com/pydantic
- GitHub: https://github.com/pydantic
- Website: NA
- Company: Pydantic (https://pydantic.dev)

## Enterprise Deep Research: The Next Killer App for Enterprise AI — Ofer Mendelevitch, Vectara

- Upload date: 2025-11-24
- Video: https://www.youtube.com/watch?v=fh9LgKXBGnQ
- Transcript: raw/20251124_fh9LgKXBGnQ/fh9LgKXBGnQ.en-orig.vtt
- Metadata: raw/20251124_fh9LgKXBGnQ/fh9LgKXBGnQ.info.json

Conversational AI has already proven itself as the first high-ROI enterprise AI application. But the real frontier lies beyond chat with high-value, document-centric workflows that still consume countless human hours. Enterprise Deep Research brings the power of web-scale research workflows into the private domain of your company’s data. By applying autonomous, multi-step reasoning to internal knowledge bases, enterprises can unlock transformative use cases: from drafting investment memos in financial services to automating RFP responses and due diligence. In this talk, we’ll learn what Enterprise Deep Research is, how it works, and see some example use-cases.

Ofer Mendelevitch leads developer relations at Vectara. He has extensive hands-on experience in machine learning, data science and big data systems across multiple industries, and has focused on developing products using large language models since 2019. Prior to Vectara he built and led data science teams at Syntegra, Helix, Lendup, Hortonworks and Yahoo! Ofer holds a B.Sc. in computer science from Technion and M.Sc. in EE from Tel Aviv university, and is the author of "Practical data science with Hadoop" (Addison Wesley), and of the upcoming "Hands-on RAG for production" (O'Reilly)

---
Socials:
- LinkedIn: https://www.linkedin.com/in/ofermend/
- X (Twitter): https://x.com/ofermend
- GitHub: https://github.com/ofermend
- Company: Vectara (https://vectara.com)

## What Data from 20m Pull Requests Reveal About AI Transformation — Nick Arcolano, Jellyfish

- Upload date: 2025-11-24
- Video: https://www.youtube.com/watch?v=WqZq8L-v9pA
- Transcript: raw/20251124_WqZq8L-v9pA/WqZq8L-v9pA.en-orig.vtt
- Metadata: raw/20251124_WqZq8L-v9pA/WqZq8L-v9pA.info.json

Engineering teams are spending millions on AI coding tools, but most have no idea what's actually working. Without hard data, you're flying blind – unable to tell which teams are actually using AI effectively. But what if you had access to workflow data from 200,000 engineers and 20 million pull requests across a thousand companies?

In this talk, we'll share insights from usage data spanning the entire AI engineering ecosystem. We've observed significant productivity gains at scale, including a 2x increase in PR throughput and 24% faster cycle times on average.

You'll learn what "good" adoption looks like (hint: autonomous agents aren't there yet), what productivity gains are possible, and what side effects to expect. More importantly, we'll explore why some teams don't see these gains. We'll show how your code architecture" is a critical, often overlooked factor.

---
Socials:
- LinkedIn: https://www.linkedin.com/in/arcolano/
- X (Twitter): https://x.com/arcolano
- GitHub: https://github.com/arcolano
- Company: Jellyfish (https://jellyfish.co)

## AI Copilots for Tech Architecture: The Highest-ROI Use Case You’re Not Building — Boris B., Catio

- Upload date: 2025-11-24
- Video: https://www.youtube.com/watch?v=QRWdapxMdSY
- Transcript: raw/20251124_QRWdapxMdSY/QRWdapxMdSY.en-orig.vtt
- Metadata: raw/20251124_QRWdapxMdSY/QRWdapxMdSY.info.json

AI copilots have already changed the game in software development. But the most strategic, highest-leverage use case is still overlooked: tech architecture decision-making. Architecture decisions drive hundreds of millions in technology spend, whether tech fuels business objectives—or slows them down, and ultimately decide whether companies stay modern-by-design or get left behind in insurmountable technical debt. Yet most organizations still manage these choices with spreadsheets, tribal knowledge, and gut instinct. In this talk, we'll explore why architecture copilots represent the next frontier beyond coding assistants—and why getting this right is where ROI is truly won or lost.

Drawing from closed-door CTO discussions and our work with enterprises and growth-stage tech companies, we'll examine three critical challenges keeping leaders up at night: achieving visibility across their entire tech estate so they're not flying blind; getting expert advice and recommendations on how to prioritize tech roadmaps based on highest impact to business objectives; and enabling autonomous developer guidance so that developers are empowered with tailor-fit expertise as they pursue their workflow while also keeps them adhering to leadership strategy and governance.

To solve this, we’ll share what it takes to build a true architecture copilot (based on work with Catio customers across $1B+ enterprises and growth-stage companies): understanding messy systems, implicit knowledge, and constantly shifting dependencies for holistic live visibility; curating the right context around company goals and architecture excellence to inform AI recommendations that truly optimize the architecture; and defining the workflow fabric that powers teams with tailor-fit designs and expert advice while adhering to organizational standards and strategy for true autonomous decision-making.

We’ll close with a look at what this unlocks: a centralized Hub for Architecture and Tech Decision-making that transforms how companies strategically plan, build, and evolve their tech estate—not simply execute more lines of code. You'll walk away with a new lens on AI strategy: one that reframes copilots not just as coding productivity enhancers, but as strategic levers for competitive advantage, staying best-in-class-by-design, and high-ROI tech outcomes.

Boris is the Co-Founder and CEO of Catio, a platform for cloud native architecture evaluation, planning, and evolution, with the help of AI. Boris is a serial entrepreneur and over the prior five years founded and lead Siden through growth to 60 people and to becoming a leader in distributed edge compute. Siden uses compute / caching placed in homes, AI to predict home content consumption, and proactive content distribution to refresh caches 24x7 using underutilized wireless network capacity. Siden uses a SaaS model to partner with wireless operators to materially expand their network capacity for Home Internet (by 2-5x), enabling them to win the Home Internet market globally (forecasted to reach 1B homes by 2032 by Qualcomm). Over his career, Boris grew 5 high caliber start-ups in total as a product-minded leader, and also funded companies from Series A to growth stages as a venture capital and private equity investor. Boris graduated the Management and Technology Program at the University of Pennsylvania with degrees from the Wharton School and School of Engineering and is a listed inventor on 15 patents.

---
Socials:
- LinkedIn: https://www.linkedin.com/in/borisbogatin/
- X (Twitter): https://x.com/borisbogatin
- Company: Catio (https://catio.tech)

## Infra that fixes itself, thanks to coding agents — Mahmoud Abdelwahab, Railway

- Upload date: 2025-11-24
- Video: https://www.youtube.com/watch?v=Q5IVm_CxN2w
- Transcript: raw/20251124_Q5IVm_CxN2w/Q5IVm_CxN2w.en-orig.vtt
- Metadata: raw/20251124_Q5IVm_CxN2w/Q5IVm_CxN2w.info.json

This talk shows how we built Railway Autofix, a plug-in template you can drop into any Railway project to monitor your infrastructure, and open PRs with fixes when issues are detected. We use OpenCode as our coding agent, as well as Inngest for durable execution

The final code will be live at https://github.com/m-abdelwahab/railway-autofix

Mahmoud Abdelwahab is a Software Engineer who works at the intersection of Product, Marketing, Education and Community. He loves building over-engineered demos and playing around with the latest technologies.

---
Socials:
- LinkedIn: https://linkedin.com/in/thisismahmoud
- X (Twitter): https://x.com/thisismahmoud
- GitHub: https://github.com/m-abdelwahab
- Company: Railway (https://railway.com)

## Context Platform Engineering to Reduce Token Anxiety — Val Bercovici, WEKA

- Upload date: 2025-11-24
- Video: https://www.youtube.com/watch?v=NTBX-wxUhHs
- Transcript: raw/20251124_NTBX-wxUhHs/NTBX-wxUhHs.en-orig.vtt
- Metadata: raw/20251124_NTBX-wxUhHs/NTBX-wxUhHs.info.json

Context Platform Engineering is the set of skills and tools to design, size, and configure systems optimized for Agent Swarm Context, at any scale.

“KV-cache hit rate is the single most important metric for a production-stage AI agent“ according to Manus AI. Context platform engineering simplifies the maximization of KV Cache hit rates.

This talk covers WEKA’s new open source context platform engineering toolkit, which helps translate Service Level Agreement (SLA) requirements of AI Agents, into Agent+LLM inference platform Service Level Objectives (SLOs) which meet required SLAs.

We present research results from WEKA Labs which provide new observability into both unit, and aggregate KV Cache hit rates, consumed by agent swarms of various leading AI coding agents.

This talk concludes with benchmark results for sizing agent swarm context for arbitrary working sets. Including context window sizes, latency, concurrency, and throughput SLOs per agent unit (swarm or sub-task) across modern GPU memory hierarchies, supporting KV Cache offloading plug-ins like vLLM/LMCache, SGLang HiCache, and NVIDIA Dynamo KVBM/NIXL.

Callan Fox is the product leader for Context Platforms at WEKA, following a series of technical expertise and leadership roles at Dell/EMC, CGI and HPE.
Val Bercovici is the Chief AI Officer at WEKA. Previously he was CTO of NetApp/SolidFire, and founding governing board member of the Kubernetes CNCF in the Linux Foundation.

---
Resources:
- https://www.linkedin.com/pulse/visual-guide-how-ai-agents-use-inference-inside-llm-callan-fox-q9brc
- https://medium.com/@callan.j.fox/evaluating-management-of-kv-cache-within-an-inference-system-2d7c3d266c3a
- https://www.linkedin.com/pulse/importance-context-platform-engineering-callan-fox-i81wc/

---
Socials:
- LinkedIn: https://www.linkedin.com/in/valentinbercovici
- X (Twitter): https://x.com/AccBalanced
- GitHub: https://github.com/weka/LMCache
- Website: https://www.weka.io/product/augmented-memory-grid/
- Company: WEKA (https://weka.io)

## Context Engineering: Connecting the Dots with Graphs — Stephen Chin, Neo4j

- Upload date: 2025-11-24
- Video: https://www.youtube.com/watch?v=LLuKshphGOE
- Transcript: raw/20251124_LLuKshphGOE/LLuKshphGOE.en-orig.vtt
- Metadata: raw/20251124_LLuKshphGOE/LLuKshphGOE.info.json

AI systems need more than intelligence; they need context. Without it, even the most advanced models can misinterpret information, lose track of details, or arrive at conclusions that don’t hold up. Context engineering is emerging as a discipline that shapes how AI perceives, recalls, and reasons about information.

This talk will explore how context provides the foundation for reasoning, problem solving, and explainability in AI. We will look at techniques such as connected memory, contextual retrieval, and graph-based knowledge representation that give large language models a more reliable way to connect information and draw logical conclusions.

Attendees will come away with a practical understanding of how to design effective context pipelines that align AI with real-world knowledge and user intent, and why context engineering is becoming a central part of building trustworthy and impactful AI systems.

Stephen Chin is VP of Developer Relations at Neo4j, conference chair of the LF AI & Data Foundation, and author of numerous titles including the upcoming GraphRAG: The Definitive Guide for O'Reilly. He has given keynotes and main stage talks at numerous conferences around the world including AI Engineer Summit, AI DevSummit, Devoxx, DevNexus, JNation, JavaOne, Shift, Joker, swampUP, and GIDS. Stephen is an avid motorcyclist who has done evangelism tours in Europe, Japan, and Brazil, interviewing developers in their natural habitat. When he is not traveling, he enjoys teaching kids how to do AI, embedded, and robot programming together with his daughters.

---
Socials:
- LinkedIn: https://linkedin.com/in/steveonjava
- X (Twitter): https://x.com/steveonjava
- GitHub: https://github.com/steveonjava
- Company: Neo4j (https://neo4j.com)

## The Cure for the Vibe Coding Hangover — Corey J. Gallon, Rexmore

- Upload date: 2025-11-24
- Video: https://www.youtube.com/watch?v=JsKTQbT58BY
- Transcript: raw/20251124_JsKTQbT58BY/JsKTQbT58BY.en-orig.vtt
- Metadata: raw/20251124_JsKTQbT58BY/JsKTQbT58BY.info.json

Download the slides, soundtrack and other resources from this talk at: https://vibecodinghangover.com

Inspiration strikes! You fire up your favorite AI coding agent and tell it "Build me an app that..." The agent grinds away, furiously, and spits back a torrent of code and it works! You’re a masterful rebel in the AI revolution!

But, then, you want to change something. You want to add a feature. You want to evolve it to production software; or, perhaps you come back to it a week later. You realize you don't understand it, can't maintain it, and have to throw most or all of it all away.

"Vibe Coding" is the low-spec, zero-planning approach to AI accelerated development that feels productive but results in brittle, unmaintainable demoware. The hangover is the resulting despair when you try to build maintainable, understandable software this way. The cure is building software with AI coding agents by applying this framework.

You’ll love this talk if:

- You value programming as a daily learning experience.
- You want to understand and own this software as you do all of the other software that you write.
- You want to be the boss of the coding agents, not their confused intern.
- Working with AI coding agents makes you feel like a prompt jockey, no longer an AI engineer.
- You're sick of throwing away code, burning time and tokens.
- You want to use coding agents to build production applications that do real work.

We'll walk through a practical framework - comprising a set of Principles, a Process, and Tools - that enables AI engineers to build, own, and maintain complex, real-world software applications using AI coding agents. This is not a conceptual framework, it is applied. It has been distilled and simplified from years of engineering work in the trenches of building software with AI coding agents. This framework has been taught and implemented across many teams, and has transformed the productivity of AI engineers in companies from solo shops to Fortune 500. We'll focus on the first crucial phase of software development: "Make it Work,” with clear ties to apply the framework to the remaining phases of “Make it Right” and “Make it Fast”.

00:00 The Vibe Coding Hangover
01:24 Introduction
03:31 The Framework - Overview
04:52 Principles
16:46 Process - Overview
17:28 Process - Planning
38:26 Process - Implementation
48:29 Tools
56:10 The Morning After

Corey J. Gallon is Head of an AI-native holding company and a battle-hardened AI engineer with a focus on building real, scaled software with AI coding agents. He is an AI coding agents OG, building coding agents since 2022 and one of the most significant contributors to GPT-Engineer (evolved into the startup Lovable). He was formerly Chief Innovation Officer, designer and leader of development of a large consulting firm's enterprise-scale AI coding agents platform. Corey is founding faculty of a university graduate AI & ML program, an artisan of specialty coffee, and a pickleball fanatic.

---
Socials:
- LinkedIn: https://www.linkedin.com/in/coreygallon
- X (Twitter): https://x.com/coreygallon
- GitHub: https://github.com/captivus
- Website: https://gallon.me
- Company: Rexmore (https://rexmore.ai)

## Hacking Subagents Into Codex CLI — Brian John, Betterup

- Upload date: 2025-11-24
- Video: https://www.youtube.com/watch?v=5eJqXtevlXg
- Transcript: raw/20251124_5eJqXtevlXg/5eJqXtevlXg.en-orig.vtt
- Metadata: raw/20251124_5eJqXtevlXg/5eJqXtevlXg.info.json

Subagents are amazing tools for managing context, among other things. But Codex CLI doesn't have them. Let's change that!

Brian John is a Principal Full Stack Engineer with over a decade of experience in technology. He is currently working on using AI to help his R&D team members ship faster and with higher quality.

---
Socials:
- LinkedIn: https://linkedin.com/in/brianjohn
- X (Twitter): https://x.com/brianpjohn
- GitHub: https://github.com/f1sherman
- Website: https://blog.brianjohn.com
- Company: Betterup (https://betterup.com)

## AI changes *Nothing* — Dax Raad, OpenCode

- Upload date: 2025-11-23
- Video: https://www.youtube.com/watch?v=o3gmwzo-Mik
- Transcript: raw/20251123_o3gmwzo-Mik/o3gmwzo-Mik.en-orig.vtt
- Metadata: raw/20251123_o3gmwzo-Mik/o3gmwzo-Mik.info.json

Everyone says AI changes everything. Dax Raad argues that when it comes to building a winning product, AI changes nothing.

In this contrarian talk, Dax breaks down why the fundamental challenges of product success: marketing, onboarding, and retention remain stubbornly human problems that AI cannot solve. He argues that while AI can generate content, it cannot generate cool. While it can write code, it cannot design the deep primitives required for long term retention.

Key Takeaways:
- Marketing is about Cool: You need to create things that people feel compelled to share. AI is too corny to help you here.
- The "Aha" Moment: You must ruthlessly eliminate friction to get users to the singular moment they understand your product. This requires deep, opinionated taste, not algorithmic optimization.
- Primitives over Features: To retain power users, you must build deep primitives first and simple experiences second. AI cannot hallucinate the right mental model for your problem space.

Winning still requires hard work, deep taste, and human ingenuity. And that's a good thing.

Dax Raad is a core contributor to SST, the framework that makes it easy to build serverless applications. He is a well-known voice in the developer community, advocating for better developer experiences and honest product thinking.

---
Socials:
- X (Twitter): https://x.com/thdxr
- GitHub: https://github.com/thdxr
- Website: https://thdxr.com/
- Company: OpenCode (https://opencode.ai)

Timestamps from the comments (thanks!)
- 0:00 — Introduction to Open Code, a fully open-source coding agent
- 0:43 — Why AI isn't going to make you a winner: the unchanging fundamentals of product success
- 1:39 — The product funnel framework: three critical moments that determine success
- 2:18 — Marketing: creating ideas people want to share organically
- 6:38 — The aha moment: ruthlessly eliminating friction to get users to product clarity
- 10:46 — Retention: balancing simplicity for new users with advanced features for power users
- 14:46 — Closing: why execution difficulty remains constant despite AI capabilities

## Z.ai GLM 4.6: What We Learned From 100 Million Open Source Downloads — Yuxuan Zhang, Z.ai

- Upload date: 2025-11-22
- Video: https://www.youtube.com/watch?v=m6MF1OR_9kM
- Transcript: raw/20251122_m6MF1OR_9kM/m6MF1OR_9kM.en-orig.vtt
- Metadata: raw/20251122_m6MF1OR_9kM/m6MF1OR_9kM.info.json

GLM 4.6 is the only open-source model currently tied for #1 on the LMSYS Chatbot Arena, standing shoulder-to-shoulder with GPT-4o and Claude 3.5 Sonnet. In this talk, Zhang Yuxuan from zAI breaks down the technical roadmap that led to over 100 million downloads across the GLM family.

Zhang deep dives into the specific training recipes behind GLM 4.6, including their move to single-stage Reinforcement Learning (RL), the "SLIME" RL framework for handling complex agent trajectories, and how they structured 15 trillion tokens of pre-training data. If you are building AI Agents or training LLMs, this breakdown offers a rare look inside the architecture of a frontier-class open-source model.

In this video, we cover:

The Data Recipe: How zAI filters 15T tokens, moves to repo-level code contexts, and integrates agentic reasoning data.

SLIME Framework: A look at the hybrid synchronous/asynchronous architecture used to train agents without bottlenecking GPU clusters.

RL Lessons: Why zAI abandoned multi-stage RL in favor of single-stage training to preserve long-context capabilities.

GLM 4.5V: How native resolution processing improves UI navigation and video understanding.

Timestamps:
0:00 - Introduction & The GLM Ecosystem
0:55 - 100 Million Downloads & Open Source Roadmap
03:22 - Tying GPT-4o on LMSYS Arena
05:04 - The Training Pipeline: From Pre-training to Long Context
07:54 - Introducing SLIME: Efficient RL for Agents
11:08 - The "Two-Stage" Curriculum Strategy
11:57 - Why Single-Stage RL beats Multi-Stage RL
12:55 - Token-Weighted Loss for Coding
14:13 - GLM 4.5V: Multimodal & Video Understanding
16:07 - Deployment: vLLM, SGLang, and Hugging Face
18:06 - Coding Assistants & Future Plans

Zhang Yuxuan has recently started a PhD at the University of Liverpool and is currently working at Z.ai. zR (Zhang) is passionate about open-source initiatives and strives for deeper exploration in this realm. Their primary activities include the following: Engaged in research on models such as GLM-4.5 (https://arxiv.org/abs/2508.06471), GLM-4.5V (https://arxiv.org/abs/2507.01006), CogVideoX (https://arxiv.org/abs/2408.06072), CogAgent (https://arxiv.org/abs/2312.08914); researching the capabilities of model Agents and the integration with Agent frameworks such as langchain-chatchat (https://github.com/chatchat-space/Langchain-Chatchat), chatpdf (https://github.com/CosmosShadow/gptpdf); participated in several national competitions, such as RoboMaster and National Students' SmartCar Competition, and achieved some results, including national awards. These competitions have been truly fascinating. Enjoys hackathon competitions and welcomes teaming up for these events.

---
Socials:
- LinkedIn: https://www.linkedin.com/in/yuxuan-zhang-86a124282/
- X (Twitter): https://x.com/zRdianjiao
- GitHub: https://github.com/zRzRzRzRzRzRzR
- Website: https://huggingface.co/ZHANGYUXUAN-zR
- Company: Z.ai (https://z.ai)

## Rishabh Garg, Tesla Optimus — Challenges in High Performance Robotics Systems

- Upload date: 2025-08-25
- Video: https://www.youtube.com/watch?v=bCGbuyv8PMk
- Transcript: raw/20250825_bCGbuyv8PMk/bCGbuyv8PMk.en-orig.vtt
- Metadata: raw/20250825_bCGbuyv8PMk/bCGbuyv8PMk.info.json

A robot's behavior is influenced by the control policy, the software configuration, and electrical characteristics of the communication protocol.

When unexpected behaviors arise, it is not straightforward to root cause them to the RL policy, electrical characteristics, mechanical characteristics. This talk walks through some of these issues and explains what might cause the observed behavior.

We will talk about concrete issues that audience will be able to take away from and develop their understanding of physical systems. It will build intuition for what kind of issues to expect when communication data rates increase manifold.

Timestamps
00:00 Introduction to high-performance robotics challenges
00:15 The problem of unexplained robot behavior
00:54 Root cause analysis: policy vs. software
01:17 Designing a toy robotics system for analysis
01:24 System architecture: sensors, CPU, GPU, actuators, CAN bus
01:57 The initial, simple code loop
02:14 Expectation vs. reality: unexpected loop execution gaps
02:42 The impact of CAN bus data rate on loop execution
03:13 Potential solutions: accepting delay vs. multithreading
04:00 A new, pipelined design for reduced cycle time
04:32 New problems: "stuttering" and abnormal motor behavior
04:49 Data collection with external transceivers and "candump"
05:24 Expected vs. actual message plots: missed messages and jitter
06:12 Using cycle time plots to identify desynchronization
06:58 Transmit phase desynchronization: missed and queued data
08:03 Receive phase desynchronization: stale data and overcompensation
08:38 Resolving synchronization issues: kernel primitives and padding
09:25 The impact of logging on system performance
11:09 Reception and priority inversion
12:02 Conclusion and summary of key takeaways

Rishabh Garg
Robotics Engineer at Tesla Optimus

I am Rishabh Garg, a robotics software engineer pushing the boundaries of software hardware integration to meet the ever increasing demand for data. I have been working with robots and embedded systems for the past 4 years, making systems more reliable and performant at companies like Tesla and Amazon. Eager to learn what experts in the industry are doing differently and share my own experience and insights into the challenges frequently encountered at the system software level for robotics.

## Building an Agentic Platform — Ben Kus, CTO Box

- Upload date: 2025-08-24
- Video: https://www.youtube.com/watch?v=12v5S1n1eOY
- Transcript: raw/20250824_12v5S1n1eOY/12v5S1n1eOY.en-orig.vtt
- Metadata: raw/20250824_12v5S1n1eOY/12v5S1n1eOY.info.json

Explore the technical evolution of metadata extraction at Box and how it shaped the foundation of our AI platform. We’ll walk through our transition to an agentic-first design—why it was necessary, how we approached the rebuild, challenges we encountered along the way, and the advantages it unlocked.

Timestamps
00:00 Box's Content Platform and Enterprise Focus
01:50 Initial AI Deployment in 2023
02:54 The Challenge of Unstructured Data in Enterprises
03:56 Limitations of Pre-Generative AI Data Extraction
04:54 First Version: LLM-Based Extraction
07:05 Challenges with the Pure LLM Approach
08:58 Despair and the Need for a New Architecture
09:30 Introducing Agentic Architecture
10:04 AI Agent Reasoning Framework
10:45 Agentic Routine for Data Extraction
12:28 Advantages of Agentic Architecture
14:05 Key Lesson Learned: Build Agentic Architecture Early
18:37 Approach to Fine-tuning and Model Support

Ben Kus
CTO

Ben Kus is the Chief Technology Officer at Box and is responsible for developing Box’s technology vision and strategy and ensuring that technological resources are aligned with the company's business needs. Previously Ben was the VP of Product Management at Box. Before joining Box, Ben was the Co-Founder and CTO of Subspace, Inc., an enterprise security solution that was acquired by Box. Ben has held various leadership positions, including the role of Chief Architect for IBM, and Senior Director of Technology for BigFix, Inc. Ben studied Computer Science at the University of California, Berkeley.

## Perceptual Evaluations: Evals for Aesthetics — Diego Rodriguez, Krea.ai

- Upload date: 2025-08-23
- Video: https://www.youtube.com/watch?v=h5ItAJuB3Fc
- Transcript: raw/20250823_h5ItAJuB3Fc/h5ItAJuB3Fc.en-orig.vtt
- Metadata: raw/20250823_h5ItAJuB3Fc/h5ItAJuB3Fc.info.json

Special session with KREA.ai's cofounder Diego Rodriguez on how evals for aesthetics and image/generative media work — the hardest kinds of evals.

  linkedin.com/in/asciidiego/

Timestamps
00:15 Introduction to Perceptual Evaluations
00:50 The Problem with Current AI Evaluations
02:16 Historical Context and Compression
05:14 Limitations in AI and Human-centric Metrics
08:00 Rethinking Evaluation and the Future of AI
12:44 Evaluating Our Evaluations
13:32 Krea's Role and Call to Action

## Five hard earned lessons about Evals — Ankur Goyal, Braintrust

- Upload date: 2025-08-23
- Video: https://www.youtube.com/watch?v=a4BV0gGmXgA
- Transcript: raw/20250823_a4BV0gGmXgA/a4BV0gGmXgA.en-orig.vtt
- Metadata: raw/20250823_a4BV0gGmXgA/a4BV0gGmXgA.info.json

The main thesis of the video is that building successful AI applications requires a sophisticated engineering approach that goes beyond simply writing good prompts. The speaker argues for the importance of evaluations (evals) as a core component of the development process, highlighting that they should be intentionally engineered to reflect real-world user feedback and drive product improvements. The video also introduces the concept of "context engineering" as the new frontier, where the focus is on optimizing the entire context provided to the model, including tool definitions and their outputs. Ultimately, the speaker advocates for a flexible, model-agnostic architecture that can quickly adapt to the rapidly evolving landscape of AI models.

Timestamps:

00:00 Introduction to 5 Lessons in AI Product Development
00:19 Lesson 1: Effective Evals Speak for Themselves
02:09 Lesson 2: Great Evals Need to Be Intentionally Engineered
04:03 Lesson 3: Context Engineering is the New Prompt Engineering
06:37 Lesson 4: Be Prepared for a New Model to Change Everything
09:09 Lesson 5: Optimize the Entire Evaluation System, Not Just the Prompts
12:21 Recap of the Five Lessons

## How BlackRock Builds Custom Knowledge Apps at Scale — Vaibhav Page & Infant Vasanth, BlackRock

- Upload date: 2025-08-23
- Video: https://www.youtube.com/watch?v=08mH36_NVos
- Transcript: raw/20250823_08mH36_NVos/08mH36_NVos.en-orig.vtt
- Metadata: raw/20250823_08mH36_NVos/08mH36_NVos.info.json

Investment Operations teams are the backbone of asset and investment management firms. Their day-to-day work not only enables portfolio managers to respond swiftly to market events but also ensures that complex, unstructured data flows seamlessly across the organization.
In this talk, we introduce a modular, Kubernetes-native AI framework purpose-built to scale custom Knowledge Apps across the enterprise. Designed with speed, flexibility, and compliance in mind, the framework empowers teams to launch production-grade document extraction applications in minutes instead of months, unlocking new levels of automation and efficiency for investment management workflows.
We’ll also share how this framework has helped BlackRock streamline document extraction processes, generate investment signals, reduce operational overhead, and accelerate the delivery of high-impact business use cases—all while maintaining the robustness and control required in a regulated industry.

00:30 Introduction to BlackRock's AI Initiatives
01:31 Classifying AI Applications
02:22 Use Case: New Issue Operations
03:59 Challenges with Scaling AI Knowledge Apps
07:02 Architecture of BlackRock's AI Framework
08:32 Demonstration of the Sandbox
15:52 Key Takeaways from the Discussion

Vaibhav Page
Principal Engineer

Vaibhav is a Principal Engineer at BlackRock, where he leads the development of the Data Science and AI platform powering
investment research and automation across the firm. Vaibhav is also the author of Argo-Events, a CNCF-graduated project widely used for event-driven automation in cloud-native environments.

Infant Vasanth
Senior Director of Engineering

Infant Vasanth leads the engineering team responsible for the Studio Compute Platform, BlackRock's analytics and automation platform that enables our users to conduct research & analysis, run automations and distribute research at scale.
In addition, Infant is also leading the Data & AI Acceleration team focusing on efforts to enhance Aladdin Studio's AI capabilities along side the Operational AI capabilities(prospectus analyzer, operational agents etc.)

## Multi Agent AI and Network Knowledge Graphs for Change — Ola Mabadeje, Cisco

- Upload date: 2025-08-22
- Video: https://www.youtube.com/watch?v=m0dxZ-NDKHo
- Transcript: raw/20250822_m0dxZ-NDKHo/m0dxZ-NDKHo.en-orig.vtt
- Metadata: raw/20250822_m0dxZ-NDKHo/m0dxZ-NDKHo.info.json

Traditional ticketing and testing workflows for change management and network operations often operate independently and lack critical real-world context and adaptive decision making capabilities. This fragmented approach results in delayed resolutions, repeated incidents, escalations, and dissatisfied stakeholders.

This session explores an innovative solution leveraging the synergy of natural language processing from IT Service Management (ITSM) systems, Multi-agent reasoning, and dynamic context derived from live knowledge network graphs. Attendees will gain insights into an end-to-end architecture where natural language intents from ITSM tickets seamlessly integrate with experts AI agents for complex workflow tasks, supported by continuous network knowledge graph ingestion pipelines.

Through a detailed production case study, we will demonstrate how Agentic reasoning combined with dynamic network knowledge graph contexts significantly improves critical validation and workflow interactions. The showcased results will highlight dramatic improvements in ticket resolution efficiency, accuracy of network testing, and overall execution quality, delivering tangible value to both technical teams and business stakeholders.

## Fuzzing in the GenAI Era — Leonard Tang, Haize Labs

- Upload date: 2025-08-22
- Video: https://www.youtube.com/watch?v=OMGPvW8TBHc
- Transcript: raw/20250822_OMGPvW8TBHc/OMGPvW8TBHc.en-orig.vtt
- Metadata: raw/20250822_OMGPvW8TBHc/OMGPvW8TBHc.info.json

"Evaluation" is one of those concepts that every AI practitioner vaguely knows is important, but few practitioners truly understand. Is "eval" the dataset for measuring the quality of your AI system? Is "eval" the measure, the metric of quality? Is "eval" the process of human annotation and scoring? Or is "eval" a third-party dataset run once to benchmark a model?

To mitigate this cacophony, this talk will provide an opinionated and principled perspective for what we actually mean when we say “evaluation”, beyond the traditional for-loop-over-a-static dataset.

In particular, this perspective draws heavy inspiration from *fuzzing*, i.e. bombarding AI with simulated, unexpected user inputs to uncover corner cases at scale. This factors into sub-problems regarding:

- Quality Metric. What is the actual criteria we, as humans, are using to determine if an AI system is producing good or bad responses? How do we elicit these criteria before the human SME can articulate them? How do we, as efficiently as possible, operationalize this criteria with an automated *Judge*?

- Stimuli Generation. Given a metric, how do we know, with confidence, that an AI system is performing well with respect to the metric? What data is representative and sufficient for discovering all potential bugs of an AI system? And how do we generate this complex, diverse, faithful data at scale?

We will discuss in detail the philosophy, technology, and case studies behind both problems of Quality Metric and Stimuli Generation, and how they interact in concert.

Timestamps
00:00 Introduction to Haizing
01:16 The "Last Mile Problem" in AI
02:47 The Brittleness of GenAI Applications
03:54 Examples of Brittle Chatbots
04:29 Inadequacy of Standard Evaluation Methods
06:09 Haizing: Simulating the Last Mile
08:43 Scaling Evaluation with Agents as Judges
09:29 Verdict: Accuracy vs. Latency
11:47 Scaling Evaluation with RL-Tuned Judges
14:06 Fuzzing vs. Adversarial Testing in AI
14:37 Simulation as Prompt Optimization
16:23 Case Study: Haizing a Major European Bank's AI App
17:05 Case Study: Haizing a F500 Bank's Voice Agents
17:46 Case Study: Scaling Voice Agent Evals with Verdict

Leonard Tang
Founder & CEO

I am the co-founder and CEO of Haize Labs, where we are solving the ultimate extant problem in AI: ensuring its reliability, quality, and alignment for any application. You might also know of us for our red-teaming work.

Prior, I studied math and computer science at Harvard. My research then covered adversarial robustness, math reasoning, computational neuroscience, interpretability, and large(-ish) language models. Much of that has now been distilled into the Haize technology agenda. I also dropped out of, before starting, a Stanford PhD in computer science.

In the limit of my life, I am chiefly invested in starting Bell Labs 2.0.

## Form factors for your new AI coworkers — Craig Wattrus, Flatfile

- Upload date: 2025-08-22
- Video: https://www.youtube.com/watch?v=CiMVKnX-CNI
- Transcript: raw/20250822_CiMVKnX-CNI/CiMVKnX-CNI.en-orig.vtt
- Metadata: raw/20250822_CiMVKnX-CNI/CiMVKnX-CNI.info.json

Designing user experiences for AI means moving beyond traditional interfaces.

Designers are grappling with how to create intuitive and effective interactions for these new AI capabilities, while growing their practice to include philosophy, ethics and coding.

What if AI interactions could be reimagined as new 'coworkers'? This talk explores AI systems as your new coworkers. Covering novel UX patterns we’ve implemented and are researching at Flatfile as well as a state of the union on emergent patterns we’re seeing and using from the industry.

Attendees will get a peek into explorations into AI cursors, forward-leaning chat paradigms and tool UX. We will discuss both work thats in production today at some of our biggest customers as well as thought-provoking demos, offering a vision for the future of AI UX.

Timestamps

00:25 Design Engineering: Form Factors for your new AI coworkers
01:04 Four main categories of AI stack: invisible, ambient, inline, and conversational
02:14 Invisible AI: Personalized demos
03:06 Ambient AI: Analyzing data for opportunities
03:10 Inline AI: Direct data manipulation
03:46 Shifting from helicopter parent to character coach
04:32 The "chat tuner" tool
05:20 Feeling the material of AI
08:20 Finding the grain in AI design
11:08 Courting emergence
11:48 Example of emergence: Combining datasets and generating reports
12:37 Example of emergence: Suggesting human intervention
14:09 Eyes on the future
14:27 "Auto-complete" for data transformations





---

Craig Wattrus
AI Design Engineer

Craig Wattrus is a product designer and technologist working at the edge of human-computer interaction and AI. He designs and codes at Flatfile, where he’s leading a product called AI Transform. He's building adaptive data systems that use agentic AI to automate complex workflows across Fortune 500 companies. With a background in both computer science and design, Craig’s work focuses on shaping new UX patterns for AI systems that observe, learn, and act alongside users not just for them.

Craig is deeply interested in rethinking form factors for AI, exploring how designers can create new patterns of interaction that feel more collaborative, contextual, and adaptive. His approach blends practical, production-ready work with speculative design exploration with working PoC's offering a grounded yet forward-looking take on what AI-native UX can become. When he’s not dreaming up new ideas or testing AI behaviors in production, he’s probably making lamps, tinkering with small-scale hardware, or enjoying a perfect espresso.

## Wisdom-Driven Knowledge Augmented Generation at Scale - Chin Keong Lam, Patho AI

- Upload date: 2025-08-22
- Video: https://www.youtube.com/watch?v=9AQOvT8LnMI
- Transcript: raw/20250822_9AQOvT8LnMI/9AQOvT8LnMI.en-orig.vtt
- Metadata: raw/20250822_9AQOvT8LnMI/9AQOvT8LnMI.info.json

The main thesis of the video is that by using a Wisdom-Driven Knowledge Graph, we can significantly enhance the quantitative analysis capabilities of Knowledge-Augmented Generation (KAG) systems. This allows for the creation of smarter AI systems that can not only retrieve information but also understand, reason, and provide expert-level advice. The talk argues that this approach surpasses traditional Retrieval-Augmented Generation (RAG) systems, which primarily rely on unstructured vector search.

00:00 Introduction to Patho AI and KAG
01:09 Defining Knowledge and Knowledge Graphs
01:56 KAG vs. RAG
02:37 The Wisdom-Decision Making-Situation Diagram
06:26 Practical Application: Competitive Analysis Chatbot
08:37 Implementation with N8n and Multi-Agent System
11:37 Why Use Knowledge Graphs over RAG
14:01 Challenges with Vector RAG and Numerical Reasoning
15:34 Building KAG Systems and Hybrid Models
16:45 Graph Extraction and Benchmarks
17:42 Conclusion and Resources

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

## The Next Unicorns: 7 Top AI startups from the HF0 Residency

- Upload date: 2025-08-21
- Video: https://www.youtube.com/watch?v=L8-5ezsoI5A
- Transcript: raw/20250821_L8-5ezsoI5A/L8-5ezsoI5A.en-orig.vtt
- Metadata: raw/20250821_L8-5ezsoI5A/L8-5ezsoI5A.info.json

HF0's Demo Days are usually hilariously oversubscribed and have never before been aired publicly. For the first time, they are joining the AIE stage to pitch AI Engineers.

https://www.hf0.com/

Timestamps

00:15 Diego Rodriguez - Krea
03:02 OpenHome
06:09 Josh - Coframe
07:31 Eugene - Featherless AI
10:39 Jonas Bauer - Upside
13:48 Lengyue - OpenAudio
18:48 Alex Atallah - OpenRouter
