from flask import Flask, app, render_template, request, flash
import random

app = Flask(__name__)

app.secret_key = "manbearpig_MUDMAN888"


@app.route('/')
def index():
    flash('')
    return render_template('index.html')


@app.route('/greet', methods=['POST', 'GET'])
def greet():
    # Arreglos propuestos
    alpha_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha_lower = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    caracters = '!#$[%&/(<)=?¿¡*}+-{],._>'


    base = alpha_upper + alpha_lower + numbers + caracters
    longitud = 14

    muestra = random.sample(base, longitud)
    password = ''.join(muestra)

    flash(password)
    return render_template('index.html')
