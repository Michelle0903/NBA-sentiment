import tweepy as tw
import pandas as pd
import csv



consumer_key= 'hsYZLYpyBMUrVWiRKa2eowMFV'
consumer_secret= 'j6DAPX5yEpAVQAk08CfHIQN1lxzeclAlxB5PMokjU0a6P8oGlu'
access_token= '1132363369837735936-53lPl5unajTNakU50Z3nqwQqPEQwL8'
access_token_secret= '79WOU5fiDuh8vXh9uXtUUkrskRL6h6vzhyyNVjKsHceht'
search_words = "mvp"
date_since = "2019-03-01"
# end_date="2019-05-15"
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
new_search = search_words + " -filter:retweets"
tweets = tw.Cursor(api.search,
              q=new_search,
              lang="en",
              since=date_since).items(10000)#爬多少条
# for tweet in tweets:
#     print(tweet.text)


csv_out = open('tweets_out_mvp.csv', mode='w') 
writer = csv.writer(csv_out) 

fields = ['text'] 
writer.writerow(fields) 
count=1
for i in tweets:
	try:
		writer.writerow([i.text.encode('ascii', 'ignore')])
		count+=1
		if count%100==0:
			print(str(count)+'has finished')
	except:
		continue


csv_out.close()