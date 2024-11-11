#Created on Sat May 04 2024 at 1:55:18 by Kevin Jonathan Tavera Perez

#File: libro.py

#Copyright (c) 2024 company

from pydantic import BaseModel, Field;

class Libro(BaseModel):
    title: str = Field(default = "The Witcher");
    author: str = Field(default = "Andrzej Sapkowski");
    year: int = Field(default=2024, le=2024)
    category: str = Field(default = "Fantasy");
    num_pages: int = Field(default = 300);
    image: str = Field(default = "https://m.media-amazon.com/images/M/MV5BMDEwOWVlY2EtMWI0ZC00OWVmLWJmZGItYTk3YjYzN2Y0YmFkXkEyXkFqcGdeQXVyMTUzMTg2ODkz._V1_.jpg");

    class Config:
        schema_extra = {
            'example': {
                'title': 'The Witcher',
                'author': 'Andrzej Sapkowski',
                'year': 2024,
                'category': 'Fansasy',
                'num_pages': 300,
                'image': "https://m.media-amazon.com/images/M/MV5BMDEwOWVlY2EtMWI0ZC00OWVmLWJmZGItYTk3YjYzN2Y0YmFkXkEyXkFqcGdeQXVyMTUzMTg2ODkz._V1_.jpg"
            }
        }