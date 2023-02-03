from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Direction(Base):

    __tablename__ = "direction"
    
    dir_id = Column(Integer,primary_key = True)
    mov_id = Column(Integer, ForeignKey("mov.id"))
