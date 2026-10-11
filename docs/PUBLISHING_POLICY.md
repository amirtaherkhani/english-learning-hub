# Publishing and approval policy

This policy applies to all modules in this repository.

## Golden Rules — immediate publish

- Whenever a new Golden Rule is taught and documented, create or update its stable `GR-NNN` Markdown lesson and any affected indexes or skills, then **commit and push to GitHub immediately in the same workflow**.
- Whenever an existing Golden Rule is corrected, extended, or reorganized, update the existing lesson (do not create a duplicate or renumber), update links/indexes if needed, then **commit and push immediately**.
- Do not wait for a batch of unrelated lessons or an additional approval unless the user explicitly asks to hold publication.
- Check that the remote write succeeded and report the commit or file URL. If GitHub is unavailable, state that the lesson is **not yet synced**; do not claim it was pushed. Retry when access is restored.
- The same immediate-publish policy applies to Golden Rules skills and their documentation whenever they are updated.

## Book lessons — approval gate

- Draft or revise book lessons locally/in the conversation while they are incomplete or awaiting review.
- **Do not commit or push a book lesson until both conditions are satisfied:** (1) the lesson is complete, and (2) the user has explicitly approved that lesson for publication.
- Once both conditions are satisfied, commit and push the approved lesson promptly, along with its index/metadata updates.
- Approval is per lesson/unit; approval of a repository structure or book edition is not approval of all future book lessons.
- Respect edition-specific paths (for example `grammar-in-use/basic/edition-04/lessons/unit-001/`) and avoid reproducing copyrighted textbook content without appropriate rights.

## Exclusions

- Practice questions, quiz attempts, answers, scores, and user performance are **live-only**, never saved in GitHub.
- Vocabulary content remains deferred until the user decides on a policy.
- Never claim remote persistence until the GitHub connector confirms it.
