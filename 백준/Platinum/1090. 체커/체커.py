import math
n = int(input())
xl = []
yl = []
arr = []
ans = [math.inf]*n
for _ in range(n):
    x,y = map(int,input().split())
    arr.append([x,y])
    xl.append(x)
    yl.append(y)
l = []
for x in xl:
    for y in yl:
        dis = []
        for nx, ny in arr:
            dis.append(abs(nx - x) + abs(ny-y))
        dis.sort()

        for i in range(len(dis)):
            d = sum(dis[:i+1])
            if ans[i] > d:
                ans[i] = d
print(*ans)