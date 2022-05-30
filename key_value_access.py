import pandas as pd
data = pd.read_csv("output.csv",keep_default_na=False)

head_data = list(data.columns)

df = data.to_dict('list')
len_df = len(df['employee name'])
final_dict = []
for i in range(len_df):
   temp_dict ={}
   for x in head_data:
      temp_dict[x]=df[x][i]
   final_dict.append(temp_dict)
print(final_dict)



