from typing import Optional
from sqlalchemy.orm import Session
from fastapi import Query
from sqlalchemy.sql import text
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
idFilial = idFilial, idUsuario = idUsuario, dtEmissao = "", dtVencimento = "", ativo = 1, status = 0)
    db.add(db_ped)
    db.commit()
    db.refresh(db_ped)
    return db_ped


def get_pedido(db: Session, skip: Optional[int] = None, limit: Optional[int] = None, filter: list[str] | None = Query(None) ):
    order = ','.join([str(i) for i in filter]) if filter else 'idPedido'
    return db.query(models.Pedido).order_by(text(order)).offset(skip).limit(limit).all()


def get_pedido_idPedido_carrinho(db: Session, filial: int, idUsuario: int, idPedido: Optional[int] = None):
    if idPedido:
        return db.query(models.Pedido).filter(models.Pedido.idFilial == filial, models.Pedido.idPedido == idPedido, models.Pedido.idUsuario == idUsuario).first()
    else:
        return db.query(models.Pedido).filter(models.Pedido.idFilial == filial, models.Pedido.ativo == 1, models.Pedido.status == 0, models.Pedido.idUsuario == idUsuario).first()


def get_pedido_idPedido(db: Session, idPedido: int):
    return db.query(models.Pedido).filter(models.Pedido.idPedido == idPedido).all()


def get_pedido_codPedido(db: Session, codPedido: str):
    return db.query(models.Pedido).filter(models.Pedido.codPedido == codPedido).first()


# idFilial, idPedido, idUsuario, idCliente, ativo, status,
def get_pedido_allParam(db: Session, idFilial: Optional[int] = None, idPedido: Optional[int] = None, idUsuario: Optional[int] = None, idCliente: Optional[int] = None, ativo: Optional[int] = None, status: Optional[str] = None, skip: Optional[int] = 0, limit: Optional[int] = None, filter: list[str] | None = Query(None)):
    order = ','.join([str(i) for i in filter]) if filter else 'idPedido'
    listParamOrig = list(locals().items())
    listParamFinal=[]
    for key, value in listParamOrig[1:-4]:
        if value:
            listParamFinal.append(f"{key} = {value}")
    makeitastring = ' and '.join(map(str, listParamFinal))
    return db.query(models.Pedido).filter(text(makeitastring)).order_by(text(order)).offset(skip).limit(limit).all()


def put_pedido_idPedido(db: Session, idPedido: int, pedido: schemas.Pedido):
    db_ped =  db.query(models.Pedido).filter(models.Pedido.idPedido == idPedido).first()

    db_ped.codPedido = pedido.codPedido or db_ped.codPedido
    db_ped.transportadora = pedido.transportadora or db_ped.transportadora
    db_ped.redespacho = pedido.redespacho or db_ped.redespacho
    db_ped.tpFrete = pedido.tpFrete or db_ped.tpFrete
    db_ped.obsPedido = pedido.obsPedido or db_ped.obsPedido
    db_ped.obsFiscal = pedido.obsFiscal or db_ped.obsFiscal
    db_ped.condPagamento = pedido.condPagamento or db_ped.condPagamento
    db_ped.vlTotal = pedido.vlTotal or db_ped.vlTotal
    db_ped.idCliente = pedido.idCliente or db_ped.idCliente
    db_ped.idMarca = pedido.idMarca or db_ped.idMarca
    db_ped.idFilial = pedido.idFilial or db_ped.idFilial
    db_ped.idUsuario = pedido.idUsuario or db_ped.idUsuario
    db_ped.dtEmissao = pedido.dtEmissao or db_ped.dtEmissao
    db_ped.dtVencimento = pedido.dtVencimento or db_ped.dtVencimento
    db_ped.ativo = pedido.ativo or db_ped.ativo
    db_ped.status = pedido.status or db_ped.status

    db.add(db_ped)
    db.commit()
    db.refresh(db_ped)
    return db_ped


def delete_pedido_idPedido(db: Session, idPedido: int):
    db_ped =  db.query(models.Pedido).filter(models.Pedido.idPedido == idPedido).first()
    db.delete(db_ped)
    db.commit()
    return db_ped