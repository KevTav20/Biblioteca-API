#Created on Sat May 04 2024 at 1:15:58 by Kevin Jonathan Tavera Perez

#File: libro.py

#Copyright (c) 2024 company

from sqlalchemy import Column, Integer, String
from config.database import Base

class Libro(Base):
    __tablename__ = 'libros'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    year = Column(Integer)
    category = Column(String)
    num_pages = Column(Integer)
    image = Column(String)
    
 