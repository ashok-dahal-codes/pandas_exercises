import pandas as pd

df = pd.read_csv("data.csv")
print(df.head(10))
print(df.tail())#default is 5 rows for head and tail from first and last respectively