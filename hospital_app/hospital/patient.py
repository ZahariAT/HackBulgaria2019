from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, Date, Time

from sys import path

path.append('../')
from database_layer.database import *
from hospital.user import User

class Patient(Base):
    __tablename__ = 'patient'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    illness = Column(String)
    user = relationship(User, backref='patient')
    
if __name__ == '__main__':
    Base.metadata.create_all(engine)
    session.commit()