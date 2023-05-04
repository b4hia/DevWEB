from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_Host'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fatec'
app.config['MYSQL_DB'] = 'unes'

mysql = MySQL(app)

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/contato", methods=['POST', 'GET'])
def contato():
    if request.method == 'POST':
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['desc']

        cur = mysql.connection.cursor()
        cur.execute(f'INSERT INTO contatos(email, assunto, descricao) VALUES ("{email}", "{assunto}", "{descricao}")')

        mysql.connection.commit()

        cur.close()

        return 'Feito!'
    else:
        return render_template("contato.html")

@app.route("/quemsomos")
def about():
    return render_template('quemsomos.html')

@app.route("/users")
def users():
    cur = mysql.connection.cursor()
    users = cur.execute('SELECT * FROM contatos')
    if users > 0:
        usersInfo = cur.fetchall()
        return render_template("users.html", usersInfo=usersInfo)