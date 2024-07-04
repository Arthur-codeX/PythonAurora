from flask import Blueprint,jsonify,request

from .models import Pet

pet_blueprint=Blueprint("student",__name__)

@pet_blueprint.route("/pet",methods=["GET"])
def get_pets():
    list_students=Pet.query.all()
    all_students=[]
    for student in list_students:
     print(vars(student))
     all_students.append({'id':student.id,'name':student.name,'email':student.email})
    
    return jsonify(all_students),200