from collections import deque
import sys
n = int(input())
dx = [0,0,-1,1]
dy = [-1,1,0,0]
l = []

for i in range(n):
    l.append(list(map(int,input().split())))

ans = -1 * sys.maxsize


def bfs(x, y,h):
    q = deque()
    q.append([x,y])
    global visited
    visited[x][y] = True
    while q:
        node = q.popleft()
        xx = node[0]
        yy = node[1]
        for i in range(4):
            global dx, dy
            cx = dx[i] + xx
            cy = dy[i] + yy
            if cx >= n or cy >= n or cx < 0 or cy < 0:
                continue
            if l[cx][cy] <= h:
                continue
            if visited[cx][cy]:
                continue
            visited[cx][cy] = True
            q.append([cx,cy])

for h in range(101):
    visited = []
    for j in range(n):
        visited.append([False] * n)
    cnt = 0
    for r in range(n):
        for c in range(n):
            if visited[r][c]:
                continue
            if l[r][c] <= h:
                continue
            bfs(r,c,h)
            cnt += 1
    ans = max(ans,cnt)
print(ans)