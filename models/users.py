from mongoengine import StringField, Document, DateTimeField,IntField
from  uuid import uuid4
from datetime import datetime
from models import mongo_storage
class User(Document):
    _id=StringField(default=lambda: str(uuid4()),primary_key=True)
    user_name = StringField(required=True)
    email = StringField(required=True)
    password = StringField(required=True)
    access_control = StringField(required=True,default='auditor')
    company = StringField(required=True)
    created_at = DateTimeField(required=True,default=str(datetime.now()))
    contact=StringField(required=True)
    address=StringField(required=True)
    db_name=StringField(required=True)
    def close(self):
        mongo_storage.close()