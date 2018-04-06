from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = "ThisIsTheSecretAwesomeKey"

@app.route('/')
def index():
    if not 'gold_count' in session and not 'activities_tracker' in session:
        session['gold_count'] = 0
        session['activities_tracker'] = []
    return render_template('index.html')

@app.route('/find_gold', methods=['POST'])
def find_gold():
    print request.form['gold_location']
    if request.form['gold_location'] == "farm":
        winnings = random.randrange(10,21)
        session['activities_tracker'].append("You found "+str(winnings)+" gold on the farm!")
        print session['activities_tracker']
        session['gold_count'] += winnings
    elif request.form['gold_location'] == "cave":
        winnings = random.randrange(5,11)
        session['activities_tracker'].append("You found "+str(winnings)+" gold in the cave!")
        print session['activities_tracker']
        session['gold_count'] += winnings
    elif request.form['gold_location'] == "house":
        winnings = random.randrange(2,6)
        session['activities_tracker'].append("You stole "+str(winnings)+" gold from someone's house! Rude.")
        print session['activities_tracker']
        session['gold_count'] += winnings
    else:
        winnings = random.randrange(-50,51)
        if winnings >= 0:
            session['activities_tracker'].append("You won "+str(winnings)+" gold at the casino!")
        elif winnings < 0:
            session['activities_tracker'].append("You lost "+str(winnings*-1)+" gold at the casino! OUCH.")
        print session['activities_tracker']
        session['gold_count'] += winnings
    return redirect('/')

app.run(debug=True)