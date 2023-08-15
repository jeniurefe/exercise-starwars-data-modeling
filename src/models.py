import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class FavoritesPerson(Base):
    __tablename__ = 'favoritesperson'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    person_id = Column(Integer, ForeignKey('person.id'))
    rating = Column(Integer, nullable = True) 

class FavoritesPlanet(Base):
    __tablename__ = 'favoritePlanet'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    person_id = Column(Integer, ForeignKey('planet.id'))

class FavoritesVehicles(Base):
    __tablename__ = 'favoritesvehicles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    person_id = Column(Integer, ForeignKey('vehicles.id')) 


class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(20), nullable=False)
    eyes_color = Column(String(20), nullable = True) #nullable = True es que se puede dejar vacía la información
    age = Column(Integer, nullable = False)
    birth_year = Column(String(40), nullable=False)
    hair_color =Column(String(40), nullable=True)
    height =Column(Integer, nullable=False)
    mass =Column(Integer, nullable=False)
    skin_color =Column(String(50), nullable=True)
    homewold =Column(String(200), nullable=False)
    films =Column(String(250), nullable=False)
    species =Column(String(200), nullable=False)
    starships =Column(String(100), nullable=False)
    vehicles =Column(String(200), nullable=False)
    url =Column(String(200), nullable=False)
    created = Column(String(100), nullable=False)
    edited =Column(String(100), nullable=False)
    favorites_person = relationship(FavoritesPerson, backref='person', lazy=True) #backref es una autoreferencia


class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    gravity = Column(Integer, nullable = False)
    population = Column(Integer, nullable=False)
    climate = Column(String(100), nullable=False)
    terrain = Column(String(100), nullable=False)
    surface_water = Column(Integer, nullable=False)
    residents = Column(String(250), nullable=False)
    films = Column(String(250), nullable=False)
    url = Column(String(200), nullable=False)
    created = Column(String(100), nullable=False)
    edited = Column(String(100), nullable=False)
    favorites_planet = relationship(FavoritesPlanet, backref='planet', lazy=True)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(100), nullable=False)
    vehicle_class = Column(String(100), nullable=False)
    manufacturer = Column(String(200), nullable=False)
    lenght = Column(String(50), nullable=False)
    cost_in_credits = Column(String(250), nullable=False)
    crew = Column(Integer, nullable=False)
    passengers = Column(Integer, nullable=False)
    max_atmosphering_speed = Column(String(250), nullable=True)
    cargo_capacity = Column(String(100), nullable=False)
    consumables = Column(String(100), nullable=False)
    films = Column(String(250), nullable=False)
    pilots = Column(String(10), nullable=False)
    url = Column(String(200), nullable=False)
    created = Column(String(100), nullable=False)
    edirted = Column(String(100), nullable=False)
    favorites_vehicles = relationship(FavoritesVehicles, backref='vehicles', lazy=True)


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False)
    age = Column(Integer, nullable = False)
    favorites_vehicle = relationship(FavoritesPerson, backref='user', lazy=True)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
