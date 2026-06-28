# AI Engineering Bootcamp — Course Handbook

*Version 1.0 · June 2026 · Flagship Project: ANIMA*

---

> This file is the single source of truth for the bootcamp. Every phase, chapter, rule, and expectation lives here. Any AI model resuming this course must read this document before teaching.

---

## I. VISION

This is a six-month journey from software engineer to production AI engineer. The vehicle is ANIMA — an open-source AI character engine with genuine persistent memory, evolving personality, and autonomous behavior. Every chapter builds toward shipping ANIMA 1.0 as a production system that other developers can star, fork, and extend.

The learning experience is structured like an RPG: chapters are quests, phases are dungeons, boss battles test cumulative mastery, and every completed chapter earns XP toward the final title of AI Engineer.

---

## II. PHILOSOPHY

1. **Never skip prerequisites.** Every concept needed to understand a topic is taught before that topic. Nothing is "out of scope."

2. **Every concept earns its place.** Decorators aren't taught abstractly — they're taught because ANIMA's plugin system uses them. Every topic has a direct application to the project.

3. **No shortcuts on fundamentals.** For every concept: why it exists → what problem it solves → how it works internally → real-world analogy → code examples → common mistakes → industry usage → interview questions.

4. **Code review at staff engineer level.** Assignments are reviewed for architecture, naming, readability, complexity, scalability, performance, edge cases, security, testability, and maintainability.

5. **Understand before you call.** The OpenAI API isn't called until transformers are understood. RAG isn't built until embeddings are internalized. Tools are used only after their foundations are taught.

6. **Build in public.** Everything ships to GitHub. Every chapter advances the ANIMA repository. By Phase 10, the portfolio is already impressive.

7. **The quiz rule.** Quiz answers are never revealed until the student submits theirs. There is no advancing past a quiz unanswered.

8. **One chapter at a time.** No chapter is started until the previous assignment is submitted and reviewed.

---

## III. STUDENT PROFILE

**Background:**
- CS degree (probability, linear algebra, data structures, algorithms, systems)
- Software engineering experience (REST APIs, backend development, databases, Git, Docker)
- Python fundamentals (variables, control flow, functions, classes, basic OOP)

**What can be compressed:**
- Python syntax and basic OOP → Phase 1 focuses only on advanced patterns
- HTTP/REST → Phase 14 (FastAPI) covers the framework, not the protocol
- SQL basics → Phase 14 focuses on production patterns and schema design
- Docker basics → Phase 16 focuses on AI-specific multi-container orchestration
- Git and CI/CD → no basic coverage needed, jumps straight to AI pipeline patterns

**What is genuinely new — full depth, no compression:**
- Advanced Python patterns specific to AI frameworks (decorators, generators, async at scale, type system, Protocols)
- Machine learning architecture and theory beyond CS intro
- Neural networks, backpropagation, and transformer architecture
- LLM internals, inference, and production API patterns
- Embeddings and the geometry of semantic space
- Vector databases and approximate nearest-neighbor search
- RAG architecture and advanced retrieval strategies
- AI agent systems, tool use, and orchestration
- Multi-agent coordination and emergent behavior
- LLM evaluation frameworks and benchmarking
- AI-specific observability and cost management
- Fine-tuning (LoRA, QLoRA, supervised fine-tuning)
- AI security and adversarial robustness

**Target:** 24 weeks at 2–3 hours/day (~6 months)

---

## IV. THE FLAGSHIP PROJECT: ANIMA

### What ANIMA Is

ANIMA is an open-source, production-quality framework for creating AI characters with:

- **Genuine persistent memory** — every conversation, fact, and event is semantically indexed and retrievable across unlimited time
- **Evolving personality** — character traits drift based on accumulated experience (modeled, not hallucinated)
- **Autonomous behavior** — characters pursue goals between conversations using agent architectures
- **Multi-character dynamics** — characters form relationships, build history, and create emergent narratives with each other
- **Knowledge grounding** — characters are built on real knowledge bases (RAG over any document corpus)
- **Production architecture** — FastAPI, PostgreSQL, Redis, Pinecone, Docker, CI/CD, cloud deployment

