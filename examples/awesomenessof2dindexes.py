from pymongo import MongoClient
import random
import string
from data import drop_data, load_data_file


def load_data(collection, n=100):
    #2d indexes FTW
    max_x = 180
    max_y = 180
    for j, d in load_data_file(n):
        d['rand'] = [random.randint(-max_x, max_x), random.randint(-max_y, max_y)]
        collection.insert( d )
    collection.create_index( [('rand', '2d')])


mc = MongoClient()
db = mc.simplerandom
collection = db.names

number_of_documents = 100

load_data(collection, number_of_documents )

x = random.randint(-180, 180)
y = random.randint( -180, 180)

query = {'rand': {'$near': [x, y]}}

winner = collection.find_one(query)

print u"AND THE WINNER IS ..... " + winner['name'].encode('utf-8', errors='ignore')

drop_data(collection)
