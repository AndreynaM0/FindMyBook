from flask_sqlalchemy import SQLAlchemy


class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:12345@localhost:5432/findmybook"
    SQLALCHEMY_TRACK_MODIFICATIONS = True


db = SQLAlchemy()

