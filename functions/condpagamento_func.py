from typing import Optional
from sqlalchemy.orm import Session
from fastapi import Query
from sqlalchemy.sql import text

import models, schemas


def post_condpagamento(db: Session, condpagamento: schemas.CondPagamento):
    db_condpagamento = models.CondPagamento(codCondPag= condpagamento.codCondPag, nomeCondPag=condpagamento.nomeCondPag, ativo=condpagamento.ativo)
    db.add(db_condpagamento)
    db.commit()
    db.refresh(db_condpagamento)
    return db_condpagamento


def get_condpagamento(db: Session, skip: Optional[int] = None, limit: Optional[int] = None, filter: list[str] | None = Query(None) ):
    order = ','.join([str(i) for i in filter]) if filter else 'id'
    return db.query(models.CondPagamento).order_by(text(order)).offset(skip).limit(limit).all()


def get_condpagamento_id(db: Session, id: int):
    return db.query(models.CondPagamento).filter(models.CondPagamento.id == id).all()


def get_condpagamento_codCondPag(db: Session, codCondPag: str):
    return db.query(models.CondPagamento).filter(models.CondPagamento.codCondPag == codCondPag).first()


def put_condpagamento_id(db: Session, id: int, condpagamento: schemas.CondPagamento):
    db_condpagamento =  db.query(models.CondPagamento).filter(models.CondPagamento.id == id).first()

    db_condpagamento.codCondPag =  condpagamento.codCondPag
    db_condpagamento.nomeCondPag =  condpagamento.nomeCondPag
    db_condpagamento.ativo =  condpagamento.ativo

    db.add(db_condpagamento)
    db.commit()
    db.refresh(db_condpagamento)
    return db_condpagamento


def delete_condpagamento_id(db: Session, id: int):
    db_condpagamento =  db.query(models.CondPagamento).filter(models.CondPagamento.id == id).first()
    db.delete(db_condpagamento)
    db.commit()
    return db_condpagamento