# Golden Rules English Trainer

Current version: **4.0.0**. The canonical Codex skill is [`SKILL.md`](SKILL.md). Codex discovers it through the repository link `.agents/skills/golden-rules-english-trainer`; edit this canonical directory rather than creating a second skill.

The trainer teaches Persian-coded English grammar at A2 by default, keeps B1 extensions optional, and uses English-only exercise instructions and questions. The full v4 specification and QA references live under [`references/`](references/). The live topic catalog is in [`references/topic_catalog.md`](references/topic_catalog.md). Text-only practice is governed by [`references/text_quiz.md`](references/text_quiz.md); native controls are used only when their behavior is actually supported and verified.

Run the validator from the repository root with:

```sh
python3 golden-rules/skills/golden-rules-english-trainer/scripts/validate_skill.py
```

Questions, answer keys, attempts, scores, and learner progress are not committed.
