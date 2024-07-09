from flask import Blueprint,jsonify,request
from flask_jwt_extended import jwt_required,get_jwt_identity

# pyjwt, flask_jwt
game_blueprint=Blueprint('game',__name__)


@game_blueprint.route("/game/board",methods=["GET"])
@jwt_required()
def get_board():
    current_user=get_jwt_identity()
    print(current_user)
    return jsonify({'message':f"Hi  this is your board"})

