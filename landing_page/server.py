from flask import Flask, render_template, request, redirect
app = Flask(__name__)

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
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    print name
    print location
    print language
    print comment
    return render_template('success.html', name=name, location=location, language=language, comment=comment)

app.run(debug=True)