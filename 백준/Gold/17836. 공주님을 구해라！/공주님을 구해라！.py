# 공주님을 구해라!

# 1. (0,0)으로 들어온다.
# 2. 칼을 찾으면 벽이 있어도 무제한으로 뚫을 수 있다.
# 3. 0 : 빈칸, 1 : 마법의 벽, 2 : 칼 위치
# 4. n: 세로 | m: 가로 _
import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    q = deque()
    v = [[0] * m for _ in range(n)]
    q.append((0,0,0))
    v[0][0] = 1
    while q:
        y, x, cnt = q.popleft()
        if y == n-1 and x == m-1:
            return cnt
        for i in range(4):
            yy = dy[i] + y
            xx = dx[i] + x
            if 0 <= yy < n and 0 <= xx < m:
                if v[yy][xx] == 0:
                    if g[yy][xx] == 0:
                        q.append((yy,xx,cnt+1))
                        v[yy][xx] = 1

def bfs_s(sword):
    q = deque()
    v = [[0] * m for _ in range(n)]
    q.append((0,0,0))
    v[0][0] = 1
    ey, ex = sword
    while q:
        y, x, cnt = q.popleft()
        if y == ey and x == ex:
            return cnt
        for i in range(4):
            yy = dy[i] + y
            xx = dx[i] + x
            if 0 <= yy < n and 0 <= xx < m:
                if v[yy][xx] == 0:
                    if g[yy][xx] != 1:
                        q.append((yy,xx,cnt+1))
                        v[yy][xx] = 1

def bfs_s_t_e(sword):
    q = deque()
    ey, ex = sword
    v = [[0] * m for _ in range(n)]
    q.append((ey,ex,0))
    v[ey][ex] = 1
    while q:
        y, x, cnt = q.popleft()
        if y == n-1 and x == m-1:
            return cnt
        for i in range(4):
            yy = dy[i] + y
            xx = dx[i] + x
            if 0 <= yy < n and 0 <= xx < m:
                if v[yy][xx] == 0:
                    q.append((yy,xx,cnt+1))
                    v[yy][xx] = 1

n, m, t = map(int,input().split())

sword = [0,0]
g = []
for i in range(n):
    tmp = list(map(int,input().split()))
    g.append(tmp)
    for j in range(m):
        if g[i][j] == 2:
            sword[0] = i
            sword[1] = j

a = bfs()
b = bfs_s(sword)
c = bfs_s_t_e(sword)
d = 0
if a == None:
    a = int(1e9)
if b == None or c == None:
    d = int(1e9)
else:
    d = b + c

ans = min(a,d)
if ans <= t:
    print(ans)
else:
    print("Fail")