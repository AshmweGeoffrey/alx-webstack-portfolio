# Import the DBStorage and MongoStorage classes
from models.engine.db_engine import DBStorage
from models.engine.mongo_engine import MongoStorage

# Create a new instance of DBStorage
storage = DBStorage()
storage.reload()

# Create a new instance of MongoStorage
mongo_storage = MongoStorage()