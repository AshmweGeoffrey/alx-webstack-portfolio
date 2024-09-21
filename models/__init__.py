from models.engine.db_engine import DBStorage
from models.engine.mongo_engine import MongoStorage
from app1 import current_db
# DBStorage instance
storage=DBStorage('AX_STOCK_ALX_PROJECT')
# Mongo Storage
mongo_storage = MongoStorage()