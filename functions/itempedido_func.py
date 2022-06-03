from typing import List, Optional
from sqlalchemy.orm import Session
import functions.pedido_func as pedido_func 

import models, schemas


# def post_itempedido(db: Session, filial, itempedido: List[schemas.ItemPedido], idUsuario):
#     existped = pedido_func.get_pedido_idPedido_carrinho(db, filial, itempedido[0].idPedido, idUsuario)
#     result = []
#     if existped:
#         for item in itempedido:
#             db_itempedido = models.ItemPedido(codProduto = item.codProduto, nmProduto = item.nmProduto, idErpColecao = item.idErpColecao, vlUnitario = item.vlUnitario, vlDesconto = item.vlDesconto, vlTotal = item.vlTotal,qtdItem = item.qtdItem, idPedido = item.idPedido)
#             result.append(db_itempedido)
#             db.add(db_itempedido)
#             db.commit()
#         db.refresh(db_itempedido)
#     return result
   
   
# id_Marca ou id_Cliente verificar !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def post_itempedido_idFilial(db: Session, filial, itempedido: List[schemas.ItemPedido], idUsuario):
    existped = pedido_func.get_pedido_idPedido_carrinho(db, filial, idUsuario)
    result = []
    if existped:
        for item in itempedido:
            db_itempedido = models.ItemPedido(codProduto = item.codProduto, nmProduto = item.nmProduto, idErpColecao = item.idErpColecao, vlUnitario = item.vlUnitario, vlDesconto = item.vlDesconto, vlTotal = item.vlTotal,qtdItem = item.qtdItem, idPedido = existped.idPedido)
            result.append(db_itempedido)
            db.add(db_itempedido)
            db.commit()
            db.refresh(db_itempedido)
        return result
    else:
        cabped = pedido_func.post_pedido_idfilial_idUsuario (db, filial, idUsuario)
        for item in itempedido:
            db_itempedido = models.ItemPedido(codProduto = item.codProduto, nmProduto = item.nmProduto, idErpColecao = item.idErpColecao, vlUnitario = item.vlUnitario, vlDesconto = item.vlDesconto, vlTotal = item.vlTotal,qtdItem = item.qtdItem, idPedido = cabped.idPedido)
            result.append(db_itempedido)
            db.add(db_itempedido)
            db.commit()
            db.refresh(db_itempedido)
        return result
    

def get_itempedido_idPedido(db: Session, filial, idUsuario, idPedido):
    if idPedido :
        return db.query(models.ItemPedido).filter(models.ItemPedido.idPedido == idPedido).all()
    else:
        existped = pedido_func.get_pedido_idPedido_carrinho(db, filial, idUsuario)
        if existped:
            return db.query(models.ItemPedido).filter(models.ItemPedido.idPedido == existped.idPedido).all()
    return []

def get_itempedido_idPedido_idItem(db: Session, idItem, idPedido):
    return db.query(models.ItemPedido).filter(models.ItemPedido.idItem == idItem, models.ItemPedido.idPedido == idPedido).first()


# def get_itempedido(db: Session, skip: Optional[int] = None, limit: Optional[int] = None, filter: Optional[str]= "nmTransp" ):
#     return db.query(models.ItemPedido).order_by(filter).offset(skip).limit(limit).all()


def put_itempedido_idPedido(db: Session, idPedido: int, itempedido: schemas.ItemPedido):
    db_itempedido =  db.query(models.ItemPedido).filter(models.ItemPedido.idPedido == idPedido, models.ItemPedido.idItem == itempedido.idItem).first()
    if db_itempedido:
        db_itempedido.codProduto =  itempedido.codProduto
        db_itempedido.nmProduto =  itempedido.nmProduto
        db_itempedido.idErpColecao =  itempedido.idErpColecao
        db_itempedido.vlUnitario =  itempedido.vlUnitario
        db_itempedido.vlDesconto =  itempedido.vlDesconto
        db_itempedido.vlTotal =  itempedido.vlTotal
        db_itempedido.qtdItem =  itempedido.qtdItem
        db_itempedido.idPedido =  itempedido.idPedido

    db.add(db_itempedido)
    db.commit()
    db.refresh(db_itempedido)
    return db_itempedido


def delete_itempedido_idPedido_idItem(db: Session, idItem: int, idPedido: int):
    db_itempedido =  db.query(models.ItemPedido).filter(models.ItemPedido.idPedido == idPedido, models.ItemPedido.idItem == idItem).first()
    db.delete(db_itempedido)
    db.commit()
    return db_itempedido


def delete_itempedido(db: Session, idPedido: int):
    db_itempedido =  db.query(models.ItemPedido).filter(models.ItemPedido.idPedido == idPedido).delete(synchronize_session="evaluate")
    # db.delete(db_itempedido)
    db.commit()
    return db_itempedido