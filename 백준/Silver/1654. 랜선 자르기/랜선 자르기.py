import sys
input = sys.stdin.readline

n, k = map(int,input().split())
l = []
for i in range(n):
    l.append(int(input()))

start = 1
end = max(l)
answer = 0
while start <= end:
    mid = (start+end) // 2
    total = 0
    for i in l:
        if mid <= i:
            total += i // mid
    if total >= k:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)