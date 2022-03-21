import pandas as pd
df = pd.read_csv('../new_vgsales.csv')
new_df=df.dropna(axis=0,how='any',subset=['NA_Sales','PAL_Sales','JP_Sales','Other_Sales','Global_Sales'])
print(new_df)
new_df.to_csv('mmm.csv')