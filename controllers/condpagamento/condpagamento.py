from typing import List, Optional
from fastapi import Depends, FastAPI, HTTPException, APIRouter, Query
from sqlalchemy.orm import Session
from pydantic import BaseModel
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


class CondPagamento(BaseModel):
   id: Optional[int] = None
   codCondPag: str
   nomeCondPag: str
   ativo: str

   class Config:
      orm_mode = True

@router_condpagamento.post("/", response_model=schemas.CondPagamento)
def create_condpagamento(condpagamento: schemas.CondPagamento, db: Session = Depends(get_db)):
    db_ConPag = condpagamento_func.get_condpagamento_codCondPag(db, condpagamento.codCondPag)
    if db_ConPag:
        raise HTTPException(status_code=400, detail="Condição de pagamento already registered")
    return condpagamento_func.post_condpagamento(db, condpagamento)


@router_condpagamento.get("/", response_model=List[schemas.CondPagamento])
def read_condpagamento(skip: Optional[int] = None, limit: Optional[int] = None, filter: list[str] | None = Query(None), id: Optional[int] = None, db: Session = Depends(get_db)):
    if id:
        db_ConPag = condpagamento_func.get_condpagamento_id(db, id)
    else:
        db_ConPag = condpagamento_func.get_condpagamento(db, skip, limit, filter)
    return db_ConPag


# @router_condpagamento.get("/{id}", response_model=schemas.CondPagamento)
# def read_condpagamento_id(id: int, db: Session = Depends(get_db)):
#     db_ConPag = condpagamento_func.get_condpagamento_id(db, id)
#     return db_ConPag
 

@router_condpagamento.put("/{id}", response_model=schemas.CondPagamento)
def update_condpagamento(id: int , condpagamento: schemas.CondPagamento, db: Session = Depends(get_db)):
    db_ConPag = condpagamento_func.get_condpagamento_id(db, id)
    if not db_ConPag:
        raise HTTPException(status_code=400, detail="register not exist")
    return condpagamento_func.put_condpagamento_id(db, id, condpagamento)


@router_condpagamento.delete("/{id}")
def delete_condpagamento(id: int, db: Session = Depends(get_db)):
   db_ConPag = condpagamento_func.get_condpagamento_id(db, id)
   if not db_ConPag:
      raise HTTPException(status_code=400, detail="register not exist")
   #  db_ConPag = condpagamento_func.delete_condpagamento_id(db, id)
   return condpagamento_func.delete_condpagamento_id(db, id)
    # return {"delete": deleted}