from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from db import get_connection

import sys
sys.path.append("..")
from config import db


class tbl_usuarios(UserMixin, db.Model):
    __tablaname__='tbl_usuarios'

    id_usuario = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(64))
    apellidoP = db.Column(db.String(64))
    apellidoM = db.Column(db.String(64))
    correo = db.Column(db.String(64))
    contrasena = db.Column(db.String(250))
    rol = db.Column(db.String(8))

    def is_active(self): return True
    def get_id(self): return self.id_usuario

    def Insert(nombre,apellidoP,apellidoM,correo,contrasena):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    'call usuariosInsert(%s,%s,%s,%s,%s)',
                    (nombre,apellidoP,apellidoM,correo,contrasena)
                )
                resultset = cursor.fetchall()
                return resultset
        except Exception as ex:
            print(ex)
# ---------------------------------------------------------------------------------
class usuariosF():
    def Select():
        usuarios = []
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call p_usuarios_select()')
                # ADMIN
                usuarios.append(cursor.fetchall())
                cursor.nextset()
                # EMPLE
                usuarios.append(cursor.fetchall())
                cursor.nextset()
                # COMUN
                usuarios.append(cursor.fetchall())
                cursor.nextset()
                # BANN
                usuarios.append(cursor.fetchall())
                return usuarios
        except Exception as ex:
            print(ex)
    def SelectOneData(id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call p_usuarios_selectOneData(%s)',(id,))
                return cursor.fetchall()
        except Exception as ex:
            print(ex)
    def Insert(nombre,apellidoP,apellidoM,correo,contrasena):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    'call usuariosInsert(%s,%s,%s,%s,%s)',
                    (nombre,apellidoP,apellidoM,correo,contrasena)
                )
                resultset = cursor.fetchall()
                return resultset
        except Exception as ex:
            print(ex)
    def UpdateRol(id,rol):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call p_usuarios_updateRol(%s,%s)',(id,rol))
                connection.commit()
                connection.close()
        except Exception as ex:
            print(ex)
    def UpdatePass(id,new_pass):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call p_usuarios_updatePass(%s,%s)',(id,new_pass))
                connection.commit()
                connection.close()
        except Exception as ex:
            print(ex)
