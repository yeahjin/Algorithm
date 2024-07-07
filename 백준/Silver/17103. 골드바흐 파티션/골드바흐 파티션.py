import sys

t = int(input())
is_prime = [True] * 2000001

is_prime[0] = False
is_prime[1] = False

for i in range(2, 2000001):
    if is_prime[i]:
        for j in range(i * 2, 2000001, i):
            if is_prime[j]:
                is_prime[j] = False

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    cnt = 0
    for i in range(2, n//2+1):
        tmp = 0
        if is_prime[i]:
            tmp = n - i
        if is_prime[tmp]:
            cnt += 1
    print(cnt)
