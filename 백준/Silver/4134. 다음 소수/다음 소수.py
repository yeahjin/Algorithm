import math

t = int(input())


def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


for i in range(t):
    n = int(input())
    if n < 2:
        print(2)
        continue
    while True:
        if isPrime(n):
            print(n)
            break
        n += 1