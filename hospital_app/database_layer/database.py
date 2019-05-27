from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine("sqlite:////home/zahari/Desktop/all_python/week11/hospital_app/utils/hospital.db")

session = sessionmaker(bind=engine)()

if __name__ == '__main__':
    Base.metadata.create_all(engine)

    session.commit()