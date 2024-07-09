from flask import Blueprint,jsonify,request

from flask_jwt_extended import create_access_token,JWTManager

from . import db,bcrypt

from datetime import timedelta,datetime,timezone

from .models import Member


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
    
    hashed_password = bcrypt.generate_password_hash(password).decode('utf8')
    
    member=Member(alias=alias,email=email,password=hashed_password)
    db.session.add(member)
    db.session.commit()
    return jsonify({"message":"Sign up success"}),201
    
@auth_blueprint.route("/login",methods=["POST"])
def login():
    body=request.get_json()
    email=body.get('email')
    password=body.get('password')

        ## Validation
    if not email or not password:
        return jsonify({'message':"Required field missing"}),400
    user=Member.query.filter_by(email=email).first()

    if not user:
        return jsonify({'message':"User not found"}),400
    
    pass_ok=bcrypt.check_password_hash(user.password.encode('utf-8'),password)
    
    expires=datetime.utcnow()+timedelta(hours=24)
    ## ACCESS TOKEN
    access_token=create_access_token(identity=user.details(),expires_delta=(expires-datetime.utcnow()))
    if not pass_ok:
        return jsonify({"message":"Invalid password"}),401
    return jsonify({'user':user.details(),'token':access_token})
    
    