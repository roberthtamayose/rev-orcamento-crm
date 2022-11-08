from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session

import functions.itemOrcamento_func  as itemOrcamento_func 
# import functions.pedido_func as pedido_func 

import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router_itemOrcamento = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router_itemOrcamento.post("/", response_model=List[schemas.ItemOrcamentoPost])
def create_orcamento(itemOrcamento: List[schemas.ItemOrcamentoPost], db: Session = Depends(get_db)):
    return itemOrcamento_func.post_itemOrcamento(db, itemOrcamento)



@router_itemOrcamento.get("/{idOrcamento}", response_model=List[schemas.ItemOrcamento])
def read_itemOrcamento_idOrcamento(idOrcamento: int, db: Session = Depends(get_db)):
    db_itemOrcamento = itemOrcamento_func.get_itemOrcamento(db, idOrcamento)
    return db_itemOrcamento

# @router_itempedido.get("/", response_model=List[schemas.ItemPedido])
# def read_itempedido_idPedido(idFilial, idUsuario, idPed: Optional[int] = None, db: Session = Depends(get_db)):
#     db_itempedido = itempedido_func.get_itempedido_idPedido(db, idFilial, idUsuario, idPed)
#     return db_itempedido
 

# @router_itempedido.put("/{idPedido}", response_model=schemas.ItemPedido)
# def update_itempedido_idPedido(idPedido, itempedido: schemas.ItemPedido, db: Session = Depends(get_db)):
#     db_itempedido = itempedido_func.get_itempedido_idPedido_idItem(db, itempedido.idItem, idPedido)
#     if not db_itempedido:
#         raise HTTPException(status_code=400, detail="register not exist")
#     return itempedido_func.put_itempedido_idPedido(db, idPedido, itempedido)


# @router_itempedido.delete("/{idPedido}/{idItem}")
# def delete_itempedido_idPedido(idPedido: int, idItem: Optional[int], db: Session = Depends(get_db)):
#     db_itempedido = itempedido_func.get_itempedido_idPedido_idItem(db, idItem, idPedido)
#     if not db_itempedido:
#         raise HTTPException(status_code=400, detail="register not exist")
#     return itempedido_func.delete_itempedido_idPedido_idItem(db, idItem, idPedido)
#     # return {"delete": deleted}
#     # delete_itempedido

# @router_itempedido.delete("/{idPedido}")
# def delete_itempedido_idPedido(idPedido: int, db: Session = Depends(get_db)):
#     db_itempedido = itempedido_func.get_itempedido_idPedido(db, idPedido)
#     if not db_itempedido:
#         raise HTTPException(status_code=400, detail="register not exist")
#     return itempedido_func.delete_itempedido(db, idPedido)
#     # return {"delete": deleted}
#     # delete_itempedido