from flask import Blueprint, redirect, render_template, url_for,request, flash,make_response
from werkzeug.utils import secure_filename

from db import get_connection
from config import db
import validaciones
import sys
sys.path.append("..")

from modelos.M_medicamentos import tbl_medicamentos, medicamentosF



med = Blueprint('med',__name__)

@med.route("/medicamentos", methods=['GET','POST'])
def productos():
    med = medicamentosF.Select()

    medicinas = [
        {'id': id, 'nombre': nombre, 'fab': fab} for id, nombre, fab in med
        ]
    
  

    return medicinas
    
    return render_template('productos.html', G=galletas)



@med.route("/medicamentos/add", methods=['POST'])
def productos_api():
     
    if request.method == 'POST' and create_form.validate():
        file = request.files['img']
        
        basepath = os.path.dirname(__file__)
        filename = secure_filename(file.filename)

        ext = os.path.splitext(filename)[1]
        nue = request.form.get('nombre')+ext
        
        up_path = os.path.join(basepath,'../static/img/productos/',nue)
        file.save(up_path)
        m = Productos.ProductosInsert(
            # nom,can,can_min,pre_U,pre_M,pro,i,des
            request.form.get('nombre'),
            request.form.get('cantidad'),
            request.form.get('cantidad_min'),
            request.form.get('precio_U'),
            
            request.form.get('precio_M'),
            request.form.get('proceso'),
            nue,
            request.form.get('descripcion')

        )







@med.route("/api/medicamentos", methods=['GET'])
def productos_api():
    med = medicamentosF.Select()
    medicinas = [
        {'id': id, 'nombre': nombre, 'fab': fab} for id, nombre, fab in med
        ]
    return medicinas