from flask import Blueprint, redirect, render_template, url_for,request, flash,current_app,make_response
from flask_login import login_user, login_required, logout_user,current_user
from werkzeug.security import generate_password_hash, check_password_hash
from itertools import groupby
import json

from db import get_connection
from config import db
import validaciones
import sys
sys.path.append("..")
from modelos.M_usuarios import tbl_usuarios, usuariosF

# from modelos.usuariosM import Usuarios
# from modelos.ventasM import Ventas


usu = Blueprint('usu',__name__)



    

# @usu.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     response = make_response(redirect(url_for('usu.login')))
#     # response.delete_cookie('carrito', domain="127.0.0.1")
#     return response
#     return redirect(url_for('usu.login'))

@usu.route('/login')
def login():
    create_form = validaciones.usuarios(request.form)
    return render_template('usu/login.html',form=create_form)


@usu.route("/login", methods=['GET','POST'])
def login_post():
    create_form = validaciones.login(request.form)
    if request.method == 'POST' and create_form.validate():
        correo = request.form.get('correo')
        contrasena = request.form.get('contrasena')
        U = tbl_usuarios.query.filter_by(correo=correo).first()

        if not U or not check_password_hash(U.contrasena, contrasena) :
            flash('El usuario y/o la contraseña son incorrectos')
            return render_template('usu/login.html',form=create_form)
        if U.rol == 'baneado':
            flash('Este usuario esta baneado')
            return redirect(url_for('usu.login'))
        login_user(U)
        return redirect(url_for('index'))
    

@usu.route('/singup', methods=['GET','POST'])
def singup():
    create_form = validaciones.usuarios(request.form)
    if request.method == 'POST' and create_form.validate():

        correo = request.form.get('correo')
        contrasena = request.form.get('contrasena')

        if contrasena != request.form.get('contrasena2'):
            flash('La contraseñas deben consider')
            return redirect(url_for('usu.singup'))
        user = tbl_usuarios.query.filter_by(correo=correo).first()
        if user:
            flash('El Correo ya esta en uso')
            return redirect(url_for('usu.singup'))
        
        # return str(

        #     request.form.get('nombre')
        #            )
        
        nuevo_usuario = tbl_usuarios(
            nombre = request.form.get('nombre'),
            apellidoP =request.form.get('apellidoP'),
            apellidoM = request.form.get('apellidoM'),
            correo = correo,
            contrasena = generate_password_hash(str(contrasena), method='sha256'),
            rol  ='comun'
            )
        
        db.session.add(nuevo_usuario)
        db.session.commit()

        # tbl_usuarios.Insert(
        #     request.form.get('nombre'),
        #     request.form.get('apellidoP'),
        #     request.form.get('apellidoM'),
        #     correo,
        #     generate_password_hash(str(contrasena), method='sha256')
        # )
        # return render_template('login.html',form=create_form)
        return redirect(url_for('usu.login',form=create_form))
    else:
        return render_template('usu/singup.html',form = create_form)


# ----------------------------------------------------------------------------------------------------
# @usu.route("/micuenta", methods=['GET','POST'])
# @login_required
# def micuenta():
#     if current_user.rol == 'baneado':
#         flash('Este usuario esta baneado')
#         return redirect(url_for('usu.login'))
#     ventas = Ventas.ventasSelectUsuario(current_user.id)
#     lista = []
#     salida = []
#     for v in ventas:
#         lista.append({
#             'id_venta': v[0],
#             'nombre': v[1],
#             'descripcion': v[2],
#             'cantidad': v[3],
#             'precio': v[4],
#             'fecha': v[5],
#             'direccion': v[6],
#             'entrega': v[7]
#         })

#     for i in range(len(lista)):
#         if i == 0:
#             salida.append({
#                 'id_venta': lista[i]['id_venta'],
#                 'fecha': lista[i]['fecha'],
#                 'direccion': lista[i]['direccion'],
#                 'entrega': lista[i]['entrega'],
#                 'productos' : [
#                         {
#                         'nombre': lista[i]['nombre'],
#                         'descripcion': lista[i]['descripcion'],
#                         'cantidad': lista[i]['cantidad'],
#                         'precio': lista[i]['precio']
#                         }
#                     ]
#                 }
#             )
#         else:
#             if lista[i]['id_venta'] == lista[i-1]['id_venta']:
#                 salida[-1]['productos'].append({
#                     'nombre': lista[i]['nombre'],
#                     'descripcion': lista[i]['descripcion'],
#                     'cantidad': lista[i]['cantidad'],
#                     'precio': lista[i]['precio']
#                 })
#             else:
#                 salida.append({
#                     'id_venta': lista[i]['id_venta'],
#                     'fecha': lista[i]['fecha'],
#                     'direccion': lista[i]['direccion'],
#                     'entrega': lista[i]['entrega'],
#                     'productos' : [
#                         {
#                         'nombre': lista[i]['nombre'],
#                         'descripcion': lista[i]['descripcion'],
#                         'cantidad': lista[i]['cantidad'],
#                         'precio': lista[i]['precio']
#                         }
#                     ]
#                 })
#     return render_template('micuenta.html', U = current_user, L = salida)

