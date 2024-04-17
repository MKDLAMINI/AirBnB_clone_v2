#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import specified_storage


class Amenity(BaseModel, Base):
    """ This class represents amenity with various attributes"""
    __tablename__ = 'amenities'
    if specified_storage == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
