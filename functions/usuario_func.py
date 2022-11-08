from typing import Optional
from sqlalchemy.orm import Session
from fastapi import Query
from sqlalchemy.sql import text
import models, schemas
import functions.vendedor_func as vendedor_func 


def post_usuario(db: Session, usuario: schemas.Usuario):
    db_usuario = models.Usuario(codUser = usuario.codUser, nome = usuario.nome,  email = usuario.email, senha = usuario.senha.encode(), adm = usuario.adm, ativo = usuario.ativo)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    # if db_usuario.adm == 1:
    #     vendedor_func.post_vendedor(db, db_usuario.codUser, db_usuario.id)
    return db_usuario
     

def get_usuario(db: Session, skip: Optional[int] = None, limit: Optional[int] = None, filter: list[str] | None = Query(None) ):
    order = ','.join([str(i) for i in filter]) if filter else 'nome'
    return db.query(models.Usuario).order_by(text(order)).offset(skip).limit(limit).all()


def get_usuario_email(db: Session, email: str):
    return db.query(models.Usuario).filter(models.Usuario.email == email).all()


def get_usuario_id(db: Session, id: str):
    return db.query(models.Usuario).filter(models.Usuario.id == id).all()


def get_usuario_codUser(db: Session, codUser: str):
    return db.query(models.Usuario).filter(models.Usuario.codUser == codUser).all()


def get_usuario_id_email(db: Session, id: str, email: str):
    return db.query(models.Usuario).filter(models.Usuario.id == id, models.Usuario.email == email).all()
    

def put_usuario_id(db: Session, id: int, usuario: schemas.Usuario):
    db_usuario =  db.query(models.Usuario).filter(models.Usuario.id == id).first()

    db_usuario.codUser = usuario.codUser
    db_usuario.nome =  usuario.nome
    db_usuario.email =  usuario.email
    db_usuario.senha =  usuario.senha.encode() or db_usuario.senha.encode()
    db_usuario.ativo =  usuario.ativo
    db_usuario.adm =  usuario.adm

    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


def delete_usuario_id(db: Session, id: int):
    db_usuario =  db.query(models.Usuario).filter(models.Usuario.id == id).first()
    db.delete(db_usuario)
    db.commit()
    return db_usuario