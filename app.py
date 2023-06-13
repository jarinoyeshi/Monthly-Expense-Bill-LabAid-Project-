
import jwt
from flask import Flask,request,jsonify
import os
from App.Database import registerDatabase,createTable
from datetime import datetime,timedelta
#from flask_jwt import JWT


def createApp()->Flask:
    
    
    app = Flask(__name__)
    
    
    
    # REGISTER CONFIG
    registerConfig(app)
    
    
    
    # REGISTER DATABASE
    registerDatabase(app)
    
    
    
    # REGISTER BLUEPRINT
    registerBluePrint(app)
    
    
    
    # REGISTER JWT
    #registerJWT(app)
    
    
    
    # REGISTER CORS
    
    
    
    
    # REGISTER SWAGGER
    
    
    
    
    # REGISTER LOGGER
    
    
    
    
    # TESTING ROUTES
    @app.route('/',methods=["GET"])
    def index():
        return {" Message ":" App Running "}
    
    
    
    
    @app.route('/create/database',methods=['GET'])
    def createDatabase():
        createTable()
        return " Database Created "
    
    return app




def registerConfig(app):
    
    
    configInfo = os.environ.get("CONFIG")
    
    if configInfo is None:
        print(" NO configuration was set. Default database dev.db working .")
        configInfo= "App.config.DevelopmentConfig"
    
    
    app.config.from_object(configInfo)
    
    print(f"DEBUG: {app.config.get('DEBUG')}")
    print(f"TESTING: {app.config.get('TESTING')}")
    print(f"DATABASE_URI: {app.config.get('DATABASE_URI')}")




def registerBluePrint(app):
    from App.Controller.UserController import user
    app.register_blueprint(user)
    





def authenticate(data):
        print('AUTHENTICATE ',app.config['SECRET_KEY'])
        token = jwt.encode({
            'user': data.username,
            'expiration': str(datetime.utcnow() + timedelta(seconds=60))
        },app.config['SECRET_KEY'])
        #print(token)
        return token
    




def token_required(func):
    from functools import wraps 
    
    # decorator factory which invoks update_wrapper() method and passes decorated function as an argument
    @wraps(func)
    def decorater(*args, **kwargs):
        
        token = request.args.get('token')
        print('token testing',token)
        if not token:
            return jsonify({'Alart': 'Missing token'})
        try: 
            print('secret key ',app.config['SECRET_KEY'])
            payload = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'Alart':'Invalid Token'})
        return func(*args, **kwargs)
    return decorater












## JWT
        # token = jwt.encode({
        #     'user': data.username,
        #     'expiration': str(datetime.utcnow() + timedelta(seconds=60))
        # },app.config.get['SECRET_KEY'])
        
        # return jsonify({'token': token})
    
    
# def registerJWT(app: Flask) -> None:
#     from App.authentication import authenticate, indetity
    
#     app.secret_key = app.config.get("SECRET_KEY")
    
#     app.config.update(
#         jwt = JWT(app, authenticate, indetity)
#     )




app = createApp()