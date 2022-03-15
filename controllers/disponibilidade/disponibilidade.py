from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session

import functions.disponibilidade_func  as disponibilidade_func 
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




@router_disponibilidade.get("/produtos", response_model= List[schemas.Produto])
def read_produtos(filial: Optional[int] = None, skip: Optional[int] = None, limit: Optional[int] = None, filter: Optional[str]= "nmProduto",  db: Session = Depends(get_db)):
    db_Disp = disponibilidade_func.get_disponibilidade_produto(db, skip, limit, filter, filial)
    return db_Disp

