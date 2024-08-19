import sys, math, itertools, heapq
input = sys.stdin.readline

def find(x):
    global p
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]

def union(a,b):
    global p
    a = find(a)
    b = find(b)
    if a < b:
        p[b] = a
    else:
        p[a] = b

n = int(input())

edge = []
d = {}
d2 = {}
p = []
for i in range(n):
    a, b = map(float,input().split())
    d[(a,b)] = i
    p.append(i)
    edge.append((a,b))
edges = []

l = list(itertools.combinations(edge,2))
for i in range(len(l)):
    x1 = l[i][0][0]
    y1 = l[i][0][1]
    x2 = l[i][1][0]
    y2 = l[i][1][1]
    cost = math.sqrt((abs(x1-x2))**2 + (abs(y1-y2))**2)
    edges.append((cost,(x1,y1),(x2,y2)))
ans = 0
edges = sorted(edges, key= lambda x:x[0])

for c, a, b in edges:
    idx_a = d[a]
    idx_b = d[b]
    if find(idx_a) != find(idx_b):
        union(idx_a,idx_b)
        ans += c
print(round(ans*100)/100)