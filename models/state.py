#!/usr/bin/python3
"""This is the state class"""
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from models.city import City
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """This is the class for State

    Attributes:
    __tablename__ (str): table States on db.
    name (sqlalchemy String): State.
    cities (sqlalchemy relationship): State-City relationship.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        """Get list of all City objects linked to state"""
        var = models.storage.all(City)
        lista = []
        for city in var.values():
            if city.state_id == self.id:
                lista.append(city)
        return lista
