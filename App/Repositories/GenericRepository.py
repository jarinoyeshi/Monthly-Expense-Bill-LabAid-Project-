

#from .IGenericRepository import IGenericRepository
from typing import TypeVar,List
from ..Database import session,Base


Entity= TypeVar('Entity',bound=Base)



class GenericRepository():
    
    def __init__(self,  modelType:type(Entity)):
        self.modelType= modelType
     
     
    def getAllData(self) -> List[Entity]:
        return session.query(self.modelType).all()
    
    
    def getDataByID(self, ID:int)->Entity:
        return session.query(self.modelType).filter_by(id=ID).first()
    

    
    
    def save(self, entity: Entity) -> Entity:
       session.add(entity)
       session.commit()
       session.refresh(entity)
       return entity
       
    
    def delete(self, ID: int)->None:
        pass
