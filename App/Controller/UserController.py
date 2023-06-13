

from App.Models import User,UserSchema
from flask import Blueprint,request,jsonify,make_response
from App.Repositories.UserRepository import UserRepository
from app import token_required,authenticate




user = Blueprint('user',__name__)

@user.route('/test',methods=['GET'])
def test():
    return " Testing "




# GET ALL USER DATA
@user.route('/user/getall',methods=['GET'])
@token_required
def getAllUser():
     #token = request.args.get('token')
     return UserSchema(many=True).dump(UserRepository().getAllData())
     


# AUTHENTICATION TESTING
@user.route('/user/login',methods=['POST'])
def login():
    
    user = UserRepository().getUserByUsername(User(**request.json).username)
    if user and user.password == User(**request.json).password:
        return  (authenticate(User(**request.json)))










# GET DATA BY ID



# ADD DATA
@user.route('/user/add',methods=['POST'])
def addUser():
     print(User(**request.json))
     #UserRepository().save(User(**request.json))
     
     return " User Saved "
    




# DELETE DATA
# UPDATE DATA