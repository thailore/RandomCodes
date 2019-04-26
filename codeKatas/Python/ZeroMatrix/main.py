#!/usr/bin/env python

def zeroMatrix(matrix):
    toBeZeroed = []
    for index1 in range(len(matrix)):
        for index2 in range(len(matrix[index1])):
            if matrix[index1][index2] == 0:
                toBeZeroed.append([index1, index2])
    for pair in toBeZeroed:
        zeroOut(pair, matrix)
    return matrix

def zeroOut(pair, matrix):
    row = pair[0]
    column = pair[1]
    for index1 in range(len(matrix)):
        for index2 in range(len(matrix)):
            if index1 == row or index2 == column:
                matrix[index1][index2] = 0

