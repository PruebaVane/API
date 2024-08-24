from BBDD.database import Base
from sqlalchemy import Column, Integer, String, Float

class Service(Base):
    __tablename__ = 'servicios'
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    categoria = Column(String)
    descripcion = Column(String)
    precio = Column(Float)
    