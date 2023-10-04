from flask import Blueprint, redirect, render_template, url_for,request, flash,make_response
from flask_login import LoginManager, login_user, login_required, logout_user,current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_required, current_user

from datetime import date
import json

from werkzeug.utils import secure_filename
import os

from db import get_connection
import validaciones
from config import db
import sys
sys.path.append("..")

from modelos.M_medicamentos import tbl_medicamentos, medicamentosF
# from modelos.productosM import Productos
# from modelos.ventasM import Ventas
# from modelos.insumosM import Insumos


med = Blueprint('med',__name__)

@med.route("/medicamentos", methods=['GET','POST'])
def productos():
    med = medicamentosF.Select()
    medicinas = [
        {'id': id, 'nombre': nombre, 'fab': fab} for id, nombre, fab in med
        ]
    # medicinas = []
    # for me in med:
    #     medicinas.append(
    #         {
    #             'id':me[0],
    #             'nombre':me[1],
    #             'fabrica':me[2]
    #         }
    #     )

    return medicinas

    

    return str(med)
    ga =  Productos.ProductosSelectTodos()
    # galletas = []
    # for g in ga:
    #     galletas.append(            
    #         {
    #         'id_producto':g[0],
    #         'nombre':g[1].capitalize(),
    #         'cantidad':g[2],
    #         'cantidad_min':g[3],
    #         'precio_U':g[4],
    #         'precio_M':g[5],
    #         'proceso':g[6].capitalize(),
    #         'img':g[7],
    #         'descripcion':g[8].capitalize(),
    #         'estado':g[9]
    #         }
    #     )
    
    return render_template('productos.html', G=galletas)

# @pro.route("/detalles", methods=['GET','POST'])
# def detalles():
#     ga = Productos.ProductosSelectUno(request.args.get('id'))
#     reseta = Productos.ProductosSelectReseta(request.args.get('id'))
#     galletas = []
#     for g in ga:
#         galletas.append(            
#             {
#             'id_producto':g[0],
#             'nombre':g[1].capitalize(),
#             'cantidad':g[2],
#             'cantidad_min':g[3],
#             'precio_U':g[4],
#             'precio_M':g[5],
#             'proceso':g[6].capitalize(),
#             'img':g[7],
#             'descripcion':g[8].capitalize()
#             }
#         )
    
#     if request.method == 'POST':
#         cantidad = request.form.get('can') if request.form.get('can') != '' else 1

#         item = {str(request.form.get('id')) : int(cantidad)}
#         data = json.dumps(item)
#         response = make_response(redirect(url_for('pro.carrito')))

#         #REVISAR SI LA COOKIE EXIRTE O NO
#         if not request.cookies.get("carrito"):
#             carrito = []
#             carrito.append(item)
#             data = json.dumps(carrito)
#             response.set_cookie('carrito',data)
#             return response
#         #REVISAR SI EL PRODUCTO ESTA O NO EN EL CARRITO
#         carrito = json.loads(request.cookies.get("carrito"))
#         item_k = list(item)
#         esta = [False,'indice','clave']
#         for index, c in enumerate(carrito):
#             c_k = list(c.keys())
#             if c_k[0] == item_k[0] :
#                 esta[0] = True
#                 esta[1] = index
#                 esta[2] = c_k[0]
#                 break
#         if esta[0] == False:
#             carrito.append(item)
#         else:
#             carrito[esta[1]][esta[2]] = item[item_k[0]]
        
#         data = json.dumps(carrito)
#         response.set_cookie('carrito',data)
#         return response
    
#     return render_template('detalles.html', G=galletas,R=reseta,current_user=current_user)


# @pro.route("/carrito_edit", methods=['GET','POST'])
# @login_required
# def carrito_edit():
#     carrito = json.loads(request.cookies.get("carrito"))
#     response = make_response(redirect(url_for('pro.carrito')))
#     id = request.args.get('id')
#     n = int(request.args.get('n'))
#     l = int(request.args.get('l'))
#     #MODIFICAR PRODUCTOS DEL CARRITO, SI SE TIENE 1 Y SE RESTA 1 SE ELIMINA DEL CARRITO
#     for index, c in enumerate(carrito):
#         c_k = list(c.keys())
#         if  c_k[0] == id:
#             if str(n) == '0':
#                 carrito.remove(c)
#                 if len(carrito)==0:
#                     response.delete_cookie('carrito', domain="127.0.0.1")
#                     break
#                 data = json.dumps(carrito)
#                 response.set_cookie('carrito',data)
#                 break
#             else:
#                 if n <= l: carrito[index][c_k[0]] = n
#             data = json.dumps(carrito)
#             response.set_cookie('carrito',data)
#             break
#     return response


