import sys

k, n = map(int,sys.stdin.readline().split())
array = []
for _ in range(k):
    array.append(int(sys.stdin.readline().rstrip()))

result = 0
start = 1
end = max(array)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for x in array:
        if x >= mid:
            total += x//mid

    if total < n:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)