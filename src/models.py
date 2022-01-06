import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    username = Column(String(200), unique=True)
    password = Column(String(200))
    state = Column(String(200))
    favorites = relationship("Favoritos")
  

class UsersGroup(Base):
    __tablename__ = 'users_group'
    user_id = Column(Integer, primary_key=True)
    user_username = Column(String(200))
    user_state = Column(String(200))

class UsersRoles(Base):
    __tablename__ = 'users_roles'
    roles_id = Column(Integer, primary_key=True)
    user_id = Column(Integer,primary_key=True )
   

class Roles(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    rol = Column(String(200))

class Favoritos(Base):
    __tablename__ = 'favoritos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    users_id = Column(Integer, ForeignKey('users.id'))
    planets_id = Column(Integer, unique=True)
    characters_id = Column(Integer, unique=True)
    planet_name = Column(String, primary_key=True)
    character_name = Column(String(200), primary_key=True)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    description = Column(Text(1000))
    state = (String(200))

class Characters(Base):
    __tablename__ = 'characters' 
    id = Column(Integer, primary_key=True)
    name = Column(String(200), unique=True)
    age = Column(Integer)
    rol = Column (String(200))
    descrption = (Text(1000))
    state = (String(200))



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')