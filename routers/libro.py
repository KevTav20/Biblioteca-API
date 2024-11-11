#Created on Sat May 04 2024 at 1:18:09 by Kevin Jonathan Tavera Perez

#File: libro.py

#Copyright (c) 2024 company

from fastapi import Path, Query, Depends, APIRouter, HTTPException;
from fastapi.responses import HTMLResponse, JSONResponse;
from typing import List
from config.database import SessionLocal as Session
from middlewares.jwt_bearer import JWTBearer;
from models.libro import Libro as LibroModel;
from fastapi.encoders import jsonable_encoder;
from models.categoria import Categoria as CategoriaModel;
from schemas.categoria import Categoria;
from services.libro import LibroService;
from schemas.libro import Libro;

libro_router = APIRouter();
categoria_router = APIRouter();

# Endpoints relacionados con libros

@libro_router.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')

@libro_router.get('/libros/', tags = ['Libros'], response_model=List[Libro], status_code=200)
def obtener_libros() -> List[Libro]:
    db = Session()
    result = LibroService(db).get_all_libros()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@libro_router.get('/libros/{id}', tags=['Libros'], response_model = Libro,  status_code=200)
def obtener_libro_por_id(id: int = Path(ge = 1, le = 200)) -> Libro:
    db = Session()
    result = LibroService(db).get_libro_by_id(id)
    if not result:
        return JSONResponse(status_code=400, content={"message": "Libro no encontrado"})
    return JSONResponse(status_code = 200, content = jsonable_encoder(result))

@libro_router.get('/libros', tags=['Libros'], response_model=List[Libro])
def obtener_libros_por_categoria(category: str = Query(min_length=5, max_length=20)) -> List[Libro]:
    db = Session()
    result = LibroService(db).get_libros_by_category(category)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@libro_router.post('/libros/', tags=['Libros'], response_model=dict, status_code=201)
def crear_libro(category: str, libro: Libro) -> dict:
    db = Session()
    mensaje = LibroService(db).create_libro(category, libro)  # Capturar el mensaje retornado por el servicio
    return JSONResponse(status_code=201, content={'message': mensaje})

@libro_router.put('/libros/{id}', tags=['Libros'], response_model=dict, status_code=200)
def actualizar_libro(id: int, libro: Libro) -> dict:
    db = Session()
    result = LibroService(db).get_libro_by_id(id)
    if not result:
        return JSONResponse(status_code=400, content={'message': 'Libro no encontrado'})
    
    mensaje = LibroService(db).update_libro(id, libro)
    if mensaje == "Libro modificado exitosamente.":
        return JSONResponse(status_code=200, content={"message": mensaje})
    else:
        return JSONResponse(status_code=400, content={"message": mensaje})

@libro_router.delete('/libros/{id}', tags=['Libros'], response_model=dict, status_code=200)
def eliminar_libro(id: int) -> dict:
    db = Session()
    result: LibroModel = db.query(LibroModel).filter(LibroModel.id == id).first()
    if not result:
        return JSONResponse(status_code=400, content={'message': 'Libro no Encontrado'})
    LibroService(db).delete_libro(id)
    return JSONResponse(status_code=200, content={'message': 'Libro eliminado'})

# Endpoints relacionados con categorías
@categoria_router.get('/categorias', tags=['Categorias'], response_model=List[Categoria])
def obtener_categorias() -> List[Categoria]:
    db = Session()
    result = LibroService(db).get_all_categorias()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@categoria_router.post('/categorias/{id}', tags=['Categorias'], response_model=dict)
def crear_categoria(categoria: Categoria) -> dict:
    db = Session()
    LibroService(db).create_categoria(categoria)
    return JSONResponse(status_code=201, content={'message': 'Categoria Creada'})

@categoria_router.put('/categorias/{category}', tags=['Categorias'], response_model=dict)
def actualizar_categoria(category: str, categoria: Categoria) -> dict:
    db = Session()
    result = db.query(CategoriaModel).filter(CategoriaModel.name == category).first()
    if not result:
        return JSONResponse(status_code=400, content={'message': 'Categoría no encontrada'})
    LibroService(db).update_categoria(category, categoria.name)
    return JSONResponse(status_code=200, content={'message': 'Categoría Actualizada'})

@categoria_router.delete('/categorias/{category}', tags=['Categorias'], response_model=dict)
def eliminar_categoria(category: str) -> dict:
    db = Session()
    result = db.query(CategoriaModel).filter(CategoriaModel.name == category).first()
    if not result:
        return JSONResponse(status_code=400, content={'message': 'Categoría no encontrada'})
    
    mensaje = LibroService(db).delete_categoria(category)
    return JSONResponse(status_code=200, content={'message': mensaje})
