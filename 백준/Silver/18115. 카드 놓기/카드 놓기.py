import sys
import collections
input = sys.stdin.readline

n = int(input())
l = list(reversed(list(map(int,input().split()))))
d = [i for i in range(1,n+1)]
ans = collections.deque()

for i in range(n):
    if l[i] == 1:
        ans.appendleft(d[i])
    elif l[i] == 2:
        ans.insert(1,d[i])
    else:
        ans.append(d[i])

print(*ans)