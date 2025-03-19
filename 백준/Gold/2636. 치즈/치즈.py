import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


def bfs(y, x):
    global n, m, on_air
    q = deque()
    q.append((y, x))
    v[y][x] = True
    ccnt = 0
    while q:
        yy, xx = q.popleft()
        for i in range(4):
            ny = dy[i] + yy
            nx = dx[i] + xx
            if 0 <= ny < n and 0 <= nx < m and not v[ny][nx]:
                if mm[ny][nx] == 0:
                    v[ny][nx] = True
                    q.append((ny, nx))
                elif mm[ny][nx] == 1:
                    v[ny][nx] = True
                    mm[ny][nx] = 0
                    ccnt += 1
    return ccnt


n, m = map(int, input().split())

mm = []
for i in range(n):
    mm.append(list(map(int, input().split())))
cnt = 0
c_cnt = 0
while True:
    flag = True
    for i in range(n):
        for j in range(m):
            if mm[i][j] == 1:
                flag = False
    if flag:
        break

    v = [[False] * m for _ in range(n)]
    c_cnt = bfs(0, 0)
    cnt += 1

print(cnt)
print(c_cnt)