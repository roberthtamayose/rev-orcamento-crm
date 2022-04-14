from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base


class Transportadora(Base):
   __tablename__ = "tb_transportadoras"

   idTransp = Column(Integer, primary_key=True, index=True)
   idErpTransp = Column(String)
   nmTransp = Column(String)
   ativo = Column(Integer)


class Filial(Base):
   __tablename__ = "tb_filiais"
   
   idFilial = Column(Integer, primary_key=True, index=True)
   codFilial = Column(String)
   nmFilial = Column(String)


class CondPagamento(Base):
   __tablename__ = "tb_condpagamento"
   
   idCondPag = Column(Integer, primary_key=True, index=True)
   idErpCondPag = Column(String)
   nmCondPag = Column(String)
   ativo = Column(Integer)


class Config:
      orm_mode = True


class Cliente(Base):
   __tablename__ = "tb_clientes"

   idCliente = Column(Integer, primary_key=True, index=True)
   idErpCliente = Column(String)
   nmCliente = Column(String)
   emailCliente = Column(String)
   tpCliente = Column(String)
   limiteCredito=	Column(Float)
   idVendedor = Column(Integer)
   ativo = Column(Integer)


class Usuario(Base):
   __tablename__ = "tb_usuarios"

   idUsuario = Column(Integer, primary_key=True, index=True)
   idErpUser = Column(String)
   nmUsuario = Column(String)
   sobrenomeUsuario = Column(String)
   emailUsuario = Column(String)
   senhaUsuario = Column(String)
   ativo = Column(Integer)
   nivel = Column(Integer)


class Vendedor(Base):
   __tablename__ = "tb_vendedores"

   idVendedor = Column(Integer, primary_key=True, index=True)
   IdErpUser = Column(String)
   idUsuario = Column(Integer)


# class Produtos(Base):
#    __tablename__ = "API_Produtos"

#    filial = Column(Integer)
#    codProduto = Column(String)
#    nmProduto = Column(String)
#    colecao = Column(String)
#    qtdEstoque = Column(Float)



# class Cores(BaseModel):
#    idFilial:	int
#    codProduto: str
#    idProduto:	int
#    colecao:	str
#    qtdEstoque:	str


# class Colecoes(BaseModel):
#    colecoes: str

class Pedido(Base):
   __tablename__ = "tb_pedidos"

   idPedido	= Column(Integer, primary_key=True, index=True)
   codPedido = Column(String)
   transportadora = Column(String)
   redespacho = Column(String)
   tpFrete = Column(String)
   obsPedido = Column(String)
   obsFiscal = Column(String)
   condPagamento = Column(String)
   vlTotal = Column(Float)
   idCliente = Column(Integer)
   idMarca = Column(Integer)
   idFilial = Column(Integer)
   idUsuario = Column(Integer)
   dtEmissao = Column(String)
   dtVencimento = Column(String)
   ativo = Column(Integer)
   status = Column(String)


class ItemPedido(Base):
   __tablename__ = "tb_itens_pedido"

   idItem = Column(Integer, primary_key=True, index=True)
   codProduto = Column(String)
   nmProduto = Column(String)
   idErpColecao = Column(String)
   vlUnitario = Column(Float)
   vlDesconto = Column(Float)
   vlTotal = Column(Float)
   qtdItem = Column(Float)
   idPedido = Column(Integer)



class Preco(Base):
   __tablename__ = "tb_preco"

   idPreco = Column(Integer, primary_key=True, index=True)
   codTab = Column(String)
   codProduto = Column(String)
   prc = Column(Float)
   ipi = Column(Float)
   prcIpi = Column(Float)
   prcRevenda = Column(Float)
   prcFinal = Column(Float)
   qtdMinima = Column(Float)
   ativo = Column(Integer)