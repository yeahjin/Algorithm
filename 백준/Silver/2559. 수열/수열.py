import sys
n, d = map(int,input().split())

l = list(map(int,input().split()))

maxTmp = -1 * sys.maxsize
tmp = 0
start = 0
idx = 0
while True:
    if idx == start + d:
        maxTmp = max(maxTmp,tmp)
        tmp -= l[start]
        start += 1
    if idx == len(l):
        break
    tmp += l[idx]
    idx += 1
print(maxTmp)