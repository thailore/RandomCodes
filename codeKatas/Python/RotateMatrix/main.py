#!/usr/bin/env python

## Given matrix NxN, rotate the matrix 90 degrees Clockwise

def rotateMatrix(matrix):
    return list(list(tupleValue)[::-1] for tupleValue in zip(*matrix))


