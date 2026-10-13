# Native quiz control boundary (v4)

Use interactive quiz controls only when the current ChatGPT/Codex interface actually exposes them and their behavior is verified. Never infer support from a skill document or promise GenUI, buttons, hidden state, or instant navigation that the current interface does not provide.

When verified controls are available, their behavior must match `references/text_quiz.md`: answer keys remain hidden until grading, Reset preserves the exact current set and clears grading, and New Set creates new questions with the selected settings. Keep all exercise text in English, make feedback accessible without color alone, and do not persist learner answers, scores, or progress.

When controls are unavailable or uncertain, use the text-only flow in `references/text_quiz.md`.
