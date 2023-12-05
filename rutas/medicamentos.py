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



med = Blueprint('med',__name__)

@med.route("/medicamentos", methods=['GET','POST'])
@login_required
def medicamentos():
    usuario = current_user
    if usuario.rol != 'ADMIN': return redirect(url_for('index'))
    m = medicamentosF.Select()
    tipos = tbl_tipos_medicina.query.all()
    tipos_json = [{'id_tipo': t.id_tipo, 'nombre': t.nombre, 'descripcion': t.descripcion} for t in tipos] 

    medicinas = [{
        'id_medicamento': id,
        'nombre': nombre,
        'fabricante': fab,
        'cantidad':can,
        'medida':med,
        'estado':est,
        'fotos':json.loads(img),
        'tipo':tip
        } for id, nombre, fab, can, med, est, img, tip in m 
        ]
    
    create_form = validaciones.medicamentos(request.form)
    if request.method == 'POST' and create_form.validate():
        ok = medicamentosF.ProductosInsert(
            request.form.get('nombre'),
            request.form.get('fabricante'),
            request.form.get('cantidad'),
            request.form.get('medida'),
            request.form.get('tipo')
        )
        if not ok:
            flash('Ocurrió un error al insertar')
            return redirect(url_for('med.medicamentos_form'))
    
    return render_template('med/medicamentos.html', M=medicinas, tipo=tipos_json, lista=True)

@med.route("/medicamentos_edit", methods=['GET','POST'])
def medicamentos_edit():
    
    create_form = validaciones.medicamentos(request.form)
    m = medicamentosF.SelectOne(request.args.get('id'))
    tipo = tbl_tipos_medicina.query.all()
    medicina = [{
        'id_medicamento': id,
        'nombre': nombre,
        'fabricante': fab,
        'cantidad':can,
        'medida':med,
        'estado':est,
        'fotos':json.loads(img),
        'tipo':tip
        } for id, nombre, fab, can, med, est, img, tip in m ]
    if request.method == 'GET':
        create_form.id_medicamento.data = medicina[0]['id_medicamento']
        create_form.nombre.data = medicina[0]['nombre']
        create_form.fabricante.data = medicina[0]['fabricante']
        create_form.cantidad.data = medicina[0]['cantidad']
        create_form.medida.data = medicina[0]['medida']
        create_form.estado.data = medicina[0]['estado']
        create_form.tipo.data = medicina[0]['tipo']

    if request.method == 'POST' and create_form.validate():
        if request.files['img'].filename != '':
            file = request.files['img']
            basepath = os.path.dirname(__file__)
            filename = secure_filename(file.filename)
            ext = os.path.splitext(filename)[1]
            nue = request.form.get('id_medicamento')+'_'+request.form.get('nombre')+ext
            up_path = os.path.join(basepath,'../static/img/medicamentos/',nue)
            file.save(up_path)

            medicamentosF.UpdateImg(request.form.get('id_medicamento'),nue)
    # def Update(nombre,fabricante,cantidad,medida,estado,tip,id):

        m = medicamentosF.Update(
            request.form.get('nombre'),
            request.form.get('fabricante'),
            request.form.get('cantidad'),
            request.form.get('medida'),
            request.form.get('estado'),
            request.form.get('tipo'),
            request.form.get('id_medicamento')
        )
        return redirect(url_for('med.medicamentos'))
    return render_template('med/medicamentos_edit.html', form=create_form, m=medicina,tipo=tipo)


@med.route("/medicamentos_add", methods=['GET','POST'])
def medicamentos_add():
    create_form = validaciones.medicamentos(request.form)
    tipo = tbl_tipos_medicina.query.all()
    if request.method == 'POST' and create_form.validate():
        file = request.files['img']
        
        basepath = os.path.dirname(__file__)
        filename = secure_filename(file.filename)

        ext = os.path.splitext(filename)[1]
        nue = request.form.get('nombre')+ext

        up_path = os.path.join(basepath,'../static/img/medicamentos/',nue)
        file.save(up_path)

        m = medicamentosF.Insert(
            request.form.get('nombre'),
            request.form.get('fabricante'),
            request.form.get('cantidad'),
            request.form.get('medida'),
            nue,
            request.form.get('tipo')
        )
        return redirect(url_for('med.medicamentos'))
    return render_template('med/medicamentos_add.html', form = create_form, tipo = tipo)

@med.route("/medicamentos_delete", methods=['GET','POST'])
def medicamentos_delete():
    m = tbl_medicamentos.query.get(request.args.get('id'))
    m.estado = 'borrado'
    db.session.commit()

    return redirect(url_for('med.medicamentos'))
#--------------------------------------------------------------------------------



@med.route("/api/medicamentos", methods=['GET'])
def api_medicamentos():
    m = medicamentosF.Select()
    medicinas = [{
        'id_medicamento': id,
        'nombre': nombre,
        'fabricante': fab,
        'cantidad':can,
        'medida':med,
        'estado':est,
        'fotos':json.loads(img),
        'tipo':tip
        } for id, nombre, fab, can, med, est, img, tip in m 
        ]
    
    return medicinas

# @med.route("/api/medicamentos_add", methods=['GET','POST'])
# def api_medicamentos_add():
#     if request.method == 'POST':
#         # file = request.files['img']
        
#         # basepath = os.path.dirname(__file__)
#         # filename = secure_filename(file.filename)

#         # ext = os.path.splitext(filename)[1]
#         # nue = request.form.get('nombre')+ext

#         # up_path = os.path.join(basepath,'../static/img/medicamentos/',nue)
#         # file.save(up_path)

#         # m = medicamentosF.Insert(
#         #     request.form.get('nombre'),
#         #     request.form.get('fabricante'),
#         #     request.form.get('cantidad'),
#         #     request.form.get('medida'),
#         #     nue
#         # )
#         # if m == True:
#             return {'status':'ok','msg':'El medicamento guardado correctamente'}
#     else:
#             return { 'status':'no','msg':'El medicamento no se pudo guardar'}