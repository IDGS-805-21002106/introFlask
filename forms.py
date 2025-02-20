from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, RadioField, IntegerField, EmailField, RadioField
from wtforms import validators, EmailField

class UserForm(Form):
    matricula=StringField('matricula', [
        validators.DataRequired(message= "El campo es requerido"),
        validators.length(min=3, max=10, message="El campo debe tener entre 3 y 10 caracteres")
    ]
    )
    nombre=StringField('Nombre',  [
        validators.DataRequired(message= "El campo es requerido"),
    ])
    apellido=StringField('Apellido', [
        validators.DataRequired(message= "El campo es requerido"),
    ])
    email=EmailField('correo', [
        validators.Email(message="Ingrese un correo valido")
    ])
    

