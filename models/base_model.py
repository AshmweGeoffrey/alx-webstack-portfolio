#!/usr/bin/python3
from datetime import datetime
import models
from uuid import uuid4
from sqlalchemy.ext.declarative import  declarative_base
Base=declarative_base()
class BaseModel:
    def __init__(self,*args,**kwargs):
        if kwargs:
            kwargs['id']=str(uuid4())
            for key, value in kwargs.items():
                setattr(self, key, value)
    def create(self):
        pass

    def read(self):
        pass

    def update(self):
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
        models.storage.new(self)
        models.storage.save()
    def select_all(self,order):
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
        table_name = self.__tablename__
        result = models.storage.command("SELECT name FROM {} WHERE name='{}'".format(table_name, user_name))
        main_list = []
        for i in result.fetchall():
            for j in i:
                main_list.append(j)
        return main_list