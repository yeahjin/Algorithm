import sys
n = map(int, sys.stdin.readline())
l = list(map(int,sys.stdin.readline().split()))
dict = {}
for i in l:
    dict[i] = 1
n2 = map(int,sys.stdin.readline())
l2 = list(map(int,sys.stdin.readline().split()))

for i in l2:
    if i in dict:
        print(1)
    else:
        print(0)