import sys
input = sys.stdin.readline

def dfs(d, t, plus, minus, multi, divide):
    global n, max_num, min_num
    if n == d:
        max_num = max(max_num, t)
        min_num = min(min_num, t)
        return
    if plus > 0:
        dfs(d + 1, t + nums[d], plus - 1, minus, multi, divide)
    if minus > 0:
        dfs(d + 1, t - nums[d], plus, minus - 1, multi, divide)
    if multi > 0:
        dfs(d + 1, t * nums[d], plus, minus, multi - 1, divide)
    if divide > 0:
        dfs(d + 1, int(t/nums[d]), plus, minus, multi, divide - 1)


n = int(input())
nums = list(map(int,input().split()))
opera = list(map(int,input().split()))
max_num = int(-1e9)
min_num = int(1e9)
dfs(1,nums[0], opera[0], opera[1], opera[2], opera[3])
print(max_num)
print(min_num)