from config import db
from models.usuarios_model import Usuarios


def cadastrar(usuario: Usuarios):

    # db.session.execute(db.select(Usuarios).where(Usuarios.email == usuario.email)).scalars()

    db.session.add(usuario)
    db.session.commit()

    return usuario

def buscar_por_email(email: str):
    db.session.query(Usuarios).filter(Usuarios.email == email).all()
