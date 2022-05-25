from asyncio.windows_events import NULL
from typing import Optional
from fastapi import Query
from sqlalchemy.sql import text
from sqlalchemy.orm import Session

import models, schemas


def get_disponibilidade_produto(db: Session, skip: Optional[int] = None, limit: Optional[int] = None, filter: list[str] | None = Query(None), filial: Optional[int] = 1 ):
    order = ','.join([str(i) for i in filter]) if filter else 'nmProduto'
    if limit:
        sql =  text(f"select codProduto, nmProduto, colecao, qtdEstoque from API_Produtos where filial={filial} ORDER BY {order} OFFSET ({skip}) ROWS FETCH NEXT {limit} ROWS ONLY")
    else:
        sql =  text(f"select codProduto, nmProduto, colecao, qtdEstoque from API_Produtos where filial={filial} ORDER BY {order}")
    db_Disp = db.execute(sql)
    result = db_Disp.mappings().all()
    return result


def get_disponibilidade_cor(db: Session, skip: Optional[int] = None, limit: Optional[int] = None, prod: Optional[str] = None, filter: list[str] | None = Query(None), filial: Optional[int] = 1 ):
    order = ','.join([str(i) for i in filter]) if filter else 'nmProduto'
    def tprod(prod):
        if prod is None:
            return ''
        return prod
    if limit:
        sql =  text(f"select codProduto, nmProduto, idProduto, colecao, qtdEstoque from API_Cores WHERE idFilial = {filial} AND codProduto LIKE '%{tprod(prod)}%' ORDER BY {order} OFFSET ({skip}) ROWS FETCH NEXT {limit} ROWS ONLY")
    else:
        sql =  text(f"select codProduto, nmProduto, idProduto, colecao, qtdEstoque from API_Cores WHERE idFilial = {filial} AND codProduto LIKE '%{tprod(prod)}%' ORDER BY {order}")
    db_Disp = db.execute(sql)
    result = db_Disp.mappings().all()
    return result


def get_disponibilidade_colecao(db: Session):
    db_Disp = db.execute("SELECT * from API_Colecoes")
    result = db_Disp.mappings().all()
    return result