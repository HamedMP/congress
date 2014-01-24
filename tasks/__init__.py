from mongo import MongoUtils

def init_mongo(host, db="congress"):
    global MONGO_CACHE
    MONGO_CACHE = MongoUtils(host, db=db)
