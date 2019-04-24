import tweepy as tw
import preprocessor as p
#import re
consumer_key= 'f42wKb5tUbNZPC6PcduwYxdG0'
consumer_secret= 'E7w8hq0ogjlsC8dNXHuoCZPplILQMhUMiWWs2RQjSeO5nCFtWn'
access_token= '128911319-9vFzl29NDvgnurRwxK80cRzO2tWukaqyYxVjA6CH'
access_token_secret= 'VlSDq7kSMlx3qloF5H0b5FW09Ljy93a8zvzcoyICgEpvM'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

#places = api.geo_search(query="USA", granularity="country")
#place_id = places[0].id
#burger,pancake,pie,beef
search_words = "Soccer -filter:retweets"
date_since = "2019-01-01"

tweets = tw.Cursor(api.search,
              q="soccer -filter:retweets",
              lang="en",
              since=date_since).items(5000)

tweets2 = tw.Cursor(api.search,
              q="basketball -filter:retweets",
              lang="en",
              since=date_since).items(5000)

tweets3 = tw.Cursor(api.search,
              q="baseball -filter:retweets",
              lang="en",
              since=date_since).items(5000)

tweets4 = tw.Cursor(api.search,
              q="ice hockey -filter:retweets",
              lang="en",
              since=date_since).items(5000)

tweets5 = tw.Cursor(api.search,
              q="american football -filter:retweets",
              lang="en",
              since=date_since).items(5000)

alltweets=[p.clean(tweet.text) for tweet in tweets if '@' not in tweet.text and not tweet.retweeted]

for t in tweets2:
    if not t.retweeted and '@' not in t.text:
        alltweets.append(p.clean(t.text))

for t1 in tweets3:
    if not t1.retweeted and '@' not in t1.text:
        alltweets.append(p.clean(t1.text))
        
for t2 in tweets4:
    if not t2.retweeted and '@' not in t2.text:
        alltweets.append(p.clean(t2.text))

for i in range(len(alltweets)):
    if 'http' in alltweets[i]:
        ind=alltweets[i].index('http')
        temp=ind
        while temp<len(alltweets[i]):
            if alltweets[i][temp]==' ':
                break
            else:
                temp+=1
        alltweets[i]=alltweets[i].replace(alltweets[i][ind:temp+1],'')
        
#remove_list = 'https:'
#for tweet in range(len(alltweets)):
 #   temp=alltweets[tweet].split()
  #  alltweets[tweet]=' '.join([i for i in temp if i not in remove_list])

with open('../Data/Twitter/TwitterData.txt', 'a') as f:
    for i in range(len(alltweets)):
        f.write(str(alltweets[i])+"\n")
        
lines_seen = set() # holds lines already seen
outfile = open('../Data/Twitter/finaltweetData.txt', "w")
for line in open('../Data/Twitter/TwitterData.txt', "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
#REFERENCE:-https://medium.com/@datamonsters/text-preprocessing-in-python-steps-tools-and-examples-bf025f872908
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords 
import re
#from nltk.tokenize import word_tokenize 
stop_words = set(stopwords.words('english')) 
newout=open('../Data/Twitter/processed_tweet.txt',"w")
#nltk.download('all')
def stemming_text_1():
    with open('../Data/Twitter/finaltweetData.txt', 'r') as f:
        for line in f:
            print(line)
            singles = []
            stemmer = SnowballStemmer('english')
            line=re.sub('\W+',' ',line)
            for plural in line.split():
                if plural.lower() not in stop_words:
                    singles.append(stemmer.stem(plural))
            newout.write((' '.join(singles))+'\n')
stemming_text_1()
