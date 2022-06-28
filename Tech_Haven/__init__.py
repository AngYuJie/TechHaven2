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
from Forms import RegisterForm, ReviewForm, ForgetPasswordForm, ContactUsForm, CreateReplyForm, PasswordResetForm, LoginForm
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from flask_bcrypt import Bcrypt
from datetime import date, datetime, timedelta
import base64
bcrypt = Bcrypt()
from Tech_Haven.TempTest import *



mail = Mail()

app = Flask(__name__)

app.secret_key = 'secret_key'
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'tech.haven.we.sell.you.buy@gmail.com'
app.config["MAIL_PASSWORD"] = 'teisjyvrlvrpnhgk'
app.config['MAIL_DEFAULT_SENDER'] = 'tech.haven.we.sell.you.buy@gmail.com'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Yu87179821OO'
app.config['MYSQL_DB'] = 'TechHavenDataBase'

######################## CAPTCHA ############################################
app.config['RECAPTCHA_PUBLIC_KEY']="6LfwyoAgAAAAAAf538D06BxhxmTsVzWhsrC8qjqe"
app.config['RECAPTCHA_PRIVATE_KEY']='6LfwyoAgAAAAAPgU74ccglcygPwEUi8ph1GdJ4zi'
######################## CAPTCHA ############################################


# Initialize MySQL
mysql = MySQL(app)

#stripe Public key
app.config['STRIPE PUBLIC KEY'] = 'pk_test_51KDhRPJ2w3z9iOVI9rVg9fkcx0RqSZJ6H9j6SZbEmUue61eznf3aDc1TM4QXlQvRaJRQV6lmyGeKdEnhgaYsRp6R00qRhAiy9r'

#stripe Secret Key
app.config['STRIPE_SECRET_KEY'] = 'sk_test_51KDhRPJ2w3z9iOVISFf5UrgptxBPuCXmrlBa1xtore80TS185XfdaAavDDqNrtL1XEEOp4bM9KpwYgf7PnGzrS9g00jXPs5vzy'

#Stripe Secret Key
stripe.api_key = 'sk_test_51KDhRPJ2w3z9iOVISFf5UrgptxBPuCXmrlBa1xtore80TS185XfdaAavDDqNrtL1XEEOp4bM9KpwYgf7PnGzrS9g00jXPs5vzy'
UPLOAD_FOLDER = 'static/ProfilePhotos/'
UPLOAD_FOLDER_CPU = 'static/Images/Products/CPU/'
UPLOAD_FOLDER_RAM = 'static/Images/Products/RAM/'
UPLOAD_FOLDER_GPU = 'static/Images/Products/GPU/'
UPLOAD_FOLDER_MOBA = 'static/Images/Products/MOBA/'
UPLOAD_FOLDER_PSU = 'static/Images/Products/PSU/'
UPLOAD_FOLDER_Storage = 'static/Images/Products/Storage/'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_FOLDER_CPU'] = UPLOAD_FOLDER_CPU
app.config['UPLOAD_FOLDER_RAM'] = UPLOAD_FOLDER_RAM
app.config['UPLOAD_FOLDER_GPU'] = UPLOAD_FOLDER_GPU
app.config['UPLOAD_FOLDER_MOBA'] = UPLOAD_FOLDER_MOBA
app.config['UPLOAD_FOLDER_PSU'] = UPLOAD_FOLDER_PSU
app.config['UPLOAD_FOLDER_Storage'] = UPLOAD_FOLDER_Storage


mail.init_app(app)
from flask import send_from_directory



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.before_request
def before_request():
    g.account = None

    # Check if user is loggedin
    if 'user_id' in session:
        # We need all the account info for the user so we can display it on the profile page
        with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute('SELECT * FROM accounts WHERE Id = %s', (session['user_id'],))
            g.account = cursor.fetchone()
            test = [g.account['FirstName'],g.account['LastName']]
            g.account2 = decoding(test)




