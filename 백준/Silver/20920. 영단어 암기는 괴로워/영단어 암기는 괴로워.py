import sys
n, m = map(int,input().split())
d = {}
for _ in range(n):
    input = sys.stdin.readline().rstrip()
    if len(input) < m:
        continue
    if input not in d:
        d[input] = 1
    else:
        d[input]+=1
# 0: 나온 횟수, 1: 길이
d = dict(sorted(d.items(), key= lambda x:(-x[1],-len(x[0]),x[0])))

for i in d.keys():
    print(i)