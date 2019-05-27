from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, Date, Time

from sys import path

path.append('../')
from database_layer.database import *
from hospital.user import User

class Doctor(Base):
    __tablename__ = 'doctor'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    title = Column(String)
    user = relationship(User, backref='doctor')
    
if __name__ == '__main__':
    Base.metadata.create_all(engine)
    session.commit()