import pandas as pd
df = pd.read_csv("duplicate_data.csv")
df.drop_duplicates(inplace = True)
print(df)