### Why ANIMA Was Chosen

Nobody has built this at production quality as open source. The README demo is immediately compelling: create a character, have ten conversations over two weeks, then ask on day fifteen "do you remember what you said about your fear of heights?" She does. In character. Grounded in her knowledge base. That five-second demo gets shared.

Target GitHub audiences: game developers (NPC AI), fiction writers (character development tools), AI researchers (emergent social behavior), customer service engineers (memory-persistent agents). These four communities don't overlap — each independently contributes to star count and forks.

The name ANIMA is Latin for *soul* and *animating principle* — precisely what the project builds into every character.

### ANIMA Evolution by Phase

| Phase | Milestone | What the Character Engine Gains |
|-------|-----------|--------------------------------|
| 1 | Core Python architecture | Type-safe codebase, plugin hooks via decorators, async core for concurrent character thinking |
| 2 | Knowledge ingestion pipeline | Parses any document corpus (PDF, HTML, JSON) into structured character knowledge |
| 3 | Personality classifier | ML model for tracking conversation tone and personality state vectors |
| 4 | Embedding-aware architecture | Understanding of why character-specific semantic search works at the model level |
| 5 | Dialogue generation engine | LLM-powered in-character responses with streaming support |
| 6 | Persona prompt system | Structured prompts encoding personality, current mood, active memories, relationship context |
| 7 | Memory encoding pipeline | Every experience embedded into semantic vector space |
| 8 | Persistent memory store | Long-term memory in Pinecone/Chroma — characters remember across unlimited sessions |
| 9 | Memory retrieval system | Hybrid search for the most relevant character memories given any conversation topic |
| 10 | Knowledge-grounded dialogue | RAG ensures characters don't hallucinate their own knowledge |
| 11 | Autonomous character behavior | Characters take actions, use tools, initiate behavior without prompting |
| 12 | Multi-character dynamics | Characters interact, form relationships, create emergent narratives |
| 13 | Long-term planning | Characters pursue multi-session goals; persistent relationship memory between characters |
| 14 | ANIMA REST API | External developers can create characters, have conversations, query memories |
| 15 | Evaluation framework | Character consistency scoring, persona red-teaming, regression testing |
| 16 | Cloud deployment | ANIMA accessible via public API with proper auth and rate limiting |
| 17 | Observability stack | Memory growth tracking, personality drift metrics, cost dashboard, anomaly alerts |
| 18 | Fine-tuned dialogue model | Character-specific fine-tuned model for superior persona consistency |
| 19 | Security hardening | Production defense against persona attacks, memory poisoning, prompt injection |
| 20 | ANIMA 1.0 | Complete production platform — documented, deployed, benchmarked, portfolio-ready |

---

## V. CURRICULUM

### Stage Overview

**Stage 1: Foundations (Phases 1–5) — 7.5 weeks**

| Phase | Title | Chapters | Duration |
|-------|-------|----------|----------|
| 1 | Python Mastery | 1–8 | 1.5 weeks |
| 2 | Data Processing | 9–13 | 1 week |
| 3 | Machine Learning Foundations | 14–18 | 1.5 weeks |
| 4 | Deep Learning & Neural Networks | 19–23 | 2 weeks |
| 5 | LLMs & APIs | 24–28 | 1.5 weeks |

**Stage 2: Intelligence Layer (Phases 6–10) — 5.25 weeks**

| Phase | Title | Chapters | Duration |
|-------|-------|----------|----------|
| 6 | Prompt Engineering | 29–32 | 1 week |
| 7 | Embeddings | 33–36 | 1 week |
| 8 | Vector Databases | 37–39 | 0.75 weeks |
| 9 | Semantic Search | 40–42 | 0.5 weeks |
| 10 | RAG Systems | 43–48 | 2 weeks |

**Stage 3: AI Systems (Phases 11–15) — 5.75 weeks**

