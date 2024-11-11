#Created on Sat May 04 2024 at 10:13:19 by Kevin Jonathan Tavera Perez

#File: user.py

#Copyright (c) 2024 company

from fastapi import APIRouter
from utils.jwt_manager import create_token
from fastapi.responses import JSONResponse
from schemas.user import Usuario
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from utils.jwt_manager import create_token
from config.database import SessionLocal

from models.user import Usuario as UserModel

user_router = APIRouter()


@user_router.post('/login', tags=['auth'])
def login(user_data: Usuario):
    db = SessionLocal()
    try:
        user = db.query(UserModel).filter(UserModel.email == user_data.email).first()
        if not user or user.password != user_data.password:
            raise HTTPException(status_code=401, detail="Correo electrónico o contraseña incorrectos")

        token = create_token({"email": user.email})
        return JSONResponse(status_code=200, content={"token": token})
    finally:
        db.close()
