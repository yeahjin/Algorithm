def r(d):
    global min_num
    if d == n:
        start, link = 0, 0
        if v.count(1) == n//2:
            for i in range(n):
                for j in range(n):
                    if v[i] == 0 and v[j] == 0:
                        start += g[i][j]
                    if v[i] == 1 and v[j] == 1:
                        link += g[i][j]
            min_num = min(min_num, abs(start - link))
        return
    v[d] = 1
    r(d + 1)
    v[d] = 0
    r( d+1)


n = int(input())
v = [0] * n
g = []
for i in range(n):
    t = list(map(int,input().split()))
    g.append(t)
min_num = int(1e9)
r(0)
print(min_num)