| Phase | Title | Chapters | Duration |
|-------|-------|----------|----------|
| 11 | AI Agents | 49–52 | 1.5 weeks |
| 12 | Multi-Agent Systems | 53–56 | 1.5 weeks |
| 13 | Memory & Planning | 57–59 | 1 week |
| 14 | Production APIs | 60–64 | 0.75 weeks |
| 15 | Evaluation & Testing | 65–67 | 1 week |

**Stage 4: Production (Phases 16–20) — 6.5 weeks**

| Phase | Title | Chapters | Duration |
|-------|-------|----------|----------|
| 16 | Deployment | 68–71 | 1 week |
| 17 | Monitoring & Observability | 72–74 | 0.75 weeks |
| 18 | Fine-tuning | 75–77 | 1.5 weeks |
| 19 | Security & System Design | 78–81 | 1.5 weeks |
| 20 | Capstone | 82–85 | 2 weeks |

**Total: ~25 weeks (6 months at 2–3 hours/day)**

---

### All 85 Chapters

**Phase 1: Python Mastery (CH 1–8)**
1. Environment setup & project scaffold
2. Type hints & the typing system
3. Decorators
4. Generators & iterators
5. Context managers
6. Dataclasses, enums & Pydantic
7. Async Python (asyncio)
8. Advanced OOP patterns

**Phase 2: Data Processing (CH 9–13)**
9. NumPy — arrays & vectorized operations
10. Pandas — DataFrames & data manipulation
11. Working with files (JSON, CSV, PDF, HTML)
12. HTTP requests & consuming APIs
13. Data cleaning & preprocessing pipelines

**Phase 3: Machine Learning Foundations (CH 14–18)**
14. ML mental model — what is learning?
15. Scikit-learn — train, test, evaluate
16. Text representation (TF-IDF, bag of words)
17. Feature engineering for text data
18. ML pipelines & model persistence

**Phase 4: Deep Learning & Neural Networks (CH 19–23)**
19. Neural networks from scratch (NumPy)
20. PyTorch fundamentals
21. Training loops, optimizers & loss functions
22. Transformer architecture (self-attention, multi-head attention, positional encoding)
23. Hugging Face — loading & running pre-trained models

**Phase 5: LLMs & APIs (CH 24–28)**
24. How large language models work (architecture → inference)
25. OpenAI API — completions, function calling, vision
26. Anthropic Claude API — Messages, tool use, streaming
27. Structured outputs & JSON mode
28. Streaming, token management & cost control

**Phase 6: Prompt Engineering (CH 29–32)**
29. Prompt engineering fundamentals & mental model
30. Advanced techniques (chain-of-thought, few-shot, ReAct, self-consistency)
31. System prompts & persona design for ANIMA characters
32. Prompt versioning, evaluation & A/B testing

**Phase 7: Embeddings (CH 33–36)**
33. What are embeddings? The geometry of meaning
34. Embedding models (OpenAI, Cohere, sentence-transformers, local)
35. Chunking strategies for documents
36. Embedding pipelines — batch processing, caching & optimization

**Phase 8: Vector Databases (CH 37–39)**
37. Vector database architecture & indexing (HNSW, IVF-PQ)
38. ChromaDB — local development & experimentation
39. Pinecone — production-scale vector search

**Phase 9: Semantic Search (CH 40–42)**
40. Building semantic search from embeddings
41. Hybrid search (dense + sparse, BM25 + embeddings)
42. Re-ranking & result quality optimization

**Phase 10: RAG Systems (CH 43–48)**
43. RAG architecture & the retrieval-augmented generation mental model
44. Document ingestion pipeline (parse, chunk, embed, index)
45. Retrieval strategies (naive → HyDE → multi-query → self-RAG)
46. Context window management & injection patterns
47. Advanced RAG (CRAG, corrective RAG, adaptive retrieval)
48. RAG evaluation framework (RAGAS: faithfulness, relevance, groundedness)

**Phase 11: AI Agents (CH 49–52)**
49. What are AI agents? The autonomy spectrum
50. Tool use & function calling
51. ReAct pattern — reasoning + acting loops
52. Building a single-agent system end to end

**Phase 12: Multi-Agent Systems (CH 53–56)**
53. Multi-agent architecture patterns
54. Agent orchestration & communication protocols
55. LangGraph for stateful agent workflows
56. CrewAI & AutoGen — multi-agent frameworks

