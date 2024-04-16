from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models import specified_storage
from models.city import City

class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    if specified_storage == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete", backref="state")

    else:
        name = ''
