from flask import Flask, render_template, request, redirect, url_for
from Estudiante import Estudiante
from Universidad import Universidad
from Facultad import Facultad
from Programa import Programa

app = Flask(__name__)

universidad = Universidad()


# Instancias de las clases
# Crear una instancia de Universidad
universidad = Universidad()

# Registrar facultad
facultad = Facultad(nombre="Ingeniería")
universidad.registrar_facultad(facultad)

# Registrar programa
programa = Programa(nombre="Ingeniería de Sistemas")
universidad.registrar_programa(programa, facultad_nombre="Ingeniería")

# Registrar un estudiante con datos básicos
estudiante = {
    "id": "101",
    "nombre": "Daniel",
    "apellido": "Zapata",
    "fecha_nacimiento": "1999-08-03",
    "sexo": "M",
    "antecedentes": "No",
}
universidad.registrar_estudiante(estudiante, programa_nombre="Ingeniería de Sistemas")

# Registrar un segundo estudiante
estudiante2 = {
    "id": "202",
    "nombre": "Carlos",
    "apellido": "Gómez",
    "fecha_nacimiento": "2000-05-15",
    "sexo": "M",
    "antecedentes": "Sí",
}
universidad.registrar_estudiante(estudiante2, programa_nombre="Ingeniería de Sistemas")

# Registrar datos de examen para el primer estudiante
datos_examen1 = {"cHDL": 45, "CT": 200}
universidad.registrar_datos_examen("101", datos_examen1)

# Registrar datos de examen para el segundo estudiante
datos_examen2 = {"cHDL": 50, "CT": 210}
universidad.registrar_datos_examen("202", datos_examen2)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registro_basico", methods=["GET", "POST"])
def registro_basico():
    if request.method == "POST":
        # Obtener los datos del formulario
        sexo = request.form["sexo"]
        fecha_nacimiento = request.form["fecha_nacimiento"]
        antecedentes = request.form["antecedentes"]

        # Actualizar la información del estudiante (ejemplo)
        estudiante.sexo = sexo
        estudiante.fecha_nacimiento = fecha_nacimiento
        estudiante.antecedentes = antecedentes

        # Registrar los cambios en la universidad
        universidad.registrar_estudiante(estudiante)
        

        return redirect(url_for("index"))
    
    return render_template("registro_basico.html")

@app.route("/registro_salud", methods=["GET", "POST"])
def registro_salud():
    if request.method == "POST":
        cHDL = request.form.get("cHDL")
        CT = request.form.get("CT")

        if  not cHDL or not CT:
            return "Error: Todos los campos son obligatorios", 400

        if estudiante:
            universidad.registrar_datos_examen("202", {"cHDL": cHDL, "CT": CT})
        else:
            return f"Error: No se encontró el estudiante con ID {id}", 404

        return redirect(url_for("index"))
    return render_template("registro_salud.html")

@app.route("/registro_medicion", methods=["GET", "POST"])
def registro_medicion():
    if request.method == "POST":
        # Obtener datos del formulario
        PA = request.form.get("PA")
        tabaquismo = request.form.get("tabaquismo")

        if not PA or not tabaquismo:
            return "Error: Todos los campos son obligatorios", 400


        print(f"Datos de medición registrados: PA={PA}, Tabaquismo={tabaquismo}")

        return redirect(url_for("index"))
    return render_template("registro_medicion.html")


@app.route("/estudiante/<id>")
def estudiante(id):
    try:
        datos = universidad.obtener_datos_estudiante(id)
        return render_template("estudiante.html", datos=datos)
    except ValueError as e:
        return str(e), 404

if __name__ == "__main__":
    app.run(debug=True)