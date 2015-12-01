#!/usr/bin/env python
from pymongo import MongoClient
import random
from data import drop_data, load_data, get_data

mc = MongoClient()
db = mc.simplerandom
collection = db.names

load_data(collection)

elements = []
for e in get_data(collection, filter={'name':1}):
    elements.append(e)

idx = random.randint(0, len(elements))

print u"AND THE WINNER IS ..... " + elements[idx]['name'].decode('utf-8', errors='ignore')

drop_data(collection)
