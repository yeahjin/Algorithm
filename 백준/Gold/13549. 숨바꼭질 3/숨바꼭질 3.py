from collections import deque
import sys

input = sys.stdin.readline
MAX = 100001
v = [-1] * (MAX + 1)


def bfs(n, m):
    q = deque()
    q.append(n)
    v[n] = 0
    while q:
        now = q.popleft()
        if now == m:
            print(v[now])
            return
        if now * 2 <= MAX and v[now * 2] == -1:
            v[now * 2] = v[now]
            q.appendleft(now * 2)
        for i in (now - 1, now + 1):
            if 0 <= i <= MAX and v[i] == -1:
                v[i] = v[now] + 1
                q.append(i)


n, m = map(int, input().split())
bfs(n,m)
