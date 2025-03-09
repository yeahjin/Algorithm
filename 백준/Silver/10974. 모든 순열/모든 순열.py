def r(d):
    global n
    if d == n:
        for i in s:
            print(i , end = " ")
        print()
        return
    for i in range(n):
        if v[i] == 0:
            v[i] = 1
            s[d] = i + 1
            r(d + 1)
            v[i] = 0


n = int(input())
a = [i for i in range(1, n + 1)]
v = [0] * n
s = [0] * n
r(0)