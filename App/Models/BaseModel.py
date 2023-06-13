from  App.Database import Base
from sqlalchemy import Column,Boolean,String,DateTime
from datetime import datetime


class BaseModel():
    IsActive= Column(Boolean, default=True)
    CreatedByID= Column(String(10))
    CreatedOn= Column(DateTime, default=datetime.now)
    UpdatedByID= Column(String(10))
    UpdatedOn= Column(DateTime, onupdate=datetime.now)