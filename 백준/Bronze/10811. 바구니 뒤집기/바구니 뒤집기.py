n, m = map(int,input().split())

l = []
for i in range(n):
    l.append(i+1)

for i in range(m):
    a, b = map(int,input().split())
    tmp = l[a-1:b]
    tmp.reverse()
    cnt = 0
    for j in range(a-1,b):
        l[j] = tmp[cnt]
        cnt+=1
print(*l)