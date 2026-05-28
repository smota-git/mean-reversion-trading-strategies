# Mean-Reversion Trading Strategies Across Assets and Averaging Horizons

## Overview

This project explores simple mean-reversion trading strategies across multiple financial assets using hourly market data.

The objective is to analyze how strategy behavior changes depending on:

* asset class,
* averaging horizon,
* and transaction costs.

The analysis includes:

* AAPL
* SPY
* BTC-USD
* XOM
* JPM

---

## Methodology

Trading signals are based on z-scores computed from rolling means and rolling standard deviations over different averaging horizons.

Trading rules:

* high positive z-score → short position
* high negative z-score → long position

Strategy performance is evaluated using:

* total return,
* Sharpe ratio,
* maximum drawdown.

Transaction costs are additionally incorporated to evaluate strategy robustness.

---

## Key Findings

Main observations:

* buy-and-hold frequently outperformed active trading strategies,
* shorter averaging horizons generated larger transaction costs,
* some profitable strategies became unprofitable after including execution costs,
* BTC showed stronger persistence of mean-reversion effects than most equities.

  <img width="1278" height="385" alt="image" src="https://github.com/user-attachments/assets/ebaf7521-4ca3-4c54-87b9-8e0c78b12d31" />




---

## Repository Contents

* research report
* backtesting code
* strategy evaluation
* performance visualizations

---

## Technologies

Python, pandas, numpy, matplotlib, yfinance

---

## Full Report

See `report/mean_reversion_trading_strategies.pdf`