**Phase 13: Memory & Planning (CH 57–59)**
57. Agent memory types (short-term, long-term, episodic, semantic)
58. Planning strategies (tree-of-thought, MCTS, hierarchical planning)
59. Knowledge graphs for agent context

**Phase 14: Production APIs (CH 60–64)**
60. FastAPI — async architecture, routing, dependency injection
61. Authentication (JWT, API keys, OAuth2)
62. PostgreSQL & SQLAlchemy (schema design, Alembic migrations)
63. Redis — caching, sessions & pub/sub
64. Background tasks (Celery, ARQ) & WebSockets

**Phase 15: Evaluation & Testing (CH 65–67)**
65. Unit & integration testing for AI systems
66. LLM evaluation frameworks (RAGAS, LLM-as-judge, human eval pipelines)
67. Red teaming & adversarial prompt testing

**Phase 16: Deployment (CH 68–71)**
68. Docker — containerizing AI systems
69. Docker Compose — multi-container AI stacks
70. CI/CD pipelines for AI (GitHub Actions: lint, test, build, deploy)
71. Cloud deployment (AWS/GCP/Azure — containers, serverless, GPU instances)

**Phase 17: Monitoring & Observability (CH 72–74)**
72. Structured logging for AI systems
73. LLM observability (LangSmith, Langfuse — traces, evals, cost tracking)
74. Cost tracking, budgeting & optimization

**Phase 18: Fine-tuning (CH 75–77)**
75. When and why to fine-tune (vs. prompt engineering vs. RAG)
76. Fine-tuning with OpenAI API (supervised fine-tuning, preference tuning)
77. Fine-tuning with Hugging Face (LoRA, QLoRA, PEFT on consumer hardware)

**Phase 19: Security & System Design (CH 78–81)**
78. AI security — prompt injection, jailbreaks, data poisoning, model extraction
79. Secure AI architecture patterns
80. AI system design — patterns, trade-offs, and real-world case studies
81. Scalable AI architecture — handling load, latency, and cost at scale

**Phase 20: Capstone (CH 82–85)**
82. Final architecture review & integration sprint
83. Performance benchmarking & optimization
84. Documentation & portfolio preparation
85. Interview preparation & career launch

---

## VI. RPG PROGRESSION SYSTEM

### XP Per Activity

| Activity | XP |
|----------|-----|
| Chapter completion (base) | +200 |
| Quiz — perfect score (100%) | +200 |
| Quiz — good (80–99%) | +100–190 |
| Quiz — passing (60–79%) | +50–90 |
| Assignment — staff-level quality | +300 |
| Assignment — senior-level quality | +200 |
| Assignment — junior-level quality | +100 |
| Bonus objective completed | +50–150 |
| Side quest completed | +200–500 |
| Boss battle defeated | +1,000 |
| Final boss defeated | +2,000 |

**Average per chapter:** ~550 XP (200 base + 150 quiz + 200 assignment)
**Total to reach Level 20:** 44,000 XP (achievable at average performance + boss battles)

### Levels & Titles

| Level | Title | XP Required | Stage | Boss? |
|-------|-------|-------------|-------|-------|
| 1 | Initiate | 0 | Foundations | |
| 2 | Code Apprentice | 300 | Foundations | |
| 3 | Python Adept | 800 | Foundations | |
| 4 | Data Artisan | 1,500 | Foundations | |
| 5 | ML Theorist | 2,400 | Foundations | ⚔ |
| 6 | Neural Scholar | 3,500 | Intelligence | |
| 7 | Language Artificer | 5,000 | Intelligence | |
| 8 | Prompt Architect | 6,800 | Intelligence | |
| 9 | Embedding Sage | 9,000 | Intelligence | ⚔ |
| 10 | Vector Commander | 11,500 | Intelligence | |
| 11 | RAG Architect | 14,000 | AI Systems | |
| 12 | Agent Summoner | 17,000 | AI Systems | ⚔ |
| 13 | Multi-Agent Overlord | 20,000 | AI Systems | |
| 14 | Memory Keeper | 23,500 | AI Systems | |
| 15 | Production Engineer | 27,000 | AI Systems | ⚔ |
| 16 | Systems Architect | 30,500 | Production | |
| 17 | Deployment Sovereign | 34,000 | Production | |
| 18 | Fine-tuning Artificer | 37,500 | Production | ⚔ |
| 19 | Security Oracle | 41,000 | Production | |
| 20 | AI Engineer | 44,000 | Production | ⚔ FINAL |

