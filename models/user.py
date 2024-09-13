#!/usr/bin/env python3
from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from requests import get
class user(BaseModel,Base):
    __tablename__='user'
    id=Column(String(50),nullable=False)
    name=Column(String(32), primary_key=True, nullable=False)
    password=Column(String(256),unique=True)
    access_control=Column(String(32))
    email=Column(String(32), nullable=False,unique=True)
    def __init__(self,*args,**kwargs):
        url='https://api.genratr.com/?length=16&uppercase&lowercase&special&numbers'
        temp=get(url)
        if temp.status_code==200:
            password=temp.json()['password']
            kwargs['password']=password
        super().__init__(*args,**kwargs)