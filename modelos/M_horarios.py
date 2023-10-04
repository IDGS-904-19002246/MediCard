from db import get_connection
from datetime import datetime 
import sys
sys.path.append("..")
from config import db


class tbl_horarios(db.Model):
    __tablaname__='tbl_horarios'

    id_horario = db.Column(db.Integer, primary_key = True)
    
    fk_id_tratamiento = db.Column(db.Integer)
    medicina_tomada = db.Column(db.Boolean)
    fecha = db.Column(db.DateTime)
    
    

