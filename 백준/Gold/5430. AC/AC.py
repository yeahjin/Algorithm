from collections import deque

t = int(input())

for i in range(t):
    s = input()
    n = int(input())
    l = deque()
    s2 = input().split(',')

    # 리스트 deque 넣기
    if n == 1:
        l.append(s2[0][1:len(s2[0])-1])
    elif n == 0:
        pass
    else:
        for i in range(len(s2)):
            if i == 0:
                l.append(s2[i][1:])
            elif i == len(s2) - 1:
                l.append(s2[i][:len(s2[i])-1])
            else:
                l.append(s2[i])
    if s.count("D") > n:
        print("error")
        continue
    # 1 이면 앞, -1이면 뒤
    flag = 1
    # deque에 입력
    for j in s:
        if j == "R":
            flag *= -1
        if j == "D":
            if flag == 1:
                l.popleft()
            else:
                l.pop()
    if flag == -1:
        l.reverse()
    ans = "["
    for i in range(len(l)-1):
        ans = ans + l[i] + ","
    if len(l) == 0:
        ans += ']'
    else:
        ans = ans + l[-1] + ']'
    print(ans)