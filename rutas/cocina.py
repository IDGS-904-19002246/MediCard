from flask import Blueprint, redirect, render_template, url_for,request, flash,make_response
from flask_login import LoginManager, login_user, login_required, logout_user,current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
import json
from flask_security.decorators import roles_required

from werkzeug.utils import secure_filename
import os

from db import get_connection
import validaciones
from config import db
import sys
sys.path.append("..")
from modelos.productosM import Productos
from modelos.ventasM import Ventas
from modelos.insumosM import Insumos,Proveedores


coc = Blueprint('coc',__name__)


@coc.route("/entregar", methods=['GET','POST'])
def entregar():
    V = db.session.query(Ventas).filter(Ventas.id_venta == request.form.get('id')).first()
    V.entrega = 1
    db.session.add(V)
    db.session.commit()
    return redirect(url_for('coc.cocina'))

@coc.route("/cocinar", methods=['GET','POST'])
def cocinar():
    N = int(request.form.get('can'))
    ids = int(request.form.get('id'))
    R = Insumos.InsumosCocinando(ids)

    P = db.session.query(Productos).filter( Productos.id_producto == ids and Productos.estado == 'ok').first()
    P.pendientes = 0
    P.cantidad += N
    db.session.add(P)
    db.session.commit()

    lista = []
    for r in R: lista.append({"id":r[0],"cantidadUno":r[1],"caducidad": json.loads(r[2]),"catidadTotal":r[3]})
    # lista[1]['caducidad'][0]['can']=40
    ind = 0
    ind2 = 0
    f = ''
    necesario = 0
    for l in lista:
        if l['caducidad'][0] == 'nada':
            f+= 'No P <br>'
            I = db.session.query(Insumos).filter(Insumos.id_insumo == l['id']).first()
            I.cantidad -= int(l['cantidadUno']) * N
            db.session.add(I)
            db.session.commit()
        else:
            f+= 'Si P <br>'
            necesario = int(l['cantidadUno']) * N

            while necesario > 0:
                necesario = necesario - l['caducidad'][0]['can']
                if necesario < 0:
                   lista[ind]['caducidad'][ind2]['can'] = (necesario * (-1))
                   break
                if necesario == 0: break
                if necesario > 0:
                    del l['caducidad'][0]
                    ind2 -= 1
                ind2 += 1
            total = 0

            for ll in l['caducidad']: total += ll['can']
            I = db.session.query(Insumos).filter(Insumos.id_insumo == lista[ind]['id']).first()
            I.cantidad = total
            # xx = lista[ind]['caducidad']
            I.caducidad = lista[ind]['caducidad']
            db.session.add(I)
            db.session.commit()
        ind += 1
    

    # Insumos.InsumosCocinar(request.form.get('id'),request.form.get('can'))
    return redirect(url_for('coc.cocina'))

@coc.route("/cocina_eliminar", methods=['GET','POST'])
def cocina_eliminar():
    P = db.session.query(Productos).filter(Productos.id_producto == int(request.args.get('id'))).first()
    P.pendientes = 0
    db.session.add(P)
    db.session.commit()
    return redirect(url_for('coc.cocina'))

@coc.route("/cocina", methods=['GET','POST'])
def cocina():
    if current_user.rol == 'baneado':
        flash('Este usuario esta baneado')
        return redirect(url_for('usu.login'))
    pro = db.session.query(Productos.id_producto, Productos.nombre, Productos.pendientes).filter(Productos.pendientes != 0).all()
    ven = Ventas.ventasSelectPendientes()
    lista = []
    salida = []

    for v in ven:
        lista.append({
            'id_venta': v[0],
            'nombre': v[1],
            'descripcion': v[2],
            'cantidad': v[3],
            'precio': v[4],
            'fecha': v[5],
            'direccion': v[6],
            'entrega': v[7],
            'cliente': v[8]
        })

    for i in range(len(lista)):
        if i == 0:
            salida.append({
                'id_venta': lista[i]['id_venta'],
                'fecha': lista[i]['fecha'],
                'direccion': lista[i]['direccion'],
                'entrega': lista[i]['entrega'],
                'cliente': lista[i]['cliente'],
                'costo': lista[i]['cantidad']*lista[i]['precio'],
                'productos' : [
                        {
                        'nombre': lista[i]['nombre'],
                        'descripcion': lista[i]['descripcion'],
                        'cantidad': lista[i]['cantidad'],
                        'precio': lista[i]['precio']
                        }
                    ]
                }
            )
        else:
            if lista[i]['id_venta'] == lista[i-1]['id_venta']:
                salida[-1]['costo'] += lista[i]['cantidad']*lista[i]['precio']
                salida[-1]['productos'].append({
                    'nombre': lista[i]['nombre'],
                    'descripcion': lista[i]['descripcion'],
                    'cantidad': lista[i]['cantidad'],
                    'precio': lista[i]['precio']
                })
            else:
                salida.append({
                    'id_venta': lista[i]['id_venta'],
                    'fecha': lista[i]['fecha'],
                    'direccion': lista[i]['direccion'],
                    'entrega': lista[i]['entrega'],
                    'cliente': lista[i]['cliente'],
                    'costo': lista[i]['cantidad']*lista[i]['precio'],
                    'productos' : [
                        {
                        'nombre': lista[i]['nombre'],
                        'descripcion': lista[i]['descripcion'],
                        'cantidad': lista[i]['cantidad'],
                        'precio': lista[i]['precio']
                        }
                    ]
                })

    return render_template('cocina_y _envios.html', P = pro, V = salida,current_user=current_user)


