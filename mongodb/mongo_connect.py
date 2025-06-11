from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import urllib.parse


def connect_mongodb():
    # Replace the placeholder with your Atlas connection string
    username = urllib.parse.quote_plus('denkard')
    password = urllib.parse.quote_plus('FnVKtmsgAqhs71cJBmCs')

    uri = f"mongodb+srv://{username}:{password}@cluster1.psym4xc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"

    # Set the Stable API version when creating a new client
    myclient = MongoClient(uri, server_api=ServerApi('1'))
    # db = myclient['medicina']

    # Send a ping to confirm a successful connection
    try:
        myclient.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    return myclient


if __name__ == '__main__':
    myclient = connect_mongodb()
    mydb = myclient["mydatabase"]
    mycol = mydb['mycollection']