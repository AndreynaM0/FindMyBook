from config import db
from models.favoritos_model import Favoritos


def buscar_por_usuario(usuario_id: int) -> list[Favoritos]:
    return db.session.execute(
        db.select(Favoritos)
        .filter_by(usuario_id=usuario_id)
        .order_by(Favoritos.criado_em.desc())
    ).scalars().all()


def titulos_do_usuario(usuario_id: int) -> set[str]:
    return {f.titulo for f in buscar_por_usuario(usuario_id)}


def alternar(usuario_id: int, titulo: str, imagem: str | None) -> bool:

    existente = db.session.execute(
        db.select(Favoritos).filter_by(usuario_id=usuario_id, titulo=titulo)
    ).scalar_one_or_none()

    if existente:
        db.session.delete(existente)
        db.session.commit()
        return False

    db.session.add(Favoritos(usuario_id=usuario_id, titulo=titulo, imagem=imagem))
    db.session.commit()
    return True