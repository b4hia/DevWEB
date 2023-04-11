from flask import Flask, render_template
app = Flask("__name__")

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/contato")
def contact():
    return render_template('contato.html')

@app.route("/quemsomos")
def about():
    return render_template('quemsomos.html')
