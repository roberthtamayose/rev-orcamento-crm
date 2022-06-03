from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session

import functions.itempedido_func  as itempedido_func 
import functions.pedido_func as pedido_func 

import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router_itempedido = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# id_Marca ou id_Cliente verificar !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
@router_itempedido.post("/", response_model=List[schemas.ItemPedido])
def create_itempedido_idPedido(idFilial, itempedido: List[schemas.ItemPedido], idUsuario, db: Session = Depends(get_db)):
    # db_itempedido = pedido_func.get_pedido_idPedido_carrinho(db, idFilial, itempedido[0].idPedido, idUsuario) 
    # if not db_itempedido:
    #     # pedido_func.post_pedido(db, schemas.Pedido)
    #     return itempedido_func.post_itempedido_idFilial(db, idFilial, itempedido, idUsuario)
    return itempedido_func.post_itempedido_idFilial(db, idFilial, itempedido, idUsuario)


# @router_itempedido.get("/", response_model=List[schemas.ItemPedido])
# def read_transportadoras(skip: Optional[int] = None, limit: Optional[int] = None, filter: Optional[str]= "itempedido",  db: Session = Depends(get_db)):
#     db_transp = itempedido_func.get_itempedido_itempedido(db, skip, limit, filter)
#     return db_transp


@router_itempedido.get("/{idPedido}", response_model=List[schemas.ItemPedido])
def read_itempedido_idPedido(idFilial, idUsuario, idPed:Optional[int] = None, db: Session = Depends(get_db)):
    db_itempedido = itempedido_func.get_itempedido_idPedido(db, idFilial, idUsuario, idPed)
    return db_itempedido
 

@router_itempedido.put("/{idPedido}", response_model=schemas.ItemPedido)
def update_itempedido_idPedido(idPedido, itempedido: schemas.ItemPedido, db: Session = Depends(get_db)):
    db_itempedido = itempedido_func.get_itempedido_idPedido_idItem(db, itempedido.idItem, idPedido)
    if not db_itempedido:
        raise HTTPException(status_code=400, detail="register not exist")
    return itempedido_func.put_itempedido_idPedido(db, idPedido, itempedido)


@router_itempedido.delete("/{idPedido}/{idItem}")
def delete_itempedido_idPedido(idPedido: int, idItem: Optional[int], db: Session = Depends(get_db)):
    db_itempedido = itempedido_func.get_itempedido_idPedido_idItem(db, idItem, idPedido)
    if not db_itempedido:
        raise HTTPException(status_code=400, detail="register not exist")
    return itempedido_func.delete_itempedido_idPedido_idItem(db, idItem, idPedido)
    # return {"delete": deleted}
    # delete_itempedido

@router_itempedido.delete("/{idPedido}")
def delete_itempedido_idPedido(idPedido: int, db: Session = Depends(get_db)):
    db_itempedido = itempedido_func.get_itempedido_idPedido(db, idPedido)
    if not db_itempedido:
        raise HTTPException(status_code=400, detail="register not exist")
    return itempedido_func.delete_itempedido(db, idPedido)
    # return {"delete": deleted}
    # delete_itempedido