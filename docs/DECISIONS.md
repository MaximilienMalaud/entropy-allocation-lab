# Decision Journal

Every methodological choice, with its reason and the alternatives considered.
Format: `D###: decision (date)`, then **Why** and **Alternatives**.

---

### D001: Base currency CHF, unhedged (2026-11-25)
**Why:** the target job market is Switzerland, and an unhedged CHF investor faces the real FX risk of
holding foreign assets. This becomes a talking point in interviews (hedging cost and CHF as a safe-haven currency).
**Alternatives:** USD base (simpler but less relevant), or CHF-hedged (requires interest-rate differentials, so it is postponed).

### D002: US-listed ETFs from yfinance (2026-11-25)
**Why:** the data are free, reproducible, cover about 20 years of history and include dividends through adjusted prices.
**Alternatives:** Swiss-listed ETFs (histories too short), Bloomberg or Refinitiv (no access).

### D003: In-sample 2006–2015, out-of-sample 2016–2026 (2026-11-25)
**Why:** each sub-period contains at least one crisis (2008 in-sample; 2020 and 2022 out-of-sample).
The out-of-sample period is used once, at the end.
**Alternatives:** a rolling walk-forward (may be added in Phase 5 as a robustness check).

### D004: Deliverables in English (2026-11-25)
**Why:** Swiss asset managers work in English, and so does the CFA curriculum.

### D005: Python 3.14 in a virtual environment (2026-11-25)
**Why:** an isolated environment with pinned dependencies makes the results reproducible.
