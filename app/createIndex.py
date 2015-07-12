from config import BONSAI_URL
from elasticsearch import Elasticsearch
import newspaper
from newspaper import Article
from collections import defaultdict
import pytz

def makeDocs():
    utc = pytz.utc
    es = Elasticsearch(BONSAI_URL, verify_certs= True)
    es.indices.delete(index='news', ignore=[400, 404])
    es.indices.create(index='news', ignore=400)

    print "Created"
    cnn_paper = newspaper.build(u'http://cnn.com', memoize_articles=False)
    a = defaultdict(int)
    cnn_articles = cnn_paper.articles
    print cnn_paper.size()
    for i in range(10):
        article = cnn_articles[i]
        url = article.url
        art = Article(url)
        art.download()
        art.parse()
        print art.publish_date
        print art.text
        print "Article" + str(i)
        print art.publish_date is not None
        print art.text is not None
        if (art.publish_date is not None) and (art.text is not None):
            try:
                doc = {
                'domain': 'CNN',
                'date': utc.localize(art.publish_date), 
                'text': art.text
                }
                res = es.index(index="news", doc_type='article', id=i, body=doc)
                print "Doc" + str(i)
            except:
                print "Doc not accepted"


makeDocs()