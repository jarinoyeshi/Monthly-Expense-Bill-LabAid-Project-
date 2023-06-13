

class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI= ""
    SECRET_KEY = ""


class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI ="sqlite:///Database/dev.db"
    SECRET_KEY = "@development#secret!key*"


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    DATABASE_URI = "sqlite:///Database/test.db"
    SECRET_KEY = "@testing#secret!key*"

class ProductionConfig(Config):
    DATABASE_URI = "sqlite:///Database/data.db"
    SECRET_KEY = "@production#secret!key*"

