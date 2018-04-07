from flask import Flask, render_template, flash, redirect, session, request
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'ThisIsMySecretKeyForNow'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # Name Validation
    if len(request.form['name']) < 1:
        flash('Name cannot be empty')
    else:
        flash('Success! Your name is {}'.format(request.form['name']))
    # Email Validation
    if len(request.form['email']) < 1:
        flash('Email cannot be empty')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("The email address you entered is invalid")
    else:
        flash('Success! Your email is {}'.format(request.form['email']))
    return redirect('/')

app.run(debug=True)