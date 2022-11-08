from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, APIRouter, Query
from sqlalchemy.orm import Session

import functions.transportadora_func  as transportadora_func 
import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router_transportadoras = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router_transportadoras.post("/", response_model=schemas.Transportadora)
def create_trasportadora(transportadora: schemas.Transportadora, db: Session = Depends(get_db)):
    db_transp = transportadora_func.get_trasportadora_codTransp(db, transportadora.codTransp)
    if db_transp:
        raise HTTPException(status_code=400, detail="Transportadora já registrada")
    return transportadora_func.post_trasportadora(db, transportadora)


@router_transportadoras.get("/", response_model=List[schemas.Transportadora])
def read_transportadoras(skip: Optional[int] = None, limit: Optional[int] = None, filter: list[str] | None = Query(None), id : Optional[str] = None, db: Session = Depends(get_db)):
    if id:
        db_transp = transportadora_func.get_trasportadora_id(db, id)
    else:
        db_transp = transportadora_func.get_trasportadora(db, skip, limit, filter)
    return db_transp


@router_transportadoras.put("/{id}", response_model=schemas.Transportadora)
def update_trasportadora(id, transportadora: schemas.Transportadora, db: Session = Depends(get_db)):
    db_transp = transportadora_func.get_trasportadora_id(db, id)
    if not db_transp:
        raise HTTPException(status_code=400, detail="register not exist")
    return transportadora_func.put_trasportadora_id(db, id, transportadora)


@router_transportadoras.delete("/{id}")
def delete_trasportadora(id: int, db: Session = Depends(get_db)):
    db_transp = transportadora_func.get_trasportadora_id(db, id)
    if not db_transp:
        raise HTTPException(status_code=400, detail="register not exist")
    return transportadora_func.delete_trasportadora_id(db, id)
    # return {"delete": deleted}