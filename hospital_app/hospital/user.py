from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, Date, Time

from sys import path

path.append('../')
from database_layer.database import *


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True) #TODO nullable=False
    password = Column(String)
    status = Column(String)

    def __str__(self):
        return self.username + ' ' + self.status

    def __repr__(self):
        return str(self)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    session.commit()