# @pro.route("/carrito", methods=['GET','POST'])
# @login_required
# def carrito():
#     carrito = request.cookies.get("carrito")
#     lista = []
    
#     #SE VERIFICA SI HAY PROCUCTOS EN EL CARRITO Y SI HAY LE DA FORMATO PARA EMVIARLO A LA VISTA
#     if not carrito: lista = ''
#     else:
#         carrito = json.loads(carrito)
#         for c in carrito:
#             c_k = list(c.keys())
#             I = Productos.ProductosSelectUno(c_k[0],)
#             if not len(I) == 0:
#                 lista.append(            
#                     {
#                     'id_producto':I[0][0],
#                     'nombre':I[0][1].capitalize(),
#                     'cantidad':I[0][2],
#                     'cantidad_min':I[0][3],
#                     'precio_U':I[0][4],
#                     'precio_M':I[0][5],
#                     'proceso':I[0][6].capitalize(),
#                     'img':I[0][7],
#                     'descripcion':I[0][8].capitalize(),
#                     'numero':c[c_k[0]]
#                     }
#                 )

#     if request.method == 'POST':
#         #GUARDAR VENTA
#         msg = Ventas.ventasInsert(int(current_user.id))

#         #SI SE LE AÑADIO ENVIO GUARDARLO
#         dir = str(request.form.get('dir'))
#         env = str(request.form.get('env'))
#         if env == 'on': Ventas.enviosInsert(dir)
        
#         #GUARDAR PRODUCTOS DE LA VENTA
#         for l in lista:
#             p = (l['precio_U'] * l['numero']) if 9 >= l['numero'] else (l['precio_M'] * l['numero']) 
#             msg += Ventas.venta_productoInsert(l['id_producto'], l['numero'], p)

#         response = make_response(redirect(url_for('pro.carrito')))
#         response.delete_cookie('carrito', domain="127.0.0.1")
#         flash('La compra se realizo con exito.')
#         return response
    
#     if current_user.rol == 'baneado':
#         flash('Esta usuario esta baneado')
#         return redirect(url_for('usu.login'))
    
#     if not current_user.is_authenticated:
#         response = make_response(redirect(url_for('pro.productos')))
#         response.delete_cookie('carrito', domain="127.0.0.1")
#         flash('Debe iniciar sesión para comprar')
#         return response
#     return render_template('carrito.html', C = lista,current_user=current_user)


# @pro.route("/productos_admin", methods=['GET','POST'])
# @login_required
# def productos_admin():
#     if current_user.rol == 'baneado':
#         flash('Este usuario esta baneado')
#         return redirect(url_for('usu.login'))
#     ga = Productos.ProductosSelectTodos()
#     galletas = []
#     msg = []
#     form = []
#     for g in ga:
#         galletas.append(            
#             {
#             'id_producto':g[0],'nombre':g[1].capitalize(),'cantidad':g[2],
#             'cantidad_min':g[3],'precio_U':g[4],'precio_M':g[5],
#             'proceso':g[6].capitalize(),'img':g[7],'descripcion':g[8].capitalize(),
#             'estado':g[9]
#             }
#         )
#     if request.method == 'POST':
#         if request.form.get('accion') == 'validar':
#             valido = Insumos.InsumosCocinarValidar( int(request.form.get('id_pro')), int(request.form.get('unidad'))) 
#             if len(valido) == 0:
#                 msg.append('El producto no tiene Reseta, añada una desde las opciones del producto')
#             else:
#                 for v in valido:
#                     if v[1] == 'no': msg.append('Faltan '+ str(v[2])+ ' '+ str(v[3])+ ' de '+ str(v[0]))
#             if len(msg) == 0:
#                 form.append(request.form.get('id_pro'))
#                 form.append(request.form.get('unidad'))
#         if request.form.get('accion') == 'cocinar':
#             P = db.session.query(Productos).filter(Productos.id_producto == request.form.get('id_pro')).first()
#             P.pendientes = request.form.get('unidad')
#             db.session.add(P)
#             db.session.commit()
#             return redirect(url_for('pro.productos_admin'))
#     return render_template('productos_admin.html', G=galletas, M = msg, F = form,current_user=current_user)

