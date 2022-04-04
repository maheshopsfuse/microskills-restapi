import os
import logging
import json
from logging.handlers import TimedRotatingFileHandler


formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s  %(name)s %(threadName)s :- %(message)s")

handler = TimedRotatingFileHandler(
    os.getenv('SERVER_LOG', 'log/MicroSkills-Server.log'), when="midnight", interval=1, encoding='utf8')
handler.suffix = "%Y-%m-%d_%H-%M-%S"
handler.setFormatter(formatter)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)

SENDGRID_API_KEY = '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'
SENDGRID_EMAIL_SENDER = 'hello@your29.com'


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    """
    Development Configuration
    """
    TESTING = True
    DEBUG = True
    ENV = 'development'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_USER = 'postgres'
    DATABASE_NAME = 'microskill'
    DATABASE_PASSWORD = '1234'
    DATABASE_URI = 'localhost'
    DATABASE_PORT = 5432
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_URI}:{DATABASE_PORT}/{DATABASE_NAME}"
    ACCESS_TOKEN_EXPIRE_IN_DAYS = 3
    REFRESH_TOKEN_EXPIRE_IN_DAYS = 16


class TestingConfig(Config):
    """
    Development Configuration
    """
    TESTING = True
    DEBUG = True
    ENV = 'testing'
    DATABASE_USER = 'postgres'
    DATABASE_NAME = 'postgres'
    DATABASE_PASSWORD = '1234'
    DATABASE_URI = '127.0.0.1'
    DATABASE_PORT = 5432
    MONGODB_CONNECT = False

    MONGODB_SETTINGS = {
        'host': f'mongodb://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_URI}:{DATABASE_PORT}/{DATABASE_NAME}?authSource={DATABASE_NAME}',
        'connect': False,
    }
    ACCESS_TOKEN_EXPIRE_IN_DAYS = 3
    REFRESH_TOKEN_EXPIRE_IN_DAYS = 16


class ProductionConfig(Config):
    """
    Production Environment Config FIle Configuration
    Environment Required Variable:
        variable         :     operation                 :      example
    ==================================================================================================================
        DATABASE_USER    : export user name              :       "root"
        DATABASE_NAME    : export name                   :       "mydb"
        DATABASE_PASSWORD: export DATABASE_USER password :       "xyz"
        DATABASE_URI     : export databse URI            :       IP Address
        DATABASE_PORT    : export port                   :       "5432"
    ==================================================================================================================
    """
    TESTING = False
    DEBUG = False
    ENV = 'production'

    DATABASE_USER = 'postgres'
    DATABASE_NAME = 'postgres'
    DATABASE_PASSWORD = '1234'
    DATABASE_URI = 'el-prod-mongodb.us-central1-a.c.elytics-321404.internal'
    DATABASE_PORT = 5432
    MONGODB_CONNECT = False
    MONGODB_SETTINGS = {
        'host': f'mongodb://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_URI}:{DATABASE_PORT}/{DATABASE_NAME}?authSource={DATABASE_NAME}',
        'connect': False,
    }
    ACCESS_TOKEN_EXPIRE_IN_DAYS = 3
    REFRESH_TOKEN_EXPIRE_IN_DAYS = 16


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY


# def load_config():
#     with open("D:\exlytics-dev\elytics-data-pipeline\config-dev.json", 'r') as f:
#         return json.load(f)
#
#
# config_data = load_config()
