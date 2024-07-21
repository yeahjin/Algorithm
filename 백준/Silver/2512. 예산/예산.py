import sys

t = int(sys.stdin.readline().rstrip())
array = list(map(int,sys.stdin.readline().split()))
budget = int(sys.stdin.readline().rstrip())

start = 1
end = max(array)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    for x in array:
        if mid < x:
            total += mid
        else:
            total += x
    if total > budget:
        end = mid - 1
    else:
        start = mid + 1
        result = mid
print(result)