#Created on Sat May 04 2024 at 1:16:38 by Kevin Jonathan Tavera Perez

#File: jwt_bearer.py

#Copyright (c) 2024 company

from utils.jwt_manager import validate_token
from fastapi.security import HTTPBearer
from fastapi import HTTPException, Request
from utils.jwt_manager import validate_token
from fastapi.security import HTTPBearer
from fastapi import HTTPException, Request
from config.database import SessionLocal as Session
from models.user import Usuario as UserModel


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        email = data.get('email')  
        if not email:
            raise HTTPException(status_code=403, detail='No se proporcionó el correo electrónico en el token JWT')
        
        # Verificar si el usuario existe en la base de datos
        db = Session()
        user = db.query(UserModel).filter(UserModel.email == email).first()
        db.close()
        
        if not user:
            raise HTTPException(status_code=403, detail='Usuario no encontrado en la base de datos')
        return user
