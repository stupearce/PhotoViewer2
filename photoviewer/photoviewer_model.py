import os
import sys
import uuid
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import inspect
import logging
 
Base = declarative_base()
 
class Photo(Base):
    __tablename__ = 'photo'
    id = Column(Integer, primary_key=True)
    rotation = Column(Integer)
    label = Column(String(250), nullable=False)
#    pathname =Column(String(255))
    path =""
    def __init__(self, id, path, label, rotation, transition, duration):
        self.id = uuid.uuid4()
        self.label = label
        self.rotation = rotation
        self.path = path
 
    def __str__(self):
        logging.info(inspect.getmembers(self))
        return "id:'{0}' label:'{1}' rotation:'{2}' path:'{3}'".format(self.id,self.label,self.rotation,self.path)

class Music():
    label = ""
    path = ""
    def __init__(self, path, label):
        self.id = uuid.uuid4()
        self.label = label
        self.path = path
 
    def __str__(self):
        logging.info(inspect.getmembers(self))
        return "id:'{0}' label:'{1}' path:'{3}'".format(self.id,self.label,self.path)

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///pv.db')
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)