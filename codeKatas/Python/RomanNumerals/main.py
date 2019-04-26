#!/usr/bin/env python

def romanNumeralsAdd(romanNumerals):
    answer = ''

    base = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    maxValues = {'I':3, 'V':1, 'X':3, 'L':1, 'C':3, 'D':1, 'M':1000}
    
    for numeral in romanNumerals:
        answer += numeral
    
    for index in range(len(base)):
        value = base[index]
        extras = ''
        if value == 'I' and answer.count(value) == maxValues.get(value) + 1:
            extras = value
        if answer.count(value) > maxValues.get(value):
            answer = answer.replace(value, '')
            answer += base[index+1]
        answer = answer + extras

        
    return answer[::-1]


