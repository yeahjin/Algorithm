import heapq
import sys

input = sys.stdin.readline
MOD = 1000000007
t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    q = []
    ans = 1
    for i in l:
        heapq.heappush(q,i)
    while q:
        if len(q) == 1:
            break
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        ans *= a * b % MOD
        heapq.heappush(q, a*b)
    print(ans % MOD)