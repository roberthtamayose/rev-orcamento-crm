from typing import Optional
from sqlalchemy.orm import Session
from fastapi import Query
from sqlalchemy.sql import text
import models, schemas


# id	int
# codVend	varchar
# user_id	int

def post_vendedor(db: Session, codVend: str, user_id: int):
    db_vendedor = models.Vendedor(codVend = codVend, user_id = user_id)
    db.add(db_vendedor)
    db.commit()
    db.refresh(db_vendedor)
    return db_vendedor



def get_vendedor(db: Session, skip: Optional[int] = None, limit: Optional[int] = None, filter: list[str] | None = Query(None)):
    order = ','.join([str(i) for i in filter]) if filter else 'id'
    return db.query(models.Vendedor).order_by(text(order)).offset(skip).limit(limit).all()


def get_vendedor_id(db: Session, id: int):
    return db.query(models.Vendedor).filter(models.Vendedor.id == id).all()


def get_vendedor_user_id(db: Session, user_id: int):
    return db.query(models.Vendedor).filter(models.Vendedor.user_id == user_id).first()