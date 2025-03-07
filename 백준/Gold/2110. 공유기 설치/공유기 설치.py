import sys

input = sys.stdin.readline

n, c = map(int,input().split())
l = []
for i in range(n):
    l.append(int(input()))

l.sort()

start = 1
end = l[-1] - l[0]
answer = 0
while start <= end:
    mid = (start + end) // 2
    total = 1
    tmp = l[0]
    for i in l[1:]:
        if i - tmp >= mid:
            tmp = i
            total += 1
    if total < c:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(answer)