@app.route('/')
def home():
    return render_template('LandingSite.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    error = ''
    if request.method == 'POST' and form.validate():
        session.clear()
        list = []
        Email = form.email.data
        list.append(Email)
        encodedEmail = encoding(list)
        Password = form.password.data

        with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute('SELECT * FROM accounts WHERE Email = %s', (encodedEmail[0],))
            g.account = cursor.fetchone()

        if g.account:
            user_hashPassword = g.account['Password']
            NoOfFailedAttemps = g.account['NoOfFailedAttemps']
            firstName = g.account['FirstName']
            lastName = g.account['LastName']
            mobileNumber = g.account['MobileNumber']
            AccountStatus = g.account['AccountStatus']
            AccountType = g.account['AccountType']



            if int(NoOfFailedAttemps) > 10 or AccountStatus=='Suspended':
                with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                    sql = 'UPDATE accounts SET NoOfFailedAttemps = %s, AccountStatus =%s  WHERE Email = %s'
                    val = (NoOfFailedAttemps,'Suspended',encodedEmail[0])
                    cursor.execute(sql,val)
                    mysql.connection.commit()
                    error = 'Your Account Has been temporarly suspended.'

            elif int(NoOfFailedAttemps) > 3 and AccountStatus!="Suspended":
                message1 = "Dear {} {} you have failed to login to your account {} times.\nIf you have forgotten your password please proceed via the forget password url on our login page.\n\n Best regards,\n Tech Haven Team.".format(firstName,lastName,NoOfFailedAttemps)
                error = 'Please check email and follow the instruction.'
                mail.send_message(
                        sender='tech.haven.we.sell.you.buy@gmail.com',
                        recipients=[Email],
                        subject="password",
                        body=message1
                    )



            if g.account and bcrypt.check_password_hash(user_hashPassword,Password) and AccountStatus!='Suspended':
                session['user_id'] = g.account['Id']
                with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                    sql = 'UPDATE accounts SET NoOfFailedAttemps = %s, FailedLoginDate= %s, FailedLoginTime = %s  WHERE Email = %s'
                    val = ("0",None,None,encodedEmail[0])
                    cursor.execute(sql,val)
                    mysql.connection.commit()

                with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                    cursor.execute('SELECT * FROM accounts WHERE Email = %s', (encodedEmail[0],))
                    account = cursor.fetchone()
                    CurrentPasswordAge = account['PasswordAge']
                    todaydate = date.today()
                    delta = todaydate - CurrentPasswordAge
                    print(delta.days)
                    if int(delta.days) > 30:
                        message = "password age is more than 30 days!"
                    else:
                        message = 'test'
                flash(message)
                return redirect(url_for('home',message=message))


            else:
                todaydate = date.today()
                failedDate = todaydate.strftime("%Y-%D-%M")
                todayTime = datetime.today()
                failedTime = todayTime.strftime("%H:%M:%S")
                test = int(NoOfFailedAttemps)+1

                with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                    sql = 'UPDATE accounts SET NoOfFailedAttemps = %s, FailedLoginDate= %s, FailedLoginTime = %s  WHERE Email = %s'
                    val = (test,failedDate,failedTime,encodedEmail[0])
                    cursor.execute(sql,val)
                    mysql.connection.commit()

                EncodedItems = [firstName,lastName,mobileNumber]
                decodeditems = decoding(EncodedItems)
                with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                    cursor.execute('INSERT INTO Logs VALUES (NULL, %s, %s, %s, %s, %s,%s,%s,%s,%s)',(decodeditems[0], decodeditems[1], Email, decodeditems[2],failedDate,failedTime,AccountType,test,AccountStatus))
                    mysql.connection.commit()
                    error = 'Invalid Credentials. Please try again.'

        else:
            message1 = "Hi you have not made an account with us yet.\n\n Best regards,\n Tech Haven Team."
            error = 'Please check email and follow the instruction.'
            mail.send_message(
                        sender='tech.haven.we.sell.you.buy@gmail.com',
                        recipients=[Email],
                        subject="password",
                        body=message1
                    )

    return render_template('login.html',form=form, error=error)



@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm(request.form)
    todaydate = date.today()
    current_date = todaydate.strftime("%Y-%D-%M")
    if request.method == 'POST' and form.validate():
            FirstName = form.first_name.data
            LastName = form.last_name.data
            Password = form.password.data
            Email = form.email.data
            Street = form.street.data
            PostalCode = form.postal_code.data
            UnitNumber = form.unit_number.data
            MobileNumber = form.mobile_number.data
            hashpassword = bcrypt.generate_password_hash(Password)
            list = [FirstName,LastName,Email,Street,PostalCode,UnitNumber,MobileNumber]
            encoder = encoding(list)
            with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                cursor.execute('SELECT * FROM accounts where Email = %s', (encoder[2],))
                account = cursor.fetchone()

                if account:
                    email_error = 'Email Has been Registered'
                    return render_template('register.html', form=form, email_error=email_error)

                else:
                    with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                        cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s, %s, %s,%s,%s,%s,NULL,NULL,%s,%s,%s,%s,%s)',
                                       (encoder[0], encoder[1], hashpassword, encoder[2], encoder[3],encoder[4],encoder[5],encoder[6],current_date,"Customer",0,'Active','default.jpg'))
                        mysql.connection.commit()
                        session['user_created'] = "You"

                    return redirect(url_for('login'))


    else:
        return render_template('register.html', form=form)


#Update User.Yu Jie
@app.route('/updateProfile/<int:id>/', methods=['GET', 'POST'])
def update_profile(id):
    #Set Update_user_form to inheriet RegistrationForm(Form) Class
    update_user_form = RegisterForm(request.form)
    #Validation if request method is post and
    if request.method == 'POST' and update_user_form.validate():
       if "avatar" in request.files:
            avatar = request.files['avatar']
            if avatar.filename == '':
                with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                    cursor.execute("select ProfilePhoto from accounts where Id = %s" % id)
                    filename = cursor.fetchone()["ProfilePhoto"]
                    #print(filename)

            elif avatar and allowed_file(avatar.filename):
                filename = secure_filename(avatar.filename)

                ver = 0
                while os.path.isfile('/static/ProfilePhotos/' + filename):  # if theres existing file
                    ver += 1
                    for filetype in ALLOWED_EXTENSIONS:
                        if filetype in filename.split('.'):
                            filename = avatar.filename.split('.')[0] + str(ver) + '.' + avatar.filename.split('.')[-1]

                filepath = '/static/ProfilePhotos/' + filename

                avatar.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            elif not allowed_file(avatar.filename):
                fileTypeError = 'Invalid file type. (Only accepts .png, .jpg, .jpeg, and .gif files)'
                return render_template('updateProfile.html', id=id, form=update_user_form, fileTypeError=fileTypeError)

            # update user information
            with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                cursor.execute("SELECT Email FROM accounts")
                userdata = cursor.fetchall()
                decodedList= [userdata]
                # Fetch one record and return result
                # userdata = cursor.fetchone()
                # list = [userdata['FirstName'],
                # userdata['LastName'],
                # userdata['Street'],
                # userdata['PostalCode'],
                # userdata['UnitNumber'],
                # userdata['MobileNumber'],
                # userdata['Email']]
                # decodedList = decoding(list)
                # print(decodedList)
                # list2 = [update_user_form.first_name.data,
                #          update_user_form.last_name.data,
                #          update_user_form.street.data,
                #          update_user_form.postal_code.data,
                #          update_user_form.unit_number.data,
                #          update_user_form.mobile_number.data,
                #          update_user_form.email.data]
                # encodedlist = encoding(list2)


            for key in decodedList:
                if update_user_form.email.data == key:
                    emailError = "Email has already been registered!"
                    return render_template('updateProfile.html', id=id, form=update_user_form, emailError=emailError)

            hashpassword = bcrypt.generate_password_hash(update_user_form.password)
            with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                cursor.execute('SELECT * FROM accounts WHERE Id = %s', (id,))
                userdata = cursor.fetchone()
                list2 = [update_user_form.first_name.data,
                         update_user_form.last_name.data,
                         update_user_form.street.data,
                         update_user_form.postal_code.data,
                         update_user_form.unit_number.data,
                         update_user_form.mobile_number.data,
                         update_user_form.email.data]
                print(list2)
                encodedlist = encoding(list2)


            if hashpassword != userdata['Password']:
                PasswordAge = date.today()
            else:
                PasswordAge = userdata["PasswordAge"]


            with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                cursor.execute('UPDATE accounts set Email = "%s", Password = "%s", FirstName = "%s", LastName = "%s", Street = "%s", PostalCode = "%s", UnitNumber = "%s", MobileNumber = "%s", PasswordAge = "%s", ProfilePhoto = "%s" WHERE Id ="%s"' %
                               (encodedlist[6],
                                hashpassword,
                                encodedlist[0],
                                encodedlist[1],
                                encodedlist[2],
                                encodedlist[3],
                                encodedlist[4],
                                encodedlist[5],
                                PasswordAge,
                                filename,
                                id))
                mysql.connection.commit()
                cursor.execute("SELECT FirstName,LastName from accounts where Id = %s" % id)
                data = cursor.fetchone()
                session['user_updated'] = data["FirstName"] + ' ' + data["LastName"]
            session['profile_updated'] = 'Profile successfully updated!'
            return redirect(url_for('profile'))
    else:

        with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT * FROM accounts where Id = %s" % (id,))
            # Fetch one record and return result
            userdata = cursor.fetchone()
            list = [userdata['FirstName'],
                userdata['LastName'],
                userdata['Street'],
                userdata['PostalCode'],
                userdata['UnitNumber'],
                userdata['MobileNumber'],
                userdata['Email']]
            decodedList = decoding(list)
        #print(userdata)

        update_user_form.first_name.data =decodedList[0]
        update_user_form.last_name.data = decodedList[1]
        update_user_form.street.data = decodedList[2]
        update_user_form.postal_code.data = decodedList[3]
        update_user_form.unit_number.data = decodedList[4]
        update_user_form.mobile_number.data = decodedList[5]
        update_user_form.email.data = decodedList[6]

        if 'user_id' in session and session['user_id'] in [userdata['Id'], 1]:
            return render_template('updateProfile.html', form=update_user_form, profile_pic=userdata['ProfilePhoto'],
                                   user_id=id)
        else:
            return 'You do not have authorized access to this webpage.'