@coc.route("/ventas", methods=['GET','POST'])
def ventas():
    if current_user.rol == 'baneado':
        flash('Este usuario esta baneado')
        return redirect(url_for('usu.login'))
    ven = Ventas.ventasSelectMes(request.args.get('f'))
    finanzas = Ventas.ventasTotal(request.args.get('f'))
    compras = Ventas.comprasSelectMes(request.args.get('f'))

    listaC = []
    for c in compras:listaC.append({'nombre':c[0],'correo':c[1],'telefono':c[2],'nombreI':c[3],'cantidad':c[4],'fecha':c[5],'costo':c[6],'medida':c[7]})

    lista = []
    salida = []

    for v in ven:
        lista.append({
            'id_venta': v[0],
            'nombre': v[1],
            'descripcion': v[2],
            'cantidad': v[3],
            'precio': v[4],
            'fecha': v[5],
            'direccion': v[6],
            'entrega': v[7],
            'cliente': v[8]
        })

    for i in range(len(lista)):
        if i == 0:
            salida.append({
                'id_venta': lista[i]['id_venta'],
                'fecha': lista[i]['fecha'],
                'direccion': lista[i]['direccion'],
                'entrega': lista[i]['entrega'],
                'cliente': lista[i]['cliente'],
                'costo': lista[i]['cantidad']*lista[i]['precio'],
                'productos' : [
                        {
                        'nombre': lista[i]['nombre'],
                        'descripcion': lista[i]['descripcion'],
                        'cantidad': lista[i]['cantidad'],
                        'precio': lista[i]['precio']
                        }
                    ]
                }
            )
        else:
            if lista[i]['id_venta'] == lista[i-1]['id_venta']:
                salida[-1]['costo'] += lista[i]['cantidad']*lista[i]['precio']
                salida[-1]['productos'].append({
                    'nombre': lista[i]['nombre'],
                    'descripcion': lista[i]['descripcion'],
                    'cantidad': lista[i]['cantidad'],
                    'precio': lista[i]['precio']
                })
            else:
                salida.append({
                    'id_venta': lista[i]['id_venta'],
                    'fecha': lista[i]['fecha'],
                    'direccion': lista[i]['direccion'],
                    'entrega': lista[i]['entrega'],
                    'cliente': lista[i]['cliente'],
                    'costo': lista[i]['cantidad']*lista[i]['precio'],
                    'productos' : [
                        {
                        'nombre': lista[i]['nombre'],
                        'descripcion': lista[i]['descripcion'],
                        'cantidad': lista[i]['cantidad'],
                        'precio': lista[i]['precio']
                        }
                    ]
                })

    return render_template('ventas.html', V = salida,current_user=current_user,F=finanzas, C = listaC)



@coc.route("/proveedores", methods=['GET','POST'])
def proveedores():
    if current_user.rol == 'baneado':
        flash('Este usuario esta baneado')
        return redirect(url_for('usu.login'))
    P = db.session.query(Proveedores).all()
    lista = []
    if request.args.get('proveedor'):
        P1 = Proveedores.ProveedoresSelectUno(request.args.get('proveedor'))
        for p in P1: lista.append({"empresa":p[0],"insumo":p[1],"cantidad":p[2],"costo":p[3],"fecha":p[4]})
    return render_template('proveedores.html', P = P, L = lista)

@coc.route("/formulario", methods=['GET','POST'])
def formulario():
    if request.method == 'POST':
        if not request.form.get('id'):
            newP = Proveedores(
                nombre = request.form.get('nombre'),
                correo = request.form.get('correo'),
                telefono = request.form.get('telefono'),
                direccion = [
                    request.form.get('calle'),
                    int(request.form.get('num')),
                    request.form.get('colonia'),
                    request.form.get('ciudad')]
            )
        else:
            newP = db.session.query(Proveedores).filter(Proveedores.id_proveedor == request.form.get('id')).first()
            newP.nombre = request.form.get('nombre'),
            newP.correo = request.form.get('correo'),
            newP.telefono = request.form.get('telefono'),
            newP.direccion = [
                request.form.get('calle'),
                int(request.form.get('num')),
                request.form.get('colonia'),
                request.form.get('ciudad')]
        db.session.add(newP)
        db.session.commit()
    return redirect(url_for('coc.proveedores'))
