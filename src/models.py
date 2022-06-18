import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuario (Base):
    __tablename__ = 'Usuario'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Favoritos (Base):
    __tablename__ = 'Favoritos'
    id = Column(Integer, primary_key=True)
    id_user = Column(String(250))
    items = Column(Integer, ForeignKey("Usuario.id"))
    

class Personajes (Base):
    __tablename__ = 'Personajes'
    id = Column(Integer, primary_key=True)
    name_pers = Column(String(250))
    year = Column(Integer, ForeignKey("Favoritos.id"))

class Planets (Base):
    __tablename__ = 'Planets'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    climate = Column(String, ForeignKey("Personajes.id"))

class Vehiculos (Base):
    __tablename__ = 'Vehiculos'
    id = Column(Integer, primary_key=True)
    name_Vh = Column(String(40))
    model = Column(String, ForeignKey("Personajes.id"))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')