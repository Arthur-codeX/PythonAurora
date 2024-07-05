from flask import Flask,render_template,request,redirect,url_for,session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from datetime import timedelta

app=Flask(__name__)
app.config.from_object(Config)

# set the session lifetime
app.config['PERMANENT_SESSION_LIFETIME']=timedelta(seconds=60)

app.secret_key='secret_key'

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
    if 'user' in session:
      
      
      return render_template('home.html',say_hello=say_hello,session=f"Session is valid {session['user']}")
    
    return render_template('home.html',say_hello=say_hello,session=f"Session has expired. go to login")


@app.route("/login")
def login():
    user={'id':2,'name':'daniel'}
    session['user']=user['id']
    return render_template('login.html')

  
   

@app.route("/students")
def students():
    all_students=[]
    list_students=Student.query.all()
    for student in list_students:
      print(vars(student))
      all_students.append({'id':student.id,'name':student.name,'email':student.email})
    return render_template('student.html',students_list=all_students)

@app.route("/student/add",methods=["GET","POST"])
def addStudent():
    if request.method=="POST":
       name=request.form['name']
       email=request.form['email']
       print(f"Student : {name}, {email}")
       st=Student(name=name,email=email)
       db.session.add(st)
       db.session.commit()
       return redirect(url_for('students'))

    return render_template('add_student.html')

if __name__ == '__main__':
    app.run(debug=True)