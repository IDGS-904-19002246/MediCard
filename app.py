import flask
from flask import session,make_response
from flask_wtf.csrf import CSRFProtect
from flask import jsonify

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask import render_template, request, redirect, url_for, jsonify, flash

from flask_security import Security
from flask_security import SQLAlchemyUserDatastore

from config import DevelopmentConfigRoot
from rutas.usuarios import usu
from rutas.medicamentos import med
# from rutas.productos import pro
# from rutas.insumos import ins
# from rutas.cocina import coc
# GOOGLE

# from model import db
from config import db
import validaciones
# MODELOS
from modelos.M_horarios import tbl_horarios
from modelos.M_medicamentos import tbl_medicamentos
from modelos.M_tratamientos import tbl_tratamientos
from modelos.M_usuarios import tbl_usuarios

# from modelos.usuariosM import Usuarios0
# from modelos.productosM import Productos
# GOOGLE
from flask_oauthlib.client import OAuth
import os

# ---------------------------------------------------------------------------------
app = flask.Flask(__name__)
app.config.from_object(DevelopmentConfigRoot)
csrf = CSRFProtect()
security = Security()

app.register_blueprint(usu)
app.register_blueprint(med)


app.secret_key ='AIzaSyD4_E5TLG6v20vgbWa9OJsbOSgei68q2HE'
oauth = OAuth(app)

google = oauth.remote_app(
    'google',
    consumer_key='585953638316-5s8ml6ebr08c0sevi671elu4tksjm7jj.apps.googleusercontent.com',
    consumer_secret='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',
    request_token_params={
        'scope': 'email',
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)
# app.register_blueprint(ins)
# app.register_blueprint(coc)



login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'usu.login'
login_manager.login_message = u"Por Favor, Inicie Sesión."

@login_manager.user_loader
def load_user(user_id): return tbl_usuarios.query.get(int(user_id))
# def load_user(user_id): return session.get(tbl_usuarios, int(user_id))




@app.route("/index", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def index():
    medicinas = tbl_medicamentos.query.all()
    medicinas_json = [{"id": medicina.id_medicamento, "nombre": medicina.nombre, "fabricante": medicina.fabricante} for medicina in medicinas]
    return jsonify(medicinas_json)


    # return render_template('index.html', current_user=current_user, )


@app.route("/nosotros", methods=['GET'])
def nosotros(): return render_template('nosotros.html',current_user=current_user)

        # return google.authorize(callback=url_for('authorized', _external=True))

@app.route("/login_google")
def login_google():
    return google.authorize(callback=url_for('authorized', _external=True))

# @app.route("/login", methods=['GET','POST'])
# def login_post():
#     create_form = validaciones.login(request.form)
#     if request.method == 'POST' and create_form.validate():
#         correo = request.form.get('correo')
#         contrasena = request.form.get('contrasena')
#         U = tbl_usuarios.query.filter_by(correo=correo).first()

#         if not U or not check_password_hash(U.contrasena, contrasena) :
#             flash('El usuario y/o la contraseña son incorrectos')
#             return render_template('login.html')
#         if U.rol == 'baneado':
#             flash('Este usuario esta baneado')
#             return redirect(url_for('usu.login'))
#         login_user(U)
#         return redirect(url_for('index'))
    
        
# --------------------------------------------------------------------------------------
# @app.route('/')
# def index():
#     return '¡Bienvenido a tu aplicación Flask! <a href="/login">Iniciar sesión con Google</a>'


@app.route('/login2', methods=['GET','POST'])
def login2(): return google.authorize(callback=url_for('authorized', _external=True))

# @app.route('/logout')
# def logout():
#     session.pop('google_token', None)
#     return redirect(url_for('index'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    session.pop('google_token', None)
    response = make_response(redirect(url_for('app.login')))
    return response
    

@app.route('/login/authorized')
@google.authorized_handler
def authorized(resp):
    if resp is None or resp.get('access_token') is None:
        return 'Acceso denegado: razón=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )

    session['google_token'] = (resp['access_token'], '')
    user_info = google.get('userinfo')

    # user_info.data['given_name']
    # {'id': '117574744195465502937', 'email': '19002246@alumnos.utleon.edu.mx', 'verified_email': True, 'picture': 'https://lh3.googleusercontent.com/a/default-user=s96-c', 'hd': 'alumnos.utleon.edu.mx'}
    return redirect(url_for('index'))
    return str(user_info.data)

@google.tokengetter
def get_google_oauth_token(): return session.get('google_token')


# app.register_blueprint(pro)

if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True)
