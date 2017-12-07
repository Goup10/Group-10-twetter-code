# import tweepy
import tweepy
import pandas as pd
from time import sleep

# access token which can be obtained at your twitter account
ckey="tt20UIreiuMuLTktOhSaaWC1A"
csecret="gqBcyZnsCrOvEraoeXvFJpxkBmwEF9R1YaMcjDETnwj5JAO62I"
atoken="919991162114633728-8mSdRyxm9ZK7fgjtDlMYzmwHrxKrjEK"
asecret="vjFQOr7ysaZJebcYCDpeAigwnkebP4MVV2VU4EX7m34iJ"

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

auth.secure = True
api = tweepy.API(auth)


# begin with an empty list
myData = []




def mine_data():

    # count the number of 403 error reports
    count403 = 0

    # three tags to maximize chance of finding more data
    for tweet in tweepy.Cursor(api.search,q='#black_friday', p='#blackfriday', r='blackfirday2017',lang='en').items(1000):

        try:
            # information per tweet
            bf=[]
            bf.append(tweet.id)
            bf.append(tweet.user.name)
            bf.append(tweet.author.location)
            bf.append(tweet.created_at)
            bf.append(tweet.text)
            bf.append(tweet.favorite_count)
            bf.append(tweet.retweet_count)
            myData.append(bf)
            print("\n\nFound tweet by: @" + tweet.user.screen_name)
            count403=0

        # pause if 403 occurs too frequently
        except tweepy.TweepError as e:
            print(e.reason)
            if "403" in e.reason:
                if count403 > 15:
                    print("There are too many 403 errors. Pausing for 30 mins")
                    sleep(1800)
                else:
                    count403 += 1
                    print("Another 403 error. Total: " + str(count403))
                    sleep(1)

       # otherwise continue with 10 seconds break
        else:
            sleep(10)
            continue




# repeat the above function for three times, with 60 seconds break after each collection process
i = 0            
while i < 3:
    mine_data()
    print ("finished")
    sleep(60)
    i=i+1


# output in the form of pd            
output=pd.DataFrame(myData, columns = ['id','username','geographic','time', 'content', 'favorite count', 'retweet_count'])
output.to_csv('blackfriday5.csv', encoding='utf-8')

