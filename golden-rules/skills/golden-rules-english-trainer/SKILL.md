---
name: golden-rules-english-trainer
description: Teach, write, correct, and quiz the project's Persian-first English Golden Rules (GR-NNN) in Codex or ChatGPT. Use when the user asks for a Golden Rule, a grammar explanation with Persian memory coding, comparisons between English forms, common phrases, or practice. Do not use for Grammar in Use book units.
metadata:
  version: "3.4"
---

# Golden Rules English Trainer

## Scope and sources

Teach English grammar to Persian speakers using accurate Persian memory codes. Use `references/topic_catalog.md` to locate the authoritative catalog, then read the relevant `GR-NNN` lesson before explaining, correcting, or testing it. Reuse its stable ID; do not create a duplicate lesson for an existing topic. Follow `golden-rules/docs/CONTENT_STANDARD.md` for lesson content and `docs/PUBLISHING_POLICY.md` for publication. Book lessons have a separate approval gate.

## Explain a rule

- Answer in Persian unless the user asks for another language. Give the detail requested; do not shorten a comprehensive explanation to a mnemonic or a few examples.
- State the core meaning, exact formula and word order, and where the pattern is used. Qualify memory codes where they are not universal.
- Contrast nearby words and structures that learners may confuse. Explain when each works, when it does not, and how meaning or register changes.
- Cover positive, negative, and question forms and meaningful tense variations. Do not manufacture tense forms for structures that lack them.
- Include common collocations and everyday phrases, at least four natural English–Persian examples, common mistakes and exceptions, and a five-second recap. Separate grammatical possibility from idiomatic preference.
- Check uncertain grammar, translations, answer keys, and usage before presenting them. Do not copy copyrighted book units.
- Offer a practice set after teaching unless the user requests explanation only or declines practice.

## Create or update a lesson

1. Search the catalog and existing lessons first. For a new topic, assign the next unused stable `GR-NNN` ID; for a correction, edit the existing lesson.
2. Follow the complete lesson contract in `golden-rules/docs/CONTENT_STANDARD.md`. Update the catalog and affected indexes or skill references.
3. Verify the lesson and its links. Commit and push every new or updated Golden Rule and related skill changes in the same workflow, as required by `docs/PUBLISHING_POLICY.md`. Confirm the remote commit; if publication fails, clearly report that the change is unsynced.
4. Never commit generated practice questions, learner answers, scores, or progress.

## Practice in the available interface

- In Codex or another text-only interface, follow `references/text_quiz.md`. Present one set at a time and perform grading or navigation in subsequent turns. Do not promise buttons, instant navigation, or `GenUI.issueNewTurn` when those capabilities are absent.
- In a native ChatGPT interactive interface that actually supports the required controls, follow `references/ui_contract.md`. Generate the preloaded sets and working controls there.
- Default to A2–B1, three distinct sets of five questions, unless the user chooses topics, level, or count. Each question must have exactly one verified correct answer and plausible alternatives. Hide answers and explanations until grading.
- Keep all generated quiz state in the live conversation or native UI. Never persist it in the repository.
- Use timelines, sentence anatomy, or simple contrasts when they clarify a grammar point. Keep English text accurate and Persian labels readable; avoid visuals that reveal quiz answers early.
