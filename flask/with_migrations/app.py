from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from config2 import Config2

db=SQLAlchemy()
migrate=Migrate()


class Student(db.Model):
  __tablename__="student"
  ## table requires columns
  id=db.Column(db.BigInteger,primary_key=True)
  name=db.Column(db.String(255),nullable=False)
  email=db.Column(db.String,unique=True,nullable=False)

class Pet(db.Model):
  __tablename__="pet"

  id=db.Column(db.BigInteger,primary_key=True)
  name=db.Column(db.String(255),nullable=False)
  age=db.Column(db.Integer)

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config2)

    db.init_app(app)
    migrate.init_app(app,db)


    return app

app=create_app()

if __name__ == '__main__':
    app.run(debug=True,port=9000)