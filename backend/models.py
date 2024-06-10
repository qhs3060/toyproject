from sqlalchemy import Column, Integer, Float
from sqlalchemy.ext.declarative import declared_attr
from db import Base

class BaseModel(Base):
    __abstract__ = True

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class CaliforniaHouse(BaseModel):
    __tablename__ = "california_house"
    
    id = Column(Integer, primary_key=True, index=True)
    longitude = Column(Float)
    latitude = Column(Float)
    houseage = Column(Float)
    averooms = Column(Float)
    avebedrms = Column(Float)
    population = Column(Float)
    aveoccup = Column(Float)
    medinc = Column(Float)
    medhouseval = Column(Float)

class Iris(BaseModel):
    __tablename__ = "iris"
    
    id = Column(Integer, primary_key=True, index=True)
    sepal_length = Column(Float)
    sepal_width = Column(Float)
    petal_length = Column(Float)
    petal_width = Column(Float)
    target = Column(Integer)
