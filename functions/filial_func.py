from typing import Optional
from sqlalchemy.orm import Session

import models, schemas


def post_filial(db: Session, filial: schemas.Filial):
    db_filial = models.Filial(codFilial= filial.codFilial, nmFilial=filial.nmFilial)
    db.add(db_filial)
    db.commit()
    db.refresh(db_filial)
    return db_filial


def get_filial(db: Session):
   return db.query(models.Filial).order_by('idFilial').all()


def get_filial_idFilial(db: Session, idFilial):
   if idFilial:
      return db.query(models.Filial).filter(models.Filial.idFilial == idFilial).all()


def get_filial_codFilial(db: Session, codFilial):
   if codFilial:
      return db.query(models.Filial).filter(models.Filial.codFilial == codFilial).first()


def put_filial_idFilial(db: Session, idFilial: int, filial: schemas.Filial):
    db_filial =  db.query(models.Filial).filter(models.Filial.idFilial == idFilial).first()

    db_filial.codFilial =  filial.codFilial
    db_filial.nmFilial =  filial.nmFilial

    db.add(db_filial)
    db.commit()
    db.refresh(db_filial)
    return db_filial


def delete_filial_idFilial(db: Session, idFilial: int):
    db_filial =  db.query(models.Filial).filter(models.Filial.idFilial == idFilial).first()
    db.delete(db_filial)
    db.commit()
    return db_filial
