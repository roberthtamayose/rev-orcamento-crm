from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from fastapi import Depends, FastAPI, HTTPException, APIRouter, Query

import models, schemas

# def get_clientes(db: Session, skip: Optional[int] = None, limit: Optional[int] = None, filter: list[str] | None = Query(None), idCliente: Optional[int] = None, idVendedor:Optional[int] = None ):

def get_clientes(db: Session, skip: Optional[int] = None, limit: Optional[int] = None, filter: list[str] | None = Query(None), idCliente:Optional[int] = None, idVendedor:Optional[int] = None ):
   order = ','.join([str(i) for i in filter]) if filter else 'idCliente'

   if idVendedor and not idCliente:
      return db.query(models.Cliente).filter(models.Cliente.idVendedor == idVendedor).order_by(text(order)).offset(skip).limit(limit).all()
   elif idCliente and not idVendedor:
      return db.query(models.Cliente).filter(models.Cliente.idCliente == idCliente).all()
   elif idCliente and idVendedor:
      return db.query(models.Cliente).filter(models.Cliente.idCliente == idCliente, models.Cliente.idVendedor == idVendedor).order_by(text(order)).offset(skip).limit(limit).all()
   else:
      return db.query(models.Cliente).order_by(text(order)).offset(skip).limit(limit).all()