import math
#Find the smallest positive number that is
# evenly divisible by all numbers from 1 to n

def find_primes(n):
    primes = [] 
    for num in range(1,n+1):
        if all(num%i!=0 for i in range(2, int(math.sqrt(num))+1)):
            primes.append(num)
    return primes

def smallest_multiple(n):
    primes = find_primes(n)
    primes.remove(1)
    answer = 1
    for p in primes:
        power = 2
        answer *= p
        while(p**power <= n):
            answer *= p
            power += 1
    return answer
