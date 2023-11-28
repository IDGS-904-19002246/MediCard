from flask import Blueprint, redirect, render_template, url_for,request, flash
from flask_login import LoginManager, login_user, login_required, logout_user,current_user
from werkzeug.security import generate_password_hash, check_password_hash
import json

from db import get_connection
from config import db
from datetime import datetime
# from model import Usuarios
import sys
sys.path.append("..")
from modelos.M_comentarios import tbl_comentarios
import validaciones

ind = Blueprint('ind',__name__)



@ind.route("/opina")
def opina():
    com = tbl_comentarios.query.all()

    return render_template('index/opina.html',form = validaciones.comentarios(request.form), com = com)

@ind.route("/opina", methods=['GET','POST'])
def opina_post():
    create_form = validaciones.comentarios(request.form)
    if request.method == 'POST' and create_form.validate():
        
        fecha_actual = datetime.now()
        com = tbl_comentarios(
            nombre = request.form.get('nombre'),
            correo = request.form.get('correo'),
            mensaje = request.form.get('mensaje'),
            fecha = fecha_actual.strftime("%Y-%m-%d")
        )
        db.session.add(com)
        db.session.commit()
        
    return redirect(url_for('ind.opina'))
    
    
