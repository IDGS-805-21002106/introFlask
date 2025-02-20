from flask import Flask, render_template, request
import forms
import formszodiaco
from datetime import datetime


app = Flask(__name__)

@app.route("/")
def index():
    titulo = "IDGS805"
    lista = ["pedro", "juan", "jorge"]
    return render_template("index.html", titulo =titulo, lista= lista)


@app.route("/alumnos", methods=["GET", "POST"])
def alumnos():
    mat= ''
    nom=''
    ape=''
    email=''
    alumno_class=forms.UserForm(request.form)
    if request.method == "POST" and alumno_class.validate():
        mat= alumno_class.matricula.data
        ape= alumno_class.apellido.data
        nom= alumno_class.nombre.data
        email= alumno_class.email.data
        print("Nombre {}".format(nom))
    return render_template("alumnos.html",form= alumno_class, mat=mat, nom=nom, ape=ape, email=email)

@app.route("/zodiaco", methods=["GET", "POST"])
def zodiaco():
    nom=''
    apePaterno=''
    apeMaterno=''
    sexo =''
    fecha=''
    imagenZ = ''
    zodiaco_class= formszodiaco.ZodiacoForm(request.form)
    if request.method == "POST" and zodiaco_class.validate():
        apePaterno= zodiaco_class.apellidoPaterno.data
        nom= zodiaco_class.nombre.data
        sexo= zodiaco_class.sexo.data
        fecha= zodiaco_class.fecha.data
        apeMaterno = zodiaco_class.apellidoMaterno.data
        if fecha:
            hoy = datetime.today()
            edad = hoy.year - fecha.year - ((hoy.month, hoy.day) < (fecha.month, fecha.day))
    añoNacimiento = fecha.year
    signoZ = [
                "mono", "gallo", "perro", "cerdo", "rata", "buey", 
                "tigre", "conejo", "dragon", "serpiente", "caballo", "cabra"
            ]
    signoChino = signoZ[añoNacimiento % 12]
    imagenZ = "img/{}.png".format(signoChino)
    return render_template("zodiaco.html",form= zodiaco_class, nom=nom, apePaterno=apePaterno, apeMaterno=apeMaterno, sexo=sexo, fecha=fecha, edad=edad, signoChino= signoChino, imagenZ= imagenZ)

@app.route("/ejemplo1")
def ejemlo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejemlo2():
    return render_template("ejemplo2.html")


@app.route("/Hola")
def hola():
    return "<h1>Holaa mundo</h1>"

@app.route("/user/<string:user>")
def user(user):
    return f"Hola, {user}"

@app.route("/numero/<int:n>")
def numero(n):
    return f"El numero es: {n}"

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return f"el usuario es : {username} con id: {id}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f"La suma es {n1 + n2}"

@app.route("/form1")
def form():
    return '''
            <form>
            <label for= "nombre"> Nombre: </label>
            <input type="text" id="nombre" required>
            '''

@app.route("/operaBas")
def opera():
    return render_template("operaBas.html")

@app.route("/resultado", methods=["GET", "POST"])
def resulttado():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        op = request.form.get("opcion")
        if op == "suma":
            resultado = "La suma de {} + {} = {}".format(num1, num2, str(int(num1) + int(num2)))
            return render_template("operaBas.html", resultado = resultado)
        if op == "resta":
            resultado = "La resta de {} - {} = {}".format(num1, num2, str(int(num1) - int(num2)))
            return render_template("operaBas.html", resultado = resultado)
        if op == "multiplicacion":
            resultado = "La multiplicacion de {} X {} = {}".format(num1, num2, str(int(num1) * int(num2)))
            return render_template("operaBas.html", resultado = resultado)
        if op == "division":
            resultado = "La division de {} / {} = {}".format(num1, num2, str(int(num1) / int(num2)))
            return render_template("operaBas.html", resultado = resultado)

@app.route("/cinepolis")
def cine():
    return render_template("cinepolis.html")

@app.route("/cinepolisRes", methods=["POST"])
def cine_res():
    nombre = request.form["nombre"]
    compradores = int(request.form["compradores"])
    boletos = int(request.form["boletos"])
    tarjeta = request.form["opcion"] == "cinecosi"
    precioBoleto = 12
    boletosPosibles = compradores * 7

    if boletos > boletosPosibles:
        error = "No puedes comprar más de 7 boletos por persona."
        return render_template("cinepolis.html", error=error)

    if boletos > 5:
        descuento = 0.15
    elif 3 <= boletos <= 5:
        descuento = 0.10
    else:
        descuento = 0

    total_compra = boletos * precioBoleto
    total_compra -= total_compra * descuento

    if tarjeta:
        total_compra -= total_compra * 0.10

    return render_template("cinepolis.html", total=total_compra)

if __name__ == "__main__":
    app.run(debug=True, port=3000)