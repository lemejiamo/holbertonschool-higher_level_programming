#!/usr/bin/python3
""" state model"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """ Class for cities table"""

    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True,
                unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
