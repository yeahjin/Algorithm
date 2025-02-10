import heapq, sys
input = sys.stdin.readline

INF = int(1e9)


def dij(start):
    d = [INF] * (v + 1)
    q = []
    heapq.heappush(q, (0, start))
    d[start] = 0
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


v, e, p = map(int, input().split())
g = [[] for _ in range(v + 1)]
for i in range(e):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))

ori = dij(1)
v1 = dij(p)
vp = ori[p] + v1[v]

if ori[v] >= vp:
    print("SAVE HIM")
else:
    print("GOOD BYE")