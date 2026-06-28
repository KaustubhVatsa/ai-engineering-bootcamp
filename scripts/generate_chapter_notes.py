#!/usr/bin/env python3
"""
ANIMA AI Engineering Bootcamp — Chapter Notes PDF Generator
Additive textbook: add new chapters to CHAPTERS list, regenerate.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, HRFlowable, KeepTogether,
)

OUTPUT = "/mnt/user-data/outputs/anima_chapter_notes.pdf"

# ── Page geometry ──────────────────────────────────────────────────────────────
PW, PH = A4
ML = MR = 22 * mm
MT = MB = 26 * mm
TW = PW - ML - MR

# ── Color palette ──────────────────────────────────────────────────────────────
def c(h):
    return HexColor(h)

COL = dict(
    navy=c('#1B2B6B'),   blue=c('#3B82F6'),   indigo=c('#4338CA'),
    dark=c('#0F172A'),   body=c('#1E293B'),   gray=c('#64748B'),
    lgray=c('#94A3B8'),  border=c('#E2E8F0'), white=c('#FFFFFF'),
    amber=c('#D97706'),  green=c('#059669'),  off=c('#F8FAFC'),
    code_bg=c('#0F172A'), code_fg=c('#A8BFCF'), code_br=c('#334155'),
    lbl_bg=c('#1E293B'),
    note_bg=c('#FFFBEB'), note_bd=c('#D97706'), note_tx=c('#78350F'),
    mile_bg=c('#F0FDF4'), mile_bd=c('#059669'), mile_tx=c('#065F46'),
    tip_bg=c('#EFF6FF'),  tip_bd=c('#3B82F6'),  tip_tx=c('#1E40AF'),
)


# ── Style builder ──────────────────────────────────────────────────────────────
def build_styles():
    def ps(name, **kw):
        base = dict(fontName='Helvetica', fontSize=11, leading=17,
                    textColor=COL['body'], alignment=TA_LEFT)
        base.update(kw)
        return ParagraphStyle(name, **base)

    return {
        'Sec':    ps('Sec',    fontName='Helvetica-Bold', fontSize=15,
                     textColor=COL['navy'], leading=22, spaceBefore=18, spaceAfter=6),
        'SubSec': ps('SubSec', fontName='Helvetica-Bold', fontSize=12,
                     textColor=COL['dark'], leading=18, spaceBefore=12, spaceAfter=5),
        'Body':   ps('Body',   fontSize=10.5, textColor=COL['body'],
                     alignment=TA_JUSTIFY, leading=17, spaceAfter=10),
        'Bullet': ps('Bullet', fontSize=10.5, textColor=COL['body'],
                     leading=17, leftIndent=14, spaceAfter=4),
        'Code':   ps('Code',   fontName='Courier', fontSize=8.5,
                     textColor=COL['code_fg'], leading=13),
        'Gray':   ps('Gray',   fontSize=8.5, textColor=COL['lgray'],
                     alignment=TA_CENTER, leading=13),
        'NTitle': ps('NTitle', fontName='Helvetica-Bold', fontSize=10,
                     textColor=COL['note_tx'], leading=14),
        'NBody':  ps('NBody',  fontSize=10, textColor=COL['note_tx'], leading=15),
        'MTitle': ps('MTitle', fontName='Helvetica-Bold', fontSize=10,
                     textColor=COL['mile_tx'], leading=14),
        'MBody':  ps('MBody',  fontSize=10, textColor=COL['mile_tx'], leading=15, spaceAfter=3),
        'TTitle': ps('TTitle', fontName='Helvetica-Bold', fontSize=10,
                     textColor=COL['tip_tx'], leading=14),
        'TBody':  ps('TBody',  fontSize=10, textColor=COL['tip_tx'], leading=15),
    }


# ── Helpers ────────────────────────────────────────────────────────────────────
def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def ic(text):
    """Inline code span."""
    return f'<font face="Courier" size="9" color="#4338CA">{esc(text)}</font>'

def bold(text):
    return f'<b>{esc(text)}</b>'

def para(text, S, key='Body'):
    return Paragraph(text, S[key])

def sec(title, S):
    return [
        KeepTogether([
            Spacer(1, 4),
            Paragraph(title, S['Sec']),
            HRFlowable(width=TW, thickness=0.5, color=COL['border'], spaceAfter=8),
        ])
    ]

def subsec(title, S):
    return [Paragraph(title, S['SubSec'])]

def code_block(text, S, label=None):
    items = []
    if label:
        lp = Paragraph(
            f'<font face="Courier" size="8" color="#94A3B8">{esc(label)}</font>',
            S['Body']
        )
        lt = Table([[lp]], colWidths=[TW])
        lt.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), COL['lbl_bg']),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('RIGHTPADDING', (0, 0), (-1, -1), 12),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ]))
        items.append(lt)

    escaped = esc(text).replace('\n', '<br/>')
    cp = Paragraph(
        f'<font face="Courier" size="8.5" color="#A8BFCF">{escaped}</font>',
        S['Body']
    )
    ct = Table([[cp]], colWidths=[TW])
    ct.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), COL['code_bg']),
        ('BOX', (0, 0), (-1, -1), 0.5, COL['code_br']),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    items.append(ct)
    items.append(Spacer(1, 10))
    return items

def callout(title, lines, S, kind='note'):
    prefix = {'note': 'N', 'milestone': 'M', 'tip': 'T'}[kind]
    bgs = {'note': COL['note_bg'], 'milestone': COL['mile_bg'], 'tip': COL['tip_bg']}
    bds = {'note': COL['note_bd'], 'milestone': COL['mile_bd'], 'tip': COL['tip_bd']}
    content = []
    if title:
        content.append(Paragraph(title, S[f'{prefix}Title']))
        content.append(Spacer(1, 4))
    for line in lines:
        txt = line if line.startswith('<') else f'• {esc(line)}'
        content.append(Paragraph(txt, S[f'{prefix}Body']))
    t = Table([[content]], colWidths=[TW])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), bgs[kind]),
        ('LEFTPADDING', (0, 0), (-1, -1), 16),
        ('RIGHTPADDING', (0, 0), (-1, -1), 14),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('LINEBEFORE', (0, 0), (0, -1), 4, bds[kind]),
    ]))
    return [t, Spacer(1, 12)]

def bullets(items_list, S):
    result = []
    for item in items_list:
        if isinstance(item, tuple):
            text = f'{bold(item[0])}  {esc(item[1])}'
        else:
            text = item if item.startswith('<') else esc(item)
        result.append(Paragraph(f'• {text}', S['Bullet']))
    result.append(Spacer(1, 6))
    return result

def chapter_banner(num, title, phase, S):
    rows = [
        [Paragraph(f'<font size="11" color="#93C5FD"><b>Chapter {num}</b></font>', S['Body'])],
        [Paragraph(f'<font size="24" color="#FFFFFF"><b>{esc(title)}</b></font>', S['Body'])],
        [Paragraph(f'<font size="11" color="#93C5FD">{esc(phase)}</font>', S['Body'])],
    ]
    t = Table(rows, colWidths=[TW])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), COL['navy']),
        ('LEFTPADDING', (0, 0), (-1, -1), 18),
        ('RIGHTPADDING', (0, 0), (-1, -1), 18),
        ('TOPPADDING', (0, 0), (0, 0), 18),
        ('BOTTOMPADDING', (0, 2), (-1, 2), 20),
        ('TOPPADDING', (0, 1), (0, 2), 6),
        ('BOTTOMPADDING', (0, 0), (-1, 1), 0),
    ]))
    return t


# ── Page decorators ────────────────────────────────────────────────────────────
def on_cover(cv, doc):
    cv.saveState()

    # Full background
    cv.setFillColor(COL['navy'])
    cv.rect(0, 0, PW, PH, fill=1, stroke=0)

    # Decorative gradient strips
    for i, col_hex in enumerate(['#152460', '#1a2d73', '#1e3380', '#223990']):
        cv.setFillColor(c(col_hex))
        cv.rect(0, PH * 0.48 + i * 8, PW, 8, fill=1, stroke=0)

    # ANIMA wordmark
    cv.setFont('Helvetica-Bold', 60)
    cv.setFillColor(c('#FFFFFF'))
    cv.drawCentredString(PW / 2, PH - 108, 'ANIMA')

    # Tagline
    cv.setFont('Helvetica', 19)
    cv.setFillColor(c('#93C5FD'))
    cv.drawCentredString(PW / 2, PH - 148, 'AI Engineering Bootcamp')

    # Rule
    cv.setStrokeColor(c('#3B82F6'))
    cv.setLineWidth(2)
    cv.line(PW / 2 - 55 * mm, PH - 168, PW / 2 + 55 * mm, PH - 168)

    # Chapter Notes label
    cv.setFont('Helvetica', 14)
    cv.setFillColor(c('#CBD5E1'))
    cv.drawCentredString(PW / 2, PH - 190, 'Chapter Notes')

    # Info card
    card_y, card_h = PH * 0.36, 98
    cv.setFillColor(c('#0D1F42'))
    cv.roundRect(ML + 5, card_y, TW - 10, card_h, 6, fill=1, stroke=0)

    cv.setFont('Helvetica', 9)
    cv.setFillColor(c('#64748B'))
    cv.drawCentredString(PW / 2, card_y + card_h - 18, 'CURRENT PHASE')

    cv.setFont('Helvetica-Bold', 21)
    cv.setFillColor(c('#FFFFFF'))
    cv.drawCentredString(PW / 2, card_y + card_h - 44, 'Phase 1: Python Mastery')

    cv.setFont('Helvetica', 11)
    cv.setFillColor(c('#93C5FD'))
    cv.drawCentredString(PW / 2, card_y + card_h - 66, 'Chapters 1-2  .  Environment Setup  .  Type System')

    # Chapter count badge
    cv.setFillColor(c('#1D4ED8'))
    cv.roundRect(PW / 2 - 30, card_y + 10, 60, 22, 11, fill=1, stroke=0)
    cv.setFont('Helvetica-Bold', 11)
    cv.setFillColor(c('#FFFFFF'))
    cv.drawCentredString(PW / 2, card_y + 18, '2 Chapters')

    # Footer
    cv.setFont('Helvetica', 8)
    cv.setFillColor(c('#334155'))
    cv.drawCentredString(PW / 2, 25,
                         'ANIMA - The AI Character Engine  |  AI Engineering Bootcamp')
    cv.restoreState()


def on_page(cv, doc):
    cv.saveState()
    # Header rule
    cv.setStrokeColor(c('#E2E8F0'))
    cv.setLineWidth(0.5)
    cv.line(ML, PH - MT + 8 * mm, PW - MR, PH - MT + 8 * mm)
    cv.setFont('Helvetica', 8)
    cv.setFillColor(c('#94A3B8'))
    cv.drawString(ML, PH - MT + 10 * mm, 'ANIMA  |  AI Engineering Bootcamp')
    cv.drawRightString(PW - MR, PH - MT + 10 * mm, 'Chapter Notes  -  Phase 1')
    # Footer rule + page number
    cv.line(ML, MB - 6 * mm, PW - MR, MB - 6 * mm)
    cv.drawCentredString(PW / 2, MB - 10 * mm, str(doc.page))
    cv.restoreState()


# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER CONTENT
# ══════════════════════════════════════════════════════════════════════════════

CHAPTERS = [

    # ── Chapter 1 ─────────────────────────────────────────────────────────────
    {
        'num': 1,
        'title': 'Environment Setup & Project Scaffold',
        'phase': 'Phase 1 - Python Mastery',
        'tagline': (
            'Before a single line of AI code is written, every professional engineer '
            'builds the same thing first: a clean, reproducible, isolated development '
            'environment. This chapter is that foundation.'
        ),

        # ── 1. Intro ──────────────────────────────────────────────────────────
        'intro': (
            'The Python ecosystem is rich but historically fragmented. Different projects '
            'need different Python versions; libraries have conflicting transitive '
            'dependencies; without discipline, a development machine turns into a graveyard '
            'of broken environments. In production AI systems -- where torch, transformers, '
            'langchain, and pinecone all coexist -- this fragmentation has real cost. A '
            f'silent downgrade of a transitive dependency can break a model pipeline at 2 AM. '
            'The answer is environmental discipline from day one.'
        ),
        'intro2': (
            f'In 2024-2025, the Python tooling ecosystem converged on a single answer: '
            f'{ic("uv")}, a Rust-powered package manager and environment tool that replaces '
            f'{ic("pyenv")}, {ic("pip")}, {ic("virtualenv")}, {ic("pip-tools")}, and {ic("Poetry")} '
            'in one binary. uv is 10-100x faster than pip and uses the PEP 621 standard '
            f'{ic("pyproject.toml")} format natively. ANIMA uses uv from day one.'
        ),

        # ── 2. What you will learn ────────────────────────────────────────────
        'learn': [
            'What a Python virtual environment is and why every project needs one',
            f'Why {ic("uv")} has replaced pyenv + pip + Poetry for modern AI projects',
            f'The PEP 621 {ic("pyproject.toml")} format -- Python\'s official project metadata standard',
            f'The {ic("src/")} directory layout used by all serious Python libraries',
            'How to configure VS Code for Python AI engineering',
            f'How to write and run your first tests with {ic("pytest")} via {ic("uv run")}',
            f'The {ic("uv.lock")} lockfile and why reproducibility is non-negotiable',
            'The complete ANIMA project scaffold that all 85 chapters build upon',
        ],

        # ── 3. Detailed explanation ───────────────────────────────────────────
        'explanation': [
            ('subsec', 'The Problem: Dependency Chaos'),
            ('body', (
                'Every Python library you install places files into a shared directory. '
                'When two projects need different versions of the same library -- a common '
                'situation in AI where langchain evolves rapidly -- they conflict. The '
                'solution is virtual environments: isolated directories containing a '
                'private Python interpreter and private package store. '
                f'{ic("uv")} creates these automatically when you run {ic("uv sync")} or '
                f'{ic("uv add")}. You never create them manually.'
            )),

            ('subsec', 'uv: One Tool to Rule Them All'),
            ('body', (
                f'{ic("uv")} is written in Rust and maintained by Astral (the same team '
                f'behind {ic("ruff")}, which is already in our toolchain). It handles: '
                'Python version management, virtual environment creation, package '
                'installation, dependency resolution, lockfile generation, and package '
                'building -- all through a single binary. Before uv, achieving this '
                'required combining pyenv, virtualenv, pip-tools, and Poetry. '
                'uv replaces all four.'
            )),
            ('code', 'bash', (
                '# Install uv -- single command, no Python required first\n'
                'curl -LsSf https://astral.sh/uv/install.sh | sh\n'
                '\n'
                '# Create the ANIMA library project (src/ layout, Python 3.12)\n'
                'uv init --lib anima --python 3.12\n'
                '\n'
                '# Add dev dependencies (updates pyproject.toml + creates uv.lock)\n'
                'uv add --dev pytest pytest-asyncio ruff mypy\n'
                '\n'
                '# Run commands in the project environment\n'
                'uv run pytest          # run tests\n'
                'uv run ruff check src/ # lint\n'
                'uv run mypy src/       # type check'
            )),

            ('subsec', 'PEP 621: The Modern pyproject.toml'),
            ('body', (
                f'Before PEP 621, each tool used its own project metadata format. '
                f'{ic("Poetry 1.x")} used {ic("[tool.poetry]")}; setuptools used '
                f'{ic("setup.py")}. PEP 621 (2021) standardized everything under '
                f'the {ic("[project]")} table. Dev-only dependencies live in '
                f'{ic("[dependency-groups]")} per PEP 735. uv generates this format '
                'natively when you run '
                f'{ic("uv init --lib")}.'
            )),
            ('code', 'project/anima/pyproject.toml', (
                '[project]\n'
                'name = "anima"\n'
                'version = "0.1.0"\n'
                'description = "AI Character Engine"\n'
                'requires-python = ">=3.12"\n'
                'dependencies = []\n'
                '\n'
                '[dependency-groups]\n'
                'dev = [\n'
                '    "pytest>=8.0",\n'
                '    "pytest-asyncio>=0.23",\n'
                '    "ruff>=0.5",\n'
                '    "mypy>=1.10",\n'
                ']\n'
                '\n'
                '[build-system]           # auto-generated by uv init --lib\n'
                'requires = ["uv_build>=0.x,<0.y"]\n'
                'build-backend = "uv_build"\n'
                '\n'
                '[tool.ruff.lint]\n'
                'select = ["E", "F", "I", "N", "UP", "B", "C4", "RUF"]\n'
                '\n'
                '[tool.mypy]\n'
                'disallow_untyped_defs = true\n'
                'ignore_missing_imports = true'
            )),

            ('subsec', 'The src/ Layout'),
            ('body', (
                f'The {ic("src/")} layout places package code inside '
                f'{ic("src/anima/")} rather than at the project root. This forces '
                'imports to resolve against the installed package -- not the local '
                'filesystem. It catches import errors at development time rather than '
                'at deployment. It also cleanly separates distributable code (what '
                f'{ic("uv build")} packages) from tests, config, and dev tooling.'
            )),
            ('code', 'project/anima/ structure', (
                'project/anima/\n'
                'project/anima/pyproject.toml     # project metadata + tool config\n'
                'project/anima/uv.lock            # exact pinned versions -- COMMIT THIS\n'
                'project/anima/.python-version    # "3.12"\n'
                'project/anima/.venv/             # managed by uv -- do NOT commit\n'
                'project/anima/src/\n'
                'project/anima/src/anima/\n'
                'project/anima/src/anima/__init__.py  # __version__ = "0.1.0"\n'
                'project/anima/src/anima/core/        # Character engine (Phase 1+)\n'
                'project/anima/src/anima/memory/      # Vector memory (Phase 7+)\n'
                'project/anima/src/anima/agents/      # Agent system (Phase 11+)\n'
                'project/anima/src/anima/api/         # FastAPI server (Phase 14+)\n'
                'project/anima/src/anima/models/      # Pydantic models (Phase 6+)\n'
                'project/anima/src/anima/utils/       # Shared utilities\n'
                'project/anima/tests/\n'
                'project/anima/tests/test_package.py  # 3 passing tests'
            )),

            ('subsec', 'Key Command Reference'),
            ('code', 'uv command reference', (
                'uv add openai            # add runtime dependency\n'
                'uv add --dev pytest      # add dev-only dependency\n'
                'uv remove openai         # remove dependency\n'
                'uv sync                  # install all deps, create .venv\n'
                'uv run pytest            # run command in project env\n'
                'uv lock --upgrade        # update all packages to latest\n'
                'uv python install 3.12   # install Python 3.12 via uv\n'
                'uv build                 # build wheel and sdist\n'
                'uv self update           # update uv itself'
            )),
        ],

        # ── 4. Explain like I'm 12 ────────────────────────────────────────────
        'analogies': [
            (
                'Virtual environments = separate backpacks',
                'Imagine you have three hobbies: painting, cooking, and coding. '
                'Each needs completely different supplies. If you threw paint brushes, '
                'spatulas, and keyboards into one bag, you\'d have a mess. Virtual '
                'environments are separate backpacks: one for each project. The painting '
                'bag has painting supplies. The cooking bag has cooking supplies. '
                'They never mix, never conflict.'
            ),
            (
                'uv = a magical backpack organizer',
                'uv is like a magical butler who (1) figures out which backpack you need '
                'for today\'s project, (2) automatically orders any missing supplies -- '
                'exact brands and sizes -- from the internet, (3) photographs the perfect '
                'backpack arrangement so it can be recreated identically in any school '
                'in the world, and (4) does all of this in about 3 seconds.'
            ),
            (
                'pyproject.toml = an official recipe card',
                'Instead of scribbling "need some Python and some libraries" on a napkin, '
                'pyproject.toml is an official printed recipe card: "Serves: Python 3.12+. '
                'Ingredients: openai library version 1.x, pydantic version 2.x." Anyone '
                'who reads it knows exactly what to prepare. No guessing.'
            ),
            (
                'uv.lock = a photo of the perfect dish',
                'After cooking something perfectly, you photograph every ingredient -- '
                'exact brand, exact amount. That\'s uv.lock. It captures "openai version '
                '1.35.3, httpx version 0.27.0..." so that two weeks from now, in a '
                'different kitchen, on a different continent, the exact same dish appears.'
            ),
            (
                'The src/ layout = a proper shop with a back room',
                'A professional bakery has a front counter (clean, organized, what '
                'customers see) and a back room (where the actual work happens). '
                'The src/ layout is that: the front counter is src/anima/ (what gets '
                'installed when someone does "uv add anima"). The back room is your '
                'tests, config files, and dev tools -- they stay behind the scenes.'
            ),
        ],

        # ── 5. ANIMA milestone ────────────────────────────────────────────────
        'milestone': [
            'project/anima/ created with uv init --lib anima --python 3.12',
            'pyproject.toml configured: [project] table, [dependency-groups] dev, tool configs for ruff + mypy + pytest',
            'Six submodules created: core/, memory/, agents/, api/, models/, utils/ -- each with __init__.py',
            'src/anima/__init__.py written with __version__ = "0.1.0"',
            'uv.lock generated and committed to version control',
            'Three passing tests: version_exists, version_format, submodules_importable',
            '.vscode/settings.json configured with correct Python interpreter path',
            'First commit pushed to GitHub: "Chapter 1: ANIMA project scaffold"',
        ],
    },

    # ── Chapter 2 ─────────────────────────────────────────────────────────────
    {
        'num': 2,
        'title': 'Type Hints & the Typing System',
        'phase': 'Phase 1 - Python Mastery',
        'tagline': (
            'Python\'s dynamic typing is a feature -- until you\'re debugging a '
            'character engine with 30 modules at midnight. Type hints let you have '
            'the flexibility of Python and the safety of a typed language.'
        ),

        # ── 1. Intro ──────────────────────────────────────────────────────────
        'intro': (
            'Python has been dynamically typed since its creation. You never declare '
            'types; you just use variables. This is excellent for 50-line scripts and '
            'rapid prototyping. In a 10,000-line AI system with 30 interacting modules '
            '-- where character data flows through memory stores, agent orchestrators, '
            'and API handlers -- dynamic typing becomes invisible danger. A function '
            'receives None when it expected a list; a dict has the wrong key name; '
            'a string is passed where a float is required. These errors happen at '
            'runtime, often in production, after hours of confused debugging.'
        ),
        'intro2': (
            f'Python\'s type hint system (PEP 484, 2015 -- dramatically improved '
            'through Python 3.12) lets you annotate what types your code works with. '
            'The annotations have no performance cost at runtime -- Python remains '
            'dynamic. What they enable is static analysis: tools like '
            f'{ic("mypy")} and VS Code\'s Pylance read your annotations and report '
            'type errors before a single line executes. For ANIMA, every module, '
            'every function, and every class is typed from Chapter 2 onward.'
        ),

        # ── 2. What you will learn ────────────────────────────────────────────
        'learn': [
            f'Why {ic("from __future__ import annotations")} belongs at the top of every file',
            f'The modern union syntax: {ic("X | None")} instead of {ic("Optional[X]")}',
            f'Collection generics: {ic("list[X]")}, {ic("dict[K, V]")}, {ic("tuple[X, ...]")}',
            f'{ic("TypeVar")} for generic functions and classes',
            f'{ic("Protocol")} for structural subtyping (duck typing with type safety)',
            f'{ic("TypedDict")} for dictionaries with known shapes',
            f'{ic("Annotated")} for types with metadata (the foundation of Pydantic and FastAPI)',
            f'{ic("TYPE_CHECKING")} guard for avoiding circular imports',
            f'{ic("Literal")}, {ic("Final")}, {ic("ClassVar")} for constrained values',
            f'Python 3.12\'s {ic("type")} statement for clean type aliases',
        ],

        # ── 3. Detailed explanation ───────────────────────────────────────────
        'explanation': [
            ('subsec', 'The Foundation: from __future__ import annotations'),
            ('body', (
                f'Every Python file in ANIMA starts with {ic("from __future__ import annotations")}. '
                'This PEP 563 directive changes how Python processes annotations: instead of '
                'evaluating them eagerly at module load time, they are stored as strings and '
                'only evaluated when explicitly requested. This enables two things: forward '
                'references (a class can reference itself in its own type hints) and '
                'avoidance of circular import errors at runtime.'
            )),
            ('code', 'The forward reference problem -- solved by __future__', (
                'from __future__ import annotations\n'
                '\n'
                '# Without __future__: NameError -- Character not defined yet\n'
                '# With __future__: works -- annotation stored as string "Character"\n'
                'class Character:\n'
                '    def clone(self) -> Character:  # forward reference: fine!\n'
                '        return Character(self.name)'
            )),

            ('subsec', 'Union Types and Optional'),
            ('body', (
                f'Python 3.10 introduced {ic("X | Y")} union syntax. Use it. '
                f'{ic("Optional[X]")} is identical to {ic("X | None")} is identical to '
                f'{ic("Union[X, None]")} -- they are exactly equivalent. The new syntax '
                'requires no import and reads more naturally.'
            )),
            ('code', 'Union syntax: old vs new', (
                '# Old syntax (pre-3.10) -- valid, seen in legacy code\n'
                'from typing import Optional, Union\n'
                'def old(name: Optional[str] = None) -> Union[str, int]: ...\n'
                '\n'
                '# New syntax (3.10+) -- use this in ANIMA\n'
                'def new(name: str | None = None) -> str | int: ...\n'
                '\n'
                '# Nested unions are still readable\n'
                'def process(data: str | bytes | None) -> dict[str, int] | None: ...'
            )),

            ('subsec', 'Collection Types'),
            ('body', (
                f'Since Python 3.9, use built-in types directly as generics. '
                f'No need to import {ic("List")}, {ic("Dict")}, {ic("Tuple")} from typing. '
                f'For abstract interfaces, use {ic("collections.abc")} -- '
                f'{ic("Sequence")} accepts any list-like, {ic("Mapping")} accepts any dict-like, '
                f'{ic("Callable")} accepts any callable.'
            )),
            ('code', 'Collection type annotations', (
                'from __future__ import annotations\n'
                'from collections.abc import Sequence, Mapping, Callable\n'
                '\n'
                'names: list[str] = []\n'
                'scores: dict[str, float] = {}\n'
                'pair: tuple[int, str] = (1, "hello")\n'
                'unique: set[int] = {1, 2, 3}\n'
                '\n'
                '# Abstract interfaces (more flexible than concrete types)\n'
                'def process(items: Sequence[str]) -> Mapping[str, int]:\n'
                '    return {item: len(item) for item in items}\n'
                '\n'
                '# Callable[[arg_types], return_type]\n'
                'def apply(func: Callable[[str, int], bool]) -> None: ...'
            )),

            ('subsec', 'TypeVar and Generic Functions'),
            ('body', (
                f'{ic("TypeVar")} links the types of two or more parameters/returns. '
                f'If a function accepts a {ic("list[T]")} and returns a {ic("T")}, '
                'mypy knows the return type matches the element type. '
                f'Python 3.12 added native generic syntax ({ic("[T]")} in brackets), '
                'eliminating the need to declare TypeVar separately.'
            )),
            ('code', 'TypeVar for generic functions (old and new syntax)', (
                'from typing import TypeVar\n'
                '\n'
                '# Classic syntax (works everywhere)\n'
                'T = TypeVar("T")\n'
                'def first(items: list[T]) -> T:\n'
                '    return items[0]\n'
                '\n'
                '# Python 3.12+ syntax (cleaner, use in ANIMA)\n'
                'def first[T](items: list[T]) -> T:\n'
                '    return items[0]\n'
                '\n'
                '# Generic class (3.12+)\n'
                'class Repository[T]:\n'
                '    def __init__(self) -> None:\n'
                '        self._items: list[T] = []\n'
                '    def add(self, item: T) -> None:\n'
                '        self._items.append(item)\n'
                '    def get(self, idx: int) -> T:\n'
                '        return self._items[idx]'
            )),

            ('subsec', 'Protocol: Structural Subtyping'),
            ('body', (
                f'{ic("Protocol")} defines an interface through methods and attributes -- '
                'without requiring explicit inheritance. Any class that has the right '
                'methods automatically satisfies the Protocol. This is Python\'s type-safe '
                'version of duck typing. In ANIMA, Protocols define contracts for '
                'character behaviors that different backends (local, Redis, Pinecone) '
                'implement without inheriting from a common base class.'
            )),
            ('code', 'Protocol example for ANIMA character behaviors', (
                'from __future__ import annotations\n'
                'from typing import Protocol, runtime_checkable\n'
                '\n'
                '@runtime_checkable\n'
                'class Memorable(Protocol):\n'
                '    """Any object with these two methods satisfies this Protocol."""\n'
                '    def remember(self, event: str, importance: float) -> None: ...\n'
                '    def recall(self, query: str, limit: int = 5) -> list[str]: ...\n'
                '\n'
                '# No inheritance -- just implement the methods\n'
                'class LocalMemoryStore:\n'
                '    def remember(self, event: str, importance: float) -> None: ...\n'
                '    def recall(self, query: str, limit: int = 5) -> list[str]: ...\n'
                '\n'
                'def use_memory(m: Memorable) -> None: ...  # accepts LocalMemoryStore\n'
                'isinstance(LocalMemoryStore(), Memorable)  # True (runtime_checkable)'
            )),

            ('subsec', 'TypedDict, Annotated, TYPE_CHECKING, and Literals'),
            ('body', (
                f'{ic("TypedDict")} defines the exact shape of a dictionary: which keys '
                f'exist and what types they map to. mypy catches wrong key names and wrong '
                f'value types. {ic("Annotated")} attaches metadata to a type -- ignored by '
                f'mypy, but read by Pydantic (Chapter 6) and FastAPI (Chapter 14) to add '
                f'validation and documentation. {ic("TYPE_CHECKING")} guards imports that '
                'only need to exist for type checkers, avoiding circular import errors. '
                f'{ic("Literal")} constrains a value to specific options; {ic("Final")} '
                f'marks a constant; {ic("ClassVar")} marks a class-level attribute.'
            )),
            ('code', 'TypedDict, Annotated, TYPE_CHECKING, Literal, Final', (
                'from __future__ import annotations\n'
                'from typing import (\n'
                '    TYPE_CHECKING, Annotated, TypedDict,\n'
                '    Literal, Final, ClassVar,\n'
                ')\n'
                '\n'
                'if TYPE_CHECKING:\n'
                '    from anima.memory.store import MemoryStore  # safe: not evaluated at runtime\n'
                '\n'
                'class PersonalityProfile(TypedDict):\n'
                '    openness: float\n'
                '    conscientiousness: float\n'
                '    extraversion: float\n'
                '\n'
                'EmotionalState = Literal["happy", "sad", "angry", "neutral", "curious"]\n'
                '\n'
                'MAX_MEMORIES: Final[int] = 10_000\n'
                '\n'
                'Score = Annotated[float, "must be 0.0 to 1.0"]  # Pydantic reads this later\n'
                '\n'
                '# Python 3.12 type aliases\n'
                'type CharacterID = str\n'
                'type Embedding = list[float]'
            )),

            ('subsec', 'The Full Typed Character Module'),
            ('body', (
                'Putting it all together: the first real typed module in ANIMA. '
                f'Create this at {ic("src/anima/core/character.py")} and verify '
                f'it passes both {ic("uv run mypy src/")} and '
                f'{ic("uv run ruff check src/")} with no errors.'
            )),
            ('code', 'src/anima/core/character.py', (
                'from __future__ import annotations\n'
                'from typing import TYPE_CHECKING, Annotated, ClassVar, Final, Literal, TypedDict\n'
                '\n'
                'if TYPE_CHECKING:\n'
                '    from anima.memory.store import MemoryStore\n'
                '\n'
                'type CharacterID = str\n'
                'type PersonalityScore = float\n'
                'EmotionalState = Literal["neutral","happy","sad","angry","curious","excited"]\n'
                'PersonalityDimension = Literal["openness","conscientiousness",\n'
                '                               "extraversion","agreeableness","neuroticism"]\n'
                '\n'
                'class PersonalityProfile(TypedDict):\n'
                '    openness: PersonalityScore\n'
                '    conscientiousness: PersonalityScore\n'
                '    extraversion: PersonalityScore\n'
                '    agreeableness: PersonalityScore\n'
                '    neuroticism: PersonalityScore\n'
                '\n'
                'MAX_NAME_LENGTH: Final[int] = 100\n'
                'DEFAULT_STATE: Final[EmotionalState] = "neutral"\n'
                '\n'
                'class Character:\n'
                '    _registry: ClassVar[dict[CharacterID, Character]] = {}\n'
                '\n'
                '    def __init__(self, name: str,\n'
                '                 emotional_state: EmotionalState = DEFAULT_STATE) -> None:\n'
                '        self.name: str = name\n'
                '        self.id: CharacterID = name.lower().replace(" ", "_")\n'
                '        self.emotional_state: EmotionalState = emotional_state\n'
                '        self._memory: MemoryStore | None = None\n'
                '\n'
                '    def update_emotion(self, state: EmotionalState) -> None:\n'
                '        self.emotional_state = state\n'
                '\n'
                '    @classmethod\n'
                '    def get(cls, cid: CharacterID) -> Character | None:\n'
                '        return cls._registry.get(cid)'
            )),
        ],

        # ── 4. Explain like I'm 12 ────────────────────────────────────────────
        'analogies': [
            (
                'Type hints = labels on kitchen jars',
                'You have three jars: SUGAR, SALT, FLOUR. Python doesn\'t stop you from '
                'putting salt in the SUGAR jar -- it\'s still just a jar. But your '
                'kitchen robot (mypy) checks all the labels before cooking begins. '
                'If someone reaches for the SUGAR jar but is holding a salt shaker, '
                'the robot says: "Wait! That looks like salt, not sugar!" Before the '
                'cake is ruined. That\'s what mypy does with type hints.'
            ),
            (
                'TypeVar = a copy machine with a promise',
                'TypeVar says: "Whatever shape you put in the top, you get the same '
                'shape out the bottom." Put in a circle, get a circle. Put in a triangle, '
                'get a triangle. The machine doesn\'t care what shape -- it just promises '
                'consistency. In Python: put in a list of numbers, get a number back. '
                'Put in a list of strings, get a string back.'
            ),
            (
                'Protocol = a job posting, not a school requirement',
                '"We need someone who can: speak French AND play piano." The job posting '
                'doesn\'t say "must have graduated from Juilliard." Anyone who can do '
                'both things gets the job. Protocol works the same way: any class that '
                'has the right methods automatically qualifies -- regardless of where '
                'it came from or what it inherits from.'
            ),
            (
                'TypedDict = a paper form with specific blanks',
                'A form says: "Name: [text only]. Age: [number only]. City: [text only]." '
                'You can\'t write your phone number where your name should go -- the form '
                'won\'t accept it. TypedDict is that form for dictionaries: specific keys, '
                'specific value types. mypy catches it if you mix them up.'
            ),
            (
                'Optional (X | None) = "maybe yes, maybe no"',
                'When a restaurant asks "Do you want extra sauce?" your answer is either '
                '"Yes, please!" (a Sauce object) or "No thanks" (None). If the cook only '
                'prepares for "yes" and someone says "no", disaster. {ic("str | None")} '
                'means your code must handle both cases -- or mypy will warn you.'
            ),
        ],

        # ── 5. ANIMA milestone ────────────────────────────────────────────────
        'milestone': [
            'src/anima/core/character.py created with full type annotations',
            'CharacterID, PersonalityScore, EmotionalIntensity type aliases defined using the type keyword',
            'PersonalityProfile TypedDict defined with all five Big Five dimensions',
            'EmotionalState Literal type defined with 7 possible emotional states',
            'Character class with typed attributes: id (CharacterID), name (str), emotional_state (EmotionalState)',
            '_memory: MemoryStore | None annotation using TYPE_CHECKING guard (no circular import)',
            'update_emotion() and adjust_trait() methods with full annotations',
            'All code passes uv run mypy src/ with zero errors',
            'All code passes uv run ruff check src/ with zero errors',
        ],
    },
]


# ══════════════════════════════════════════════════════════════════════════════
# PDF BUILDER
# ══════════════════════════════════════════════════════════════════════════════

def build_chapter(ch: dict, S: dict) -> list:
    story = []

    # Chapter banner
    story.append(chapter_banner(ch['num'], ch['title'], ch['phase'], S))
    story.append(Spacer(1, 10))

    # Tagline
    story.append(Paragraph(ch['tagline'], S['Body']))
    story.append(HRFlowable(width=TW, thickness=0.5, color=COL['border'], spaceAfter=6))
    story.append(Spacer(1, 4))

    # ── Section 1: Introduction ────────────────────────────────────────────────
    story.extend(sec('1. Introduction', S))
    story.append(Paragraph(ch['intro'], S['Body']))
    if ch.get('intro2'):
        story.append(Paragraph(ch['intro2'], S['Body']))

    # ── Section 2: What you will learn ────────────────────────────────────────
    story.extend(sec('2. What You Will Learn', S))
    story.extend(bullets(ch['learn'], S))

    # ── Section 3: Detailed Explanation ───────────────────────────────────────
    story.extend(sec('3. Detailed Explanation', S))
    for item in ch['explanation']:
        kind = item[0]
        if kind == 'subsec':
            story.extend(subsec(item[1], S))
        elif kind == 'body':
            story.append(Paragraph(item[1], S['Body']))
        elif kind == 'code':
            story.extend(code_block(item[2], S, label=item[1]))

    # ── Section 4: Explained Simply ───────────────────────────────────────────
    story.extend(sec('4. Explained Simply', S))
    story.append(Paragraph(
        'Technical concepts explained with everyday analogies.',
        S['Body']
    ))
    story.append(Spacer(1, 6))
    for title, explanation in ch['analogies']:
        story.extend(subsec(title, S))
        story.append(Paragraph(explanation, S['Body']))

    # ── Section 5: ANIMA Milestone ────────────────────────────────────────────
    story.extend(sec(f'5. ANIMA Project — Chapter {ch["num"]} Milestone', S))
    story.append(Paragraph(
        f'Complete all items below before starting Chapter {ch["num"] + 1}.',
        S['Body']
    ))
    story.append(Spacer(1, 6))
    story.extend(callout(
        f'Chapter {ch["num"]} Deliverables',
        [f'[ ]  {m}' for m in ch['milestone']],
        S,
        kind='milestone',
    ))

    story.append(PageBreak())
    return story


def build_pdf():
    S = build_styles()

    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=A4,
        leftMargin=ML, rightMargin=MR,
        topMargin=MT, bottomMargin=MB,
        title='ANIMA AI Engineering Bootcamp — Chapter Notes',
        author='AI Engineering Bootcamp',
        subject='Phase 1: Python Mastery',
    )

    story = []

    # Cover page -- drawn entirely by on_cover callback on the canvas.
    # A tiny spacer + PageBreak creates page 1 without a LayoutError.
    story.append(Spacer(1, 0.1))
    story.append(PageBreak())

    # Table of Contents
    story.append(Spacer(1, 10))
    story.append(Paragraph('Contents', ParagraphStyle(
        'TOCHead', fontName='Helvetica-Bold', fontSize=22,
        textColor=COL['navy'], leading=30, spaceAfter=14
    )))
    story.append(HRFlowable(width=TW, thickness=1, color=COL['blue'], spaceAfter=12))

    for ch in CHAPTERS:
        story.append(Paragraph(
            f'Chapter {ch["num"]}  —  {ch["title"]}',
            ParagraphStyle('TOCEntry', fontName='Helvetica', fontSize=12,
                           textColor=COL['body'], leading=22)
        ))
        subs = ['Introduction', 'What You Will Learn',
                'Detailed Explanation', 'Explained Simply', 'ANIMA Milestone']
        for sub in subs:
            story.append(Paragraph(
                f'    {sub}',
                ParagraphStyle('TOCSub', fontName='Helvetica', fontSize=10,
                               textColor=COL['gray'], leading=16, leftIndent=16)
            ))
        story.append(Spacer(1, 8))

    story.append(PageBreak())

    # Chapters
    for ch in CHAPTERS:
        story.extend(build_chapter(ch, S))

    doc.build(story, onFirstPage=on_cover, onLaterPages=on_page)
    print(f'PDF generated: {OUTPUT}')


if __name__ == '__main__':
    build_pdf()
