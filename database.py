from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import urllib

from decouple import config
JWT_SERVER = config("server")

params = urllib.parse.quote_plus(JWT_SERVER)

engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()