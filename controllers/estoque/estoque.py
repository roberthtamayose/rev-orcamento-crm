from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, APIRouter, Query
from sqlalchemy.orm import Session

import functions.estoque_func  as estoque_func 
import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router_estoque = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router_estoque.get("/", response_model=List[schemas.Estoque])
def read_estoques(filial: Optional[str] = None, db: Session = Depends(get_db)):
    db_Disp = estoque_func.get_estoque(db, filial)
    return db_Disp

@router_estoque.get("/{codProd}", response_model=List[schemas.Estoque])
def read_estoques_codProd(filial: Optional[str] = '01', codProd= str, db: Session = Depends(get_db)):
    db_est = estoque_func.get_estoque_codProd(db, filial, codProd)
    return db_est