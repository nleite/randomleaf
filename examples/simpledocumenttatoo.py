from pymongo import MongoClient
import random
import string
from data import drop_data, load_data_file


def load_data(collection, n=100):
    #for each element we will insert the `i` value
    for i,d in load_data_file(n):
        d['i'] = i
        collection.insert( d )

mc = MongoClient()
db = mc.simplerandom
collection = db.names

number_of_documents = 100

load_data(collection, number_of_documents )

query = {'i': random.randint(0, number_of_documents )  }

winner = collection.find_one(query);

print u"AND THE WINNER IS ..... " + winner['name']

drop_data(collection)
