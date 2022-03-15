from typing import Optional
from sqlalchemy.orm import Session

import models, schemas


def post_condpagamento(db: Session, condpagamento: schemas.CondPagamento):
    db_condpagamento = models.CondPagamento(idErpCondPag= condpagamento.idErpCondPag, nmCondPag=condpagamento.nmCondPag, ativo=condpagamento.ativo)
    db.add(db_condpagamento)
    db.commit()
    db.refresh(db_condpagamento)
    return db_condpagamento


def get_condpagamento(db: Session, skip: Optional[int] = None, limit: Optional[int] = None, filter: Optional[str]= "idCondPag" ):
    return db.query(models.CondPagamento).order_by(filter).offset(skip).limit(limit).all()


def get_condpagamento_idCondPag(db: Session, idCondPag: int):
    return db.query(models.CondPagamento).filter(models.CondPagamento.idCondPag == idCondPag).first()


def get_condpagamento_idErpCondPag(db: Session, idErpCondPag: str):
    return db.query(models.CondPagamento).filter(models.CondPagamento.idErpCondPag == idErpCondPag).first()


def put_condpagamento_idCondPag(db: Session, idCondPag: int, condpagamento: schemas.CondPagamento):
    db_condpagamento =  db.query(models.CondPagamento).filter(models.CondPagamento.idCondPag == idCondPag).first()

    db_condpagamento.idErpCondPag =  condpagamento.idErpCondPag
    db_condpagamento.nmCondPag =  condpagamento.nmCondPag
    db_condpagamento.ativo =  condpagamento.ativo

    db.add(db_condpagamento)
    db.commit()
    db.refresh(db_condpagamento)
    return db_condpagamento


def delete_condpagamento_idCondPag(db: Session, idCondPag: int):
    db_condpagamento =  db.query(models.CondPagamento).filter(models.CondPagamento.idCondPag == idCondPag).first()
    db.delete(db_condpagamento)
    db.commit()
    return db_condpagamento