@app.route('/profile')
def profile():
    user_id = session['user_id']
    #print(user_id)
    with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("select * from accounts where Id = %s" % user_id)
        userdata = cursor.fetchone()
        list = [userdata['FirstName'],
                userdata['LastName'],
                userdata['Street'],
                userdata['PostalCode'],
                userdata['UnitNumber'],
                userdata['MobileNumber'],
                userdata['Email']]
        decodedList = decoding(list)
        id = userdata['Id']
        CurrentPasswordAge = userdata['PasswordAge']
        todaydate = date.today()
        delta = todaydate - CurrentPasswordAge
        print(delta.days)
        if int(delta.days) > 30:
            message = "Your password age is more than 30 days!"
        else:
            message = ''



    #print(userdata)
    return render_template('profile.html', data=decodedList, data2=userdata,message=message)

@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.pop('user_id', None)

    return redirect(url_for('home'))


@app.route('/<product_id>/review', methods=['GET', 'POST'])
def review(product_id):
    users_dict = {}
    products = []
    db = shelve.open('products.db', 'c')
    CPU_list = db['CPU']
    RAM_list = db['RAM']
    GPU_list = db['GPU']
    MOBA_list = db['MOBA']
    PSU_list = db['PSU']
    Storage_list = db['Storage']
    db.close()

    #For loop to loop through the products.db database
    for eachitem in CPU_list:
        products.append(CPU_list[eachitem].get_product_id())
    for eachitem2 in RAM_list:
        products.append(RAM_list[eachitem2].get_product_id())
    for eachitem3 in GPU_list:
        products.append(GPU_list[eachitem3].get_product_id())
    for eachitem4 in MOBA_list:
        products.append(MOBA_list[eachitem4].get_product_id())
    for eachitem5 in PSU_list:
        products.append(PSU_list[eachitem5].get_product_id())
    for eachitem6 in Storage_list:
        products.append(Storage_list[eachitem6].get_product_id())


    if product_id in products:
        form = ReviewForm(request.form)
        already_submitted = False
        db_name = 'Review-' + product_id
        db_count = db_name + '-Count'
        if request.method == 'POST' and form.validate():
            reviews_dict = {}
            db = shelve.open('reviews.db', 'c')

            # get review information based on product_id of product
            try:

                reviews_dict = db[db_name]
            except:
                print("Error in retrieving Reviews from reviews.db.")

            Review.Review.count_id = db[db_count]+1

            review = Review.Review(form.rating.data, form.title.data, form.review.data, g.user)
            # set default attribute of avatar, votes, upvotes and downvotes
            setattr(review, 'avatar', g.user.avatar)
            setattr(review, 'votes', 0)
            setattr(review, 'upvoters', [])
            setattr(review, 'downvoters', [])

            # save information into db using id of review
            reviews_dict[review.get_review_id()] = review
            db[db_name] = reviews_dict
            db.close()
            return redirect(url_for('review_submitted'))

        elif request.method == 'GET':
            reviews_dict = {}
            db = shelve.open('reviews.db', 'c')
            userdb = shelve.open('register.db', 'w')
            try:
                reviews_dict = db[db_name]
            except:
                print("Error in retrieving Reviews from reviews.db")

            try:
                users_dict = userdb['Users']
            except:
                print("Error in retrieving Reviews from reviews.db")

            reviews_list = []
            for key in reviews_dict:
                rev = reviews_dict.get(key)
                reviews_list.append(rev)



            users_email_list = []
            for i in range(len(reviews_list)):
                review = reviews_list[i]
                for key in users_dict:
                    user = users_dict.get(key)
                    users_email_list.append(user.get_email())
                    if review.get_user_object().get_email() == user.get_email():
                        setattr(review.get_user_object(), 'avatar', user.avatar)
                        review.get_user_object().set_first_name(user.get_first_name())
                        review.get_user_object().set_last_name(user.get_last_name())
                if review.get_user_object().get_email() not in users_email_list:
                    review.get_user_object().set_first_name('[deleted]')
                    review.get_user_object().set_last_name('')
            if 'user_id' in session:

                for i in range(len(reviews_list)):
                    review = reviews_list[i]
                    if g.user.get_email() == review.get_user_object().get_email():
                        already_submitted = True
            reviews_list = sorted(reviews_list, key=lambda review: review.votes, reverse=True)

            db[db_count] = len(reviews_list)
            new_review_dict = {}

            for index, review in enumerate(reviews_list):
                review.set_review_id(index+1)
                new_review_dict[index+1] = review

            db[db_name] = new_review_dict
            db.close()

            template = 'products/' + product_id + '.html'
            return render_template(template, form=form, count=len(reviews_list), reviews_list=reviews_list, already_submitted=already_submitted)

