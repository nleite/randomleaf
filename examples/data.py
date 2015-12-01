import random
import string
import simplejson as json
def drop_data(collection):
    collection.drop()


def load_data_file(n):
    i = 0;
    with open('../members.json', 'r') as fdata:
        data = json.load(fdata)

    for d in data:
        yield (i, d)
        i+=1
        if i >= n:
            break

def load_data(collection, n=100):
    for i,d in load_data_file(n):
        collection.insert( d )

def get_data(collection, query={}, filter=None):
    for d in collection.find(query, filter):
        yield d
