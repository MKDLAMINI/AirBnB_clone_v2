#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Column, String, ForeignKey
from models import specified_storage


class Review(BaseModel, Base):
    """ Review class that stores all review data in specified storage """
    __tablename__ = 'reviews'
    if specified_storage == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    else:
        place_id = ""
        user_id = ""
        text = ""
