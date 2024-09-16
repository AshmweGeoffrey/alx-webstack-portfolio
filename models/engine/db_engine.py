#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from web_flask.app1 import current_db
class DBStorage:
    __engine = None
    __session = None
    def __init__(self):
        if current_db is None:
            self.__engine = create_engine('mysql+mysqldb://root:Ashimwe#001@localhost:3306/{}'.format('AX_STOCK_ALX_PROJECT'),pool_pre_ping=True)
        else:
            self.__engine = create_engine('mysql+mysqldb://root:Ashimwe#001@localhost:3306/{}'.format(current_db),pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        self.engine= self.__engine
    def all(self, cls):
        if cls:
            return self.__session.query(cls).all()
        else:
            return self.__session.query(cls).all()
    def new(self, obj):
        self.__session.add(obj)
    def save(self):
        self.__session.commit()
    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)
    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
    def command(self, command):
        return self.__engine.execute(command)
    def close(self):
        self.__session.close()