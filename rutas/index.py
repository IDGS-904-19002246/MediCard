from flask import Blueprint, redirect, render_template, url_for,request, flash
from flask_login import LoginManager, login_user, login_required, logout_user,current_user
from werkzeug.security import generate_password_hash, check_password_hash
import json

from db import get_connection
from config import db
from datetime import datetime
# from model import Usuarios

from flask import Flask, render_template
import plotly.express as px
from plotly.offline import plot
from plotly.utils import PlotlyJSONEncoder
import io
import base64

from modelos.M_usuarios import tbl_usuarios, usuariosF
# pip install Flask matplotlib
# pip install pandas
# pip install plotly



import sys
sys.path.append("..")
from modelos.M_comentarios import tbl_comentarios
from modelos.M_graficas import graficasF
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
    
@ind.route("/dashboard", methods=['GET','POST'])
@login_required
def dashbord():
    usuario = current_user
    if usuario.rol != 'ADMIN': return redirect(url_for('index'))
    fecha = str(datetime.now())[:10]
    # if method.
    if request.method == 'POST':
        fecha =  str(datetime(
            int(request.form.get('anyo')),
            int(request.form.get('mes')), 1))[:10]
    medicinas7_grudo = graficasF.grafica_top7medicinas(fecha)
    medicinas7 = {G[0]: G[1] for G in medicinas7_grudo}

    graficaUsuarios = [{
        'usu':G[0],
        'tra':G[1]
        }for G in graficasF.grafica_top7usuarios(fecha)]

    pastel_crudo = graficasF.grafica_pastelEmpresas(fecha)
    pastel_label = [G[0] for G in pastel_crudo]
    pastel_values = [G[1] for G in pastel_crudo]

    tipos_grudo = graficasF.grafica_lineas(fecha)
    tipos = {G[0]: G[1] for G in tipos_grudo}
    # data = {
    #     'x':[1,2,3,4],
    #     'y1':[1,3,5,6],
    #     'y2':[1,66,6,90]
    #     }

    # fig  = px.line(data, x ='x', y=['y1','y2'], labels={'value':'Valor','variable':'lineas'})
    # fig_html = fig.to_html(full_html = False)
# -----------------------------------------------------------------------------------------
    # Generar la gráfica de barras con Plotly
    medicinas_ok = px.bar(x=list(medicinas7.keys()), y=list(medicinas7.values()),
        labels={'x':'Medicamento', 'y':'Tratamientos'}, title='Top 7 Medicamentos')
    # Guardar la gráfica en formato HTML
    medicinas_html = plot(medicinas_ok, output_type='div')

    pastel_cocinado = px.pie(names= pastel_label, values=pastel_values,title='Empresas con más presencia')
    pastel_html = pastel_cocinado.to_html(full_html = False)

    tipos_ok = px.bar(x=list(tipos.keys()), y=list(tipos.values()),
        labels={'x':'Categorias', 'y':'Tratamientos'}, title='Top 7 cartegorias con mas precencia ')
    # Guardar la gráfica en formato HTML
    tipo_html = plot(tipos_ok, output_type='div')

    return render_template(
        'index/dashboard.html',
        medicinas_html=medicinas_html,
        usu = graficaUsuarios,
        pastel_html = pastel_html,
        tipo_html = tipo_html,
        mes = fecha[5:7]
        )





# def generate_bar_chart(data):
#     # Crear una gráfica de barras
#     plt.bar(data.keys(), data.values())
#     plt.xlabel('Categorías')
#     plt.ylabel('Valores')
#     plt.title('Gráfica de Barras')

#     # Guardar la gráfica en un objeto BytesIO
#     img = BytesIO()
#     plt.savefig(img, format='png')
#     img.seek(0)
#     plt.close()

#     return img