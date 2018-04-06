from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "TimIsAwesome"

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/show')
# def submit():
#     return render_template('show.html', name = session['name'], email = session['email'])

@app.route('/show')
def submit():
    return render_template('show.html')

# FORM SUBMIT - POST METHOD
@app.route('/submit', methods=['POST'])
def show_user_profile():
    if request.form['action'] == 'register':
        session['name'] = request.form['name']
        session['email'] = request.form['email']
        print session['name'], session['email']
        return redirect('/')

# # FORM SUBMIT - GET METHOD
# @app.route('/submit/<name>/<email>')
# def show_user_profile(name,email):
#     print name,email
#     return render_template('submit.html')

app.run(debug=True)