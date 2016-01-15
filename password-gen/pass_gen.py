#! usr/bin/env python
# -*- coding: utf-8 -*-

""" Saturday Jan 9th, 2016
Author - Borgeson
Password generator script - basic version 1.0

Returns randomly generated password of requested length
"""

import random
from flask import Flask, render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_password', methods=['GET','POST'])
def get_password():
    length = request.form['length']
    #Password of length passed
    letters = list('abcdefghijklmnopqrstuvwxyz')
    numbers = list('0123456789')
    characters = list('!@#$%&*?')
    libraries = [letters, numbers, characters]
    new_pass = []

    for i in range(int(length)):
        pool = random.choice(libraries)
        new_pass.append(random.choice(pool))
    
    return ''.join(new_pass)


if __name__ == '__main__':
    app.run(debug=True)
