from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://admin:aLr3MfCjfwsoc17A@fliq.efxw0yx.mongodb.net/?retryWrites=true&w=majority")
db = client.fliq
