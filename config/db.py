from pymongo import MongoClient


client = MongoClient(
    "mongodb+srv://user:user.123.p@socialmediacluster.elxk9mp.mongodb.net/?retryWrites=true&w=majority")
db = client.API

#db = connection[userData]
