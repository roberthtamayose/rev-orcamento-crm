from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, APIRouter, Query
from sqlalchemy.orm import Session

import functions.cliente_func  as cliente_func 
import functions.usuario_func  as usuario_func 
import functions.vendedor_func  as vendedor_func 


import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router_cliente = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# def read_cliente(skip: Optional[int] = None, limit: Optional[int] = None, filter: Optional[str]= "id", id:Optional[int] = None, idVendedor:Optional[int] = None, idUsuario:Optional[int] = None, db: Session = Depends(get_db)):

@router_cliente.get("/", response_model=List[schemas.Cliente])
def read_cliente(vend_id: int, skip: Optional[int] = None, limit: Optional[int] = None, filter: list[str] | None = Query(None), db: Session = Depends(get_db)):
    db_Cliente = cliente_func.get_clientes(db, vend_id, skip, limit, filter)
    return db_Cliente


@router_cliente.get("/{id}", response_model=List[schemas.Cliente])
def read_cliente(id: int, db: Session = Depends(get_db)):
    db_Cliente = cliente_func.get_clientes_id(db, id)
    return db_Cliente