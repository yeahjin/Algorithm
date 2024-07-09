import sys
n = int(input())
d = {}
for i in range(n):
    a = sys.stdin.readline().rstrip()
    if a not in d:
        d[a] = 1
    else:
        d[a] += 1
d = dict(sorted(d.items(), key=lambda x:x[0]))
d = sorted(d.items(), key=lambda x:x[1],reverse=True)

print(d[0][0])