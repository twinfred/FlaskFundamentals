from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja(ninja):
    print ninja
    return render_template('ninja.html', img = "static/img/tmnt.png", alt = 'tmnt')

@app.route('/ninja/<color>')
def ninja_color(color):
    print color
    if color == "red":
        return render_template('ninja.html', img = "/static/img/raphael.jpg", alt = 'tmnt')
    elif color == "blue":
        return render_template('ninja.html', img = "/static/img/leonardo.jpg", alt = 'tmnt')
    elif color == "orange":
        return render_template('ninja.html', img = "/static/img/michelangelo.jpg", alt = 'tmnt')
    elif color == "purple":
        return render_template('ninja.html', img = "/static/img/donatello.jpg", alt = 'tmnt')
    else:
        return render_template('ninja.html', img = "/static/img/notapril.jpg", alt = 'tmnt')

app.run(debug=True)