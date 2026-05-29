import pandas as pd


def moving_average_strategy(
    data: pd.DataFrame,
    short_window: int = 20,
    long_window: int = 50
) -> pd.DataFrame:
    data = data.copy()

    data["short_ma"] = data["Close"].rolling(window=short_window).mean()
    data["long_ma"] = data["Close"].rolling(window=long_window).mean()

    data["signal"] = 0
    data.loc[data["short_ma"] > data["long_ma"], "signal"] = 1

    data["position"] = data["signal"].shift(1).fillna(0)

    return data