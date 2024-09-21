#!/usr/bin/python
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from models.base_model import BaseModel ,Base
from datetime import datetime
from models.category import category
class inventory(BaseModel,Base):
    # sql model for the inventory table
    __tablename__='inventory'
    id=Column(String(50),nullable=False)
    name=Column(String(64),nullable=False,primary_key=True)
    category_name=Column(String(32),ForeignKey('category.name'),nullable=False)
    inventory_quantity=Column(Integer,nullable=False,default=0)
    incoming_time_stamp=Column(DateTime,nullable=True)
    def __init__(self,*args,**kwargs):
        kwargs['incoming_time_stamp']=datetime.now()
        super().__init__(**kwargs)