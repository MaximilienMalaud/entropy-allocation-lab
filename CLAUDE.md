# Instructions for Claude

This file gives Claude the project context on any machine. Read it at the start of every session,
then read `docs/ROADMAP.md` to see where the project stands.

## Project

A portfolio research project built to strengthen a job application for portfolio-management roles
in Switzerland. The question: does entropy help a multi-asset investor (CHF base) manage risk beyond
volatility and correlation? The full scope, hypotheses H1–H5 and safeguards are in
`docs/PROJECT_CHARTER.md`; every methodological choice is logged in `docs/DECISIONS.md`.

## The author

- Finance graduate with middle-office private-equity experience, CFA Level 1 candidate (exam February 2027).
- Intermediate Python (pandas, NumPy).
- **Converse in French.** Deliverables in the repository (code, docs, README) are in English.

## How we work

1. **Teach, don't just deliver.** The author must be able to explain every line in an interview.
   Explain the idea first, then the code, then ask the author to reformulate or modify it.
2. **Every phase ends with a comprehension check**: interview-style questions, honest feedback
   (what is right, what is wrong, and the corrected formulation).
3. **Hypotheses are pre-registered.** Never change H1–H5 after seeing results; new ideas are labelled
   *exploratory*. The 2016–2026 out-of-sample period is never used for calibration.
4. **Log decisions** in `docs/DECISIONS.md` (`D###`, with *Why* and *Alternatives*).
5. **The CFA comes first**: about 5 hours per week on the project until the exam.
6. Update the status in `docs/ROADMAP.md` when a step is finished.

## Current status

- **Phase 1, lesson 1 (Shannon entropy) taught on 2026-11-26.** Exercises pending:
  1. Biased coin p = 0.9: compute H and compare with a fair coin.
  2. 20 days: 4 down, 6 flat, 10 up: compute H and normalised H.
  3. Series A (`+1,-1` alternating) vs series B (same ups and downs in irregular order): same volatility,
     same Shannon entropy (1 bit), but A is perfectly predictable. Shannon ignores the **order** of
     observations, which motivates permutation entropy.
  4. (Optional) Write `shannon_entropy(probabilities)` in NumPy, handling p = 0.
- Next: correct the exercises, then lesson 2 (permutation entropy, computed by hand on 8 returns),
  then lesson 3 (spectral entropy of a correlation matrix), then the author's own summary notes.

## Technical setup

- Windows; keep the repository on a **short path outside OneDrive** (for example `C:\Users\<user>\Projects`):
  Windows long-path limits break `pip`, and OneDrive sync corrupts `.venv` and `.git`.
- Python 3.14 virtual environment in `.venv`; dependency versions are pinned in `requirements.txt`.
- Run `python scripts/check_environment.py` to check the environment and the data download.
- `data/` is a local cache that is not versioned: re-download it on each machine.
- Commits use the author's GitHub no-reply e-mail address. Sync between machines through GitHub:
  run `git pull` when starting a session and `git push` when ending it.
