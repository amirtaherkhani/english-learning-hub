# Requirements coverage

The complete 54-section v4.0.0 source specification is preserved in `full-specification-v4.md`. The operational skill summarizes and applies it. This map points to the project files that implement the major requirement groups.

| Requirement | Implemented in |
|---|---|
| Native conversation output; no unrequested HTML or files | `SKILL.md` — Practice and interaction; full spec GR-001 |
| Persian teaching and English-only exercise fields | `SKILL.md` — Scope and practice; full spec GR-002 and 16 |
| A1/A2 core, A2 default, optional B1 | `SKILL.md` — Learner level; full spec GR-003 |
| Topic classification and adaptive lesson architecture | `SKILL.md` — Learner level; full spec sections 3–4 |
| Persian mental code, contrasts, five-second method | `SKILL.md` — Learner level; full spec sections 4, 10, 13 |
| Topic-relevant forms, tenses, category analysis | `SKILL.md` — Learner level; full spec sections 5–8 |
| Strict rules, tendencies, context, exceptions | `SKILL.md` — Learner level; full spec sections 9, 12, 44 |
| Coursebook exercise formats and context | `SKILL.md` — Practice and interaction; full spec sections 17–18 |
| Ambiguity prevention and valid alternatives | `SKILL.md` — Practice and interaction; full spec sections 19, 22, 27 |
| Difficulty and question counts | `SKILL.md` — Practice and interaction; full spec sections 14–15 |
| Fresh sets and concept coverage | `SKILL.md` — Practice and interaction; full spec sections 20–21 |
| Reset/New Set and batch behavior | `references/text_quiz.md`; full spec sections 24–25 |
| Progressive hints, grading, and feedback | `SKILL.md` — Practice and interaction; full spec sections 26–31 |
| Adaptive practice, mastery, spaced review | `SKILL.md` — Practice and interaction; full spec sections 32–35 |
| Lesson pacing and progression | `SKILL.md` — Learner level; full spec section 36 |
| RTL/LTR, punctuation, accessibility, readability | `SKILL.md` — Language and presentation; full spec sections 37–42 |
| Commands, prerequisites, and personalization boundaries | `SKILL.md` — Practice and interaction; full spec sections 46–49 |
| QA and definition of done | `references/qa-checklist.md`; full spec sections 50–53 |
| Local structural and content validation | `scripts/validate_skill.py` |

The supplied `good-well-a2-sample.md` and `good-well-a2-answer-key.md` were used as private authoring/QA references. They are intentionally excluded from the repository because `docs/PUBLISHING_POLICY.md` keeps practice questions and answers in the live conversation.
