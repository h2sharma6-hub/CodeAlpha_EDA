
# Task 2 : Exploratory Data Analysis (EDA)
import pandas as pd

df = pd.read_csv("quotes.csv")

# Checking basic info
print(df.info())

# Missing values check
print("Missing values:\n", df.isnull().sum())

# Top authors
print("Top authors:\n", df['Author'].value_counts().head(5))

# Quote length column
df['Quote_Length'] = df['Quote'].apply(len)
print("Average quote length:", df['Quote_Length'].mean())

