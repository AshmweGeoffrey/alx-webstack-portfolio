from models.base_model import BaseModel,Base
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from models.user import user
from models.inventory_model import inventory
class sale_weekly(BaseModel,Base):
    # sql model for the sale_weekly table
    __tablename__ = 'sale_weekly'
    id = Column(String(50),primary_key=True,nullable=False)
    item_name = Column(String(64),ForeignKey('inventory.name'),unique=True)
    quantity = Column(Integer,nullable=False,default=1)
    price = Column(Integer,nullable=False,default=0)
    user_name = Column(String(32),unique=True)
    payment_method = Column(String(50),nullable=False)
    time_stamp = Column(DateTime,unique=True)
    def __init__(self,*args,**kwargs):
        kwargs['time_stamp']=datetime.now()
        super().__init__(*args,**kwargs)
