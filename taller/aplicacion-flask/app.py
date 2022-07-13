from flask import Flask, render_template
import requests
import json
from config import user, password
app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return "<p>Hola mundo, si se pudo!</p>"


@app.route("/losedificios")
def los_edificios():
    r = requests.get("http://127.0.0.1:8000/api/edificios/",
            auth=(user, password))        
    edificios = json.loads(r.content)
    numero_edificios = len(edificios)
    return render_template("losedificios.html", edificios=edificios,
    numero_edificios=numero_edificios)


@app.route("/losdepartamentos")
def los_departamentos():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/departamentos/",
            auth=(user, password))
    datos = json.loads(r.content)
    numero = len(datos)
    return render_template("losdepartamentos.html", datos=datos,
    numero=numero)


@app.route("/losdepartamentosdos")
def los_departamentos_dos():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/departamentos/",
            auth=(user, password))
    datos = json.loads(r.content)
    numero = len(datos)
    datos2 = []
    for d in datos:
        datos2.append({'nombre_propietario':d['nombre_propietario'],
        'costo_departamento':d['costo_departamento'],
        'num_cuartos':d['num_cuartos'],
        'edificio': obtener_edificio(d['edificio'])})
    return render_template("losdepartamentosdos.html", datos=datos2,
    numero=numero)

# funciones ayuda

def obtener_edificio(url):
    """
    """
    r = requests.get(url, auth=(user, password))
    nombre_edificio = json.loads(r.content)['nombre']
    return nombre_edificio
