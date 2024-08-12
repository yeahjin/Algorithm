import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int,input().split()))

ns = sum(l)
ans = 0

for i in l:
    ns -= i
    ans += ns * i

print(ans)