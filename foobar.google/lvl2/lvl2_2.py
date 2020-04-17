def solution(x, y):
    '''
    Seems like a mathematical equation could be possible to solve this
    due to the relational pattern;'' between numbers
    
    [1]       [2]       [3]       [4]
    [1]    1 (+1) -> 2 (+2) -> 4 (+3) -> 7
    [2]    3 (+2) -> 5 (+3) -> 8 (+4) -> 12
    [3]    6 (+3) -> 9 (+4) -> 13 (+5) -> 18
    [4]    10 (+4) -> 14 (+5) -> 19 (+6) -> 25
    
    [(n)(n-1) / 2] + 1 starting at 1
    (1 * (1-1) / 2 ) + 1 == 1
    (2 * (2-1) / 2 ) + 1 == 2
    (3 * (3-1) / 2 ) + 1 == 4
    (4 * (4-1) / 2 ) + 1 == 7
    
    [(n+1)(n) / 2] + 2 starting at 1
    (1 * (1+1) / 2 ) + 2 == 3
    (2 * (2+1) / 2 ) + 2 == 5
    (3 * (3+1) / 2 ) + 2 == 8
    (4 * (4+1) / 2 ) + 2 == 12
    
    [(n+2)(n+1) / 2] + 3 starting at 1
    [(n)(n+1) / 2] + 2 starting at 1
    (1 * (1+1) / 2 ) + 2 == 3
    (2 * (2+1) / 2 ) + 2 == 5
    (3 * (3+1) / 2 ) + 2 == 8
    (4 * (4+1) / 2 ) + 2 == 12
    
    (x + [n – 1]) ([x – 1] + [n – 1]) / 2 + x
    simplified as 
    [(x + n – 1)(x + n – 2)] / 2 + x
    where n can be represented as y
    '''
    val = (((x + y - 1) * (x + y - 2)) / 2) + x
    return str(int(val))
