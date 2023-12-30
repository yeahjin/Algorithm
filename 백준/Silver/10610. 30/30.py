n = input()
l = []
for i in n:
    l.append(int(i))
l = sorted(l, reverse=True)

if sum(l) % 3 ==0 and l[-1] == 0:
    tmp = ''
    for i in l:
        tmp += str(i)
    print(int(tmp))
else:
    print(-1)