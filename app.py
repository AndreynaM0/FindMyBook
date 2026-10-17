from mimetypes import init

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config, db
from controllers.login_controller import login_controller
from models.usuarios_model import Usuarios
from repositories import user_DAO
from flask_login import LoginManager

app = Flask(__name__)

app.config.from_object(Config)
app.secret_key = "RnluZE15Qm9vaw=="
db.init_app(app)
login_manager = LoginManager()
login_manager.login_view = 'login.login'
login_manager.init_app(app)

with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    try:
        return db.session.get(Usuarios, int(user_id))
    except Exception:
        return None

@app.route('/')
def principal():
    return render_template('index.html')


app.register_blueprint(login_controller, url_prefix='/login')



if __name__ == '__main__':
    app.run(debug=True)
    # user_DAO.cadastrar(Usuarios(email='andreyna_test@gmail.com', senha='12345', nome="Andreyna"))