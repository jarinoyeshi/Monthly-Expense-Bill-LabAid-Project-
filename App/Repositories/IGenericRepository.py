
from abc import ABC,abstractmethod
from typing import TypeVar,List
from App.Database import Base



Entity= TypeVar('Entity',bound=Base)

class IGenericRepostory(ABC):
    
    
    @abstractmethod
    def getAll(self,)->Entity:
        pass
    
    
    
    
    @abstractmethod
    def getByID(ID: str):
        pass
    
    
    
    
    @abstractmethod
    def addData(data):
        pass
    
    
    
    
    @abstractmethod
    def deleteData(ID: int)->None:
        pass
    
    
    
    
    @abstractmethod
    def deleteData(entity: Entity)->None:
        pass
    
    
    
    
    
    @abstractmethod
    def updateData():
        pass