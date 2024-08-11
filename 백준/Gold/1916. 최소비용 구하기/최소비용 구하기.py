import sys, heapq, math
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
distance = [math.inf] * (n+1)


for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))

start, end = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for e, c in graph[now]:
            cost = dist + c
            if cost < distance[e]:
                distance[e] = cost
                heapq.heappush(q,(cost,e))

dijkstra(start)

print(distance[end])