import yfinance as yf
import mplfinance as mpf
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from datetime import datetime, timedelta
import pandas as pd  # Import pandas

def fetch_data(ticker, interval):
    """Fetch historical data for the given ticker and interval."""
    end_date = datetime.now()
    if interval in ['1h', '2h', '4h']:
        start_date = end_date - timedelta(days=730)
    else:
        start_date = end_date - timedelta(days=365 * 5)
    data = yf.download(ticker, start=start_date, end=end_date, interval=interval)
    return data

def plot_chart(data, interval):
    """Plot the candlestick chart with the given data and interval."""
    if not isinstance(data.index, pd.DatetimeIndex):
        data.index = pd.to_datetime(data.index)
    plt.figure()
    mpf.plot(data, type='candle', style='charles', title=f'Bitcoin ({interval} Chart)', ylabel='Price ($)')
    plt.show()

def update_chart(interval):
    """Fetch new data and update the chart."""
    data = fetch_data('BTC-USD', interval)
    plot_chart(data, interval)

# Define different time intervals
intervals = {
    '1h': '1h',
    '2h': '2h',
    '4h': '4h',
    '1d': '1d'
}

# Fetch initial data and plot the chart
initial_interval = '1h'
data = fetch_data('BTC-USD', intervals[initial_interval])
plot_chart(data, initial_interval)

# Create buttons for each interval
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)

ax_1h = plt.axes([0.1, 0.05, 0.1, 0.075])
ax_2h = plt.axes([0.21, 0.05, 0.1, 0.075])
ax_4h = plt.axes([0.32, 0.05, 0.1, 0.075])
ax_1d = plt.axes([0.43, 0.05, 0.1, 0.075])

btn_1h = Button(ax_1h, '1 Hour')
btn_2h = Button(ax_2h, '2 Hours')
btn_4h = Button(ax_4h, '4 Hours')
btn_1d = Button(ax_1d, '1 Day')

def on_1h(event):
    update_chart('1h')

def on_2h(event):
    update_chart('2h')

def on_4h(event):
    update_chart('4h')

def on_1d(event):
    update_chart('1d')

btn_1h.on_clicked(on_1h)
btn_2h.on_clicked(on_2h)
btn_4h.on_clicked(on_4h)
btn_1d.on_clicked(on_1d)

plt.show()
