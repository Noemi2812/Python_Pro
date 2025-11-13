from flask import Flask
import random

app = Flask(__name__)

lista_fatti = ["ciao a tutti","oggi ho creato la mia prima app con flask","mi piace questa lezione"] 

@app.route("/")
def home():
    return '<p>Benvenuti a <a href="moneta"> Tira la moneta </a> e <a href="fatto_casuale"> Scopri un fatto casuale </a></p>'

@app.route("/fatto_casuale")
def ciao_mondo():
    return f'<p>{random.choice(lista_fatti)}</p>'

@app.route("/moneta")
def lancio_moneta():
    risultato = random.choice(["Testa", "Croce"])
    return f'<p>Il risulatato del lancio della moneta è: {risultato}</p>'

app.run(debug=True)
