from pymongo.mongo_client import MongoClient # type: ignore

uri = "<URL OF MONGODB>"

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)