l = [True] * 300000

l[0] = l[1] = False

for i in range(2,300000):
    if l[i]:
        for j in range(2*i,300000,i):
            if l[j]:
                l[j] = False

n = int(input())

while True:
    if n == 0:
        break
    cnt = 0
    for i in range(n+1, 2*n+1):
        if l[i]:
            cnt += 1
    print(cnt)
    n = int(input())