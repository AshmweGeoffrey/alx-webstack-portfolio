# Import the DBStorage and MongoStorage classes
from models.engine.db_engine import DBStorage
from models.engine.mongo_engine import MongoStorage
from app1 import current_db
# Create a new instance of DBStorag
import threading
# models/engine/dynamic_storage.py

from models.engine.db_engine import DBStorage
from models.engine.mongo_engine import MongoStorage
from app1 import current_db
# DBStorage instance
storage=DBStorage(current_db)
# Mongo Storage
mongo_storage = MongoStorage()