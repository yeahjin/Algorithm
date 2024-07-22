import sys

n, m = map(int,sys.stdin.readline().split())
array = []
for _ in range(n):
    s = int(sys.stdin.readline().rstrip())
    array.append(s)

start = max(array)
end = sum(array)

result = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    hand = 0
    for x in array:
        if x > hand:
            cnt += 1
            hand = mid - x
        else:
            hand = hand - x
    if cnt <= m:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)