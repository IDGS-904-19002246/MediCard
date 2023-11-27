from flask import Blueprint, redirect, render_template, url_for,request, flash, jsonify
from flask_login import LoginManager, login_user, login_required, logout_user,current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
# from flask_wtf.csrf import CSRFProtect


import json
import os

from db import get_connection
from config import db
import validaciones
import sys
sys.path.append("..")

from modelos.M_medicamentos import tbl_medicamentos, medicamentosF
from modelos.M_tipo import tbl_tipos_medicina



cat = Blueprint('cat',__name__)

@cat.route("/api/categorias", methods=['GET','POST'])
def categorias():
    
    tipos = tbl_tipos_medicina.query.all()
    tipos_json = [{'id_tipo': t.id_tipo, 'nombre': t.nombre, 'descripcion': t.descripcion} for t in tipos] 

    return tipos_json

@cat.route("/categoria_add", methods=['GET','POST'])
def categoria_add():
    if request.method == 'POST':

        if request.form.get('accion') == 'add':
            tipo = tbl_tipos_medicina(
                nombre = str(request.form.get('tipo_nombre')),
                descripcion = str(request.form.get('tipo_descripcion'))
            )
            db.session.add(tipo)

        if request.form.get('accion') == 'update':
            tipo = tbl_tipos_medicina.query.filter_by(id_tipo=request.form.get('id_tipo')).first()
            if tipo:
                tipo.nombre = request.form.get('tipo_nombre')
                tipo.descripcion = request.form.get('tipo_descripcion')

        db.session.commit()
        db.session.close()
        return redirect(url_for('med.medicamentos'))
    else:
        return redirect(url_for('med.medicamentos'))


@cat.route("/categoria_delete", methods=['GET','POST'])
def categoria_delete():
    medicinas = tbl_medicamentos.query.filter_by(fk_id_tipo = request.args.get('id'))
    if medicinas:
        for m in medicinas:
            m.fk_id_tipo = 1
    
    tipo = tbl_tipos_medicina.query.get(request.args.get('id'))
    db.session.delete(tipo)
    db.session.commit()
    db.session.close()
    return redirect(url_for('med.medicamentos'))