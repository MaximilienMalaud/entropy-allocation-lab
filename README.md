# Entropy Allocation Lab

**Does entropy help a multi-asset investor manage risk beyond volatility and correlation?**
A research project from a Swiss (CHF-based) investor's perspective.

> 🚧 Work in progress. See the [roadmap](docs/ROADMAP.md).

## What this project does

1. **Market disorder:** measures how "ordered" or "random" markets are, using permutation entropy and the spectral entropy of the correlation matrix.
2. **Diversification:** measures how many *independent bets* a portfolio really holds, using the Effective Number of Bets.
3. **Application:** tests a pre-specified, entropy-based risk overlay, with transaction costs and an untouched out-of-sample period.

The hypotheses were written **before** any analysis: see the [project charter](docs/PROJECT_CHARTER.md).
Every methodological choice is logged in the [decision journal](docs/DECISIONS.md).

## Repository structure

```
docs/            charter, roadmap, decision journal
src/entropy_lab/ reusable Python code (data, entropy measures, portfolios, backtest)
notebooks/       analysis notebooks, one per phase
tests/           unit tests
scripts/         utility scripts
reports/         figures and the final research note
data/            local data cache (not versioned)
```

## Setup

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python scripts/check_environment.py
```

## Author

Maximilien Malaud, CFA Level 1 candidate
