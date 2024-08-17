import sys
input = sys.stdin.readline

def union(a,b):
    global p
    a = find(a)
    b = find(b)
    if a < b:
        p[b] = a
    else:
        p[a] = b

def find(x):
    global p
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]


n,m = map(int,input().split())
p = []
for i in range(n):
    p.append(i)
ans = 0
for i in range(m):
    a, b = map(int,input().split())
    if find(a) != find(b):
        union(a,b)
    else:
        ans = i + 1
        break

print(ans)