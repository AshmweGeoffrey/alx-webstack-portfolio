from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
class outgoing_stock(BaseModel,Base):
    __tablename__='outgoing_stock'
    id=Column(String(50), primary_key=True,nullable=False)
    item_name=Column(String(64),ForeignKey('inventory.name'),unique=True,nullable=False)
    #category_name=Column(String(32),ForeignKey('inventory.category_name'),unique=True,nullable=False)
    user_name=Column(String(32),ForeignKey('user.name'),unique=True)
    branch_name=Column(String(16),ForeignKey('branch.branch_name'),nullable=False,unique=True)
    quantity=Column(Integer,nullable=False)
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)