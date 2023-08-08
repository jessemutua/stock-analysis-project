import pandas as pd
import random

# Read the data from the CSV file
df = pd.read_csv("data/i'll_use_this.csv")

# Data cleaning
# Round numerical columns to six decimal places
numerical_columns = ["Open", "High", "Low", "Close", "Adj Close"]
df[numerical_columns] = df[numerical_columns].apply(lambda x: round(x, 6))

# Fill cases where volume is 0 with random values
non_zero_volumes = df[df["Volume"] != 0]["Volume"]
mean_volume = non_zero_volumes.mean()
std_volume = non_zero_volumes.std()


def generate_random_volume():
    return random.uniform(mean_volume, std_volume)


df["Volume"] = df["Volume"].apply(
    lambda x: generate_random_volume() if x == 0 else x)

# Save the cleaned DataFrame to a new CSV file
df.to_csv("cleaned_data.csv", index=False)
