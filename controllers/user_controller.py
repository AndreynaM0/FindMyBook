from flask import Blueprint, render_template, request
from repositories import user_DAO
from models.usuarios_model import Usuarios

user_controller = Blueprint('usuarios', __name__)
@user_controller.route('/cadastrar', methods=['GET', 'POST'])
def cadastroUsuario():
    if request.method == 'GET':
        return render_template('cadastroUsuario.html')

    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')

    usuario = Usuarios(nome=nome, email=email, senha=senha)

    user_DAO.cadastrar(usuario)

    request.s
    return render_template('index.html')


