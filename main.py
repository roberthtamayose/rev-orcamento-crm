from fastapi import FastAPI, Depends
from controllers.auth.authbearer import JWTBearer
# from .authbearer import JWTBearer


from controllers.transportadora.transportadora import router_transportadoras
from controllers.filial.filial import router_filiais
from controllers.condpagamento.condpagamento import router_condpagamento
from controllers.cliente.cliente import router_cliente
from controllers.usuario.usuario import router_usuario
from controllers.vendedor.vendedor import router_vendedor
from controllers.disponibilidade.disponibilidade import router_disponibilidade
from controllers.pedido.pedido import router_pedido
from controllers.itempedido.itempedido import router_itempedido
from controllers.auth.auth import router_auth






app = FastAPI()

app.include_router(router_transportadoras,prefix="/transportadoras", dependencies=[Depends(JWTBearer())], tags=["transportadoras"])
app.include_router(router_filiais,prefix="/filiais", dependencies=[Depends(JWTBearer())], tags=["filiais"])
app.include_router(router_condpagamento,prefix="/condpagamentos", dependencies=[Depends(JWTBearer())], tags=["condpagamentos"])
app.include_router(router_cliente,prefix="/clientes", dependencies=[Depends(JWTBearer())], tags=["clientes"])
app.include_router(router_usuario,prefix="/usuarios", dependencies=[Depends(JWTBearer())], tags=["usuarios"])
app.include_router(router_vendedor,prefix="/vendedores", dependencies=[Depends(JWTBearer())], tags=["vendedores"])
app.include_router(router_disponibilidade,prefix="/disponibilidades", dependencies=[Depends(JWTBearer())], tags=["disponibilidades"])
app.include_router(router_pedido,prefix="/pedidos", dependencies=[Depends(JWTBearer())], tags=["pedidos"])
app.include_router(router_itempedido,prefix="/itempedidos", dependencies=[Depends(JWTBearer())], tags=["itempedidos"])
app.include_router(router_auth,prefix="/auth", tags=["auth"])








