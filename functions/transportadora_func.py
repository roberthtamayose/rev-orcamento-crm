from typing import Optional
from sqlalchemy.orm import Session

import models, schemas


def post_trasportadora(db: Session, transportadora: schemas.Transportadora):
    db_trasportadora = models.Transportadora(idErpTransp= transportadora.idErpTransp, nmTransp=transportadora.nmTransp, ativo=transportadora.ativo)
    db.add(db_trasportadora)
    db.commit()
    db.refresh(db_trasportadora)
    return db_trasportadora


def get_trasportadora_idTransp(db: Session, idTransp: str):
    return db.query(models.Transportadora).filter(models.Transportadora.idTransp == idTransp).first()


def get_trasportadora_idErpTransp(db: Session, idErpTransp: str):
    return db.query(models.Transportadora).filter(models.Transportadora.idErpTransp == idErpTransp).first()


def get_trasportadora(db: Session, skip: Optional[int] = None, limit: Optional[int] = None, filter: Optional[str]= "nmTransp" ):
    return db.query(models.Transportadora).order_by(filter).offset(skip).limit(limit).all()


def put_trasportadora_idTransp(db: Session, idTransp: int, transportadora: schemas.Transportadora):
    db_trasportadora =  db.query(models.Transportadora).filter(models.Transportadora.idTransp == idTransp).first()

    db_trasportadora.idErpTransp =  transportadora.idErpTransp
    db_trasportadora.nmTransp =  transportadora.nmTransp
    db_trasportadora.ativo =  transportadora.ativo

    db.add(db_trasportadora)
    db.commit()
    db.refresh(db_trasportadora)
    return db_trasportadora


def delete_trasportadora_idTransp(db: Session, idTransp: int):
    db_trasportadora =  db.query(models.Transportadora).filter(models.Transportadora.idTransp == idTransp).first()
    db.delete(db_trasportadora)
    db.commit()
    return db_trasportadora