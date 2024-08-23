import sys

input = sys.stdin.readline

n = int(input())
d = {}
l = []
cnt = 0
for i in range(n):
    s = str(input()).rstrip()
    d[s] = i

for i in range(n):
    s = str(input()).rstrip()
    l.append(s)

for i in range(n-1):
    for j in range(i,n):
        if d[l[i]] > d[l[j]]:
            cnt += 1
            break

print(cnt)
