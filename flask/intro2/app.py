from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy


conf={
    'dbname':'postgres',
    'user':'postgres.erojatpkqtqexubknucv',
    'password':'4zY63KNsPFznj2oX',
    'host':'aws-0-ap-south-1.pooler.supabase.com',
    'port':'5432'
}

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=f"postgresql://{conf['user']}:{conf['password']}@{conf['host']}:5432/postgres"
db=SQLAlchemy(app)

#####---###

class Student(db.Model):
  __tablename__="student"
  ## table requires columns
  id=db.Column(db.BigInteger,primary_key=True)
  name=db.Column(db.String(255),nullable=False)
  email=db.Column(db.String,unique=True,nullable=False)



@app.route("/home",methods=["GET"])
def hello():
  return "Welcome to my Flask Server",200

# GET, READ REQUEST
@app.route("/student",methods=["GET"])
def student_list():
  students=[{"name":"Sam","email":"sam@gmail.com"},{"name":"Delilah","email":"delilah@gmail.com"}]
  all_students=[]
  list_students=Student.query.all()
  for student in list_students:
    print(vars(student))
    all_students.append({'id':student.id,'name':student.name,'email':student.email})
  return jsonify(all_students),200

# ADD POST
@app.route("/student",methods=["POST"])
def add_student():
  # VALIDATION
  # API YOU HAVE TO BE VERY SPECIFIC
  body=request.get_json()
  name=body.get('name')
  email=body.get('email')

  if not name or not email:
    return jsonify({'message':"Email or name missing"}),400
  exist_student=Student.query.filter_by(email=email).first()

  if exist_student:
    return jsonify({'message':f"student with email {email} already exists",'data':{
      'name':exist_student.name,
      'email':exist_student.email
    }}),400

  st=Student(name=name,email=email)
  db.session.add(st)
  db.session.commit()
  return jsonify({'message':"Student Added"}),200

# ADD PUT, UPDATE
@app.route("/student",methods=["PUT"])
def update_student():
  body=request.get_json()
  id=body.get("id")
  name=body.get('name')
  email=body.get('email')

  if not id:
    return request({'message':"Student id required"}),400
  
  #exist_student=Student.query.filter_by(id=id).first()
  exist_student=Student.query.get(id)

  if name:
    exist_student.name=name
  if email:
    exist_student.email=email
  
  db.session.commit()
  return jsonify({'message':"Student updated",'student':{    'name':exist_student.name,
      'email':exist_student.email}}),200

# Identify the student, delete. <id>
@app.route("/student",methods=["DELETE"])
def delete_student():
  query_params=request.args
  print(query_params)
  obj={}
  for key,value in query_params.items():
   obj[key]=value
  print(obj)

  id=obj.get('id')

  if not id:
    return jsonify({'message':'Id required to delete student'}),400
  
  exist_student=Student.query.get(id)

  if not exist_student:
    return jsonify({'message':'Student to delete does not exist'}),400
  
  db.session.delete(exist_student)
  db.session.commit()

  return jsonify({}),204

# CRUD, CREATE, READ , UPDATE , DELETE

# DYNAMIC URLS

# GET student by id
@app.route("/student/<int:id>",methods=["GET"])
def get_student_by_id(id):
  student=Student.query.get(id)

  if not student:
    return jsonify({'message':f'Student with id {id} does not exist'}),400
  
  return jsonify({  'name':student.name,'email':student.email}),200


if __name__=="__main__":
  app.run(debug=True,port=9000)