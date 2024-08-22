import sys, math
from itertools import combinations

input = sys.stdin.readline

def union(a,b):
    global p
    a = find(a)
    b = find(b)
    if a < b:
        p[b] =a
    else:
        p[a]= b

def find(x):
    global p
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]


n, m = map(int,input().split())
p = []
for i in range(n+1):
    p.append(i)
d = {}
edges = []

for i in range(n):
    a, b = map(int,input().split())
    edges.append((a,b))
    d[(a,b)] = i+1

for i in range(m):
    a, b = map(int,input().split())
    union(a,b)

l = list(combinations(edges,2))
result = []

for a,b in l:
    x1 = a[0]
    x2 = b[0]
    y1 = a[1]
    y2 = b[1]
    length = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    result.append((length,d[a],d[b]))

result = sorted(result, key = lambda x:x[0])
ans = 0
for i in range(len(result)):
    cost, a, b = result[i]
    if find(a) != find(b):
        union(a,b)
        ans += cost
print("%.2f" %ans)