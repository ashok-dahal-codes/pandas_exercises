import pandas as pd
df = pd.read_csv("download_data.csv")
print(df.corr())