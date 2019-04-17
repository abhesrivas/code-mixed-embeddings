from scraper import AdvancedSearchScraper
import sys
import string
import re

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def scrape_tweets(word, count, start, end):
	
	if(start==0 and end==0):
		name = "scraped/"+word+".txt"
		ass = AdvancedSearchScraper(word, count)
		tweets = ass.scrape()
		with open(name, 'w') as f:
		    for tweet in tweets:
		        text = tweet['tweet_text']
		        t_id = tweet['tweet_id']
		        language = tweet['tweet_language']
		        text = re.sub(r"http\S+", "", text)
		        text = text.translate(str.maketrans('','',string.punctuation))
		        text = text.lower()
		        text = text.translate(str.maketrans('','','1234567890'))
		        
		        if((is_ascii(text)) and (language=='en')):
			        f.write(str(t_id)+","+text+"\n")

	else:
		words = open("data/frequent_set_words.txt").read().split('\n')
		words = list(sorted(set(words)))
		name = "scraped/"+words[start]+"_to_"+words[end-1]+".txt"
		print(name)
	
		for i in range(start, end):
			word = words[i]
			ass = AdvancedSearchScraper(word, count)
			tweets = ass.scrape()
			print("Done for "+str(i)+" "+words[i])
			with open(name, 'a+') as f:
				for tweet in tweets:
					text = tweet['tweet_text']
					t_id = tweet['tweet_id']
					language = tweet['tweet_language']
					text = re.sub(r"http\S+", "", text)
					text = text.translate(str.maketrans('','',string.punctuation))
					text = text.lower()
					text = text.translate(str.maketrans('','','1234567890'))
			        
					if(is_ascii(text)):
						f.write(str(t_id)+","+text+"\n")

word = sys.argv[1]
count = int(sys.argv[2])
start = int(sys.argv[3])
end = int(sys.argv[4])

try:
	scrape_tweets(word, count, start, end)

except Exception as e:
	print("exception:")
	print(e)

print("Done!")
