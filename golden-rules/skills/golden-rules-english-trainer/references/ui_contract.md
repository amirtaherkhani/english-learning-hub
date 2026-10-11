# Interactive UI contract (v3.1)

## Controls

| Button | Behavior | Availability |
|---|---|---|
| نتیجه | Lock answers; grade; reveal feedback and percent | All questions answered, not yet graded |
| ریست | Clear current answers and score, preserve exact questions | Always |
| بعدی | Show next pre-generated set instantly | Graded and not last set |
| جدید | Request fresh 3–5 sets using GenUI.issueNewTurn | Last set graded |

- Default: 3 pre-generated sets, 5 questions per set, level A2–B1.
- Use client state for answers, current set, grading state and score history.
- Generate all current sets in the same response. No external requests for Next.
- The New button is a **new chat turn**, not an in-place background AI call.
- Grading: `Math.round(100 * correct / total)`.
- Hide feedback until Results.
- After grading, wrong label in **light red** `#F87171`, correct answer in **green** `#22C55E`, golden rule in **light yellow** `#FACC15`; adjust for light themes.
- Four short buttons in a compact row or 2x2 grid. Show progress and percentage.
- Reset must not change the question batch or accidentally unlock New before the final set.
