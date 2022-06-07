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
   senhaUsuario: Optional[str] = None
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
   transportadora: Optional[str] = None
   redespacho: Optional[str] = None
   tpFrete: Optional[str] = None
   obsPedido: Optional[str] = None
   obsFiscal: Optional[str] = None
   condPagamento: Optional[str] = None
   vlTotal: Optional[float] = None
   idCliente: Optional[int] = None
   idMarca: Optional[int] = None
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


class Preco(BaseModel):
   idPreco: Optional[int] = None
   codTab: str
   codProduto: str
   prc: float
   ipi: float
   prcIpi: float
   prcRevenda: float
   prcFinal: float
   qtdMinima: float
   ativo: int

   class Config:
      orm_mode = True