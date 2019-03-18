#!/usr/bin/env python

## From "Cracking the code Interview"
## 
## 1.1 Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

def isUniqueWithCount(inputedString):
    for char in inputedString:
        if inputedString.count(char) > 1:
            return False
    return True

def isUniqueWOutCount(inputedString):
    lettersHash = dict()

    for char in inputedString:
        if char in lettersHash:
            return False
        lettersHash.update({char : True})
    return True

def isUniqueNoDataStructure(inputedString):
    letters = sorted(list(inputedString))

    for index in range(len(letters)-1):
        if letters[index] == letters[index+1]:
            return False
    return True
    

if __name__ == "__main__":
    word = input("Enter word to see if unique: ")
    print(isUniqueWithCount(word))

    print(isUniqueWOutCount(word))
    
    print(isUniqueNoDataStructure(word))

