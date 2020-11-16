from flask import Flask, render_template, request
from flask_mysql_connector import MySQL

app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DATABASE'] = 'testing'
mysql = MySQL(app)

'''
class Contact(mysql.Model):

    sno = mysql.Column(mysql.Integer, primary_key=True)
    name = mysql.Column(mysql.String(80), nullable=False)
    phone_num = mysql.Column(mysql.String(12), nullable=False)
    msg = mysql.Column(mysql.String(120), nullable=False)
    date = mysql.Column(mysql.String(12))
    email = mysql.Column(mysql.String(20), nullable=False)
'''
@app.route ("/home")
def home():
    return render_template('home.html')


@app.route ("/")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template ('about.html')

@app.route ("/post")
def post():
    return render_template ('post.html')



@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html')

    if request.method == 'POST':
        ''' sno name phone_num message date email
        '''
        name = request.form['name']
        phone_num = request.form['phone']
        message = request.form['message']
        #date = request.form['date']
        email = request.form['email']
        cursor = mysql.connection.cursor()

        cursor.execute(''' INSERT INTO contact VALUES(%s,'',%s,%s)''', (name, phone_num,message,email))
        for row in cursor:
            print(row)

        mysql.connection.commit()
        cursor.close()
    return render_template('contact.html')


app.run(debug=True)