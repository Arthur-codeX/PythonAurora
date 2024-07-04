from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app=Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy(app)
migrate=Migrate(app,db)

class Student(db.Model):
  __tablename__="student"

  id=db.Column(db.BigInteger,primary_key=True)
  name=db.Column(db.String(255),nullable=False)
  email=db.Column(db.String,unique=True,nullable=False)

class Pet(db.Model):
  __tablename__="pet"

  id=db.Column(db.BigInteger,primary_key=True)
  name=db.Column(db.String(255),nullable=False)
  type=db.Column(db.String(255),nullable=False)
  age=db.Column(db.Integer)


@app.route("/")
def home():
    say_hello="This is my students application"
    return render_template('home.html',say_hello=say_hello)

@app.route("/students")
def students():
    all_students=[]
    list_students=Student.query.all()
    for student in list_students:
      print(vars(student))
      all_students.append({'id':student.id,'name':student.name,'email':student.email})
    return render_template('student.html',students_list=all_students)

@app.route("/student/add")
def addStudent():
    return render_template('add_student.html')

if __name__ == '__main__':
    app.run(debug=True)