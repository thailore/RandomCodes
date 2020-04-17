def solution(n):
    n = int(n)
    steps = 0
    
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        elif (n == 3) or ((n + 1) & n) > ((n - 1)&(n - 2)):
            n -= 1
        else:
            n += 1
        steps += 1
    return steps

"""

The solution involves using bitwise comparators, it was difficult to understand why that works
until i read https://whatis.techtarget.com/definition/bitwise a bit more

"""
