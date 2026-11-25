# Roadmap

Each phase ends with a **deliverable** and a **comprehension check** (an oral quiz, interview style).
A phase is "done" only when both are completed.

| # | Phase | Deliverable | Comprehension check | Status |
|---|-------|-------------|---------------------|--------|
| 0 | Scoping and setup | Charter, repository, environment, first commit | Explain the research question and H1–H5 in 2 minutes | 🟡 In progress |
| 1 | Theory | Personal notes: Shannon, permutation and spectral entropy | Compute a permutation entropy by hand on 8 data points | ⬜ |
| 2 | Data pipeline | `src/entropy_lab/data.py` and tests | Why convert to CHF? What does an adjusted close mean? | ⬜ |
| 3 | Pillar 1: market disorder (H1, H2, H3) | Notebook and figures | "Why not just use volatility?" | ⬜ |
| 4 | Pillar 2: diversification (H4) | Notebook and comparison table | Explain the Effective Number of Bets to a non-quant | ⬜ |
| — | **Milestone: first presentable version (before the CFA exam)** | Short README and figures | | ⬜ |
| 5 | Pillar 3: overlay backtest (H5) | Backtest report | Look-ahead bias, overfitting, transaction costs | ⬜ |
| 6 | Bonus: Entropy Pooling | Notebook | How to blend manager views with a prior | ⬜ |
| 7 | Packaging | README, research note (PDF), 6-slide deck, CV line | Mock presentation | ⬜ |
| 8 | Interview preparation | Q&A sheet (about 40 questions), 2-minute pitch | Full mock interview | ⬜ |

## Phase 0 checklist

- [x] Project charter with pre-registered hypotheses (`docs/PROJECT_CHARTER.md`)
- [x] Decision journal started (`docs/DECISIONS.md`)
- [x] Repository structure
- [x] Virtual environment and dependencies installed (versions pinned in `requirements.txt`)
- [x] Data download smoke test: all 11 tickers available, common start date 2006-02-06
- [ ] Git installed, first commit
- [ ] GitHub repository created and pushed
- [ ] Comprehension check: explain the question and H1–H5 in 2 minutes
