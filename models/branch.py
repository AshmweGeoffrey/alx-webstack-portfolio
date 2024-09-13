from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship 
class branch(BaseModel,Base):
    __tablename__='branch'
    id=Column(String(50),nullable=False)
    branch_name=Column(String(16), nullable=False,primary_key=True)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)