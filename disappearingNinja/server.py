from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja/<color>')
def ninja():
    print color
    return render_template('ninja.html', alt = 'tmnt')


app.run(debug=True)