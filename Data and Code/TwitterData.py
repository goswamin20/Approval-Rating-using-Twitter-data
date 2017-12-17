import tweepy
import os
import MySQLdb as db

API_KEY = "LLgQNESwH8hlATxvLCe20clkM"
API_SECRET = "vxdbVrJENbhFp0KQnUfWBxtXjkkeZL63LHEU9zmNXfLiqepdJu"

auth = tweepy.AppAuthHandler(API_KEY, API_SECRET)
tweepy_api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

queries = ["@potus", "@uspresident", "@whitehouse", "@donaldtrump", "\"white house\"" ,
			"trump", "\"us president\"","potus", "uspresident", "whitehouse",  "@trump", 
		     "\"donald trump\"", "donaldtrump", "@realdonaldtrump"];

tweets = [];
connect = db.connect("localhost","root","","test");
cursor = connect.cursor()



def tweetCollector(x):
    t = tweepy.Cursor(tweepy_api.search, q=x+" -RT", lang="en", show_user=True)
    for tweet in t.items(2000000):
        if ("http" not in tweet.text):
            statustext = tweet.text.encode('ascii', 'ignore').decode('ascii')
            statustime = tweet.created_at
            userid = tweet.user.id
            statusid = tweet.id 
            sql_query = "INSERT INTO tweetdataset(userid, statusid, statustime, tweet) VALUES (\'"+ str(userid)+"\', \'"+ str(statusid) +"\', \'"+ str(statustime) +"\', \'"+ str(statustext) +"\')"
            try:
               cursor.execute(sql_query)
               connect.commit()
            except:
               connect.rollback()
    return tweets
	
query = "";
for i in range(len(queries)):
    if i == 0:
       query = queries[i] + "";
    else:
       query = query + " OR " + queries[i];
tweetCollector(query)
connect.close();