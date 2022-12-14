from asyncio.windows_events import NULL
from typing import Optional
from fastapi import Query
from sqlalchemy.sql import text
from sqlalchemy.orm import Session

import models, schemas


# def get_disponibilidade_produto(db: Session, filial: Optional[int] = 1, codProduto: Optional[str] = None, nmProduto: Optional[str] = None, skip: Optional[int] = None, limit: Optional[int] = None, filter: list[str] | None = Query(None)):
#     order = ','.join([str(i) for i in filter]) if filter else 'nmProduto'

#     listParamOrig = list(locals().items())   #get params dict
#     aux=[]
#     for key, value in listParamOrig[1:4]:
#         if value:
#             if(key == 'nmProduto'):
#                 aux.append(f"{key} like '%{value}%'")
#             else:
#                 aux.append(f"{key} = '{value}'")
#     listParamFinal = ' and '.join(map(str, aux))
#     if limit:
#         sql =  text(f"select codProduto, nmProduto, colecao, qtdEstoque from API_Produtos where {listParamFinal} ORDER BY {order} OFFSET ({skip}) ROWS FETCH NEXT {limit} ROWS ONLY")
#     else:
#         sql =  text(f"select codProduto, nmProduto, colecao, qtdEstoque from API_Produtos where {listParamFinal} ORDER BY {order}")
#     db_Disp = db.execute(sql)
#     result = db_Disp.mappings().all()
#     return result

def get_disponibilidade_produto(db: Session, skip: Optional[int] = None, limit: Optional[int] = None, filter: list[str] | None = Query(None) ): 
    order = ','.join([str(i) for i in filter]) if filter else 'nmProduto'
    return db.query(models.Produto).order_by(text(order)).offset(skip).limit(limit).all()


def get_disponibilidade_produto_codProduto(db: Session, codProduto: str):
    return db.query(models.Produto).filter(models.Produto.codProduto == codProduto).all()


def get_disponibilidade_estoque_codProduto(db: Session, idFilial: int, codProduto: str):
    return db.query(models.Estoque).filter(models.Estoque.idFilial == idFilial, models.Estoque.codProduto.like(f'%{codProduto}%')).all()


# def get_disponibilidade_cor(db: Session, skip: Optional[int] = None, limit: Optional[int] = None, prod: Optional[str] = None, filter: list[str] | None = Query(None), filial: Optional[int] = 1 ):
#     order = ','.join([str(i) for i in filter]) if filter else 'nmProduto'
#     def tprod(prod):
#         if prod is None:
#             return ''
#         return prod
#     if limit:
#         sql =  text(f"select codProduto, nmProduto, idProduto, colecao, qtdEstoque from API_Cores WHERE idFilial = {filial} AND codProduto LIKE '%{tprod(prod)}%' ORDER BY {order} OFFSET ({skip}) ROWS FETCH NEXT {limit} ROWS ONLY")
#     else:
#         sql =  text(f"select codProduto, nmProduto, idProduto, colecao, qtdEstoque from API_Cores WHERE idFilial = {filial} AND codProduto LIKE '%{tprod(prod)}%' ORDER BY {order}")
#     db_Disp = db.execute(sql)
#     result = db_Disp.mappings().all()
#     return result


# def get_disponibilidade_colecao(db: Session):
#     db_Disp = db.execute("SELECT * from API_Colecoes")
#     result = db_Disp.mappings().all()
#     return result