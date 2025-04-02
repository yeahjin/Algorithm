import heapq
import sys
input = sys.stdin.readline
# 다익스트라를 위한 코드 (인접리스트)
INF = int(1e9)

def dij(start,g):
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


n, m, x = map(int,input().split())
g = [[] for _ in range(n+1)]
g_r = [[] for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int,input().split())
    g[a].append((b,c))
    g_r[b].append((a,c))

ntox = dij(x,g)
xton = dij(x,g_r)
ans = -1
for i in range(1,n+1):
    if i != x:
        ans = max(ans,ntox[i] + xton[i])
print(ans)