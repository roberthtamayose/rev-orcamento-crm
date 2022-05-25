from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, APIRouter, Query
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
def read_vendedor(skip: Optional[int] = None, limit: Optional[int] = None, filter: list[str] | None = Query(None), idVendedor: Optional[int] = None, db: Session = Depends(get_db)):
    if idVendedor:
        db_Vend= vendedor_func.get_vendedor_idVendedor(db, idVendedor)
    else:
        db_Vend = vendedor_func.get_vendedor(db, skip, limit, filter)
    return db_Vend