import sys
sys.setrecursionlimit(100000)
def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        par[b] = a
    else:
        par[a] = b


def find(a):
    if par[a] != a:
        par[a] = find(par[a])
    return par[a]


n, m = map(int,input().split())
par = [i for i in range(n+1)]

for _ in range(m):
    x,a,b = map(int,sys.stdin.readline().split())
    if x == 0:
        union(a,b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")