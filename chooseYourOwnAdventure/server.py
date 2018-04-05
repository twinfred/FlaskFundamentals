from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def start():
    return render_template('choice00-start.html')

@app.route('/01a')
def lvl_01a():
    return render_template('choice01a.html')

@app.route('/01b')
def lvl_01b():
    return render_template('choice01b.html')

@app.route('/02a')
def lvl_02a():
    return render_template('choice02a.html')

@app.route('/02b')
def lvl_02b_die():
    return render_template('choice02b-die.html')

@app.route('/02c')
def lvl_02c():
    return render_template('choice02c.html')

@app.route('/02d')
def lvl_02d_die():
    return render_template('choice02d-die.html')

@app.route('/03a')
def lvl_03a():
    return render_template('choice03a.html')

@app.route('/03b')
def lvl_03b_die():
    return render_template('choice03b-die.html')

@app.route('/win')
def win():
    return render_template('choice04-win.html')

app.run(debug=True)