# Moving Average Backtest

A simple quantitative finance backtesting project using Python.

## Project Overview

This project tests a moving average trading strategy on historical AAPL stock price data.

The strategy compares:

- Buy and Hold
- Moving Average Strategy

## Strategy Logic

The strategy uses two moving averages:

- Short moving average: 20 days
- Long moving average: 50 days

Trading rule:

- Hold the stock when the 20-day moving average is above the 50-day moving average
- Stay out of the market when the 20-day moving average is below the 50-day moving average

## Tools Used

- Python
- pandas
- numpy
- matplotlib
- yfinance

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt