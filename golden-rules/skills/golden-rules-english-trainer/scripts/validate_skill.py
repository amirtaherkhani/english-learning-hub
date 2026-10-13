#!/usr/bin/env python3
"""Validate the repository's Golden Rules Trainer v4 package."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    "SKILL.md",
    "README.md",
    "references/topic_catalog.md",
    "references/text_quiz.md",
    "references/ui_contract.md",
    "references/qa-checklist.md",
    "references/lesson-and-quiz-patterns.md",
    "references/full-specification-v4.md",
    "references/requirements-map.md",
]
errors = [f"Missing required file: {name}" for name in required if not (ROOT / name).is_file()]

skill_path = ROOT / "SKILL.md"
skill = skill_path.read_text(encoding="utf-8") if skill_path.exists() else ""
spec_path = ROOT / "references/full-specification-v4.md"
spec = spec_path.read_text(encoding="utf-8") if spec_path.exists() else ""
quiz_path = ROOT / "references/text_quiz.md"
quiz = quiz_path.read_text(encoding="utf-8") if quiz_path.exists() else ""

for token in (
    "name: golden-rules-english-trainer",
    'version: "4.0.0"',
    "A1/A2",
    "B1",
    "Easy",
    "Normal",
    "Hard",
    "Mixed",
    "5 items for short practice",
    "10 for comprehensive practice",
    "Reset",
    "New Set",
    "well",
    "RTL",
    "LTR",
    "mastery",
):
    if token not in skill:
        errors.append(f"SKILL.md missing required marker: {token}")

for token in (
    "# 1. Mission",
    "# 19. Ambiguity Prevention",
    "# 24. Reset and New Set",
    "# 33. Mastery Tracking",
    "# 38. RTL and LTR Typography",
    "# 53. Definition of Done",
    "# 54. Final Behavioral Rule",
):
    if token not in spec:
        errors.append(f"Full v4 specification missing section: {token}")

for token in ("English", "Reset", "New Set", "conversation only"):
    if token not in quiz:
        errors.append(f"Text quiz contract missing required marker: {token}")

for name in ("good-well-a2-sample.md", "good-well-a2-answer-key.md"):
    if (ROOT / "references" / name).exists():
        errors.append(f"Do not persist practice sample or answer key: {name}")

for bad in ("<html", "<!doctype html", "personal notes:"):
    if bad in skill.lower():
        errors.append(f"Prohibited content found in SKILL.md: {bad}")

if errors:
    print("FAIL")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)

print(f"PASS: {len(required)} required files and v4 skill markers validated.")
