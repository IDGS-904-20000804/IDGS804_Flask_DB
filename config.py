import os
from sqlalchemy import create_engine

import urllib

class Config(object):
    SECRET_KEY = 'MY_SECRET_KEY'
    SESSION_COOKIE_SECURE = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1029384756-MySQL_root@127.0.0.1/idgs804'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
