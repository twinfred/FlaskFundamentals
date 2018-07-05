from flask import Flask, render_template, request, redirect
from hey import fruit_qualities

app = Flask(__name__)

users = []

@app.route('/', methods=['GET'])

def hello_world():
    first = str(request.args.get("first"))
    last = str(request.args.get("last"))
    return render_template('index.html', users = users, first = first, last = last)

@app.route('/', methods=['POST'])

def add_params():
    first = str(request.args.get("first"))
    last = str(request.args.get("last"))
    firstname = request.form.get('firstname')
    print str(firstname)
    lastname = request.form.get('lastname')
    print str(lastname)
    users.append({
        "firstname": firstname,
        "lastname": lastname,
    })
    return redirect("/?first="+first+"&last="+last)

app.run(debug=True)