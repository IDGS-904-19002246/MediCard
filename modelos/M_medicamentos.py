from db import get_connection

import sys
sys.path.append("..")
from config import db


class tbl_medicamentos(db.Model):
    __tablaname__='tbl_medicamentos'

    id_medicamento = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(64))
    fabricante =db.Column(db.String(64))

    def __init__(self,id , nom, fab):
        self.id_medicamento =  id
        self.nombre = nom
        self.fabricante = fab
    
class medicamentosF():
    def Select():
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call p_medicamentos_select()')
                return cursor.fetchall()
        except Exception as ex:
            print(ex)
