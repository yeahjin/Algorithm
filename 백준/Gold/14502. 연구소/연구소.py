import sys
import copy
from collections import deque
from itertools import combinations
input = sys.stdin.readline

ans = -1
dx = [0,0,-1,1]
dy = [1,-1,0,0]
n, m = map(int,input().split()) # 세로, 가로
def print_arr(arr):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                cnt += 1
    return cnt

def bfs(y,x,g3):
    q = deque()
    q.append((y,x))
    while q:
        yy, xx = q.popleft()
        for i in range(4):
            ny = yy + dy[i]
            nx = xx + dx[i]
            if ny >= n or nx >= m or ny < 0 or nx < 0:
                continue
            if g3[ny][nx] != 0:
                continue
            g3[ny][nx] = 2
            q.append((ny,nx))

g = []

for i in range(n):
    g.append(list(map(int,input().split())))

# 바이러스, 벽 위치 판별
v = [] # 바이러스
w = [] # 벽 X, 바이러스 X
for i in range(n):
    for j in range(m):
        if g[i][j] == 2:
            v.append((i,j))
        if g[i][j] == 0:
            w.append((i,j))

# 3개 겹치지 않게 벽 세우기
walls = list(combinations(w,3))

# 새로 세운 벽 반영해서 바이러스 퍼지게 하기
for wall in walls:
    a, b, c = wall
    g2 = copy.deepcopy(g)
    g2[a[0]][a[1]] = 1
    g2[b[0]][b[1]] = 1
    g2[c[0]][c[1]] = 1
    for y in range(n):
        for x in range(m):
            if g2[y][x] == 2:
                bfs(y,x,g2)
    ans = max(ans, print_arr(g2))
print(ans)