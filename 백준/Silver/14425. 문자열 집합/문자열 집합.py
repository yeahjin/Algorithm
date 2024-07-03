import sys

m, s = map(int,input().split())

d = set()

for i in range(m):
    string = sys.stdin.readline().rstrip()
    d.add(string)

cnt = 0
for i in range(s):
    string = sys.stdin.readline().rstrip()
    if string in d:
        cnt += 1

print(cnt)