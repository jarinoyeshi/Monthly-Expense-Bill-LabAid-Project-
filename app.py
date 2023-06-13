

from flask import Flask
import os
from App.Database import registerDatabase,createTable



def createApp()-> Flask:
    
    app = Flask(__name__)
    
    # REGISTER CONFIG
    registerConfig(app)
    
    
    # REGISTER DATABASE
    registerDatabase(app)
    
    # REGISTER JWT
    
    
    # REGISTER CORS
    
    
    # REGISTER BLUEPRINT
    
    # REGISTER LOGGER
    
    # REGISTER SWAGGER
    
    
    
    # TESTING ROUTES
    @app.route('/test',methods=['GET'])
    def index():
        return { "Message" : "App working" }
    
    
    
    @app.route('/create/table',methods=['GET'])
    def createDatabase():
        createTable()
        return {" Database Created "}
    return app






# FUNCTION DEFINITION
def registerConfig(app):
   
   configInfo = os.environ.get("CONFIG")         # os.environ.get() method is used to access environment variables
   
   if configInfo is None:
       print("No defined environment found. Default Development environment working !! ")
       configInfo = "App.config.DevelopmentConfig"
       
   app.config.from_object(configInfo)
   
   print(f"DEBUG: {app.config.get('DEBUG')}")
   print(f"TESTING: {app.config.get('TESTING')}")
   print(f"DATABASE_URI: {app.config.get('DATABASE_URI')}")
    
    






# DATABSE REGISTER





app = createApp()