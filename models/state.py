#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship(
            "City",
            cascade="all,delete-orphan",
            backref=backref("state", cascade="all"),
            passive_deletes=True,
            single_parent=True)

    if getenv("HBNB_TYPE_STORAGE") == "fs":
        @property
        def cities(self):
            """returns list of City instances with state_id"""
            from models import storage
            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
            """
            return {k: v for k, v in storage.all().items()
                    if v.state_id == self.id}
            """
