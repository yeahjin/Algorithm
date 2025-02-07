import heapq
def solution(n, edge):
    answer = 0
    
    INF = int(1e9)
    g =[[] for i in range(n+1)]
    d = [INF] * (n+1)
    
    for a, b in edge:
        g[a].append((b,1))
        g[b].append((a,1))
        
    d[1] = 0
    q = []
    heapq.heappush(q,(0,1))
    
    while q:
        dist, now = heapq.heappop(q)
        if dist > d[now]:
            continue
        for i in g[now]:
            cost = dist + i[1]
            if cost < d[i[0]]:
                d[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    answer = d.count(max(d[1:]))
    
    return answer