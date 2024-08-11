import math
import sys
import heapq
input = sys.stdin.readline

v, e = map(int,input().split())
start = int(input())
graph = [[] for i in range(v+1)]
distance = [math.inf] * (v+1)

for _ in range(e):
    u, v, w = map(int,input().split())
    graph[u].append((v,w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

dijkstra(start)

for i in range(1,len(distance)):
    if distance[i] == math.inf:
        print("INF")
    else:
        print(distance[i])