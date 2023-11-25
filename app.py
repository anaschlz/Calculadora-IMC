from flask import Flask, render_template, request
from controllers import AppCalculadoraIMC

if __name__ == '__main__':
    app_calculadora = AppCalculadoraIMC()
    app_calculadora.run()
