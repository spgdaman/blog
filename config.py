import os

class Config:
    SECRET_KEY = 'mykey'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://simon:m1m1@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}