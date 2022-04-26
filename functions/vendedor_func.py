from typing import Optional
from sqlalchemy.orm import Session

import models, schemas


def get_vendedor(db: Session, skip: Optional[int] = None, limit: Optional[int] = None, filter: Optional[str]= "idVendedor" ):
    return db.query(models.Vendedor).order_by(filter).offset(skip).limit(limit).all()


def get_vendedor_idVendedor(db: Session, idVendedor: int):
    return db.query(models.Vendedor).filter(models.Vendedor.idVendedor == idVendedor).first()


def get_vendedor_idUsuario(db: Session, idUsuario: int):
    return db.query(models.Vendedor).filter(models.Vendedor.idUsuario == idUsuario).first()