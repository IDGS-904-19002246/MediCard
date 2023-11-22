from wtforms import Form
from wtforms import StringField,IntegerField,DateField,EmailField, TextAreaField,FileField,PasswordField

from wtforms import validators
# !"#$%&'()*+,-./:;<=>?@[]^_`{|}~ 
CaracteresNoValidos = [
    '!',
    '"',
    '#',
    '$',
    '%',
    '&',
    "'",
    '(',
    ')',
    '*',
    '+',
    ',',
    # '-',
    # '.',
    '/',
    ':',
    ';',
    '<',
    '=',
    '>',
    '?',
    # '@',
    '[',
    ']',
    '^',
    # '_',
    '`',
    '{',
    '|',
    '}',
    '~', 
]

def Valido(form,field):
    if len(str(field.data)) != 0:
        for c in str(field.data):
            if c in CaracteresNoValidos:
                raise validators.ValidationError('''El campo no debe contener ninguno de estos caracteres !#$%&'()*+,/:;<=>?[]^`{|}~"''')

def NoVacio(form,field):
    if len(str(field.data)) == 0:
        raise validators.ValidationError('El campo no tiene datos')
    
def NoNumeros(form,field):
    if len(str(field.data)) != 0:
        for c in str(field.data):
            if c.isalpha() != True and c != ' ' or c in [0,1,2,3,4,5,6,7,8,9]:
                raise validators.ValidationError('El campo no debe contener números')
            
def NoEspacios(form,field):
    if len(str(field.data)) != 0:
        if ' ' in str(field.data):
            raise validators.ValidationError('El campo no debe contener números ni espacios')
        
def Numeros(form,field):
    if len(str(field.data)) != 0:
        if ' ' in str(field.data) or str(field.data).isnumeric() == False:
            raise validators.ValidationError('El campo debe contener solo números y sin espacios')

class usuarios(Form):
    id_usuario = IntegerField('id_usuario')
    nombre = StringField('Nombre',[validators.DataRequired(message='Dato requerido'),Valido])

    apellidoP = StringField('Apellido Paterno',[NoVacio,NoNumeros,Valido])
    apellidoM = StringField('Apellido Materno',[NoVacio,NoNumeros,Valido])
    
    correo = EmailField('Correo',[validators.Email(message='Dame un correo valido'),NoVacio,NoEspacios,Valido])
    contrasena = PasswordField('Contraseña',[NoVacio,validators.length(min=4,max=16,message='La contraseña debe tener entre 4 y 16 caracteres'),Valido])
    contrasena2 = PasswordField('Repita su Contraseña',[NoVacio,validators.length(min=4,max=16,message='La contraseña debe tener entre 4 y 16 caracteres'),Valido])

class medicamentos(Form):
    id_medicamento = IntegerField('id_medicamento')
    nombre = StringField('Nombre',[validators.DataRequired(message='Dato requerido'),Valido])
    fabricante = StringField('Fabricante',[validators.DataRequired(message='Dato requerido'),Valido])
    cantidad = IntegerField('Cantidad',[NoVacio,Numeros,Valido])
    estado = StringField('Estado')
    medida = StringField('Medida')
    tipo = IntegerField('Tipo')

class login(Form):
    correo = EmailField('Correo',[validators.Email(message='Dame un correo valido'),NoVacio,NoEspacios,Valido])
    contrasena = PasswordField('Contraseña',[NoVacio,validators.length(min=4,max=16,message='La contraseña debe tener entre 4 y 16 caracteres'),Valido])
    

# ----------------------------------------------------------------------------------------------------------------------

class productos(Form):
    id_producto = IntegerField('id_producto')
    nombre = StringField('Nombre',[validators.DataRequired(message='Dato requerido')])

    cantidad = IntegerField('Cantidad (Existencias)',[validators.Optional(),validators.number_range(min=0,message='El campo no puede ser menor a 0')])
    cantidad_min = IntegerField('Cantidad Minima',[validators.DataRequired(message='Dato requerido'),validators.number_range(min=1,message='El campo no puede ser 0')])
    precio_U = IntegerField('Precio por Unidad',[validators.DataRequired(message='Dato requerido'),validators.number_range(min=1,message='El campo no puede ser 0')])
    precio_M = IntegerField('Precio Mayoreo',[validators.DataRequired(message='Dato requerido'),validators.number_range(min=1,message='El campo no puede ser 0')])
    img = FileField('Imagen')
    proceso = TextAreaField('Proceso',[validators.DataRequired(message='Dato requerido')])
    descripcion = TextAreaField('Descripción',[validators.DataRequired(message='Dato requerido')])


class insumos(Form):
    nombre = StringField('Nombre',[validators.length(min=4,max=32,message='El nombre debe tener entre 8 y 32 caracteres')])
    cantidad = IntegerField('Cantidad',[validators.Optional(),validators.number_range(min=1,message='El valor no puede ser menor a 0')])
    cantidad_min = IntegerField('Cantidad Mínima',[validators.number_range(min=1,message='El valor no puede ser menor a 1')])



class UserForm(Form):
    id = IntegerField('id',
        [validators.number_range
        (min=1,max=100,message='valor no valido')])
    nombre = StringField('Nombre',[NoNumeros,NoVacio])

    apaterno = StringField('Apellido Paterno',[NoVacio,NoNumeros])
    
    email = EmailField('correo',[validators.Email(message='Dame un correo valido'),NoVacio,NoEspacios])
    
class Profes(Form):
    id = IntegerField('id')
    nombre = StringField('Nombre',[NoNumeros,NoVacio])
    
    apaterno = StringField('Apellido Paterno',[NoVacio,NoNumeros])
    
    email = EmailField('email',[validators.Email(message='Dame un correo valido'),NoVacio,NoEspacios])
    
    sueldo = IntegerField('sueldo',
        [
        validators.DataRequired(message='Dato requerido'),
        validators.number_range(min=200,max=100000,message='Valor no valido')])
    telefono = StringField('telefono',
        [
        validators.DataRequired(message='Dato requerido'),
        validators.length(min=10,max=10,message='Ingrese 10 numeros'),Numeros])