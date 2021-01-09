from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

salononclick2 = Flask(__name__)
salononclick2.config['MYSQL_HOST'] = '10.1.1.61'
salononclick2.config['MYSQL_PORT'] = 3308
salononclick2.config['MYSQL_USER'] = 'root'
salononclick2.config['MYSQL_PASSWORD'] = 'root'
salononclick2.config['MYSQL_DB'] = 'asma'

mysql = MySQL(salononclick2)


@salononclick2.route('/')
def home():
    return render_template('index.html')


@salononclick2.route('/contactus')
def contactus():
    return render_template('contact.html')


@salononclick2.route('/aboutus')
def aboutus():
    return render_template('about.html')


@salononclick2.route('/pricing')
def pricing():
    return render_template('pricing.html')


@salononclick2.route('/features')
def features():
    return render_template('features.html')


@salononclick2.route('/login', methods=["POST","GET"])
def login():
    mysql.connection.commit()
    cur = mysql.connection.cursor()
    if request.method == "POST":
        logine = request.form
        user = logine["user"]
        password = logine["password"]
        cur.execute("SELECT * FROM users")
        account = cur.fetchone()
        if account:
            session['login'] = True
            session['user'] = account['user']
            session['password'] = account['password']
            return redirect(url_for('admin.html'))
        else:
            return "Sorry Your password is incorrect"


@salononclick2.route('/admin')
def admin():
    return render_template('admin.html')


if '__main__' == __name__:
    salononclick2.run(debug=True)
