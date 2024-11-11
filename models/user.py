#Created on Sun May 05 2024 at 22:11:16 by Kevin Jonathan Tavera Perez

#File: user.py

#Copyright (c) 2024 company

from sqlalchemy import Column, Integer, String
from config.database import Base

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)

