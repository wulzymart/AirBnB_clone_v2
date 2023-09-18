#!/usr/bin/python3

"""
This module contains the database storage class that helps to store date
in a relational database
"""
import sys
from base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBStorage():
    """
    This class allows for the storage of our data in a relational database
    """
    __engine = None
    __session = None
    def __init__(self):
        """initialize a new database session"""
        user, pword, host, db, env = (
            sys.getenv(HBNB_MYSQL_USER),
            sys.getenv(HBNB_MYSQL_PWD),
            sys.getenv(HBNB_MYSQL_HOST),
            sys.getenv(HBNB_MYSQL_DB),
            sys.getenv(HBNB_ENV)
        )
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"\
                                      .format(user, pword, host, db),
                                      pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
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
            for objs in self.__session.query(User, State, City, Amenity, Place,
                                             Amenity).all():
                for obj in objs:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    result[key] = obj
        return result

    def new(self, obj):
        """
        Add the object to the current database session
        """
        self.__session.add(obj)

    def save(self, obj):
        """
        Commit all changes of the current database session
        """
        self.__session.commit(obj)
