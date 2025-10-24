
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://sujalbs2018:51qNQH03qAbm2Yhr@cluster0.3wwcdmo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)