from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config, db
from controllers.user_controller import user_controller
from models.usuarios_model import Usuarios

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def principal():
    return render_template('index.html')


app.register_blueprint(user_controller, url_prefix='/usuarios')



if __name__ == '__main__':
    app.run(debug=True)