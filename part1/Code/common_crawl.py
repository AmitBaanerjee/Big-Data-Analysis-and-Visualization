#https://gist.github.com/Smerity/afe7430fdb4371015466
#https://pypi.org/project/langdetect/
#!pip install warc3-wet
import warc
import wget
from langdetect import detect

exurl ="https://commoncrawl.s3.amazonaws.com/crawl-data/CC-MAIN-2019-13/segments/1552912202658.65/wet/CC-MAIN-20190322115048-20190322141048-00227.warc.wet.gz"
wget.download(exurl,out="../Data/Commoncrawl")
from sh import gunzip
gunzip("../Data/Commoncrawl/CC-MAIN-20190322115048-20190322141048-00227.warc.wet.gz")
records = warc.open("../Data/Commoncrawl/CC-MAIN-20190322115048-20190322141048-00227.warc.wet")
counter=0
data=[]
urls=set()
keywords=['soccer','basketball','sports','baseball','score','hockey','mls','nba','ncaa','nfl','knicks','mma','nhl','golf']
for record in records:
    if counter==600:
        break
    else:
        url=record.header.get('warc-target-uri',None)
        if not url:
            continue
        if url not in urls:
            urls.add(url)
            text=record.payload.read()
            try:
                if detect(text.decode('utf-8'))=='en':
                    if (any(word in text.decode('utf-8') for word in keywords)):
                        data.append(str(text,'utf-8'))
                        counter+=1
            except Exception:
                print("lang detect exception")
                continue

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer('english')
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import re
import preprocessor as p
newfile=open('../Data/Commoncrawl/CrawlData.txt','a')
for line in data:
    stop_words = set(stopwords.words('english'))
    stoplist=['jan','feb','mar','apr','may','june','july','august','oct','nov','dec','sept','mr','Mr','said','/','//','www','http','url','avail','file','doc','descript','servic']
    for i in stoplist:
        stop_words.add(i)
    line=re.sub('\W+',' ',line)
    singles=[]
    for plural in line.split():
        if not wordnet.synsets(plural):
            continue
        else:
            if plural.lower() not in stop_words:
                if len(plural.lower())>=3:
                    singles.append(p.clean(stemmer.stem(plural)))
    if len(singles)>3:    
        newfile.write((' '.join(singles)))
        newfile.write('\n\n')


        
