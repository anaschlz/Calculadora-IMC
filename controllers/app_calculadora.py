from flask import Flask, render_template, request
from models import CalculadoraIMC
import os

class AppCalculadoraIMC:
    def __init__(self):
        self.app = Flask(__name__, template_folder=os.path.abspath("templates"))
        print(self.app.jinja_loader.searchpath)
        self.calculadora = None

        @self.app.route('/', methods=['GET', 'POST'])
        def calcular():
            if request.method == 'POST':
                nome = request.form['nome']
                peso = float(request.form['peso'])
                altura = float(request.form['altura'])
                genero = request.form['genero']

                try:
                    self.calculadora = CalculadoraIMC(nome, peso, altura, genero)
                    imc = self.calculadora.calcular_imc()
                    classificacao = self.calculadora.classificar_imc()
                    peso_ideal = self.calculadora.calcular_peso_ideal()

                    return render_template('index.html', nome=nome, imc=imc, classificacao=classificacao, peso_ideal=peso_ideal)
                
                except ValueError as e:
                    return render_template('index.html', error_message=str(e))

            return render_template('index.html')

    def run(self):
        self.app.run(debug=True, host='127.0.0.1', port=8000)
