from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session

import functions.vendedor_func  as vendedor_func 
import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router_vendedor = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router_vendedor.get("/", response_model=List[schemas.Vendedor])
def read_vendedor(skip: Optional[int] = None, limit: Optional[int] = None, filter: Optional[str]= "idVendedor",  db: Session = Depends(get_db)):
    db_ConPag = vendedor_func.get_vendedor(db, skip, limit, filter)
    return db_ConPag


@router_vendedor.get("/{idVendedor}", response_model=schemas.Vendedor)
def read_vendedor_idVendedor(idVendedor, db: Session = Depends(get_db)):
    db_ConPag = vendedor_func.get_vendedor_idVendedor(db, idVendedor)
    return db_ConPag