import itertools
import sys
t = int(input())

for _ in range(t):
    t2 = int(input())
    l = []
    for i in range(t2):
        s = sys.stdin.readline().rstrip()
        l.append(s)
    l2 = list(itertools.permutations(l,2))
    tmp = ""
    l3 = []
    for s1, s2 in l2:
        tmp+=s1 + s2
        l3. append(tmp)
        tmp = ""
    ans = []
    for s1 in l3:
        if s1 == s1[::-1]:
            ans.append(s1)
            break

    if len(ans) == 0:
        print(0)
    else:
        for j in ans:
            print(j)