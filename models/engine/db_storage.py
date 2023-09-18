#!/usr/bin/python3

"""
This module contains the database storage class that helps to store date
in a relational database
"""
import os
from sqlalchemy import create_engine
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage():
    """
    This class allows for the storage of our data in a relational database
    """
    __engine = None
    __session = None

    def __init__(self):
        """initialize a new database session"""
        user, pword, host, db, env = (
            os.getenv("HBNB_MYSQL_USER"),
            os.getenv("HBNB_MYSQL_PWD"),
            os.getenv("HBNB_MYSQL_HOST"),
            os.getenv("HBNB_MYSQL_DB"),
            os.getenv("HBNB_ENV")
        )
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(user, pword, host, db),
                                      pool_pre_ping=True)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        if env == "test":
            Base.metadata.drop_all()

    def all(self, cls=None):
        """
        Query on the current database session (self.__session) all objects
        depending of the class name (argument cls)
        """
        result = {}
        if cls:
            for obj in self.__session.query(cls).all():
                key = "{}.{}".format(cls.__name__, obj.id)
                result[key] = obj
        else:
            classes = [User, State, City, Amenity, Place, Amenity]
            for cls in classes:
                for obj in self.__session.query(cls).all():
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    result[key] = obj
        return result

    def new(self, obj):
        """
        Add the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session obj if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        quit and restart a session
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(self.__engine, expire_on_commit=False)
        self.__session = Session()
