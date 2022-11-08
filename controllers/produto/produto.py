from typing import List, Optional, Dict

from fastapi import Depends, FastAPI, HTTPException, APIRouter, Query
from sqlalchemy.orm import Session

import functions.produto_func  as produto_func
import functions.estoque_func  as estoque_func

import models, schemas
from database import SessionLocal, engine
from pydantic import BaseModel

models.Base.metadata.create_all(bind=engine)

router_produto = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Cores(BaseModel):
   codCor: str
   nomeCor: str

   class Config:
      orm_mode = True

class Estoque(BaseModel):
   id: Optional[int] = None
   colecao: str
   quantidade: float

   class Config:
      orm_mode = True

class ProdutoFull(BaseModel):
    id: Optional[int] = None
    filial: str
    codProd: str
    nomeProd: str
    # colecao: str
    ativo: str
    cores: Cores 
    estoque: list[Estoque] = None

    class Config:
        orm_mode = True

class ProdutoCodProd(BaseModel):
    codProd: str
    nomeProd: str

    class Config:
        orm_mode = True


@router_produto.get("/", response_model=List[ProdutoCodProd])
def read_produtos(filial: Optional[str] = None, db: Session = Depends(get_db)):
    db_Prod = produto_func.get_produto(db, filial)
    return db_Prod

@router_produto.get("/{codProd}", response_model=List[ProdutoFull])
def read_produto_codProd(filial: Optional[str] = '01', codProd= str, db: Session = Depends(get_db)):
    db_Prod = produto_func.get_produto_codProd(db, filial, codProd)
    return db_Prod