import itertools
n = input()
l = []
for i in n:
    l.append(i)
result = []
num = list(itertools.permutations(l, len(n)))
for i in num:
    tmp = ""
    for j in i:
        tmp += j
    result.append(int(tmp))
ans = int(n)
result2 = []
for i in result:
    if i > ans:
        result2.append(i)
result2.sort()
if len(result2) == 0:
    print(0)
else:
    print(result2[0])