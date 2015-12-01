from pymongo import MongoClient
import random
import string
from data import drop_data, load_data

mc = MongoClient()
db = mc.simplerandom
collection = db.names
number_of_documents = 100

load_data(collection, number_of_documents)

winner = [ d for d in collection.aggregate([{'$sample': {'size': 1 }}])][0]

print u"AND THE WINNER IS ..... " + winner['name'].encode('utf-8', errors='ignore')

drop_data(collection)
