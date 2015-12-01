from pymongo import MongoClient
import random
import string
from data import drop_data, load_data_file


def load_data(collection, n=100):
    #fixed number of marks
    max_i = 10
    for j,d in load_data_file(n):
        d['i'] = random.randint(0, max_i)
        collection.insert( d )

mc = MongoClient()
db = mc.simplerandom
collection = db.names

number_of_documents = 100

load_data(collection, number_of_documents )

query = {'i': random.randint(0, 10 )  }

docs = [x for x in collection.find(query)]

winner = random.sample(docs, 1)[0]

print u"AND THE WINNER IS ..... " + winner['name'].encode('utf-8', errors='ignore')

drop_data(collection)
