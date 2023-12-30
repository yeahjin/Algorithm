import sys
input = sys.stdin.readline

n = int(input())
d = {}
for i in range(n):
    a, b = map(str,input().split())
    d[a] = b

l = []
for name, stat in d.items():
    if stat == 'enter':
        l.append(name)
l = sorted(l, reverse=True)

print(*l)