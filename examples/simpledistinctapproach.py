from pymongo import MongoClient
import random
import string
from data import drop_data, load_data_file

def load_data(collection, n=100):
    #let's skip some elements
    skiplist = [10, 12, 231 , 2 , 4]
    for i,d in load_data_file(n):
        d['i'] = i
        if i in skiplist:
            continue
        collection.insert( d )

mc = MongoClient()
db = mc.simplerandom
collection = db.names


load_data(collection, 100)

distinct = collection.distinct('i')

ivalue = random.sample(distinct, 1)[0]

winner = collection.find_one({ 'i': ivalue })

print u"AND THE WINNER IS ..... " + winner['name']

drop_data(collection)
