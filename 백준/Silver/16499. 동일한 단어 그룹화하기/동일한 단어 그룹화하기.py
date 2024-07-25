import sys

n = int(sys.stdin.readline().rstrip())
s = set()
for i in range(n):
    word = sys.stdin.readline().rstrip()
    l = []
    for x in word:
        l.append(x)
    l.sort()
    tmp = ""
    for x in l:
        tmp += x
    s.add(tmp)
print(len(s))