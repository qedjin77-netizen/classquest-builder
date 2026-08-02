# Document Set Validation

## Release

- Version: **2.0**
- Generated: **2026-08-02**
- Intended use: GitHub repository document baseline
- Markdown files: **26**
- Relative Markdown links checked: **42**
- Broken relative links: **0**
- Stale operational path references: **0**

## Verified structure

- Current work: `tasks/`
- Sprint change history: `changelog/`
- Architecture decisions: `decisions/`
- Product and technical documents: `docs/`
- Current Sprint plans: `docs/sprints/`
- Replaced plans: `docs/archive/`
- Automated validator: `scripts/validate_documents.py`

## Core numeric rules checked

- Rooms per game: 3
- Questions per room: 3–5
- Questions per game: 9–15
- Maximum students per session: 30
- Team count: 2–6
- Hint unlock: same student, same question, after 2 wrong attempts
- MVP target: 3 months

## Validation result

**PASS**

- All Markdown relative links resolve.
- No known stale operational file paths remain.
- Document names and folder references use the v2.0 structure.
- Duplicate document-conflict sections were merged.
- Excluded MVP features are not represented as actionable Backlog checkboxes.

## Re-run validation

From the repository root:

```bash
python scripts/validate_documents.py
```
