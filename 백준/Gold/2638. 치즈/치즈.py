import sys
from collections import deque
input = sys.stdin.readline

dc = [0, 0, 1, -1]
dr = [1, -1, 0, 0]

def valid(l):
    for i in range(len(l)):
        for j in range(len(l[0])):
            if l[i][j] == 1:
                return False
    return True
def bfs(c, r):
    q = deque()
    q.append((c, r))
    v[c][r] = True
    s = set()
    while q:
        cc, rr = q.popleft()
        for i in range(4):
            nc = dc[i] + cc
            nr = dr[i] + rr
            if 0 <= nc < n and 0 <= nr < m:
                if g[nc][nr] == 0 and not v[nc][nr]:
                    q.append((nc, nr))
                    v[nc][nr] = True
                if g[nc][nr] == 1:
                    if (nc, nr) in s:
                        g[nc][nr] = 0
                        v[nc][nr] = True
                    else:
                        s.add((nc, nr))


n, m = map(int, input().split())
g = []


for i in range(n):
    tmp = list(map(int, input().split()))
    g.append(tmp)
cnt = 0
while True:
    if valid(g):
        print(cnt)
        break
    v = [[False] * m for _ in range(n)]
    bfs(0,0)
    cnt += 1