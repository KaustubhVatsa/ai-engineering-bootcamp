"""
ANIMA — The AI Character Engine.

An open-source framework for creating AI characters with genuine persistent
memory, evolving personality, and autonomous behavior.

Phases:
    1-5   Foundations:        Python → Data → ML → Deep Learning → LLMs
    6-10  Intelligence Layer: Prompts → Embeddings → Vector DB → Search → RAG
    11-15 AI Systems:         Agents → Multi-Agent → Memory → APIs → Evaluation
    16-20 Production:         Deploy → Monitor → Fine-tune → Security → Capstone
"""

from __future__ import annotations

from . import agents, api, core, memory, models, utils

__version__ = "0.1.0"
__author__ = "Kaustubh Vatsa"

__all__ = [
    "__author__",
    "__version__",
    "agents",
    "api",
    "core",
    "memory",
    "models",
    "utils",
]
