#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ This is the class for amenities """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
