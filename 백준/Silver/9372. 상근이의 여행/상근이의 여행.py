import sys
input = sys.stdin.readline

def find(x):
    global p
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(a, b):
    global p
    a = find(a)
    b = find(b)
    if a < b:
        p[b] = a
    else:
        p[a] = b


t = int(input())
for _ in range(t):
    p = []
    n, m = map(int,input().split())

    for i in range(n+1):
        p.append(i)
    cnt = 0
    edge = []
    for i in range(m):
        a, b = map(int,input().split())
        if find(a) != find(b):
            union(a,b)
            cnt += 1

    print(cnt)