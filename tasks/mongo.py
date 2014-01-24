from pymongo import MongoClient


class MongoUtils:
    """
    MongoUtils uses MongoClient from the pymongo library to store scraped congress data
    """

    def __init__(self, host="localhost", port=27017, db="congress"):

        # Construct a client to MongoDB
        try:
            self.client = MongoClient(host=host, port=port)
        except Exception as e:
            raise e

        # Get a Mongo database
        self.db = self.client[db]


    def put(self, document, collection="congress"):
        """
        Universal method for storing scraped data as MongoDB documents
        """
        col = self.db[collection]
        col.insert(document)

    def vote_exists(self, vote_id, collection="congress"):
        """
        Check for the existence of a vote
        """
        col = self.db[collection]

        condition = {"vote_id": vote_id}

        exists = col.find_one(condition)

        return True if exists else False

    def bill_exists(self, bill_id, collection="congress"):
        """
        Check for the existence of a bill
        """
        col = self.db[collection]

        condition = {"bill_id": bill_id}

        exists = col.find_one(condition)

        return True if exists else False

    def amendment_exists(self, amendment_id, collection="congress"):
        """
        Check for the existence of an amendment
        """
        col = self.db[collection]

        condition = {"amendment_id": amendment_id}

        exists = col.find_one(condition)

        return True if exists else False

    def nomination_exists(self, nomination_id, collection="congress"):
        """
        Check for the existence of a nomination
        """
        col = self.db[collection]

        condition = {"nomination_id": nomination_id}

        exists = col.find_one(condition)

        return True if exists else False
