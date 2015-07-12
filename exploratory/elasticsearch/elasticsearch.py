# ES Testing
from elasticsearch import Elasticsearch 

BONSAI_URL = "INSERT_URL"

# Creating elasticsearch and index
es = Elasticsearch(BONSAI_URL)
es.indices.create(index='news', ignore=400)

# Adding and retrieving a document
doc = {
    'domain': 'CNN',
    'date': datetime(2010, 10, 10, 10, 10, 10),
    'text': 'This is an article.'
}
res = es.index(index="news", doc_type='article', id=1, body=doc)
res = es.get(index="news", doc_type='article', id=1)
es.indices.refresh(index="news")

# Returning all documents
res = es.search(index="news", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])

# Finding simlarity
# NOTE similarity does not work for test sentences. 
# A senstence will generally not be simialr enough regardless
es.mlt(index='news', doc_type="article",
                          id=1, mlt_fields="text", 
                          search_size=7,
                          min_term_freq=0,
                          min_doc_freq=0,
                          percent_terms_to_match= 0)

