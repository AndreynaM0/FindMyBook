from contextlib import redirect_stderr

from flask import Blueprint, render_template, request, redirect, url_for, flash
from repositories import user_DAO
from models.usuarios_model import Usuarios
from flask_login import login_user,logout_user

login_controller = Blueprint('login', __name__)
@login_controller.route('/cadastrar', methods=['GET', 'POST'])
def cadastroUsuario():
    if request.method == 'GET':
        return render_template('cadastroUsuario.html')

    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')

    usuario = Usuarios(nome=nome, email=email, senha=senha)

    usuario_cadastrado= user_DAO.cadastrar(usuario)

    if usuario_cadastrado is None:
        flash("E-mail já cadastrado.")
        return render_template('cadastroUsuario.html')
    else:
        login_user(usuario_cadastrado)
        return redirect(url_for("livro.buscar"))


@login_controller.route('/', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        return render_template('login.html')

    email = request.form.get('email')
    senha = request.form.get('senha')

    usuario= user_DAO.buscar_por_email(email)
    if usuario is None:
        flash("Usuario não encontrado.")
        return render_template('login.html')
    else:
        if usuario.senha == senha:
            login_user(usuario)
            return redirect(url_for("livro.buscar"))
        else:
            flash("Senha incorreta.")
            return render_template('login.html')


@login_controller.route('/logout', methods=['POST'])
def logout():
    if request.method == 'POST':
        logout_user()
        return redirect(url_for("login.login"))