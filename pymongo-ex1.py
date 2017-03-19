from pymongo import MongoClient
import datetime
import pprint

client = MongoClient()

#symbol='XXBTCZEUR'
#client = MongoClient()
#db = client['bitkraken']
#ltc_books = db[symbol+'_books']

client = MongoClient('localhost',27017)
db = client.test_database
collection = db['test-collection']

post = {"author": "Mike",
        "test":"My fisrt blog post!",
        "tags":["mongodb","python","pymongo"],
        "date": datetime.datetime.utcnow()}
post_id = db.posts.insert_one(post).inserted_id
print post_id
#pprint.pprint(db.posts.find_one())


post2 = {"author": "Mike",
        "test":"My second blog post!",
        "tags":["mongodb","python","pymongo"],
        "date": datetime.datetime.utcnow()}
post_id = db.posts.insert_one(post2).inserted_id
print post_id


#pprint(db.posts.find_one())


#db.inventory.find({"author" : "Mike"})

var = db.inventory.find()


print var
