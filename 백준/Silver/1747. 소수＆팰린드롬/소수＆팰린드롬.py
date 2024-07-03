n = int(input())

l = [True] * 1500000
l[0] = l[1] = False
for i in range(2, 1500000):
    if l[i]:
        for j in range(i * 2, 1500000, i):
            if l[j]:
                l[j] = False

for i in range(n, 1500000):
    if l[i]:
        if str(i) == str(i)[::-1]:
            print(str(i))
            break
