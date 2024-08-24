import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


sqliteName = 'sevicios.sqlite'
base_dir = os.path.dirname(os.path.realpath(__file__))
datebaseUrl = f'sqlite:///{os.path.join(base_dir, sqliteName)}'


engine = create_engine(datebaseUrl, echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()

#Esto es solo la creacion de la conexion de la BBDD


