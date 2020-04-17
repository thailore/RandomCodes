def solution(n):
    size = n + 1

    # create staircase foundation in form of zeros matrix
    staircase = [[0 for _ in xrange(size)] for _ in xrange(size)]
    staircase[0][0] = 1 # base value
    
    for i in xrange(1, size):
        for j in xrange(0, size):
            staircase[i][j] = staircase[i - 1][j]
            if j >= i:
                staircase[i][j] += staircase[i - 1][j - i]

    return staircase[n][n] - 1

