from typing import Optional
from sqlalchemy.sql import text
from sqlalchemy.orm import Session

import models, schemas


def get_disponibilidade_produto(db: Session, skip: Optional[int] = None, limit: Optional[int] = None, filter: Optional[str]= "nmProduto", filial: Optional[int] = None ):
    sql =  text(f"select codProduto, nmProduto, colecao, qtdEstoque from API_Produtos where filial={filial} ORDER BY {filter} OFFSET ({skip}) ROWS FETCH NEXT {limit} ROWS ONLY")
    result = db.execute(sql)
   #  print ("db_prod.......",db_prod)
    return result

   #  query = f'select codProduto, nmProduto, colecao, qtdEstoque from API_Produtos where filial={filial} ORDER BY 1,2 OFFSET (20*{page}-20) ROWS FETCH NEXT 20 ROWS ONLY'


# def get_condpagamento_idCondPag(db: Session, idCondPag: int):
#     return db.query(models.CondPagamento).filter(models.CondPagamento.idCondPag == idCondPag).first()


# def get_condpagamento_idErpCondPag(db: Session, idErpCondPag: str):
#     return db.query(models.CondPagamento).filter(models.CondPagamento.idErpCondPag == idErpCondPag).first()