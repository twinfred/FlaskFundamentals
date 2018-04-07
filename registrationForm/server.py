from flask import Flask, redirect, render_template, session, flash, request
from datetime import date, datetime
import re
app = Flask(__name__)
app.secret_key = "SomeSecretKeysAreVerySecret"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/submit', methods=['POST'])
def submit():
    # VALIDATION
    valid = True
    today = str(date.today())
    today_year = int(today.split("-")[0])
    today_month = int(today.split("-")[1])
    today_day = int(today.split("-")[2])
    # FORM INPUTS
    email = request.form['email']
    first_name = request.form['first_name']
    last_name= request.form['last_name']
    birthday = request.form['birthday']
    if isinstance(birthday, unicode):
        flash(u'Please enter your birthday.', 'error')
        valid = False
        return redirect('/')
    print birthday
    print type(birthday)
    birth_year = int(str(request.form['birthday']).split("-")[0])
    birth_month = int(str(request.form['birthday']).split("-")[1])
    birth_day = int(str(request.form['birthday']).split("-")[2])
    age = today_year - birth_year - ((today_month, today_day) < (birth_month, birth_day))
    username = request.form['username']
    password = request.form['password']
    pass_confirm = request.form['pass_confirm']
    # EMAIL VALIDATION
    if len(email) < 1:
        flash(u'An email is requred.', 'error')
        valid = False
    elif not EMAIL_REGEX.match(email):
        flash(u'The email you entered is not the correct format.', 'error')
        valid = False
    # NAME VALIDATION
    if len(first_name) < 1:
        flash(u'First Name cannot be empty.', 'error')
        valid = False
    if len(last_name) < 1:
        flash(u'Last Name cannot be empty.', 'error')
        valid = False
    # AGE VALIDATION
    if age < 13:
        flash(u"Sorry, you're too young.", 'error')
        valid = False
    # USERNAME VALIDATION
    if len(username) < 1:
        flash(u'Username cannot be empty.', 'error')
        valid = False
    # PASSWORD VALIDATION
    if len(password) < 8 or len(pass_confirm) < 8:
        flash(u'Your password must be at least 8 characters long.', 'error')
        valid = False
    elif password != pass_confirm:
        flash(u"The passwords you entered don't match.", 'error')
        valid = False
    elif re.search('[0-9]', password) is None or re.search('[A-Z]', password) is None:
        flash(u"Your password must contain at least one uppercase letter and one numeric value.", 'error')
        valid = False
    if valid == False:
        return redirect('/')
    else: 
        flash(u"Your account has been created!", 'success')
        return redirect('/welcome')

app.run(debug=True)