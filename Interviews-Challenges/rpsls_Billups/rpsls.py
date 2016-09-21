#! usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

#initialize scores and wins at beginning
scores = [0,0,0]
wins = []

@app.route('/_RPSLS')
def RPSLS():
    user_choice = request.args.get('user_choice',type=str).lower()

    choices = ['rock','paper','scissors','lizard','spock']

    #Dictionary of each choice with the decisions it loses to
    decisions = {'rock':['paper','spock'],
                 'paper':['lizard','scissors'],
                 'scissors':['rock','spock'],
                 'spock':['lizard','paper'],
                 'lizard':['scissors','rock']}

    #get random number from endpoint provided
    uri = "http://codechallenge.boohma.com/random"
    rand_num = json.loads(requests.get(uri).text)['random_number']

    #divide number to get one of the five choices and make computer choice
    comp_choice = choices[rand_num//20]

    #if ten wins already shown, delete oldest one
    if len(wins) == 10:
        wins.remove(wins[0])

    #comparisons of choices
    if user_choice == comp_choice:
        winner = 'Tie'
        won = "It's a Tie!"
    else:
        if comp_choice in decisions[user_choice]:
            winner = 'Computer'
            won = "Computer Won :("
        else:
            winner = 'User'
            won = "User Won! :)"
    
    #array of number of wins
    wins.append(winner)
    scores[0] = wins.count('Computer')
    scores[1] = wins.count('User')
    scores[2] = wins.count('Tie')

    #send json of data back to jquery
    return jsonify(result="Computer chose {0}: User chose {1} -- {2}".format(
        comp_choice.capitalize(), user_choice.capitalize(), won), score=scores)


@app.route('/reset', methods=['GET', 'POST'])
def reset():
    wins = []
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    wins.clear()
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

