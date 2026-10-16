from config import db
from models.usuarios_model import Usuarios


def cadastrar(usuario: Usuarios):

    # db.session.execute(db.select(Usuarios).where(Usuarios.email == usuario.email)).scalars()

    db.session.add(usuario)
    db.session.commit()

    return usuario