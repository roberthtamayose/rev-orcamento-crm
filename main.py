from fastapi import FastAPI, Depends
from controllers.auth.authbearer import JWTBearer
# # from .authbearer import JWTBearer


from controllers.transportadora.transportadora import router_transportadoras
from controllers.filial.filial import router_filiais
from controllers.condpagamento.condpagamento import router_condpagamento
from controllers.cliente.cliente import router_cliente
from controllers.usuario.usuario import router_usuario
from controllers.vendedor.vendedor import router_vendedor
# from controllers.disponibilidade.disponibilidade import router_disponibilidade
# from controllers.pedido.pedido import router_pedido
# from controllers.itempedido.itempedido import router_itempedido
# from controllers.preco.preco import router_preco
from controllers.estoque.estoque import router_estoque
from controllers.produto.produto import router_produto
from controllers.orcamento.orcamento import router_orcamento
from controllers.itemOrcamento.itemOrcamento import router_itemOrcamento
from controllers.auth.auth import router_auth
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()
origins = [
     "http://localhost:3000",   
     "http://localhost",
     "http://localhost/orcamentos",
           # libera cors
]
app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,           # libera cors
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# dependencies=[Depends(JWTBearer())]

app.include_router(router_transportadoras,prefix="/transportadoras", dependencies=[Depends(JWTBearer())], tags=["transportadoras"])
app.include_router(router_filiais,prefix="/filiais", dependencies=[Depends(JWTBearer())], tags=["filiais"])
app.include_router(router_condpagamento,prefix="/condpagamentos", dependencies=[Depends(JWTBearer())], tags=["condpagamentos"])
app.include_router(router_cliente,prefix="/clientes", dependencies=[Depends(JWTBearer())], tags=["clientes"])
app.include_router(router_usuario,prefix="/usuarios", dependencies=[Depends(JWTBearer())], tags=["usuarios"])
app.include_router(router_vendedor,prefix="/vendedores", dependencies=[Depends(JWTBearer())], tags=["vendedores"])
# app.include_router(router_disponibilidade,prefix="/disponibilidades",  tags=["disponibilidades"])
app.include_router(router_orcamento,prefix="/orcamentos", dependencies=[Depends(JWTBearer())], tags=["orcamento"])
app.include_router(router_itemOrcamento,prefix="/itemOrcamentos", dependencies=[Depends(JWTBearer())], tags=["itemOrcamento"])
# app.include_router(router_itempedido,prefix="/carrinhos",  tags=["Carrinhos"])
# app.include_router(router_preco,prefix="/precos",  tags=["Precos"])
app.include_router(router_estoque,prefix="/estoques", dependencies=[Depends(JWTBearer())], tags=["estoques"])
app.include_router(router_produto,prefix="/produtos", dependencies=[Depends(JWTBearer())], tags=["produtos"])
app.include_router(router_auth,prefix="/auth", tags=["auth"])








