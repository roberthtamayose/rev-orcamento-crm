from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import urllib

params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};SERVER=10.111.70.1;DATABASE=PEDIDOS_NS;UID=pedidos;PWD=Pedidos@2022")

engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()