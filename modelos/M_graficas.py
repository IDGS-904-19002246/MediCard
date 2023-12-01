from db import get_connection

import sys
sys.path.append("..")
from config import db


class graficasF():
    def grafica_top7medicinas(fecha):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call p_grafica_top7medicinas(%s)',(fecha,))
                return cursor.fetchall()
        except Exception as ex: print(ex)

    def grafica_top7usuarios(fecha):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call p_grafica_top7usuarios(%s)',(fecha,))
                return cursor.fetchall()
        except Exception as ex: print(ex)

    def grafica_pastelEmpresas(fecha):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call p_grafica_pastelEmpresas(%s)',(fecha,))
                return cursor.fetchall()
        except Exception as ex: print(ex)
    
    def grafica_lineas(fecha):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call p_grafica_lineas(%s)',(fecha,))
                return cursor.fetchall()
        except Exception as ex: print(ex)