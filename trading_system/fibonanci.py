import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc

# Generate mock Bitcoin price data for illustration
np.random.seed(0)
dates = pd.date_range(start='2023-01-01', periods=200, freq='D')
prices = np.cumsum(np.random.randn(200) * 1000 + 30000)

# Create a DataFrame
df = pd.DataFrame({
    'Date': dates,
    'Open': prices,
    'High': prices + np.random.rand(200) * 1000,
    'Low': prices - np.random.rand(200) * 1000,
    'Close': prices + np.random.randn(200) * 100
})

# Calculate recent high and low
recent_high = df['High'].max()
recent_low = df['Low'].min()
diff = recent_high - recent_low

fib_levels = {
    '0.0%': recent_high,
    '23.6%': recent_high - 0.236 * diff,
    '38.2%': recent_high - 0.382 * diff,
    '50.0%': recent_high - 0.500 * diff,
    '61.8%': recent_high - 0.618 * diff,
    '78.6%': recent_high - 0.786 * diff,
    '100.0%': recent_low
}

# Prepare data for candlestick plot
df['Date'] = df['Date'].apply(mdates.date2num)
ohlc = df[['Date', 'Open', 'High', 'Low', 'Close']]

# Plotting
fig, ax = plt.subplots(figsize=(14, 7))

# Plot candlestick chart
candlestick_ohlc(ax, ohlc.values, width=0.6, colorup='g', colordown='r')

# Draw Fibonacci levels
for level, price in fib_levels.items():
    ax.hlines(price, df['Date'].min(), df['Date'].max(), colors='r', linestyles='dashed')
    ax.text(df['Date'].max(), price, f'{level} ({price:.2f})', va='center', ha='left', backgroundcolor='w')

# Formatting
ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax.set_title('Bitcoin Price with Fibonacci Retracement Levels (1 Day Time Frame)')
ax.set_xlabel('Date')
ax.set_ylabel('Price (USD)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