# @usu.route('/micuenta_editar', methods=['GET','POST'])
# def micuenta_editar():
#     if current_user.rol == 'baneado':
#         flash('Este usuario esta baneado')
#         return redirect(url_for('usu.login'))
#     if request.method == 'POST':
#         if request.form.get('accion') == 'update':
#             id = request.form.get('id')
#             nombre = request.form.get('nombre')
#             apellidoP = request.form.get('apellidoP')
#             apellidoM = request.form.get('apellidoM')
#             correo = request.form.get('correo')

#             user = Usuarios.query.filter_by(correo=correo).filter(Usuarios.id != id).all()
#             if user:
#                 flash('El Correo ya esta siendo usado por otra cuenta')
#                 return redirect(url_for('usu.micuenta_editar'))
            
#             Usuarios.usuariosUpdate(id,nombre,apellidoP,apellidoM,correo)
#             return 'update'
            
#         if request.form.get('accion') == 'pass':
#             id = request.form.get('id')
#             pass1 = request.form.get('pass1')
#             pass2 = request.form.get('pass2')

#             if not pass1 == pass2:
#                 flash('La contraseñas no son iguales')
#                 return redirect(url_for('usu.micuenta_editar'))
#             pas = generate_password_hash(pass1, method='sha256')
#             Usuarios.usuariosNuevaContrasena(id,pas)
#             return 'new password'
#     return redirect(url_for('usu.micuenta'))


@usu.route('/usuarios', methods=['GET','POST'])
def usuarios():
    U = usuariosF.Select()
    ADMIN = [{'id_usuario':id, 'nombre':nom, 'correo':c,'rol':r} for id,nom,c,r in U[0]]
    EMPLE = [{'id_usuario':id, 'nombre':nom, 'correo':c,'rol':r} for id,nom,c,r in U[1]]
    COMUN = [{'id_usuario':id, 'nombre':nom, 'correo':c,'rol':r} for id,nom,c,r in U[2]]
    BANN = [{'id_usuario':id, 'nombre':nom, 'correo':c,'rol':r} for id,nom,c,r in U[3]]

    return render_template("usu/usuarios.html",ADMIN=ADMIN,COMUN=COMUN,EMPLE=EMPLE,BANN=BANN)

@usu.route('/usuarios_rol', methods=['GET','POST'])
def usuarios_rol():
    usuariosF.UpdateRol(request.args.get('id'),request.args.get('es'))
    return redirect(url_for('usu.usuarios'))

# @usu.route('/usuarios_new_pass', methods=['GET','POST'])
# def usuarios():
#     return
@usu.route("/usuarios_delete", methods=['GET','POST'])
def medicamentos_delete():
    u = tbl_usuarios.query.get(request.args.get('id'))
    u.rol = 'BORRADO'
    db.session.commit()
    db.session.close()

    return redirect(url_for('med.medicamentos'))

@usu.route('/usuarios_detalles', methods=['GET','POST'])
def usuarios_detalles():
    usuario = tbl_usuarios.query.get(4)
    tratamientos = usuariosF.SelectOneData(usuario.id_usuario)

    create_form = validaciones.usuarios(request.form)
    
    create_form.id_usuario.data = usuario.id_usuario
    create_form.nombre.data = usuario.nombre
    create_form.apellidoP.data = usuario.apellidoP
    create_form.apellidoM.data = usuario.apellidoM
    create_form.correo.data = usuario.correo
    

    tratamientos_json = [
        {'id':id, 'medicina':med, 'inicio': ini,'final':fin,'precio':pre,'horarios':[
            json.loads(h) for h in json.loads(hor)
            ]
        }
        for id,med,ini,fin,pre,hor in tratamientos
    ]

    if request.method == 'POST':
        
        u = tbl_usuarios.query.get(request.form.get('id_usuario'))
        u.nombre = request.form.get('nombre')
        u.apellidoP = request.form.get('apellidoP')
        u.apellidoM = request.form.get('apellidoM')
        u.correo = request.form.get('correo')
        db.session.commit()
        db.session.close()

        return redirect(url_for('usu.usuarios_detalles'))   


    return render_template("usu/usuarios_edit.html", lista = tratamientos_json, U=usuario, form = create_form)