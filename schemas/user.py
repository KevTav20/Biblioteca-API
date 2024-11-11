#Created on Sat May 04 2024 at 2:22:50 by Kevin Jonathan Tavera Perez

#File: user.py

#Copyright (c) 2024 company

from pydantic import BaseModel, Field

class Usuario(BaseModel):
    email: str
    password: str

    email: str = Field(default = "kevin_tavera11@yahoo.com");
    password: str = Field(default = "1234");

    class Config:
        schema_extra = {
            'example': {
                'email': 'kevin_tavera11@yahoo.com',
                'password': '1234',
            }
        }