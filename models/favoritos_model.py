from config import db


class Favoritos(db.Model):
    __tablename__ = "favoritos"

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey("usuarios.id", ondelete="CASCADE"),
        nullable=False
    )
    titulo = db.Column(db.Text, nullable=False)
    imagem = db.Column(db.Text)
    criado_em = db.Column(db.DateTime, server_default=db.func.now())

    __table_args__ = (
        db.UniqueConstraint("usuario_id", "titulo", name="uq_favorito_usuario_titulo"),
    )