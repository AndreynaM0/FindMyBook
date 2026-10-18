from flask import Blueprint, request, render_template
from flask_login import login_required


livro_controller = Blueprint('livro', __name__)
@livro_controller.route('/', methods=['GET', 'POST'])
@login_required
def buscar():
    if request.method == 'GET':
        return render_template("busca_livro.html")