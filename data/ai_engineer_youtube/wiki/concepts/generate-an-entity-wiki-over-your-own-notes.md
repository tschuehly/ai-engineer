# Generate an Entity Wiki Over Your Own Notes

Summary: Above a folder of raw notes, have an agent generate a second layer organized by *entities* — people, concepts, organizations, sources — scoped to a focus area you name, with links back down to the raw material. The entities are the browsable index the raw notes never had.

Use when:
- A note corpus has grown past the point where chronological or folder organization helps.
- You need "everyone I met with," "every concept in this research area," or "every source I cited" as first-class pages rather than as a search you re-run.
- Reading unfamiliar material where the hard part is keeping track of who and what, not what you thought about it.

Details:
- Provenance: the idea comes from a gist by Andrej Karpathy (captioned "Andre Carpathy") — "this is where the LLM knowledge base idea kind of came together. You can find this really easily now if you just search his name and then wiki." The speaker notes Karpathy "even calls this an idea," i.e. a starting point to tweak, not a spec. ([LLM Knowledge Bases](../sources/20260812_I3bpdgFJCUY.md), 11:40-12:16)
- The principle in one sentence: "We want to take a raw directory… and we want to combine it into whatever focus area that we care about. So, we grab the raw sources, we create a wiki." The prompt that produced his AI wiki was as plain as that: "these are the things that I care about. They're in this raw folder. Here's the rest of his gist. Go ahead and generate a wiki for me." (11:53-12:26)
- The output is an entity index — "a set of people, places, and things basically": sources, topics, concepts, people, organizations. Some entries are ones you would predict; some are the point. His AI-news wiki surfaced "a Ralph loop rabbit hole" as a concept and Adam Neely, "a jazz musician that's been talking about how AI has affected the music industry," as a person, pulled in from an AI-and-music tangent he had dictated once and forgotten. (10:08-11:27)
- Focus-area scoping is what keeps the layer coherent: the wiki is generated *for a stated interest* over the whole raw folder, not as one wiki over everything. He runs several — "latest in AI news" alongside one over a Bible-in-a-Year podcast — each with its own entity set from the same underlying notes. (10:08-10:14, 12:31-12:40)
- The clearest value case is unfamiliar domains where entity tracking is the actual work: on the podcast wiki, the material was "totally outside of my wheelhouse with a number of characters that I forget the name of," where "all the names sound very similar and can be hard to pronounce," so "having something that can pull together all the people with references to what each of them did is very useful" — one generated entry per character. (12:31-13:00)
- The workplace form is direct: "If you take a lot of meeting notes and you want to have a people section of all the people they met with, interested clients if you're in customer success, it can generate all of those for you. And then it can create back links over to any related meetings you've had with them. Maybe the source links," so a reader can descend from an entity page to the meetings and then to the raw note. (13:00-13:24)
- Why generate rather than curate, stated as a time argument rather than a quality one: "all of that is generated programmatically. I didn't write any of this because all I have time to do is generate the raw ingredients not connecting it all together myself." (11:27-11:37)
- This is a *derivative* layer, and the wiki's other sources agree on that architecture: raw sources stay immutable, the generated layer sits above them, and every entry links back. Towards AI's product build used the same three-folder shape (`raw`, a generated index, an LLM-written `wiki`) crediting the same Karpathy idea; the research-wiki concept adds a cheapest-first read path over the same structure. What differs here is the consumer — Holmes optimizes the layer for a *human* clicking through, which is the case the measured null result on agentic browsing does not cover. See [Build a File-Based Research Wiki With Progressive-Disclosure Retrieval](file-based-research-wiki-with-progressive-disclosure-retrieval.md) and [Measure Agentic Knowledge-Base Browsing Before Adding It](measure-agentic-knowledge-base-browsing-before-adding-it.md).
- Open operational question the source leaves untouched: the wiki is regenerated on a schedule over notes that keep arriving, and nothing is said about what happens to a generated entry you edited by hand, or about entity merging when the same person appears under two spellings.

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Build a File-Based Research Wiki With Progressive-Disclosure Retrieval](file-based-research-wiki-with-progressive-disclosure-retrieval.md)
- [Materialize Backlinks at Ingest With Key-Term Search](materialize-backlinks-at-ingest-with-key-term-search.md)
- [Measure Agentic Knowledge-Base Browsing Before Adding It](measure-agentic-knowledge-base-browsing-before-adding-it.md)
- [Optimize Capture Bandwidth Before Note Organization](optimize-capture-bandwidth-before-note-organization.md)
- [Personal Knowledge Bases Become Agent Context Substrates](personal-knowledge-bases-become-agent-context-substrates.md)
- [Knowledge graphs make agent memory traversable and explainable](knowledge-graphs-make-agent-memory-traversable-and-explainable.md)

Sources:
- [LLM Knowledge Bases: a practical guide — Ben Holmes, Warp](../sources/20260812_I3bpdgFJCUY.md), 09:56-13:24
