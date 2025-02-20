from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, RadioField, IntegerField, EmailField, DateField
from wtforms import validators, EmailField

class ZodiacoForm(Form):
    nombre=StringField('Nombre',  [
        validators.DataRequired(message= "El campo es requerido"),
    ])
    apellidoPaterno=StringField('Apellido Paterno', [
        validators.DataRequired(message= "El campo es requerido"),
    ])
    apellidoMaterno=StringField('Apellido Materno', [
        validators.DataRequired(message= "El campo es requerido"),
    ])
    sexo=RadioField('Sexo', choices=[('Masculino','Masculino'),('Femenino','Femenino')])

    fecha= DateField('Fecha', format='%Y-%m-%d')
