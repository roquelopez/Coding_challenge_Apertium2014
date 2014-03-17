# -*- coding: utf-8 -*-
'''
Created on 16/03/2014

@author: roque
'''
import codecs
import os
from twython import Twython, TwythonError

APP_KEY = 'NYMv3BWY4MXjuG3pSKaY3w'
APP_SECRET = 'IjQfkJndkIf7adcrrPsuhSpMkp3E0bPv8CHTXW0Lg'
OAUTH_TOKEN = '262471257-tGXsQqGI9zhgbrI5cmIsrfSeZ9jbS3mqyQY5Ftsj'
OAUTH_TOKEN_SECRET = 'PnZe42OGjF951ejJCHvhjnAFp9x2eabFuF2Lio1CLKE'

api = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

def search_tweets(keyword, total_tweets, file_name):
    ''' Search tweets that contains the keyword '''
    fout = codecs.open(file_name, 'a', 'utf-8')
    
    if total_tweets > 100:
        total_tweets = 100
        print("The maximum number for this example is 100")
    
    tweets = api.search(q=keyword, count=total_tweets, lang='en', result_type='recent')      
    for tweet in tweets["statuses"]:
        fout.write("%s ==> %s\n" % (tweet['id'], tweet['text'].encode('utf-8').replace('\n','')))
    
    fout.close()
    print("Total tweets: ", total_tweets)
      
def main():
    ''' The main function '''
    file_in = "../resource/data_twitter.txt"
    file_out = "../resource/data_translated.txt"
    keyword = "you"
    total_tweets = 100
    from_to = "en-es"
    search_tweets(keyword, total_tweets, file_in)
    #os.system("apertium %s %s %s" % (from_to, file_in, file_out)) 
           
if __name__ == '__main__':
    main()
    