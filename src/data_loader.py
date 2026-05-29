import pandas as pd
import yfinance as yf


def load_price_data(ticker: str, start: str, end: str) -> pd.DataFrame:
    data = yf.download(ticker, start=start, end=end)

    data = data[["Open", "High", "Low", "Close", "Volume"]]
    data = data.dropna()

    return data


if __name__ == "__main__":
    df = load_price_data("AAPL", "2020-01-01", "2024-01-01")
    print(df.head())