@app.route('/review_submitted')
def review_submitted():
    return render_template('reviewSubmitted.html')

@app.route('/<product_id>/review/upvote/<int:review_id>/')
def upvote(product_id, review_id):
    if 'user_id' in session:
        reviews_dict = {}
        db_name = 'Review-' + product_id
        db = shelve.open('reviews.db', 'w')
        reviews_dict = db[db_name]

        review = reviews_dict.get(review_id)

        downvoters = review.downvoters
        upvoters = review.upvoters
        if g.user.get_email() in upvoters:
            votes = review.votes - 1
            setattr(review, 'votes', votes)
            upvoters.remove(g.user.get_email())
        else:
            votes = review.votes
            if g.user.get_email() in downvoters:
                votes = review.votes + 1
                downvoters.remove(g.user.get_email())
            votes = votes + 1
            setattr(review, 'votes', votes)
            upvoters.append(g.user.get_email())
            setattr(review, 'upvoters', upvoters)
        print(review.upvoters)
        db[db_name] = reviews_dict
        db.close()
        return redirect(url_for('review', product_id=product_id))
    else:
        return redirect(url_for('login'))

@app.route('/<product_id>/review/downvote/<int:review_id>/')
def downvote(product_id, review_id):
    if 'user_id' in session:
        reviews_dict = {}
        db_name = 'Review-' + product_id
        db = shelve.open('reviews.db', 'w')
        reviews_dict = db[db_name]

        review = reviews_dict.get(review_id)

        upvoters = review.upvoters
        downvoters = review.downvoters
        if g.user.get_email() in downvoters:
            votes = review.votes + 1
            setattr(review, 'votes', votes)
            downvoters.remove(g.user.get_email())
        else:
            votes = review.votes
            if g.user.get_email() in upvoters:
                votes = review.votes - 1
                upvoters.remove(g.user.get_email())
            votes = votes - 1
            setattr(review, 'votes', votes)
            downvoters.append(g.user.get_email())
            setattr(review, 'downvoters', downvoters)
        print(review.downvoters)
        db[db_name] = reviews_dict
        db.close()
        return redirect(url_for('review', product_id=product_id))
    else:
        return redirect(url_for('login'))

@app.route('/<product_id>/deleteReview/<int:id>', methods=["POST"])
def delete_review(product_id, id):
    reviews_dict = {}
    db_name = 'Review-' + product_id
    db = shelve.open('reviews.db', 'w')
    reviews_dict = db[db_name]
    print(db_name)
    print(reviews_dict[id].get_title())
    review = reviews_dict.pop(id)

    db[db_name] = reviews_dict
    db.close()

    return redirect(url_for('review', product_id=product_id))


@app.route('/<product_id>/updateReview/<int:id>/', methods=['GET', 'POST'])
def update_review(product_id, id):
    reviews_dict = {}
    db_name = 'Review-' + product_id
    db = shelve.open('reviews.db', 'w')
    reviews_dict = db[db_name]

    review = reviews_dict.get(id)

    review.set_rating(request.form['rating'])
    review.set_title(request.form['title'])
    review.set_review(request.form['review'])

    db[db_name] = reviews_dict
    db.close()

    return redirect(url_for('review', product_id=product_id))



@app.route('/Products', methods=["GET", "POST"])
def add_to_cart():
    db = shelve.open('products.db', 'c')
    CPU_list = db['CPU']
    RAM_list = db['RAM']
    GPU_list = db['GPU']
    MOBA_list = db['MOBA']
    PSU_list = db['PSU']
    Storage_list = db['Storage']
    db.close()

    already_in_cart = False
    cart_dict = {}
    cart_list = []
    subtotal = 0

    if 'user_id' in session:
        user_id = session['user_id']
        # after submit the form, receive product_id,and quantity
        if request.method == "POST":
            product_id = request.form.get('product_id')
            quantity = int(request.form.get('quantity'))

            db = shelve.open('cart.db', 'c')
            try:
                cart_dict = db['Cart']
            except:
                print('error')

            try:
                cart_list = cart_dict[user_id]
            except:
                pass

            for i in range(len(cart_list)):
                if product_id == cart_list[i].get_product_id():  # if cart already has the same product id
                    already_in_cart = True
                    current_quantity = cart_list[i].get_quantity()
                    new_quantity = int(current_quantity) + quantity
                    cart_list[i].set_quantity(new_quantity)
                    break

            if not already_in_cart:
                product_obj = Product.Product(product_id, quantity)
                cart_list.append(product_obj)
                cart_dict[user_id] = cart_list

            db['Cart'] = cart_dict
            db.close()

        elif request.method == "GET":  # Counts how many things u have in cart upon loading page, displays it as Your Cart(1)
            db = shelve.open('cart.db', 'c')
            try:
                cart_dict = db['Cart']
            except:
                print('error')

            try:
                cart_list = cart_dict[user_id]
            except:
                pass

        # for i in range(len(cart_list)):
        #     product_price = cart_list[i].get_price()
        #     subtotal += product_price


        return render_template('trialproductpage.html', cart_dict=cart_dict,
                               cart_list=cart_list, subtotal=round(subtotal, 2),
                               CPU_list=CPU_list, RAM_list=RAM_list,
                               GPU_list=GPU_list, MOBA_list=MOBA_list,
                               PSU_list=PSU_list, Storage_list=Storage_list)
    else:
        return render_template('trialproductpage.html', CPU_list=CPU_list,
                               RAM_list=RAM_list, GPU_list=GPU_list,
                               MOBA_list=MOBA_list, PSU_list=PSU_list, Storage_list=Storage_list,)


