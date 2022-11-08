from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, APIRouter, Query
from sqlalchemy.orm import Session

import functions.orcamento_func as orcamento_func 
import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router_orcamento= APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router_orcamento.post("/", response_model=schemas.OrcamentoPost)
def create_orcamento(orcamento: schemas.OrcamentoPost1,  db: Session = Depends(get_db)):
    print ("orcamento..........",orcamento)
    if orcamento.numOrc :
        db_orc = orcamento_func.get_orcamento_numOrc(db, orcamento.numOrc)
        if db_orc:
            return orcamento_func.post_orcamento_revisao(db, orcamento)
            # raise HTTPException(status_code=400, detail="Orcamento já cadatrado.")
        else:
            return orcamento_func.post_orcamento(db, orcamento)
    else: 
        return orcamento_func.post_orcamento(db, orcamento)

@router_orcamento.get("/", response_model=List[schemas.Orcamento])
def get_orcamento(skip: Optional[int] = None, limit: Optional[int] = None, filter: list[str] | None = Query(None), db: Session = Depends(get_db)):
    db_Orc = orcamento_func.get_orcamento(db, skip, limit, filter)
    return db_Orc


@router_orcamento.get("/{id}", response_model=List[schemas.Orcamento])
def get_orcamento_id(id: int, db: Session = Depends(get_db)):
    db_Orc = orcamento_func.get_orcamento_id(db, id)
    return db_Orc

@router_orcamento.get("/max/", response_model=schemas.OrcamentoMaxNum)
def get_orcamento_max_numOrc(filial: str, db: Session = Depends(get_db)):
    db_Orc = orcamento_func.get_orcamento_max_numOrc(db, filial)
    return db_Orc


@router_orcamento.put("/{id}", response_model=schemas.OrcamentoPost)
def update_orcamento( id: int, orcamento: schemas.OrcamentoPost, db: Session = Depends(get_db)):
    db_orc = orcamento_func.get_orcamento_id(db, id)
    if not db_orc:
        raise HTTPException(status_code=400, detail="Orcamento com Id: {id} não existe.")
    return orcamento_func.put_orcamento(db, id, orcamento)


# @router_pedido.put("/{idPedido}", response_model=schemas.Pedido)
# def update_pedido(idPedido: int , pedido: schemas.Pedido, db: Session = Depends(get_db)):
#     db_Ped = orcamento_func.get_pedido_idPedido(db, idPedido)
#     if not db_Ped:
#         raise HTTPException(status_code=400, detail="register not exist")
#     return orcamento_func.put_pedido_idPedido(db, idPedido, pedido)


# @router_pedido.delete("/{idPedido}")
# def delete_pedido(idPedido: int, db: Session = Depends(get_db)):
#     db_Ped = orcamento_func.get_pedido_idPedido(db, idPedido)
#     if not db_Ped:
#         raise HTTPException(status_code=400, detail="register not exist")
#     return orcamento_func.delete_pedido_idPedido(db, idPedido)
#     # return {"delete": deleted}