
import uvicorn
from fastapi import Body, Depends, APIRouter
from sqlalchemy.orm import Session


import functions.usuario_func  as usuario_func 
from .models import UserLoginSchema
# from .authbearer import JWTBearer
from .auth_handler import signJWT
from database import SessionLocal, engine

# models.Base.metadata.create_all(bind=engine)


router_auth = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



def check_user(data, db):
    user = usuario_func.get_usuario_emailUsuario(db, data.email)
    if user:
        if data.email == user.emailUsuario and data.password == user.senhaUsuario:
            return True
    return False

@router_auth.post("/login")
def user_login(user: UserLoginSchema = Body(...), db: Session = Depends(get_db)):
    if check_user(user, db):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }