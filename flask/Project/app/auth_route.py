from flask import Blueprint,jsonify,request

from . import db

from .models import Member

import bcrypt

auth_blueprint=Blueprint('auth',__name__)

@auth_blueprint.route("/signup",methods=["POST"])
def signup():
    body=request.get_json()
    alias=body.get('alias')
    email=body.get('email')
    password=body.get('password')

    ## Validation
    if not email or not password or not alias:
        return jsonify({'message':"Required field missing"}),400
    
    if len(email)<4:
        return jsonify({'message':"Email too short"}),400
    
    if len(alias)<4:
        return jsonify({'message':"Name too short"}),400
    
    if len(password)<4:
        return jsonify({'message':"Password too short"}),400
    
    existing_member=Member.query.filter_by(email=email).first()

    if existing_member:
        return jsonify({'message':f"Email already in use {email}"}),400
    
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    member=Member(alias=alias,email=email,password=hashed_password)
    db.session.add(member)
    db.session.commit()
    return jsonify({"message":"Sign up success"}),201
    