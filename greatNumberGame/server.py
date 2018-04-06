from flask import Flask, render_template, session, request, redirect
import random
app = Flask(__name__)
app.secret_key = "TimIsAwesome"

@app.route('/')
def index():
    if not 'status' in session or session['status'] == "Play Again" and session['answer'] == 0:
        session['status'] = ""
        session['answer'] = random.randrange(0, 101)
        print session['answer']
        return render_template('index.html')
    else:
        if session['status'] == "Winner":
            return render_template('winner.html')
        elif session['status'] == "Too Low":
            return render_template('too_low.html')
        elif session['status'] == "Too High":
            return render_template('too_high.html')
        else:
            return render_template('index.html')

@app.route('/check_num', methods=['POST'])
def guess():
    print request.form['guess']
    if session['answer'] == 0:
        session['answer'] = random.randrange(0, 101)
        print session['answer']
    if int(request.form['guess']) == session['answer']:
        session['status'] = "Winner"
    elif int(request.form['guess']) < session['answer'] and int(request.form['guess']) != 0:
        session['status'] = "Too Low"
    elif int(request.form['guess']) > session['answer']:
        session['status'] = "Too High"
    else:
        session['status'] = "Play Again"
        session['answer'] = 0
    return redirect('/')

app.run(debug=True)