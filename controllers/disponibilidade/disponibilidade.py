from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, APIRouter, Query
from sqlalchemy.orm import Session

import functions.estoque_func  as estoque_func 
import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router_disponibilidade = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




# @router_disponibilidade.get("/produtos", response_model= List[schemas.Produto])
# def read_produtos(filial: Optional[int] = 1, codProduto: Optional[str] = None, nmProduto: Optional[str] = None, skip: Optional[int] = 0, limit: Optional[int] = None, filter: list[str] | None = Query(None),  db: Session = Depends(get_db)):
#     db_Disp = disponibilidade_func.get_disponibilidade_produto(db, filial, codProduto, nmProduto, skip, limit, filter)
#     return db_Disp

@router_disponibilidade.get("/produtos", response_model=List[schemas.Produto])
def read_produtos(skip: Optional[int] = None, limit: Optional[int] = None, filter: list[str] | None = Query(None), codProduto : Optional[str] = None, db: Session = Depends(get_db)):
    if codProduto:
        db_Disp = estoque_func.get_disponibilidade_produto_codProduto(db, codProduto)
    else:
        db_Disp = estoque_func.get_disponibilidade_produto(db, skip, limit, filter)
    return db_Disp


@router_disponibilidade.get("/estoques", response_model=List[schemas.Estoque])
def read_estoques(idFilial: Optional[int] = None, codProduto : Optional[str] = None, db: Session = Depends(get_db)):
    db_Disp = estoque_func.get_disponibilidade_estoque_codProduto(db, idFilial, codProduto)
    return db_Disp


# @router_disponibilidade.get("/cores", response_model= List[schemas.Cores])
# def read_cores(filial: Optional[int] = 1, skip: Optional[int] = 0, limit: Optional[int] = None, prod: Optional[str] = None, filter: list[str] | None = Query(None),  db: Session = Depends(get_db)):
#     db_Disp = disponibilidade_func.get_disponibilidade_cor(db, skip, limit, prod, filter, filial)
#     return db_Disp


# @router_disponibilidade.get("/colecoes", response_model= List[schemas.Colecoes])
# def read_cores(db: Session = Depends(get_db)):
#     db_Disp = disponibilidade_func.get_disponibilidade_colecao(db)
#     return db_Disp