"""Phase 0 smoke test: are the libraries installed, and can we download every ticker in the universe?

Run with:  python scripts/check_environment.py
"""

import importlib
import sys

# The provisional universe from docs/PROJECT_CHARTER.md, section 4
UNIVERSE = ["SPY", "EFA", "EEM", "EWL", "IEF", "TLT", "TIP", "GLD", "DBC", "VNQ", "USDCHF=X"]
LIBRARIES = ["numpy", "pandas", "scipy", "statsmodels", "matplotlib", "yfinance"]


def check_libraries() -> bool:
    """Import each library and print its version."""
    print(f"Python {sys.version.split()[0]}")
    ok = True
    for name in LIBRARIES:
        try:
            module = importlib.import_module(name)
            print(f"  [OK]   {name} {getattr(module, '__version__', '?')}")
        except ImportError:
            print(f"  [FAIL] {name} is not installed")
            ok = False
    return ok


def check_data() -> bool:
    """Download the full history of each ticker and report its first date and number of rows."""
    import yfinance as yf

    data = yf.download(UNIVERSE, start="2000-01-01", auto_adjust=True, progress=False)["Close"]
    print("\nTicker      First date   Rows")
    ok = True
    for ticker in UNIVERSE:
        series = data[ticker].dropna() if ticker in data else None
        if series is None or series.empty:
            print(f"  {ticker:<10} NO DATA")
            ok = False
        else:
            print(f"  {ticker:<10} {series.index[0].date()}   {len(series)}")

    # The common start date is the latest first date among all tickers
    common_start = data.apply(lambda s: s.first_valid_index()).max()
    print(f"\nCommon start date for the full universe: {common_start.date()}")
    return ok


if __name__ == "__main__":
    libs_ok = check_libraries()
    data_ok = check_data() if libs_ok else False
    print("\nEnvironment ready." if libs_ok and data_ok else "\nSome checks failed, see above.")
