import json
import requests
from flask import Flask, render_template
from flask import request
from random import randint
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET','POST'])
def RPSLS():
    user_choice = request.form['user_choice']
    choices = ['rock','paper','scissors','lizard','spock']
    decisions = {'rock':['paper','spock'],
                 'paper':['lizard','scissors'],
                 'scissors':['rock','spock'],
                 'spock':['lizard','paper'],
                 'lizard':['scissors','rock']}
    
    uri = "http://codechallenge.boohma.com/random"
    rand_num = json.loads(requests.get(uri).text)['random_number']
    comp_choice = choices[rand_num//20]
    user_choice = input("Enter your choice: ").lower()
    while user_choice not in choices:
        user_choice = input("Not a valid choice: ").lower()
    if user_choice == comp_choice:
        winner = 'Tie'
    else:
        if comp_choice in decisions[user_choice]:
            winner = 'Computer'
        else:
            winner = 'User'
    print("Computer chose {0}: User chose {1} -- Winner is {2}".format(
        comp_choice.capitalize(), user_choice.capitalize(), winner))
    return "Computer chose {0}: User chose {1} -- Winner is {2}".format(
        comp_choice.capitalize(), user_choice.capitalize(), winner)


if __name__ == '__main__':
    app.run(debug=True)
    