### Boss Battles

| # | Name | Trigger | Challenge | Reward |
|---|------|---------|-----------|--------|
| 1 | The Python Gauntlet | After Phase 1 | Build a complete async data pipeline in 2 hours — all Phase 1 patterns tested simultaneously | +1,000 XP |
| 2 | Transformer Awakens | After Phase 4 | Implement simplified attention in PyTorch; explain every single line | +1,000 XP |
| 3 | The RAG Dungeon | After Phase 10 | Build full RAG pipeline from scratch; score >80% on RAGAS benchmark | +1,000 XP |
| 4 | Agent Uprising | After Phase 13 | Multi-agent task with 5+ tool calls + full agent handoffs | +1,000 XP |
| 5 | Production Siege | After Phase 17 | Production-ready in one day: Docker + CI/CD + cloud + monitoring | +1,000 XP |
| 6 | ANIMA Awakens | After Phase 20 | Full ANIMA production review — all systems operational and documented | +2,000 XP |

### Achievement Categories (60 total)

**Foundations (15)**
- Hello World — Complete Chapter 1
- Pythonista — Phase 1 at 90%+ quiz average
- Async Awakening — Complete asyncio chapter
- The Clean Coder — Assignment scores 95%+
- Type Safety — Complete type hints chapter with zero mypy errors

**Intelligence (12)**
- First Vector — Build first vector store
- The Grounding — First RAG response correctly grounded in retrieved context
- Memory Palace — 1,000 character memories stored
- Chunk Master — Sub-100ms retrieval on 10,000+ documents

**AI Systems (18)**
- Agent Zero — First autonomous agent action
- Many Minds — First successful multi-agent interaction
- ANIMA Lives — First persistent character created
- The Immortal — Character persists and is recalled correctly after 30 days
- Relationship Engine — Two ANIMA characters develop a documented relationship arc

**Production (10)**
- Shipped It — First cloud deployment
- The Watcher — First observability dashboard live
- Cost Wizard — Reduce API costs 20% through optimization
- Green Pipeline — All CI/CD tests passing on first deploy

**Legendary (5)**
- Perfectionist — 100% on any quiz
- Speed Runner — Complete any phase 30% faster than estimated
- Open Source Hero — Merged PR to a major AI library
- Polyglot — ANIMA character functions correctly in three languages
- Legend — All other achievements unlocked

### Side Quests

| Quest | Challenge | Reward | Difficulty |
|-------|-----------|--------|------------|
| The Paper Trail | Read and annotate "Attention is All You Need" | +200 XP | Medium |
| The Benchmark | Compare 3 embedding models; publish findings as a writeup | +300 XP | Hard |
| Open Source Hero | Merged PR to LangChain, CrewAI, or similar | +500 XP | Legendary |
| The Cost Whisperer | Cut ANIMA API costs 30% through architecture optimization | +400 XP | Hard |
| The Novelist | Co-write a coherent story with ANIMA across 20 sessions | +300 XP | Medium |
| The Historian | ANIMA character built entirely from historical documents | +250 XP | Medium |
| The Battle | 20-round debate between two ANIMA characters | +200 XP | Easy |

### Weekly Challenges

- **Week 2:** Build the cleanest Python class you have ever written
- **Week 5:** Explain transformer attention in a 5-minute verbal explanation
- **Week 10:** Build a RAG system from scratch in under 3 hours
- **Week 15:** Build a multi-agent system that generates a complete research report
- **Week 20:** Deploy any AI system to full production in a single working day
- **Week 24:** Record a 10-minute ANIMA demo video for the GitHub README

