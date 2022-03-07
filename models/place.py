#!/usr/bin/python3
""" Place Module for HBNB project """
from msilib import Table
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from models.review import Review
from os import getenv
import models


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer(), nullable=False, default=0)
    number_bathrooms = Column(Integer(), nullable=False, default=0)
    max_guest = Column(Integer(), nullable=False, default=0)
    price_by_night = Column(Integer(), nullable=False, default=0)
    latitude = Column(Float(), nullable=True)
    longitude = Column(Float(), nullable=True)
    amenity_ids = []
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref='place',
                              cascade='all, delete-orphan')
    else:
        @property
        def reviews(self):
            """Attribute for FileStorage"""
            reviewList = []
            for obj in models.storage.all(Review).values():
                if obj.place_id == self.id:
                    reviewList.append(obj)
            return reviewList

        place_amenity = Table('place_amenity',
                              Column('place_id', String(60),
                                     ForeignKey('places.id'), nullable=False),
                              Column('amenity_id', String(60),
                                     ForeignKey('amenities.id'),
                                     nullable=False),
                              )
