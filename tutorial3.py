from flask import Flask , render_template , request
from flask_mysql_connector  import MySQL

app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DATABASE'] = 'testing'
mysql = MySQL(app)


@app.route ('/')
def index():
    return render_template ('welcome.html')


@app.route ('/form')
def form():
    return render_template ('form.html')

@app.route ('/login' , methods = ['POST' , 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form or "

    if request.method == 'POST':
        name=request.form['name']
        age=request.form['age']
        cursor=mysql.connection.cursor ()

        cursor.execute (''' INSERT INTO testflask VALUES(%s,%s)''' , (name , age))
        mysql.connection.commit ()
        cursor.close ()
        return f"Done!!"

app.run (host = 'localhost' , port = 5000)