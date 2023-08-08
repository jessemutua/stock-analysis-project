import pandas as pd
import random
import matplotlib.pyplot as plt
import mplfinance as mpf

# Read the data from the CSV file
df = pd.read_csv("i'll_use_this.csv")

# Data cleaning
numerical_columns = ["Open", "High", "Low", "Close", "Adj Close"]
df[numerical_columns] = df[numerical_columns].apply(lambda x: round(x, 6))

# Fill cases where volume is 0 with random values
non_zero_volumes = df[df["Volume"] != 0]["Volume"]
min_volume = non_zero_volumes.min()
max_volume = non_zero_volumes.max()
mean_volume = non_zero_volumes.mean()
std_volume = non_zero_volumes.std()


def generate_random_volume():
    return random.uniform(mean_volume, std_volume)


df["Volume"] = df["Volume"].apply(
    lambda x: generate_random_volume() if x == 0 else x)

# Display the cleaned DataFrame (first 200 entries)
print(df.head(200))


# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Sort the DataFrame by date in ascending order
df.sort_values(by='Date', inplace=True)


# Get summary information
summary_stats = df[['Open', 'High', 'Low',
                    'Close', 'Adj Close', 'Volume']].describe()
# print(summary_stats)


# Create the line chart
plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
# plt.plot(df['Date'], df['Close'], marker='o')

# Customize the chart
plt.title('NYA Index Closing Prices over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price')

# Rotate the x-axis labels for better readability (optional)
plt.xticks(rotation=45)

# Show the chart
# plt.tight_layout()
# plt.show()


# Candle sticks
ohlc = df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
ohlc = ohlc.set_index('Date')

# Consider only the first 200 data entries for candlestick chart
ohlc = ohlc.head(200)

# Plot the candlestick chart
mpf.plot(ohlc, type='candle', style='yahoo',
         title='Candlestick Chart', ylabel='Price', volume=True)


# Daily returns
# Consider only the first 200 data entries for daily returns
df = df.head(200)

# Convert data to DataFrame
df = pd.DataFrame(df)

# Convert the 'Date' column to datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Sort the DataFrame by date in ascending order
df.sort_values(by='Date', inplace=True)

# Calculate the daily returns
df['DailyReturns'] = df['Close'].pct_change()

print(df)
