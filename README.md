# AI Engineering Bootcamp

> **Building ANIMA** — an open-source AI character engine with genuine persistent memory, evolving personality, and autonomous behavior.

A project-based, RPG-styled AI engineering curriculum designed from scratch. Every chapter builds toward shipping ANIMA 1.0 as a production system.

---

## The Project: ANIMA

ANIMA is a production-quality framework for creating AI characters that **remember everything, forever** — grounded in knowledge bases, capable of autonomous behavior, and able to form relationships with other AI characters. Built across 20 phases, it ships as a complete open-source platform at Phase 20.

**Why ANIMA:** Every AI chatbot resets on every conversation. ANIMA solves that. The demo is immediately compelling: create a character, have ten conversations over two weeks, ask on day fifteen "do you remember what you told me?" — and she does. In character. Grounded in her knowledge base. That five-second demo gets shared.

---

## Repository Structure

| Path | Purpose |
|------|---------|
| [`HANDBOOK.md`](HANDBOOK.md) | Single source of truth — vision, curriculum, RPG system, all rules |
| [`CONTINUE.md`](CONTINUE.md) | Briefing for any AI model resuming the course |
| [`PROGRESS.md`](PROGRESS.md) | Live XP, chapter, and achievement tracker |
| [`ROADMAP.md`](ROADMAP.md) | Full curriculum map — all 20 phases, all 85 chapters |
| [`CHANGELOG.md`](CHANGELOG.md) | Per-session log of completed chapters |
| [`docs/`](docs/) | Chapter documents — built up as the course proceeds |
| [`templates/`](templates/) | Blank templates for the 7 per-chapter documents |
| [`reference/`](reference/) | Topic-level reference docs — grows across the course |
| [`project/anima/`](project/anima/) | ANIMA source code — grows each phase |
| [`scripts/generate_chapter_notes.py`](scripts/generate_chapter_notes.py) | PDF generator for cumulative chapter notes |

---

## Curriculum at a Glance

| Stage | Phases | Chapters | Theme |
|-------|--------|----------|-------|
| 1 — Foundations | 1–5 | 1–28 | Python → Data → ML → Deep Learning → LLMs |
| 2 — Intelligence Layer | 6–10 | 29–48 | Prompts → Embeddings → Vector DB → Search → RAG |
| 3 — AI Systems | 11–15 | 49–67 | Agents → Multi-Agent → Memory → APIs → Evaluation |
| 4 — Production | 16–20 | 68–85 | Deploy → Monitor → Fine-tune → Security → Capstone |

**Total:** 20 phases · 85 chapters · 6 boss battles · ~24 weeks

---

## Toolchain

| Tool | Purpose |
|------|---------|
| `uv` | Python version + package management (replaces pyenv + Poetry) |
| `ruff` | Linting and formatting |
| `mypy` | Type checking |
| `pytest` | Testing |
| `FastAPI` | REST API (Phase 14+) |
| `Pinecone / Chroma` | Vector memory (Phase 8+) |

---

## How to Resume This Course

If continuing with an AI assistant in a new session, share `CONTINUE.md` and `HANDBOOK.md`, then paste:

> *"Read CONTINUE.md and HANDBOOK.md in full. Continue teaching my AI engineering bootcamp from where we left off. Follow the chapter format in Section VIII of the handbook exactly. Generate all 7 chapter documents at the end of each chapter per Section XI. Never reveal quiz answers before I submit mine."*

---

## RPG Progression

| | |
|---|---|
| **Current level** | 1 — Initiate |
| **Current XP** | 0 / 300 (to Level 2) |
| **Current phase** | Phase 1: Python Mastery |
| **Chapters completed** | 0 / 85 |
| **Boss battles** | 0 / 6 |

See [`PROGRESS.md`](PROGRESS.md) for the full tracker.

---

## Per-Chapter Document System

Every completed chapter generates 7 permanent documents in `docs/phase-XX/chapter-XX/`:

```
chapter-01-setup/
├── lesson.md             Full chapter content — theory, code, examples
├── assignment.md         Coding assignment that advances ANIMA
├── quiz.md               28 questions with answers
├── cheatsheet.md         Quick reference card
├── summary.md            Takeaways + XP breakdown + ANIMA milestone
├── architecture-notes.md ANIMA design decisions (ADR format)
└── interview-prep.md     5–10 interview Q&As from this topic
```

After 85 chapters: **595 documents** — a complete AI engineering textbook.

---

*Started: June 2026 · Target completion: ~24 weeks*
