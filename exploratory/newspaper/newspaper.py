# Newspaper Stuff
# Needed to run the following commands for module to download on Mac
# brew install libxml2 libxslt
# brew install libtiff libjpeg webp little-cms2
# pip install newspaper
# http://stackoverflow.com/questions/19548011/cannot-install-lxml-on-mac-os-x-10-9

import newspaper
from newspaper import Article
from collections import defaultdict
import pickle
import datetime, date, timedelta
import pytz

def buildNewspaper():
    cnn_paper = newspaper.build(u'http://cnn.com', memoize_articles=False)
    a = defaultdict(int)
    print cnn_paper.size()
    for index, art in enumerate(cnn_paper2.articles):
        url = art.url
        article = Article(url)
        article.download()
        article.parse()
        if article.publish_date:
            a[url] = article.publish_date
        print "Article Added " + str(index) 
    pickle.dump( a, open( "unsorted.p", "wb" ) )

def sortNewspaper():
    utc = pytz.UTC
    toDelete = []

    news = pickle.load( open( "unsorted.p", "rb" ) )
    for i, key in enumerate(news.keys()):
        try:
            news[key] = utc.localize(news[key]) 
        except:
            toDelete.append(key)
        print "yay " + str(i)
    print toDelete
    for k in toDelete:
        news.pop(k, None)
    sortedNews = sorted(news.items(), key=lambda p: p[1])
    print sortedNews
    pickle.dump( sortedNews, open( "sorted.p", "wb" ) )

def dayCount():
    news = pickle.load( open( "sorted.p", "rb" ) )
    for days_to_subtract in range(0,30):    
        total = 0
        d = (utc.localize(datetime.today() - timedelta(days=days_to_subtract) ).date()
        for i, key in enumerate(news.keys()):
            if news[key].date() == d:
                total +=1   
        print "{}\tdocuments from\t{}".format(total,d)

def newsToday():
    for i, key in enumerate(news.keys()):
        if news[key].date() == utc.localize(datetime.today() - timedelta(days=0) ).date():
            print key











