from typing import Collection
import pymongo


class Database:
    def __init__(self, database, collection):
        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            connectionString = "mongodb+srv://raulmp016:5W7QJkZne8DjiJZD@cluster0.16w8hl9.mongodb.net/test"
            self.clusterConnection = pymongo.MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
            print("Database connected successfully!")
        except Exception as e:
            print(e)

    def disconnect(self):
        try:
            self.db.drop_collection(self.collection)
            self.collection.insert_many()
            print("Database reseted successfully!")
        except Exception as e:
            print(e)