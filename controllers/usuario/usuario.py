from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session

import functions.usuario_func  as usuario_func 
import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router_usuario = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router_usuario.post("/", response_model=schemas.Usuario)
def post_usuario(usuario: schemas.Usuario, db: Session = Depends(get_db)):
    db_User = usuario_func.get_usuario_idErpUser(db, usuario.idErpUser)
    if db_User:
        raise HTTPException(status_code=400, detail="user already registered")
    return usuario_func.post_usuario(db, usuario)


@router_usuario.get("/", response_model=List[schemas.Usuario])
def read_usuario(skip: Optional[int] = None, limit: Optional[int] = None, filter: Optional[str]= "nmUsuario",  db: Session = Depends(get_db)):
    db_User = usuario_func.get_usuario(db, skip, limit, filter)
    return db_User


@router_usuario.get("/{idUsuario}", response_model=schemas.Usuario)
def read_usuario_idUsuario(idUsuario: int , db: Session = Depends(get_db)):
    db_User = usuario_func.get_usuario_idUsuario(db, idUsuario)
    return db_User
 

@router_usuario.put("/{idUsuario}", response_model=schemas.Usuario)
def update_usuario(idUsuario: int , usuario: schemas.Usuario, db: Session = Depends(get_db)):
    db_User = usuario_func.get_usuario_idUsuario(db, idUsuario)
    if not db_User:
        raise HTTPException(status_code=400, detail="register not exist")
    return usuario_func.put_usuario_idUsuario(db, idUsuario, usuario)


@router_usuario.delete("/{idUsuario}", response_model=schemas.Usuario)
def delete_usuario(idUsuario: int, db: Session = Depends(get_db)):
   db_User = usuario_func.get_usuario_idUsuario(db, idUsuario)
   if not db_User:
      raise HTTPException(status_code=400, detail="register not exist")
   return usuario_func.delete_usuario_idUsuario(db, idUsuario)