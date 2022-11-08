from tkinter.tix import INTEGER
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, VARBINARY
from sqlalchemy.orm import relationship

from database import Base


# class Config:
#       orm_mode = True







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
   __tablename__ = "tb_itens_pedidos"

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

# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------


class Produto(Base):
   __tablename__ = "TB_PRODUTOS"

   id = Column(Integer, primary_key=True, index=True)
   filial = Column(String)
   codProd = Column(String)
   nomeProd = Column(String)
   colecao = Column(String)
   ativo = Column(String)
   cor_id = Column (Integer, ForeignKey('TB_CORES.id'))
   estoque = relationship("Estoque", backref  = "TB_PRODUTOS")
   cores = relationship("Cor", backref  = "TB_PRODUTOS")


class Estoque(Base):
   __tablename__ = "TB_ESTOQUES"

   id = Column(Integer, primary_key=True, index=True)
   filial = Column(String)
   codProd = Column(String)
   colecao = Column(String)
   quantidade = Column(Float)
   prod_id = Column (Integer, ForeignKey('TB_PRODUTOS.id'))
   ativo = Column(String)
   
class Cor(Base):
   __tablename__ = "TB_CORES"

   id = Column(Integer, primary_key=True, index=True)
   codCor = Column(String)
   nomeCor = Column(String)
   ativo = Column(String)

##Produto.TB_ESTOQUES = relationship("Estoque", order_by = Estoque.prod_id, back_populates = "TB_PRODUTOS")



class CondPagamento(Base):
   __tablename__ = "TB_CONDPAG"
   
   id = Column(Integer, primary_key=True, index=True)
   codCondPag = Column(String)
   nomeCondPag = Column(String)
   ativo = Column(String)


class Transportadora(Base):
   __tablename__ = "TB_TRANSPORTADORAS"

   id = Column(Integer, primary_key=True, index=True)
   codTransp = Column(String)
   nomeTransp = Column(String)
   ativo = Column(String)


class Usuario(Base):
   __tablename__ = "TB_USUARIOS"

   id = Column(Integer, primary_key=True, index=True)
   codUser = Column(String)
   nome = Column(String)
   email = Column(String)
   senha = Column(VARBINARY)
   adm = Column(String)
   ativo = Column(String)
   vend = relationship("Vendedor", backref  = "TB_USUARIOS")


class Vendedor(Base):
   __tablename__ = "TB_VENDEDORES"

   id = Column(Integer, primary_key=True, index=True)
   codVend = Column(String)
   nomeVend = Column(String)
   user_id = Column (Integer, ForeignKey('TB_USUARIOS.id'))
   ativo = Column(String)
   cliente =  relationship("Cliente", backref  = "TB_VENDEDORES")


class Cliente(Base):
   __tablename__ = "TB_CLIENTES"

   id = Column(Integer, primary_key=True, index=True)
   codCliente = Column(String)
   nomeCliente = Column(String)
   emailCliente = Column(String)
   vend_id = Column (Integer, ForeignKey('TB_VENDEDORES.id'))
   ativo = Column(String)





class ItemOrcamento(Base):
   __tablename__ = "TB_ITENS_ORCAMENTOS"

   id	= Column(Integer, primary_key=True, index=True)
   filial = Column(String)
   quantidade = Column(Float)
   preco = Column(Float)
   orc_id = Column (Integer, ForeignKey('TB_ORCAMENTOS.id'))
   prod_id = Column (Integer, ForeignKey('TB_PRODUTOS.id'))
   ativo = Column(String)
   produto = relationship("Produto", backref  = "TB_ITENS_ORCAMENTOS")
   orcamento = relationship("Orcamento", backref  = "TB_ITENS_ORCAMENTOS")


class Orcamento(Base):
   __tablename__ = "TB_ORCAMENTOS"

   id	= Column(Integer, primary_key=True, index=True)
   filial = Column(String)
   numOrc = Column(String)
   numRevisao = Column(String)
   status = Column(String)
   cliente_id = Column (Integer, ForeignKey('TB_CLIENTES.id'))
   vend_id = Column (Integer, ForeignKey('TB_VENDEDORES.id'))
   condPag_id = Column (Integer, ForeignKey('TB_CONDPAG.id'))
   transp_id = Column (Integer, ForeignKey('TB_TRANSPORTADORAS.id'))
   ativo = Column(String)
   cliente = relationship("Cliente", backref  = "TB_ORCAMENTOS")
   vendedor = relationship("Vendedor", backref  = "TB_ORCAMENTOS")
   condPagamento = relationship("CondPagamento", backref  = "TB_ORCAMENTOS")
   transportadora = relationship("Transportadora", backref  = "TB_ORCAMENTOS")
   item = relationship("ItemOrcamento", backref  = "TB_ORCAMENTOS")


class Filial(Base):
   __tablename__ = "TB_FILIAIS"
   
   id = Column(Integer, primary_key=True, index=True)
   codFilial = Column(String)
   nomeFilial = Column(String)