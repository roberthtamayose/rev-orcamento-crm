from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, APIRouter, Query
from sqlalchemy.orm import Session

import functions.preco_func as preco_func 
import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router_preco= APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router_preco.get("/", response_model=List[schemas.Preco])
def get_preco(skip: Optional[int] = None, limit: Optional[int] = None, filter: list[str] | None = Query(None), codProduto: Optional[str] = None, db: Session = Depends(get_db)):
    if codProduto :
        db_Ped = preco_func.get_preco_codProduto(db, codProduto)
    else:
        db_Ped = preco_func.get_preco(db, skip, limit, filter)
    return db_Ped