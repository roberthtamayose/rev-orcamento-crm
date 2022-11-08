from typing import Optional
from sqlalchemy.orm import Session
from fastapi import Query
from sqlalchemy.sql import text
import models, schemas
from sqlalchemy.sql.expression import func
import functions.itemOrcamento_func as itemOrcamento_func 


def post_orcamento(db: Session, orcamento: schemas.OrcamentoPost1):
    numOrcMax = get_orcamento_max_numOrc(db)
    db_orc = models.Orcamento(
        filial = orcamento.filial, 
        numOrc = str(int(numOrcMax.numOrc)+1).zfill(6), 
        numRevisao = "01", 
        status = orcamento.status,
        cliente_id = orcamento.cliente_id, 
        vend_id = orcamento.vend_id, 
        condPag_id = orcamento.condPag_id, 
        transp_id = orcamento.transp_id, 
        ativo = orcamento.ativo
    )
    db.add(db_orc)
    db.commit()
    db.refresh(db_orc)
    for item in orcamento.itemOrcamento:
        item.orc_id = db_orc.id
    itemOrcamento_func.post_itemOrcamento(db, orcamento.itemOrcamento)
    return db_orc

def post_orcamento_revisao(db: Session, orcamento: schemas.OrcamentoPost):
    numOrcMax = get_orcamento_max_numOrc(db)
    print ("numOrcMax.........",numOrcMax)
    db_orc = models.Orcamento(
        filial = orcamento.filial, 
        numOrc = str(int(numOrcMax.numOrc)+1).zfill(6), 
        numRevisao = str(int(numOrcMax.numRevisao)+1).zfill(2), 
        status = orcamento.status,
        cliente_id = orcamento.cliente_id, 
        vend_id = orcamento.vend_id, 
        condPag_id = orcamento.condPag_id, 
        transp_id = orcamento.transp_id, 
        ativo = orcamento.ativo
    )
    db.add(db_orc)
    db.commit()
    db.refresh(db_orc)
    return db_orc


def get_orcamento_max_numOrc(db: Session):
    return db.query(models.Orcamento).order_by(models.Orcamento.numOrc.desc(),models.Orcamento.numRevisao.desc()).first()


def get_orcamento(db: Session, skip: Optional[int] = None, limit: Optional[int] = None, filter: list[str] | None = Query(None) ):
    order = ','.join([str(i) for i in filter]) if filter else 'numOrc'
    return db.query(models.Orcamento).order_by(text(order)).offset(skip).limit(limit).all()


def get_orcamento_id(db: Session, id: int):
    return db.query(models.Orcamento).filter(models.Orcamento.id == id ).all()


def get_orcamento_revisao(db: Session, orc: str, rev: str):
    return db.query(models.Orcamento).filter(models.Orcamento.numOrc == orc , models.Orcamento.numRevisao == rev).all()


def get_orcamento_numOrc(db: Session, orc: str,):
    return db.query(models.Orcamento).filter(models.Orcamento.numOrc == orc ).all()



def put_orcamento(db: Session, id: int, orcamento: schemas.OrcamentoPost):
    db_orc =  db.query(models.Orcamento).filter(models.Orcamento.id == id).first()

    db_orc.filial = orcamento.filial
    db_orc.numOrc = orcamento.numOrc
    db_orc.numRevisao = orcamento.numRevisao
    db_orc.status = orcamento.status
    db_orc.cliente_id = orcamento.cliente_id
    db_orc.vend_id = orcamento.vend_id
    db_orc.condPag_id = orcamento.condPag_id
    db_orc.transp_id = orcamento.transp_id
    db_orc.ativo = orcamento.ativo

    db.add(db_orc)
    db.commit()
    db.refresh(db_orc)
    return db_orc


# def delete_pedido_idPedido(db: Session, idPedido: int):
#     db_ped =  db.query(models.Pedido).filter(models.Pedido.idPedido == idPedido).first()
#     db.delete(db_ped)
#     db.commit()
#     return db_ped