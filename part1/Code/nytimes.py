#REFERENCE:-https://dlab.berkeley.edu/blog/scraping-new-york-times-articles-python-tutorial
import requests
import time
from bs4 import BeautifulSoup

soccer_articles=[]
for count in range(0,100):
    time.sleep(7)
    r = requests.get("http://api.nytimes.com/svc/search/v2/articlesearch.json?q=soccer&begin_date=20190101&page=%d&api-key=NyFyz5eXPhwf3MJgp3GAayXQTWbIrVVE"%(count))
    print(count)
    articles = r.json()
    for i in articles["response"]["docs"]:
        soccer_articles.append(i['web_url'])

all_articles=soccer_articles

querywords=['basketball','baseball','american football','ice hockey']
for word in querywords:
    for count in range(0,100):
        time.sleep(7)
        r = requests.get("http://api.nytimes.com/svc/search/v2/articlesearch.json?q=%s&begin_date=20190101&page=%d&api-key=NyFyz5eXPhwf3MJgp3GAayXQTWbIrVVE"%(word,count))
        print(count)
        articles = r.json()
        for i in articles["response"]["docs"]:
            all_articles.append(i['web_url'])
            
data=[]
for i in range(0,len(all_articles)):
    try:
        test=requests.get(all_articles[i])
        html=BeautifulSoup(test.content,'html.parser')
        paragraphs = html.find_all('p', class_='css-1ygdjhk evys1bk0')
        for p in paragraphs:
            data.append(p.get_text())
    except requests.ConnectionError as e:
        print("connection error received")
        continue
    except requests.Timeout as e:
        print("timeout error achieved")
        continue
    except requests.RequestException as e:
        print("general error")
        continue
    
with open('../Data/NYT/NytData.txt','a') as file:
    for i in range(0,len(data)):
        file.write(str(data[i])+"\n\n")
      
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
import re

def stemming():
    stop_words = set(stopwords.words('english')) 
    stop_words.add('Mr')
    stop_words.add('mr')
    stop_words.add('said')
    newout=open('../Data/NYT/processed_NytData.txt',"w")
    with open('NytData.txt', 'r') as f:
        for line in f:
            singles = []
            stemmer = SnowballStemmer('english')
            line=re.sub('\W+',' ',line)
            for plural in line.split():
                if plural.lower() not in stop_words:
                    singles.append(stemmer.stem(plural))
            newout.write((' '.join(singles))+'\n')
stemming()
