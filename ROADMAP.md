# ROADMAP.md — AI Engineering Bootcamp Curriculum Map

*20 Phases · 85 Chapters · 6 Boss Battles · 24 Weeks · Project: ANIMA*

---

## Stage Overview

| Stage | Phases | Chapters | Duration | Theme |
|-------|--------|----------|----------|-------|
| 1: Foundations | 1–5 | 1–28 | 7.5 weeks | From Python to calling LLMs |
| 2: Intelligence Layer | 6–10 | 29–48 | 5.25 weeks | Embeddings, search, and RAG |
| 3: AI Systems | 11–15 | 49–67 | 5.75 weeks | Agents, memory, production APIs |
| 4: Production | 16–20 | 68–85 | 6.5 weeks | Deploy, monitor, fine-tune, ship |

---

## Stage 1: Foundations (Weeks 1–7.5)

| Phase | Title | Chapters | Duration | ANIMA Gains | Boss Battle |
|-------|-------|----------|----------|-------------|-------------|
| 1 | Python Mastery | 1–8 | 1.5 weeks | Core architecture + plugin system | — |
| 2 | Data Processing | 9–13 | 1 week | Knowledge ingestion pipeline | — |
| 3 | ML Foundations | 14–18 | 1.5 weeks | Personality classifier | — |
| 4 | Deep Learning | 19–23 | 2 weeks | Embedding-aware architecture | — |
| 5 | LLMs & APIs | 24–28 | 1.5 weeks | Dialogue generation engine | ⚔ The Python Gauntlet |

### Chapters

| CH | Title | Key Concept |
|----|-------|-------------|
| 1 | Environment setup & project scaffold | Project structure, virtual environments, tooling |
| 2 | Type hints & the typing system | Type annotations, generics, Protocols |
| 3 | Decorators | Higher-order functions, factory decorators |
| 4 | Generators & iterators | Lazy evaluation, `yield`, `__iter__` |
| 5 | Context managers | `with` blocks, `__enter__`/`__exit__`, `contextlib` |
| 6 | Dataclasses, enums & Pydantic | Data modeling, validation, serialization |
| 7 | Async Python (asyncio) | `async`/`await`, event loops, concurrent IO |
| 8 | Advanced OOP patterns | ABCs, Protocols, mixins, composition |
| 9 | NumPy | Arrays, broadcasting, vectorized math |
| 10 | Pandas | DataFrames, indexing, groupby, transforms |
| 11 | Working with files | JSON, CSV, PDF parsing, HTML extraction |
| 12 | HTTP requests | `httpx`, async requests, auth patterns |
| 13 | Data cleaning & preprocessing | Missing values, normalization, pipelines |
| 14 | ML mental model | What is learning? Loss, generalization, bias-variance |
| 15 | Scikit-learn | Train/test split, cross-validation, evaluation |
| 16 | Text representation | TF-IDF, bag of words, n-grams |
| 17 | Feature engineering | Text features, embeddings as features |
| 18 | ML pipelines & model persistence | `Pipeline`, `joblib`, versioning |
| 19 | Neural networks from scratch | Perceptrons, layers, backpropagation in NumPy |
| 20 | PyTorch fundamentals | Tensors, autograd, `nn.Module` |
| 21 | Training loops | Optimizers, schedulers, gradient clipping |
| 22 | Transformer architecture | Self-attention, multi-head attention, positional encoding |
| 23 | Hugging Face | `transformers`, tokenizers, inference pipelines |
| 24 | How LLMs work | Autoregression, sampling, temperature, top-p |
| 25 | OpenAI API | Chat completions, function calling, vision |
| 26 | Anthropic Claude API | Messages, tool use, streaming, system prompts |
| 27 | Structured outputs | JSON mode, response schemas, validation |
| 28 | Streaming & cost control | Token counting, streaming, cost optimization |

---

## Stage 2: Intelligence Layer (Weeks 7.5–12.75)

