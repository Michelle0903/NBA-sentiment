import pandas as pd 
df=pd.read_csv('training.csv',encoding="ISO-8859-1")
print(df.columns.values.tolist())
print(df.columns)
sum=0
for i in df['text']:
	if 'nba' in i.lower():
		sum+=1
print(sum)

