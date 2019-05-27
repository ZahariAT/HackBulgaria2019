from sys import path

path.append('../')
from hospital.user import User
from database_layer.database import session
#   from utils.logger import Logger

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Gateway(metaclass=Singleton):
    #log = Logger()
    db = session