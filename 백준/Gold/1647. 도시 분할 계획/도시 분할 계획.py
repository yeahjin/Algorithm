import sys, itertools
input = sys.stdin.readline

def union(a, b):
    global p
    a = find(a)
    b = find(b)
    if a < b:
        p[b] = a
    else:
        p[a] = b

def find(x):
    global p
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

n, m = map(int,input().split())
graph = []
p = []
for _ in range(m):
    a, b, c= map(int,input().split())
    graph.append((c,a,b))

for i in range(n+1):
    p.append(i)
graph.sort()
result = 0
last = 0
for i in graph:
    cost, a, b = i
    if find(a) != find(b):
        result += cost
        last = cost
        union(a,b)

print(result-last)