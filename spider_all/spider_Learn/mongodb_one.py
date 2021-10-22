import pymongo
import time
client = pymongo.MongoClient('localhost', 27017)
db = client.testone
collection = db.books
book = [{
    "author": "mike",
    "text": "my test book",
    "tags": ["spider", "web", "python"],
    "datetime": "20190401"
    },
    {
    "author": "qiye",
    "text": "my test book two",
    "tags": ["data", "scince", "python"],
    "datetime": "20190402"
    },
    {
    "author": "jake",
    "text": "my test book three",
    "tags": ["big data", "pysaprk", "python"],
    "datetime": "20190403"
    }
]

book_id = collection.insert(book)

time.sleep(4)

for book in collection.find({"author": "qiye"}):
    print(book)
time.sleep(3)

print(collection.find({"author": "qiye"}).count())
