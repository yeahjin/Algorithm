import sys

n = int(input())
l = []
for i in range(n):
    number = sys.stdin.readline().rstrip()
    l.append(int(number))

stack = []
idx = 0
flag = False
ans = []
for i in range(1,n+1):
    stack.append(i)
    ans.append("+")
    while stack[-1] == l[idx]:
        ans.append("-")
        stack.pop()
        idx += 1
        if len(stack) == 0:
            break
        if idx >= len(l):
            break

if len(stack) != 0:
    print("NO")
else:
    for i in ans:
        print(i)