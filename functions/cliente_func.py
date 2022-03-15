from typing import Optional
from sqlalchemy.orm import Session

import models, schemas


def get_clientes(db: Session, skip: Optional[int] = None, limit: Optional[int] = None, filter: Optional[str]= "idCliente", idCliente:Optional[int] = None, idVendedor:Optional[int] = None ):
   if idVendedor and not idCliente:
      return db.query(models.Cliente).filter(models.Cliente.idVendedor == idVendedor).order_by(filter).offset(skip).limit(limit).all()
   elif idCliente and not idVendedor:
      return db.query(models.Cliente).filter(models.Cliente.idCliente == idCliente).all()
   elif idCliente and idVendedor:
      return db.query(models.Cliente).filter(models.Cliente.idCliente == idCliente, models.Cliente.idVendedor == idVendedor).order_by(filter).offset(skip).limit(limit).all()
   else:
      return db.query(models.Cliente).order_by(filter).offset(skip).limit(limit).all()