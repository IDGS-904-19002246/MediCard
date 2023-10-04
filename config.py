import os
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
import urllib

db=SQLAlchemy()
class Config(object):
    SECRET_KEY='MY_SECRET_KEY'
    SESSION_COOKIE_SECURE=False

class DevelopmentConfigRoot(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:@127.0.0.1/idgs1004_medicard'
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class DevelopmentConfigNoRoot(Config):
    def __init__(self,usuario, contrasena):
        super().__init__()
        self.DEBUG = True
        self.SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{usuario}:{contrasena}@127.0.0.1/idgs1004_medicard'
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False

    # config = DevelopmentConfigRoot('tu_usuario', 'tu_contraseña')
# https://www.digitalocean.com/community/tutorials/crear-un-nuevo-usuario-y-otorgarle-permisos-en-mysql-es
    # USE idgs1004_medicard;
    # SELECT USER, HOST,authentication_string   FROM mysql.user;
    # CREATE USER 'nuevo_usuario'@'localhost' IDENTIFIED BY 'contraseña';
    # GRANT ALL PRIVILEGES ON nombre_de_base_de_datos.* TO 'nuevo_usuario'@'localhost';
    
