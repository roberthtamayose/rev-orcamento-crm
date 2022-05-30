from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from fastapi import Depends, FastAPI, HTTPException, APIRouter, Query
import functions.vendedor_func  as vendedor_func 

import models, schemas

# def get_clientes(db: Session, skip: Optional[int] = None, limit: Optional[int] = None, filter: list[str] | None = Query(None), idCliente: Optional[int] = None, idVendedor:Optional[int] = None ):

def get_clientes(db: Session, idCliente:Optional[int] = None, idVendedor:Optional[int] = None, idUsuario:Optional[int] = None, skip: Optional[int] = None, limit: Optional[int] = None, filter: list[str] | None = Query(None)):
   order = ','.join([str(i) for i in filter]) if filter else 'idCliente'
   
   #Busca idvendedor pelo param idUsuario
   if idUsuario:
      aux =  vendedor_func.get_vendedor_idUsuario(db, idUsuario)
      db_vend = aux.idVendedor

   listParamOrig = list(locals().items())
   aux=[]
   for key, value in listParamOrig[1:4]:
      if value:
         if key == 'idUsuario':
            aux.append(f"idVendedor = {db_vend}")
         else:
            aux.append(f"{key} = {value}")
   listParamFinal = ' and '.join(map(str, aux))
   return db.query(models.Cliente).filter(text(listParamFinal)).order_by(text(order)).offset(skip).limit(limit).all()