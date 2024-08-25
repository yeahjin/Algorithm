import sys
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

while True:
    n , m = map(int,input().split())
    if n == 0 and m == 0:
        break
    edges = []
    p = []
    for i in range(n):
        p.append(i)

    total = 0
    for i in range(m):
        a,b,c = map(int,input().split())
        edges.append((c,a,b))
        total += c
    edges.sort()

    result = 0
    for i in edges:
        cost, a, b = i
        if find(a) != find(b):
            result += cost
            union(a,b)

    print(total - result)