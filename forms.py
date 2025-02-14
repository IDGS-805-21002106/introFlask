from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, RadioField, IntegerField, EmailField

class UserForm(Form):
    matricula=StringField('matricula')
    nombre=StringField('Nombre')
    apellido=StringField('Apellido')
    email=EmailField('correo')

