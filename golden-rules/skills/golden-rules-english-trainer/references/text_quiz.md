# Text quiz contract for Codex

Use this contract when the conversation cannot render the native interactive controls described in `ui_contract.md`.

## Start

- If the user says «تمرین» without a topic, briefly offer the available categories and topics from `topic_catalog.md`, plus level (A1/A2/B1/B2) and question count. Use A2–B1 and five questions when the user leaves those unspecified.
- Plan three distinct sets by default and generate each set when it is reached; show only the current set. Do not claim that the next set is preloaded or can appear without a new conversation turn.
- Number questions and label answer options A/B/C/D. Check that exactly one option is correct and that the wording has no unintended second answer. Do not reveal the key or explanations yet.

## Grade and navigate

- Accept answers in a compact form such as `1A 2C 3B 4D 5A`. Ask for missing answers before grading.
- On «نتیجه», grade only when every current question has an answer. Report `round(100 × correct / total)` percent, identify the correct answer for each missed question, and explain the relevant Golden Rule in Persian.
- On «ریست», repeat the exact same questions and option order from the current set, clear its answers and score, and allow another attempt. Reset does not count as a new set.
- On «بعدی», after grading, show the next distinct set in the next assistant turn. Keep the chosen topics, level, and question count. After the final set, offer «جدید».
- On «جدید», after the final graded set, generate a fresh batch in the next assistant turn. Avoid repeating recent examples and questions.
- Three attempts means three graded sets, not three guesses on one question. Keep the current set and progress clear in each response.

Do not store generated questions, answers, scores, or progress in project files.
