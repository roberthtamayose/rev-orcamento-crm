from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, APIRouter
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
    db_transp = transportadora_func.get_trasportadora_idErpTransp(db, transportadora.idErpTransp)
    if db_transp:
        raise HTTPException(status_code=400, detail="Email already registered")
    return transportadora_func.post_trasportadora(db, transportadora)


@router_transportadoras.get("/", response_model=List[schemas.Transportadora])
def read_transportadoras(skip: Optional[int] = None, limit: Optional[int] = None, filter: Optional[str]= "idErpTransp",  db: Session = Depends(get_db)):
    db_transp = transportadora_func.get_trasportadora(db, skip, limit, filter)
    return db_transp


@router_transportadoras.get("/{idTransp}", response_model=schemas.Transportadora)
def read_transportadoras_idTransp(idTransp, db: Session = Depends(get_db)):
    db_transp = transportadora_func.get_trasportadora_idTransp(db, idTransp)
    return db_transp
 

@router_transportadoras.put("/{idTransp}", response_model=schemas.Transportadora)
def update_trasportadora(idTransp, transportadora: schemas.Transportadora, db: Session = Depends(get_db)):
    db_transp = transportadora_func.get_trasportadora_idTransp(db, idTransp)
    if not db_transp:
        raise HTTPException(status_code=400, detail="register not exist")
    return transportadora_func.put_trasportadora_idTransp(db, idTransp, transportadora)


@router_transportadoras.delete("/{idTransp}")
def delete_trasportadora(idTransp: int, db: Session = Depends(get_db)):
    db_transp = transportadora_func.get_trasportadora_idTransp(db, idTransp)
    if not db_transp:
        raise HTTPException(status_code=400, detail="register not exist")
    return transportadora_func.delete_trasportadora_idTransp(db, idTransp)
    # return {"delete": deleted}