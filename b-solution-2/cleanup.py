import pandas as pd

# Read the data from the Feather file into a DataFrame
df = pd.read_feather("out.feather")

# Write the DataFrame to a CSV file
df.to_csv("out.csv", index=False)