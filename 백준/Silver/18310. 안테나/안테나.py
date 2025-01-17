n = int(input())
l = list(map(int,input().split()))
l.sort()
if n % 2 == 0:
    mid = l[n//2 - 1]
else:
    mid = l[n//2]
print(mid)