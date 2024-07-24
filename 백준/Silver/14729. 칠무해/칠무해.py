import sys
l = []
n = int(input())
for i in range(n):
    s = float(sys.stdin.readline())
    l.append(s)
l.sort()
for i in range(7):
    print("%.3f" %l[i])