import collections

d = collections.deque()

n = int(input())

l = list(map(int,input().split()))

for i in range(n):
    d.append((l[i],i+1))
ans = []
while d:
    turn, index = d.popleft()
    if turn > 0:
        d.rotate(1-turn)
    else:
        d.rotate(-turn)
    ans.append(index)
print(*ans)