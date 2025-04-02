import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
n, m, x = map(int,input().split())
g = [[] for _ in range(n+1)]
dis = [[INF] * (n+1) for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int,input().split())
    g[a].append((b,c))

def dij(start):
    d = [INF] * (n + 1)
    q = []
    heapq.heappush(q,(0, start))
    d[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > d[now]:
            continue
        for i in g[now]:
            cost = dist + i[1]
            if d[i[0]] > cost:
                d[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))
    return d

for i in range(1,n+1):
    tmp = dij(i)
    for j in range(1,n+1):
        dis[i][j] = tmp[j]
ans = -1
for i in range(1,n+1):
    total = dis[i][x] + dis[x][i]
    ans = max(total, ans)
print(ans)