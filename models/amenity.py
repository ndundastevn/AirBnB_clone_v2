#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models import storage_type
from sqlalchemy import Column, String


class Amenity(BaseModel):
    """
    Class represents amenity
    Inherits from ORM Base and links to amenities entity on db.

    Attributes:
    __tablename__ (str): table on db for amenities.
    name (sqlalchemy String): name.
    place_amenities (sqlalchemy relationship): relationship btn
    ammenty and place.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
