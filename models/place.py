#!/usr/bin/python3
""" Place Module for HBNB project """
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
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
        place_amenity = Table('place_amenity', Base.metadata,
                              Column('place_id', String(60),
                                     ForeignKey('places.id'), nullable=False),
                              Column('amenity_id', String(60),
                                     ForeignKey('amenities.id'),
                                     nullable=False),
                              )
        amenities = relationship("Amenities",
                                 secondary="place_amenities", viewonly=False)
                                
    else:
        @property
        def reviews(self):
            """Property Getter for FileStorage"""
            reviewList = []
            for obj in models.storage.all(Review).values():
                if obj.place_id == self.id:
                    reviewList.append(obj)
            return reviewList
        
        @property
        def amenities(self):
            """Amenity getter for FileStorage"""
            amenitiesList = []
            for obj in models.strorage.all(Amenity).values():
                if obj.place_id == self.id:
                    amenitiesList.append(obj)
                return amenitiesList

        @amenities.setter
        def amenities(self, obj=None):
            """Amenity setter for File Storage"""
            if type(obj) == Amenity:
                self.amenity_ids.append(obj)
