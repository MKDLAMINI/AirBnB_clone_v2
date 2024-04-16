from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models import specified_storage

class City(BaseModel, Base):
    """ City class """

    __tablename__ = 'cities'
    if specified_storage == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    else:
        name = ''
        stae_id = ''
