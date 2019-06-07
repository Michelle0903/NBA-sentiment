 

from twitter import *
import re
import pandas as pd
import sys
import csv
sys.path.append(".")

auth = OAuth("1132363369837735936-53lPl5unajTNakU50Z3nqwQqPEQwL8",
                  "79WOU5fiDuh8vXh9uXtUUkrskRL6h6vzhyyNVjKsHceht",
                  "hsYZLYpyBMUrVWiRKa2eowMFV","j6DAPX5yEpAVQAk08CfHIQN1lxzeclAlxB5PMokjU0a6P8oGlu"
                  )
search_term=['houston rocket','Houston','Rocket']
pattern = re.compile("%s" % search_term, re.IGNORECASE)
stream = TwitterStream(auth = auth, secure = True)
tweet_iter = stream.statuses.filter(track = search_term,language='en')
# df = pd.DataFrame(columns=['id','Twitt_text'])

count=0

# for i in tweet_iter:
# 	if count>100:
# 		break
# 	count+=1
# 	print(i['text'])
# 	df=df.append({'id':i['id'],'Twitt_text':i['text']},ignore_index=True)
# df.to_csv('result.csv',encoding="utf8")



csv_out = open('tweets_out_houston.csv', mode='w') 
writer = csv.writer(csv_out) 

fields = ['text'] 
writer.writerow(fields) 

for i in tweet_iter:
	try:
		if count>100000:
		  break
		writer.writerow([i['text'].encode('ascii', 'ignore')])
		count+=1
		if count%100==0:
			print(str(count)+'has finished')
	except:
		continue


csv_out.close()

