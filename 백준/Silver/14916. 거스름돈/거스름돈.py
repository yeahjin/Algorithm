n = int(input())
cnt = 0
while True:
    if n == 1:
        cnt = -1
        break
    if n % 5 == 0:
        cnt += 1
        n -= 5
    else:
        cnt += 1
        n -= 2
    if n == 0:
        break
    elif 0 < n < 2:
        cnt = -1
        break
print(cnt)