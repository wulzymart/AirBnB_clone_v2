#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    @cities.getter
    def cities(self):
        """
        Getter attribute cities that returns the list of City
        instances with state_id equals to the current
        """
        return [city for city in cities if city.state_id == State.id]
