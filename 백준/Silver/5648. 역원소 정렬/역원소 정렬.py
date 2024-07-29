import sys
l = list(map(str,sys.stdin.read().split()))
l = l[1:]
for i in range(len(l)):
    l[i] = int(l[i][::-1])
l.sort()
for i in l:
    print(i)