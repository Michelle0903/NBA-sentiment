from textblob import TextBlob
import pandas as pd 



df=pd.read_csv('tweets_out.csv')
text=[]
result=[]
sum=0
for i in df.text:
	temp=TextBlob(i).sentiment[0]
	if temp==0:
		sum+=1

	elif temp>0:
		text.append(i)
		result.append(4)
	else:
		text.append(i)
		result.append(0)
final=pd.DataFrame(result)
final.to_csv('xxx.csv')
text=pd.DataFrame(text)
text.to_csv('modified.csv')
