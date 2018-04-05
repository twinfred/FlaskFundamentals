from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/submit')
def submit():
    return render_template('submit.html', name = "Tim")

# FORM SUBMIT - POST METHOD
# @app.route('/submit', methods=['POST'])
# def show_user_profile():
#     name = request.form['name']
#     email = request.form['email']
#     print name,email
#     return redirect('/submit')

# FORM SUBMIT - GET METHOD
@app.route('/submit/<name>/<email>')
def show_user_profile(name,email):
    print name,email
    return render_template('submit.html')

app.run(debug=True)