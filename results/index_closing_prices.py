import pandas as pd
import matplotlib.pyplot as plt

# Read the cleaned data from the CSV file
df = pd.read_csv("cleaned_data.csv")

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Sort the DataFrame by date in ascending order
df.sort_values(by='Date', inplace=True)

# Create the line chart
plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
plt.plot(df['Date'], df['Close'], marker='o', label='Closing Price')

# Customize the chart
plt.title('NYA Index Closing Prices over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price')

# Rotate the x-axis labels for better readability (optional)
plt.xticks(rotation=45)

# Add legend
plt.legend()

# Show the chart
plt.tight_layout()
plt.show()
