#!/usr/bin/python3
""" Place Module for HBNB project """
import models
import os
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place",
                               cascade="all, delete")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 backref="place_amenities")

    else:
        @property
        def reviews(self):
            """
            getter attribute reviews that returns the list of Review
            instances with place_id equals to the current Place.id
            """
            objs = models.storage.all(type(self))
            return [v for k, v in objs.items() if v.place_id == self.id]

        @property
        def amenities(self):
            """
            Getter attribute amenities that returns the list of
            Amenity instances based on the attribute amenity_ids that
            contains all Amenity.id linked to the Place
            """
            objs = models.storage.all(Amenity)
            return [v for k, v in objs.items() if v.amenities_id
                    in self.amenity_ids]

        @amenities.setter
        def amenities(self, amenities_obj):
            """
            Setter attribute amenities that handles append method for
            adding an Amenity.id to the attribute amenity_ids
            """
            if type(amenities_obj).__name__ == "Amenity":
                self.amenity_ids.append(amenities_obj.id)
