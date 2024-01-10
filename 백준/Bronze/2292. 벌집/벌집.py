n = int(input())

acc = 1 # 1부터 시작한다.
cnt = 1
while True:
    if acc >= n:
        print(cnt)
        break
    acc = acc + cnt * 6
    cnt += 1