---

## VII. STUDY SCHEDULE

**24-Week Optimized Plan (CS degree + SE background)**

| Weeks | Stage | Phase | Content | Boss Battle |
|-------|-------|-------|---------|-------------|
| 1–1.5 | Foundations | 1 | Python Mastery | — |
| 1.5–2.5 | Foundations | 2 | Data Processing | — |
| 2.5–4 | Foundations | 3 | ML Foundations | — |
| 4–6 | Foundations | 4 | Deep Learning | — |
| 6–7.5 | Foundations | 5 | LLMs & APIs | Boss #1: Python Gauntlet |
| 7.5–8.5 | Intelligence | 6 | Prompt Engineering | Boss #2: Transformer Awakens |
| 8.5–9.5 | Intelligence | 7 | Embeddings | — |
| 9.5–10.25 | Intelligence | 8 | Vector Databases | — |
| 10.25–10.75 | Intelligence | 9 | Semantic Search | — |
| 10.75–12.75 | Intelligence | 10 | RAG Systems | Boss #3: The RAG Dungeon |
| 12.75–14.25 | AI Systems | 11 | AI Agents | — |
| 14.25–15.75 | AI Systems | 12 | Multi-Agent | — |
| 15.75–16.75 | AI Systems | 13 | Memory & Planning | — |
| 16.75–17.5 | AI Systems | 14 | Production APIs | — |
| 17.5–18.5 | AI Systems | 15 | Evaluation | Boss #4: Agent Uprising |
| 18.5–19.5 | Production | 16 | Deployment | — |
| 19.5–20.25 | Production | 17 | Monitoring | Boss #5: Production Siege |
| 20.25–21.75 | Production | 18 | Fine-tuning | — |
| 21.75–23.25 | Production | 19 | Security & Design | — |
| 23.25–25 | Production | 20 | Capstone | Boss #6: ANIMA Awakens |

**Suggested daily structure (2.5h/day)**
- 15 min: Review previous chapter notes
- 60 min: Theory, code walkthrough, and examples
- 60 min: Assignment / ANIMA project work
- 15 min: Update PROGRESS.md and CONTINUE.md

---

## VIII. ASSESSMENT STRATEGY

### Chapter Format (always in this order)

1. **Why it exists** — the real-world problem this concept solves in production AI
2. **What it is** — precise definition and mental model
3. **How it works** — internals, architecture, or algorithm explained from first principles
4. **Analogy** — intuitive explanation via a concrete metaphor
5. **Visual** — diagram, code trace, or architecture drawing
6. **Code walkthrough** — complete code, explained line by line
7. **Common mistakes** — how experienced engineers get this wrong
8. **Industry usage** — how OpenAI, Anthropic, Google use this in production
9. **Mini exercises** — 5–10 exercises of increasing difficulty
10. **Quiz** — 10 MCQ + 5 debugging + 5 output prediction + 5 conceptual + 3 architecture (answers never revealed until student submits)
11. **Coding assignment** — builds ANIMA, reviewed at staff engineer standard
12. **Code review** — 10 dimensions (see below)
13. **Project milestone** — explicit checkpoint in ANIMA's evolution

### Quiz Rules
- Answers are never revealed before student submits
- After submission: every answer explained (correct and incorrect options both)
- Output: score, difficulty rating, weak areas identified, specific concepts to revisit

### Code Review Dimensions

Every assignment is reviewed across all ten dimensions:

1. **Architecture** — is the design correct for the problem?
2. **Naming** — do variables, functions, and classes communicate intent precisely?
3. **Readability** — can another engineer understand this in 30 seconds?
4. **Complexity** — is it as simple as possible while fully doing the job?
5. **Scalability** — does this hold up at 100x the current load?
6. **Performance** — are there obvious inefficiencies or unnecessary allocations?
7. **Edge cases** — what inputs or states would break this?
8. **Security** — is there an exploitable vulnerability?
9. **Testability** — is this code easy to unit test without mocks everywhere?
10. **Maintainability** — can this be extended without rewriting it?

---

## IX. CAPSTONE REQUIREMENTS

