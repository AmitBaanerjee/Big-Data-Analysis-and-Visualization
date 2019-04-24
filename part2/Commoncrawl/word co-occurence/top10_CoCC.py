from collections import defaultdict
dictionary=defaultdict(int)

with open('reducer_output/part-00000.txt','r') as f:
        for line in f:
            temp=line.split('\t')
            dictionary[temp[0]]+=int(temp[1])
        f.close()

with open('reducer_output/part-00001.txt','r') as f:
        for line in f:
            temp=line.split('\t')
            dictionary[temp[0]]+=int(temp[1])
        f.close()

with open('reeducer_output/part-00002.txt','r') as f:
        for line in f:
            temp=line.split('\t')
            dictionary[temp[0]]+=int(temp[1])
        f.close()
        
counter=0


with open('top10_CoCommonCrawl.txt','w') as f:
    for w in sorted(dictionary, key=dictionary.get, reverse=True):
        if counter==10:
            break
        temp=w+'\t'+str(dictionary[w])
        print(temp)
        f.write(temp+'\n')
        counter+=1
    f.close()
