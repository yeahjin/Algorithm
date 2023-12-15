n = int(input())
l = list(map(int,input().split()))
x = int(input())

j = n - 1
i = 0
cnt = 0

l = sorted(l)

while True:
    if i >= j:
        break
    if l[i] + l[j] > x:
        j -= 1
    elif l[i] + l[j] < x:
        i += 1
    else:
        cnt += 1
        i += 1
        j -= 1
print(cnt)