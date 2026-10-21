from concurrent.futures import ThreadPoolExecutor
from flask import Blueprint, request, render_template, jsonify
from flask_login import login_required, current_user

from services.pricematch_service import get_livros
from repositories import favorito_DAO

livro_controller = Blueprint('livro', __name__)


@livro_controller.route('/', methods=['GET'])
@login_required
def buscar():
    titulo = request.args.get("titulo", "").strip()

    contexto = {"favoritos": favorito_DAO.titulos_do_usuario(current_user.id)}
    if titulo:
        contexto["livros"] = get_livros(titulo)

    return render_template("busca_livro.html", **contexto)


@livro_controller.route('/favoritar', methods=['POST'])
@login_required
def favoritar():
    dados = request.get_json(silent=True) or {}
    titulo = (dados.get("titulo") or "").strip()

    if not titulo:
        return jsonify(erro="Título obrigatório"), 400

    favorito = favorito_DAO.alternar(
        current_user.id,
        titulo,
        dados.get("imagem") or None
    )
    return jsonify(favorito=favorito)


@livro_controller.route('/adicionados')
@login_required
def adicionados():
    favs = favorito_DAO.buscar_por_usuario(current_user.id)

    def carregar(fav):
        for r in get_livros(fav.titulo):
            if (r["titulo"] or "").strip().lower() == fav.titulo.strip().lower():
                return r
        return {"titulo": fav.titulo, "imagem": fav.imagem,
                "lojas": [], "preco_minimo": None}

    with ThreadPoolExecutor(max_workers=5) as ex:
        livros = list(ex.map(carregar, favs))

    return render_template("perfil.html", livros=livros)