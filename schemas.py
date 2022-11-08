from datetime import date
from typing import List, Optional
from pydantic import BaseModel





class Filial(BaseModel):
   idFilial: Optional[int] = None
   codFilial: str
   nmFilial: str

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
      
class Estoque(BaseModel):
   id: Optional[int] = None
   filial: str
   codProd: str
   colecao: str
   quantidade: float
   ativo: str

   class Config:
      orm_mode = True

class Produto(BaseModel):
   id: Optional[int] = None
   filial: str
   codProd: str
   nomeProd: str
   colecao: str
   ativo: str

   class Config:
      orm_mode = True



# ----------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------


class Transportadora(BaseModel):
   id: Optional[int] = None
   codTransp: str
   nomeTransp: str
   ativo: str 

   class Config:
      orm_mode = True


class CondPagamento(BaseModel):
   id: Optional[int] = None
   codCondPag: str
   nomeCondPag: str
   ativo: str

   class Config:
      orm_mode = True


class Cliente(BaseModel):
   id: Optional[int] = None
   codCliente: str
   nomeCliente: str
   emailCliente: str
   # vend_id: int
   ativo: str

   class Config:
         orm_mode = True


class Vendedor(BaseModel):
   id: Optional[int] = None
   codVend: str
   nomeVend: str
   user_id: int
   ativo: str
   
   class Config:
         orm_mode = True


class VendedorCliente(BaseModel):
   id: Optional[int] = None
   codVend: str
   nomeVend: str
   user_id: int
   ativo: str
   cliente: List[Cliente]

   class Config:
         orm_mode = True


class VendedorUser(BaseModel):
   id: Optional[int] = None
   codVend: str
   nomeVend: str
   ativo: str

   class Config:
         orm_mode = True


class Usuario(BaseModel):
   id: Optional[int] = None
   codUser: str
   nome: str
   email: str
   senha: Optional[str] = None
   adm: str
   ativo: str

   class Config:
         orm_mode = True



class UsuarioVend(BaseModel):
   id: Optional[int] = None
   codUser: str
   nome: str
   email: str
   senha: Optional[str] = None
   adm: str
   ativo: str
   vend: List[VendedorUser]

   class Config:
         orm_mode = True

class OrcamentoPost(BaseModel):
   id: Optional[int] = None
   filial: str
   numOrc: str
   numRevisao: str
   status: str
   cliente_id: int
   vend_id: int
   condPag_id: int
   transp_id: int
   ativo: str

   class Config:
         orm_mode = True


class ItemOrcamentoGet(BaseModel):
   id: Optional[int] = None
   filial: str
   quantidade: float
   preco: float
   produto: Produto
   ativo: str

   class Config:
         orm_mode = True


class OrcamentoMaxNum(BaseModel):
   numOrc: str
   
   class Config:
         orm_mode = True


class Orcamento(BaseModel):
   id: Optional[int] = None
   filial: str
   numOrc: str
   numRevisao: str
   status: str
   cliente: Cliente
   vendedor: Vendedor
   condPagamento: CondPagamento
   transportadora: Transportadora
   item: List[ItemOrcamentoGet]
   ativo: str
   

   class Config:
         orm_mode = True


class OrcamentoPitem(BaseModel):
   id: Optional[int] = None
   filial: str
   numOrc: str
   numRevisao: str
   status: str
   ativo: str
   

   class Config:
         orm_mode = True


class ItemOrcamentoPost(BaseModel):
   id: Optional[int] = None
   filial: str
   quantidade: float
   preco: float
   orc_id: int
   prod_id: int
   ativo: str

   class Config:
         orm_mode = True


class ItemOrcamento(BaseModel):
   id: Optional[int] = None
   filial: str
   quantidade: float
   preco: float
   orcamento: Orcamento
   produto: Produto
   ativo: str

   class Config:
         orm_mode = True


class Filial(BaseModel):
   id: Optional[int] = None
   codFilial: str
   nomeFilial: str

   class Config:
      orm_mode = True


class OrcamentoPost1(BaseModel):
   id: Optional[int] = None
   filial: str
   numOrc: str
   numRevisao: str
   status: str
   cliente_id: int
   vend_id: int
   condPag_id: int
   transp_id: int
   ativo: str
   itemOrcamento: List[ItemOrcamentoPost]

   class Config:
         orm_mode = True
