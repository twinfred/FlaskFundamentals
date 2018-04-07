from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "ThisIsMyAwesomeSecretKey"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojos/new')
def dojos():
    return render_template('dojos.html')

@app.route('/submit', methods=["POST"])
def submit_name():
    valid = True
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    if len(request.form['name']) < 1:
        flash('Name cannot be empty.')
        valid = False
    if len(request.form['comment']) > 120:
        flash('Comment cannot be more than 120 characters.')
        valid = False
    if valid == False:
        return redirect('/dojos/new')
    else:
        return render_template('success.html', name=name, location=location, language=language, comment=comment)

app.run(debug=True)