t = int(input())
for _ in range(t):
    d = {}
    c = int(input())
    for i in range(c):
        name, gen = map(str,input().split())
        if gen not in d.keys():
            d[gen] = 1
            continue
        d[gen] += 1
    ans = 1
    for i in d:
        ans *= ( d[i]+1) # 1을 더하는 이유는 안입는 경우
    print(ans-1) # 알몸인 경우 빼주기