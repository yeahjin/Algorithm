t = int(input())
l = []
for _ in range(t):
    l.append(list(map(int,input().split())))
cnt = 0
for hund in range(1,10):
    for ten in range(1,10):
        for one in range(1,10):
            if hund == ten or ten == one or hund == one:
                continue
            num = str(hund) + str(ten) + str(one)
            result = 0
            for x,y,z in l:
                num2 = str(x)
                strike = 0
                ball = 0
                if num2[0] == num[0]:
                    strike += 1
                if num2[1] == num[1]:
                    strike += 1
                if num2[2] == num[2]:
                    strike += 1

                if num2[0] == num[1]:
                    ball += 1
                if num2[0] == num[2]:
                    ball += 1
                if num2[1] == num[2]:
                    ball += 1
                if num2[1] == num[0]:
                    ball += 1
                if num2[2] == num[0]:
                    ball += 1
                if num2[2] == num[1]:
                    ball += 1
                if ball == z and strike == y:
                    result += 1
            if result == t:
                cnt += 1

print(cnt)
