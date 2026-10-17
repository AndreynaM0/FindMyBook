from contextlib import redirect_stderr

from flask import Blueprint, render_template, request, redirect, url_for
from repositories import user_DAO
from models.usuarios_model import Usuarios
from flask_login import login_user

login_controller = Blueprint('login', __name__)
@login_controller.route('/cadastrar', methods=['GET', 'POST'])
def cadastroUsuario():
    if request.method == 'GET':
        return render_template('cadastroUsuario.html')

    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')

    usuario = Usuarios(nome=nome, email=email, senha=senha)

    user_DAO.cadastrar(usuario)
    print(usuario.id)

    login_user(usuario)
    return redirect(url_for('/'))

@login_controller.route('/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

