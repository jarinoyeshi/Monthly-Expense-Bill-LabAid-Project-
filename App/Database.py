

from flask import Flask
from sqlalchemy.orm import declarative_base,Session,scoped_session,sessionmaker
from sqlalchemy import create_engine



engine = None
Base= None
session = None



def  registerDatabase(app):
    global engine,Base,session
    
    engine= create_engine(app.config.get("DATABASE_URI"))
    session = scoped_session(sessionmaker(bind=engine,autoflush=False,autocommit=False))
    Base = declarative_base()


def createTable():
    from .Models.User import User
    Base.metadata.create_all(bind=engine)
    
    # from .Repositories.UserRepository import UserRepository
    # newUser = User("Jarin","123456")
    # UserRepository().save(newUser)
    