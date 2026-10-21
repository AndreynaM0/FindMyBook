from flask import Blueprint, request, render_template
from flask_login import login_required, current_user
from services.pricematch_service import get_livros

livro_controller = Blueprint('livro', __name__)

@livro_controller.route('/', methods=['GET', 'POST'])
@login_required
def buscar():
    titulo = request.args.get("titulo", "").strip()

    livros = []
    if titulo:
        livros = get_livros(titulo)

    return render_template("busca_livro.html", livros=livros, titulo=titulo)

@livro_controller.route('/adicionados')
@login_required
def adicionados():
    favoritos = []
    return render_template("perfil.html", livros=favoritos)