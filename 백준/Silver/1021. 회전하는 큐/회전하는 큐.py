from collections import deque
import sys
n, m = map(int,sys.stdin.readline().split())
l = list(map(int,sys.stdin.readline().split()))
d = deque([i for i in range(1,n+1)])
cnt = 0


for i in l:
    while True:
        if i == d[0]:
            d.popleft()
            break
        else:
            if d.index(i) < len(d)/2:
                d.rotate(-1)
                cnt += 1
            else:
                d.rotate(1)
                cnt += 1
print(cnt)