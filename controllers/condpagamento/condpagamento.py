from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session

import functions.condpagamento_func  as condpagamento_func 
import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router_condpagamento = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router_condpagamento.post("/", response_model=schemas.CondPagamento)
def create_condpagamento(condpagamento: schemas.CondPagamento, db: Session = Depends(get_db)):
    db_ConPag = condpagamento_func.get_condpagamento_idErpCondPag(db, condpagamento.idErpCondPag)
    if db_ConPag:
        raise HTTPException(status_code=400, detail="Condição de pagamento already registered")
    return condpagamento_func.post_condpagamento(db, condpagamento)


@router_condpagamento.get("/", response_model=List[schemas.CondPagamento])
def read_condpagamento(skip: Optional[int] = None, limit: Optional[int] = None, filter: Optional[str]= "idErpCondPag",  db: Session = Depends(get_db)):
    db_ConPag = condpagamento_func.get_condpagamento(db, skip, limit, filter)
    return db_ConPag


@router_condpagamento.get("/{idCondPag}", response_model=schemas.CondPagamento)
def read_condpagamento_idCondPag(idCondPag: int, db: Session = Depends(get_db)):
    db_ConPag = condpagamento_func.get_condpagamento_idCondPag(db, idCondPag)
    return db_ConPag
 

@router_condpagamento.put("/{idCondPag}", response_model=schemas.CondPagamento)
def update_condpagamento(idCondPag: int , condpagamento: schemas.CondPagamento, db: Session = Depends(get_db)):
    db_ConPag = condpagamento_func.get_condpagamento_idCondPag(db, idCondPag)
    if not db_ConPag:
        raise HTTPException(status_code=400, detail="register not exist")
    return condpagamento_func.put_condpagamento_idCondPag(db, idCondPag, condpagamento)


@router_condpagamento.delete("/{idCondPag}")
def delete_condpagamento(idCondPag: int, db: Session = Depends(get_db)):
   db_ConPag = condpagamento_func.get_condpagamento_idCondPag(db, idCondPag)
   if not db_ConPag:
      raise HTTPException(status_code=400, detail="register not exist")
   #  db_ConPag = condpagamento_func.delete_condpagamento_idCondPag(db, idCondPag)
   return condpagamento_func.delete_condpagamento_idCondPag(db, idCondPag)
    # return {"delete": deleted}