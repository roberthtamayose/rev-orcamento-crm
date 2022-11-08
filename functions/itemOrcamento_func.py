from typing import List, Optional
from sqlalchemy.orm import Session

import models, schemas


def post_itemOrcamento(db: Session, itemOrcamento: List[schemas.ItemOrcamentoPost]):
    result=[]
    for item in itemOrcamento:
        db_orc = models.ItemOrcamento(
            filial = item.filial, 
            quantidade = item.quantidade, 
            preco = item.preco, 
            orc_id = item.orc_id,
            prod_id = item.prod_id, 
            ativo = item.ativo
        )
        db.add(db_orc)
        db.commit()
        result.append(db_orc)
        db.refresh(db_orc)
    return result


def get_itemOrcamento(db: Session, orc_id: int):
   return db.query(models.ItemOrcamento).filter(models.ItemOrcamento.orc_id == orc_id).all()
