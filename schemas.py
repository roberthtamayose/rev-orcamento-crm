from datetime import date
from typing import List, Optional

from pydantic import BaseModel


class Transportadora(BaseModel):
   idTransp: Optional[int] = None
   idErpTransp: str
   nmTransp: str
   ativo: int 

   class Config:
      orm_mode = True


class Filial(BaseModel):
   idFilial: Optional[int] = None
   codFilial: str
   nmFilial: str

   class Config:
      orm_mode = True


class CondPagamento(BaseModel):
   idCondPag: Optional[int] = None
   idErpCondPag: str
   nmCondPag: str
   ativo: int

   class Config:
      orm_mode = True


class Cliente(BaseModel):
   idCliente: Optional[int] = None
   idErpCliente: str
   nmCliente: str
   emailCliente: str
   tpCliente: Optional[str]
   limiteCredito:	Optional[float]
   idVendedor: int
   ativo: int

   class Config:
         orm_mode = True


class Usuario(BaseModel):
   idUsuario: Optional[int] = None
   idErpUser: str
   nmUsuario: str
   sobrenomeUsuario: str
   emailUsuario: str
   senhaUsuario: str
   ativo: int
   nivel: int

   class Config:
         orm_mode = True


class Vendedor(BaseModel):
   idVendedor: int
   IdErpUser: str
   idUsuario: int

   class Config:
         orm_mode = True


class Produto(BaseModel):
   # filial: Optional[int]
   codProduto: str
   nmProduto: str
   colecao: Optional[str]
   qtdEstoque: Optional[float]

   class Config:
      orm_mode = True


class Cores(BaseModel):
   # idFilia:	int
   codProduto: str
   nmProduto: str
   idProduto:	int
   colecao: Optional[str]
   qtdEstoque: Optional[str]

   class Config:
      orm_mode = True


class Colecoes(BaseModel):
   colecoes: str

   class Config:
      orm_mode = True


class Pedido(BaseModel):
   idPedido: Optional[int] = None
   codPedido: Optional[str] = None
   transportadora: str
   redespacho: Optional[str] = None
   tpFrete: str
   obsPedido: str
   obsFiscal: Optional[str] = None
   condPagamento: str
   vlTotal: float
   idCliente: int
   idMarca: int
   idFilial: int
   idUsuario: int
   dtEmissao: Optional[date] = None      ##ajuste p/ data
   dtVencimento: Optional[str] = None      ##ajuste p/ data
   ativo: int
   status: str

   class Config:
      orm_mode = True


class ItemPedido(BaseModel):
   idItem: Optional[int] = None
   codProduto: str
   nmProduto: str
   idErpColecao: str
   vlUnitario: float
   vlDesconto: float
   vlTotal: float
   qtdItem: float
   idPedido: Optional[int] = None

   class Config:
      orm_mode = True