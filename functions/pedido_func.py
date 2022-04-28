from typing import Optional
from sqlalchemy.orm import Session

import models, schemas


def post_pedido(db: Session, pedido: schemas.Pedido):
    db_ped = models.Pedido(codPedido = pedido.codPedido, transportadora = pedido.transportadora, redespacho = pedido.redespacho, tpFrete = pedido.tpFrete,
obsPedido = pedido.obsPedido, obsFiscal = pedido.obsFiscal, condPagamento = pedido.condPagamento, vlTotal = pedido.vlTotal, idCliente = pedido.idCliente, idMarca = pedido.idMarca,
idFilial = pedido.idFilial, idUsuario = pedido.idUsuario, dtEmissao = pedido.dtEmissao, dtVencimento = pedido.dtVencimento, ativo = pedido.ativo, status = pedido.status)
    db.add(db_ped)
    db.commit()
    db.refresh(db_ped)
    return db_ped


# id_Marca ou id_Cliente verificar !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def post_pedido_idfilial_idUsuario(db: Session, idFilial: int, idUsuario: int):
    db_ped = models.Pedido(codPedido = "", transportadora = "", redespacho = "", tpFrete = "", obsPedido = "", obsFiscal = "", condPagamento = "", vlTotal = 0, idCliente = 1, idMarca = 1,
idFilial = idFilial, idUsuario = idUsuario, dtEmissao = "", dtVencimento = "", ativo = 1, status = 1)
    db.add(db_ped)
    db.commit()
    db.refresh(db_ped)
    return db_ped


def get_pedido(db: Session, skip: Optional[int] = None, limit: Optional[int] = None, filter: Optional[str]= "idPedido" ):
    return db.query(models.Pedido).order_by(filter).offset(skip).limit(limit).all()


def get_pedido_idPedido(db: Session, idPedido: int):
    return db.query(models.Pedido).filter(models.Pedido.idPedido == idPedido).all()


def get_pedido_idPedido_carrinho(db: Session, idPedido: int):
    return db.query(models.Pedido).filter(models.Pedido.idPedido == idPedido, models.Pedido.ativo == 1).first()


def get_pedido_codPedido(db: Session, codPedido: str):
    return db.query(models.Pedido).filter(models.Pedido.codPedido == codPedido).first()


def get_pedido_idFilial(db: Session, idFilial: int, skip: Optional[int] = 0, limit: Optional[int] = None, filter: Optional[str]= "idPedido"):
    return db.query(models.Pedido).filter(models.Pedido.idFilial == idFilial).order_by(filter).offset(skip).limit(limit).all()


def get_pedido_idUsuario(db: Session, idUsuario: int, skip: Optional[int] = 0, limit: Optional[int] = None, filter: Optional[str]= "idPedido"):
    return db.query(models.Pedido).filter(models.Pedido.idUsuario == idUsuario).order_by(filter).offset(skip).limit(limit).all()


def get_pedido_idFilial_idUsuario(db: Session, idUsuario: int, idFilial: int, skip: Optional[int] = 0, limit: Optional[int] = None, filter: Optional[str]= "idPedido"):
    return db.query(models.Pedido).filter(models.Pedido.idFilial == idFilial, models.Pedido.idUsuario == idUsuario).order_by(filter).offset(skip).limit(limit).all()


def put_pedido_idPedido(db: Session, idPedido: int, pedido: schemas.Pedido):
    db_ped =  db.query(models.Pedido).filter(models.Pedido.idPedido == idPedido).first()

    db_ped.codPedido = pedido.codPedido
    db_ped.transportadora = pedido.transportadora
    db_ped.redespacho = pedido.redespacho
    db_ped.tpFrete = pedido.tpFrete
    db_ped.obsPedido = pedido.obsPedido
    db_ped.obsFiscal = pedido.obsFiscal
    db_ped.condPagamento = pedido.condPagamento
    db_ped.vlTotal = pedido.vlTotal
    db_ped.idCliente = pedido.idCliente
    db_ped.idMarca = pedido.idMarca
    db_ped.idFilial = pedido.idFilial
    db_ped.idUsuario = pedido.idUsuario
    db_ped.dtEmissao = pedido.dtEmissao
    db_ped.dtVencimento = pedido.dtVencimento
    db_ped.ativo = pedido.ativo
    db_ped.status = pedido.status

    db.add(db_ped)
    db.commit()
    db.refresh(db_ped)
    return db_ped


def delete_pedido_idPedido(db: Session, idPedido: int):
    db_ped =  db.query(models.Pedido).filter(models.Pedido.idPedido == idPedido).first()
    db.delete(db_ped)
    db.commit()
    return db_ped