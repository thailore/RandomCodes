from fractions import Fraction

def solution(mat):
    result = transform(mat)
    if result[1] == len(mat):
        return [1, 1]
    Q, R = splitQR(*result)
    inv = inverse(Q)
    result = multiplyMatrices(inv, R)
    row = result[0]
    l = 1
    for item in row:
        l = leastCommonMultiple(l, item.denominator)
    result = list(map(lambda x: long(x.numerator*l/x.denominator), row))
    result.append(l)
    return result
    
def greatestCommonDenominator(x, y):
    def gcd1(x, y):
        if y == 0:
            return x
        return gcd1(y, x%y)
    return gcd1(abs(x), abs(y))

def simplify(x, y):
    denominator = greatestCommonDenominator(x, y)
    return Fraction(long(x/denominator), long(y/denominator))

def leastCommonMultiple(x, y):
    return long(x*y/greatestCommonDenominator(x,y))

def transform(mat):
    listOfSums = list(map(sum, mat))
    booleanIndices = list(map(lambda x: x == 0, listOfSums))
    indices = set([i for i, x in enumerate(booleanIndices) if x])
    newMatrix = []
    for i in range(len(mat)):
        newMatrix.append(list(map(lambda x: Fraction(0, 1) if(listOfSums[i] == 0) else simplify(x, listOfSums[i]), mat[i])))
    transformedMatrix = []
    zerosMatrix = []
    for i in range(len(newMatrix)):
        if i not in indices:
            transformedMatrix.append(newMatrix[i])
        else:
            zerosMatrix.append(newMatrix[i])
    transformedMatrix.extend(zerosMatrix)
    tmat = []
    for i in range(len(transformedMatrix)):
        tmat.append([])
        extendedMatrix = []
        for j in range(len(transformedMatrix)):
            if j not in indices:
                tmat[i].append(transformedMatrix[i][j])
            else:
                extendedMatrix.append(transformedMatrix[i][j])
        tmat[i].extend(extendedMatrix)
    return [tmat, len(zerosMatrix)]

def copyMatrix(matrix):
    copiedMatrix = []
    for i in range(len(matrix)):
        copiedMatrix.append([])
        for j in range(len(matrix[i])):
            copiedMatrix[i].append(Fraction(matrix[i][j].numerator, matrix[i][j].denominator))
    return copiedMatrix

def gaussElmination(matrix, values):
    mat = copyMatrix(matrix)
    for i in range(len(mat)):
        index = -1
        for j in range(i, len(mat)):
            if mat[j][i].numerator != 0:
                index = j
                break
        if index == -1:
            raise ValueError('Gauss elimination failed!')
        mat[i], mat[index] = mat[index], mat[j]
        values[i], values[index] = values[index], values[i]
        for j in range(i+1, len(mat)):
            if mat[j][i].numerator == 0:
                continue
            ratio = -mat[j][i]/mat[i][i]
            for k in range(i, len(mat)):
                mat[j][k] += ratio * mat[i][k]
            values[j] += ratio * values[i]
    result = [0 for i in range(len(mat))]
    for i in range(len(mat)):
        index = len(mat) -1 -i
        end = len(mat) - 1
        while end > index:
            values[index] -= mat[index][end] * result[end]
            end -= 1
        result[index] = values[index]/mat[index][index]
    return result

def transpose(mat):
    tmat = []
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i == 0:
                tmat.append([])
            tmat[j].append(mat[i][j])
    return tmat

def inverse(matrix):
    transponsedMatrix = transpose(matrix)
    inversedMatrix = []
    for i in range(len(transponsedMatrix)):
        values = [Fraction(int(i==j), 1) for j in range(len(matrix))]
        inversedMatrix.append(gaussElmination(transponsedMatrix, values))
    return inversedMatrix

def multiplyMatrices(mat1, mat2):
    result = []
    for i in range(len(mat1)):
        result.append([])
        for j in range(len(mat2[0])):
            result[i].append(Fraction(0, 1))
            for k in range(len(mat1[0])):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result

def splitQR(matrix, lengthR):
    lengthQ = len(matrix) - lengthR
    Q = []
    R = []
    for i in range(lengthQ):
        Q.append([int(i==j)-matrix[i][j] for j in range(lengthQ)])
        R.append(matrix[i][lengthQ:])
    return [Q, R]
