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
import io
import base64
# pip install Flask matplotlib
# pip install pandas



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
    
@ind.route("/dashbord")
def dashbord():


    data = {'Categoría 1': 20, 'Categoría 2': 35, 'Categoría 3': 15}

    # Generar la gráfica de barras con Plotly
    fig = px.bar(x=list(data.keys()), y=list(data.values()), labels={'x':'Categorías', 'y':'Valores'}, title='Gráfica de Barras')

    # Guardar la gráfica en formato HTML
    graph_html = plot(fig, output_type='div')

    return render_template('index/dashbord.html', graph_html=graph_html)
    return render_template('index/dashbord.html')


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