@app.route('/ShoppingCart', methods=["GET", "POST"])
def cart():
    db = shelve.open('products.db', 'c')
    CPU_list = db['CPU']
    RAM_list = db['RAM']
    GPU_list = db['GPU']
    MOBA_list = db['MOBA']
    PSU_list = db['PSU']
    Storage_list = db['Storage']
    db.close()

    subtotal = 0
    if 'user_id' in session:
        user_id = session['user_id']
        db = shelve.open('cart.db', 'c')
        try:
            cart_dict = db['Cart']
        except:
            cart_dict = []

        try:
            cart_list = cart_dict[user_id]
        except:
            cart_list = []


        # if product_id in cart_list does not exist, remove it from cart
        i = 0
        while i < len(cart_list):
           product_id = cart_list[i].get_product_id()
           if product_id not in CPU_list and product_id not in RAM_list and product_id not in GPU_list and product_id not in MOBA_list and product_id not in PSU_list and product_id not in Storage_list:
               cart_list.pop(i)
           else:
               i += 1
        cart_list.pop(product_id)
        cart_dict[user_id] = cart_list
        db['Cart'] = cart_dict

            # product_price = cart_list[i].get_price() * int(cart_list[i].get_quantity())
            # subtotal += product_price
        # cart_dict = {user_id: cart_list}
        # cart_list = [<obj>, <obj>, <obj>]

        for i in range(len(cart_list)):
            product_id = cart_list[i].get_product_id()
            quantity = int(cart_list[i].get_quantity())
            if product_id in CPU_list:
                price = quantity*int(CPU_list[product_id].get_price())
            elif product_id in RAM_list:
                price = quantity*int(RAM_list[product_id].get_price())
            elif product_id in GPU_list:
                price = quantity*int(GPU_list[product_id].get_price())
            elif product_id in MOBA_list:
                price = quantity*int(MOBA_list[product_id].get_price())
            elif product_id in PSU_list:
                price = quantity*int(PSU_list[product_id].get_price())
            elif product_id in Storage_list:
                price = quantity*int(Storage_list[product_id].get_price())
            subtotal += price

        return render_template('ShoppingCart.html', cart_dict=cart_dict,
                               cart_list=cart_list, subtotal=round(subtotal, 2),
                               CPU_list=CPU_list, RAM_list=RAM_list,
                               GPU_list=GPU_list, MOBA_list=MOBA_list,
                               PSU_list=PSU_list, Storage_list=Storage_list)
    else:
        return render_template('ShoppingCart.html')


@app.route('/deleteProduct/<int:product_id>', methods=["POST"])
def delete_product(product_id):
    cart_list = []
    cart_dict = {}
    user_id = session['user_id']
    db = shelve.open('cart.db', 'w')
    try:
        cart_dict = db['Cart']
    except:
        print('Error in retrieving cart_dict from cart.db')

    try:
        cart_list = cart_dict[user_id]
    except:
        pass
    # cart_list = [<product object>, <product object>]
    # cart_dict = { 1: [<product object>, <product object>], 2: [<product object>, <product object]}
    cart_list.pop(product_id)
    cart_dict[user_id] = cart_list
    db['Cart'] = cart_dict

    db.close()

    return redirect(url_for('cart'))

@app.route('/updateProduct/<int:product_id>', methods=["POST", "GET"])
def update_product(product_id):
    db = shelve.open('products.db', 'c')
    CPU_list = db['CPU']
    RAM_list = db['RAM']
    GPU_list = db['GPU']
    MOBA_list = db['MOBA']
    PSU_list = db['PSU']
    Storage_list = db['Storage']
    db.close()

    cart_dict = {}
    cart_list = []
    user_id = session['user_id']
    db = shelve.open('cart.db', 'c')
    try:
        cart_dict = db['Cart']
    except:
        print('Error in retrieving cart_dict from cart.db')

    try:
        cart_list = cart_dict[user_id]
    except:
        pass


        # item_information - used to get all information of the item
    if cart_list[product_id].get_product_id() in CPU_list:
        item_information = CPU_list[cart_list[product_id].get_product_id()]
    elif cart_list[product_id].get_product_id() in RAM_list:
        item_information = RAM_list[cart_list[product_id].get_product_id()]
    elif cart_list[product_id].get_product_id() in GPU_list:
        item_information = GPU_list[cart_list[product_id].get_product_id()]
    elif cart_list[product_id].get_product_id() in MOBA_list:
        item_information = MOBA_list[cart_list[product_id].get_product_id()]
    elif cart_list[product_id].get_product_id() in PSU_list:
        item_information = PSU_list[cart_list[product_id].get_product_id()]
    elif cart_list[product_id].get_product_id() in Storage_list:
        item_information = Storage_list[cart_list[product_id].get_product_id()]

    # selected item - used to get the quantity for item selected
    selected_item = cart_list[product_id]

    if request.method == 'POST':
        quantity = request.form.get('quantity')
        id_product = request.form.get('product_id')
        for id in range(len(cart_list)):
            # check if product id is in cart
            if cart_list[id].get_product_id() == id_product:
                cart_list[id].set_quantity(quantity)
                cart_dict[user_id] = cart_list
        db['Cart'] = cart_dict
        db.close()
        return redirect(url_for('cart'))
    else:
        return render_template('UpdateProduct.html', selected_item=selected_item, product_id=product_id, item_information=item_information)


@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    db = shelve.open('products.db', 'c')
    CPU_list = db['CPU']
    RAM_list = db['RAM']
    GPU_list = db['GPU']
    MOBA_list = db['MOBA']
    PSU_list = db['PSU']
    Storage_list = db['Storage']
    db.close()

    cart_dict = {}
    cart_list = []
    user_id = g.user.get_user_id()
    db = shelve.open('cart.db', 'c')
    try:
        cart_dict = db['Cart']
    except:
        print('error')


    try:
        cart_list = cart_dict[user_id]
    except:
        pass

    subtotal = 0
    for i in range(len(cart_list)):
        product_id = cart_list[i].get_product_id()
        quantity = int(cart_list[i].get_quantity())
        if product_id in CPU_list:
            price = int(CPU_list[product_id].get_price())
        elif product_id in RAM_list:
            price = int(RAM_list[product_id].get_price())
        elif product_id in GPU_list:
            price = int(GPU_list[product_id].get_price())
        elif product_id in MOBA_list:
            price = int(MOBA_list[product_id].get_price())
        elif product_id in PSU_list:
            price = int(PSU_list[product_id].get_price())
        elif product_id in Storage_list:
            price = int(Storage_list[product_id].get_price())
        subtotal += price*quantity
    subtotal = subtotal * 100


    session = stripe.checkout.Session.create(
        billing_address_collection='required',
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'sgd',
                'product_data': {
                    'name': 'Subtotal',
                },
                'unit_amount': int(subtotal),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=url_for("success", _external=True),
        cancel_url=url_for("cart", _external=True),
    )



    db.close()

    return jsonify(id=session.id)


