

from .GenericRepository import GenericRepository
from ..Database import Base, session
from ..Models.User import User,UserSchema

class UserRepository(GenericRepository):
        
        def __init__(self):
            super().__init__(User)
            
            
        def getUserByUsername(self, username):
            return session.query(User).filter_by(username=username).first()