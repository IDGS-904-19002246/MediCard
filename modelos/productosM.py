# from db import get_connection

# import sys
# sys.path.append("..")
# from config import db

# class Productos(db.Model):
#     __tablaname__='productos'
#     id_producto = db.Column(db.Integer, primary_key = True)
#     nombre=db.Column(db.String(32))

#     cantidad=db.Column(db.Integer)
#     cantidad_min=db.Column(db.Integer)

#     precio_U=db.Column(db.Integer)
#     precio_M=db.Column(db.Integer)

#     proceso=db.Column(db.String(250))
#     img=db.Column(db.String(250))
#     descripcion=db.Column(db.String(64))
#     estado=db.Column(db.String(4))
#     pendientes=db.Column(db.Integer)

#     def ProductosSelectTodos():
#         try:
#             connection = get_connection()
#             with connection.cursor() as cursor:
#                 cursor.execute('call ProductosSelectTodos()')
#                 resultset = cursor.fetchall()
#                 return resultset
#         except Exception as ex:
#             print(ex)

#     def ProductosSelectUno(id):
#         try:
#             connection = get_connection()
#             with connection.cursor() as cursor:
#                 cursor.execute('call ProductosSelectUno(%s)',(id,))
#                 resultset = cursor.fetchall()
#                 return resultset
#         except Exception as ex:
#             print(ex)

#     def ProductosSelectReseta(id):
#         try:
#             connection = get_connection()
#             with connection.cursor() as cursor:
#                 cursor.execute('call ProductosSelectReseta(%s)',(id,))
#                 resultset = cursor.fetchall()
#                 return resultset
#         except Exception as ex:
#             print(ex)

#     def ProductosUpdate(id,nom,can,can_min,pre_U,pre_M,pro,i,des):
#             try:
#                 connection = get_connection()
#                 with connection.cursor() as cursor:
#                     cursor.execute('call ProductosUpdate(%s,%s,%s,%s,%s,%s,%s,%s,%s)',
#                                 (id,nom,can,can_min,pre_U,pre_M,pro,i,des))
#                     connection.commit()
#                     connection.close()
#             except Exception as ex:
#                 print(ex)

#     def ProductosInsert(nom,can,can_min,pre_U,pre_M,pro,i,des):
#             try:
#                 connection = get_connection()
#                 with connection.cursor() as cursor:
#                     cursor.execute('call ProductosInsert(%s,%s,%s,%s,%s,%s,%s,%s)',
#                                 (nom,can,can_min,pre_U,pre_M,pro,i,des))
#                     connection.commit()
#                     connection.close()
#             except Exception as ex:
#                 print(ex)

#     def ProductosDelete(id):
#         try:
#             connection = get_connection()
#             with connection.cursor() as cursor:
#                 cursor.execute('call ProductosDelete(%s)',(id,))
#                 connection.commit()
#                 connection.close()
#                 return 'ok'
#         except Exception as ex:
#             print(ex)

#     def resetasInsert(id_pro,id_ins,can):
#             try:
#                 connection = get_connection()
#                 with connection.cursor() as cursor:
#                     cursor.execute('call resetasInsert(%s,%s,%s)',
#                                 (id_pro,id_ins,can))
#                     connection.commit()
#                     connection.close()
#             except Exception as ex: print(ex)
#     def resetasDelete(id):
#         try:
#             connection = get_connection()
#             with connection.cursor() as cursor:
#                 cursor.execute('call resetasDelete(%s)',(id,))
#                 connection.commit()
#                 connection.close()
#                 return 'ok'
#         except Exception as ex:
#             print(ex)
    