@app.route("/success")
def success():
    cart_dict = {}
    cart_list = []
    analysis_quantity_dict = {}
    analysis_revenue_dict = {}
    user_id = g.user.get_user_id()

    db = shelve.open('products.db', 'c')
    CPU_list = db['CPU']
    RAM_list = db['RAM']
    GPU_list = db['GPU']
    MOBA_list = db['MOBA']
    PSU_list = db['PSU']
    Storage_list = db['Storage']
    db.close()

    db = shelve.open('cart.db', 'c')
    try:
        cart_dict = db['Cart']
    except:
        print('error')

    try:
        cart_list = cart_dict[user_id]
    except:
        pass


    analysis_db = shelve.open('analysis.db', 'c')
    try:
        analysis_quantity_dict = analysis_db['Analysis_quantity']
        analysis_revenue_dict = analysis_db['Analysis_revenue']
    except:
        print('error')



    for i in range(len(cart_list)):
        product_id = cart_list[i].get_product_id()
        if product_id in analysis_quantity_dict:
            analysis_quantity_dict[product_id] = (int(analysis_quantity_dict[product_id]) + int(cart_list[i].get_quantity()))
        if product_id not in analysis_quantity_dict:
            analysis_quantity_dict[product_id] = int(cart_list[i].get_quantity())


        quantity = int(cart_list[i].get_quantity())
        if product_id in CPU_list:
            price = int(CPU_list[product_id].get_price())
        elif product_id in RAM_list:
            price = int(RAM_list[product_id].get_price())
        elif product_id in GPU_list:
            price = int(GPU_list[product_id].get_price())
        elif product_id in MOBA_list:
            price = int(MOBA_list[product_id].get_price())
        elif product_id in PSU_list:
            price = int(PSU_list[product_id].get_price())
        elif product_id in Storage_list:
            price = int(Storage_list[product_id].get_price())
        total = quantity*price

        if product_id not in analysis_revenue_dict:
            analysis_revenue_dict[product_id] = int(total)
        elif product_id in analysis_revenue_dict:
            analysis_revenue_dict[product_id] += int(total)


    analysis_db['Analysis_quantity'] = analysis_quantity_dict
    analysis_db['Analysis_revenue'] = analysis_revenue_dict


    # remove all items from the current cart of the user
    cart_list.clear()
    cart_dict[user_id] = cart_list
    db['Cart'] = cart_dict
    db.close()

    return render_template("Thanks.html")

@app.route('/ContactUs', methods=['GET', 'POST'])
def create_feedback():
    create_feedback_form = ContactUsForm(request.form)
    if request.method == 'POST' and create_feedback_form.validate():
        feedbacks_dict = {}
        db = shelve.open('feedback.db', 'c')
        i = 0

        feedback_count_id = 0
        for key in db:
            i = 0
            while True:
                if i not in db[key]:
                    print('g')
                    feedback_count_id = i
                    print(feedback_count_id)
                    break
                else:
                    i += 1

        try:
            feedbacks_dict = db['Feedbacks']
        except:
            print("Error in retrieving Customers from customer.db")

        feedback = Feedback.Feedback(create_feedback_form.first_name.data, create_feedback_form.last_name.data,
                                     create_feedback_form.email.data,
                                     create_feedback_form.subject.data, create_feedback_form.inquiry.data, feedback_count_id)
        feedbacks_dict[feedback.get_feedback_id()] = feedback
        db['Feedbacks'] = feedbacks_dict
        db.close()
        return redirect(url_for('home'))
    return render_template('ContactUs.html', form=create_feedback_form)

@app.route('/retrieveFeedback')
def retrieve_feedbacks():
    feedbacks_dict = {}
    db = shelve.open('feedback.db')
    feedbacks_dict = db['Feedbacks']
    db.close()

    feedbacks_list = []
    for key in feedbacks_dict:
        feedback = feedbacks_dict.get(key)
        feedbacks_list.append(feedback)

    return render_template('retrieveFeedbacks.html', feedbacks_list=feedbacks_list)

@app.route('/deleteFeedback/<int:feedback_id>', methods=['POST'])
def delete_feedback(feedback_id):
    feedbacks_dict = {}
    db = shelve.open('feedback.db')
    feedbacks_dict = db['Feedbacks']

    feedbacks_dict.pop(feedback_id)

    db['Feedbacks'] = feedbacks_dict
    db.close()

    return redirect(url_for('retrieve_feedbacks'))

@app.route('/createReply/<int:id>', methods=['GET', 'POST'])
def create_reply(id):
    create_reply_form = CreateReplyForm(request.form)

    db = shelve.open('feedback.db')
    feedbacks_dict = db['Feedbacks']
    db.close()
    user_info = feedbacks_dict[id]

    if request.method == 'POST' and create_reply_form.validate():
        msg = Message(user_info.get_subject(), recipients=[user_info.get_email()])
        msg.html = 'Dear ' + user_info.get_first_name() + ' ' + user_info.get_last_name() + ',<br><br> Regarding your inquiry, "' + user_info.get_inquiry() + '",<br><br>Our suggestion is to ' + create_reply_form.reply.data + '<br><br>Your Sincerely,<br> Tech Haven Support Team'
        mail.send(msg)

        db = shelve.open('feedback.db')
        feedbacks_dict = db['Feedbacks']

        feedbacks_dict.pop(id)

        db['Feedbacks'] = feedbacks_dict
        db.close()

        return redirect(url_for('retrieve_feedbacks'))
    return render_template('CreateReply.html', form=create_reply_form, user_info=user_info)

