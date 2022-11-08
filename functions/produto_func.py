from asyncio.windows_events import NULL
from typing import Optional
from fastapi import Query
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

import models, schemas



def get_produto(db: Session, filial: str):
    return db.query(func.substring(models.Produto.codProd,1,9).distinct().label("codProd"),func.substring(models.Produto.nomeProd,1,func.charindex("./",models.Produto.nomeProd)-1).label("nomeProd")).filter(models.Produto.filial == filial).all()

# def get_produto(db: Session, filial: str):
#     return db.query(models.Produto).filter(models.Produto.filial == filial).all()


def get_produto_codProd(db: Session, filial: str, codProd: str):
    return db.query(models.Produto).filter(models.Produto.filial == filial, models.Produto.codProd.like(f'%{codProd}%')).all()