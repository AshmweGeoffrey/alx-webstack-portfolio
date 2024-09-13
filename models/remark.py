from models.base_model import BaseModel, Base
from sqlalchemy import Column, String,DateTime
from datetime import datetime
from sqlalchemy.orm import relationship 
class remark(BaseModel,Base):
    __tablename__='remark'
    id=Column(String(50),primary_key=True)
    time_stamp=Column(DateTime,nullable=False)
    message=Column(String(1000),nullable=False)
    def __init__(self, *args, **kwargs):
        kwargs['time_stamp']=datetime.now()
        super().__init__(*args, **kwargs)