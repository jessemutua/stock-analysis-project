import pandas as pd
import mplfinance as mpf

# Read the cleaned data from the CSV file
df = pd.read_csv("cleaned_data.csv")

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Sort the DataFrame by date in ascending order
df.sort_values(by='Date', inplace=True)

# Candle sticks
ohlc = df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
ohlc = ohlc.set_index('Date')

# Consider only the first 200 data entries for the candlestick chart
ohlc = ohlc.head(200)

# Plot the candlestick chart
mpf.plot(ohlc, type='candle', style='yahoo',
         title='Candlestick Chart', ylabel='Price', volume=True)
