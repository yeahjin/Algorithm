import sys
n = int(input())
d = set()
ans = 0
for i in range(n):
    s = sys.stdin.readline().rstrip()
    if s == "ENTER":
        ans += len(d)
        d = set()
        continue
    d.add(s)
ans += len(d)
print(ans)
