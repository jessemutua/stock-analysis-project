# scatter_plot.py

import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
df = pd.read_csv("data/i'll_use_this.csv")

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Sort the DataFrame by date in ascending order
df.sort_values(by='Date', inplace=True)

# Create the scatter plot for closing prices vs. trading volumes
plt.figure(figsize=(10, 6))
plt.scatter(df['Close'], df['Volume'], alpha=0.7, color='blue')
plt.title('Scatter Plot of Closing Prices vs. Trading Volumes')
plt.xlabel('Closing Prices')
plt.ylabel('Trading Volumes')
plt.grid(True)
plt.tight_layout()
plt.savefig('results/closing_prices_vs_trading_volumes_scatter.png')
plt.show()
