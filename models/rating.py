from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Rating(Base):
    
    __tablename__ = "rating"
    
    id = Column(Integer,primary_key = True, index=True)
    mov_id = Column(Integer, ForeignKey("mov.id"))
    rev_id = Column(Integer, ForeignKey("rev.id"))
    rev_stars = Column(Integer, ForeignKey("rev.stars"))
    num_o_ratings = Column(Integer, ForeignKey("num.o.ratings"))