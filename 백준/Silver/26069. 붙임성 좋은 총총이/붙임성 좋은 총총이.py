import sys
n = int(sys.stdin.readline().rstrip())
s = {"ChongChong"}

for i in range(n):
    a, b = map(str,sys.stdin.readline().split())
    if a in s:
        s.add(b)
    if b in s:
        s.add(a)

print(len(s))