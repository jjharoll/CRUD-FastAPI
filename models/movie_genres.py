from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class MoviesGenres(Base):
    
    __tablename__ = "movie_genres"
    
    mov_id = Column(Integer,primary_key = True)
    gen_id = Column(Integer, ForeignKey("genres.id"))