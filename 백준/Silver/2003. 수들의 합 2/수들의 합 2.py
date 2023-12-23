n, m = map(int,input().split())
l = list(map(int,input().split()))

start = 0
end = 0
sumNum = 0
ans = 0
while True:
    sumNum = sum(l[end:start+1])
    if sumNum > m:
        end += 1
    elif sumNum < m:
        start += 1
    if sumNum == m:
        start += 1
        ans += 1
    if start >= n:
        break
print(ans)