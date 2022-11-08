from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, APIRouter, Query
from sqlalchemy.orm import Session

import functions.usuario_func  as usuario_func 
import functions.vendedor_func as vendedor_func 

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
    db_User = usuario_func.get_usuario_codUser(db, usuario.codUser)
    if db_User:
        raise HTTPException(status_code=400, detail="user already registered")
    return usuario_func.post_usuario(db, usuario)


@router_usuario.get("/", response_model=List[schemas.UsuarioVend])
def read_usuario(skip: Optional[int] = None, limit: Optional[int] = None, filter: list[str] | None = Query(None),  db: Session = Depends(get_db)):
    db_User = usuario_func.get_usuario(db, skip, limit, filter)
    return db_User


# @router_usuario.get("/", response_model=List[schemas.Usuario])
# def read_usuario_id(id: Optional[int] = None, emailUsuario: Optional[str] = None, idVendedor: Optional[int] = None, skip: Optional[int] = None, limit: Optional[int] = None, filter: list[str] | None = Query(None), db: Session = Depends(get_db)):
#     if id and emailUsuario and idVendedor:
#         db_Vend = vendedor_func.get_vendedor_idVendedor(db, idVendedor)
#         # if db_Vend and db_Vend.id == id:
#         db_User = usuario_func.get_usuario_id_emailUsuario(db, id, emailUsuario) if db_Vend and db_Vend[0].id == id else []
#         # else:
#         #     db_User = []
#     elif id and emailUsuario and not idVendedor:  
#         db_User = usuario_func.get_usuario_id_emailUsuario(db, id, emailUsuario)
#     elif id and not emailUsuario and not idVendedor:
#         db_User = usuario_func.get_usuario_id(db, id)
#     elif emailUsuario and not id and not idVendedor:
#         db_User = usuario_func.get_usuario_emailUsuario(db, emailUsuario)
#     elif idVendedor and not emailUsuario and not id:
#         db_Vend = vendedor_func.get_vendedor_idVendedor(db, idVendedor)
#         db_User = usuario_func.get_usuario_id(db, db_Vend[0].id)  if db_Vend else []
#     elif not emailUsuario and not id and not idVendedor:
#         db_User = usuario_func.get_usuario(db, skip, limit, filter)
   
#     return db_User
 

@router_usuario.put("/{id}", response_model=schemas.Usuario)
def update_usuario(id: int , usuario: schemas.Usuario, db: Session = Depends(get_db)):
    db_User = usuario_func.get_usuario_id(db, id)
    if not db_User:
        raise HTTPException(status_code=400, detail="register not exist")
    return usuario_func.put_usuario_id(db, id, usuario)


@router_usuario.delete("/{id}", response_model=schemas.Usuario)
def delete_usuario(id: int, db: Session = Depends(get_db)):
   db_User = usuario_func.get_usuario_id(db, id)
   if not db_User:
      raise HTTPException(status_code=400, detail="register not exist")
   return usuario_func.delete_usuario_id(db, id)