| Phase | Title | Chapters | Duration | ANIMA Gains | Boss Battle |
|-------|-------|----------|----------|-------------|-------------|
| 6 | Prompt Engineering | 29–32 | 1 week | Persona prompt system | ⚔ Transformer Awakens |
| 7 | Embeddings | 33–36 | 1 week | Memory encoding pipeline | — |
| 8 | Vector Databases | 37–39 | 0.75 weeks | Persistent memory store | — |
| 9 | Semantic Search | 40–42 | 0.5 weeks | Memory retrieval system | — |
| 10 | RAG Systems | 43–48 | 2 weeks | Knowledge-grounded dialogue | ⚔ The RAG Dungeon |

### Chapters

| CH | Title | Key Concept |
|----|-------|-------------|
| 29 | Prompt engineering fundamentals | Prompt structure, instructions, context |
| 30 | Advanced techniques | Chain-of-thought, few-shot, ReAct, self-consistency |
| 31 | System prompts & persona design | Character prompts, role framing, consistency |
| 32 | Prompt versioning & A/B testing | Prompt management, evaluation, iteration |
| 33 | What are embeddings? | Semantic geometry, vector space, similarity |
| 34 | Embedding models | OpenAI, Cohere, sentence-transformers, local |
| 35 | Chunking strategies | Fixed, semantic, recursive, late chunking |
| 36 | Embedding pipelines | Batching, caching, async processing |
| 37 | Vector DB architecture | HNSW, IVF-PQ, ANN search |
| 38 | ChromaDB | Local vector store, collections, metadata filtering |
| 39 | Pinecone | Production scale, namespaces, sparse-dense |
| 40 | Building semantic search | End-to-end semantic search system |
| 41 | Hybrid search | BM25 + dense, reciprocal rank fusion |
| 42 | Re-ranking | Cross-encoder re-ranking, result quality |
| 43 | RAG architecture | Retrieval-augmented generation mental model |
| 44 | Document ingestion pipeline | Parse → chunk → embed → index |
| 45 | Retrieval strategies | Naive → HyDE → multi-query → self-RAG |
| 46 | Context window management | Context injection, window sizing, compression |
| 47 | Advanced RAG | CRAG, corrective RAG, adaptive retrieval |
| 48 | RAG evaluation | RAGAS, faithfulness, relevance, groundedness |

---

## Stage 3: AI Systems (Weeks 12.75–18.5)

| Phase | Title | Chapters | Duration | ANIMA Gains | Boss Battle |
|-------|-------|----------|----------|-------------|-------------|
| 11 | AI Agents | 49–52 | 1.5 weeks | Autonomous character behavior | — |
| 12 | Multi-Agent Systems | 53–56 | 1.5 weeks | Multi-character dynamics | — |
| 13 | Memory & Planning | 57–59 | 1 week | Long-term character planning | — |
| 14 | Production APIs | 60–64 | 0.75 weeks | ANIMA REST API | — |
| 15 | Evaluation & Testing | 65–67 | 1 week | Evaluation framework | ⚔ Agent Uprising |

### Chapters

| CH | Title | Key Concept |
|----|-------|-------------|
| 49 | What are AI agents? | Autonomy spectrum, sense-plan-act loop |
| 50 | Tool use & function calling | Tool definitions, calling, error handling |
| 51 | ReAct pattern | Reasoning + acting loops, scratchpad |
| 52 | Single-agent system | End-to-end autonomous agent |
| 53 | Multi-agent architecture | Orchestrator-worker, peer-to-peer, hierarchical |
| 54 | Agent orchestration | Communication protocols, handoffs, state |
| 55 | LangGraph | State machines, conditional edges, persistence |
| 56 | CrewAI & AutoGen | Crew-based agents, conversational multi-agent |
| 57 | Agent memory types | Short-term, long-term, episodic, semantic, procedural |
| 58 | Planning strategies | Tree-of-thought, MCTS, hierarchical planning |
| 59 | Knowledge graphs | Nodes, edges, traversal for agent context |
| 60 | FastAPI | Async architecture, routing, dependency injection |
| 61 | Authentication | JWT, API keys, OAuth2, middleware |
| 62 | PostgreSQL & SQLAlchemy | Schema design, ORM, Alembic migrations |
| 63 | Redis | Caching, sessions, pub/sub, TTL |
| 64 | Background tasks & WebSockets | Celery/ARQ, real-time communication |
| 65 | Testing AI systems | Unit, integration, mocking LLMs |
| 66 | LLM evaluation | RAGAS, LLM-as-judge, human eval pipelines |
| 67 | Red teaming | Adversarial prompts, persona attacks, coverage |

