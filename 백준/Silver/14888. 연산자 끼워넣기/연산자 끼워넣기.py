from itertools import permutations
import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
m = list(map(int,input().split())) # + - * /
l = []

for i in range(4):
    if i == 0:
        for j in range(m[i]):
            l.append("+")
    elif i == 1:
        for j in range(m[i]):
            l.append("-")
    elif i == 2:
        for j in range(m[i]):
            l.append("*")
    else:
        for j in range(m[i]):
            l.append("/")

c = list(permutations(l,n-1))

l2 = []
for i in c:
    tmp = a[0]
    for j in range(1,n):
        if i[j-1] == "+":
            tmp += a[j]
        elif i[j-1] == "*":
            tmp *= a[j]
        elif i[j-1] == "-":
            tmp -= a[j]
        else:
            tmp = int(tmp/a[j])
    l2.append(tmp)
print(max(l2))
print(min(l2))