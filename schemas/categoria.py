#Created on Sat May 04 2024 at 2:55:59 by Kevin Jonathan Tavera Perez

#File: categoria.py

#Copyright (c) 2024 company

from pydantic import BaseModel, Field;
from typing import Optional;

class Categoria(BaseModel):
    # id: Optional[int] = None;
    name: str = Field(default = "Fantasy", max_length = 20, min_length = 5);
    image: str = Field(default = "https://i0.wp.com/xn--oo-yjab.cl/wp-content/uploads/2020/06/oso-polar-definicion-genero-de-la-fantasia.jpg?fit=980%2C589&ssl=1");

    class Config:
        schema_extra = {
            'example': {
                'category': 'Fantasy',
                'image': 'https://i0.wp.com/xn--oo-yjab.cl/wp-content/uploads/2020/06/oso-polar-definicion-genero-de-la-fantasia.jpg?fit=980%2C589&ssl=1'
            }
        }