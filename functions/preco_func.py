from typing import Optional
from sqlalchemy.orm import Session

import models, schemas


def get_preco(db: Session, skip: Optional[int] = None, limit: Optional[int] = None, filter: Optional[str]= "codProduto" ):
    return db.query(models.Preco).order_by(filter).offset(skip).limit(limit).all()

def get_preco_codProduto(db: Session, codProduto: str):
    return db.query(models.Preco).filter(models.Preco.codProduto == codProduto).all()


# def get_trasportadora_idErpTransp(db: Session, idErpTransp: str):
#     return db.query(models.Transportadora).filter(models.Transportadora.idErpTransp == idErpTransp).first()


# def get_trasportadora(db: Session, skip: Optional[int] = None, limit: Optional[int] = None, filter: Optional[str]= "nmTransp" ):
#     return db.query(models.Transportadora).order_by(filter).offset(skip).limit(limit).all()