from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from config.database import engine, Base, SessionLocal
from middlewares.error_handler import ErrorHandler
from routers.libro import libro_router, categoria_router
from routers.user import user_router
from fastapi.middleware.cors import CORSMiddleware
from models.user import Usuario as UserModel

app = FastAPI()
app.title = "Biblioteca Digital"
app.version = "2.0"
app.description = "API para la Biblioteca Digital"

Base.metadata.create_all(bind=engine)

# # Dependencia para obtener la sesión
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
# # Crear instancias de usuarios y confirmar los cambios
# def create_users(db: Session):
#     user1 = UserModel(email="kevin_tavera11@yahoo.com", password="1234")
#     user2 = UserModel(email="user2@example.com", password="1234")
#     user3 = UserModel(email="alan@gmail.com", password="1234")
#
#     db.add(user1)
#     db.add(user2)
#     db.add(user3)
#     db.commit()
#
# # Inicialización de usuarios al iniciar la aplicación
# with SessionLocal() as db:
#     create_users(db)

app.include_router(user_router)
app.include_router(categoria_router)
app.include_router(libro_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)