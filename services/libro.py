#Created on Sat May 04 2024 at 1:54:00 by Kevin Jonathan Tavera Perez

#File: libro.py

#Copyright (c) 2024 company

from models.libro import Libro as LibroModel
from schemas.libro import Libro
from models.categoria import Categoria as CategoriaModel
from schemas.categoria import Categoria

class LibroService:
    def __init__(self, db) -> None:
        self.db = db

    # Métodos relacionados con libros
    def get_all_libros(self):
        result = self.db.query(LibroModel).all()
        return result
    
    def get_libro_by_id(self, id):
        result = self.db.query(LibroModel).filter(LibroModel.id == id).first()
        return result
    
    def get_libros_by_category(self, category):
        result = self.db.query(LibroModel).filter(LibroModel.category == category).all()
        return result
    
    def create_libro(self, category: str, libro: Libro):
            # Verificar si la categoría existe en la tabla de categorías
            categoria_existente = self.db.query(CategoriaModel).filter(CategoriaModel.name == category).first()
            if categoria_existente:
                # Convertir el objeto Categoria a su nombre como string
                categoria_nombre = categoria_existente.name
                
                # Crear un nuevo libro con los datos proporcionados
                new_libro = LibroModel(
                    title=libro.title,
                    author=libro.author,
                    year=libro.year,
                    category=categoria_nombre,  # Asignar el nombre de la categoría como string
                    num_pages=libro.num_pages,
                    image = libro.image
                )
                self.db.add(new_libro)
                self.db.commit()
                return "Libro creado exitosamente."
            else:
                return "No se puede crear el libro porque la categoría no existe"
    
    def update_libro(self, id: int, data: Libro):
        libro = self.db.query(LibroModel).filter(LibroModel.id == id).first()
        if libro:
            # Buscamos la categoría por su nombre en los datos del libro
            categoria_existente = self.db.query(CategoriaModel).filter(CategoriaModel.name == data.category).first()
            if categoria_existente:
                libro.title = data.title
                libro.author = data.author
                libro.year = data.year
                libro.category = data.category  # Asignar el nombre de la categoría
                libro.num_pages = data.num_pages
                libro.image = data.image
                self.db.commit()
                return "Libro modificado exitosamente."
            else:
                return "No se puede modificar el libro porque la categoría no existe."
        else:
            return "No se puede encontrar el libro especificado."

        
    def delete_libro(self, id: int):
        libro = self.db.query(LibroModel).filter(LibroModel.id == id).first()
        self.db.delete(libro)
        self.db.commit()
        return

    # Métodos relacionados con categorías

    def get_all_categorias(self):
        result = self.db.query(CategoriaModel).all()
        return result
    
    def get_categoria_by_id(self, id: int):
        categoria = self.db.query(CategoriaModel).filter(CategoriaModel.id == id).first()
        return categoria
    
    def create_categoria(self, categoria: Categoria):
        new_categoria = CategoriaModel(**categoria.dict())
        self.db.add(new_categoria)
        self.db.commit()
        return
    
    # Método
    def update_categoria(self, category: str, nueva_categoria: str):
        # Buscar la categoría por su nombre
        categoria_db = self.db.query(CategoriaModel).filter(CategoriaModel.name == category).first()
        if categoria_db:
            # Actualizar la categoría en CategoriaModel
            categoria_db.name = nueva_categoria
            categoria_db.image = nueva_categoria
            self.db.commit()

            # Actualizar la categoría en los libros que la tienen
            libros_con_categoria = self.db.query(LibroModel).filter(LibroModel.category == category).all()
            for libro in libros_con_categoria:
                libro.category = nueva_categoria
            self.db.commit()
            return "Categoría actualizada exitosamente."
        else:
            return "No se puede encontrar la categoría especificada."

    
    
    def delete_categoria(self, category: str):
        # Buscar la categoría por su nombre
        buscar_categoria = self.db.query(CategoriaModel).filter(CategoriaModel.name == category).first()
        
        # Verificar si hay libros asociados a la categoría
        encontrar_libros_con_categoria = self.db.query(LibroModel).filter(LibroModel.category == category).first()
        
        if not encontrar_libros_con_categoria:
            # Si no hay libros asociados, eliminar la categoría
            self.db.delete(buscar_categoria)  # Eliminar el objeto de categoría
            self.db.commit()
            return "Categoría eliminada exitosamente."
        else:
            return "No se puede eliminar la categoría porque existen libros asociados a ella."
