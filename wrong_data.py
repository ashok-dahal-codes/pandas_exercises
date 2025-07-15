import pandas as pd
df = pd.read_csv("wrong_data.csv")
df.loc[7, "Duration"]=45
print(df.to_string())
