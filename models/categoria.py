#Created on Sat May 04 2024 at 2:53:33 by Kevin Jonathan Tavera Perez

#File: categoria.py

#Copyright (c) 2024 company

from config.database import Base;
from sqlalchemy import Column, Integer, String;

class Categoria(Base):
    __tablename__ = 'categorias'

    id = Column(Integer, primary_key = True);
    name = Column(String);
    image = Column(String);