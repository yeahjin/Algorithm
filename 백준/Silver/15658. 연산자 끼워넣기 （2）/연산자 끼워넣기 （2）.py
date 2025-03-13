import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int,input().split()))
op = list(map(int,input().split()))

max_num = int(-1e9)
min_num = int(1e9)

def dfs(d, t, plus, minus, multiply, divide):
    global max_num, min_num
    if d == n:
        max_num = max(t, max_num)
        min_num = min(t, min_num)
        return
    if plus > 0:
        dfs(d + 1 , t + num[d], plus - 1, minus, multiply, divide)
    if minus > 0:
        dfs(d+1, t - num[d], plus, minus - 1, multiply, divide)
    if multiply > 0:
        dfs(d+1, t * num[d], plus, minus, multiply - 1, divide)
    if divide > 0:
        dfs(d+1, int(t/num[d]), plus, minus, multiply, divide - 1)

dfs(1,num[0],op[0],op[1],op[2],op[3])
print(max_num)
print(min_num)