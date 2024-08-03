from collections import deque
n, k, m = map(int,input().split())
d = deque([i for i in range(1,n+1)])
cnt = 0
while d:
    if k > 0:
        d.rotate(1-k)
    else:
        d.rotate(-k)
    print(d.popleft())
    cnt += 1
    if cnt % m == 0:
        k *= -1
