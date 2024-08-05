from itertools import permutations
import sys

n = int(input())
k = int(input())
l = []
for i in range(n):
    l.append(sys.stdin.readline().rstrip())
l2 = list(permutations(l,k))
s = set()
for i in l2:
    tmp = ""
    for j in i:
        tmp += j
    s.add(tmp)
print(len(s))