import sys
import heapq
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [1,-1,0,0]

n, m = map(int,input().split())
g = [list(map(str,input().strip())) for _ in range(m)]
INF = int(1e9)
g2 = [[INF] * n for _ in range(m)]
def bfs():
    q = []
    heapq.heappush(q,(0,0,0))
    g2[0][0] = 0
    while q:
        cnt, yy, xx = heapq.heappop(q)
        if yy == m-1 and xx == n-1:
            print(cnt)
            return
        for i in range(4):
            nx = dx[i] + xx
            ny = dy[i] + yy
            if 0 <= ny < m and 0 <= nx < n:
                if g[ny][nx] == '0':
                    cost = cnt
                    if g2[ny][nx] > cost:
                        g2[ny][nx] = cost
                        heapq.heappush(q,(cost, ny, nx))
                if g[ny][nx] == '1':
                    cost = cnt + 1
                    if g2[ny][nx] > cost:
                        g2[ny][nx] = cost
                        heapq.heappush(q,(cost,ny,nx))
bfs()