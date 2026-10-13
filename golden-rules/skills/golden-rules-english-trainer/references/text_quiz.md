# Text quiz contract for Codex (v4)

Use this contract when the conversation does not expose verified native quiz controls.

## Start

- Read `topic_catalog.md` when a topic is missing; offer a short choice from the real catalog rather than inventing topics.
- Default to A2 and Normal difficulty. Use 5 questions for short practice and 10 for comprehensive practice. Honor requested topics, level, difficulty, and count.
- Show one set at a time unless the learner requests a batch. If several sets are requested, keep each distinct and label what remains.
- State the selected difficulty before the set. Write every exercise instruction, stem, context, and option in English. Persian may appear in the lesson and after-submission feedback.
- Number questions and label options A/B/C/D. Check that each single-answer item has exactly one valid answer in context. Do not reveal the key or explanations before submission.

## Grade and navigate

- Accept clear answers such as `1B, 2A, 3C`. Ask for missing answers before grading if the instruction requires all items.
- Grade grammar and meaning, not exact string match alone. Accept valid alternatives and explain meaning or register differences. For each missed item, show the corrected English and explain the specific Golden Rule in Persian.
- Report a score only after grading the submitted set. Identify concepts that were understood, need review, or were not tested; do not claim mastery from untested concepts.
- On `Reset` / `ریست`, repeat the exact same questions and options, clear the current answers and score, and invite a new attempt.
- On `New Set` / `تمرین جدید`, create fresh questions while preserving settings when the conversation context permits. Do not merely reorder an earlier set.
- A new set is a new conversational turn. Do not claim an instant button, background model call, or preloaded batch unless the active interface proves that capability.
- Keep questions, answers, scores, and progress in the visible conversation only; never write them to project files.
