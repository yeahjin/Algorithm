from collections import deque
import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n, m = map(int,sys.stdin.readline().split())
    l = list(map(int,sys.stdin.readline().split()))

    d1 = deque() # idx
    d2 = deque() # rank
    for i in range(n):
        d1.append(i)
        d2.append(l[i])
    cnt = 0
    while True:
        max_num = max(d2)
        if d1[0] == m and max_num == d2[0]:
            cnt += 1
            print(cnt)
            break
        if max_num == d2[0]:
            d1.popleft()
            d2.popleft()
            cnt += 1
        else:
            d1.rotate(-1)
            d2.rotate(-1)