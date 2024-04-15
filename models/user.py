#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """ User class that inherits from BaseModel and Base """
    __tablename__ = 'users'

    password = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    last_name = Column(String(128))
    first_name = Column(String(128))
