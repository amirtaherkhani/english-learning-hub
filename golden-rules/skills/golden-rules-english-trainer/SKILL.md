---
name: golden-rules-english-trainer
description: Teach Persian-coded English Golden Rules and produce native ChatGPT interactive quizzes with preloaded sets, reset, next, results, and new AI-generated batches.
version: 3.3
---

# Golden Rules English Trainer v3.3

## Scope
Teach English grammar to Persian speakers with memory codes, then quiz entirely inside ChatGPT. No external quiz app, API, or website. The user may choose one or more topics from the catalog.

## Teach a new Golden Rule
1. Find whether an existing GR-NNN lesson covers the topic. Avoid duplicates; if new, assign the next unused stable identifier.
2. Explain Persian mnemonic, exact formula, idiomatic usage and register, tense variations, positive/negative/question forms where relevant, common errors and exceptions, and at least four real-life examples.
3. Include a concise five-second summary.
4. Add the new topic to the active catalog, write the Markdown lesson and update indexes. **Immediately commit and push every newly created or updated Golden Rule and related skill changes to GitHub in the same workflow.** Confirm the remote commit. If write access is unavailable, clearly label the lesson as unsynced; never claim publication.
5. Immediately offer or show the interactive exercise, unless the user asks for explanation only.

## Quiz generation
- On "تمرین" with no topic, show compact selectors for categories, one/multiple topics, level A1/A2/B1/B2, and question count.
- Default A2–B1; generate **3 distinct sets** in one response, each with **5 questions** (3–5 allowed when requested).
- Pre-generate all sets with distinct questions, plausible distractors, verified single correct answer, and Persian rule explanation.
- Hide answers and explanation until grading.
- Grading score: `Math.round(100 * correct / total)`. Report percent and optionally average across graded sets.
- "نتیجه" grades only when all current questions have answers.
- "ریست" clears only the current set's answers and graded state; retains identical questions, order, and current position; invalidate its current score if regraded.
- "بعدی" advances instantly to the next **already generated** set after grading; NO new conversation turn.
- "جدید" is enabled only after completing the final set (default third); calls `GenUI.issueNewTurn` from its click handler to request 3 new sets. Do not recycle fixed batches. Carry topic, level, count and recent examples forward.
- Three attempts means three graded sets, not three guesses on one question. Reset does not consume a new set.
- Four compact buttons: **نتیجه · ریست · بعدی · جدید**, in a row if space allows or responsive 2×2 grid.
- Do not show inert buttons or claim live generation without a new model turn.

## Optional visual teaching and graphical exercises
- The trainer MAY use native ChatGPT graphical teaching capabilities when they materially improve comprehension: timelines for tenses, color-coded sentence anatomy, side-by-side grammar contrasts, simple flow diagrams, visual matching and interactive cards.
- Prefer clear, responsive, mobile-friendly visuals with Persian labels and accurate English text. Use accessible text labels, not color alone.
- Choose visualizations based on the grammar concept; avoid decorative images, irrelevant pictures, or visuals that reveal quiz answers before grading.
- Keep all exercise interactions inside ChatGPT. Do not require external websites, apps, paid services, or image-generation tools for ordinary quizzes.
- Optional static illustrations are permitted when educationally useful, but they must not replace editable questions or the four core controls.
- Visual components are ephemeral UI; do not save generated quizzes, learner answers, or scores in the repository.
- Preserve preloaded batches, percentage grading, and the short buttons (نتیجه، ریست، بعدی، جدید) even when visuals are used.
- If a visual cannot be rendered reliably, fall back to a clear text/table explanation without delaying the lesson.

## Feedback colors after grading only
- Wrong response: light red `#F87171` with label **پاسخ اشتباه**.
- Correct answer: green `#22C55E` with label **پاسخ صحیح**.
- Golden Rule explanation and the reason for the error: light yellow `#FACC15` with label **قانون طلایی**.
- On light backgrounds adjust for readable contrast. Always include labels/icons, not only colors.
- For wrong responses show the correct answer separately in green, then explanation in yellow.

## Publishing gates
- Golden Rules: **new rule or any rule update → immediate GitHub commit and push**, with index and related skill updates. No extra approval required unless the user explicitly requests a draft.
- Book lessons: **complete AND explicitly approved by the user → GitHub commit and push**. Until both conditions hold, do not publish the lesson.
- Never treat approval of the repository architecture as approval of future book units.
- See repository policy: `docs/PUBLISHING_POLICY.md`.

## Persistence
- Persist curated lessons and skill instructions only.
- Never commit dynamically generated quiz questions, user answers, scores, or progress to GitHub.
- Vocabulary and practice directories are reserved and documentation-only for now.

## Verification
Before rendering, independently check every option, answer key, grammar claim, Persian translation, and explanation. Check there is exactly one correct choice and no repeated examples in the batch. Avoid translating English structures mechanically from Persian.

See `references/ui_contract.md` and `references/topic_catalog.md`.
