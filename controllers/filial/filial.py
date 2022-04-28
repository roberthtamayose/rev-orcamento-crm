from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session

import functions.filial_func  as filial_func 
import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router_filiais = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router_filiais.post("/", response_model=schemas.Filial)
def create_filial(filial: schemas.Filial, db: Session = Depends(get_db)):
    db_filial = filial_func.get_filial_codFilial(db, filial.codFilial)
    if db_filial:
        raise HTTPException(status_code=400, detail="Filial já Cadastrada")
    return filial_func.post_filial(db, filial)


@router_filiais.get("/", response_model=List[schemas.Filial])
def read_filiais(idFilial: Optional[str] = None, db: Session = Depends(get_db)):
    if idFilial:
        db_filial = filial_func.get_filial_idFilial(db, idFilial)
    else:
        db_filial = filial_func.get_filial(db)
    return db_filial
 
# @router_filiais.get("/{idFilial}", response_model=schemas.Filial)
# def read_filial(idFilial, db: Session = Depends(get_db)):
#     db_filial = filial_func.get_filial_idFilial(db, idFilial)
#     return db_filial
 
@router_filiais.put("/{idFilial}", response_model=schemas.Filial)
def update_filial(idFilial, filial: schemas.Filial, db: Session = Depends(get_db)):
    db_filial = filial_func.get_filial_idFilial(db, idFilial)
    if not db_filial:
        raise HTTPException(status_code=400, detail="register not exist")
    return filial_func.put_filial_idFilial(db, idFilial, filial)


@router_filiais.delete("/{idFilial}")
def read_item(idFilial: int, db: Session = Depends(get_db)):
    db_filial = filial_func.get_filial_idFilial(db, idFilial)
    if not db_filial:
        raise HTTPException(status_code=400, detail="register not exist")
    return filial_func.delete_filial_idFilial(db, idFilial)
    # return {"delete": deleted}

