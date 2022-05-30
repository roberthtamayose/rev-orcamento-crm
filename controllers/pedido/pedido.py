from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, APIRouter, Query
from sqlalchemy.orm import Session

import functions.pedido_func as pedido_func 
import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router_pedido= APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router_pedido.post("/", response_model=schemas.Pedido)
def create_pedido(pedido: schemas.Pedido, db: Session = Depends(get_db)):
    db_Ped = pedido_func.get_pedido_codPedido(db, pedido.codPedido)
    if db_Ped:
        raise HTTPException(status_code=400, detail="Condição de pagamento already registered")
    return pedido_func.post_pedido(db, pedido)


@router_pedido.get("/", response_model=List[schemas.Pedido])
def get_pedido(skip: Optional[int] = None, limit: Optional[int] = None, filter: list[str] | None = Query(None), idFilial:Optional[int] = None, idUsuario:Optional[int] = None, idPedido:Optional[int] = None, ativo:Optional[int] = None, status:Optional[int] = None, idCliente:Optional[int] = None, db: Session = Depends(get_db)):
    db_Ped = pedido_func.get_pedido_allParam(db, idFilial, idPedido, idUsuario, idCliente, ativo, status, skip, limit, filter)
    return db_Ped


@router_pedido.put("/{idPedido}", response_model=schemas.Pedido)
def update_pedido(idPedido: int , pedido: schemas.Pedido, db: Session = Depends(get_db)):
    db_Ped = pedido_func.get_pedido_idPedido(db, idPedido)
    if not db_Ped:
        raise HTTPException(status_code=400, detail="register not exist")
    return pedido_func.put_pedido_idPedido(db, idPedido, pedido)


@router_pedido.delete("/{idPedido}")
def delete_pedido(idPedido: int, db: Session = Depends(get_db)):
    db_Ped = pedido_func.get_pedido_idPedido(db, idPedido)
    if not db_Ped:
        raise HTTPException(status_code=400, detail="register not exist")
    return pedido_func.delete_pedido_idPedido(db, idPedido)
    # return {"delete": deleted}