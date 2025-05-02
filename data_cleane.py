import pandas as pd 
import numpy as np



df = pd.read_csv("uncleaned_employee_data.csv", encoding="latin1")
print(df.head(10))
print(df.tail(10))
print(df.isnull().sum())
df['age'].fillna(df["age"].mean(), inplace=True)
df['salary'].fillna(df["salary"].mean(), inplace=True)
df['experience'].fillna(df["experience"].mean(), inplace=True)
# df['city'].fillna(df["experience"].mean(), inplace=True)

print(df.isnull().sum())
df.replace([np.inf, -np.inf,], np.nan, inplace= True)
print(df.head(10))
print(df.tail(10))
print("is nan")
print(df.isna().sum())
df['salary'].fillna(df["salary"].mean(), inplace=True)
df['rating'].fillna(df["rating"].mean(), inplace=True)

print(df.head(10))
print(df.tail(10))


df.drop_duplicates(inplace=True)
df["salary"] = np.where(df["salary"] < 0, df["salary"].mean(), df["salary"])

df.to_csv('cleaned_employee_data.csv', index = False)
print("Cleaning complete")