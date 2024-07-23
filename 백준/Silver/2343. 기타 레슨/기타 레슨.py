import sys
n, m = map(int,sys.stdin.readline().split())
array = list(map(int,sys.stdin.readline().split()))

start = max(array)
end = sum(array)
result = []

while start <= end:
    mid = (start + end) //2
    tmp = 0 # 합하는 용도
    cnt = 1
    for x in array:
        tmp += x
        if tmp > mid:
            cnt += 1
            tmp = x
    if cnt > m:
        start = mid + 1
    else:
        end = mid -1
        result.append(mid)

print(min(result))