from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from fastapi import Query

import models, schemas


def post_trasportadora(db: Session, transportadora: schemas.Transportadora):
    db_trasportadora = models.Transportadora(codTransp= transportadora.codTransp, nomeTransp=transportadora.nomeTransp, ativo=transportadora.ativo)
    db.add(db_trasportadora)
    db.commit()
    db.refresh(db_trasportadora)
    return db_trasportadora


def get_trasportadora_id(db: Session, id: str):
    return db.query(models.Transportadora).filter(models.Transportadora.id == id).all()


def get_trasportadora_codTransp(db: Session, codTransp: str):
    return db.query(models.Transportadora).filter(models.Transportadora.codTransp == codTransp).first()


def get_trasportadora(db: Session, skip: Optional[int] = None, limit: Optional[int] = None, filter: list[str] | None = Query(None) ): 
    order = ','.join([str(i) for i in filter]) if filter else 'nomeTransp'
    return db.query(models.Transportadora).order_by(text(order)).offset(skip).limit(limit).all()


def put_trasportadora_id(db: Session, id: int, transportadora: schemas.Transportadora):
    db_trasportadora =  db.query(models.Transportadora).filter(models.Transportadora.id == id).first()

    db_trasportadora.codTransp =  transportadora.codTransp
    db_trasportadora.nomeTransp =  transportadora.nomeTransp
    db_trasportadora.ativo =  transportadora.ativo

    db.add(db_trasportadora)
    db.commit()
    db.refresh(db_trasportadora)
    return db_trasportadora


def delete_trasportadora_id(db: Session, id: int):
    db_trasportadora =  db.query(models.Transportadora).filter(models.Transportadora.id == id).first()
    db.delete(db_trasportadora)
    db.commit()
    return db_trasportadora