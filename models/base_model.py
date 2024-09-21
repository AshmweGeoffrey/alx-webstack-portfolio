#!/usr/bin/python3
from datetime import datetime
import models
from uuid import uuid4
from sqlalchemy.ext.declarative import  declarative_base
from app1 import current_db
import redis
Base=declarative_base()
class BaseModel:
    # Base class for all the models in the application
    def __init__(self,*args,**kwargs):
        if kwargs:
            kwargs['id']=str(uuid4())
            for key, value in kwargs.items():
                setattr(self, key, value)
    def create(self):
        pass

    def read(self):
        pass

    def update_db_name(self):
        pass

    def delete(self):
        pass

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,self.__dict__)
    def __repr__(self):
        pass
    def __del__(self):
        pass
    def save(self):
        # save the current object to the database
        if current_db is not None:
            client = redis.Redis(host='localhost', port=6379, db=0)
            db_name=(client.get(current_db)).decode('utf-8')
            models.storage.connect(db_name)
        models.storage.new(self)
        models.storage.save()
    def select_all(self,order):
        # custom select all query for the current table
        if current_db is not None:
            client = redis.Redis(host='localhost', port=6379, db=0)
            db_name=(client.get(current_db)).decode('utf-8')
            models.storage.connect(db_name)
        table_name=self.__tablename__
        if order is None:
            query="SELECT * FROM {:s}".format(table_name)
        else:
            query="SELECT * FROM {:s} {:s}".format(table_name,order)
        result=models.storage.command(query)
        main_list=[]
        inner_list=[]
        for  i in result.fetchall():
            for j in i:
                inner_list.append(j)
            main_list.append(inner_list)
            inner_list=[]
        return main_list
    def get_user(self, user_name):
        # -+> get the user from the current table [Discontinued]!!
        if current_db is not None:
            client = redis.Redis(host='localhost', port=6379, db=0)
            db_name=(client.get(current_db)).decode('utf-8')
            models.storage.connect(db_name)
        table_name = self.__tablename__
        result = models.storage.command("SELECT name FROM {} WHERE name='{}'".format(table_name, user_name))
        main_list = []
        for i in result.fetchall():
            for j in i:
                main_list.append(j)
        return main_list