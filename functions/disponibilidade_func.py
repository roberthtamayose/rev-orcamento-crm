from asyncio.windows_events import NULL
from typing import Optional
from sqlalchemy.sql import text
from sqlalchemy.orm import Session

import models, schemas


def get_disponibilidade_produto(db: Session, skip: Optional[int] = 0, limit: Optional[int] = None, filter: Optional[str]= "nmProduto", filial: Optional[int] = 1 ):
    sql =  text(f"select codProduto, nmProduto, colecao, qtdEstoque from API_Produtos where filial={filial} ORDER BY {filter} OFFSET ({skip}) ROWS FETCH NEXT {limit} ROWS ONLY")
    db_Disp = db.execute(sql)
    result = db_Disp.mappings().all()
    return result


def get_disponibilidade_cor(db: Session, skip: Optional[int] = 0, limit: Optional[int] = None, prod: Optional[str] = None, filter: Optional[str] = "nmProduto", filial: Optional[int] = 1 ):
    def tprod(prod):
        if prod is None:
            return ''
        return prod
    sql =  text(f"select codProduto, nmProduto, idProduto, colecao, qtdEstoque from API_Cores WHERE idFilial = {filial} AND codProduto LIKE '%{tprod(prod)}%' ORDER BY {filter} OFFSET ({skip}) ROWS FETCH NEXT {limit} ROWS ONLY")
    print ("sql....",sql)
    db_Disp = db.execute(sql)
    result = db_Disp.mappings().all()
    return result


def get_disponibilidade_colecao(db: Session):
    db_Disp = db.execute("SELECT * from API_Colecoes")
    result = db_Disp.mappings().all()
    return result