# @pro.route("/productos_editar", methods=['GET','POST'])
# @login_required
# def productos_editar():
#     if current_user.rol == 'baneado':
#         flash('Este usuario esta baneado')
#         return redirect(url_for('usu.login'))
#     create_form = validaciones.productos(request.form)
#     ga = Productos.ProductosSelectUno(request.args.get('id'))
#     if request.method == 'GET':
#         create_form.id_producto.data = ga[0][0]
#         create_form.nombre.data = ga[0][1]
#         create_form.cantidad.data = ga[0][2]
#         create_form.cantidad_min.data = ga[0][3]

#         create_form.precio_U.data = ga[0][4]
#         create_form.precio_M.data = ga[0][5]
#         create_form.proceso.data = ga[0][6]
#         create_form.img.data = ga[0][7]
#         create_form.descripcion.data = ga[0][8]

#     if request.method == 'POST' and create_form.validate():
#         nue = ''
#         if request.files and request.files['img'].filename != '':
#             file = request.files['img']
#             basepath = os.path.dirname(__file__)
#             filename = secure_filename(file.filename)
#             ext = os.path.splitext(filename)[1]
#             nue = request.form.get('id_producto')+'_'+request.form.get('nombre')+ext
#             up_path = os.path.join(basepath,'../static/img/productos/',nue)
#             file.save(up_path)
#         m = Productos.ProductosUpdate(
#             request.form.get('id_producto'),
#             request.form.get('nombre'),
#             request.form.get('cantidad'),
#             request.form.get('cantidad_min'),
#             request.form.get('precio_U'),
#             request.form.get('precio_M'),
#             request.form.get('proceso'),
#             nue,
#             request.form.get('descripcion')
#         )
#         return redirect(url_for('pro.productos_admin'))
#     return render_template('productos_editar.html', form = create_form,current_user=current_user)

# @pro.route("/productos_añadir", methods=['GET','POST'])
# @login_required
# def productos_añadir():
#     if current_user.rol == 'baneado':
#         flash('Este usuario esta baneado')
#         return redirect(url_for('usu.login'))
#     create_form = validaciones.productos(request.form)
#     ga = Productos.ProductosSelectUno(request.args.get('id'))
    
#     if request.method == 'POST' and create_form.validate():
#         file = request.files['img']
        
#         basepath = os.path.dirname(__file__)
#         filename = secure_filename(file.filename)

#         ext = os.path.splitext(filename)[1]
#         nue = request.form.get('nombre')+ext
        
#         up_path = os.path.join(basepath,'../static/img/productos/',nue)
#         file.save(up_path)
#         m = Productos.ProductosInsert(
#             # nom,can,can_min,pre_U,pre_M,pro,i,des
#             request.form.get('nombre'),
#             request.form.get('cantidad'),
#             request.form.get('cantidad_min'),
#             request.form.get('precio_U'),
            
#             request.form.get('precio_M'),
#             request.form.get('proceso'),
#             nue,
#             request.form.get('descripcion')

#         )
#         return redirect(url_for('pro.productos_admin'))
#     return render_template('productos_añadir.html', form = create_form,current_user=current_user)

# @pro.route("/ProductosDelete", methods=['GET','POST'])
# @login_required
# def ProductosDelete():
#     Productos.ProductosDelete(request.args.get('id'))
#     return redirect(url_for('pro.productos_admin'))

# @pro.route("/productos_reseta", methods=['GET','POST'])
# @login_required
# def productos_reseta():
#     if current_user.rol == 'baneado':
#         flash('Este usuario esta baneado')
#         return redirect(url_for('usu.login'))
#     reseta = Productos.ProductosSelectReseta(request.args.get('id'))
#     producto = Productos.ProductosSelectUno(request.args.get('id'))
#     insumos = Insumos.InsumosSelectTodos()

#     inputs = []
#     if not reseta == '()':
#         for r in reseta:inputs.append({"insumo":r[0],"cantidad":r[1],"medida":r[2],"id":r[3]})
    
#     if request.method == 'POST':
#         pro = request.form.get('producto')
#         R = db.session.query(Productos).filter(Productos.id_producto == pro).first()
#         R.proceso = request.form.get('proceso')
#         db.session.add(R)
#         db.session.commit()
#         Productos.resetasDelete(pro)
#         for id_ins in request.form:
#             if request.form[id_ins]:
#                 if not id_ins == 'producto' and not id_ins == 'csrf_token' and not id_ins == 'proceso':
#                     Productos.resetasInsert(pro,id_ins,request.form[id_ins])
#         return redirect(url_for('pro.productos_admin'))
#     return render_template('productos_reseta.html', R = reseta, P = producto, I = insumos, inputs = str(inputs),current_user=current_user)