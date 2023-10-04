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
# ---------------------------------------------------------------------------------
class usuariosF():
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


# class Proveedores(db.Model):
#     __tablaname__='proveedores'

#     id_proveedor = db.Column(db.Integer, primary_key = True)
#     nombre=db.Column(db.String(32))
#     correo=db.Column(db.String(32))
#     telefono=db.Column(db.String(10))
#     direccion = db.Column(db.JSON)       

#     def ProveedoresSelectUno(id):
#         try:
#             connection = get_connection()
#             with connection.cursor() as cursor:
#                 cursor.execute('call ProveedoresSelectUno(%s)',(id,))
#                 resultset = cursor.fetchall()
#                 return resultset
#         except Exception as ex:
#             print(ex)
    
#     # def ProveedoresSelectTodo():
#     #     try:
#     #         connection = get_connection()
#     #         with connection.cursor() as cursor:
#     #             cursor.execute('call ProveedoresSelectTodo()')
#     #             resultset = cursor.fetchall()
#     #             return resultset
#     #     except Exception as ex:
#     #         print(ex)
    



# class Insumos(db.Model):
#     __tablaname__='insumos'
#     id_insumo = db.Column(db.Integer, primary_key = True)
#     nombre=db.Column(db.String(32))

#     cantidad=db.Column(db.Integer)
#     cantidad_min=db.Column(db.Integer)

#     caducidad = db.Column(db.JSON)


#     def InsumosSelectTodos():
#         try:
#             connection = get_connection()
#             with connection.cursor() as cursor:
#                 cursor.execute('call InsumosSelectTodos()')
#                 resultset = cursor.fetchall()
#                 return resultset
#         except Exception as ex:
#             print(ex)
        
#     def InsumosDelete(id):
#         try:
#             connection = get_connection()
#             with connection.cursor() as cursor:
#                 cursor.execute('call InsumosDelete(%s)',(id,))
#                 connection.commit()
#                 connection.close()
#                 return 'ok'
#         except Exception as ex:
#             print(ex)

#     def InsumosInsert(nom, can, can_min, med, cad):
#         try:
#             connection = get_connection()
#             with connection.cursor() as cursor:
#                 cursor.execute('call InsumosInsert(%s,%s,%s,%s,%s)',(nom, can, can_min, med, cad))
#                 connection.commit()
#                 connection.close()
#                 return 'ok'
#         except Exception as ex:
#             print(ex)
    
#     def InsumosUpdate(id,nom, can, can_min, med,cad):
#         try:
#             connection = get_connection()
#             with connection.cursor() as cursor:
#                 cursor.execute(
#                     'call InsumosUpdate(%s,%s,%s,%s,%s,%s)',
#                     (id,nom, can, can_min, med,cad))
#                 connection.commit()
#                 connection.close()
#                 return 'ok'
#         except Exception as ex:
#             print(ex)
    
#     def InsumosAdd(id, can, fec, prov, cost):
#         try:
#             connection = get_connection()
#             with connection.cursor() as cursor:
#                 cursor.execute(
#                     'call InsumosAdd(%s,%s,%s,%s,%s)',
#                     (id, can, fec,prov, cost))
#                 connection.commit()
#                 connection.close()
#                 return 'ok'
#         except Exception as ex:
#             print(ex)
    
#     def InsumosCocinar(id_pro,can):
#         try:
#             connection = get_connection()
#             with connection.cursor() as cursor:
#                 cursor.execute(
#                     'call InsumosCocinar(%s,%s)',
#                     (id_pro, can))
#                 connection.commit()
#                 connection.close()
#                 return 'ok'
#         except Exception as ex:
#             print(ex)
    
#     def InsumosCocinarValidar(id_pro,can):
#         try:
#             connection = get_connection()
#             with connection.cursor() as cursor:
#                 cursor.execute( 'call InsumosCocinarValidar(%s,%s)',(id_pro, can))
#                 return cursor.fetchall()
#         except Exception as ex:
#             print(ex)

#     def InsumosCocinando(id_pro):
#         try:
#             connection = get_connection()
#             with connection.cursor() as cursor:
#                 cursor.execute( 'call InsumosCocinando(%s)',(id_pro,))
#                 resultset = cursor.fetchall()
#                 return resultset
#         except Exception as ex:
#             print(ex)