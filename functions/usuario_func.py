from typing import Optional
from sqlalchemy.orm import Session

import models, schemas


def post_usuario(db: Session, usuario: schemas.Usuario):
    db_usuario = models.Usuario(idErpUser = usuario.idErpUser, nmUsuario = usuario.nmUsuario, sobrenomeUsuario = usuario.sobrenomeUsuario, emailUsuario = usuario.emailUsuario, senhaUsuario = usuario.senhaUsuario, ativo = usuario.ativo, nivel = usuario.nivel)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


def get_usuario(db: Session, skip: Optional[int] = None, limit: Optional[int] = None, filter: Optional[str]= "nmUsuario" ):
    return db.query(models.Usuario).order_by(filter).offset(skip).limit(limit).all()


def get_usuario_emailUsuario(db: Session, emailUsuario: str):
    return db.query(models.Usuario).filter(models.Usuario.emailUsuario == emailUsuario).all()


def get_usuario_idUsuario(db: Session, idUsuario: str):
    return db.query(models.Usuario).filter(models.Usuario.idUsuario == idUsuario).all()


def get_usuario_idErpUser(db: Session, idErpUser: str):
    return db.query(models.Usuario).filter(models.Usuario.idErpUser == idErpUser).all()


def get_usuario_idUsuario_emailUsuario(db: Session, idUsuario: str, emailUsuario: str):
    return db.query(models.Usuario).filter(models.Usuario.idUsuario == idUsuario, models.Usuario.emailUsuario == emailUsuario).all()
    

def put_usuario_idUsuario(db: Session, idUsuario: int, usuario: schemas.Usuario):
    db_usuario =  db.query(models.Usuario).filter(models.Usuario.idUsuario == idUsuario).first()

    db_usuario.idErpUser = usuario.idErpUser
    db_usuario.nmUsuario =  usuario.nmUsuario
    db_usuario.sobrenomeUsuario =  usuario.sobrenomeUsuario
    db_usuario.emailUsuario =  usuario.emailUsuario
    db_usuario.senhaUsuario =  usuario.senhaUsuario
    db_usuario.ativo =  usuario.ativo
    db_usuario.nivel =  usuario.nivel

    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


def delete_usuario_idUsuario(db: Session, idUsuario: int):
    db_usuario =  db.query(models.Usuario).filter(models.Usuario.idUsuario == idUsuario).first()
    db.delete(db_usuario)
    db.commit()
    return db_usuario