@app.route('/analysis')
def create_analysis():
    analysis_dict = {}
    analysis_list = {}

    analysis_db = shelve.open('analysis.db', 'c')
    try:
        analysis_quantity_dict = analysis_db['Analysis_quantity']
    except:
        print('error')

    try:
        analysis_revenue_dict = analysis_db['Analysis_revenue']
    except:
        print('error')


    analysis_quantity_dict_x = []
    analysis_quantity_dict_y = []
    for i in analysis_quantity_dict:
        analysis_quantity_dict_x.append(i)
        analysis_quantity_dict_y.append(analysis_quantity_dict[i])

    analysis_revenue_dict_x = []
    analysis_revenue_dict_y = []
    for i in analysis_revenue_dict:
        analysis_revenue_dict_x.append(i)
        analysis_revenue_dict_y.append(analysis_revenue_dict[i])


    return render_template('Chart.html',
                           analysis_quantity_dict_x=analysis_quantity_dict_x,analysis_quantity_dict_y=analysis_quantity_dict_y,
                           analysis_revenue_dict_x=analysis_revenue_dict_x, analysis_revenue_dict_y=analysis_revenue_dict_y)


@app.route('/Report')
def create_analysis2():
    with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute('SELECT * FROM logs')
        records = cursor.fetchall()


    return render_template('ReportGeneration.html',logs=records)

# @app.route('/Report')
# def create_analysis():
#     analysis_dict = {}
#     analysis_list = {}
#
#
#     analysis_db = shelve.open('analysis.db', 'c')
#     try:
#         analysis_quantity_dict = analysis_db['Analysis_quantity']
#     except:
#         print('error')
#
#     try:
#         analysis_revenue_dict = analysis_db['Analysis_revenue']
#     except:
#         print('error')
#
#
#     analysis_quantity_dict_x = []
#     analysis_quantity_dict_y = []
#     for i in analysis_quantity_dict:
#         analysis_quantity_dict_x.append(i)
#         analysis_quantity_dict_y.append(analysis_quantity_dict[i])
#
#     analysis_revenue_dict_x = []
#     analysis_revenue_dict_y = []
#     for i in analysis_revenue_dict:
#         analysis_revenue_dict_x.append(i)
#         analysis_revenue_dict_y.append(analysis_revenue_dict[i])
#
#
#     return render_template('Report.html',
#                            analysis_quantity_dict_x=analysis_quantity_dict_x,analysis_quantity_dict_y=analysis_quantity_dict_y,
#                            analysis_revenue_dict_x=analysis_revenue_dict_x, analysis_revenue_dict_y=analysis_revenue_dict_y)
@app.route('/viewProducts')
def view_products_admin():
    db = shelve.open('products.db', 'c')
    CPU_list = db['CPU']
    RAM_list = db['RAM']
    GPU_list = db['GPU']
    MOBA_list = db['MOBA']
    PSU_list = db['PSU']
    Storage_list = db['Storage']
    db.close()


    return render_template('viewProductsAdmin.html',
                           CPU_list=CPU_list, RAM_list=RAM_list,
                           GPU_list=GPU_list, MOBA_list=MOBA_list,
                           PSU_list=PSU_list, Storage_list=Storage_list)

@app.route('/updateProductsAdmin/<product_id>', methods=['POST', 'GET'])
def update_products_admin(product_id):
    db = shelve.open('products.db', 'c')
    CPU_list = db['CPU']
    RAM_list = db['RAM']
    GPU_list = db['GPU']
    MOBA_list = db['MOBA']
    PSU_list = db['PSU']
    Storage_list = db['Storage']


    if product_id in CPU_list:
        item_information = CPU_list[product_id]
    elif product_id in RAM_list:
        item_information = RAM_list[product_id]
    elif product_id in GPU_list:
        item_information = GPU_list[product_id]
    elif product_id in MOBA_list:
        item_information = MOBA_list[product_id]
    elif product_id in PSU_list:
        item_information = PSU_list[product_id]
    elif product_id in Storage_list:
        item_information = Storage_list[product_id]

    if request.method == 'POST':
        product_id = request.form.get('product_id')
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        if product_id in CPU_list:
            if price != '':
                CPU_list[product_id].set_price(int(price))
            if name != '':
                CPU_list[product_id].set_name(name)
            if description != '':
                CPU_list[product_id].set_description(description)
            db['CPU'] = CPU_list
        elif product_id in RAM_list:
            if price != '':
                RAM_list[product_id].set_price(int(price))
            if name != '':
                RAM_list[product_id].set_name(name)
            if description != '':
                RAM_list[product_id].set_description(description)
            db['RAM'] = RAM_list
        if product_id in GPU_list:
            if price != '':
                GPU_list[product_id].set_price(int(price))
            if name != '':
                GPU_list[product_id].set_name(name)
            if description != '':
                GPU_list[product_id].set_description(description)
            db['GPU'] = GPU_list
        if product_id in MOBA_list:
            if price != '':
                MOBA_list[product_id].set_price(int(price))
            if name != '':
                MOBA_list[product_id].set_name(name)
            if description != '':
                MOBA_list[product_id].set_description(description)
            db['MOBA'] = MOBA_list
        if product_id in PSU_list:
            if price != '':
                PSU_list[product_id].set_price(int(price))
            if name != '':
                PSU_list[product_id].set_name(name)
            if description != '':
                PSU_list[product_id].set_description(description)
            db['PSU'] = PSU_list
        if product_id in Storage_list:
            if price != '':
                Storage_list[product_id].set_price(int(price))
            if name != '':
                Storage_list[product_id].set_name(name)
            if description != '':
                Storage_list[product_id].set_description(description)
            db['Storage'] = Storage_list
        return redirect(url_for('view_products_admin'))
    else:
        return render_template('updateProductsAdmin.html', item_information=item_information)

@app.route('/deleteProductsAdmin/<product_id>', methods=['GET', 'POST'])
def delete_products_admin(product_id):
    db = shelve.open('products.db', 'c')
    CPU_list = db['CPU']
    RAM_list = db['RAM']
    GPU_list = db['GPU']
    MOBA_list = db['MOBA']
    PSU_list = db['PSU']
    Storage_list = db['Storage']

    if request.method == 'POST':
        if product_id in CPU_list:
            CPU_list.pop(product_id)
            db['CPU'] = CPU_list
        elif product_id in RAM_list:
            RAM_list.pop(product_id)
            db['RAM'] = RAM_list
        elif product_id in GPU_list:
            GPU_list.pop(product_id)
            db['GPU'] = GPU_list
        elif product_id in MOBA_list:
            MOBA_list.pop(product_id)
            db['MOBA'] = MOBA_list
        elif product_id in PSU_list:
            PSU_list.pop(product_id)
            db['PSU'] = PSU_list
        elif product_id in Storage_list:
            Storage_list.pop(product_id)
            db['Storage'] = Storage_list


    return render_template('viewProductsAdmin.html',
                           CPU_list=CPU_list, RAM_list=RAM_list,
                           GPU_list=GPU_list, MOBA_list=MOBA_list,
                           PSU_list=PSU_list, Storage_list=Storage_list)