---

## Stage 4: Production (Weeks 18.5–25)

| Phase | Title | Chapters | Duration | ANIMA Gains | Boss Battle |
|-------|-------|----------|----------|-------------|-------------|
| 16 | Deployment | 68–71 | 1 week | Cloud deployment | — |
| 17 | Monitoring & Observability | 72–74 | 0.75 weeks | Observability stack | ⚔ Production Siege |
| 18 | Fine-tuning | 75–77 | 1.5 weeks | Fine-tuned dialogue model | — |
| 19 | Security & System Design | 78–81 | 1.5 weeks | Security hardening | — |
| 20 | Capstone | 82–85 | 2 weeks | ANIMA 1.0 | ⚔ ANIMA Awakens (Final) |

### Chapters

| CH | Title | Key Concept |
|----|-------|-------------|
| 68 | Docker | Containerization, multi-stage builds, best practices |
| 69 | Docker Compose | Multi-container stacks, networking, volumes |
| 70 | CI/CD | GitHub Actions, automated testing, deployment |
| 71 | Cloud deployment | AWS/GCP/Azure — containers, serverless, GPU |
| 72 | Structured logging | Log levels, structured JSON, correlation IDs |
| 73 | LLM observability | LangSmith/Langfuse — traces, evals, costs |
| 74 | Cost tracking | Token budgets, cost dashboards, optimization |
| 75 | When to fine-tune | Fine-tune vs. RAG vs. prompting — the decision |
| 76 | Fine-tuning with OpenAI | Supervised fine-tuning, preference tuning, evaluation |
| 77 | Fine-tuning with Hugging Face | LoRA, QLoRA, PEFT, training on consumer hardware |
| 78 | AI security | Prompt injection, jailbreaks, data poisoning, extraction |
| 79 | Secure architecture | Defense patterns, input validation, sandboxing |
| 80 | AI system design | Patterns, trade-offs, real-world case studies |
| 81 | Scalable architecture | Load, latency, cost — architectural decisions |
| 82 | Final architecture review | Integration sprint, system audit, gap fill |
| 83 | Performance benchmarking | Latency, throughput, cost, quality metrics |
| 84 | Documentation & portfolio | README, docs, portfolio presentation |
| 85 | Interview prep & career launch | Final prep, job search strategy, positioning |

---

## Boss Battles

| # | Name | After | Challenge | XP |
|---|------|-------|-----------|-----|
| 1 | The Python Gauntlet | Phase 1 | Build a complete async data pipeline in 2 hours | +1,000 |
| 2 | Transformer Awakens | Phase 4 | Implement attention in PyTorch; explain every line | +1,000 |
| 3 | The RAG Dungeon | Phase 10 | Full RAG pipeline; score >80% on RAGAS | +1,000 |
| 4 | Agent Uprising | Phase 13 | Multi-agent task: 5+ tool calls + handoffs | +1,000 |
| 5 | Production Siege | Phase 17 | Production-ready in one day | +1,000 |
| 6 | ANIMA Awakens | Phase 20 | Full ANIMA production review | +2,000 |

---

## Documentation Map

Every chapter generates 7 documents. After 85 chapters: 595 documents total.

```
chapter-XX-[name]/
├── lesson.md            Full chapter content (never truncated)
├── assignment.md        Coding assignment for ANIMA
├── quiz.md              28-question quiz with answers
├── cheatsheet.md        Quick reference card
├── summary.md           Takeaways + XP log + ANIMA update
├── architecture-notes.md  ANIMA design decision (ADR)
└── interview-prep.md    5–10 interview Q&As
```

---

*See HANDBOOK.md for full course details. See PROGRESS.md for current status.*
