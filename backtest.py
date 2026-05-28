import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

#Input parameters:
# buy_hold (boolean) - if the chosen trading strategy is or is not buy&hold
# asset - one of "AAPL", "SPY", "BTC", "XOM", "JPM"
# meantime - averaging horizon (one of "1y","halfyear","Qyear","1m","20")

buy_hold = True
asset = "SPY"
meantime = "1m"

# for buy&hold trading strategy, for the purpose of code consistency, meantime is taken to be 20
if buy_hold is True:
    meantime = "20"

# data0 - fixed horizon for processing data (1year, from 29/04/2025 to 29/04/2026)
data0 = yf.download(asset, start="2025-04-29", end="2026-04-29", interval="1h")

# data - fixed + averaging horizon(meantime)
if meantime == "1y":
    data = yf.download(asset, start="2024-05-29", end="2026-04-29", interval="1h")
elif meantime == "halfyear":
    data = yf.download(asset, start="2024-10-29", end="2026-04-29", interval="1h")
elif meantime == "Qyear":
    data = yf.download(asset, start="2025-01-29", end="2026-04-29", interval="1h")
elif meantime == "1m":
    data = yf.download(asset, start="2025-03-29", end="2026-04-29", interval="1h")
elif meantime == "20":
    data = yf.download(asset, start="2025-04-29", end="2026-04-29", interval="1h")

### Implementation:

data.columns = data.columns.get_level_values(0)
data = data.dropna()

# window - count of records in averaging horizon (corresponds with approprpiate count of trading hours)
window = max(20,data.shape[0]-data0.shape[0])
data['ma'] = data['Close'].rolling(window).mean()
data['std'] = data['Close'].rolling(window).std()

# Z-score
data['zscore'] = (data['Close'] - data['ma']) / data['std']

# trading rules
data['position'] = 0
data.loc[data['zscore'] > 1, 'position'] = -1  # short position
data.loc[data['zscore'] < -1, 'position'] = 1  # long position
#buy&hold
data['position'] = 1 if buy_hold is True else data['position']

data['position'] = data['position'].shift(1)

# backtest
data['returns'] = data['Close'].pct_change()
data['strategy'] = data['position'] * data['returns']
data['equity'] = (1 + data['strategy']).cumprod()

# evaluation
sharpe = np.sqrt(252) * data['strategy'].mean() / data['strategy'].std()
total_return = data['equity'].iloc[-1] - 1
data_max = max(data['equity'].iloc[window:])
drawdown = data['equity'] / data['equity'].cummax() - 1
max_dd = drawdown.min()

# graph
data['equity'].iloc[window:].plot(title="Strategy Equity Curve")

# backtest and evaluation with transaction costs:
cost = 0.0005
data['strategy_net'] = data['strategy'] - cost * data['position'].diff().abs().fillna(0)
data['equity_net'] = (1 + data['strategy_net']).cumprod()

sharpe_net = np.sqrt(252) * data['strategy_net'].mean() / data['strategy_net'].std()
total_return_net = data['equity_net'].iloc[-1] - 1
data_max_net = max(data['equity_net'].iloc[window:])
drawdown_net = data['equity_net'] / data['equity_net'].cummax() - 1
max_dd_net = drawdown_net.min()

# graph with transaction costs (uncomment if needed)
data['equity_net'].iloc[window:].plot(title="Strategy Equity Curve With Transaction Costs")

# summary of results
print(f"Asset: {asset}")
print(f"Window: {'Buy&Hold' if buy_hold is True else window}")
print(f"Return: {100 * total_return:.1f}%")
print(f"Sharpe: {sharpe:.2f}")
print(f"Max_DD: {100 * max_dd:.10f}%")
print(f"Maximal Equity: {data_max:.2f}")
print("")
print("With transaction costs:")
print(f"Return: {100 * total_return_net:.1f}%")
print(f"Sharpe: {sharpe_net:.2f}")
print(f"Max_DD: {100 * max_dd_net:.10f}%")
print(f"Maximal Equity: {data_max_net:.2f}")

# plot of graph
plt.show()



