from asyncio.windows_events import NULL
from typing import Optional
from fastapi import Query
from sqlalchemy.sql import text
from sqlalchemy.orm import Session

import models, schemas



def get_estoque(db: Session, filial: str):
    return db.query(models.Estoque).filter(models.Estoque.filial == filial).all()

def get_estoque_codProd(db: Session, filial: str, codProd: str):
    return db.query(models.Estoque).filter(models.Estoque.filial == filial, models.Estoque.codProd.like(f'%{codProd}%')).all()