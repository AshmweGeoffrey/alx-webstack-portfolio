#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from models.base_model import BaseModel ,Base
class category(BaseModel,Base):
    # sql model for the category table
    __tablename__='category'
    id=Column(String(50))
    name=Column(String(32), nullable=False, primary_key=True,)
    percentage=Column(String(16))
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)