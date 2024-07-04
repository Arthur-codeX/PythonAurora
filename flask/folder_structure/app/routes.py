from flask import Blueprint,jsonify,request

from .models import Student

student_blueprint=Blueprint("student",__name__)

@student_blueprint.route("/student",methods=["GET"])
def get_students():
    list_students=Student.query.all()
    all_students=[]
    for student in list_students:
     print(vars(student))
     all_students.append({'id':student.id,'name':student.name,'email':student.email})
    
    return jsonify(all_students),200