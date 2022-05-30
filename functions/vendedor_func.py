from typing import Optional
from sqlalchemy.orm import Session
from fastapi import Query
from sqlalchemy.sql import text
import models, schemas


# idVendedor	int
# IdErpUser	varchar
# idUsuario	int

def post_vendedor(db: Session, IdErpUser: str, idUsuario: int):
    db_vendedor = models.Vendedor(IdErpUser = IdErpUser, idUsuario = idUsuario)
    db.add(db_vendedor)
    db.commit()
    db.refresh(db_vendedor)
    return db_vendedor



def get_vendedor(db: Session, skip: Optional[int] = None, limit: Optional[int] = None, filter: list[str] | None = Query(None)):
    order = ','.join([str(i) for i in filter]) if filter else 'idVendedor'
    return db.query(models.Vendedor).order_by(text(order)).offset(skip).limit(limit).all()


def get_vendedor_idVendedor(db: Session, idVendedor: int):
    return db.query(models.Vendedor).filter(models.Vendedor.idVendedor == idVendedor).all()


def get_vendedor_idUsuario(db: Session, idUsuario: int):
    return db.query(models.Vendedor).filter(models.Vendedor.idUsuario == idUsuario).first()