# Project Charter — Entropy Allocation Lab

*Version 1.0 — 25 November 2026 — written **before** any data analysis (pre-registration).*

## 1. Research question

> Does entropy — a measure of disorder and information — help a multi-asset investor
> understand and manage portfolio risk **beyond what volatility and correlation already tell us**?

Point of view: a **Swiss (CHF-based) investor** holding a diversified multi-asset portfolio.

## 2. Why this matters for portfolio management

- **Market efficiency** — if returns become more "ordered" (lower entropy), they are more predictable,
  which is a departure from weak-form efficiency.
- **Hidden concentration** — a portfolio can look diversified by weights while its risk is driven by
  one or two factors. Entropy measures *how many independent bets* a portfolio really holds.
- **Diversification failure in crises** — correlations tend to rise in sell-offs. Entropy of the
  correlation structure measures this directly.

## 3. Hypotheses (fixed in advance)

These hypotheses are written down before looking at results. They will not be changed after the
fact; any new idea discovered along the way will be labelled as *exploratory*.

| ID | Hypothesis | How it will be tested |
|----|-----------|-----------------------|
| **H1** | Permutation entropy of daily equity returns is **lower in stress periods** than in calm periods. | Stress = days when the global equity proxy is more than 15% below its running maximum. Compare distributions (Mann–Whitney test) and visualise around 2008, 2020, 2022. |
| **H2** | Entropy contains information about **future risk** that **current volatility does not** already capture. | Regress forward 21-day realised volatility on current realised volatility, with and without entropy. Newey–West standard errors; out-of-sample R² improvement. |
| **H3** | The **spectral entropy of the cross-asset correlation matrix** drops (risk concentrates on one factor) during crises. | Rolling correlation matrix → eigenvalues → normalised entropy. Compare with the absorption ratio (Kritzman et al., 2011) and with stress periods. |
| **H4** | Portfolios that look diversified by weights hold **far fewer effective bets**; risk parity has a higher Effective Number of Bets than 60/40. | Compute Effective Number of Bets (Meucci, 2009) for equal weight, 60/40, minimum variance and risk parity. |
| **H5** | A **pre-specified entropy overlay** (cut risky exposure when the entropy signal crosses a threshold) improves risk-adjusted returns **after transaction costs, out of sample**. | Calibrate only on 2006–2015; test once on 2016–2026. Compare Sharpe ratio, max drawdown, Calmar ratio and turnover with the static benchmark. |

**Success criterion:** the project succeeds if every hypothesis is tested rigorously and reported
honestly, **including negative results**. A rejected H5 is a valid and presentable outcome.

## 4. Data (provisional, to be validated in Phase 2)

Free daily data from `yfinance`. US-listed ETFs are used for their long histories and are converted
to CHF (unhedged investor).

| Asset class | Proxy | Note |
|-------------|-------|------|
| US equities | SPY | |
| Developed ex-US equities | EFA | |
| Emerging equities | EEM | |
| Swiss equities | EWL | iShares MSCI Switzerland |
| US Treasuries 7–10y | IEF | |
| US Treasuries 20y+ | TLT | |
| Inflation-linked | TIP | |
| Gold | GLD | |
| Commodities | DBC | Starts 2006 → defines the common start date |
| Real estate | VNQ | |
| FX | USDCHF=X | Converts USD prices to CHF |

- **Period:** 2006 → 2026, with an **in-sample** period from 2006 to 2015 and an **out-of-sample** period from 2016 to 2026.
- **Known limitations:** withholding taxes are ignored, FX exposure is unhedged, the data come from
  Yahoo Finance and their quality must be checked, and there is no Swiss bond proxy with a long history yet (to be investigated).

## 5. Methods

| Concept | Reference |
|---------|-----------|
| Shannon entropy | Shannon (1948), *A Mathematical Theory of Communication* |
| Permutation entropy | Bandt & Pompe (2002), *Physical Review Letters* |
| Permutation entropy and market efficiency | Zunino et al. (2009), *Physica A* |
| Absorption ratio | Kritzman, Li, Page & Rigobon (2011), *Journal of Portfolio Management* |
| Effective Number of Bets | Meucci (2009), *Managing Diversification*, Risk |
| Maximum-entropy diversification | Bera & Park (2008), *Econometric Reviews* |
| Entropy Pooling (optional) | Meucci (2008), *Fully Flexible Views*, Risk |

**Performance metrics:** annualised return and volatility, Sharpe ratio, Sortino ratio, maximum drawdown, Calmar ratio,
turnover and Effective Number of Bets.

## 6. Scope

**In scope:** daily multi-asset data, descriptive and statistical analysis, one rule-based overlay
and a backtest.

**Out of scope:** intraday data, single stocks, machine-learning forecasting, live trading.

## 7. Methodological safeguards

1. **No look-ahead bias:** every signal at date *t* uses only data available up to *t*, and trades happen at *t+1*.
2. **Untouched test set:** the period from 2016 to 2026 is not used for any calibration.
3. **Transaction costs:** at least 10 bp per unit of turnover, plus a sensitivity test.
4. **Robustness:** the results are shown for a range of parameters, not only the best one.
5. **Decision journal:** every methodological choice is recorded in `DECISIONS.md` with its reason.

## 8. Deliverables

1. A clean GitHub repository (code, tests and notebooks)
2. A 4–6 page research note in English (PDF)
3. A 6-slide presentation
4. An interview Q&A sheet and a 2-minute pitch

## 9. Main risks

| Risk | Mitigation |
|------|-----------|
| Overfitting / data snooping | Hypotheses written in advance and an untouched out-of-sample period |
| Scope creep | Out-of-scope list; the bonus phase only starts after the CFA exam |
| Competition with CFA preparation | About 5 hours per week until the exam; a first presentable version (Phases 0–4) before it |
| Not being able to explain the code | Rule: no line of code kept that the author cannot explain |
