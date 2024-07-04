from . import db

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
  type=db.Column(db.String(255),nullable=False)
  age=db.Column(db.Integer)