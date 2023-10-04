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
    periodo_en_horas = db.Column(db.Integer)
    fecha_inicio = db.Column(db.Date)
    fecha_final   = db.Column(db.Date)
    
    

