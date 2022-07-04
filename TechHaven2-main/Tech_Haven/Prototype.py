import os
import random
import shelve
import stripe
from flask import Flask, render_template, request, redirect, url_for, session, g, flash, jsonify, send_from_directory
from flask_mail import Message, Mail
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import Product
import Review
import User
import Feedback
import AddProduct
from Forms import RegisterForm, ReviewForm, ForgetPasswordForm, ContactUsForm, CreateReplyForm, PasswordResetForm
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re



mail = Mail()

app = Flask(__name__)
app.secret_key = 'secret_key'
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'tech.haven.we.sell.you.buy@gmail.com'
app.config["MAIL_PASSWORD"] = 'Zgmf-X19A'
app.config['MAIL_DEFAULT_SENDER'] = 'tech.haven.we.sell.you.buy@gmail.com'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Yu87179821OO'
app.config['MYSQL_DB'] = 'techhavendatabase'

# Initialize MySQL
mysql = MySQL(app)

@app.route('/MyWebApp/', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'Email' in request.form and 'Password' in request.form:
    # Create variables for easy access
        Email = request.form['Email']
        Password = request.form['Password']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        cursor.execute('SELECT * FROM accounts WHERE Email = %s AND Password = %s', (Email,Password,))

        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['Id'] = account['Id']
            session['Email'] = account['Email']
            return 'Logged in successfully!'
            msg = "ur in"
        else:
            # Account doesn’t exist or username/password incorrect
            msg = 'Incorrect username/password!'
            # Show the login form with message (if any)

    return render_template('Prototype.html', msg=msg)



if __name__ == '__main__':

    app.run()
