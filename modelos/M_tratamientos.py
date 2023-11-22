from db import get_connection

import sys
sys.path.append("..")
from config import db


class tbl_tratamientos(db.Model):
    __tablaname__='tbl_tratamientos'

    id_tratamiento = db.Column(db.Integer, primary_key = True)
    
    fk_id_usuario = db.Column(db.Integer)
    fk_id_medicamento = db.Column(db.Integer)

    precio = db.Column(db.Integer)
    dosis = db.Column(db.Integer)
    periodo_en_horas = db.Column(db.Integer)
    fecha_inicio = db.Column(db.DateTime)
    fecha_final   = db.Column(db.DateTime)
    
class tratamientosF():
    def Insert(inicio, final,n_horas):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call p_horarios_insertAll(%s,%s,%s)',(inicio, final, n_horas))
                connection.commit()
                connection.close()
                return True
        except Exception as ex: print(ex)
    

