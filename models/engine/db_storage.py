from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.state import State
from models.city import City

class DBStorage:
    """ Database storage engine """

    __engine = None
    __session = None

    def __init__(self):
        """ Initialize DBStorage """
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@{host}/{db}',
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ Query objects from database """
        session = self.__session
        objs = {}
        if cls:
            objs = session.query(cls).all()
        else:
            classes = [State, City]  # Add other classes as needed
            for cls in classes:
                objs.update({obj.id: obj for obj in session.query(cls).all()})
        return objs

    def new(self, obj):
        """ Add object to current database session """
        if obj:
            self.__session.add(obj)

    def save(self):
        """ Commit changes to current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete object from current database session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Create all tables in the database and create a new session """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))()
