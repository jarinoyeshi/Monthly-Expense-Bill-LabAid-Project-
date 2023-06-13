

from sqlalchemy import Column, Integer, String 
from .BaseModel import BaseModel
from  App.Database import Base
from marshmallow import Schema,fields


class User(Base,BaseModel):
    __tablename__ = 'User'
    
    
    id = Column(Integer(), primary_key= True, autoincrement= True)
    username= Column(String(50),unique=True)
    password= Column(String(100))
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        return self



class UserSchema(Schema):
    
    id= fields.Int()
    username= fields.Str()
    password= fields.Str()
    
    IsActive= fields.Bool()
    CreatedByID= fields.Str()