# from flask_sqlalchemy import SQLAlchemy
# from flask_login import UserMixin
# from db import get_connection

# import sys
# sys.path.append("..")
# from config import db


# class Usuarios(UserMixin,db.Model):
#     __tablaname__='usuarios'

#     id = db.Column(db.Integer, primary_key = True)
#     nombre=db.Column(db.String(64))
#     apellidoP=db.Column(db.String(64))
#     apellidoM=db.Column(db.String(64))

#     correo=db.Column(db.String(64))
#     contrasena = db.Column(db.String(250))
#     rol=db.Column(db.String(8))

#     def usuariosUpdate(id,nombre,apellidoP,apellidoM,correo):
#         try:
#             connection = get_connection()
#             with connection.cursor() as cursor:
#                 cursor.execute('call usuariosUpdate(%s,%s,%s,%s,%s)',(id,nombre,apellidoP,apellidoM,correo))
#                 connection.commit()
#                 connection.close()
#         except Exception as ex:
#             print(ex)

#     def usuariosNuevaContrasena(id,new_pass):
#         try:
#             connection = get_connection()
#             with connection.cursor() as cursor:
#                 cursor.execute('call usuariosNuevaContrasena(%s,%s)',(id,new_pass))
#                 connection.commit()
#                 connection.close()
#         except Exception as ex:
#             print(ex)

#     def usuariosSelectTodo():
#         usuarios = []
#         try:
#             connection = get_connection()
#             with connection.cursor() as cursor:
#                 cursor.execute('call usuariosSelectTodo()')
                
#                 usuarios.append(cursor.fetchall())

#                 cursor.nextset()
#                 usuarios.append(cursor.fetchall())

#                 cursor.nextset()
#                 usuarios.append(cursor.fetchall())

#                 cursor.nextset()
#                 usuarios.append(cursor.fetchall())
                
#                 return usuarios
#         except Exception as ex:
#             print(ex)

#     def usuariosRol(id,rol):
#         try:
#             connection = get_connection()
#             with connection.cursor() as cursor:
#                 cursor.execute('call usuariosRol(%s,%s)',(id,rol))
#                 connection.commit()
#                 connection.close()
#         except Exception as ex:
#             print(ex)
    
#     # def consultarTodos():
#     #     try:
#     #         connection = get_connection()
#     #         with connection.cursor() as cursor:
#     #             cursor.execute('call consultarTodos()')
#     #             resultset = cursor.fetchall()
                
#     #             return resultset
#     #     except Exception as ex:
#     #         print(ex)

    

# # VER INGREDIENTES
# # SELECT i.nombre AS 'Ingrediente', CONCAT(r.cantidad,'-',i.medida) AS Cantidad FROM productos AS p
# # INNER JOIN resetas AS r ON p.id_producto = r.id_producto
# # INNER JOIN insumos AS i ON r.id_insumo = i.id_insumo
# # WHERE p.id_producto = 1;