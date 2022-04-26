from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from fastapi import Depends, FastAPI, HTTPException, APIRouter, Query

import models, schemas

# def get_clientes(db: Session, skip: Optional[int] = None, limit: Optional[int] = None, filter: list[str] | None = Query(None), idCliente: Optional[int] = None, idVendedor:Optional[int] = None ):

def get_clientes(db: Session, skip: Optional[int] = None, limit: Optional[int] = None, order: list[str] | None = Query(None), filter: list[str] | None = Query(None), idVendedor:Optional[int] = None):
   order = ','.join([str(i) for i in order]) if order else 'idCliente'
   
   filter = ' and '.join([str(i) for i in filter]) if filter else ''
   print("filter......", filter)
   

   if filter and not idVendedor:
      return db.query(models.Cliente).filter(text(filter)).order_by(text(order)).offset(skip).limit(limit).all()
   elif not filter and idVendedor:
      return db.query(models.Cliente).filter(models.Cliente.idVendedor == idVendedor).order_by(text(order)).offset(skip).limit(limit).all()
   elif filter and idVendedor:
      print("idVendedor....", idVendedor)
      return db.query(models.Cliente).filter(text(filter), models.Cliente.idVendedor == idVendedor).order_by(text(order)).offset(skip).limit(limit).all()
   else:
      return db.query(models.Cliente).order_by(text(order)).offset(skip).limit(limit).all()