# 다익스트라
import heapq, sys

input = sys.stdin.readline
INF = int(1e9)


def dij(start):
    d = [INF] * (n + 1)
    d[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > d[now]:
            continue
        for i in g[now]:
            cost = i[1] + dist
            if cost < d[i[0]]:
                d[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return d


n, m, k, x = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int,input().split())
    g[a].append((b,1))
ori = dij(x)
flag = False
for i in range(1,n+1):
    if ori[i] == k:
        print(i)
        flag = True
if not flag:
    print(-1)