@app.route('/addProductsAdmin', methods=['GET', 'POST'])
def add_products_admin():
    db = shelve.open('products.db', 'c')
    CPU_list = db['CPU']
    RAM_list = db['RAM']
    GPU_list = db['GPU']
    MOBA_list = db['MOBA']
    PSU_list = db['PSU']
    Storage_list = db['Storage']

    product_id_list = []
    form_name_list = []
    # append all product id and form name into different lists
    for product_type in db:
        for product_id in db[product_type]:
            product_id_list.append(product_id)
            form_name_list.append(db[product_type][product_id].get_form_name())


    if request.method == 'POST':
        product_type = request.form.get('type')
        # product_img = request.form.get('file')
        product_id = request.form.get('product_id')
        name = request.form.get('product_name')
        description = request.form.get('product_description')
        price = request.form.get('product_price')
        form_name = request.form.get('form_name')
        # img = '/static/Images/not-found.png'
        # print(product_img)

        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            if product_type == 'CPU':
                file.save(os.path.join(app.config['UPLOAD_FOLDER_CPU'], filename))
                img = '/static/Images/Products/CPU/' + filename
            elif product_type == 'RAM':
                file.save(os.path.join(app.config['UPLOAD_FOLDER_RAM'], filename))
                img = '/static/Images/Products/RAM/' + filename
            elif product_type == 'GPU':
                file.save(os.path.join(app.config['UPLOAD_FOLDER_GPU'], filename))
                img = '/static/Images/Products/GPU/' + filename
            elif product_type == 'MOBA':
                file.save(os.path.join(app.config['UPLOAD_FOLDER_MOBA'], filename))
                img = '/static/Images/Products/MOBA/' + filename
            elif product_type == 'PSU':
                file.save(os.path.join(app.config['UPLOAD_FOLDER_PSU'], filename))
                img = '/static/Images/Products/PSU/' + filename
            elif product_type == 'Storage':
                file.save(os.path.join(app.config['UPLOAD_FOLDER_Storage'], filename))
                img = '/static/Images/Products/Storage/' + filename


        if product_type == 'CPU':
            CPU_list[product_id] = AddProduct.AddProduct(img, product_id, name, description, price, form_name)
            db['CPU'] = CPU_list
        elif product_type == 'RAM':
            RAM_list[product_id] = AddProduct.AddProduct(img, product_id, name, description, price, form_name)
            db['RAM'] = RAM_list
        elif product_type == 'GPU':
            GPU_list[product_id] = AddProduct.AddProduct(img, product_id, name, description, price, form_name)
            db['GPU'] = GPU_list
        elif product_type == 'MOBA':
            MOBA_list[product_id] = AddProduct.AddProduct(img, product_id, name, description, price, form_name)
            db['MOBA'] = MOBA_list
        elif product_type == 'PSU':
            PSU_list[product_id] = AddProduct.AddProduct(img, product_id, name, description, price, form_name)
            db['PSU'] = PSU_list
        elif product_type == 'Storage':
            Storage_list[product_id] = AddProduct.AddProduct(img, product_id, name, description, price, form_name)
            db['Storage'] = Storage_list
        return redirect(url_for('view_products_admin'))
    else:
        return render_template('addProductsAdmin.html', product_id_list=product_id_list, form_name_list=form_name_list)

@app.route('/viewCustomers')
def view_customers_admin():
    db = shelve.open('register.db', 'c')
    users_dict = db['Users']



    return render_template('viewCutomerssAdmin.html', users_dict=users_dict)



@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/forget_password', methods=["GET", "POST"])
def forget_password():
    error = None
    todaydate = date.today() +timedelta(days=-30)
    passwordAge = todaydate.strftime("%Y-%D-%M")

    form = ForgetPasswordForm(request.form)
    if request.method == 'POST' and form.validate():
        session.pop('user_id', None)

        Email = form.email.data
        list = [Email]
        encodedEmail = encoding(list)
        with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute('SELECT * FROM accounts where Email = %s', (encodedEmail,))
            account = cursor.fetchone()
            if account:
                error = None
                random_str1 = random.randint(1000000,10000000)
                random_str = str(random_str1)

                with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                    cursor.execute('SELECT * FROM accounts where Email = %s', (encodedEmail,))
                    account = cursor.fetchone()
                    Firstname = account['FirstName']
                    LastName = account['LastName']
                    hashpassword = bcrypt.generate_password_hash(random_str)
                    list = [Firstname,LastName]
                    decodingNames = decoding(list)
                    fullname = "{} {}".format(decodingNames[0],decodingNames[1])
                    sql = 'UPDATE accounts SET PasswordAge = %s, Password= %s WHERE Email = %s'
                    val = (passwordAge,hashpassword,encodedEmail)
                    cursor.execute(sql,val)
                    mysql.connection.commit()


                message1 = "Dear {} we have reset your password, your new password is: {} please login and change your password immediately .\n\n Best regards,\n Tech Haven Team.".format(fullname,random_str)
                message = 'Please check email and follow the instruction.'
                mail.send_message(
                        sender='tech.haven.we.sell.you.buy@gmail.com',
                        recipients=[Email],
                        subject="password",
                        body=message1
                    )

                return render_template("LandingSite.html", message=message)


            else:
                message1 = "Dear customer you have not created an account with us. You can create an account by registering with us.\n\n Best regards,\n Tech Haven Team."
                message = 'Please check email and follow the instruction.'
                mail.send_message(
                        sender='tech.haven.we.sell.you.buy@gmail.com',
                        recipients=[Email],
                        subject="Forget Password",
                        body=message1
                    )

                return render_template("LandingSite.html", message=message)




    return render_template('forget_password.html', form=form ,error=error)




if __name__ == '__main__':
    app.run()

