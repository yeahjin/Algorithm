def bracket(s):
    l = []
    for j in s:
        if j == "(":
            l.append(j)
        else:
            if len(l) == 0:
                return "NO"
            else:
                l.pop()
    if len(l) == 0:
        return "YES"
    else:
        return "NO"


n = int(input())
for i in range(n):
    s = input()
    print(bracket(s))