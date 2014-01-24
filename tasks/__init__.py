from mongo import MongoUtils

def init_mongo(host):
    global MONGO_CACHE
    MONGO_CACHE = MongoUtils(host)
