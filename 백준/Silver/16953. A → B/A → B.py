a, b = map(int,input().split())
cnt = 0
while True:
    if b % 2 == 0:
        b //= 2
        cnt += 1
    elif str(b)[-1] == "1":
        b = int(str(b)[:len(str(b))-1])
        cnt += 1
    else:
        print(-1)
        exit()
    if b == a:
        cnt += 1
        break
    if b < a:
        print(-1)
        exit()
print(cnt)