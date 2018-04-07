from flask import Flask, redirect, render_template, session, flash, request
app = Flask(__name__)
app.secret_key = "SomeSecretKeysAreVerySecret"

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/submit', methods=['POST'])
# def submit():


app.run(debug=True)