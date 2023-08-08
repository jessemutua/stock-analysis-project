# daily_returns.py

import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
df = pd.read_csv("data/i'll_use_this.csv")

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Sort the DataFrame by date in ascending order
df.sort_values(by='Date', inplace=True)

# Calculate the daily returns
df['DailyReturns'] = df['Close'].pct_change()

# Create the histogram for daily returns
plt.figure(figsize=(10, 6))
plt.hist(df['DailyReturns'].dropna(), bins=50, edgecolor='black', alpha=0.7)
plt.title('Distribution of Daily Returns')
plt.xlabel('Daily Returns')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.savefig('results/daily_returns_histogram.png')
plt.show()
