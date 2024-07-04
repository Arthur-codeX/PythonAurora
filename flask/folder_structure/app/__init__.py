from flask import Flask,g
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

db=SQLAlchemy()
migrate=Migrate()

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app,db)

    from .routes import student_blueprint
    from .pet_route import pet_blueprint
    app.register_blueprint(student_blueprint)
    app.register_blueprint(pet_blueprint)

    return app

