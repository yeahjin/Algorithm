import sys
input = sys.stdin.readline

def r(t):
    global cnt
    if t <= 0:
        if t == 0:
            cnt += 1
        return
    r(t-1)
    r(t-2)
    r(t-3)


l = []
n = int(input())
for i in range(n):
    num = int(input())
    cnt =0
    r(num)
    print(cnt)