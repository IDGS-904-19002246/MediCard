from db import get_connection

import sys
sys.path.append("..")
from config import db


class tbl_tipos_medicina(db.Model):
    __tablaname__='tbl_tipos_medicina'

    id_tipo = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(32))
    descripcion = db.Column(db.String(128))
    