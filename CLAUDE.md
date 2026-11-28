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
7. **Keep `docs/JOURNAL_APPRENTISSAGE.md` up to date** (in French). After each lesson or comprehension
   check, add what the author learned: intuition, formulas, reference results, key takeaways for the
   project, interview phrasing, Python learned, common pitfalls (written generically) and environment
   tips. The author asked for this file explicitly; it is the author's revision support.

## Current status

- **Phase 1, lesson 1 (Shannon entropy) taught on 2026-11-26.**
- 2026-11-26 (laptop): no lesson work. Cleaned up a virtual environment that had been created at the
  repository root, which had overwritten the root `.gitignore`. The laptop is now in sync with GitHub
  and `scripts/check_environment.py` passes.
- 2026-11-27 (desktop): exercises 1–3 done.
  - Ex. 1: H = 0.469 bit.
  - Ex. 2: H = 1.485 bit, normalised 0.937, which is close to maximum disorder even with 50% up days.
  - Ex. 3: Shannon entropy and volatility both ignore the **order** of observations
    (the "bag of marbles" image).
  - Code is written in VS Code with Jupyter notebooks, not in the PowerShell REPL.
  - Exercise 4 is in `notebooks/01_shannon_entropy.ipynb` (steps 1–3 ready to run).
- 2026-11-28 (desktop): mini-challenge `normalized_shannon_entropy` done and correct. **Lesson 1 is
  complete.** `docs/JOURNAL_APPRENTISSAGE.md` was created.
- 2026-11-28 (desktop): **Lesson 2 (permutation entropy, m = 3), theory and hand calculation done.**
  The 6 patterns are named ① rise, ② fall, ③ peak ending higher, ④ peak ending lower,
  ⑤ trough ending higher, ⑥ trough ending lower. Hand exercise on `3,5,2,8,9,4,6,7`: H = 1.918 bit,
  normalised 0.742 (correct). Understood: invariance to scale (×10), and a monotonic series gives 0.
  The journal has a "Leçon 2" section marked "en cours".
- **Next (the author will resume on the laptop):** prepare `notebooks/02_permutation_entropy.ipynb`
  on the same model as notebook 01 (building blocks first, then the function, then checks against
  the hand results, then a mini-challenge). The checks to include:
  (1) reproduce 0.742 on `[3,5,2,8,9,4,6,7]` and 0.580 on `[4,7,9,10,6,11]`;
  (2) the same value after multiplying the series by 10;
  (3) series A (`+1,-1` alternating) versus series B (`+1,+1,-1,+1,-1,-1,-1,+1,+1,-1`), which contain
      ties: break them by order of appearance (`np.argsort(..., kind="stable")`) and explain this rule;
  (4) shuffling a series changes its permutation entropy but not its Shannon entropy.
  Then complete the journal's "Leçon 2" section, then lesson 3 (spectral entropy of a correlation
  matrix), then the author's own summary notes.
- Teaching style: concrete images, worked tables and step-by-step guidance; prefer simple yes/no
  questions to open fill-in-the-blank prompts.

## Technical setup

- Windows; keep the repository on a **short path outside OneDrive** (for example `C:\Users\<user>\Projects`):
  Windows long-path limits break `pip`, and OneDrive sync corrupts `.venv` and `.git`.
- Python 3.14 virtual environment in `.venv`; dependency versions are pinned in `requirements.txt`.
  Create it with `python -m venv .venv` from the repository root. Never point `venv` at the root
  itself: it writes `Lib/`, `Include/`, `pyvenv.cfg` and executables into `scripts/` (Windows ignores
  case, so `Scripts/` and `scripts/` are the same folder), and it overwrites the root `.gitignore` with `*`.
- Run `python scripts/check_environment.py` to check the environment and the data download.
- `data/` is a local cache that is not versioned: re-download it on each machine.
- Commits use the author's GitHub no-reply e-mail address. Sync between machines through GitHub:
  run `git pull` when starting a session and `git push` when ending it.
