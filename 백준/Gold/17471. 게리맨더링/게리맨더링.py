from collections import deque
import sys

input = sys.stdin.readline

def bfs(a):
    q = deque()
    visited = [0] * (n+1)
    q.append(a[0])
    visited[a[0]] = 1
    cnt = 1
    while q:
        node = q.popleft()
        for i in g[node]:
            if i in a and visited[i] == 0:
                visited[i] = 1
                cnt += 1
                q.append(i)
    return cnt


# 선거구 나누기
def dfs(d):
    global cnt, min_num
    if cnt >= (2**n) // 2:
        return
    if d == n:
        cnt += 1
        if v == [1] * n:
            return
        arr1, arr2 = [], []
        for i in range(n):
            if v[i] == 1:
                arr1.append(i+1)
            if v[i] == 0:
                arr2.append(i+1)
        if bfs(arr1) + bfs(arr2) == n:
            tmp1, tmp2 = 0, 0
            for i in arr1:
                tmp1 += human[i]
            for i in arr2:
                tmp2 += human[i]
            min_num = min(min_num, abs(tmp1-tmp2))

        return
    v[d] = 1
    dfs(d+1)
    v[d] = 0
    dfs(d+1)



n = int(input())
human = [0] + list(map(int,input().split()))

g = [[]]
for i in range(n):
    tmp = list(map(int,input().split()))
    g.append(tmp[1:])
v = [0] * n
cnt = 0
min_num = int(1e9)
dfs(0)
if min_num == int(1e9):
    print(-1)
else:
    print(min_num)