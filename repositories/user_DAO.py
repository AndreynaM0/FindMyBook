from config import db
from models.usuarios_model import Usuarios
from sqlalchemy.exc import NoResultFound


def cadastrar(usuario: Usuarios):

    user = buscar_por_email(usuario.email)
    if user is None:
        db.session.add(usuario)
        db.session.commit()
        return usuario
    else:
        return None

def buscar_por_email(email: str) -> Usuarios:

    try:
        user = db.session.execute(db.select(Usuarios).filter_by(email=email)).scalar_one()
        return user
    except NoResultFound:
        return None

