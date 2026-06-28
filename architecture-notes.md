# Architecture Notes: Chapter [N] — [TITLE]

*ANIMA Design Record · Phase [N] · [Date]*

---

## Decision

**What was built:** [One sentence describing the concrete architectural addition to ANIMA in this chapter]

**Status:** Accepted

---

## Context

*Why did this chapter require an architectural decision for ANIMA?*

[2–3 sentences: the problem that needed to be solved, why the naive approach wasn't good enough, what constraints existed.]

---

## Options Considered

| Option | Approach | Pros | Cons |
|--------|----------|------|------|
| A | [Description] | [Advantages] | [Disadvantages] |
| B | [Description] | [Advantages] | [Disadvantages] |
| **C (chosen)** | **[Description]** | **[Advantages]** | **[Disadvantages]** |

---

## The Decision

[Why option C was chosen. Reason from first principles — not "because the tutorial said so" but because of specific requirements, constraints, or trade-offs. 2–4 sentences.]

---

## Implementation

The key addition to ANIMA in this chapter:

```python
# [Brief description of what this is]
[code snippet — the architectural addition, not the whole file]
```

**Where this lives in the repo:** `project/anima/[path/to/file.py]`

---

## Impact on Future Phases

- **Enables (Phase [N+X]):** [What future capability this decision makes possible]
- **Constrains (Phase [N+Y]):** [What this decision rules out or limits going forward]

---

## Revision Conditions

[Under what circumstances should this decision be revisited? E.g., "Reconsider if ANIMA needs to support more than 1,000 concurrent characters — at that scale, [alternative] becomes more attractive."]

---

*This is part of the running ANIMA Architecture Decision Log. See `project/architecture/decision-log.md` for all decisions chronologically.*
