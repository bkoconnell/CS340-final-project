# Project 2
# python module for CRUD operations

# create a MongoDB Client to the running mongod instance
from pymongo import MongoClient
from bson.objectid import ObjectId
import os


class AnimalShelter(object):

    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Start MongoDB
        os.system('/usr/local/bin/mongod_ctl start')
        
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:28441/?authMechanism=DEFAULT&authSource=AAC' % (username, password))
        self.database = self.client['AAC']

    # Method to implement the CREATE functionality
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary
            print('Successfully created.')
            return True
        else:
            print('Failed.  Data parameter is empty, nothing to save.')
            return False

    # Method to implement the READ functionality
    def read(self, data):
        if data is not None:
            return self.database.animals.find(data,{"_id":False})
        else:
            print('No results.  Data parameter is empty.')
            return False

    # Method to implement the UPDATE functionality
    def update(self, keyValue, updateValue):
        if updateValue is not None:
            self.database.animals.update(keyValue, updateValue)
            return True
        else:
            print('Failed.  Data parameter is empty, nothing to save.')
            return False

    # Method to implement the DELETE functionality
    def delete(self, keyValue):
        if keyValue is not None:
            self.database.animals.remove(keyValue)
            return True
        else:
            print('Failed.  Data parameter is empty, nothing to delete.')
            return False