ANIMA 1.0 must satisfy all of the following before graduation:

**Core engine**
- [ ] Character creation with name, backstory, personality traits, and knowledge base
- [ ] Genuine persistent memory — tested surviving restarts and recalled 30+ days later
- [ ] Personality drift — tracked, quantified, and visible across conversation history
- [ ] Autonomous behavior — characters pursue goals between conversations

**Multi-character**
- [ ] Two or more characters interact with persistent relationship memory
- [ ] Emergent narrative documented across 10+ character interactions

**Production stack**
- [ ] FastAPI backend with full async endpoints
- [ ] JWT authentication with API key management
- [ ] PostgreSQL with Alembic schema migrations
- [ ] Redis caching layer (session state + query caching)
- [ ] Pinecone or Chroma for vector memory at production scale
- [ ] RAG over character knowledge bases with groundedness testing

**Agent system**
- [ ] Minimum 5 distinct tools (web search, calendar, memory write, knowledge query, relationship lookup)
- [ ] Agent handoff demonstrated in multi-character scenario

**Infrastructure**
- [ ] Docker Compose for the full stack (API + DB + Redis + vector DB)
- [ ] CI/CD via GitHub Actions (lint + test + build + deploy)
- [ ] Cloud deployment (AWS, GCP, or Azure)
- [ ] Auto-scaling or serverless configuration documented

**Observability**
- [ ] LangSmith or Langfuse integration with full trace coverage
- [ ] Cost tracking dashboard (daily API spend, per-character cost breakdown)
- [ ] Personality drift metrics
- [ ] Alert on anomalous character behavior

**Quality**
- [ ] Minimum 70% test coverage (unit + integration)
- [ ] Character consistency evaluation suite (RAGAS-based)
- [ ] Red team test suite covering prompt injection and persona attack vectors
- [ ] Performance benchmark: p99 response latency < 3 seconds

**Documentation**
- [ ] README with demo GIF, architecture diagram, and 5-minute quick start
- [ ] OpenAPI/Swagger documentation (auto-generated by FastAPI)
- [ ] System design document (architecture decisions, trade-offs)
- [ ] SDK example — 20-line integration code
- [ ] Performance benchmarks published

---

## X. INTERVIEW PREPARATION

Starting from Phase 10, each chapter accumulates interview preparation material. By Phase 20, the interview prep section includes:

**Questions answered from memory:**
- Explain RAG and when to use it over fine-tuning
- How does transformer attention work?
- How do you evaluate an LLM application in production?
- Design a scalable AI character system with persistent memory
- How do you prevent prompt injection in a production AI system?
- What are the trade-offs between Pinecone, Chroma, and Weaviate?
- How do you handle LLM latency in a user-facing product?
- Walk me through a multi-agent orchestration architecture
- How do you manage LLM cost at scale?
- What is LoRA and when would you use it over full fine-tuning?

**System design problems (practiced in full):**
- Design a production RAG system for 10 million documents
- Design a multi-agent research pipeline
- Design an AI companion with persistent memory (the ANIMA problem)
- Design a cost-efficient LLM inference layer with caching and fallbacks

**Python patterns tested in AI interviews:**
- Async patterns for concurrent LLM calls
- Streaming response handling
- Retry logic with exponential backoff
- Batch embedding optimization

---

## XI. REPOSITORY STRUCTURE

### Per-Chapter Document System

Every completed chapter generates 7 permanent documents in `docs/phase-XX-[name]/chapter-XX-[name]/`:

| Document | Purpose |
|----------|---------|
| `lesson.md` | Full chapter content — theory, code, examples, common mistakes |
| `assignment.md` | Coding assignment that advances ANIMA |
| `quiz.md` | 28 questions with answers revealed after submission |
| `cheatsheet.md` | Quick reference card — patterns, golden rules, gotchas |
| `summary.md` | Key takeaways, XP breakdown, ANIMA milestone update |
| `architecture-notes.md` | ANIMA design decisions in ADR format |
| `interview-prep.md` | 5–10 interview Q&As from this chapter's topic |

