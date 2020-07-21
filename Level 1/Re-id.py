import math


def prime(a):
    if (a % 2 == 0) and (a > 2):
        return False
    return all(a % i for i in range(3, int(math.sqrt(a)) + 1, 2))


primes = ''

for i in range(2, 21000):
    if len(primes) < 10000:
        if prime(i):
            primes = primes + str(i)
    else:
        break


def solution(a):
    reid = primes[a:a+5:1]
    return(reid)
