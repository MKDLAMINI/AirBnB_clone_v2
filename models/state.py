#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models import specified_storage
from models.city import City


class State(BaseModel, Base):
    """ A class representing state data """

    __tablename__ = 'states'
    if specified_storage == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete", backref="state")

    else:
        name = ''

def __init__(self, *args, **kwargs):
    """Initialize state"""
    super().__init__(*args, **kwargs)

if specified_storage == "db":
   @property
   def cities(self):
       """Getter for list of city instances related to state"""
       city_list = []
       all_cities = models.storage.all(City)
       for city in all_cities.values():
           if city.state_id == self.id:
               city_list.append(city)
       return city_list
