import os

class Config:
    SECRET_KEY = 'mykey'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://simon:m1m1@localhost/blog'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}