**After 85 chapters:** 595 documents — a complete, permanently version-controlled AI engineering textbook.

### Full Directory Structure

```
ai-engineering-bootcamp/
├── README.md                   # GitHub landing page
├── HANDBOOK.md                 # This file — master course reference
├── ROADMAP.md                  # Visual curriculum map (all 20 phases)
├── CONTINUE.md                 # AI continuation briefing
├── PROGRESS.md                 # Live XP and achievement tracker
├── CHANGELOG.md                # Per-session log of all completions
│
├── docs/                       # All chapter documents (grow as course proceeds)
│   └── phase-01-python/
│       ├── README.md           # Phase overview, objectives, milestone
│       └── chapter-01-setup/
│           ├── lesson.md
│           ├── assignment.md
│           ├── quiz.md
│           ├── cheatsheet.md
│           ├── summary.md
│           ├── architecture-notes.md
│           └── interview-prep.md
│
├── reference/                  # Standalone reference docs (grow as course proceeds)
│   ├── python/                 # Advanced Python patterns and idioms
│   ├── ml/                     # ML algorithms and concepts
│   ├── llms/                   # LLM behavior, APIs, and patterns
│   ├── rag/                    # RAG architectures and strategies
│   ├── agents/                 # Agent frameworks and patterns
│   ├── deployment/             # Production deployment guides
│   ├── security/               # AI security patterns and defenses
│   └── architecture/
│       ├── design-patterns/    # Reusable AI system design patterns
│       └── diagrams/           # Architecture diagrams (exported)
│
├── project/
│   ├── anima/                  # ANIMA source code (grows each phase)
│   └── architecture/
│       └── decision-log.md     # Chronological ANIMA design history
│
├── assets/
│   └── diagrams/               # Diagrams for README and docs
│
└── templates/                  # Template for each of the 7 document types
    ├── lesson.md
    ├── assignment.md
    ├── quiz.md
    ├── cheatsheet.md
    ├── summary.md
    ├── architecture-notes.md
    └── interview-prep.md
```

---

## XII. CONTINUATION PROTOCOL

### End-of-chapter protocol (after every chapter)

**Step 1 — Generate all 7 documents** in `docs/phase-XX-[name]/chapter-XX-[name]/` using the templates in `templates/`:
- `lesson.md` — full chapter content (never truncated)
- `assignment.md` — coding assignment for ANIMA
- `quiz.md` — all 28 questions + answers (answers at the bottom, clearly separated)
- `cheatsheet.md` — quick reference card
- `summary.md` — takeaways + XP breakdown + ANIMA milestone
- `architecture-notes.md` — ANIMA design decision (ADR format)
- `interview-prep.md` — 5–10 interview Q&As from this chapter

**Step 2 — Update CONTINUE.md** with:

```
Last chapter completed:  [number and title]
Date:                    [date]
XP this chapter:         [base + quiz + assignment + bonus]
Running total XP:        [total]
Current level:           [number — title]
ANIMA current state:     [one sentence — what ANIMA can do now]
Outstanding questions:   [anything to revisit]
Next chapter:            [number and title]
```

**Step 3 — Update PROGRESS.md:** check off the chapter, log XP in the table.

**Step 4 — Append to CHANGELOG.md:**
```
## [DATE] — Chapter [N]: [Title]
XP earned: +[N] (running total: [N]) | Level: [N] — [Title]
Documents generated: lesson.md, assignment.md, quiz.md, cheatsheet.md, summary.md, architecture-notes.md, interview-prep.md
ANIMA update: [what ANIMA gained this chapter]
```

### How to resume with a new AI model

1. Share `CONTINUE.md` and `HANDBOOK.md`
2. Paste this prompt:

> *"Read CONTINUE.md and HANDBOOK.md in full. Continue teaching my AI engineering bootcamp from where we left off. Follow the chapter format in Section VIII exactly. Generate all 7 chapter documents at the end of each chapter per Section XI. Never reveal quiz answers before I submit mine."*

Any AI model that reads these two files can continue teaching from any point in the course.

---

*Handbook v1.1 — documentation architecture updated. Updated after each phase milestone.*
