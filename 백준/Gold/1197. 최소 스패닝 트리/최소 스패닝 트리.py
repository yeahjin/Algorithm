import sys, heapq
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
def find(x):
    global parent
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    global parent
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

v, e = map(int,input().split())
parent = []
for i in range(v+1):
    parent.append(i)

edges = []
ans = 0

for _ in range(e):
    a, b, c = map(int,input().split())
    heapq.heappush(edges,(c,a,b))

for i in range(e):
    cost, a, b = heapq.heappop(edges)
    if find(a) != find(b):
        union(a,b)
        ans += cost
        
print(ans)