from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    titulo = "IDGS805"
    lista = ["pedro", "juan", "jorge"]
    return render_template("index.html", titulo =titulo, lista= lista)


@app.route("/ejemlo1")
def ejemlo1():
    return render_template("ejemplo1.html")

@app.route("/ejemlo2")
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


if __name__ == "__main__":
    app.run(debug=True, port=3000)