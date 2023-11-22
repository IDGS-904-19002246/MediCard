from db import get_connection

import sys
sys.path.append("..")
from config import db


class tbl_medicamentos(db.Model):
    __tablaname__='tbl_medicamentos'

    id_medicamento = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(64))
    fabricante = db.Column(db.String(64))
    cantidad = db.Column(db.Integer)
    medida = db.Column(db.String(16))
    estado = db.Column(db.String(16))
    fk_id_tipo = db.Column(db.Integer)

    
class medicamentosF():
    def Select():
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call p_medicamentos_select()')
                return cursor.fetchall()
        except Exception as ex:
            print(ex)
    def SelectOne(id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call p_medicamentos_selectOne(%s)',(id,))
                return cursor.fetchall()
        except Exception as ex:
            print(ex)
    def Insert(nombre,fabricante,cantidad,medida,img,tip):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call p_medicamentos_insert(%s,%s,%s,%s,%s,%s)',
                            (nombre,fabricante,cantidad,medida,img,tip))
                connection.commit()
                connection.close()
                return True
        except Exception as ex: print(ex)
    def InsertApi(nombre,fabricante,cantidad,medida,img,tip):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call p_medicamentos_insertApi(%s,%s,%s,%s,%s,%s)',
                            (nombre,fabricante,cantidad,medida,img,tip))
                connection.commit()
                connection.close()
                return True
        except Exception as ex: print(ex)
    def Update(nombre,fabricante,cantidad,medida,estado,tip,id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call p_medicamentos_update(%s,%s,%s,%s,%s,%s,%s)',
                            (nombre,fabricante,cantidad,medida,estado,tip,id))
                connection.commit()
                connection.close()
                return True
        except Exception as ex: print(ex)
    def UpdateImg(id,url):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call p_imagen_update(%s,%s)',
                            (id,url))
                connection.commit()
                connection.close()
                return True
        except Exception as ex: print(ex)
