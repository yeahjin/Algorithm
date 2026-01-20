import sys
input = sys.stdin.readline

def solve(n,t,p):
    dp = [0]*(n+1)

    if t[n-1] == 1:
        dp[n-1] = p[n-1]

    for i in range(n-2,-1,-1):
        day = i+t[i]
        if day == n:
            dp[i] = max(p[i],dp[i+1])
        elif day < n:
            dp[i] = max(p[i]+dp[day],dp[i+1])
        elif day > n:
            dp[i] = dp[i+1]

    print(dp[0])

n = int(input())
t = []
p = []
for i in range(n):
    ti, pi = map(int,input().split())
    t.append(ti)
    p.append(pi)
solve(n,t,p)