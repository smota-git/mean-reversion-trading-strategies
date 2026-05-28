# Mean-Reversion Trading Strategies Across Assets and Averaging Horizons

## Overview

This project explores the performance of simple mean-reversion trading strategies across multiple financial assets and averaging horizons.

The objective is not to develop a production-ready trading system, but rather to investigate how strategy behavior changes depending on:
- asset class,
- averaging window,
- trading frequency,
- and transaction costs.

The analysis includes:
- AAPL
- SPY
- BTC-USD
- XOM
- JPM

---

## Methodology

For each asset, rolling mean and rolling standard deviation were computed using multiple averaging horizons:
- 20 trading hours
- 1 month
- 1 quarter
- 1 half-year
- 1 year

A z-score signal was defined as:

z = (price - rolling_mean) / rolling_std

Trading rules:
- z-score > 1 → short position
- z-score < -1 → long position
- otherwise → flat position

Portfolio returns were evaluated using a simple backtesting framework with shifted positions to avoid look-ahead bias.

---

## Performance Metrics

The strategies were evaluated using:
- total return
- Sharpe ratio
- maximum drawdown

Transaction costs were additionally incorporated to evaluate the sensitivity of highly active strategies.

---

## Key Findings

Main observations:
- Buy-and-hold frequently outperformed active mean-reversion strategies.
- Strategy performance strongly depended on averaging horizon and asset class.
- Shorter averaging horizons generated significantly higher transaction costs.
- Some seemingly profitable strategies became unprofitable after including execution costs.
- BTC showed stronger persistence of mean-reversion effects compared to traditional equities.

---

## Example Results

| Asset | Strategy | Total Return | Sharpe |
|---|---|---|---|
| AAPL | Buy-and-Hold | 28.4% | 0.45 |
| BTC | 20h Mean Reversion | 37.4% | 0.44 |
| SPY | Buy-and-Hold | 29.4% | 0.76 |
