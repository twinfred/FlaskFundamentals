from flask import Flask, render_template, session
app = Flask(__name__)
app.secret_key = "TimIsAwesome"

@app.route('/')
def index():
    if not 'counter' in session:
        session['counter'] = 1
    else:
        session['counter'] += 1
    return render_template('index.html')

app.run(debug=True)