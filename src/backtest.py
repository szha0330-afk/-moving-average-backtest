import os
import numpy as np
import matplotlib.pyplot as plt

from data_loader import load_price_data
from strategy import moving_average_strategy


def run_backtest():
    ticker = "AAPL"
    start_date = "2020-01-01"
    end_date = "2024-01-01"

    data = load_price_data(ticker, start_date, end_date)
    data = moving_average_strategy(data)

    data["market_return"] = data["Close"].pct_change()
    data["strategy_return"] = data["position"] * data["market_return"]

    data["market_equity"] = (1 + data["market_return"]).cumprod()
    data["strategy_equity"] = (1 + data["strategy_return"]).cumprod()

    total_return = data["strategy_equity"].iloc[-1] - 1
    volatility = data["strategy_return"].std() * np.sqrt(252)

    if data["strategy_return"].std() != 0:
        sharpe_ratio = (
            data["strategy_return"].mean()
            / data["strategy_return"].std()
            * np.sqrt(252)
        )
    else:
        sharpe_ratio = 0

    rolling_max = data["strategy_equity"].cummax()
    drawdown = data["strategy_equity"] / rolling_max - 1
    max_drawdown = drawdown.min()

    print("Backtest Result")
    print("----------------")
    print(f"Ticker: {ticker}")
    print(f"Total Return: {total_return:.2%}")
    print(f"Volatility: {volatility:.2%}")
    print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
    print(f"Max Drawdown: {max_drawdown:.2%}")

    os.makedirs("results", exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data["market_equity"], label="Buy and Hold")
    plt.plot(data.index, data["strategy_equity"], label="Moving Average Strategy")
    plt.title("Strategy vs Buy and Hold")
    plt.xlabel("Date")
    plt.ylabel("Equity")
    plt.legend()
    plt.savefig("results/equity_curve.png")
    plt.show()


if __name__ == "__main__":
    run_backtest()