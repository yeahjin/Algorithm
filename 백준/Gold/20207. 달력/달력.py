import sys

input = sys.stdin.readline

n = int(input())
l = []
for i in range(n):
    a, b= map(int,input().split())
    l.append((a,b))

l = sorted(l, key=lambda x:x[1])
l = sorted(l)
d = {}
for a, b in l:
    for i in range(a,b+1):
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

a = []
max_num = list(d.keys())[0]
t = [max_num]

for n in list(d.keys())[1:]:
    if max_num + 1 == n:
        max_num = n
        t.append(n)
    else:
        max_num = n
        a.append(t)
        t = [n]
if len(t) > 0:
    a.append(t)
ans = 0
for i in a:
    w = max(i) - min(i) + 1
    h = 0
    for j in i:
        if h < d[j]:
            h = d[j]
    ans += w * h
print(ans)